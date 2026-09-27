#!/usr/bin/env python3
"""L'application « En route vers Compostelle » — l'espagnol du pèlerin, sur téléphone.

    python3 build/compostelle_app.py     # → modules-autonomes/compostelle/index.html

Produite, jamais écrite à la main. Elle lit build/contenu/compostelle/ :
`lexique.py`, `etapes.py`, `personnages.py`, `poche.py` ; et la liste des sons
de build/compostelle_commun.py (la même que celle du générateur de voix).

CE QUI Y EST
- L'accueil : la credencial (dix cases, un tampon par journée réussie), la
  frise du chemin, et la prochaine journée.
- Dix journées, sept temps chacune (voir etapes.py) : le lieu, les mots,
  j'entends, on me répond, je le dis, la scène, le soir avec Marta.
- La poche : les phrases du chemin par situation, les urgences, le bouton
  « Montrer » (la phrase en grand, à tendre à quelqu'un), et « Préparer pour
  le chemin », qui met tous les sons et les images dans le téléphone.
- Les mots (onze planches), les faux amis, la Compostela à la fin.

TÉLÉPHONE D'ABORD : une colonne, des boutons de 48 px, rien qui déborde à
375 px. Hors ligne : le service worker du site (/sw.js) garde les pages
(réseau d'abord) et les médias (cache d'abord) ; « Préparer pour le chemin »
ne fait que les demander tous une fois.

RIEN NE PART : l'état (pèlerin ou pèlerine, tampons, choix faits) vit dans le
localStorage du téléphone. Le prénom de la Compostela ne quitte jamais
l'appareil. La reconnaissance vocale est celle du navigateur.

LE THÈME : francis, avec le jaune de la flèche réservé à la progression
(tampons, frise) — décision du plan, 25 sept. 2026.
"""
import json, pathlib, sys

RACINE = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RACINE / "build"))
import compostelle_commun as C  # noqa: E402

SORTIE = RACINE / "modules-autonomes" / "compostelle" / "index.html"
MEDIA = RACINE / "assets" / "interactive" / "compostelle"
# La conversation libre avec l'assistant (build/contenu/compostelle/jeu_de_role.py)
# passe par /api/jeu-de-role, qui charge le scénario « camino-es-fr » depuis le
# 26 sept. 2026 (Daniel : « d'accord pour le groupe Pilote Compostelle, branche
# le jeu de rôle »). L'accès : un code d'élève du groupe « Pilote Compostelle ».
# Remettre False retire le temps sans toucher au serveur.
JEU_LIBRE = True
MEDIA_V = "6"  # 6 : révision 4 ; 5 : 5 : révision 3 (allergie à Pamplona, variantes de León, test) ; 4 : 4 : allergie choisie dans la scène de León et le test ; 2 : sons à 48 kbit/s (27 → 9 Mo) ; 3 : 25 répliques corrigées après relecture, 25 sept. 2026


def verifier(ET):
    """Ce qui ne lève aucune erreur à l'écran et casse pourtant l'exercice."""
    ecarts = []
    for et in ET.ETAPES:
        for k, tour in enumerate(et["scene"]["tours"] + et["soir"]["tours"]):
            if "choix" not in tour:
                continue
            ch = tour["choix"]
            if not tour.get("libre"):
                assert ch[0][2] is None and all(c[2] for c in ch[1:]), f"{et['id']}/{k} : la bonne d'abord, une rétroaction par mauvaise"
                b = len(ch[0][0])
                for c in ch[1:]:
                    if abs(len(c[0]) - b) / b > 0.45:
                        ecarts.append(f"{et['id']}/{k} longueurs : « {ch[0][0]} » / « {c[0]} »")
        for es, choix in et["ecoute"]:
            assert choix[0][1] is None and all(c[1] for c in choix[1:]), f"{et['id']} écoute : {es}"
        for m in et["mots"]:
            assert m == "@alergia" or m in MOTS_IDS, f"{et['id']} : mot inconnu {m}"
    return ecarts


def donnees():
    LX, ET, PS, PO, TS = (C.charger("lexique"), C.charger("etapes"), C.charger("personnages"),
                          C.charger("poche"), C.charger("test"))
    TS.verifier()
    LX.verifier()
    PR = C.charger("preparation")
    CF = C.charger("confidentialite"); CF.verifier()
    # Les leçons narrées (build/compostelle_lecons.py) : seulement celles qui ont leur son.
    LE = C.charger("lecons").LECONS
    temps_l = json.loads((C.CONTENU / "lecons_temps.json").read_text()) if (C.CONTENU / "lecons_temps.json").exists() else {}
    lecons = {sid: {"segs": [list(x) for x in segs], "debuts": temps_l[sid]["debuts"], "duree": temps_l[sid]["duree"]}
              for sid, segs in LE.items()
              if sid in temps_l and len(temps_l[sid]["debuts"]) == len(segs) and (C.SONS / "prep" / sid / "lecon.mp3").exists()}
    PR.verifier({e[0] for e in LX.LEXIQUE}, PS.PERSONNAGES)
    global MOTS_IDS
    MOTS_IDS = {e[0] for e in LX.LEXIQUE}
    for e in verifier(ET):
        print("  à regarder :", e)
    sons = sorted(x["fichier"] for x in C.extraits() if (C.SONS / x["fichier"]).exists())
    sons = sorted(sons + [f"prep/{sid}/lecon.mp3" for sid in lecons])
    tous = [x["fichier"] for x in C.extraits()]
    manque = len(tous) - len(sons)
    mots = {}
    for i, pl, es, fr, dessin, note in LX.LEXIQUE:
        img = ""
        if dessin == "croquis" and (MEDIA / "croquis" / f"{i}.jpg").exists():
            img = "croquis"
        elif dessin.startswith("picto:"):
            img = dessin
        mots[i] = {"p": pl, "es": es, "fr": fr, "img": img, "note": note}
    pieges = [{"id": i, "es": t[0], "bonne": t[1], "fausse": t[2], "seconde": t[3], "expl": t[4]}
              for i, t in LX.PIEGES.items()]
    perso = {k: {"nom": v[0], "qui": v[1], "ou": v[2], "g": v[3],
                 "portrait": bool(v[6]) and (MEDIA / "portraits" / f"{v[6]}.jpg").exists()}
             for k, v in PS.PERSONNAGES.items()}
    # La poche : on regroupe, on ne réécrit rien.
    par_etape = {et["id"]: et for et in ET.ETAPES}
    poche = []
    # Audit tour 2 (C2) : les phrases sur soi avaient échoué sous « À la
    # pharmacie ». Elles ont leur rubrique.
    moi = [{"es": d[1], "fr": d[3].get("trad", d[0]), "son": f"{et['id']}/dire-{n}", "var": d[3].get("var", "")}
           for et in ET.ETAPES for n, d in enumerate(et["dire"]) if len(d) > 3 and d[3].get("perso")]
    for cle, titre, source in PO.RUBRIQUES:
        if cle == "pelerins":
            poche.append({"cle": "moi", "titre": "Me présenter", "items": moi})
        items = []
        if source == "urgences":
            items = [{"es": es, "fr": fr, "son": f"poche/{i}"} for i, es, fr in PO.URGENCES]
        elif source.startswith("etape:"):
            et = par_etape[source[6:]]
            items = [{"es": d[1], "fr": d[0].split(" (")[0] if "{alg" in d[0] else d[0], "son": f"{et['id']}/dire-{n}"}
                     for n, d in enumerate(et["dire"]) if not (len(d) > 3 and d[3].get("perso"))]
            # Audit tour 1 (F2) : la poche ne donnait que ce qu'on DIT. Ce qu'on
            # risque d'ENTENDRE en retour est l'autre moitié de l'écart.
            poche.append({"cle": cle, "titre": titre, "items": items,
                          "reponses": [{"es": es, "fr": ch[0][0], "son": f"{et['id']}/ecoute-{n}"}
                                       for n, (es, ch) in enumerate(et["ecoute"])]})
            continue
        elif source.startswith("planche:"):
            items = [{"es": e[2], "fr": e[3], "son": f"mots/{e[0]}"} for e in LX.LEXIQUE if e[1] == source[8:]]
        poche.append({"cle": cle, "titre": titre, "items": items})
    etapes = []
    for et in ET.ETAPES:
        e = dict(et)
        e["vignette"] = (MEDIA / "etapes" / f"{et['img']}.jpg").exists()
        etapes.append(e)
    poids = sum((C.SONS / f).stat().st_size for f in sons) + sum(
        f.stat().st_size for d in ("croquis", "portraits", "etapes") for f in (MEDIA / d).glob("*.jpg") if ".orig" not in f.name)
    alergenos = [{"code": c, "fr": fr, "sans": sans, "phrase": PO.phrase_alergia(c), "formes": PO.formes(c)}
                 for c, _a, sans, fr in PO.ALERGENOS]
    return {"v": MEDIA_V, "jeuLibre": JEU_LIBRE, "alergenos": alergenos,
            "test": {"formes": TS.FORMES, "objectifs": TS.OBJECTIFS, "seuil": TS.SEUIL},
            "prep": {"seances": PR.SEANCES, "test": PR.TEST, "objectifs": PR.OBJECTIFS, "seuil": PR.SEUIL, "conseils": PR.CONSEILS,
                     "fin": PR.FIN, "halte": PR.HALTE, "lecons": lecons},
            "confid": {"responsable": CF.RESPONSABLE, "courriel": CF.COURRIEL, "maj": CF.MISE_A_JOUR, "bref": CF.EN_BREF,
                       "donnees": CF.DONNEES, "hors": CF.HORS_QUEBEC, "nefait": CF.NE_FAIT_PAS},
            "poids": round(poids / 1e6), "planches": LX.PLANCHES, "mots": mots, "pieges": pieges, "perso": perso,
            "etapes": etapes, "poche": poche, "sons": sons}, manque, len(tous)


def icones():
    """L'icône de l'écran d'accueil : la coquille du lexique, sur blanc (any) et
    sur le sable de la credencial (maskable, la coquille dans la zone sûre)."""
    from PIL import Image
    src = MEDIA / "croquis" / "concha.png"
    src = src if src.exists() else MEDIA / "croquis" / "concha.jpg"
    coq = Image.open(src).convert("RGB")
    dest = SORTIE.parent / "icones"; dest.mkdir(parents=True, exist_ok=True)
    for nom, cote, fond, part in (("icone-192.png", 192, "#FFFFFF", .86), ("icone-512.png", 512, "#FFFFFF", .86),
                                  ("icone-maskable-512.png", 512, "#FBF6E9", .62), ("icone-180.png", 180, "#FFFFFF", .86)):
        im = Image.new("RGB", (cote, cote), fond)
        c = coq.resize((round(cote * part),) * 2, Image.LANCZOS)
        if fond != "#FFFFFF":   # le blanc du croquis devient le sable du fond
            import numpy as np
            a = np.asarray(c).copy(); a[(a >= 245).all(axis=2)] = (0xFB, 0xF6, 0xE9); c = Image.fromarray(a)
        im.paste(c, ((cote - c.width) // 2, (cote - c.height) // 2))
        im.save(dest / nom, optimize=True)
    base = "/modules-autonomes/compostelle/"
    (SORTIE.parent / "manifest.webmanifest").write_text(json.dumps({
        "name": "En route vers Compostelle — francis",
        "short_name": "Compostelle",
        "description": "L'espagnol du pèlerin, étape par étape sur le Camino francés.",
        "lang": "fr-CA", "dir": "ltr", "start_url": base, "scope": base,
        "display": "standalone", "orientation": "portrait",
        "background_color": "#F3ECDD", "theme_color": "#FFFFFF",
        "icons": [{"src": base + "icones/icone-192.png", "sizes": "192x192", "type": "image/png", "purpose": "any"},
                  {"src": base + "icones/icone-512.png", "sizes": "512x512", "type": "image/png", "purpose": "any"},
                  {"src": base + "icones/icone-maskable-512.png", "sizes": "512x512", "type": "image/png", "purpose": "maskable"}],
    }, ensure_ascii=False, indent=2), encoding="utf-8")


def main():
    icones()
    D, manque, total = donnees()
    page = GABARIT.replace("%%DONNEES%%", json.dumps(D, ensure_ascii=False, separators=(",", ":")))
    SORTIE.parent.mkdir(parents=True, exist_ok=True)
    SORTIE.write_text(page, encoding="utf-8")
    print(f"{SORTIE.relative_to(RACINE)}  {len(page)//1024} Ko — sons {total - manque}/{total}")


GABARIT = r"""<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>En route vers Compostelle</title>
<meta name="description" content="L'espagnol du pèlerin francophone, étape par étape sur le Camino francés.">
<link rel="stylesheet" href="/assets/design-system/styles.css">
<link rel="stylesheet" href="/assets/design-system/marque-francis.css">
<link rel="icon" href="/assets/design-system/marque-francis-favicon.svg">
<link rel="manifest" href="/modules-autonomes/compostelle/manifest.webmanifest">
<link rel="apple-touch-icon" href="/modules-autonomes/compostelle/icones/icone-180.png">
<meta name="apple-mobile-web-app-title" content="Compostelle">
<meta name="theme-color" content="#FFFFFF">
<style>
/* Page produite par build/compostelle_app.py — ne pas l'éditer. */
:root{--fleche:#F2C230;--fleche-ink:#5C4400;--fleche-bg:#FFF6D6;
  --encre-1:#9B2C2C;--encre-2:#1D4E89;--encre-3:#1F6F5C;--encre-4:#7A4B1E}
/* Habit « La flèche et la borne » (variation B, choisie par Daniel le 26 sept. 2026,
   avec les tampons rouges de la variation A) : la flèche jaune est l'action, le bleu
   de la borne galicienne encadre, l'encre des tampons est le rouge de Santiago.
   Voir assets/presentations/compostelle-variations.html. */
/* Fond beige « credencial » (26 sept. 2026 : Daniel préfère le beige au gris-bleu ; le bleu reste aux bornes). */
:root{--surface-page:#F3ECDD;--accent:#F2C230;--accent-ink:#13233B;--accent-soft:#E3EBF7;
  --text-accent:#1F4E9C;--text-strong:#13233B;--text-body:#22324A;--text-muted:#5B6979;
  --audio:#1F4E9C;--borne:#1F4E9C;--borne-bg:#E3EBF7;--borne-trait:#AFBFD3;--tampon:#9B2C2C}
*{box-sizing:border-box}
[hidden]{display:none!important}
html{-webkit-text-size-adjust:100%}
body{margin:0;background:var(--surface-page,#F7F7F5);color:var(--text-body,#2B2D31);
  font-family:Nunito,system-ui,sans-serif;font-size:17px;line-height:1.5}
.fr-barre .fr-barre__in{max-width:760px;padding-left:16px;padding-right:16px}
.secteur{display:flex;flex-direction:column;align-items:flex-end;text-align:right;line-height:1.15}
.secteur small{font-size:11px;font-weight:800;letter-spacing:.08em;text-transform:uppercase;color:var(--text-muted)}
.secteur b{font-size:17px;font-weight:900;color:var(--text-accent)}
@media (max-width:480px){.secteur small{display:none}.secteur b{font-size:15px}}
main{max-width:760px;margin:0 auto;padding:14px 16px 90px}
h1{font-size:28px;line-height:1.15;margin:6px 0 6px;color:var(--text-strong)}
h2{font-size:21px;line-height:1.2;margin:22px 0 10px;color:var(--text-strong)}
h3{font-size:17px;margin:16px 0 6px;color:var(--text-strong)}
p{margin:0 0 10px}
.muted{color:var(--text-muted)}
.surtitre{font-size:13px;font-weight:800;letter-spacing:.08em;text-transform:uppercase;color:var(--text-muted);margin:0}
button{font:inherit}
.btn{font-weight:800;font-size:16px;cursor:pointer;border-radius:12px;padding:10px 16px;min-height:48px;
  border:1px solid var(--line-300,#D6D6D2);background:var(--surface-card,#fff);color:var(--text-strong);
  display:inline-flex;gap:8px;align-items:center;justify-content:center;text-decoration:none}
.btn:active{transform:translateY(1px)}
.btn--pri{background:var(--accent);border-color:var(--accent);color:var(--accent-ink)}
.btn--large{width:100%}
.btn--son{background:var(--audio);border-color:var(--audio);color:#fff;min-width:48px;padding:10px 12px}
.btn--petit{min-height:44px;padding:6px 12px;font-size:14.5px}
.btn svg{width:20px;height:20px;flex:none}
.btn[disabled]{opacity:.45;cursor:not-allowed}
.rangee{display:flex;flex-wrap:wrap;gap:10px;align-items:center}
.carte{background:var(--surface-card,#fff);border:1px solid var(--line-200,#E8E8E4);border-radius:16px;padding:16px}
.retour{display:inline-flex;align-items:center;gap:6px;font-weight:800;font-size:15px;color:var(--text-muted);
  background:none;border:0;padding:8px 0;cursor:pointer;min-height:44px}
.retour svg{width:18px;height:18px}

/* Accueil */
.heros{position:relative;border-radius:18px;overflow:hidden;background:#fff;border:1px solid var(--line-200)}
.heros img{display:block;width:100%;aspect-ratio:3/2;object-fit:cover}
.heros .txt{padding:14px 16px 16px}
.cred{display:grid;grid-template-columns:repeat(5,minmax(0,1fr));gap:6px 6px;background:#FBF6E9;border:1px solid #E2D6BA;
  border-radius:14px;padding:10px 8px}
.case-w{display:flex;flex-direction:column;align-items:center;gap:3px;min-width:0}
.case-w small{font-size:9.5px;letter-spacing:-.2px;font-weight:800;color:var(--text-muted);line-height:1.1;text-align:center;max-width:100%;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.case{width:100%;aspect-ratio:1/1;border:1.5px dashed #CDBF9C;border-radius:10px;display:flex;align-items:center;
  justify-content:center;cursor:pointer;background:transparent;padding:2px;color:var(--text-muted)}
.case span{font-size:20px;font-weight:900}
.case.faite{border-style:solid;border-color:transparent;background:transparent}
.case svg.tampon{width:100%;height:100%}
svg.tampon{opacity:.9}
#app a{color:var(--text-accent)}
.carte-prep{display:flex;flex-direction:column;gap:3px;width:100%;text-align:left;cursor:pointer;background:#fff;border:1px solid var(--borne-trait);
  border-left:5px solid var(--accent);border-radius:14px;padding:12px 14px;margin-bottom:12px;font:inherit;color:var(--text-body)}
.carte-prep b{font-size:17px;color:var(--text-strong)}
.carte-prep .muted{font-size:14px}
.pied{max-width:720px;margin:24px auto 0;padding:14px 16px 28px;text-align:center;font-size:13.5px;color:var(--text-muted)}
.pied a{color:var(--text-muted)}
.a-remplir{background:#FDF0CF;color:#7A4A00;border:1px dashed #D9A43A;border-radius:6px;padding:0 6px;font-weight:800}
.cf-bref ul{margin:0;padding-left:20px}.cf-bref li{margin:6px 0}
.cf-ligne dl{display:grid;grid-template-columns:auto 1fr;gap:4px 12px;margin:8px 0 0;font-size:15px}
.cf-ligne dt{color:var(--text-muted);font-weight:700}.cf-ligne dd{margin:0}
.cf-hors{margin:6px 0}
.avis-fond{position:fixed;inset:0;background:rgba(19,35,59,.55);display:grid;place-items:center;padding:16px;z-index:50}
.avis-micro{background:#fff;border-radius:16px;padding:18px;max-width:440px;width:100%;box-shadow:0 16px 40px rgba(0,0,0,.3)}
.avis-micro h3{margin:0 0 8px}.avis-micro p{margin:0 0 10px;font-size:15.5px}
.avis-micro .rangee{display:flex;gap:8px;flex-wrap:wrap}
@media (max-width:420px){.cf-ligne dl{grid-template-columns:1fr}.cf-ligne dt{margin-top:4px}}
/* accueil en deux temps : le sac, puis le chemin */
.deux-temps{list-style:none;padding:0;margin:4px 0 10px;display:grid;grid-template-columns:1fr 1fr;gap:8px}
.deux-temps a{display:flex;flex-direction:column;gap:2px;text-decoration:none;color:var(--text-muted);background:#fff;border:1px solid var(--line-200);border-radius:12px;padding:10px 12px 10px 48px;position:relative;min-height:60px}
.deux-temps span{position:absolute;left:12px;top:50%;transform:translateY(-50%);width:28px;height:28px;border-radius:50%;display:grid;place-items:center;font-weight:900;background:var(--line-200);color:var(--text-muted)}
.deux-temps b{font-size:15px;line-height:1.2;color:inherit}.deux-temps small{font-size:12.5px}
.deux-temps .actif a{border-color:var(--borne);color:var(--borne);box-shadow:inset 0 0 0 1px var(--borne)}
.deux-temps .actif span{background:var(--borne);color:#fff}
.deux-temps .fait span{background:#2E7D4F;color:#fff}
.acc-temps{background:#FBF7EE;border:1px solid #E2D8C3;border-radius:18px;padding:16px;margin:14px 0}
.acc-temps--fait{padding-bottom:12px}
.acc-h{margin:2px 0 6px;font-size:26px;line-height:1.15}
.acc-p{margin:0 0 12px;font-size:16px}
.acc-temps .btn--large{white-space:normal;line-height:1.25}
.acc-note{font-size:14px;margin:8px 0 0;text-align:center}
.sac{display:grid;grid-template-columns:120px 1fr;gap:12px;align-items:start;margin:0 0 14px}
.sac-dos{text-align:center;position:sticky;top:8px}
.sac-dos img{width:100%;max-width:120px;display:block;margin:0 auto;mix-blend-mode:multiply}
.sac-dos b{display:block;font-size:24px;color:var(--borne);line-height:1}.sac-dos small{font-size:13px;color:var(--text-muted)}
.sac-objets{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:8px}
.sac-o{display:grid;grid-template-columns:52px 1fr;grid-template-rows:auto auto;column-gap:10px;align-items:center;text-align:left;background:#fff;
  border:1.5px dashed #CDBF9F;border-radius:12px;padding:6px 8px;font:inherit;color:inherit;cursor:pointer;position:relative;min-height:64px}
.sac-o .sac-img{grid-row:1/3;position:relative;width:52px;height:52px}
.sac-o img{width:52px;height:52px;object-fit:contain;filter:grayscale(1);opacity:.35;mix-blend-mode:multiply}
.sac-o b{font-size:13.5px;line-height:1.2;color:var(--text)}.sac-o small{font-size:12px;color:var(--text-muted);line-height:1.25}
.sac-n{position:absolute;top:-7px;left:-7px;width:22px;height:22px;border-radius:50%;background:#fff;border:1.5px solid #CDBF9F;font-size:12px;font-weight:900;display:grid;place-items:center;color:var(--text-muted)}
.sac-o.dans{border-style:solid;border-color:#B9D8C4;background:#F3FAF5}
.sac-o.dans img{filter:none;opacity:1}
.sac-o.dans .sac-n{background:#2E7D4F;border-color:#2E7D4F;color:#fff}
.sac-img i{position:absolute;right:-4px;bottom:-2px;width:20px;height:20px;border-radius:50%;background:#2E7D4F;color:#fff;font-style:normal;font-size:12px;font-weight:900;display:grid;place-items:center}
.sac-o.courant{border:2px solid var(--accent);background:#FFF9E6}
.sac-o.courant .sac-n{background:var(--accent);border-color:var(--accent);color:var(--accent-ink)}
.sac--petit .sac-o small{display:block}
@media (max-width:520px){.sac{grid-template-columns:1fr}.sac-dos{position:static;display:flex;align-items:center;gap:10px;justify-content:center}
  .sac-dos img{width:64px;margin:0}.sac-objets{grid-template-columns:1fr;gap:7px}
  .sac-o{grid-template-columns:44px 1fr;min-height:54px;padding:5px 10px}.sac-o .sac-img,.sac-o img{width:44px;height:44px}
  .sac-o b{font-size:14.5px}.sac-o small{font-size:12.5px}}
.livret{background:#FFFDF6;border:1px solid #D9C9A3;border-radius:6px 14px 14px 6px;padding:12px 12px 14px;margin-top:10px;
  box-shadow:inset 6px 0 0 #E9DFC6, 0 2px 0 #E9DFC6, 0 4px 0 #D9C9A3}
.livret-tete{display:flex;align-items:center;gap:10px;border-bottom:1.5px solid #D9C9A3;padding:0 0 8px 6px;margin-bottom:8px}
.livret-tete img{width:40px;height:40px;object-fit:contain;mix-blend-mode:multiply}
.livret-tete>div{min-width:0}
.livret-tete div small{display:block;font-family:Newsreader,Georgia,serif;font-style:italic;font-size:12px;letter-spacing:.05em;color:var(--tampon);text-transform:uppercase}
.livret-tete b{font-size:19px;color:var(--text)}
.livret-compte{flex:none;white-space:nowrap;margin-left:auto;text-align:right;font-weight:900;font-size:20px;color:var(--tampon);line-height:1}
.livret-tete .livret-compte small{display:block;font-family:inherit;font-style:normal;text-transform:none;letter-spacing:0;font-size:12px;font-weight:700;color:var(--text-muted)}
.livret-leg{font-size:14px;margin:0 0 10px 6px;color:var(--text-muted)}
.livret .cred{background:none;border:0;padding:0 0 0 6px;box-shadow:none}
.case{flex-direction:column}
.case em{display:block;font-style:normal;font-size:10.5px;letter-spacing:.08em;text-transform:uppercase;color:#B5A47E;margin-top:2px;font-weight:800}
.case.courante em{color:var(--accent-ink)}
.l-lecteur{display:flex;align-items:center;gap:14px;flex-wrap:wrap}
.l-jouer{display:inline-flex;align-items:center;gap:8px;min-height:48px}
.l-barre{flex:1;min-width:120px;height:8px;border-radius:99px;background:var(--line-200);overflow:hidden}
.l-barre span{display:block;height:100%;width:0;background:var(--borne);transition:width .25s linear}
.l-temps{font-size:14px;font-variant-numeric:tabular-nums}
.l-texte{margin-top:12px}
.l-seg{margin:0 0 8px;padding:4px 8px;border-radius:8px;line-height:1.5;transition:background .2s;cursor:default}
.l-es{font-weight:800;color:var(--borne);padding-left:14px;border-left:3px solid var(--accent)}
.l-seg.actif{background:#FBF1CF}
.lien-btn{background:none;border:0;padding:0;font:inherit;color:var(--borne);text-decoration:underline;cursor:pointer}
.meca{background:#fff;border:1px solid var(--line-200);border-left:4px solid var(--borne);border-radius:12px;padding:10px 14px;margin:10px 0 14px}
.meca ul{margin:6px 0 0;padding-left:18px}.meca li{margin:5px 0;font-size:15.5px;line-height:1.5}
.liste-ecoute{padding:4px 0}
.liste-ecoute .ph:first-child{border-top:0}
.carte-borne{display:grid;grid-template-columns:128px minmax(0,1fr);gap:16px;align-items:center;background:#FBF6E9;border:1px solid #E2D6BA;
  border-radius:18px;padding:14px 16px 14px 10px;margin-bottom:14px}
.carte-borne h1{margin:2px 0 4px}
.carte-borne .muted{margin:0}
.cb-reste{margin:10px 0 0;font-size:16px;color:var(--text-strong)}
.cb-reste b{color:var(--borne)}
.cb-reste span,.bande-borne span{font-size:14px;color:var(--text-muted)}
.borne-img{position:relative;width:100%;line-height:0}
.borne-img img{width:100%;height:auto;mix-blend-mode:multiply}
.borne-img .plaque{position:absolute;left:56%;top:72%;transform:translate(-50%,-50%);background:#5E594F;color:#F3ECDD;
  font:900 15px/1 Nunito,system-ui,sans-serif;padding:5px 7px;border-radius:3px;white-space:nowrap;box-shadow:inset 0 0 0 1.5px #3D3931;letter-spacing:.02em}
.borne-img.petite{width:58px;flex:none}
.borne-img.petite .plaque{font-size:8.5px;padding:2px 3px}
.bande-borne{display:flex;gap:12px;align-items:center;background:#FBF6E9;border:1px solid #E2D6BA;border-radius:14px;padding:8px 14px 8px 8px;margin:10px 0}
.bande-borne p{margin:0;font-size:15.5px;color:var(--text-strong)}
.bande-borne b{color:var(--borne)}
@media (max-width:380px){.carte-borne{grid-template-columns:104px minmax(0,1fr);gap:12px}.borne-img .plaque{font-size:13px}}
.code-achat{font-size:34px;font-weight:900;letter-spacing:.18em;text-align:center;background:#fff;border:2px dashed var(--tampon);color:var(--tampon);border-radius:14px;padding:14px;margin:12px 0}
.lien-guide{margin-top:10px;background:transparent;border-color:var(--borne-trait);color:var(--text-accent)}
.g-phase{background:#fff;border:1px solid var(--line-200);border-left:4px solid var(--borne);border-radius:12px;padding:10px 14px;margin:8px 0}
.g-phase .surtitre span{text-transform:none;letter-spacing:0;font-weight:700}
.g-phase ol{margin:6px 0 0;padding-left:22px}.g-phase li{margin:4px 0;font-size:15.5px}
.g-tamp{display:inline-block;font-size:12px;font-weight:900;color:var(--tampon);border:1.5px solid var(--tampon);border-radius:99px;padding:0 7px;line-height:1.5}
.g-jours{padding-left:0;list-style:none;margin:8px 0}.g-jours li{background:#fff;border:1px solid var(--line-200);border-radius:12px;padding:9px 12px;margin:6px 0;font-size:15px}
.g-liste{padding-left:20px}.g-liste li{margin:6px 0;font-size:15.5px}
.case.courante{border-color:var(--accent);border-style:solid;box-shadow:inset 0 0 0 2px var(--accent);background:var(--fleche-bg);color:var(--accent-ink)}
.outils{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:10px}
.outil{display:flex;gap:10px;align-items:center;text-align:left;cursor:pointer;background:#fff;border:1px solid var(--line-200);
  border-radius:14px;padding:12px;min-height:64px;border-left:4px solid var(--borne)}
.outil svg{width:26px;height:26px;flex:none;color:var(--text-accent)}
.outil b{display:block;font-size:15.5px;color:var(--text-strong)}
.outil span{font-size:13px;color:var(--text-muted);line-height:1.3;display:block}
.frise{width:100%;height:auto;display:block}
.frise .ligne{stroke:var(--borne-trait);stroke-width:3;stroke-dasharray:1 7;stroke-linecap:round}
.frise .ok{fill:var(--borne);stroke:var(--accent-ink);stroke-width:1.5}
.frise .ko{fill:#fff;stroke:var(--borne-trait);stroke-width:1.5}
.frise text{font:700 11px Nunito,system-ui,sans-serif;fill:var(--text-muted);text-anchor:middle}

/* Journée */
.bandeau{border-radius:16px;overflow:hidden;position:relative;background:#fff;border:1px solid var(--line-200)}
.bandeau img{width:100%;display:block;aspect-ratio:3/2;object-fit:cover}
.etapes-j{list-style:none;padding:0;margin:14px 0 0;display:flex;flex-direction:column;gap:8px}
.etapes-j button{width:100%;display:flex;align-items:center;gap:12px;text-align:left;background:#fff;border:1px solid var(--line-200);
  border-radius:14px;padding:12px 14px;cursor:pointer;min-height:60px}
.etapes-j .num{width:32px;height:32px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-weight:900;
  background:var(--surface-sunken,#FBFBFA);border:1px solid var(--line-200);flex:none;font-size:14px}
.etapes-j .fait .num{background:var(--ok-bg);border-color:var(--ok-line);color:var(--ok-ink)}
.etapes-j b{display:block;color:var(--text-strong)}
.etapes-j span.d{font-size:13.5px;color:var(--text-muted);display:block;line-height:1.3}
.etat{margin-left:auto;font-size:12.5px;font-weight:800;color:var(--ok-ink);white-space:nowrap}

/* Mots */
.grille{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:10px}
@media (min-width:600px){.grille{grid-template-columns:repeat(3,minmax(0,1fr))}}
.mot{background:#fff;border:1px solid var(--line-200);border-radius:14px;padding:8px;display:flex;flex-direction:column;gap:6px;
  cursor:pointer;text-align:left;min-width:0}
.mot .img{aspect-ratio:1/1;border-radius:10px;background:#fff;display:flex;align-items:center;justify-content:center;overflow:hidden}
.mot .img img{width:100%;height:100%;object-fit:contain}
.mot .img svg{width:62%;height:62%}
.mot .img .sans{width:44%;height:44%;color:#CDBF9C;display:flex}
.mot .img .sans svg{width:100%;height:100%}
.mot .img:has(.sans){background:#FBF6E9}
.mot .es{font-weight:900;font-size:16.5px;color:var(--text-strong);line-height:1.2;overflow-wrap:anywhere}
.mot .fr{font-size:14px;color:var(--text-muted);line-height:1.25}
.mot .fr[hidden]{display:none}
.mot .piege{font-size:11.5px;font-weight:900;letter-spacing:.06em;text-transform:uppercase;color:var(--warn-ink);background:var(--warn-bg);
  border:1px solid var(--warn-line);border-radius:99px;padding:1px 8px;align-self:flex-start}
.note-piege{font-size:13.5px;background:var(--warn-bg);border-left:3px solid var(--warn-line);padding:6px 8px;border-radius:6px;color:var(--warn-ink)}

/* Exercices */
.consigne{font-size:15.5px;color:var(--text-muted);margin:0 0 10px}
.progres{height:8px;background:#EEE9DA;border-radius:99px;overflow:hidden;margin:6px 0 14px}
.progres i{display:block;height:100%;background:var(--borne);border-radius:99px;transition:width .3s}
.choix{display:flex;flex-direction:column;gap:8px;margin:10px 0}
.choix button{text-align:left;background:#fff;border:1.5px solid var(--line-300,#D6D6D2);border-radius:12px;padding:12px 14px;
  cursor:pointer;min-height:52px;font-size:16.5px;color:var(--text-strong);line-height:1.3}
.choix button small{display:block;font-size:13.5px;color:var(--text-muted);margin-top:3px}
.choix button.juste::before{content:"✓ ";font-weight:900}
.choix button.juste{border-color:var(--ok-line);background:var(--ok-bg);color:var(--ok-ink)}
.choix button.faux{border-color:var(--no-line);background:var(--no-bg);color:var(--no-ink);text-decoration:line-through;cursor:default}
.images{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:10px}
.images button{background:#fff;border:2px solid var(--line-200);border-radius:14px;padding:6px;cursor:pointer;aspect-ratio:1/1;
  display:flex;align-items:center;justify-content:center}
.images button img{width:100%;height:100%;object-fit:contain}
.images button svg{width:60%;height:60%}
.images button.juste{border-color:var(--ok-line);background:var(--ok-bg)}
.images button.faux{border-color:var(--no-line);background:var(--no-bg);opacity:.55}
.retro{border-radius:10px;padding:10px 12px;margin:8px 0;font-size:15.5px}
.retro.ok{background:var(--ok-bg);border:1px solid var(--ok-line);color:var(--ok-ink)}
.retro.no{background:var(--no-bg);border:1px solid var(--no-line);color:var(--no-ink)}
.retro.info{background:var(--fleche-bg);border:1px solid #E6CF7A;color:#5C4400}
.gros-son{display:flex;justify-content:center;margin:10px 0 4px}
.gros-son .btn--son{width:84px;height:84px;border-radius:50%}
.gros-son .btn--son svg{width:36px;height:36px}
.phrase-es{font-size:21px;font-weight:900;color:var(--text-strong);line-height:1.3;margin:6px 0}
.micro{display:flex;flex-direction:column;align-items:center;gap:8px;margin:12px 0}
.micro .btn-micro{width:84px;height:84px;border-radius:50%;background:var(--surface-inverse,#17181A);color:#fff;border:0;cursor:pointer;
  display:flex;align-items:center;justify-content:center}
.micro .btn-micro svg{width:34px;height:34px}
.micro .btn-micro.ecoute{background:var(--audio);animation:pouls 1.2s infinite}
@keyframes pouls{0%{box-shadow:0 0 0 0 rgba(220,38,38,.45)}70%{box-shadow:0 0 0 16px rgba(220,38,38,0)}100%{box-shadow:0 0 0 0 rgba(220,38,38,0)}}
.entendu{font-size:15.5px;min-height:24px;text-align:center;color:var(--text-body)}

/* Scène */
.scene-tete{display:flex;gap:12px;align-items:center;margin:4px 0 10px}
.scene-tete img{width:64px;height:64px;border-radius:50%;object-fit:cover;border:2px solid #fff;box-shadow:0 0 0 1px var(--line-200)}
.fil{display:flex;flex-direction:column;gap:10px}
.bulle{max-width:88%;border-radius:16px;padding:10px 12px;background:#fff;border:1px solid var(--line-200);position:relative}
.bulle.lui{align-self:flex-start;border-top-left-radius:4px}
.bulle.moi{align-self:flex-end;background:var(--accent-soft,#E6F5EE);border-color:var(--borne-trait);border-top-right-radius:4px}
.bulle .qui{font-size:13.5px;font-weight:900;letter-spacing:.05em;text-transform:uppercase;color:var(--text-muted);display:flex;gap:6px;align-items:center}
.bulle .qui svg{width:14px;height:14px}
.bulle .es{font-size:17px;color:var(--text-strong);font-weight:700}
.bulle .fr{font-size:14px;color:var(--text-muted);margin-top:4px}
.bulle .outils-b{display:flex;gap:6px;margin-top:6px}
.bulle .outils-b button{background:none;border:1px solid var(--line-200);border-radius:99px;padding:2px 10px;font-size:13px;font-weight:800;
  color:var(--text-muted);cursor:pointer;min-height:44px;display:inline-flex;align-items:center;gap:4px}
.bulle .es[hidden]{display:none!important}
.bulle .ecoute-dabord{font-size:14.5px;color:var(--text-muted);font-style:italic}
.objectif{background:var(--fleche-bg);border:1px solid #E6CF7A;border-radius:12px;padding:10px 12px;margin:10px 0;font-size:15.5px;color:#4A3A0A}
.rappel{font-size:12.5px;font-weight:900;letter-spacing:.06em;text-transform:uppercase;color:#7A6A45;background:#FBF6E9;border:1px solid #E6DCC3;border-radius:99px;padding:2px 10px;display:inline-block;margin-bottom:6px}
.bulle .outils-b svg{width:15px;height:15px}
.bulle .perso-mini{width:28px;height:28px;border-radius:50%;object-fit:cover}
.eliminatoire{border:2px solid var(--no-line);background:var(--no-bg);border-radius:14px;padding:14px;margin:12px 0}
.regle{border:1px dashed var(--warn-line);background:var(--warn-bg);color:var(--warn-ink);border-radius:12px;padding:10px 12px;font-size:15px;margin:8px 0}
.aide-bascule{display:flex;align-items:center;gap:8px;min-height:44px;font-size:14.5px;font-weight:800;color:var(--text-muted);margin:6px 0;cursor:pointer}
.aide-bascule input{width:20px;height:20px}

/* Poche */
details.rub{background:#fff;border:1px solid var(--line-200);border-radius:14px;margin:8px 0}
details.rub summary{padding:14px;font-weight:900;color:var(--text-strong);cursor:pointer;list-style:none;display:flex;justify-content:space-between;align-items:center;min-height:52px}
details.rub summary::-webkit-details-marker{display:none}
details.rub summary span{font-size:13px;color:var(--text-muted);font-weight:700;white-space:nowrap;flex:none;margin-left:12px}
.ph{display:flex;gap:10px;align-items:center;padding:10px 14px;border-top:1px solid var(--line-200)}
.ph .t{flex:1;min-width:0}
.ph .t b{display:block;color:var(--text-strong);font-size:16.5px;line-height:1.25}
.ph .t span{font-size:14px;color:var(--text-muted)}
.montrer{position:fixed;inset:0;background:#fff;z-index:50;display:flex;flex-direction:column;justify-content:center;align-items:center;
  padding:24px;text-align:center}
.montrer .grand{font-size:clamp(30px,9vw,64px);font-weight:900;line-height:1.15;color:#111}
.montrer .petit{font-size:17px;color:var(--text-muted);margin-top:14px}
.montrer .fermer{position:absolute;top:14px;right:14px}

/* Tampon */
.tampon-anim{animation:tamponner .55s cubic-bezier(.2,1.6,.4,1) both}
@keyframes tamponner{0%{transform:scale(2.4) rotate(-18deg);opacity:0}60%{opacity:1}100%{transform:scale(1) rotate(var(--rot,-8deg));opacity:1}}
.voile{position:fixed;inset:0;background:#FBF6E9;z-index:40;display:flex;flex-direction:column;align-items:center;
  justify-content:center;padding:24px;text-align:center}
.voile svg.tampon{width:min(62vw,260px);height:auto}

/* Compostela */
.compostela{background:#FBF4E2;border:1px solid #D9C79C;border-radius:8px;padding:26px 22px;text-align:center;
  font-family:Newsreader,Georgia,serif;color:#3B2E14;box-shadow:inset 0 0 0 6px #FBF4E2,inset 0 0 0 7px #CDB887}
.compostela .titre{font-size:30px;letter-spacing:.12em;text-transform:uppercase;margin:6px 0 12px}
.compostela,.compostela p{font-weight:400}
.compostela .latin{font-style:italic;font-size:17px;line-height:1.55}
.compostela .tampons{display:grid;grid-template-columns:repeat(5,minmax(0,1fr));gap:4px;margin-top:14px}
.compostela .tampons svg{width:100%;height:auto}
.compostela .nom{font-size:26px;margin:14px 0;border-bottom:1px solid #CDB887;display:inline-block;min-width:60%;padding:0 10px}
.avis-local{font-size:13px;color:var(--text-muted)}
.cache{display:none!important}
@media print{.fr-barre,.pas-imprimer{display:none!important}main{padding:0}}
</style>
</head>
<body>
<div class="fr-barre"><div class="fr-barre__in">
  <span class="fr-lockup"><span class="fr-nom" role="img" aria-label="francis">franc<span class="fr-i" aria-hidden="true">ı<span class="fr-point"></span></span>s</span><span class="fr-trait" aria-hidden="true"></span><span class="fr-desc">Aide à l'apprentissage de l'espagnol</span></span>
  <span class="secteur"><small>Voyage · chemin de Saint-Jacques</small><b>En route vers Compostelle</b></span>
</div></div>
<main id="app"></main>
<footer class="pied"><a href="#guide">Comment ça marche ?</a> · <a href="#confidentialite">Confidentialité</a></footer>
<audio id="lecteur" preload="none"></audio>
<script>
const D = %%DONNEES%%;
const SONS = new Set(D.sons);
const BASE = '/assets/interactive/compostelle/';
const E = s => String(s).replace(/[&<>"]/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const $ = s => document.querySelector(s);
const ICO = {
  guide:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="M9.1 9a3 3 0 0 1 5.8 1c0 2-3 3-3 3"/><path d="M12 17h.01"/></svg>',
  son:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M11 5 6 9H3v6h3l5 4V5z"/><path d="M15.5 8.5a5 5 0 0 1 0 7"/><path d="M18.5 5.5a9 9 0 0 1 0 13"/></svg>',
  oeil:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M2 12s3.5-7 10-7 10 7 10 7-3.5 7-10 7S2 12 2 12z"/><circle cx="12" cy="12" r="3"/></svg>',
  retour:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M15 18l-6-6 6-6"/></svg>',
  micro:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><rect x="9" y="3" width="6" height="11" rx="3"/><path d="M5 11a7 7 0 0 0 14 0"/><path d="M12 18v3"/></svg>',
  stop:'<svg viewBox="0 0 24 24" fill="currentColor"><rect x="6" y="6" width="12" height="12" rx="2"/></svg>',
  tel:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1.9.4 1.8.7 2.7a2 2 0 0 1-.5 2.1L8 9.8a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.7.7a2 2 0 0 1 1.7 2z"/></svg>',
  poche:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="7" width="18" height="14" rx="2.5"/><path d="M9 7V5a1 1 0 0 1 1-1h4a1 1 0 0 1 1 1v2M12 11v6M9 14h6"/></svg>',
  livre:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20V3H6.5A2.5 2.5 0 0 0 4 5.5z"/><path d="M4 19.5A2.5 2.5 0 0 0 6.5 22H20v-5"/></svg>',
  piege:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M10.3 3.9 1.8 18a2 2 0 0 0 1.7 3h17a2 2 0 0 0 1.7-3L13.7 3.9a2 2 0 0 0-3.4 0z"/><path d="M12 9v4M12 17h.01"/></svg>',
  test:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M9 11l3 3L22 4"/><path d="M21 12v7a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11"/></svg>',
  reglage:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="3"/><path d="M19.4 15a1.7 1.7 0 0 0 .3 1.8l.1.1a2 2 0 1 1-2.8 2.8l-.1-.1a1.7 1.7 0 0 0-1.8-.3 1.7 1.7 0 0 0-1 1.5V21a2 2 0 1 1-4 0v-.1a1.7 1.7 0 0 0-1.1-1.5 1.7 1.7 0 0 0-1.8.3l-.1.1a2 2 0 1 1-2.8-2.8l.1-.1a1.7 1.7 0 0 0 .3-1.8 1.7 1.7 0 0 0-1.5-1H3a2 2 0 1 1 0-4h.1a1.7 1.7 0 0 0 1.5-1.1 1.7 1.7 0 0 0-.3-1.8l-.1-.1a2 2 0 1 1 2.8-2.8l.1.1a1.7 1.7 0 0 0 1.8.3H9a1.7 1.7 0 0 0 1-1.5V3a2 2 0 1 1 4 0v.1a1.7 1.7 0 0 0 1 1.5 1.7 1.7 0 0 0 1.8-.3l.1-.1a2 2 0 1 1 2.8 2.8l-.1.1a1.7 1.7 0 0 0-.3 1.8V9a1.7 1.7 0 0 0 1.5 1H21a2 2 0 1 1 0 4h-.1a1.7 1.7 0 0 0-1.5 1z"/></svg>'
};
const PICTO = {
  gauche:'<svg viewBox="0 0 64 64"><path d="M50 32H16M28 18 14 32l14 14" fill="none" stroke="#1D6B8F" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/></svg>',
  droite:'<svg viewBox="0 0 64 64"><path d="M14 32h34M36 18l14 14-14 14" fill="none" stroke="#1D6B8F" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/></svg>',
  droit:'<svg viewBox="0 0 64 64"><path d="M32 52V14M18 26l14-14 14 14" fill="none" stroke="#1D6B8F" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/></svg>',
  haut:'<svg viewBox="0 0 64 64"><rect x="10" y="10" width="44" height="18" rx="3" fill="#F2C230" stroke="#5C4400" stroke-width="3"/><rect x="10" y="36" width="44" height="18" rx="3" fill="#fff" stroke="#5C4400" stroke-width="3"/></svg>',
  bas:'<svg viewBox="0 0 64 64"><rect x="10" y="10" width="44" height="18" rx="3" fill="#fff" stroke="#5C4400" stroke-width="3"/><rect x="10" y="36" width="44" height="18" rx="3" fill="#F2C230" stroke="#5C4400" stroke-width="3"/></svg>'
};
function horloge(h, m){
  const a = (h % 12) * 30 + m / 2, b = m * 6, r = x => (x - 90) * Math.PI / 180;
  const p = (ang, L) => `${32 + L * Math.cos(r(ang))},${32 + L * Math.sin(r(ang))}`;
  let t = ''; for (let i = 0; i < 12; i++) { const q = i * 30; t += `<line x1="${p(q,24).split(',')[0]}" y1="${p(q,24).split(',')[1]}" x2="${p(q,27).split(',')[0]}" y2="${p(q,27).split(',')[1]}" stroke="#333" stroke-width="2"/>`; }
  return `<svg viewBox="0 0 64 64"><circle cx="32" cy="32" r="29" fill="#fff" stroke="#333" stroke-width="3"/>${t}
    <line x1="32" y1="32" x2="${p(a,15).split(',')[0]}" y2="${p(a,15).split(',')[1]}" stroke="#111" stroke-width="4" stroke-linecap="round"/>
    <line x1="32" y1="32" x2="${p(b,23).split(',')[0]}" y2="${p(b,23).split(',')[1]}" stroke="#111" stroke-width="2.5" stroke-linecap="round"/>
    <circle cx="32" cy="32" r="2.5" fill="#111"/></svg>`;
}
function picto(nom){
  if (PICTO[nom]) return PICTO[nom];
  const m = /^h(\d{1,2})(30)?$/.exec(nom); if (m) return horloge(+m[1], m[2] ? 30 : 0);
  return '';
}
function imageMot(m, id){
  if (m.img === 'croquis') return `<img src="${BASE}croquis/${id}.jpg?v=${D.v}" alt="" loading="lazy">`;
  if (m.img.startsWith('picto:')) return picto(m.img.slice(6));
  return `<span class="sans" aria-hidden="true">${ICO.son}</span>`;
}

/* ---------- l'état, dans ce téléphone seulement ---------- */
const CLE = 'compostelle:v1';
let S = {genre:null, nom:'', aide:false, lent:false, alergia:'', essais:{}, jours:{}, vars:{}};
try { Object.assign(S, JSON.parse(localStorage.getItem(CLE) || '{}')); } catch(e) {}
function sauver(){ try { localStorage.setItem(CLE, JSON.stringify(S)); } catch(e) {} }
function jour(id){ return S.jours[id] || (S.jours[id] = {faits:{}, tampon:null}); }
// L'allergie choisie (défaut : les noix) remplit les {alg:…} ; audit tour 2.
const algCode = () => (S.alergia && D.alergenos.some(a => a.code === S.alergia)) ? S.alergia : 'frutos_secos';
const algDe = t => String(t).replace(/\{alg:(\w+)\}/g, (_, k) => D.alergenos.find(a => a.code === algCode()).formes[k]);
const g = t => algDe(t).replace(/\{([^{}|]*)\|([^{}|]*)\}/g, (_, m, f) => S.genre === 'f' ? f : m);
const aGenre = t => /\{[^{}|]*\|[^{}|]*\}/.test(algDe(t));
const suf = t => (/\{alg:/.test(t) ? '-a' + algCode() : '') + (aGenre(t) ? (S.genre === 'f' ? '-f' : '-m') : '');

/* ---------- le son ---------- */
const lecteur = $('#lecteur');
function jouer(fichier, naturel){
  return new Promise(res => {
    if (!fichier || !SONS.has(fichier)) { res(false); return; }
    arreterMicro();
    lecteur.pause();
    lecteur.src = BASE + 'sons/' + fichier + '?v=' + D.v;
    // Le ralenti étire dans le navigateur, sans changer la hauteur (mémoire
    // bouton-vitesse-voix) : les fichiers restent ceux du débit naturel.
    lecteur.playbackRate = (S.lent && !naturel) ? 0.8 : 1; lecteur.preservesPitch = true;
    lecteur.onended = () => res(true); lecteur.onerror = () => res(false);
    const p = lecteur.play(); if (p && p.catch) p.catch(() => res(false));
  });
}
const sonDe = (base, texte) => base + suf(texte) + '.mp3';

/* ---------- le micro (reconnaissance du navigateur, en es-ES) ---------- */
const Reco = window.SpeechRecognition || window.webkitSpeechRecognition;
let recoActive = null;
function arreterMicro(){ if (recoActive) { try { recoActive.stop(); } catch(e) {} } }
/* Loi 25 (27 sept. 2026) : avant le premier usage, dire où va la voix — chez
   le fournisseur du navigateur, pas chez nous. Accepté une fois, gardé dans
   le téléphone ; refusé, rien ne s'ouvre et l'exercice se fait en touchant. */
let micRefuse = false;
// Le message quand le micro ne rend rien : refusé à l'avis, ou rien entendu.
const rienEntendu = sinon => micRefuse
  ? 'Micro fermé, comme vous l’avez choisi. ' + (sinon.includes('touchez votre réponse') ? 'Touchez votre réponse.' : 'Dites la phrase à voix haute, puis touchez le bouton « je l’ai dit ».')
  : sinon;
function fournisseurVoix(){
  const u = navigator.userAgent;
  if (/Edg\//.test(u)) return 'Microsoft (Edge)';
  if (/Chrome|CriOS|Android/.test(u)) return 'Google (Chrome)';
  if (/Safari|iPhone|iPad|Macintosh/.test(u)) return 'Apple (Safari)';
  return 'l’éditeur de votre navigateur';
}
function ecouterMicro(surTexte, surFin){
  if (S.avisMicro) return ouvrirMicro(surTexte, surFin);
  const fond = document.createElement('div'); fond.className = 'avis-fond';
  fond.innerHTML = `<div class="avis-micro" role="dialog" aria-modal="true" aria-labelledby="avisT">
    <h3 id="avisT">Avant d'ouvrir le micro</h3>
    <p>Pour comprendre ce que vous dites, l'application utilise la reconnaissance vocale de <b>votre navigateur</b>.
    Votre voix est donc envoyée à <b>${fournisseurVoix()}</b>, aux États-Unis, qui la transcrit et renvoie le texte.</p>
    <p>Nous ne recevons pas votre voix et ne l'enregistrons pas. Le texte reste dans votre téléphone.</p>
    <p class="muted" style="font-size:14px">Vous préférez ne pas l'utiliser ? Tout se fait aussi sans micro : dites la phrase à voix haute, puis touchez « je l’ai dit » — elle n’est alors pas vérifiée. <a href="#confidentialite">En savoir plus</a></p>
    <div class="rangee"><button class="btn btn--pri" id="avisOui">J'ai compris, ouvrir le micro</button><button class="btn" id="avisNon">Pas maintenant</button></div></div>`;
  document.body.appendChild(fond);
  const fermer = () => fond.remove();
  fond.querySelector('#avisOui').onclick = () => { S.avisMicro = aujourdhui(); sauver(); fermer(); ouvrirMicro(surTexte, surFin); };
  fond.querySelector('#avisNon').onclick = () => { fermer(); micRefuse = true; surFin(''); micRefuse = false; };
  fond.querySelector('a').onclick = () => fermer();
  fond.querySelector('#avisOui').focus();
}
function ouvrirMicro(surTexte, surFin){
  // Le micro qui coupe (leçon de Francœur) : reconnaissance continue qui
  // accumule, fin sur « Arrêter » ou 4 s de silence (9 s avant le premier mot).
  const r = new Reco(); r.lang = 'es-ES'; r.continuous = true; r.interimResults = true;
  let final = '', minuterie = null, parle = false;
  const relancer = d => { clearTimeout(minuterie); minuterie = setTimeout(() => { try { r.stop(); } catch(e) {} }, d); };
  r.onresult = ev => {
    parle = true; let prov = '';
    for (let i = ev.resultIndex; i < ev.results.length; i++) {
      if (ev.results[i].isFinal) final += ev.results[i][0].transcript + ' ';
      else prov += ev.results[i][0].transcript;
    }
    surTexte((final + prov).trim()); relancer(4000);
  };
  r.onerror = () => {};
  r.onend = () => { clearTimeout(minuterie); recoActive = null; surFin(final.trim()); };
  recoActive = r; lecteur.pause();
  try { r.start(); relancer(9000); } catch(e) { recoActive = null; surFin(''); }
}
/* La reconnaissance espagnole écrit les nombres en chiffres (« 2 cafés »,
   « ¿12 €? », « a las 8:30 h ») : on les remet en lettres avant de comparer.
   Audit « Avant de partir », tour 1 (E1) : 4 phrases sur 8 refusées à tort. */
const NB = ['cero','uno','dos','tres','cuatro','cinco','seis','siete','ocho','nueve','diez','once','doce','trece','catorce','quince',
  'dieciseis','diecisiete','dieciocho','diecinueve','veinte','veintiuno','veintidos','veintitres','veinticuatro','veinticinco',
  'veintiseis','veintisiete','veintiocho','veintinueve'];
const DIZ = {3:'treinta',4:'cuarenta',5:'cincuenta',6:'sesenta',7:'setenta',8:'ochenta',9:'noventa'};
function nombreEs(n){ n = +n; if (n < 30) return NB[n]; if (n === 100) return 'cien'; if (n > 100) return String(n);
  const d = Math.floor(n / 10), u = n % 10; return DIZ[d] + (u ? ' y ' + NB[u] : ''); }
function heureEs(h, m){ h = +h % 12 || 12; m = +m; const H = x => (x % 12 || 12) === 1 ? 'una' : nombreEs(x % 12 || 12);
  if (m === 0) return H(h); if (m === 30) return H(h) + ' y media'; if (m === 15) return H(h) + ' y cuarto';
  if (m === 45) return H(h + 1) + ' menos cuarto'; return H(h) + ' y ' + nombreEs(m); }
const enLettres = t => String(t)
  .replace(/(\d{1,2}):(\d{2})\s*(h\b)?/gi, (_, h, m) => heureEs(h, m))
  .replace(/(\d+)[,.](\d{1,2})\s*€/g, (_, a, b) => nombreEs(a) + ' con ' + nombreEs(b) + ' euros')
  .replace(/€\s*(\d+)/g, (_, a) => a + ' euros').replace(/(\d+)\s*€/g, (_, a) => a + ' euros')
  .replace(/\d+/g, n => ' ' + nombreEs(n) + ' ');
const plat = t => enLettres(t).toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g, '').replace(/[^a-z0-9ñ ]+/g, ' ').replace(/\s+/g, ' ').trim();

// Une clé qui commence par « ~ » est une expression régulière sur le texte aplati
// (audit tour 3 : « no lo entiendo », « porque », « no tengo alergias »…).
const trouve = (t, cle) => cle.startsWith('~') ? new RegExp(cle.slice(1)).test(' ' + plat(t) + ' ') : cle.split('|').some(a => new RegExp('(^| )' + plat(a).replace(/[.*+?^${}()|[\]\\]/g, '\\$&') + '(s|es)?( |$)').test(plat(t)));
/* ---------- ordre des choix : jamais la bonne toujours au même rang ---------- */
function ordre(n, graine){ const o = [...Array(n).keys()]; const d = graine % n; return o.slice(d).concat(o.slice(0, d)); }

/* ---------- le tampon ---------- */
function tampon(et, date){
  const enc = 'var(--tampon)', rot = ((et.n * 37) % 17) - 8;
  const nom = et.lieu.toUpperCase(), id = 'arc' + et.id.replace(/[^a-z]/g, '');
  const img = et.vignette ? `<clipPath id="c${id}"><circle cx="60" cy="60" r="30"/></clipPath>
    <image href="${BASE}etapes/${et.img}.jpg?v=${D.v}" x="15" y="30" width="90" height="60" clip-path="url(#c${id})" preserveAspectRatio="xMidYMid slice" style="filter:grayscale(1) sepia(.6) contrast(1.1)" opacity=".85"/>` : '';
  return `<svg class="tampon" viewBox="0 0 120 120" style="--rot:${rot}deg;transform:rotate(${rot}deg)" role="img" aria-label="Tampon de ${E(et.lieu)}">
    <defs><path id="${id}" d="M60,60 m-44,0 a44,44 0 1,1 88,0 a44,44 0 1,1 -88,0"/></defs>
    <circle cx="60" cy="60" r="56" fill="none" stroke="${enc}" stroke-width="3"/>
    <circle cx="60" cy="60" r="49" fill="none" stroke="${enc}" stroke-width="1.2"/>
    ${img}<circle cx="60" cy="60" r="30" fill="none" stroke="${enc}" stroke-width="2"/>
    <text font-family="Nunito,system-ui" font-weight="900" font-size="${nom.length > 16 ? 8.2 : 10}" letter-spacing="1.5" fill="${enc}">
      <textPath href="#${id}" startOffset="${nom.length > 16 ? 2 : 6}%">${E(nom)} · ${et.n} ·</textPath></text>
    ${date ? `<text x="60" y="104" text-anchor="middle" font-family="Nunito,system-ui" font-weight="800" font-size="7.5" fill="${enc}">${E(date)}</text>` : ''}
  </svg>`;
}
const aujourdhui = () => new Date().toLocaleDateString('fr-CA', {day:'numeric', month:'short', year:'numeric'});

/* ---------- la borne ---------- */
/* Le mojón, dans le trait des autres croquis (le dessin du lexique, recadré en
   decor/borne.jpg), avec sur sa face la plaque des kilomètres qui restent —
   comme sur le vrai chemin. 26 sept. 2026 : le premier essai, une borne en SVG
   collée au titre, était « petit et mal intégré » (Daniel). */
const KM_TOTAL = 775, KM_JOUR = 25;
function joursMarche(e){ const i = D.etapes.indexOf(e), avant = i > 0 ? D.etapes[i - 1].km : 0;
  return Math.max(1, Math.ceil((e.km - avant) / KM_JOUR - 0.2)); }
function marche(e){ const i = D.etapes.indexOf(e), j = joursMarche(e);
  return `${j} jour${j > 1 ? 's' : ''} de marche depuis ${i > 0 ? E(COURT[D.etapes[i - 1].id] || D.etapes[i - 1].lieu) : 'Saint-Jean'}`; }
function plaque(reste){ return reste > 0 ? reste.toLocaleString('fr-CA') + ' km' : '¡Santiago!'; }
function borneImg(reste, petite){
  return `<div class="borne-img${petite ? ' petite' : ''}" role="img" aria-label="Borne du chemin : ${reste > 0 ? 'encore ' + reste + ' kilomètres jusqu’à Santiago' : 'Santiago'}">
    <img src="${BASE}decor/borne.jpg?v=${D.v}" alt=""><span class="plaque">${plaque(reste)}</span></div>`;
}
/* ---------- navigation ---------- */
const TEMPS = [
  ['lieu', 'Le lieu', 'Ce qu’on y voit, ce qu’on y visite'],
  ['mots', 'Les mots du jour', 'En images, avec la voix'],
  ['entends', 'J’entends, je trouve', 'Un mot entendu, son image'],
  ['repond', 'Ce qu’on me répond', 'Comprendre une réponse dite vite'],
  ['scene', 'La scène', 'La situation, jouée'],
  ['dire', 'Je le dis', 'Ce que vous venez d\u2019entendre, à vous de le dire'],
  ['soir', 'Le soir, avec Marta', 'La conversation du jour']];
const app = $('#app');
function aller(h){ location.hash = h; }
window.addEventListener('hashchange', rendre);
function retour(h, t){ return `<button class="retour pas-imprimer" onclick="aller('${h}')">${ICO.retour} ${E(t)}</button>`; }
function etapeParId(id){ return D.etapes.find(e => e.id === id); }
function prochaine(){ return D.etapes.find(e => !jour(e.id).tampon) || null; }

function rendre(){
  arreterMicro(); lecteur.pause(); lecteur.ontimeupdate = null;
  const p = (location.hash.slice(1) || 'accueil').split('/');
  window.scrollTo(0, 0);
  if (p[0] === 'guide') return vueGuide();
  if (p[0] === 'confidentialite') return vueConfidentialite();
  if (p[0] === 'achat') return vueAchat(p[1]);
  if (p[0] === 'achat-annule') return vueAchatAnnule();
  if (!S.genre && p[0] !== 'reglages') return vueBienvenue();
  if (p[0] === 'jour' && etapeParId(p[1])) {
    const et = etapeParId(p[1]);
    if (!p[2]) return vueJour(et);
    const f = {lieu: vueLieu, mots: vueMotsJour, entends: vueEntends, repond: vueRepond, dire: vueDire,
               scene: (e) => vueScene(e, 'scene'), soir: (e) => vueScene(e, 'soir'),
               libre: (e) => D.jeuLibre ? vueLibre(e) : vueJour(e)}[p[2]];
    if (f) return f(et);
  }
  if (p[0] === 'prep') return p[1] === 'test' ? vuePrepTest() : p[1] ? vueSeance(p[1], p[2]) : vuePrep();
  if (p[0] === 'trousse' || p[0] === 'poche') return vuePoche();
  if (p[0] === 'mots') return vueMots(p[1]);
  if (p[0] === 'pieges') return vuePieges();
  if (p[0] === 'reglages') return vueReglages();
  if (p[0] === 'test') return vueTest();
  if (p[0] === 'compostela') return vueCompostela();
  return vueAccueil();
}

/* ---------- confidentialité (Loi 25) ---------- */
/* Texte : build/contenu/compostelle/confidentialite.py. Les cases à remplir
   restent visibles en ambre ; la durée de conservation vient du serveur. */
function vueConfidentialite(){
  const C = D.confid;
  const ambre = t => `<span class="a-remplir">${t}</span>`;
  const resp = C.responsable ? `${E(C.responsable[0])}, ${E(C.responsable[1])}` : ambre('personne responsable à désigner');
  const rendu = cons => {
    const duree = `effacés ${cons} jours après la fin de votre accès (et un code jamais payé, après 7 jours)`;
    app.innerHTML = `${retour(S.genre ? 'accueil' : '', S.genre ? 'Accueil' : 'Retour')}
    <p class="surtitre">Loi 25 · mise à jour le ${E(C.maj)}</p><h1>Vos renseignements personnels</h1>
    <div class="carte cf-bref"><h3 style="margin-top:0">En bref</h3><ul>${C.bref.map(t => `<li>${t}</li>`).join('')}</ul></div>
    <h2>Ce que nous savons de vous, et où c'est</h2>
    ${C.donnees.map(([q, ou, qui, dur]) => `<div class="carte cf-ligne"><b>${E(q)}</b>
      <dl><dt>Où</dt><dd>${E(ou)}</dd><dt>Qui le voit</dt><dd>${E(qui)}</dd><dt>Combien de temps</dt><dd>${E(dur).replace('{conservation}', duree)}</dd></dl></div>`).join('')}
    <h2>Ce qui sort du Québec</h2>
    <p>Certains services sont situés à l'extérieur du Québec. Voici lesquels, et ce qu'ils reçoivent :</p>
    <div class="carte">${C.hors.map(([qui, quoi, ou]) => `<p class="cf-hors"><b>${E(qui)}</b> — ${E(quoi)} <span class="muted">(${E(ou)})</span></p>`).join('')}</div>
    <p>Vous pouvez éviter l'envoi de votre voix : n'ouvrez pas le micro ; dites les phrases à voix haute et touchez « je l'ai dit » (elles ne sont alors pas vérifiées). Vous pouvez éviter l'envoi à Anthropic : n'utilisez pas « Parler librement ». Le reste de l'application fonctionne sans.</p>
    <h2>Ce que nous ne faisons pas</h2><ul>${C.nefait.map(t => `<li>${E(t)}</li>`).join('')}</ul>
    <h2>Vos droits</h2>
    <p>Vous pouvez demander à savoir ce que nous détenons à votre sujet, le faire corriger ou effacer. Comme nous ne savons pas qui vous êtes, donnez-nous votre <b>code d'accès</b> : c'est tout ce que nous avons.
    Ce qui est dans votre téléphone, vous l'effacez vous-même : <a href="#reglages">Réglages</a> → recommencer, ou vider les données du navigateur.</p>
    <p>Pour toute question ou demande : <a href="mailto:${E(C.courriel)}">${E(C.courriel)}</a>. Responsable de la protection des renseignements personnels : ${resp}.</p>
    <p class="muted" style="font-size:14px">Si notre réponse ne vous satisfait pas, vous pouvez vous adresser à la Commission d'accès à l'information du Québec.</p>
    <h2>En cas d'incident</h2>
    <p>Si un incident touchait des renseignements que nous détenons (vos codes), nous le consignerions et avertirions la Commission d'accès à l'information et les personnes concernées lorsque la loi l'exige.</p>`;
  };
  rendu('365'); offreServeur().then(o => { if (o && o.conservation && location.hash === '#confidentialite') rendu(String(o.conservation)); });
}

/* ---------- comment ça marche ---------- */
/* Demande de Daniel, 26 sept. 2026 : un lien sur la première page vers
   l'explication de l'outil. La même route que l'infographie du classeur
   (assets/presentations/compostelle-parcours.html), dite au pèlerin. */
function vueGuide(){
  const phases = [['Découvrir', 'vous recevez', ['lieu', 'mots', 'entends']],
                  ['Comprendre', 'vous reconnaissez ce qu’on vous dit', ['repond']],
                  ['Agir', 'vous parlez, vous jouez', ['scene', 'dire', 'soir']]];
  const TAMP = ['repond', 'scene', 'dire', 'soir'];
  const ph = phases.map(([nom, sous, ks]) => `<div class="g-phase"><p class="surtitre">${nom} <span>· ${sous}</span></p><ol>${
    ks.map(k => { const i = TEMPS.findIndex(t => t[0] === k), t = TEMPS[i];
      return `<li value="${i + 1}"><b>${E(t[1])}</b>${TAMP.includes(k) ? ' <span class="g-tamp" title="compte pour le tampon">✓ tampon</span>' : ''}<br><span class="muted">${E(t[2])}</span></li>`; }).join('')}</ol></div>`).join('');
  const jours = D.etapes.map(e => `<li><b>Halte ${e.n} · ${E(e.lieu)}</b> <span class="muted">km ${e.km} · ${marche(e)}</span><br>${E(e.objectif)}</li>`).join('');
  app.innerHTML = `${retour(S.genre ? 'accueil' : '', S.genre ? 'La credencial' : 'Retour')}
  <p class="surtitre">Le mode d'emploi</p><h1>Comment ça marche ?</h1>
  <p>Dix haltes sur le Camino francés, de Roncesvalles à Santiago — environ ${D.etapes.reduce((t, e) => t + joursMarche(e), 0)} jours de marche. Chaque halte prépare une situation dont vous aurez
  besoin ce soir-là : trouver un lit, commander, vous soigner, demander votre chemin, parler avec les autres.</p>
  <div class="retro info"><b>Avant de partir</b> : préparer votre sac — huit entraînements de quinze minutes, à la maison — les sons, la politesse, les nombres, l'heure, quatre verbes, les questions, se présenter, comprendre la réponse — puis le test « Prêt à partir ? ». Conseillées, jamais obligatoires. <a href="#prep">Y aller</a>.</div>
  <div class="objectif"><b>La règle du chemin :</b> comprendre avant de dire, dire avant de jouer, jouer avant d'y aller seul.</div>
  <h2>Une halte, sept temps</h2>
  <p>Toujours dans le même ordre. Touchez un temps dans la halte pour le faire ; vous pouvez le refaire autant que vous voulez.</p>
  ${ph}
  <h2>Le tampon</h2>
  <p>Votre credencial se tamponne quand les quatre temps marqués <span class="g-tamp">✓ tampon</span> sont faits : comprendre,
  jouer la scène, dire, parler le soir. Lire et écouter ne suffisent pas : sur le chemin, il faudra parler.</p>
  <h2>Les dix haltes</h2>
  <p>Faites-les dans l'ordre : ce qui a été appris revient plus loin, sans prévenir (« Rappel · halte 2 »).
  À <b>León</b>, votre allergie est éliminatoire : la rater fait rejouer la scène. Après León, elle revient chaque jour.</p>
  <ol class="g-jours">${jours}</ol>
  <h2>Et aussi</h2>
  <ul class="g-liste">
   <li><b>Parler librement</b> — au bas de chaque halte${D.jeuLibre ? '' : ' (bientôt)'} : la même personne vous répond vraiment, à votre vitesse, puis un bilan en français. Il faut un code : il s'obtient là, en quelques secondes, ou vient de votre groupe. Les haltes, elles, restent gratuites.</li>
   <li><b>Ma trousse</b> — la trousse de secours pour se débrouiller : les phrases du chemin, les urgences (112) et votre carte d'allergie en grand, à montrer. « Préparer pour le chemin » les garde dans le téléphone : elles marchent sans réseau.</li>
   <li><b>Tous les mots</b> et <b>les faux amis</b> — pour revoir, quand vous voulez.</li>
   <li><b>Suis-je prêt ?</b> — un quart d'heure de situations nouvelles avant le départ. Il vous situe (Solide · En route · À reprendre), il ne vous note pas.</li>
   <li><b>La Compostela</b> — au dixième tampon, un souvenir à imprimer.</li>
  </ul>
  <h2>Conseils</h2>
  <ul class="g-liste">
   <li>Mettez des écouteurs, et parlez à voix haute : le micro vous écoute seulement quand vous le touchez.</li>
   <li>Les voix vont trop vite ? Cochez « Voix plus lentes », dans la scène.</li>
   <li>Pour l'avoir comme une application : menu du navigateur, « Ajouter à l'écran d'accueil » (sur iPhone : Partager, puis « Sur l'écran d'accueil »). Sur iPhone, c'est aussi ce qui garde vos tampons si vous restez des semaines sans l'ouvrir.</li>
   <li>Rien ne quitte ce téléphone : aucun compte, aucune inscription. Changer de téléphone, c'est repartir de zéro.</li>
  </ul>
  ${S.genre ? `<button class="btn btn--pri btn--large" style="margin-top:14px" onclick="aller('accueil')">Reprendre la route</button>` :
             `<button class="btn btn--pri btn--large" style="margin-top:14px" onclick="aller('')">Commencer</button>`}`;
}

/* ---------- bienvenue ---------- */
function vueBienvenue(){
  app.innerHTML = `
  <div class="heros"><img src="${BASE}etapes/meseta.jpg?v=${D.v}" alt="La Meseta, un chemin droit dans les blés, une borne à flèche jaune">
   <div class="txt"><p class="surtitre">Le Camino francés · 775 km</p><h1>En route vers Compostelle</h1>
   <p>L'espagnol qu'il faut pour le chemin : trouver un lit, manger, se soigner, demander sa route, et parler avec les gens — halte après halte, de Roncesvalles à Santiago.</p></div></div>
  <div class="carte" style="margin-top:14px">
   <h2 style="margin-top:0">Avant de partir</h2>
   <p>Deux questions. L'allergie d'abord : c'est la phrase que vous apprendrez à dire, et celle qui ne pardonne pas.</p>
   <label for="alg0" style="display:block;font-weight:800;margin:6px 0">Avez-vous une allergie alimentaire ?</label>
   <select id="alg0" onchange="S.alergia=this.value;sauver()" style="font:inherit;padding:8px;border-radius:10px;border:1px solid var(--line-300);min-height:44px;width:100%;margin-bottom:12px">
    <option value="">Non, aucune</option>${D.alergenos.map(a => `<option value="${a.code}" ${S.alergia === a.code ? 'selected' : ''}>Oui, ${E(a.fr)}</option>`).join('')}</select>
   <div class="rangee"><button class="btn btn--pri" onclick="choisirGenre('m')">Un pèlerin</button>
   <button class="btn btn--pri" onclick="choisirGenre('f')">Une pèlerine</button></div>
   <p class="avis-local" style="margin-top:12px">Puis : en espagnol, on ne dit pas la même chose à un pèlerin et à une pèlerine (<i>cansado</i>, <i>cansada</i>). Tout ce que vous faites ici reste dans ce téléphone : rien n'est envoyé.</p>
  </div>
  <button class="btn btn--large lien-guide" onclick="aller('guide')">${ICO.guide} Comment ça marche ?</button>`;
}
function choisirGenre(x){ S.genre = x; sauver(); location.hash = '#accueil'; rendre(); }

/* ---------- accueil ---------- */
function frise(){
  const W = 340, x = n => 14 + (W - 28) * (D.etapes[n].km / 775);
  let s = `<svg class="frise" viewBox="0 0 ${W} 58" role="img" aria-label="Votre avancée sur le chemin"><line class="ligne" x1="14" y1="24" x2="${W-14}" y2="24"/>`;
  D.etapes.forEach((e, i) => {
    const ok = jour(e.id).tampon; s += `<circle class="${ok ? 'ok' : 'ko'}" cx="${x(i)}" cy="24" r="${ok ? 7 : 5}"/>`;
    if (i === 0 || i === 4 || i === 9) s += `<text x="${x(i)}" y="50" style="text-anchor:${i === 0 ? 'start' : i === 9 ? 'end' : 'middle'}">${E(COURT[e.id] || e.lieu)}</text>`;
  });
  return s + `<circle class="ok" cx="14" cy="24" r="4"/><text x="14" y="10" style="text-anchor:start">St-Jean</text></svg>`;
}
const COURT = {'puente-la-reina': 'Puente', 'carrion': 'Carrión', 'o-cebreiro': 'Cebreiro', 'santiago': 'Santiago'};
function vueAccueil(){
  const pro = prochaine(), faits = D.etapes.filter(e => jour(e.id).tampon).length;
  const nP = prepFaites(), totP = D.prep.seances.length, sacPret = nP === totP, proP = prepProchaine();
  const testFait = !!((S.prep || {}).test || {}).passages, pret = S.genre === 'f' ? 'prête' : 'prêt';
  const cases = D.etapes.map(e => {
    const j = jour(e.id);
    const nom = `<small>${E(COURT[e.id] || e.lieu)}</small>`;
    if (j.tampon) return `<div class="case-w"><button class="case faite" onclick="aller('jour/${e.id}')" aria-label="${E(e.lieu)} : tamponné">${tampon(e, '')}</button>${nom}</div>`;
    const cour = pro && pro.id === e.id;
    return `<div class="case-w"><button class="case${cour ? ' courante' : ''}" onclick="aller('jour/${e.id}')" aria-label="Étape ${e.n} : ${E(e.lieu)}"><span>${e.n}</span><em>${cour ? 'à faire' : 'sello'}</em></button>${nom}</div>`;
  }).join('');
  // 1 · le sac
  const sac = `<section class="acc-temps${sacPret ? ' acc-temps--fait' : ''}" id="sac">
    <p class="surtitre">1 · Avant de partir</p>
    <h2 class="acc-h">${sacPret ? `Mon sac est prêt ✓` : 'Préparer mon sac'}</h2>
    ${sacPret ? '' : `<p class="acc-p">Avant le Camino, on prépare son sac et on s'entraîne à marcher. Pour l'espagnol, c'est pareil :
      <b>huit entraînements de quinze minutes</b>, à la maison. Chacun met un outil dans votre sac.</p>`}
    ${sacGrille(true)}
    ${!sacPret ? `<button class="btn btn--pri btn--large" onclick="aller('prep/${proP.id}')">Entraînement ${nP + 1} : ${E(proP.titre)}</button>
      <p class="muted acc-note">Conseillé, jamais obligatoire : le chemin reste ouvert.</p>` :
      !testFait ? `<button class="btn btn--pri btn--large" onclick="aller('prep/test')">La marche d'essai : ${pret} à partir ?</button>
      <p class="muted acc-note">Un quart d'heure pour savoir où vous en êtes — à refaire la veille du départ.</p>` :
      `<button class="btn btn--large" onclick="aller('prep')">Revoir mon sac</button>`}
  </section>`;
  // 2 · le chemin
  const chemin = `<section class="acc-temps" id="chemin">
    <p class="surtitre">2 · Sur le chemin</p>
    <h2 class="acc-h">Dix étapes choisies</h2>
    <p class="acc-p">Le Camino francés compte une trentaine d'étapes de marche, de Saint-Jean à Santiago. Nous en avons retenu <b>dix</b> :
      celles où l'espagnol devient nécessaire — trouver un lit, commander, se soigner, demander son chemin, parler avec les autres.</p>
    <div class="carte-borne">${borneImg(pro ? KM_TOTAL - pro.km : 0)}<div class="cb-txt">
     <p class="surtitre">${pro ? 'Prochaine étape · ' + pro.n + ' sur 10' : 'Au bout du chemin'}</p>
     <h1>${faits === 10 ? '¡Lo has conseguido!' : pro ? E(pro.lieu) : ''}</h1>
     ${pro ? `<p class="muted">${E(pro.titre)} — ${E(pro.region)}</p>
     <p class="cb-reste">Encore <b>${(KM_TOTAL - pro.km).toLocaleString('fr-CA')} km</b> jusqu'à Santiago<br><span>${marche(pro)}</span></p>` :
     `<p class="cb-reste">Vous êtes arrivé${S.genre === 'f' ? 'e' : ''} à Santiago.</p>`}</div></div>
    ${pro ? `<button class="btn ${sacPret || faits ? 'btn--pri' : ''} btn--large" onclick="aller('jour/${pro.id}')">${faits ? 'Reprendre la route' : 'Partir : étape 1, ' + E(pro.lieu)}</button>` :
      `<button class="btn btn--pri btn--large" onclick="aller('compostela')">Voir ma Compostela</button>`}
    <div style="margin:16px 0 6px">${frise()}</div>
    <div class="livret">
      <div class="livret-tete"><img src="${BASE}croquis/concha.jpg?v=${D.v}" alt=""><div><small>Credencial del peregrino</small><b>Ma credencial</b></div>
        <span class="livret-compte">${faits} / 10<small>tampons</small></span></div>
      <p class="livret-leg">Le carnet du pèlerin. Sur le vrai chemin, on le fait tamponner à chaque arrêt ; ici, chaque étape réussie y pose son tampon — <i lang="es">el sello</i>.</p>
      <div class="cred">${cases}</div>
    </div>
    <details class="rub" style="margin-top:12px"><summary>Au bout du chemin, vous saurez… <span>la règle</span></summary>
     <div style="padding:0 14px 12px;font-size:15.5px"><ul style="margin:0 0 8px;padding-left:20px">
      <li>obtenir un lit, et comprendre le prix et les heures ;</li><li>commander, et <b>dire votre allergie</b> puis comprendre la réponse ;</li>
      <li>dire où vous avez mal et comprendre la posologie ;</li><li>demander votre chemin et le suivre ;</li><li>parler avec un autre pèlerin.</li></ul>
      <p style="margin:0">Une erreur ne pardonne pas : <b>l'allergie</b>. À León comme au test « Suis-je prêt ? », la rater fait recommencer.
      ${S.alergia ? 'La vôtre : ' + E(allergie().fr) + '.' : 'Choisissez la vôtre dans les réglages.'}</p></div></details>
  </section>`;
  app.innerHTML = `
  <ol class="deux-temps">
    <li class="${sacPret ? 'fait' : 'actif'}"><a href="#accueil" onclick="event.preventDefault();document.getElementById('sac').scrollIntoView({behavior:'smooth'})"><span>${sacPret ? '✓' : '1'}</span><b>Préparer mon sac</b><small>${nP} / ${totP} entraînements</small></a></li>
    <li class="${sacPret || faits ? 'actif' : ''}${faits === 10 ? ' fait' : ''}"><a href="#accueil" onclick="event.preventDefault();document.getElementById('chemin').scrollIntoView({behavior:'smooth'})"><span>${faits === 10 ? '✓' : '2'}</span><b>Marcher le chemin</b><small>${faits} / 10 étapes</small></a></li>
  </ol>
  <button class="btn btn--large lien-guide" onclick="aller('guide')">${ICO.guide} Comment ça marche ?</button>
  ${sacPret ? chemin + sac : sac + chemin}
  <h2>Pour la route</h2>
  <div class="outils">
   <button class="outil" onclick="aller('trousse')">${ICO.poche}<div><b>Ma trousse</b><span>La trousse de secours pour se débrouiller : les phrases du chemin, les urgences — sans réseau</span></div></button>
   <button class="outil" onclick="aller('mots')">${ICO.livre}<div><b>Tous les mots</b><span>${Object.keys(D.mots).length} mots, onze planches</span></div></button>
   <button class="outil" onclick="aller('pieges')">${ICO.piege}<div><b>Les faux amis</b><span>constipado, embarazada, la carta…</span></div></button>
   <button class="outil" onclick="aller('test')">${ICO.test}<div><b>Suis-je ${pret} ?</b><span>Le test du chemin, après les étapes</span></div></button>
   <button class="outil" onclick="aller('reglages')">${ICO.reglage}<div><b>Réglages</b><span>Pèlerin ou pèlerine, traductions, recommencer</span></div></button>
  </div>`;
}

/* ---------- une journée ---------- */
function vueJour(et){
  const j = jour(et.id);
  const liste = TEMPS.map(([k, t, d], i) => {
    const f = j.faits[k];
    return `<li class="${f ? 'fait' : ''}"><button onclick="aller('jour/${et.id}/${k}')"><span class="num">${f ? '✓' : i + 1}</span>
      <span><b>${t}</b><span class="d">${d}</span></span>${f ? '<span class="etat">✓ fait</span>' : ''}</button></li>`;
  }).join('');
  const suivant = TEMPS.find(([k]) => !j.faits[k]);
  const libre = D.jeuLibre ? `<h2>Pour aller plus loin</h2><ul class="etapes-j"><li><button onclick="aller('jour/${et.id}/libre')"><span class="num">+</span>
      <span><b>Parler librement, avec l'assistant</b><span class="d">${E(D.perso[et.local].nom)} ou Marta vous répondent vraiment. Il faut du réseau et un code.</span></span></button></li></ul>` : '';
  app.innerHTML = `${retour('accueil', 'La credencial')}
  <div class="bandeau">${et.vignette ? `<img src="${BASE}etapes/${et.img}.jpg?v=${D.v}" alt="">` : ''}</div>
  <p class="surtitre" style="margin-top:12px">Halte ${et.n} · ${E(et.region)} · km ${et.km}</p>
  <h1>${E(et.lieu)}</h1><p class="muted">${E(et.titre)}</p>
  ${OUTILLE[et.id] ? `<p class="avis-local" style="margin:4px 0 0">Les outils de cette halte : ${OUTILLE[et.id].map(id => `<a href="#prep/${id}">entraînement ${numSeance(seanceParId(id))}, ${E(seanceParId(id).titre.toLowerCase())}</a>`).join(' · ')}.</p>` : ''}
  <div class="bande-borne">${borneImg(KM_TOTAL - et.km, true)}<p>Encore <b>${(KM_TOTAL - et.km).toLocaleString('fr-CA')} km</b> jusqu'à Santiago<br><span>${marche(et)}</span></p></div>
  <div class="objectif"><b>Aujourd'hui :</b> ${E(et.objectif)}</div>
  ${j.tampon ? `<div class="retro ok">✓ Tamponné le ${E(j.tampon)}. Vous pouvez rejouer chaque temps.</div>` :
   peutTamponner(et) ? `<button class="btn btn--pri btn--large" onclick="poserTampon(etapeParId('${et.id}'))">Faire tamponner ma credencial</button>` :
   `<button class="btn btn--pri btn--large" onclick="aller('jour/${et.id}/${suivant ? suivant[0] : 'lieu'}')">${suivant && suivant[0] !== 'lieu' ? 'Continuer : ' + suivant[1] : 'Commencer la halte'}</button>`}
  <ul class="etapes-j">${liste}</ul>${libre}
  <p class="avis-local" style="margin-top:12px">Le tampon se gagne avec « Ce qu'on me répond », la scène, « Je le dis » et le soir avec Marta.</p>`;
}
function peutTamponner(et){ const j = jour(et.id); return !j.tampon && ['repond', 'scene', 'dire', 'soir'].every(x => j.faits[x]); }
function fini(et, k){
  jour(et.id).faits[k] = true; sauver();
  if (peutTamponner(et)) { setTimeout(() => { const b = $('#tampF'); if (b) b.onclick = () => poserTampon(et); }, 0);
    return `<button class="btn btn--pri btn--large" id="tampF">Faire tamponner ma credencial</button>`; }
  const i = TEMPS.findIndex(t => t[0] === k), s = TEMPS[i + 1];
  return s ? `<button class="btn btn--pri btn--large" onclick="aller('jour/${et.id}/${s[0]}')">Suivant : ${s[1]}</button>` :
    `<button class="btn btn--pri btn--large" onclick="aller('jour/${et.id}')">Retour à la halte</button>`;
}
function tete(et, k){
  const i = TEMPS.findIndex(t => t[0] === k);
  return `${retour('jour/' + et.id, 'Halte ' + et.n + ' · ' + et.lieu)}<p class="surtitre">${i + 1} / 7</p><h1>${TEMPS[i][1]}</h1>`;
}

/* 1. le lieu */
function vueLieu(et){
  app.innerHTML = `${tete(et, 'lieu')}
  <div class="bandeau">${et.vignette ? `<img src="${BASE}etapes/${et.img}.jpg?v=${D.v}" alt="">` : ''}</div>
  <div style="margin-top:12px">${et.intro.map(p => `<p>${E(p)}</p>`).join('')}</div>
  <h2>À voir</h2>
  <div class="carte" style="padding:0">${et.voir.map(([es, fr], i) => `<div class="ph">
    <button class="btn btn--son" aria-label="Écouter" onclick="jouer('voir/${et.id}-${i}.mp3')">${ICO.son}</button>
    <div class="t"><b>${E(es)}</b><span>${E(fr)}</span></div></div>`).join('')}</div>
  <div style="margin-top:16px" id="fin"></div>`;
  $('#fin').innerHTML = fini(et, 'lieu');
}

/* 2. les mots */
function carteMot(id, montrer){
  const m = D.mots[id]; if (!m) return '';
  const piege = m.note.startsWith('PIÈGE');
  return `<button class="mot" onclick="toucherMot(this,'${id}')">
    <div class="img">${imageMot(m, id)}</div>
    ${piege ? '<span class="piege">Faux ami</span>' : ''}
    <span class="es">${E(g(m.es))}</span>
    <span class="fr" ${montrer || S.aide ? '' : 'hidden'}>${E(m.fr)}</span>
    ${piege ? `<span class="note-piege" ${montrer || S.aide ? '' : 'hidden'}>${E(m.note.replace(/^PIÈGE\s*(\([^)]*\))?\s*:\s*/, ''))}</span>` : ''}
  </button>`;
}
function toucherMot(el, id){
  jouer('mots/' + id + '.mp3');
  el.querySelectorAll('.fr,.note-piege').forEach(x => x.hidden = false);
}
function vueMotsJour(et){
  app.innerHTML = `${tete(et, 'mots')}
  <p class="consigne">Touchez une carte : vous entendez le mot, et la traduction apparaît.</p>
  <div class="grille">${et.mots.map(motId).map(id => carteMot(id)).join('')}</div>
  <div style="margin-top:16px">${fini(et, 'mots')}</div>`;
}

/* 3. j'entends, je trouve */
function vueEntends(et){
  const pool = et.mots.map(motId).filter(id => D.mots[id] && D.mots[id].img);
  const dec = Math.floor(Math.random() * pool.length);
  const tours = pool.slice(dec).concat(pool.slice(0, dec)).slice(0, Math.min(6, pool.length));
  let n = 0, erreurs = 0;
  function tour(){
    if (n >= tours.length) {
      app.innerHTML = `${tete(et, 'entends')}<div class="retro ok">✓ ${tours.length} mots trouvés${erreurs ? ', ' + erreurs + ' erreur' + (erreurs > 1 ? 's' : '') + ' en route' : ' du premier coup'}.</div>
        <div style="margin-top:12px">${fini(et, 'entends')}</div>`; return;
    }
    const cible = tours[n];
    const autres = pool.filter(x => x !== cible);
    const opts = [cible, ...autres.slice((n * 3) % Math.max(1, autres.length)).concat(autres).slice(0, 3)];
    const o = ordre(opts.length, n * 7 + et.n);
    app.innerHTML = `${tete(et, 'entends')}
      <div class="progres"><i style="width:${100 * n / tours.length}%"></i></div>
      <p class="consigne">Écoutez, puis touchez l'image du mot entendu.</p>
      <div class="gros-son"><button class="btn btn--son" aria-label="Réécouter" onclick="jouer('mots/${cible}.mp3')">${ICO.son}</button></div>
      <div class="images" style="margin-top:12px">${o.map(i => `<button data-id="${opts[i]}" aria-label="${E(D.mots[opts[i]].fr)}">${imageMot(D.mots[opts[i]], opts[i])}</button>`).join('')}</div>
      <div id="r"></div>`;
    app.querySelectorAll('.images button').forEach(b => b.onclick = () => {
      if (b.dataset.id === cible) {
        b.classList.add('juste');
        $('#r').innerHTML = `<div class="retro ok">✓ <b>${E(g(D.mots[cible].es))}</b> — ${E(D.mots[cible].fr)}</div>`;
        n++; setTimeout(() => { tour(); if (n < tours.length) setTimeout(() => jouer('mots/' + tours[n] + '.mp3'), 250); }, 1100);
      } else if (!b.classList.contains('faux')) {
        erreurs++; b.classList.add('faux');
        $('#r').innerHTML = `<div class="retro no">Ce n'est pas ça : ceci, c'est <b>${E(g(D.mots[b.dataset.id].es))}</b>. Réécoutez.</div>`;
        jouer('mots/' + b.dataset.id + '.mp3').then(() => setTimeout(() => jouer('mots/' + cible + '.mp3'), 300));
      }
    });
  }
  tour();
  setTimeout(() => jouer('mots/' + tours[0] + '.mp3'), 300);
}

/* 4. ce qu'on me répond */
// Audit tour 1 (F3/D3) : chaque journée rouvre deux réponses des journées
// d'avant — la veille, et une plus ancienne ; l'allergie revient après León.
function rappels(et){
  const i = D.etapes.indexOf(et), out = [];
  const prendre = (src, k) => { if (src && src.ecoute[k]) out.push({src, k}); };
  const leon = D.etapes.find(e => e.id === 'leon');
  if (i >= 1) prendre(D.etapes[i - 1], D.etapes[i - 1] === leon ? 0 : et.n % D.etapes[i - 1].ecoute.length);
  if (i > D.etapes.indexOf(leon)) prendre(leon, et.n % 2 ? 2 : 3);
  else if (i >= 2) { const src = D.etapes[(et.n * 7) % (i - 1)]; prendre(src, (et.n * 3) % src.ecoute.length); }
  return out;
}
function vueRepond(et){
  let n = 0, erreurs = 0;
  const items = [...rappels(et).map(r => ({src:r.src, k:r.k, rappel:true})), ...et.ecoute.map((_, k) => ({src:et, k}))];
  function tour(){
    if (n >= items.length) {
      const nr = items.length - et.ecoute.length;
      app.innerHTML = `${tete(et, 'repond')}<div class="retro ok">✓ ${items.length} réponses comprises${nr ? ', dont ' + nr + ' rappel' + (nr > 1 ? 's' : '') : ''}${erreurs ? ' (' + erreurs + ' erreur' + (erreurs > 1 ? 's' : '') + ')' : ', du premier coup'}.</div>
        <div style="margin-top:12px">${fini(et, 'repond')}</div>`; return;
    }
    const it = items[n], src = it.src, p = D.perso[src.local];
    const [es, choix] = src.ecoute[it.k], fichier = sonDe(`${src.id}/ecoute-${it.k}`, es);
    const o = ordre(choix.length, n + et.n);
    app.innerHTML = `${tete(et, 'repond')}
      <div class="progres"><i style="width:${100 * n / items.length}%"></i></div>
      ${it.rappel ? `<span class="rappel">Rappel · halte ${src.n}, ${E(src.lieu)}</span>` : ''}
      <div class="scene-tete">${p.portrait ? `<img src="${BASE}portraits/${src.local}.jpg?v=${D.v}" alt="">` : ''}
       <div><b>${E(p.nom)}</b><div class="muted" style="font-size:14px">${E(p.qui)}, ${E(p.ou)}</div></div></div>
      <p class="consigne">${E(p.nom)} vous répond, à sa vitesse. Que veut-${p.g === 'f' ? 'elle' : 'il'} dire ?</p>
      <div class="gros-son"><button class="btn btn--son" aria-label="Écouter" onclick="jouer('${fichier}')">${ICO.son}</button></div>
      <div class="choix">${o.map(i => `<button data-i="${i}">${E(g(choix[i][0]))}</button>`).join('')}</div>
      <div id="r"></div>`;
    app.querySelectorAll('.choix button').forEach(b => b.onclick = () => {
      const i = +b.dataset.i;
      if (i === 0) {
        b.classList.add('juste');
        $('#r').innerHTML = `<div class="retro ok">✓ Compris. Ce qu'${p.g === 'f' ? 'elle' : 'il'} a dit : <b>« ${E(g(es))} »</b></div>
          <button class="btn btn--pri btn--large" id="suite">Suivant</button>`;
        $('#suite').onclick = () => { n++; tour(); if (n < items.length) { const x = items[n]; setTimeout(() => jouer(sonDe(`${x.src.id}/ecoute-${x.k}`, x.src.ecoute[x.k][0])), 250); } };
      } else if (!b.classList.contains('faux')) {
        erreurs++; b.classList.add('faux');
        $('#r').innerHTML = `<div class="retro no">${E(g(choix[i][1]))}</div>`;
      }
    });
  }
  tour();
  setTimeout(() => { const x = items[0]; jouer(sonDe(`${x.src.id}/ecoute-${x.k}`, x.src.ecoute[x.k][0])); }, 300);
}

/* 5. je le dis — audit tour 1 (D1/A2) : le modèle ne s'ouvre qu'après une
   tentative (micro, ou « je l'ai dit ») ; le temps n'est « fait » que si la
   moitié des phrases ont été dites, et le tampon l'exige. */
function choixVar(nom){
  for (const e of D.etapes) for (const bloc of ['scene', 'soir']) {
    const k = e[bloc].tours.findIndex(t => t.var === nom && t.choix); if (k < 0) continue;
    const j = e[bloc].tours[k].choix.findIndex(c => c[0] === S.vars[nom]); if (j < 0) return null;
    const es = e[bloc].tours[k].choix[j][0];
    return {es, fr: e[bloc].tours[k].choix[j][1], fichier: sonDe(`${e.id}/${bloc}-${k}-c${j}`, es)};
  }
  return null;
}
// « @alergia » dans une liste de mots = le mot de l'allergie choisie (audit tour 3).
const motId = id => id === '@alergia' ? (algCode() === 'gluten' ? 'sin_gluten' : algCode()) : id;
function allergie(){ return D.alergenos.find(a => a.code === S.alergia) || null; }
function vueDire(et){
  let n = 0, dites = 0;
  const items = et.dire.map((d, i) => {
    const f = d[3] || {}, it = {fr:d[0], es:d[1], cles:d[2], fichier:sonDe(`${et.id}/dire-${i}`, d[1]), oblig:!!f.oblig, dit:false};
    // Audit tour 2 (C2) : le modèle d'une phrase sur soi reprend la réponse
    // choisie plus tôt (le métier, la raison du chemin), avec son son.
    if (f.var && S.vars[f.var]) { const c = choixVar(f.var); if (c) { it.es = c.es; it.fichier = c.fichier; it.exemple = false; } }
    else if (f.perso) it.exemple = true;
    return it;
  });
  function tour(){
    if (n >= items.length) {
      const obligManque = items.filter(x => x.oblig && !x.dit);
      const assez = dites >= Math.ceil(items.length / 2) && !obligManque.length;
      if (assez) jour(et.id).faits.dire = true, sauver();
      app.innerHTML = `${tete(et, 'dire')}<div class="retro ${assez ? 'ok' : 'info'}">${assez ? '✓' : '→'} ${dites} phrase${dites > 1 ? 's' : ''} dite${dites > 1 ? 's' : ''} sur ${items.length}.
        ${assez ? 'Le plus dur est fait : oser.' : obligManque.length ? 'Les phrases de l\u2019allergie ne se passent pas : dites-les à voix haute.' : 'Pour ce temps (et pour le tampon), dites-en au moins la moitié à voix haute.'}</div>
        <div style="margin-top:12px">${assez ? fini(et, 'dire') : `<button class="btn btn--pri btn--large" onclick="rendre()">Recommencer</button>`}</div>`; return;
    }
    const it = items[n];
    let tente = false;
    app.innerHTML = `${tete(et, 'dire')}
      <div class="progres"><i style="width:${100 * n / items.length}%"></i></div>
      <div class="carte"><p class="surtitre">La situation${it.oblig ? ' · obligatoire' : ''}</p><p style="font-size:19px;font-weight:800;color:var(--text-strong);margin:4px 0 0">${E(g(it.fr))}</p></div>
      ${Reco ? `<div class="micro"><button class="btn-micro" id="mic" aria-label="Parler">${ICO.micro}</button>
        <div class="muted" id="micEtat" style="font-size:14px">Touchez le micro, dites-le en espagnol.</div>
        <div class="entendu" id="entendu"></div></div>` : ''}
      <button class="btn btn--large" id="dit" style="margin:6px 0">Je l'ai dit à voix haute</button>
      <div id="r"></div>
      <div class="rangee" style="margin-top:10px"><button class="btn" id="modele" disabled>${ICO.son} Le modèle</button>
       <button class="btn btn--pri" id="suite" style="flex:1" disabled>Suivant</button></div>
      <p class="avis-local" style="margin-top:8px">Le modèle s'ouvre après votre essai : on cherche d'abord, on compare ensuite. <a href="#" id="passer">Passer</a></p>`;
    const zoneR = $('#r');
    const montrerModele = () => { if (!document.body.contains(zoneR)) return; zoneR.insertAdjacentHTML('beforeend', `<div class="retro info"><span class="surtitre">${it.exemple ? 'Un exemple (dites la vôtre)' : 'Le modèle'}</span><div class="phrase-es">${E(g(it.es))}</div></div>`); jouer(it.fichier); };
    const essaye = () => { if (!tente) { tente = true; dites++; it.dit = true; } $('#modele').disabled = false; $('#suite').disabled = false; };
    // Audit tour 3 (M2) : une phrase d'allergie ne compte que DITE JUSTE —
    // reconnue au micro, ou, sans micro, redite après avoir écouté le modèle.
    let redire = false;
    $('#modele').onclick = () => { $('#modele').disabled = true; montrerModele(); };
    $('#suite').onclick = () => { n++; tour(); };
    $('#passer').onclick = e => { e.preventDefault(); n++; tour(); };
    if (it.oblig) $('#passer').parentNode.innerHTML = S.alergia ? 'Cette phrase-ci ne se passe pas : c\u2019est celle de votre allergie.'
      : 'Cette phrase-ci ne se passe pas. Exercice : les noix — choisissez votre allergie dans les réglages.';
    $('#dit').onclick = () => {
      if (!it.oblig) { essaye(); $('#modele').disabled = true; montrerModele(); return; }
      if (!redire) { redire = true; montrerModele(); $('#dit').textContent = 'Je l\u2019ai redite, comme le modèle'; return; }
      essaye(); $('#dit').disabled = true;
    };
    if (Reco) {
      const mic = $('#mic');
      mic.onclick = () => {
        if (recoActive) { arreterMicro(); return; }
        mic.classList.add('ecoute'); mic.innerHTML = ICO.stop; $('#micEtat').textContent = 'Je vous écoute… touchez pour arrêter.';
        ecouterMicro(t => { $('#entendu').textContent = '« ' + t + ' »'; }, final => {
          mic.classList.remove('ecoute'); mic.innerHTML = ICO.micro; $('#micEtat').textContent = 'Touchez le micro pour réessayer.';
          if (!final) { $('#r').innerHTML = `<div class="retro info">${rienEntendu('Je n\u2019ai rien entendu. Vérifiez que le micro est permis, ou dites-le et touchez « Je l\u2019ai dit ».')}</div>`; return; }
          const t = ' ' + plat(final).replace(/ o no$/, '') + ' ';
          const manque = it.cles.map(c => g(c)).filter(c => !c.split('|').some(a => t.includes(' ' + plat(a) + ' ') || t.includes(plat(a))));
          // Audit tour 2 (E1) : « no quedan camas » passait pour « quedan camas ».
          const nonEnTrop = / no /.test(t) && !/ no /.test(' ' + plat(g(it.es)) + ' ');
          $('#r').innerHTML = manque.length ? `<div class="retro no">Presque. Il manque : <b>${manque.map(c => E(c.split('|')[0])).join(', ')}</b>. Comparez avec le modèle, puis réessayez.</div>`
            : nonEnTrop ? `<div class="retro no">Attention : j'ai entendu « no ». Votre phrase dit peut-être le contraire. Comparez avec le modèle.</div>`
            : `<div class="retro ok">✓ ¡Muy bien! On vous a compris.</div>`;
          if (!it.oblig || (!manque.length && !nonEnTrop)) essaye();
          else if (it.oblig) $('#r').insertAdjacentHTML('beforeend', `<div class="retro info">Cette phrase-là doit être dite juste pour compter. Réessayez.</div>`);
          $('#modele').disabled = true; setTimeout(montrerModele, manque.length ? 0 : 600);
        });
      };
    }
  }
  tour();
}

/* 6 et 7. la scène et le soir — le même moteur */
function varTour(tour){
  const nom = (/\{var:(\w+)\}/.exec(tour.es) || [])[1];
  const cles = Object.keys(tour.var), v = S.vars[nom], j = cles.indexOf(v);
  if (j >= 0) return {es: tour.var[cles[j]][0], fr: tour.var[cles[j]][1], base: `-v${j}`};
  if (tour.defaut) return {es: tour.defaut[0], fr: tour.defaut[1], base: '-vd'};
  return {es: tour.var[cles[0]][0], fr: tour.var[cles[0]][1], base: '-v0'};
}
function vueScene(et, bloc){
  const sc = et[bloc], qui = bloc === 'soir' ? 'marta' : sc.qui, p = D.perso[qui];
  let k = 0, aide = S.aide;
  const cleS = et.id + '/' + bloc;
  S.erreurs = S.erreurs || {}; let erreurs = S.erreurs[cleS] || 0;
  // Audit tour 3 (M4) : quel plat contient l'allergène se tire au hasard à la
  // première partie, puis change à chaque reprise.
  const tirage = (jour(et.id).tirage != null) ? jour(et.id).tirage : (jour(et.id).tirage = Math.floor(Math.random() * 2));
  const groupe = ['A', 'B'][(tirage + ((S.essais || {})[cleS] || 0)) % 2];
  const visible = t => t && !(t.siAlergia && !S.alergia) && !(t.sansAlergia && S.alergia) && !(t.groupe && t.groupe !== groupe);
  app.innerHTML = `${tete(et, bloc)}
    <div class="bandeau" style="max-height:170px">${et.vignette ? `<img src="${BASE}etapes/${et.img}.jpg?v=${D.v}" alt="" style="aspect-ratio:auto;height:170px">` : ''}</div>
    <div class="scene-tete" style="margin-top:10px">${p.portrait ? `<img src="${BASE}portraits/${qui}.jpg?v=${D.v}" alt="">` : ''}
      <div><b>${E(sc.titre)}</b><div class="muted" style="font-size:14px">${E(p.nom)} — ${E(p.qui)}</div></div></div>
    ${et.eliminatoire && bloc === 'scene' ? `<div class="regle"><b>Règle de cette scène.</b> ${E(et.eliminatoire)}</div>` : ''}
    <p class="consigne">Écoutez d'abord : le texte de ${E(p.nom)} s'affiche après votre réponse — ou tout de suite avec « Lire », sauf avant une réponse éliminatoire.</p>
    <label class="aide-bascule"><input type="checkbox" id="aide" ${aide ? 'checked' : ''}> Montrer le français sous chaque réplique</label>
    <label class="aide-bascule"><input type="checkbox" id="lent" ${S.lent ? 'checked' : ''}> Voix plus lentes</label>
    <div class="fil" id="fil"></div><div id="zone"></div>`;
  $('#lent').onchange = e => { S.lent = e.target.checked; sauver(); };
  $('#aide').onchange = e => { aide = e.target.checked;
    app.querySelectorAll('.choix small').forEach(x => x.hidden = !aide);
    app.querySelectorAll('.bulle').forEach(b => { if (!b.querySelector('.es').hidden) b.querySelector('.fr').hidden = !aide; }); };
  const fil = $('#fil'), zone = $('#zone');
  let dernier = null;
  const devoiler = b => { if (!b) return; b.querySelector('.es').hidden = false; const l = b.querySelector('.lire'), e = b.querySelector('.ecoute-dabord');
    if (l) l.remove(); if (e) e.remove(); b.querySelector('.vfr').hidden = false; if (aide) b.querySelector('.fr').hidden = false; };
  function bulle(qui2, es, fr, fichier, tel, verrou){
    const pp = D.perso[qui2], moi = qui2 === 'moi';
    const b = document.createElement('div'); b.className = 'bulle ' + (moi ? 'moi' : 'lui');
    const cache = !moi;
    b.innerHTML = `<div class="qui">${!moi && pp.portrait ? `<img class="perso-mini" src="${BASE}portraits/${qui2}.jpg?v=${D.v}" alt="">` : ''}${tel ? ICO.tel : ''}${moi ? 'Vous' : E(pp.nom)}</div>
      ${cache ? `<div class="ecoute-dabord">${verrou ? 'Écoutez bien : la réponse qui suit est éliminatoire.' : 'Écoutez…'}</div>` : ''}
      <div class="es" ${cache ? 'hidden' : ''}>${E(es)}</div><div class="fr" hidden>${E(fr)}</div>
      <div class="outils-b">${fichier && SONS.has(fichier) ? `<button class="reec" aria-label="Réécouter">${ICO.son} Réécouter</button>` : ''}
        ${cache && !verrou ? `<button class="lire">${ICO.oeil} Lire</button>` : ''}<button class="vfr" ${cache ? 'hidden' : ''}>${ICO.oeil} Français</button></div>`;
    if (fichier && SONS.has(fichier)) b.querySelector('.reec').onclick = () => jouer(fichier);
    const l = b.querySelector('.lire'); if (l) l.onclick = () => devoiler(b);
    b.querySelector('.vfr').onclick = () => { const f = b.querySelector('.fr'); f.hidden = !f.hidden; };
    if (!cache && aide) b.querySelector('.fr').hidden = false;
    fil.appendChild(b); b.scrollIntoView({behavior:'smooth', block:'end'});
    if (!moi) dernier = b;
    return b;
  }
  function suivant(){
    zone.innerHTML = '';
    while (k < sc.tours.length && !visible(sc.tours[k])) k++;
    if (k >= sc.tours.length) return terminer();
    const tour = sc.tours[k], base = `${et.id}/${bloc}-${k}`;
    if (tour.dit) {
      let es = tour.es, fr = tour.fr, fichier;
      if (tour.var) { const v = varTour(tour); es = v.es; fr = v.fr; fichier = base + v.base + suf(es) + '.mp3'; }
      else fichier = sonDe(base, es);
      let kk = k + 1; while (kk < sc.tours.length && !visible(sc.tours[kk])) kk++;
      bulle(tour.dit, g(es), g(fr), fichier, tour.tel, !!(sc.tours[kk] && sc.tours[kk].critique));
      k++;
      const suite = sc.tours[kk];
      const continuer = () => setTimeout(suivant, 350);
      if (!suite || suite.dit) {
        zone.innerHTML = `<button class="btn btn--large" id="cont" style="margin-top:12px">Continuer</button>`;
        $('#cont').onclick = () => { lecteur.pause(); suivant(); };
        jouer(fichier);
      } else jouer(fichier).then(continuer);
      return;
    }
    const cleEssai = et.id + '/' + bloc, essais = (S.essais || {})[cleEssai] || 0;
    const n = tour.choix.length, o = (tour.libre ? [...Array(n).keys()] : ordre(n, k + et.n * 3 + (bloc === 'soir' ? 1 : 0) + essais))
      .filter(i => !(tour.choix[i][3] && (tour.choix[i][3].sauf || []).includes(algCode()) && S.alergia));
    zone.innerHTML = `<p class="consigne" style="margin-top:12px">${tour.libre ? 'Toutes les réponses sont justes : choisissez <b>la vôtre</b>.' : 'Que répondez-vous ?'}</p>
      <div class="choix">${o.map(i => `<button data-i="${i}">${E(g(tour.choix[i][0]))}<small ${aide && !tour.critique ? '' : 'hidden'}>${E(g(tour.choix[i][1]))}</small></button>`).join('')}</div>
      ${Reco ? `<div class="micro" style="margin:4px 0"><button class="btn" id="dire">${ICO.micro} Le dire au lieu de toucher</button><div class="entendu" id="entendu"></div></div>` : ''}
      <div id="r"></div>`;
    zone.scrollIntoView({behavior:'smooth', block:'end'});
    if (Reco) $('#dire').onclick = () => {
      const bt = $('#dire');
      if (recoActive) { arreterMicro(); return; }
      bt.innerHTML = ICO.stop + ' Arrêter'; bt.classList.add('btn--son');
      ecouterMicro(t => { $('#entendu').textContent = '« ' + t + ' »'; }, final => {
        bt.innerHTML = ICO.micro + ' Le dire au lieu de toucher'; bt.classList.remove('btn--son');
        if (!final) { $('#r').innerHTML = `<div class="retro info">${rienEntendu('Je n\u2019ai rien entendu. Réessayez, ou touchez votre réponse.')}</div>`; return; }
        // La phrase dite rejoint le choix dont elle partage le plus de mots.
        const dits = new Set(plat(final).split(' '));
        const score = i => { const m = plat(g(tour.choix[i][0])).split(' ').filter(Boolean); return m.filter(w => dits.has(w)).length / Math.max(m.length, 1); };
        const libres = [...zone.querySelectorAll('.choix button')].filter(b => !b.classList.contains('faux')).map(b => +b.dataset.i);
        const best = libres.sort((a, b) => score(b) - score(a))[0];
        if (best == null || score(best) < 0.5) { $('#r').innerHTML = `<div class="retro info">J'ai entendu « ${E(final)} », sans reconnaître une des réponses. Réessayez, ou touchez-la.</div>`; return; }
        zone.querySelector(`.choix button[data-i="${best}"]`).click();
      });
    };
    zone.querySelectorAll('.choix button').forEach(b => b.onclick = () => {
      const i = +b.dataset.i, c = tour.choix[i];
      if (i === 0 || tour.libre) {
        if (tour.var) S.vars[tour.var] = c[0], sauver();
        zone.innerHTML = ''; devoiler(dernier);
        const f = sonDe(`${base}-c${i}`, c[0]);
        bulle('moi', g(c[0]), g(c[1]), f);
        k++; jouer(f).then(() => setTimeout(suivant, 300));
      } else if (!b.classList.contains('faux')) {
        erreurs++; S.erreurs[cleS] = erreurs; sauver(); b.classList.add('faux');
        if (tour.critique) {
          // La reprise ne se fait pas de mémoire de position (D4) : autre graine.
          S.essais = S.essais || {}; S.essais[cleEssai] = essais + 1; sauver();
          devoiler(dernier);
          zone.innerHTML = `<div class="eliminatoire"><b>Arrêt : c'est l'erreur qui coûte cher.</b><p style="margin:6px 0 0">${E(g(c[2]))}</p>
            <button class="btn btn--pri btn--large" style="margin-top:10px" onclick="rendre()">Recommencer la scène</button></div>`;
          return;
        }
        $('#r').innerHTML = `<div class="retro no">${E(g(c[2]))}</div>`;
      }
    });
  }
  function terminer(){
    const j = jour(et.id); j.faits[bloc] = true; S.erreurs[cleS] = 0; sauver();
    const manque = ['repond', 'dire'].filter(x => !j.faits[x]);
    const tamponner = j.faits.scene && j.faits.soir && !manque.length && !j.tampon;
    const manqueDire = j.faits.scene && j.faits.soir && manque.length && !j.tampon;
    const arrets = (S.essais || {})[et.id + '/' + bloc] || 0;
    zone.innerHTML = `<div class="retro ok" style="margin-top:14px">✓ ${bloc === 'soir' ? 'Belle soirée.' : 'Scène réussie' + (arrets ? ', au ' + (arrets + 1) + '<sup>e</sup> essai' : '') + '.'} ${erreurs ? erreurs + ' essai' + (erreurs > 1 ? 's' : '') + ' de trop, et c’est ainsi qu’on apprend.' : 'Sans une erreur !'}</div>
      ${tamponner ? `<button class="btn btn--pri btn--large" id="tamp">Faire tamponner ma credencial</button>` :
        manqueDire ? `<div class="retro info">Pour le tampon, il reste : ${manque.map(x => TEMPS.find(t => t[0] === x)[1]).join(' et ')}.</div><button class="btn btn--pri btn--large" onclick="aller('jour/${et.id}/${manque[0]}')">${TEMPS.find(t => t[0] === manque[0])[1]}</button>` : fini(et, bloc)}`;
    if (tamponner) $('#tamp').onclick = () => poserTampon(et);
  }
  setTimeout(suivant, 200);
}
function poserTampon(et){
  const j = jour(et.id); j.tampon = aujourdhui(); sauver();
  const v = document.createElement('div'); v.className = 'voile';
  v.innerHTML = `<div class="tampon-anim" style="--rot:${((et.n * 37) % 17) - 8}deg">${tampon(et, j.tampon)}</div>
    <h1 style="margin-top:18px">${E(et.lieu)}</h1><p class="muted">Tampon ${et.n} sur 10${et.n === 10 ? ' — ¡Enhorabuena!' : ''}</p>
    <button class="btn btn--pri" id="ok">${et.n === 10 ? 'Ma Compostela' : 'Retour à la credencial'}</button>`;
  document.body.appendChild(v);
  $('#ok').onclick = () => { v.remove(); aller(et.n === 10 ? 'compostela' : 'accueil'); };
}

/* ---------- la conversation libre, avec l'assistant ----------
   /api/jeu-de-role, scénario « camino-es-fr » : la personne du lieu, ou Marta.
   La réponse est dite par la voix espagnole du téléphone (speechSynthesis
   es-ES) : les voix Azure du serveur ne connaissent pas encore ces gens-là. */
const CLE_CODE = 'compostelle:code';
function voixEs(t){
  try {
    speechSynthesis.cancel();
    const u = new SpeechSynthesisUtterance(t); u.lang = 'es-ES'; u.rate = S.lent ? .8 : .95;
    const v = speechSynthesis.getVoices().find(x => x.lang === 'es-ES') || speechSynthesis.getVoices().find(x => /^es/.test(x.lang));
    if (v) u.voice = v;
    speechSynthesis.speak(u);
  } catch(e) {}
}
function vueLibre(et){
  let code = ''; try { code = localStorage.getItem(CLE_CODE) || ''; } catch(e) {}
  let qui = et.local, palier = 'lent';
  const choixQui = () => [et.local, 'marta'].map(k => `<button class="btn ${qui === k ? 'btn--pri' : ''}" data-qui="${k}">${E(D.perso[k].nom)}</button>`).join('');
  const choixPal = () => [['lent', 'Lentement'], ['normal', 'Normalement'], ['rapide', 'Comme en Espagne']].map(([k, t]) => `<button class="btn btn--petit ${palier === k ? 'btn--pri' : ''}" data-pal="${k}">${t}</button>`).join('');
  function accueil(err){
    app.innerHTML = `${retour('jour/' + et.id, 'Halte ' + et.n + ' · ' + et.lieu)}<p class="surtitre">Avec l'assistant</p><h1>Parler librement</h1>
      <p class="muted">La même situation, mais la personne vous répond vraiment : dites ce que vous voulez, comme vous pouvez. Il faut du réseau.</p>
      <h3>À qui parler</h3><div class="rangee" id="qui">${choixQui()}</div>
      <h3>Comment on vous parle</h3><div class="rangee" id="pal">${choixPal()}</div>
      <h3>Votre code</h3><input id="code" value="${E(code)}" autocomplete="off" autocapitalize="characters" style="font:inherit;font-size:20px;letter-spacing:.2em;padding:10px;border-radius:10px;border:1px solid var(--line-300);width:10em;text-transform:uppercase">
      <div id="compte"></div>
      <p class="avis-local">Le code de votre achat, ou celui de votre groupe. Il ouvre l'assistant ; il ne dit pas qui vous êtes.</p>
      ${err ? `<div class="retro no">${E(err)}</div>` : ''}
      <button class="btn btn--pri btn--large" id="go" style="margin-top:10px">Commencer</button>
      <div id="offre"></div>`;
    afficherCompte(code); afficherOffre(!code);
    $('#qui').onclick = e => { const b = e.target.closest('[data-qui]'); if (b) { qui = b.dataset.qui; $('#qui').innerHTML = choixQui(); } };
    $('#pal').onclick = e => { const b = e.target.closest('[data-pal]'); if (b) { palier = b.dataset.pal; $('#pal').innerHTML = choixPal(); } };
    $('#go').onclick = () => { code = $('#code').value.trim().toUpperCase(); try { localStorage.setItem(CLE_CODE, code); } catch(e) {} conversation(); };
  }
  function conversation(){
    const cas = qui === 'marta' ? 'marta-' + et.id : et.id, p = D.perso[qui], hist = [];
    let fini = false;
    app.innerHTML = `${retour('jour/' + et.id, 'Halte ' + et.n + ' · ' + et.lieu)}
      <div class="scene-tete">${p.portrait ? `<img src="${BASE}portraits/${qui}.jpg?v=${D.v}" alt="">` : ''}<div><b>${E(p.nom)}</b><div class="muted" style="font-size:14px">${E(qui === 'marta' ? et.soir.titre : et.scene.titre)}</div></div></div>
      <div class="fil" id="fil"></div>
      <div id="saisie" style="margin-top:12px">
        ${Reco ? `<div class="micro"><button class="btn-micro" id="mic" aria-label="Parler">${ICO.micro}</button><div class="entendu" id="entendu"></div></div>` : ''}
        <div class="rangee"><input id="txt" placeholder="…ou écrivez en espagnol" style="flex:1;min-width:0;font:inherit;padding:10px;border-radius:10px;border:1px solid var(--line-300)">
        <button class="btn btn--pri" id="env">Envoyer</button></div>
        <button class="btn btn--large" id="fin" style="margin-top:10px">Terminer et voir le bilan</button></div><div id="r"></div>`;
    const fil = $('#fil');
    const bulle = (moi, t) => { const b = document.createElement('div'); b.className = 'bulle ' + (moi ? 'moi' : 'lui');
      b.innerHTML = `<div class="qui">${moi ? 'Vous' : E(p.nom)}</div><div class="es">${E(t)}</div>`; fil.appendChild(b); b.scrollIntoView({behavior:'smooth', block:'end'}); };
    async function tour(texte){
      if (texte) { hist.push({role:'user', contenu:texte}); bulle(true, texte); }
      const att = document.createElement('div'); att.className = 'muted'; att.textContent = p.nom + ' réfléchit…'; fil.appendChild(att);
      try {
        const r = await fetch('/api/jeu-de-role', {method:'POST', headers:{'Content-Type':'application/json'},
          body: JSON.stringify({code, scenario:'camino-es-fr', cas, role:'pelerin', niveau:palier, historique:hist})});
        const d = await r.json().catch(() => ({})); att.remove();
        if (!r.ok) {
          if (r.status === 401) return accueil('Ce code n’est pas accepté.');
          if (d.pelerin && (r.status === 402 || r.status === 429)) { att.remove(); return accueil(d.error); }
          $('#r').innerHTML = `<div class="retro no">${E(d.error || 'Erreur')}</div>`; return; }
        if (d.pelerin) memoCompte(d.pelerin);
        if (d.ouverture) { hist.unshift({role:'user', contenu:d.ouverture}); bulle(true, d.ouverture); }
        let t = String(d.reponse || ''); fini = /\bFIN\s*$/.test(t); t = t.replace(/\bFIN\s*$/, '').trim();
        hist.push({role:'assistant', contenu:t}); bulle(false, t); voixEs(t);
        if (fini) bilan();
      } catch(e) { att.remove(); $('#r').innerHTML = `<div class="retro no">Pas de réseau ? L’assistant a besoin d’une connexion.</div>`; }
    }
    const envoyer = () => { const t = $('#txt').value.trim(); if (t && !fini) { $('#txt').value = ''; tour(t); } };
    $('#env').onclick = envoyer; $('#txt').onkeydown = e => { if (e.key === 'Enter') envoyer(); };
    $('#fin').onclick = () => bilan();
    if (Reco) $('#mic').onclick = () => {
      const mic = $('#mic'); if (recoActive) { arreterMicro(); return; }
      try { speechSynthesis.cancel(); } catch(e) {}
      mic.classList.add('ecoute'); mic.innerHTML = ICO.stop;
      ecouterMicro(t => { $('#entendu').textContent = '« ' + t + ' »'; }, final => {
        mic.classList.remove('ecoute'); mic.innerHTML = ICO.micro; $('#entendu').textContent = '';
        if (final && !fini) tour(final);
      });
    };
    async function bilan(){
      fini = true; $('#saisie').innerHTML = `<div class="muted">Le bilan arrive…</div>`;
      try {
        const r = await fetch('/api/jeu-de-role', {method:'POST', headers:{'Content-Type':'application/json'},
          body: JSON.stringify({code, scenario:'camino-es-fr', cas, role:'pelerin', bilan:true, historique:hist.slice(1)})});
        const d = await r.json().catch(() => ({})), b = d.bilan;
        if (!r.ok || !b) { $('#saisie').innerHTML = `<div class="retro no">${E(d.error || 'Pas de bilan cette fois.')}</div>`; return; }
        $('#saisie').innerHTML = `<h2>Le bilan</h2>
          ${b.resume ? `<div class="retro ok">${E(b.resume)}</div>` : ''}
          ${(b.compris || []).length ? `<h3>Ce que vous avez obtenu</h3><ul>${b.compris.map(x => `<li>${E(x)}</li>`).join('')}</ul>` : ''}
          ${(b.phrases || []).length ? `<h3>À dire autrement</h3>${b.phrases.map(x => `<div class="carte" style="margin:6px 0"><div class="muted">${E(x.dit)}</div><div class="phrase-es" style="font-size:18px">${E(x.mieux)}</div></div>`).join('')}` : ''}
          ${b.conseil ? `<div class="retro info">${E(b.conseil)}</div>` : ''}
          <button class="btn btn--pri btn--large" onclick="aller('jour/${et.id}')">Retour à la halte</button>`;
      } catch(e) { $('#saisie').innerHTML = `<div class="retro no">Pas de réseau pour le bilan.</div>`; }
    }
    tour('');
  }
  accueil();
}

/* ---------- l'accès payant à « Parler librement » ---------- */
/* Formule B de assets/presentations/compostelle-prix.html, décidée le 26 sept.
   2026 : le chemin est gratuit, seul l'assistant se paie. Le serveur fait foi
   sur le prix et les limites (/api/pelerins/offre) ; la page ne les écrit pas. */
const estPelerin = c => /^PC[A-Z2-9]{6}$/.test(c || '');
const dollars = c => (c / 100).toLocaleString('fr-CA', {style:'currency', currency:'CAD'});
const dateFr = iso => { const [a, m, j] = String(iso).split('-').map(Number); return a ? new Date(a, m - 1, j).toLocaleDateString('fr-CA', {day:'numeric', month:'long', year:'numeric'}) : ''; };
let OFFRE = null;
async function offreServeur(){
  if (OFFRE) return OFFRE;
  try { const r = await fetch('/api/pelerins/offre'); if (r.ok) OFFRE = await r.json(); } catch(e) {}
  return OFFRE;
}
function memoCompte(etat){ try { localStorage.setItem('compostelle:compte', JSON.stringify(etat)); } catch(e) {} }
async function afficherCompte(code){
  const z = $('#compte'); if (!z || !estPelerin(code)) return;
  let e = null;
  try { const r = await fetch('/api/pelerins/etat?code=' + encodeURIComponent(code)); if (r.ok) e = await r.json(); } catch(x) {}
  if (!e) { try { e = JSON.parse(localStorage.getItem('compostelle:compte') || 'null'); } catch(x) {} }
  if (!e || !$('#compte')) return;
  memoCompte(e);
  const expire = e.expire && e.expire < new Date().toISOString().slice(0, 10);
  $('#compte').innerHTML = `<div class="retro ${e.restant && !expire ? 'info' : 'no'}" style="margin-top:8px">${
    expire ? `Votre accès a pris fin le ${dateFr(e.expire)}.` :
    `Il vous reste <b>${e.restant} conversation${e.restant > 1 ? 's' : ''}</b>, jusqu'au ${dateFr(e.expire)}.`}</div>`;
  const o = await offreServeur();
  if (o && o.ouverte && !expire && e.restant <= 10)
    $('#compte').insertAdjacentHTML('beforeend', `<button class="btn btn--large" id="recharger" style="margin-top:6px">Ajouter ${o.rechargeConversations} conversations — ${dollars(o.recharge)}</button>`);
  if (o && o.ouverte && expire) afficherOffre(true);
  const b = $('#recharger'); if (b) b.onclick = () => acheter(code);
}
async function afficherOffre(ouvrir){
  const o = await offreServeur(), z = $('#offre');
  if (!z || !o || !o.ouverte) return;
  z.innerHTML = `<details class="rub" style="margin-top:16px"${ouvrir ? ' open' : ''}><summary>Pas encore de code ? <span>${dollars(o.prix)}</span></summary>
    <div style="padding:0 14px 14px;font-size:15.5px">
     <p style="margin:0 0 8px"><b>${o.conversations} conversations</b> avec les gens du chemin, pendant <b>${Math.round(o.jours / 30.4)} mois</b> :
     la même personne qu'à l'étape, qui vous répond vraiment, puis un bilan en français.</p>
     <p class="muted" style="font-size:14px;margin:0 0 10px">Les dix haltes, la trousse et le test restent gratuits. Paiement par carte chez Stripe ;
     nous ne recevons ni votre nom ni votre carte. Le code s'affiche ici tout de suite, et il est aussi écrit sur votre reçu.</p>
     <button class="btn btn--pri btn--large" id="acheter">Obtenir mon code — ${dollars(o.prix)}</button></div></details>`;
  $('#acheter').onclick = () => acheter(null);
}
async function acheter(recharge){
  const b = document.activeElement; if (b && b.tagName === 'BUTTON') { b.disabled = true; b.textContent = 'Vers le paiement…'; }
  try {
    const r = await fetch('/api/pelerins/achat', {method:'POST', headers:{'Content-Type':'application/json'}, body: JSON.stringify(recharge ? {recharge} : {})});
    const d = await r.json().catch(() => ({}));
    if (r.ok && d.url) {
      try { sessionStorage.setItem('compostelle:retour', location.hash); } catch(e) {}
      location.href = d.url; return;
    }
    alert(d.error || 'Le paiement ne s’ouvre pas. Réessayez dans un moment.');
  } catch(e) { alert('Pas de réseau : le paiement demande une connexion.'); }
  if (b && b.tagName === 'BUTTON') { b.disabled = false; b.textContent = 'Réessayer'; }
}
function suiteApresAchat(){
  let h = ''; try { h = sessionStorage.getItem('compostelle:retour') || ''; } catch(e) {}
  if (/^#jour\/[^/]+\/libre$/.test(h)) return h.slice(1);
  const et = prochaine() || D.etapes[0]; return 'jour/' + et.id + '/libre';
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
  if (!d) { $('#z').innerHTML = `<div class="retro no">${E(err || 'Le paiement n’est pas encore confirmé.')} Si vous avez payé, votre code est écrit sur le reçu reçu par courriel ; entrez-le dans « Parler librement ».</div>
    <button class="btn btn--large" onclick="location.reload()">Vérifier de nouveau</button>`; return; }
  try { localStorage.setItem(CLE_CODE, d.code); } catch(e) {}
  memoCompte(d);
  $('#z').innerHTML = `<p>Voici votre code. Il est gardé dans ce téléphone ; notez-le quand même, pour un autre appareil (il est aussi sur votre reçu).</p>
    <div class="code-achat" id="lecode">${E(d.code)}</div>
    <div class="rangee" style="justify-content:center"><button class="btn" id="copier">Copier le code</button></div>
    <div class="retro ok" style="margin-top:12px">✓ ${d.restant} conversations, jusqu'au ${dateFr(d.expire)}.</div>
    <button class="btn btn--pri btn--large" style="margin-top:10px" onclick="aller('${suiteApresAchat()}')">Parler librement</button>`;
  $('#copier').onclick = async () => { try { await navigator.clipboard.writeText(d.code); $('#copier').textContent = 'Copié'; } catch(e) {} };
}
function vueAchatAnnule(){
  app.innerHTML = `${retour('accueil', 'La credencial')}<h1>Paiement annulé</h1>
    <div class="retro info">Rien n'a été facturé. Le chemin reste ouvert : les dix haltes, la trousse et le test ne demandent aucun code.</div>
    <button class="btn btn--pri btn--large" onclick="aller('${suiteApresAchat()}')">Revenir à « Parler librement »</button>`;
}

/* ---------- avant de partir : huit séances et « Prêt à partir ? » ---------- */
/* Décisions de Daniel du 26 sept. 2026 (compostelle-preparation-plan.html) :
   conseillées, jamais verrouillées ; un encadré « la mécanique » par séance ;
   un test qui situe. Le contenu : build/contenu/compostelle/preparation.py.
   Révisé au tour 1 de la boucle didactique (27 sept.) : voir compostelle-audit.html. */
// « La leçon » d'abord : quelqu'un explique avant qu'on joue (Daniel, 27 sept. 2026).
const PREP_TEMPS = [...(D.prep.lecons && Object.keys(D.prep.lecons).length ? [['lecon', 'La leçon', 'On vous explique, en une ou deux minutes']] : []),
                    ['ecoute', 'J’écoute', 'Les phrases et les mots, avec leur voix'],
                    ['quiz', 'Je reconnais', 'J’entends, je choisis'],
                    ['dire', 'Je le dis', 'Au micro, puis le modèle']];
// La séance qui outille chaque halte (audit tour 1, D1/F3).
const OUTILLE = {'roncesvalles': ['p4', 'p3'], 'pamplona': ['p5', 'p3'], 'puente-la-reina': ['p8', 'p2'], 'logrono': ['p5'], 'burgos': ['p8', 'p6'],
                 'carrion': ['p7'], 'leon': ['p7', 'p8'], 'sarria': ['p3'], 'santiago': ['p7']};
function prepEtat(id){ if (!S.prep) S.prep = {}; return S.prep[id] || (S.prep[id] = {faits:{}, fin:null}); }
const seanceParId = id => D.prep.seances.find(x => x.id === id);
const prepFaites = () => D.prep.seances.filter(x => prepEtat(x.id).fin).length;
const prepProchaine = () => D.prep.seances.find(x => !prepEtat(x.id).fin) || null;
const numSeance = x => D.prep.seances.indexOf(x) + 1;
/* Le sac (Daniel, 27 sept. 2026) : avant le Camino on prépare son sac et on
   s'entraîne ; chaque entraînement y met un objet. Le croquis de l'objet vient
   du lexique ; il se colore quand l'entraînement est fait. */
const SAC = {p1: ['botas', 'les chaussures', 'la base : tout repose dessus'],
             p2: ['concha', 'la coquille', 'le signe du pèlerin : elle ouvre les portes'],
             p3: ['efectivo', 'le porte-monnaie', 'payer, et comprendre le prix'],
             p4: ['horario', "l'horloge", 'ne pas trouver la porte fermée'],
             p5: ['baston', 'le bâton', 'on s’appuie dessus pour tout'],
             p6: ['flecha', 'la flèche', 'trouver ce qu’on cherche'],
             p7: ['credencial', 'la credencial', 'qui vous êtes, d’où vous venez'],
             p8: ['chubasquero', "l'imperméable", 'prêt pour la réponse qui tombe']};
function sacGrille(petit){
  const pro = prepProchaine();
  return `<div class="sac${petit ? ' sac--petit' : ''}"><div class="sac-dos"><img src="${BASE}croquis/mochila.jpg?v=${D.v}" alt="">
    <b>${prepFaites()} / ${D.prep.seances.length}</b><small>dans le sac</small></div><div class="sac-objets">${
    D.prep.seances.map((x, i) => { const o = SAC[x.id] || ['mochila', '', ''], fait = !!prepEtat(x.id).fin, cour = !fait && pro && pro.id === x.id;
      return `<button class="sac-o${fait ? ' dans' : ''}${cour ? ' courant' : ''}" onclick="aller('prep/${x.id}')" aria-label="Entraînement ${i + 1} : ${E(x.titre)}${fait ? ', fait' : ''}">
        <span class="sac-img"><img src="${BASE}croquis/${o[0]}.jpg?v=${D.v}" alt="" loading="lazy">${fait ? '<i aria-hidden="true">✓</i>' : ''}</span>
        <span class="sac-n">${i + 1}</span><b>${E(x.titre)}</b><small>${E(o[1])}${petit ? '' : ' — ' + E(o[2])}</small></button>`; }).join('')}</div></div>`;
}
function vuePrep(){
  const n = prepFaites(), pro = prepProchaine();
  const liste = D.prep.seances.map((x, i) => { const e = prepEtat(x.id);
    return `<li class="${e.fin ? 'fait' : ''}"><button onclick="aller('prep/${x.id}')"><span class="num">${e.fin ? '✓' : i + 1}</span>
      <span><b>${E(x.titre)}</b><span class="d">${E(D.prep.objectifs[x.obj])} · ${x.minutes} min</span></span>${e.fin ? '<span class="etat">✓ faite</span>' : ''}</button></li>`; }).join('');
  const t = (S.prep && S.prep.test) || {};
  app.innerHTML = `${retour('accueil', 'Accueil')}<p class="surtitre">1 · Avant de partir · ${n} sur ${D.prep.seances.length} dans le sac</p>
  <h1>Préparer mon sac</h1>
  <p>Avant le Camino, on prépare son sac et on s'entraîne à marcher. Pour l'espagnol, c'est pareil : huit entraînements de quinze minutes,
  à faire dans l'ordre, dans les semaines qui précèdent le départ. Chacun met un outil dans votre sac — les sons, les nombres, l'heure,
  quatre verbes, les questions — et vous le ressortirez, étape après étape, sur le chemin.</p>
  ${sacGrille()}
  <div class="retro info">Elles sont conseillées, pas obligatoires : le chemin reste ouvert, et vous pouvez y revenir quand vous voulez.</div>
  ${pro ? `<button class="btn btn--pri btn--large" style="margin:6px 0 4px" onclick="aller('prep/${pro.id}')">${n ? 'Continuer' : 'Commencer'} : ${E(pro.titre)}</button>` : ''}
  <ul class="etapes-j">${liste}</ul>
  <h2>La marche d'essai : « Prêt${S.genre === 'f' ? 'e' : ''} à partir ? »</h2>
  <p class="muted">${D.prep.test[0].length} questions, dont ${D.prep.test[0].filter(it => it.type === 'oral').length} au micro, pour savoir où vous en êtes après les entraînements. Il vous situe, il ne vous note pas.
  Refaites-le la veille du départ : ce sera l'autre forme.${t.dernier ? ' Dernier passage : ' + E(t.dernier) + '.' : ''}</p>
  <button class="btn btn--large" onclick="aller('prep/test')">${ICO.test} Faire la marche d'essai</button>
  <p class="avis-local" style="margin-top:10px">À ne pas confondre avec « Suis-je prêt${S.genre === 'f' ? 'e' : ''} ? », le test du chemin, à faire après les haltes.</p>
  <button class="btn btn--pri btn--large" style="margin-top:14px" onclick="aller('accueil')">Aller au chemin</button>`;
}
function teteSeance(x, k){
  const i = PREP_TEMPS.findIndex(t => t[0] === k);
  return `${retour('prep/' + x.id, 'Entraînement ' + numSeance(x) + ' · ' + x.titre)}<p class="surtitre">${i + 1} / ${PREP_TEMPS.length}</p><h1>${PREP_TEMPS[i][1]}</h1>`;
}
function finTemps(x, k){
  const e = prepEtat(x.id); e.faits[k] = true;
  if (PREP_TEMPS.every(([t]) => e.faits[t]) && !e.fin) e.fin = aujourdhui();
  sauver();
  const suivant = PREP_TEMPS.find(([t]) => !e.faits[t]);
  if (suivant) return `<button class="btn btn--pri btn--large" onclick="aller('prep/${x.id}/${suivant[0]}')">Suivant : ${suivant[1]}</button>`;
  const pro = prepProchaine();
  return `<div class="retro ok">✓ Entraînement terminé : ${SAC[x.id] ? E(SAC[x.id][1]) + ' dans le sac. ' : ''}${prepFaites()} sur ${D.prep.seances.length}.</div>
    ${pro ? `<button class="btn btn--pri btn--large" onclick="aller('prep/${pro.id}')">Entraînement suivant : ${E(pro.titre)}</button>` :
      `<button class="btn btn--pri btn--large" onclick="aller('prep/test')">Les huit sont faites : le test de la maison</button>`}
    <button class="btn btn--large" style="margin-top:8px" onclick="aller('prep')">Mon sac</button>`;
}
function vueSeance(id, k){
  const x = seanceParId(id); if (!x) return vuePrep();
  if (k === 'lecon') return seanceLecon(x);
  if (k === 'ecoute') return seanceEcoute(x);
  if (k === 'quiz') return seanceQuiz(x);
  if (k === 'dire') return seanceDire(x);
  const e = prepEtat(x.id);
  const liste = PREP_TEMPS.map(([t, nom, d], j) => `<li class="${e.faits[t] ? 'fait' : ''}"><button onclick="aller('prep/${x.id}/${t}')"><span class="num">${e.faits[t] ? '✓' : j + 1}</span>
    <span><b>${nom}</b><span class="d">${d}</span></span>${e.faits[t] ? '<span class="etat">✓ fait</span>' : ''}</button></li>`).join('');
  const suivant = PREP_TEMPS.find(([t]) => !e.faits[t]) || PREP_TEMPS[0];
  app.innerHTML = `${retour('prep', 'Avant de partir')}<p class="surtitre">Entraînement ${numSeance(x)} sur ${D.prep.seances.length} · ${x.minutes} minutes</p>
    <h1>${E(x.titre)}</h1><p>${E(x.intro)}</p>
    <div class="objectif">${E(D.prep.fin[x.obj])}</div>
    <div class="meca"><p class="surtitre">La mécanique</p><ul>${x.meca.map(t => `<li>${g(t)}</li>`).join('')}</ul></div>
    <button class="btn btn--pri btn--large" onclick="aller('prep/${x.id}/${suivant[0]}')">${e.fin ? 'Refaire' : Object.keys(e.faits).length ? 'Continuer' : 'Commencer'} : ${suivant[1]}</button>
    <ul class="etapes-j">${liste}</ul>`;
}
/* La leçon narrée : la guide explique, la voix d'Espagne dit les exemples ; le
   texte suit l'écoute. Le temps est fait quand on a écouté jusqu'au bout — ou
   qu'on a choisi de lire (sans son, malentendant). */
const blobLecon = {};
function seanceLecon(x){
  const L = D.prep.lecons[x.id];
  if (!L) { prepEtat(x.id).faits.lecon = true; sauver(); return aller('prep/' + x.id + '/ecoute'); }
  const mmss = t => Math.floor(t / 60) + ':' + String(Math.floor(t % 60)).padStart(2, '0');
  const texte = L.segs.map(([l, t], k) => l === 'es'
    ? `<p class="l-seg l-es" data-k="${k}" lang="es">${E(t)}</p>` : `<p class="l-seg" data-k="${k}">${E(t)}</p>`).join('');
  app.innerHTML = `${teteSeance(x, 'lecon')}
    <p class="consigne">Écoutez d'abord : on vous explique la mécanique, avec des exemples. Environ ${Math.max(1, Math.round(L.duree / 60))} minute${Math.round(L.duree / 60) > 1 ? 's' : ''}.</p>
    <div class="carte l-lecteur">
      <button class="btn btn--pri l-jouer" id="lJouer">${ICO.son} Écouter la leçon</button>
      <div class="l-barre" aria-hidden="true"><span id="lPlein"></span></div>
      <div class="muted l-temps"><span id="lT">0:00</span> / ${mmss(L.duree)}</div>
    </div>
    <div class="carte l-texte" id="lTexte">${texte}</div>
    <div id="finLecon" style="margin-top:16px"><button class="btn btn--pri btn--large" id="lFini" disabled>J'ai écouté la leçon</button>
      <p class="muted" style="font-size:14px;margin:8px 0 0">Pas de son ? <button class="lien-btn" id="lLire">J'ai lu le texte</button></p></div>`;
  const segs = [...app.querySelectorAll('.l-seg')];
  let joue = false, fini = false;
  const maj = () => {
    const t = lecteur.currentTime || 0;
    $('#lT').textContent = mmss(t); $('#lPlein').style.width = Math.min(100, t / L.duree * 100) + '%';
    let k = 0; L.debuts.forEach((d, j) => { if (t >= d - 0.05) k = j; });
    segs.forEach((el, j) => el.classList.toggle('actif', joue && j === k));
    if (t >= L.duree * 0.92) finir();
  };
  const finir = () => { if (fini) return; fini = true; const b = $('#lFini'); if (b) b.disabled = false; };
  $('#lJouer').onclick = () => {
    if (!joue) {
      // Le fichier entier en mémoire : le serveur ne sert pas les plages
      // (Range), et sans elles on ne peut pas revenir à une phrase touchée.
      arreterMicro(); lecteur.pause(); joue = true; $('#lJouer').textContent = 'Chargement…';
      const url = BASE + 'sons/prep/' + x.id + '/lecon.mp3?v=' + D.v;
      (blobLecon[url] ? Promise.resolve(blobLecon[url]) : fetch(url).then(r => r.blob()).then(b => blobLecon[url] = URL.createObjectURL(b)))
        .catch(() => url).then(src => {
          if (!document.body.contains(segs[0])) return;
          lecteur.src = src; lecteur.playbackRate = 1; lecteur.ontimeupdate = maj;
          lecteur.onended = () => { maj(); finir(); $('#lJouer').innerHTML = ICO.son + ' Réécouter'; joue = false; };
          lecteur.play().catch(() => {}); $('#lJouer').textContent = 'Pause'; });
    } else if (lecteur.paused) { lecteur.play().catch(() => {}); $('#lJouer').textContent = 'Pause'; }
    else { lecteur.pause(); $('#lJouer').innerHTML = ICO.son + ' Reprendre'; }
  };
  segs.forEach((el, j) => el.onclick = () => { if (!joue) return; lecteur.currentTime = L.debuts[j]; if (lecteur.paused) { lecteur.play().catch(() => {}); $('#lJouer').textContent = 'Pause'; } });
  $('#lLire').onclick = () => { finir(); $('#lFini').click(); };
  $('#lFini').onclick = () => { lecteur.pause(); lecteur.ontimeupdate = null; $('#finLecon').innerHTML = finTemps(x, 'lecon'); };
}
function seanceEcoute(x){
  // Audit tour 1 (G2) : le temps n'est fait qu'une fois chaque phrase écoutée.
  const entendues = new Set();
  const lignes = x.ecoute.map(([es, fr], k) => `<div class="ph"><button class="btn btn--son" aria-label="Écouter" data-k="${k}" data-f="${sonDe('prep/' + x.id + '/e' + k, es)}">${ICO.son}</button>
    <div class="t"><b lang="es">${E(g(es))}</b><span class="sens" ${S.aide ? '' : 'hidden'}>${E(g(fr))}</span></div></div>`).join('');
  app.innerHTML = `${teteSeance(x, 'ecoute')}
    <p class="consigne">Touchez le haut-parleur : vous entendez la phrase, et son sens apparaît. Répétez-la à voix haute, deux fois.</p>
    <div class="carte liste-ecoute">${lignes}</div>
    <h2>Les mots, en images</h2><p class="consigne">Des mots que vous retrouverez sur le chemin.</p>
    <div class="grille">${x.mots.map(id => carteMot(id)).join('')}</div>
    <div id="finEcoute" style="margin-top:16px"><button class="btn btn--pri btn--large" id="jaiEcoute" disabled>J'ai tout écouté (0 sur ${x.ecoute.length})</button></div>`;
  app.querySelectorAll('.liste-ecoute .btn--son').forEach(b => b.onclick = () => {
    jouer(b.dataset.f); b.closest('.ph').querySelector('.sens').hidden = false; entendues.add(b.dataset.k);
    const bt = $('#jaiEcoute'); if (!bt) return; bt.textContent = entendues.size >= x.ecoute.length ? 'J’ai tout écouté' : `J'ai tout écouté (${entendues.size} sur ${x.ecoute.length})`;
    bt.disabled = entendues.size < x.ecoute.length; });
  $('#jaiEcoute').onclick = () => { $('#finEcoute').innerHTML = finTemps(x, 'ecoute'); };
}
/* Une question à choix, jouée jusqu'à la bonne réponse : chaque mauvais choix
   dit pourquoi (E1), et la place de la bonne tourne (D4). */
function questionPrep(it, fichier, graine, surFin, rappel, une){
  const p = it.qui ? D.perso[it.qui] : null, estEs = it.type !== 'rep';
  const o = ordre(it.choix.length, graine);
  let erreurs = 0, fini = false;
  const titre = it.type === 'rep' ? 'Que veut dire la phrase ?' : it.type === 'mot' ? (it.q || 'Quel mot entendez-vous ?') : 'Que dites-vous ?';
  const haut = it.type === 'dire' ? `<div class="carte"><p style="font-size:18px;font-weight:800;margin:0">${E(g(it.fr))}</p></div>`
    : `${p ? `<div class="scene-tete">${p.portrait ? `<img src="${BASE}portraits/${it.qui}.jpg?v=${D.v}" alt="">` : ''}<div><b>${E(p.nom)}</b><div class="muted" style="font-size:14px">${E(p.qui)}</div></div></div>` : ''}
       <div class="gros-son"><button class="btn btn--son" aria-label="Réécouter" id="rejouer">${ICO.son}</button></div>`;
  const html = `${rappel ? `<span class="rappel">${E(rappel)}</span>` : ''}${une ? '<span class="rappel">Une seule écoute, comme au comptoir</span>' : ''}<h2 style="margin-top:6px">${titre}</h2>${haut}
    <div class="choix">${o.map(i => `<button data-i="${i}" ${estEs ? 'lang="es"' : ''}>${E(g(it.choix[i][0]))}</button>`).join('')}</div><div id="r"></div>`;
  function brancher(){
    if ($('#rejouer')) {
      const jouerUne = () => { if (une) $('#rejouer').disabled = true; jouer(fichier, une).then(ok => { if (!ok && une) $('#rejouer').disabled = false; }); };
      $('#rejouer').onclick = jouerUne; setTimeout(jouerUne, 250); }
    app.querySelectorAll('.choix button').forEach(b => b.onclick = () => {
      if (fini || b.disabled) return; const i = +b.dataset.i;
      if (i === 0) {
        fini = true; b.classList.add('juste');
        $('#r').innerHTML = `<div class="retro ok">✓ ${it.type === 'rep' ? '« ' + E(g(it.es)) + ' »' : it.type === 'dire' ? 'C’est bien ce qu’il faut dire.' : 'Bien entendu.'}</div>`;
        if (it.type === 'dire') jouer(fichier);
        surFin(erreurs);
      } else { erreurs++; b.classList.add('faux'); b.disabled = true;
        $('#r').innerHTML = `<div class="retro no">${E(g(it.choix[i][1]))} Essayez encore.</div>`; }
    });
  }
  return [html, brancher];
}
function seanceQuiz(x){
  // Audit tour 1 (D1/F3) : deux questions de la séance précédente ouvrent le quiz.
  const idx = D.prep.seances.indexOf(x);
  const vues = D.prep.seances.slice(0, idx).flatMap((y, j) => y.quiz.map((it, k) => ({it, sid:y.id, k, rappel:'Rappel · entraînement ' + (j + 1)})));
  const tires = []; while (vues.length && tires.length < 2) tires.push(vues.splice(Math.floor(Math.random() * vues.length), 1)[0]);
  // Tour 2 (D2) : aux séances 3, 4 et 8, les deux dernières questions ne s'écoutent qu'une fois, comme au comptoir.
  const unefois = ['p3', 'p4', 'p8'].includes(x.id);
  const items = [...tires, ...x.quiz.map((it, k) => ({it, sid:x.id, k, une: unefois && k >= x.quiz.length - 2}))];
  let n = 0, erreurs = 0;
  function tour(){
    if (n >= items.length) {
      app.innerHTML = `${teteSeance(x, 'quiz')}<div class="retro ok">✓ ${items.length} questions${erreurs ? ', ' + erreurs + ' essai' + (erreurs > 1 ? 's' : '') + ' de trop — c’est ainsi qu’on apprend' : ', toutes du premier coup'}.</div>
        <div style="margin-top:12px">${finTemps(x, 'quiz')}</div>`; return;
    }
    const {it, sid, k, rappel, une} = items[n];
    const fichier = sonDe(`prep/${sid}/q${k}` + (it.type === 'dire' ? '-c0' : ''), it.type === 'dire' ? it.choix[0][0] : it.es);
    // Audit tour 1 (D4) : la graine dépend aussi de la séance — plus de motif commun.
    const [html, brancher] = questionPrep(it, fichier, ((n + 1) * 7919 + (idx + 1) * 104729) % 97, e => {
      erreurs += e; const b = document.createElement('button'); b.className = 'btn btn--pri btn--large'; b.textContent = 'Suivant';
      b.onclick = () => { n++; tour(); }; $('#r').appendChild(b); }, rappel, une);
    app.innerHTML = `${teteSeance(x, 'quiz')}<div class="progres"><i style="width:${100 * n / items.length}%"></i></div>${html}`;
    brancher();
  }
  tour();
}
// Les mots du modèle qui correspondent à une clé manquante, écrits comme dans le modèle (audit tour 1, E1).
function motDuModele(es, cle){
  const mots = g(es).replace(/[¿?¡!.,]/g, ' ').split(/\s+/).filter(Boolean);
  const tailles = cle.startsWith('~') ? [1, 2, 3, 4] : [cle.split('|')[0].split(' ').length];
  for (const n of tailles)
    for (let i = 0; i + n <= mots.length; i++) { const bout = mots.slice(i, i + n).join(' '); if (trouve(bout, cle)) return bout; }
  return cle.startsWith('~') ? g(es) : cle.split('|')[0];
}
function seanceDire(x){
  let n = 0, comprises = 0, dites = 0;
  function tour(){
    if (n >= x.dire.length) {
      const assez = dites >= Math.ceil(x.dire.length / 2);
      app.innerHTML = `${teteSeance(x, 'dire')}<div class="retro ${assez ? 'ok' : 'info'}">${assez ? '✓' : '→'} ${dites} phrase${dites > 1 ? 's' : ''} dite${dites > 1 ? 's' : ''} sur ${x.dire.length}${Reco ? `, dont ${comprises} comprise${comprises > 1 ? 's' : ''} au micro du premier ou du deuxième coup` : ''}. ${assez ? 'Le plus dur est fait : oser.' : 'Dites-en au moins la moitié à voix haute pour terminer la séance.'}</div>
        <div style="margin-top:12px">${assez ? finTemps(x, 'dire') : `<button class="btn btn--pri btn--large" onclick="rendre()">Recommencer</button>`}</div>`; return;
    }
    let [fr, es, cles] = x.dire[n], fichier = sonDe(`prep/${x.id}/d${n}`, es);
    // Tour 2 (A3) : sans allergie déclarée, on ne fait pas dire une allergie inventée.
    if (x.dire[n][3] && !S.alergia) { [fr, es, cles] = x.dire[n][3].sans; fichier = sonDe(`prep/${x.id}/d${n}-sans`, es); }
    let tente = false, essais = 0, modeleVu = false;
    app.innerHTML = `${teteSeance(x, 'dire')}<div class="progres"><i style="width:${100 * n / x.dire.length}%"></i></div>
      <div class="carte"><p class="surtitre">À vous</p><p style="font-size:19px;font-weight:800;color:var(--text-strong);margin:4px 0 0">${E(g(fr))}</p></div>
      ${Reco ? `<div class="micro"><button class="btn-micro" id="mic" aria-label="Parler">${ICO.micro}</button>
        <div class="muted" id="micEtat" style="font-size:14px">Touchez le micro, dites-le en espagnol.</div><div class="entendu" id="entendu"></div></div>` : ''}
      <button class="btn btn--large" id="dit" style="margin:6px 0">Je l'ai dit à voix haute</button><div id="r"></div>
      <div class="rangee" style="margin-top:10px"><button class="btn" id="modele" disabled>${ICO.son} Le modèle</button>
       <button class="btn btn--pri" id="suite" style="flex:1" disabled>Suivant</button></div>
      <p class="avis-local" style="margin-top:8px">Le modèle s'ouvre après votre essai : on cherche d'abord, on compare ensuite.</p>
      <button class="btn btn--petit" id="passer" style="margin-top:4px">Passer cette phrase</button>`;
    // La zone de CETTE phrase : un modèle différé ne doit jamais tomber sur la suivante.
    const zone = $('#r');
    const montrer = () => { if (modeleVu || !document.body.contains(zone)) return; modeleVu = true; $('#modele').disabled = true;
      zone.insertAdjacentHTML('beforeend', `<div class="retro info"><span class="surtitre">Le modèle</span><div class="phrase-es">${E(g(es))}</div></div>`); jouer(fichier); };
    const essaye = () => { if (!tente) { tente = true; dites++; } $('#modele').disabled = modeleVu; $('#suite').disabled = false; };
    $('#modele').onclick = montrer;
    $('#suite').onclick = () => { n++; tour(); };
    $('#passer').onclick = () => { n++; tour(); };
    $('#dit').onclick = () => { essaye(); montrer(); };
    if (Reco) $('#mic').onclick = () => {
      const mic = $('#mic'); if (recoActive) { arreterMicro(); return; }
      mic.classList.add('ecoute'); mic.innerHTML = ICO.stop; $('#micEtat').textContent = 'Je vous écoute… touchez pour arrêter.';
      ecouterMicro(t => { $('#entendu').textContent = '« ' + t + ' »'; }, final => {
        mic.classList.remove('ecoute'); mic.innerHTML = ICO.micro; $('#micEtat').textContent = 'Touchez le micro pour réessayer.';
        if (!final) { $('#r').innerHTML = `<div class="retro info">${rienEntendu('Je n\u2019ai rien entendu. Vérifiez que le micro est permis, ou dites-le et touchez « Je l\u2019ai dit ».')}</div>`; return; }
        essais++;
        const manque = cles.map(c => g(algDe(c))).filter(c => !trouve(final, c));
        const algCle = cles.find(c => /\{alg:/.test(c));
        const alg = algCle && manque.length === 1 && manque[0] === g(algDe(algCle));
        if (!manque.length) { if (essais <= 2 && !modeleVu) comprises++;
          $('#r').innerHTML = `<div class="retro ok">✓ ¡Muy bien! On vous a compris.</div>`; essaye(); setTimeout(montrer, 600); return; }
        const presque = manque.length <= cles.length / 2;
        $('#r').innerHTML = `<div class="retro no">${alg ? 'On sait que vous êtes allergique, mais pas à quoi : dites l’aliment. '
          : presque ? `Presque. Il manque : <b>${manque.map(c => E(motDuModele(es, c))).join(', ')}</b>. ` : 'Je n’ai pas reconnu la phrase. '}${essais < 2 && !modeleVu ? 'Réessayez, sans regarder le modèle.' : 'Comparez avec le modèle.'}</div>`;
        essaye();
        // Audit tour 1 (D1) : un deuxième essai à l'aveugle avant le modèle.
        if (essais >= 2) montrer(); else $('#modele').disabled = false;
      });
    };
  }
  tour();
}
function vuePrepTest(){
  if (!S.prep) S.prep = {}; const T = S.prep.test || (S.prep.test = {});
  const f = T.prochaine != null ? T.prochaine : Math.floor(Math.random() * 2);
  const items = D.prep.test[f]; let k = 0; const res = {}, nonVerif = {}, manquees = {};
  const prete = S.genre === 'f' ? 'prête' : 'prêt';
  function intro(){
    app.innerHTML = `${retour('prep', 'Avant de partir')}<p class="surtitre">Le test de la maison</p><h1>${prete[0].toUpperCase() + prete.slice(1)} à partir ?</h1>
      <p>${items.length} questions, un quart d'heure, avec le son et le micro. Pour chacun des cinq objectifs, quelques questions — surtout des phrases
      nouvelles : les mêmes outils que dans les entraînements, d'autres mots.</p>
      <div class="regle"><b>Comme sur le chemin.</b> Les phrases qu'on vous dit ne s'écoutent <b>qu'une fois</b>, au débit normal. Au micro, <b>deux essais</b>.
      ${E(D.prep.seuil.split(' Au micro')[0])} C'est un repère sur un échantillon, pas une note : il ne vous empêche de rien.</div>
      <button class="btn btn--pri btn--large" id="go">Commencer</button>`;
    $('#go').onclick = tour;
  }
  function tour(){
    if (k >= items.length) return bilan();
    let it = items[k]; let compte = false;
    const sansAlg = it.sans && !S.alergia; if (sansAlg) it = {...it, ...it.sans};
    const noter = ok => { if (compte) return; compte = true; const r = res[it.obj] || (res[it.obj] = [0, 0]); r[1]++; if (ok) r[0]++;
      else (manquees[it.obj] || (manquees[it.obj] = [])).push(g(algDe(it.es || it.modele || it.choix[0][0]))); };
    const suite = () => { const b = document.createElement('button'); b.className = 'btn btn--pri btn--large'; b.textContent = 'Suivant'; b.onclick = () => { k++; tour(); }; $('#r').appendChild(b); };
    const tete2 = `${retour('prep', 'Avant de partir')}<p class="surtitre">Question ${k + 1} sur ${items.length}</p><div class="progres"><i style="width:${100 * k / items.length}%"></i></div>`;
    if (it.type === 'oral') {
      let prises = 0;
      app.innerHTML = `${tete2}<h1>Dites-le</h1><div class="carte"><p style="font-size:18px;font-weight:800;margin:0">${E(g(it.fr))}</p></div>
        ${Reco ? `<div class="micro"><button class="btn-micro" id="mic" aria-label="Parler">${ICO.micro}</button><div class="muted" id="micEtat" style="font-size:14px">Deux essais.</div><div class="entendu" id="entendu"></div></div>` : ''}
        <div id="r"></div><button class="btn btn--large" id="sansmic" style="margin-top:8px">${Reco ? 'Sans micro : je l’ai dit à voix haute' : 'Je l’ai dit à voix haute'}</button>`;
      const fin = (ok, verifie) => { if (verifie) noter(ok); else { compte = true; nonVerif[it.obj] = (nonVerif[it.obj] || 0) + 1; }
        if ($('#sansmic')) $('#sansmic').remove(); if ($('#mic')) $('#mic').disabled = true;
        $('#r').insertAdjacentHTML('beforeend', `<div class="retro ${!verifie ? 'info' : ok ? 'ok' : 'no'}">${!verifie ? 'Non vérifié : cette question ne compte pas.' : ok ? '✓ On vous a compris.' : 'Deux essais sans qu’on vous comprenne tout à fait.'}</div>
          <div class="retro info"><span class="surtitre">Le modèle</span><div class="phrase-es">${E(g(it.modele))}</div></div>`);
        jouer(sonDe(`prep/test/${f}-${k}-m${sansAlg ? '-sans' : ''}`, it.modele)); suite(); };
      $('#sansmic').onclick = () => fin(false, false);
      if (Reco) $('#mic').onclick = () => { const mic = $('#mic'); if (recoActive) { arreterMicro(); return; }
        mic.classList.add('ecoute'); mic.innerHTML = ICO.stop;
        ecouterMicro(t => { $('#entendu').textContent = '« ' + t + ' »'; }, final => {
          mic.classList.remove('ecoute'); mic.innerHTML = ICO.micro;
          if (!final) { $('#r').innerHTML = `<div class="retro info">${rienEntendu('Je n\u2019ai rien entendu. Vérifiez que le micro est permis et réessayez — ou touchez « je l\u2019ai dit ».')}</div>`; return; }
          const manque = it.cles.map((c, i) => [g(algDe(c)), i]).filter(([c]) => !trouve(final, c));
          prises++;
          // Tour 2 (F1) : une fois le micro entendu, « le micro ne marche pas » n'est plus une issue.
          if ($('#sansmic')) $('#sansmic').remove();
          if (!manque.length) { $('#r').innerHTML = ''; return fin(true, true); }
          const quoi = it.parties ? 'Il manque : ' + manque.map(([, i]) => E(g(algDe(it.parties[i])))).join(', ') + '.' : `J'ai entendu « ${E(final)} ».`;
          if (prises >= 2) { $('#r').innerHTML = `<div class="retro no">${quoi}</div>`; return fin(false, true); }
          $('#r').innerHTML = `<div class="retro no">${quoi} Réessayez (dernier essai).</div>`;
        }); };
      return;
    }
    // Au test, le premier choix compte. P2 et P5 : une seule écoute, au débit naturel (audit tour 1, F1).
    const fichier = sonDe(`prep/test/${f}-${k}` + (it.type === 'dire' ? '-c0' : ''), it.type === 'dire' ? it.choix[0][0] : it.es);
    const unefois = it.obj === 'P2' || it.obj === 'P5';
    const o = ordre(it.choix.length, ((k + 1) * 7919 + f * 104729) % 97), estEs = it.type !== 'rep', p = it.qui ? D.perso[it.qui] : null;
    const titre = it.type === 'rep' ? 'Que veut dire la phrase ?' : it.type === 'mot' ? 'Quel mot entendez-vous ?' : 'Que dites-vous ?';
    app.innerHTML = `${tete2}<h1>${titre}</h1>
      ${it.type === 'dire' ? `<div class="carte"><p style="font-size:18px;font-weight:800;margin:0">${E(g(it.fr))}</p></div>` :
        `${p ? `<div class="scene-tete">${p.portrait ? `<img src="${BASE}portraits/${it.qui}.jpg?v=${D.v}" alt="">` : ''}<div><b>${E(p.nom)}</b><div class="muted" style="font-size:14px">${unefois ? 'Une seule écoute, comme au comptoir.' : 'Vous pouvez réécouter.'}</div></div></div>` : ''}
         <div class="gros-son"><button class="btn btn--son" aria-label="Écouter" id="ecoute1">${ICO.son}</button></div>`}
      <div class="choix">${o.map(i => `<button data-i="${i}" ${estEs ? 'lang="es"' : ''}>${E(g(it.choix[i][0]))}</button>`).join('')}</div><div id="r"></div>`;
    if (it.type !== 'dire') {
      let joue = false;
      const une = () => { if (unefois && joue) return; if (unefois) { joue = true; $('#ecoute1').disabled = true; }
        jouer(fichier, unefois).then(ok => { if (!ok && unefois) { joue = false; $('#ecoute1').disabled = false; } }); };
      $('#ecoute1').onclick = une; setTimeout(une, 250);
    }
    app.querySelectorAll('.choix button').forEach(b => b.onclick = () => {
      if (compte) return; const i = +b.dataset.i; noter(i === 0);
      b.classList.add(i === 0 ? 'juste' : 'faux'); if (i !== 0) app.querySelector('.choix button[data-i="0"]').classList.add('juste');
      $('#r').innerHTML = `<div class="retro ${i === 0 ? 'ok' : 'no'}">${i === 0 ? '✓' + (it.es ? ' « ' + E(g(it.es)) + ' »' : '') : E(g(it.choix[i][1]))}</div>`;
      if (it.type === 'dire') jouer(fichier); suite();
    });
  }
  function bilan(){
    const HALTE_N = id => D.etapes.find(e => e.id === id);
    const lignes = Object.keys(D.prep.objectifs).map(o => {
      const [ok, tot] = res[o] || [0, 0], nv = nonVerif[o] || 0, h = HALTE_N(D.prep.halte[o]);
      if (!tot) return `<div class="carte" style="margin:8px 0"><b>${E(D.prep.objectifs[o])}</b><div class="retro info" style="margin:6px 0">Non vérifié au micro : refaites ces questions avec le micro.</div><p class="muted" style="margin:0;font-size:15px">${E(D.prep.conseils[o])}</p></div>`;
      const r = ok / tot;
      const etat = r >= .8 ? ['ok', '✓ Solide'] : r >= .5 ? ['info', '→ En route'] : ['no', '— À reprendre'];
      return `<div class="carte" style="margin:8px 0"><b>${E(D.prep.objectifs[o])}</b><div class="retro ${etat[0]}" style="margin:6px 0">${etat[1]} — ${ok} sur ${tot}${nv ? ` (et ${nv} non vérifiée${nv > 1 ? 's' : ''} au micro)` : ''}</div>
        ${r < .8 ? `<p class="muted" style="margin:0;font-size:15px">${E(D.prep.conseils[o])}</p>` : ''}
        ${(manquees[o] || []).length ? `<p class="muted" style="margin:4px 0 0;font-size:14px">À revoir : ${manquees[o].map(t => '<i lang="es">' + E(t) + '</i>').join(' · ')}</p>` : ''}
        ${h ? `<p class="muted" style="margin:4px 0 0;font-size:14px">Vous en aurez besoin dès la halte ${h.n}, ${E(h.lieu)}.</p>` : ''}</div>`;
    }).join('');
    T.prochaine = 1 - f; T.passages = (T.passages || 0) + 1; T.dernier = aujourdhui(); sauver();
    app.innerHTML = `${retour('prep', 'Avant de partir')}<h1>Où vous en êtes</h1>
      <p>Un repère sur un échantillon, pas une note. La prochaine fois — la veille du départ, par exemple — ce sera l'autre forme.</p>${lignes}
      <button class="btn btn--pri btn--large" onclick="aller('jour/${D.etapes[0].id}')">En route : halte 1, ${E(D.etapes[0].lieu)}</button>
      <button class="btn btn--large" style="margin-top:8px" onclick="aller('prep')">Revoir mon sac</button>`;
  }
  intro();
}

/* ---------- la poche ---------- */
function vuePoche(){
  app.innerHTML = `${retour('accueil', 'La credencial')}<p class="surtitre">Trousse de secours · pour se débrouiller</p><h1>Ma trousse</h1>
  <p class="muted">Les phrases du chemin, avec leur voix. « Montrer » affiche la phrase en grand, pour la tendre à quelqu'un.</p>
  <div class="carte" style="margin:12px 0"><b>Sans réseau sur la Meseta ?</b>
   <p class="muted" style="font-size:15px;margin:4px 0 10px">Une fois, avec du wifi : mettez tous les sons et les images dans ce téléphone (environ ${D.poids} Mo).</p>
   <button class="btn btn--pri" id="prep">Préparer pour le chemin</button><div id="prepEtat" class="muted" style="font-size:14px;margin-top:8px"></div></div>
  <details class="rub" open><summary>Ma carte d'allergie <span>${allergie() ? E(allergie().fr) : 'à choisir'}</span></summary>
   <div class="ph" style="flex-wrap:wrap"><label for="alg" style="font-weight:800">Mon allergie :</label>
    <select id="alg" style="font:inherit;padding:8px;border-radius:10px;border:1px solid var(--line-300);min-height:44px;flex:1">
     <option value="">— aucune —</option>${D.alergenos.map(a => `<option value="${a.code}" ${S.alergia === a.code ? 'selected' : ''}>${E(a.fr)}</option>`).join('')}</select></div>
   ${allergie() ? `<div class="ph"><button class="btn btn--son" aria-label="Écouter" onclick="jouer('poche/alergia-${allergie().code}.mp3')">${ICO.son}</button>
     <div class="t"><b lang="es">${E(allergie().phrase)}</b><span>J'ai une allergie grave ${E(allergie().fr)}. Ce plat en contient-il ?</span></div>
     <button class="btn btn--petit" onclick="montrerAllergie()">Montrer</button></div>
     <p class="avis-local" style="padding:0 14px 10px;margin:0">Plusieurs allergies ? Changez le choix ci-dessus pour montrer chacune ; au restaurant, dites-les toutes.</p>` : ''}</details>
  ${D.poche.map((r, ri) => `<details class="rub"${ri === 0 ? ' open' : ''}><summary>${E(r.titre)} <span>${r.items.length}</span></summary>
    ${r.items.map(itemPoche).map((x, xi) => `<div class="ph"><button class="btn btn--son" aria-label="Écouter" onclick="jouer('${x.fichier}')">${ICO.son}</button>
     <div class="t"><b>${E(g(x.es))}</b><span>${E(g(x.fr))}</span></div>
     <button class="btn btn--petit" onclick="montrer(${ri},${xi})">Montrer</button></div>`).join('')}
    ${(r.reponses || []).length ? `<div class="ph" style="background:#FBF6E9"><b style="font-size:13px;letter-spacing:.06em;text-transform:uppercase;color:#7A6A45">Ce qu'on peut vous répondre</b></div>
     ${r.reponses.map(x => `<div class="ph"><button class="btn btn--son" aria-label="Écouter" onclick="jouer('${sonDe(x.son, x.es)}')">${ICO.son}</button>
      <div class="t"><b>${E(g(x.es))}</b><span>${E(g(x.fr))}</span></div></div>`).join('')}` : ''}</details>`).join('')}`;
  $('#prep').onclick = preparer;
  $('#alg').onchange = e => { S.alergia = e.target.value; sauver(); vuePoche(); };
}
function itemPoche(x){
  if (x.var && S.vars[x.var]) { const c = choixVar(x.var); if (c) return {es:c.es, fr:c.fr, fichier:c.fichier}; }
  return {es:x.es, fr:x.trad || x.fr, fichier:sonDe(x.son, x.es)};
}
function montrerAllergie(){
  const a = allergie(); if (!a) return;
  D.poche.__a = {es:a.phrase, fr:`J'ai une allergie grave ${a.fr}. Ce plat en contient-il ?`, son:`poche/alergia-${a.code}`};
  montrerX(D.poche.__a);
}
function montrer(ri, xi){ const x = itemPoche(D.poche[ri].items[xi]); montrerX({es:x.es, fr:x.fr, fichier:x.fichier}); }
function montrerX(x){
  const v = document.createElement('div'); v.className = 'montrer';
  v.innerHTML = `<button class="btn fermer">Fermer</button><div class="grand" lang="es">${E(g(x.es))}</div><div class="petit">${E(g(x.fr))}</div>
    <button class="btn btn--son" style="margin-top:22px;width:72px;height:72px;border-radius:50%">${ICO.son}</button>`;
  document.body.appendChild(v);
  v.querySelector('.fermer').onclick = () => v.remove();
  v.querySelector('.btn--son').onclick = () => jouer(x.fichier || sonDe(x.son, x.es));
}
async function preparer(){
  const etat = $('#prep'), txt = $('#prepEtat'); etat.disabled = true;
  if ('serviceWorker' in navigator) { try { await navigator.serviceWorker.register('/sw.js'); await navigator.serviceWorker.ready; } catch(e) {} }
  const urls = [...D.sons.map(f => BASE + 'sons/' + f + '?v=' + D.v)];
  Object.entries(D.mots).forEach(([id, m]) => m.img === 'croquis' && urls.push(BASE + 'croquis/' + id + '.jpg?v=' + D.v));
  D.etapes.forEach(e => e.vignette && urls.push(BASE + 'etapes/' + e.img + '.jpg?v=' + D.v));
  Object.keys(D.perso).forEach(k => D.perso[k].portrait && urls.push(BASE + 'portraits/' + k + '.jpg?v=' + D.v));
  urls.push(BASE + 'etapes/meseta.jpg?v=' + D.v, location.pathname);
  // Ce que la page a chargé AVANT que le service worker ne la contrôle
  // (feuilles du système de design, polices, icône) : sans eux, la page
  // hors ligne s'affiche sans ses styles. Vu en ligne le 25 sept. 2026.
  performance.getEntriesByType('resource').forEach(r => { try { const u = new URL(r.name);
    if (u.origin === location.origin && !u.pathname.startsWith('/api/') && !urls.includes(u.pathname + u.search)) urls.push(u.pathname + u.search); } catch(e) {} });
  ['/assets/design-system/styles.css', '/assets/design-system/marque-francis.css', '/assets/design-system/marque-francis-favicon.svg']
    .forEach(u => urls.includes(u) || urls.push(u));
  let fait = 0, echec = 0;
  const lot = async u => { try { const r = await fetch(u, {cache:'reload'}); if (!r.ok) echec++; } catch(e) { echec++; } fait++; txt.textContent = `${fait} / ${urls.length} fichiers…`; };
  for (let i = 0; i < urls.length; i += 6) await Promise.all(urls.slice(i, i + 6).map(lot));
  const controle = navigator.serviceWorker && navigator.serviceWorker.controller;
  txt.innerHTML = echec ? `${echec} fichiers n'ont pas pu être pris. Réessayez avec un meilleur réseau.` :
    (controle ? '✓ Tout est dans le téléphone. Bon chemin !' : '✓ Téléchargé. Rouvrez la page une fois, avec du réseau, pour que le téléphone la garde aussi.');
  etat.disabled = false;
}

/* ---------- tous les mots ---------- */
function vueMots(pl){
  if (pl) {
    const P = D.planches.find(x => x[0] === pl);
    const ids = Object.keys(D.mots).filter(id => D.mots[id].p === pl);
    app.innerHTML = `${retour('mots', 'Les planches')}<p class="surtitre">${E(P[2])}</p><h1>${E(P[1])}</h1>
      <p class="consigne">Touchez une carte pour entendre le mot et voir sa traduction.</p>
      <div class="grille">${ids.map(id => carteMot(id)).join('')}</div>`;
    return;
  }
  app.innerHTML = `${retour('accueil', 'La credencial')}<h1>Tous les mots</h1>
  <div class="outils">${D.planches.map(([k, fr, es]) => {
    const n = Object.values(D.mots).filter(m => m.p === k).length;
    return `<button class="outil" onclick="aller('mots/${k}')"><div><b>${E(fr)}</b><span>${E(es)} · ${n} mots</span></div></button>`;
  }).join('')}</div>`;
}

/* ---------- les faux amis ---------- */
function vuePieges(){
  let n = 0, erreurs = 0;
  function tour(){
    if (n >= D.pieges.length) {
      app.innerHTML = `${retour('accueil', 'La credencial')}<h1>Les faux amis</h1><div class="retro ok">✓ Les ${D.pieges.length} faux amis sont démasqués${erreurs ? ' (' + erreurs + ' erreur' + (erreurs > 1 ? 's' : '') + ')' : ''}.</div>
        <button class="btn btn--pri btn--large" onclick="aller('accueil')">Retour</button>`; return;
    }
    const x = D.pieges[n], opts = [x.bonne, x.fausse, x.seconde], o = ordre(3, n);
    app.innerHTML = `${retour('accueil', 'La credencial')}<p class="surtitre">Faux ami ${n + 1} sur ${D.pieges.length}</p><h1>Que veut dire la phrase ?</h1>
      <div class="progres"><i style="width:${100 * n / D.pieges.length}%"></i></div>
      <div class="carte"><div class="rangee"><button class="btn btn--son" onclick="jouer('pieges/${x.id}.mp3')">${ICO.son}</button>
       <div class="phrase-es" style="flex:1">${E(x.es)}</div></div></div>
      <div class="choix">${o.map(i => `<button data-i="${i}">${E(opts[i])}</button>`).join('')}</div><div id="r"></div>`;
    app.querySelectorAll('.choix button').forEach(b => b.onclick = () => {
      const i = +b.dataset.i;
      if (i === 0) {
        b.classList.add('juste');
        $('#r').innerHTML = `<div class="retro ok">✓ ${E(x.expl)}</div><button class="btn btn--pri btn--large" id="suite">Suivant</button>`;
        $('#suite').onclick = () => { n++; tour(); };
      } else if (!b.classList.contains('faux')) { erreurs++; b.classList.add('faux'); $('#r').innerHTML = `<div class="retro no">${E(x.expl)}</div>`; }
    });
    setTimeout(() => jouer('pieges/' + x.id + '.mp3'), 250);
  }
  tour();
}

/* ---------- le test « Suis-je prêt ? » ----------
   Audit tour 1 (F1, bloquant) : deux formes parallèles d'items INÉDITS
   (build/contenu/compostelle/test.py), les cinq objectifs dans chacune,
   l'allergie éliminatoire — règle affichée avant. Plus quelques mots et faux
   amis de la pratique, pour le vocabulaire. La première forme est tirée au
   hasard, la reprise prend l'autre. */
function vueTest(){
  if (!S.test) S.test = {};
  const f = S.test.prochaine != null ? S.test.prochaine : Math.floor(Math.random() * 2);
  const items = D.test.formes[f].map((it, n) => ({...it, n}));
  const pool = D.etapes.flatMap(e => e.mots).filter((x, i, a) => a.indexOf(x) === i && D.mots[x] && D.mots[x].img === 'croquis');
  pool.filter((_, i) => i % 2 === f).slice(0, 3).forEach(id => items.push({type:'mot', obj:'mots', id}));
  D.pieges.filter((_, i) => i % 2 === f).slice(0, 2).forEach(x => items.push({type:'piege', obj:'mots', x}));
  let k = 0; const res = {}; let elimRate = false, nonVerifie = false;
  const prete = S.genre === 'f' ? 'prête' : 'prêt';
  function intro(){
    app.innerHTML = `${retour('accueil', 'La credencial')}<p class="surtitre">Le test du chemin</p><h1>Suis-je ${prete} ?</h1>
      <p>${items.length} questions, un quart d'heure, avec le son. Des phrases <b>nouvelles pour la plupart</b> : comprendre et dire, pour un lit, un repas, la pharmacie, un chemin, un autre pèlerin — puis quelques mots.</p>
      <div class="regle"><b>La règle.</b> Les questions marquées « allergie » ne pardonnent pas : en rater une donne « Pas encore ${prete} », quel que soit le reste.
      Pour chaque objectif, plusieurs questions : ${E(D.test.seuil)} L'allergie dite au micro compte comme les autres questions d'allergie. ${allergie() ? 'Les questions d\u2019allergie portent sur la vôtre (' + E(allergie().fr) + ').' : 'Choisissez votre allergie dans les réglages : sans elle, les questions portent sur les noix.'}</div>
      ${S.test.passages >= 2 ? `<div class="retro info">Vous avez vu les deux formes. Refaites quelques haltes avant de repasser : les réponses sont encore fraîches.</div>` : ''}
      ${S.test.dernier ? `<div class="retro info">Dernier passage : ${E(S.test.dernier)}</div>` : ''}
      <button class="btn btn--pri btn--large" id="go">Commencer</button>`;
    $('#go').onclick = tour;
  }
  function tour(){
    if (k >= items.length) return bilan();
    const it = items[k]; let tentee = false;
    const tete2 = `${retour('accueil', 'La credencial')}<p class="surtitre">Question ${k + 1} sur ${items.length}</p><div class="progres"><i style="width:${100 * k / items.length}%"></i></div>
      ${(it.elim || (it.type === 'oral' && it.obj === 'O2')) ? '<span class="rappel" style="background:var(--no-bg);border-color:var(--no-line);color:var(--no-ink)">Allergie — ne pardonne pas</span>' : ''}`;
    const noter = ok => { if (tentee) return; tentee = true; const r = res[it.obj] || (res[it.obj] = [0, 0]); r[1]++; if (ok) r[0]++; if (!ok && it.elim) elimRate = true; };
    const suite = () => { const b = document.createElement('button'); b.className = 'btn btn--pri btn--large'; b.textContent = 'Suivant'; b.onclick = () => { k++; tour(); }; $('#r').appendChild(b); };
    const qcm = (textes, retros, bonneTxt) => {
      // Audit tour 2 (D4) : la place de la bonne suivait un cycle fixe.
      const o = ordre(textes.length, ((k + 1) * 7919 + f * 104729) % 97);
      return [`<div class="choix">${o.map(i => `<button data-i="${i}" ${bonneTxt ? 'lang="es"' : ''}>${E(g(textes[i]))}</button>`).join('')}</div><div id="r"></div>`, () =>
        app.querySelectorAll('.choix button').forEach(b => b.onclick = () => {
          if (tentee) return; const i = +b.dataset.i; noter(i === 0);
          b.classList.add(i === 0 ? 'juste' : 'faux');
          if (i !== 0) app.querySelector('.choix button[data-i="0"]').classList.add('juste');
          $('#r').innerHTML = `<div class="retro ${i === 0 ? 'ok' : 'no'}">${i === 0 ? '✓ ' + E(bonneTxt || '') : E(g(retros[i]))}</div>`; suite();
        })];
    };
    if (it.type === 'rep' || it.type === 'repondre') {
      const fichier = sonDe(`test/${f}-${it.n}`, it.es), p = D.perso[it.qui];
      const [html, brancher] = qcm(it.choix.map(c => c[0]), it.choix.map(c => c[1]), it.type === 'rep' ? '« ' + g(it.es) + ' »' : '');
      app.innerHTML = `${tete2}<h1>${it.type === 'rep' ? 'Que veut dire la phrase ?' : 'Que répondez-vous ?'}</h1>
        <div class="scene-tete">${p.portrait ? `<img src="${BASE}portraits/${it.qui}.jpg?v=${D.v}" alt="">` : ''}<div><b>${E(p.nom)}</b><div class="muted" style="font-size:14px">Vous pouvez réécouter.</div></div></div>
        <div class="gros-son"><button class="btn btn--son" aria-label="Écouter" onclick="jouer('${fichier}')">${ICO.son}</button></div>${html}`;
      brancher(); setTimeout(() => jouer(fichier), 250);
    } else if (it.type === 'oral') {
      // Audit tour 4 (F1/G2, majeur) : trois prises, la meilleure compte ; rien
      // entendu ou micro refusé → un message et le repli « non vérifié ».
      // Seul l'oral d'ALLERGIE (O2) est éliminatoire, et seulement vérifié.
      let prises = 0;
      app.innerHTML = `${tete2}<h1>Dites-le</h1><div class="carte"><p style="font-size:18px;font-weight:800;margin:0">${E(g(it.fr))}</p></div>
        ${Reco ? `<div class="micro"><button class="btn-micro" id="mic" aria-label="Parler">${ICO.micro}</button><div class="muted" id="micEtat" style="font-size:14px">Trois essais ; le meilleur compte.</div><div class="entendu" id="entendu"></div></div>` : ''}
        <div id="r"></div><button class="btn btn--large" id="sansmic" style="margin-top:8px">${Reco ? 'Sans micro : je l’ai dit à voix haute' : 'Je l’ai dit à voix haute'}</button>
        ${Reco ? '' : '<p class="avis-local">Ce navigateur ne reconnaît pas la voix : cette question ne sera pas vérifiée.</p>'}`;
      const modele = () => `<div class="retro info"><span class="surtitre">Le modèle</span><div class="phrase-es">${E(g(it.modele || ''))}</div></div>`;
      const fin = (ok, verifie) => {
        if (verifie) { if (it.obj === 'O2') it.elim = true; noter(ok); } else { tentee = true; if (it.obj === 'O2') nonVerifie = true; }
        if ($('#sansmic')) $('#sansmic').remove(); if ($('#mic')) $('#mic').disabled = true;
        $('#r').innerHTML = `<div class="retro ${!verifie ? 'info' : ok ? 'ok' : 'no'}">${!verifie ? 'Non vérifié : cette question ne compte pas.' : ok ? '✓ On vous a compris.' : 'Trois essais sans qu’on vous comprenne.'}</div>${modele()}`;
        if (it.obj === 'O2') jouer(sonDe('leon/dire-0', 'Soy alérgic{o|a} {alg:a}.'));
        suite(); };
      $('#sansmic').onclick = () => fin(false, false);
      if (Reco) $('#mic').onclick = () => { const mic = $('#mic'); if (recoActive) { arreterMicro(); return; }
        mic.classList.add('ecoute'); mic.innerHTML = ICO.stop;
        ecouterMicro(t => { $('#entendu').textContent = '« ' + t + ' »'; }, final => {
          mic.classList.remove('ecoute'); mic.innerHTML = ICO.micro;
          if (!final) { $('#r').innerHTML = `<div class="retro info">${rienEntendu('Je n\u2019ai rien entendu. Vérifiez que le micro est permis et réessayez — ou touchez « je l\u2019ai dit ».')}</div>`; return; }
          const t = ' ' + plat(final).replace(/ o no$/, '') + ' ', non = it.obj === 'O2' && / no /.test(t);
          const ok = !non && it.cles.every(c => g(c).split('|').some(x => t.includes(plat(x))));
          prises++;
          if (ok) return fin(true, true);
          if (prises >= 3) return fin(false, true);
          $('#r').innerHTML = `<div class="retro no">J'ai entendu « ${E(final)} ». ${non ? 'Attention au « no ». ' : ''}Réessayez (${prises} sur 3).</div>`;
        }); };
    } else if (it.type === 'dire') {
      const [html, brancher] = qcm(it.choix.map(c => c[0]), it.choix.map(c => c[1]), 'C’est bien ce qu’il faut dire.');
      app.innerHTML = `${tete2}<h1>Que dites-vous ?</h1><div class="carte"><p style="font-size:18px;font-weight:800;margin:0">${E(g(it.fr))}</p></div>${html}`;
      brancher();
    } else if (it.type === 'mot') {
      const autres = pool.filter(x => x !== it.id), d = (k * 5) % autres.length;
      const opts = [it.id, autres[d], autres[(d + 7) % autres.length], autres[(d + 13) % autres.length]], o = ordre(4, k + f * 3);
      app.innerHTML = `${tete2}<h1>Quel est le mot entendu ?</h1>
        <div class="gros-son"><button class="btn btn--son" aria-label="Écouter" onclick="jouer('mots/${it.id}.mp3')">${ICO.son}</button></div>
        <div class="images">${o.map(i => `<button data-id="${opts[i]}" aria-label="${E(D.mots[opts[i]].fr)}">${imageMot(D.mots[opts[i]], opts[i])}</button>`).join('')}</div><div id="r"></div>`;
      app.querySelectorAll('.images button').forEach(b => b.onclick = () => {
        if (tentee) return; const ok = b.dataset.id === it.id; noter(ok);
        b.classList.add(ok ? 'juste' : 'faux');
        $('#r').innerHTML = `<div class="retro ${ok ? 'ok' : 'no'}"><b>${E(g(D.mots[it.id].es))}</b> — ${E(D.mots[it.id].fr)}${ok ? '' : ' (vous avez touché : ' + E(D.mots[b.dataset.id].fr) + ')'}</div>`; suite();
      });
      setTimeout(() => jouer('mots/' + it.id + '.mp3'), 250);
    } else {
      const x = it.x;
      const [html, brancher] = qcm([x.bonne, x.fausse, x.seconde], [null, x.expl, x.expl], x.expl);
      app.innerHTML = `${tete2}<h1>Que veut dire la phrase ?</h1>
        <div class="carte"><div class="rangee"><button class="btn btn--son" onclick="jouer('pieges/${x.id}.mp3')">${ICO.son}</button><div class="phrase-es" style="flex:1">${E(x.es)}</div></div></div>${html}`;
      brancher();
    }
  }
  function bilan(){
    const noms = {...D.test.objectifs, mots: 'Reconnaître les mots et les faux amis'};
    const conseils = {O1: 'Refaites la halte 1 (Roncesvalles) et le « Ce qu’on me répond » de Burgos.', O2: 'Refaites León en entier' + (S.alergia ? '.' : ', et choisissez votre allergie dans les réglages.'),
      O3: 'Refaites la pharmacie de Logroño.', O4: 'Refaites Puente la Reina, voix plus lentes d’abord.', O5: 'Refaites les soirs avec Marta, en répondant au micro.', mots: 'Reprenez « Tous les mots » et « Les faux amis ».'};
    const lignes = Object.keys(noms).filter(o => res[o]).map(o => {
      const [ok, tot] = res[o], r = ok / tot;
      const etat = (r >= .99 && tot >= 2) ? ['ok', '✓ Solide'] : r > 0 ? ['info', '→ En route'] : ['no', '— À reprendre'];
      return `<div class="carte" style="margin:8px 0"><b>${E(noms[o])}</b><div class="retro ${etat[0]}" style="margin:6px 0">${etat[1]} — ${ok} sur ${tot}</div>${r < .99 ? `<p class="muted" style="margin:0;font-size:15px">${E(conseils[o])}</p>` : ''}</div>`;
    }).join('');
    S.test.prochaine = 1 - f; S.test.passages = (S.test.passages || 0) + 1; S.test.dernier = aujourdhui() + (elimRate ? ' — allergie ratée' : nonVerifie ? ' — allergie non vérifiée' : ' — allergie réussie'); sauver();
    app.innerHTML = `${retour('accueil', 'La credencial')}<h1>Où vous en êtes</h1>
      ${elimRate ? `<div class="eliminatoire"><b>Pas encore ${prete} : l'allergie.</b><p style="margin:6px 0 0">Une question sur l'allergie a été ratée. C'est la seule erreur qui ne pardonne pas sur le chemin. Refaites León, puis repassez le test : ce seront d'autres phrases.</p></div>`
        : nonVerifie ? `<div class="retro info"><b>L'allergie : dite sans micro, donc non vérifiée.</b> C'est la phrase qui compte le plus sur le chemin :
          faites-la vérifier une fois au micro (à León, « Je le dis »), ou dites-la à quelqu'un qui parle espagnol. Le reste est un repère, pas une note.</div>`
        : `<div class="retro ok">✓ L'allergie : réussie. Le reste est un repère, pas une note.</div>`}
      ${lignes}
      <p class="muted">La vraie épreuve, ce sera le premier « ¿Qué te pongo? » à Pamplona.</p>
      <button class="btn btn--pri btn--large" onclick="aller('accueil')">Retour à la credencial</button>`;
  }
  intro();
}

/* ---------- réglages ---------- */
function vueReglages(){
  app.innerHTML = `${retour('accueil', 'La credencial')}<h1>Réglages</h1>
  <div class="carte"><h3 style="margin-top:0">Vous êtes</h3>
   <div class="rangee"><button class="btn ${S.genre === 'm' ? 'btn--pri' : ''}" onclick="S.genre='m';sauver();vueReglages()">Un pèlerin</button>
   <button class="btn ${S.genre === 'f' ? 'btn--pri' : ''}" onclick="S.genre='f';sauver();vueReglages()">Une pèlerine</button></div>
   <h3>Mon allergie</h3>
   <select onchange="S.alergia=this.value;sauver()" style="font:inherit;padding:8px;border-radius:10px;border:1px solid var(--line-300);min-height:44px;width:100%">
    <option value="">— aucune —</option>${D.alergenos.map(a => `<option value="${a.code}" ${S.alergia === a.code ? 'selected' : ''}>${E(a.fr)}</option>`).join('')}</select>
   <p class="avis-local">Elle sert à votre carte « Montrer » de la trousse, et à la phrase que vous direz à León.</p>
   <h3>Les voix</h3>
   <label class="aide-bascule"><input type="checkbox" ${S.lent ? 'checked' : ''} onchange="S.lent=this.checked;sauver()"> Voix plus lentes (partout)</label>
   <h3>Les traductions</h3>
   <label class="aide-bascule"><input type="checkbox" ${S.aide ? 'checked' : ''} onchange="S.aide=this.checked;sauver()"> Toujours montrer le français sous l'espagnol</label>
   <p class="avis-local">Par défaut, le français reste caché : on essaie d'abord de comprendre, on vérifie ensuite.</p>
   <h3>Recommencer</h3>
   <button class="btn" onclick="if(confirm('Effacer vos tampons et recommencer le chemin ?')){S.jours={};S.vars={};sauver();aller('accueil')}">Effacer mes tampons</button>
   <p class="avis-local" style="margin-top:12px">Tout reste dans ce téléphone. Rien n'est envoyé : ni vos réponses, ni votre voix, ni votre prénom.</p></div>`;
}

/* ---------- la Compostela ---------- */
function vueCompostela(){
  const faits = D.etapes.filter(e => jour(e.id).tampon).length;
  if (faits < 10) { app.innerHTML = `${retour('accueil', 'La credencial')}<h1>La Compostela</h1><div class="retro info">Encore ${10 - faits} tampon${10 - faits > 1 ? 's' : ''} avant Santiago.</div>`; return; }
  app.innerHTML = `${retour('accueil', 'La credencial')}
  <div class="compostela"><div class="surtitre" style="color:#7A6A45">francis · En route vers Compostelle</div>
   <div class="titre">Compostela</div>
   <p class="latin">Hoc testimonium datur ${S.genre === 'f' ? 'peregrinae' : 'peregrino'}</p>
   <div class="nom" id="nomC">${E(S.nom) || '&nbsp;'}</div>
   <p class="latin">qui iter Sancti Iacobi, lingua hispanica loquens, a Roncesvalles usque ad Compostellam, per decem mansiones, feliciter perfecit.</p>
   <p style="font-size:14px;margin-top:10px">Traduction : Ce témoignage est remis au pèlerin qui a fait le chemin de Saint-Jacques en parlant espagnol, de Roncesvalles jusqu'à Compostelle, en dix étapes, avec succès.</p>
   <p style="font-size:14px">${E(aujourdhui())}</p>
   <div class="tampons">${D.etapes.map(e => tampon(e, '')).join('')}</div></div>
  <div class="carte pas-imprimer" style="margin-top:14px"><label for="nom"><b>Votre prénom sur la Compostela</b></label>
   <input id="nom" value="${E(S.nom)}" style="display:block;width:100%;font:inherit;padding:10px;border-radius:10px;border:1px solid var(--line-300);margin:6px 0">
   <p class="avis-local">Il reste dans ce téléphone. Ce n'est pas la vraie Compostela : celle-là se reçoit au bureau du pèlerin, à Santiago, credencial en main.</p>
   <button class="btn" onclick="print()">Imprimer</button></div>`;
  $('#nom').oninput = e => { S.nom = e.target.value.slice(0, 60); sauver(); $('#nomC').textContent = S.nom || ' '; };
}

if ('serviceWorker' in navigator) window.addEventListener('load', () => navigator.serviceWorker.register('/sw.js').catch(() => {}));
rendre();
</script>
</body>
</html>
"""

if __name__ == "__main__":
    main()
