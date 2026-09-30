#!/usr/bin/env python3
"""« Montréal en poche » — un guide touristique de Montréal en trois langues.

    python3 build/montreal_app.py     # → modules-autonomes/montreal/index.html

Demande de Daniel, 29 septembre 2026 : « un peu à l'image de Compostelle »,
mais pas pour apprendre une langue — un guide des lieux intéressants de
Montréal (sites, quartiers, smoked meat, bagels, cafés célèbres), en
français, en anglais et en espagnol, avec des croquis du même carnet.

Produite, jamais écrite à la main. Elle lit build/contenu/montreal/ (par
build/montreal_commun.py) ; les croquis viennent de build/montreal_croquis.py,
l'audioguide de build/montreal_audio.py.

CE QUI Y EST
- La langue choisie au premier écran, changeable partout (fr · en · es) : TOUT
  bascule, l'interface comme le contenu.
- Découvrir : 28 lieux en cartes, filtrés par genre (à voir, quartiers,
  manger, cafés et bières), triables « autour de moi ».
- Le lieu : croquis, l'audioguide dans la langue choisie, le texte du guide,
  quoi commander, le « saviez-vous », le conseil d'ici, l'itinéraire.
- La carte (Leaflet + OpenStreetMap), quatre circuits à pied, le passeport à
  tampons (un tampon par lieu visité), le guide pratique, les mots d'ici.

RIEN NE PART : la langue, les tampons et la position (« autour de moi ») ne
quittent jamais le téléphone ; l'itinéraire ouvre Google Maps avec les
coordonnées du LIEU seulement.
"""
import json, pathlib, sys

RACINE = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RACINE / "build"))
import montreal_commun as M  # noqa: E402

SORTIE = RACINE / "modules-autonomes" / "montreal" / "index.html"
BASE = "/modules-autonomes/montreal/"
MEDIA_URL = "/assets/interactive/montreal/"
MEDIA_V = "1"
CATS = ("voir", "quartier", "manger", "boire")


def verifier(lieux, ex):
    ids = [l["id"] for l in lieux]
    assert len(ids) == len(set(ids)), "id en double"
    for l in lieux:
        for k in ("nom", "bref", "texte", "conseil", "anecdote"):
            assert all(l[k].get(g) for g in M.LANGUES), f"{l['id']} : {k} incomplet"
        assert l["cat"] in CATS, l["id"]
        if l["cat"] in ("manger", "boire"):
            assert all(l.get("commander", {}).get(g) for g in M.LANGUES), f"{l['id']} : commander"
        assert (M.MEDIA / "lieux" / f"{l['id']}.jpg").exists(), f"{l['id']} : pas de croquis"
    for c in ex.CIRCUITS:
        assert all(e in ids for e in c["etapes"]), c["id"]
        for g in M.LANGUES:
            assert len(c["liaisons"][g]) == len(c["etapes"]) - 1, f"{c['id']} {g} : liaisons"


def donnees():
    lieux = M.lieux()
    ex = M.charger("extras")
    verifier(lieux, ex)
    audio = M.MEDIA / "audio"
    for l in lieux:
        l.pop("verifier", None)
        l["son"] = [g for g in M.LANGUES if (audio / g / f"{l['id']}.mp3").exists()]
    mots = []
    for i, m in enumerate(ex.MOTS):
        mots.append(dict(m, son=(audio / "mots" / f"{i:02d}.mp3").exists()))
    scenes = M.scenes()
    verifier_scenes(scenes, {l["id"] for l in lieux})
    for sc in scenes:
        sc["img"] = sc["lieu"] or sc["id"]
        sc["son"] = all((audio / f"scenes/{sc['id']}/{n}.mp3").exists() for n in noms_sons(sc))
    fam = M.enfants()
    for e in fam:
        assert e["lieu"] in {l["id"] for l in lieux}, e["lieu"]
        assert (M.MEDIA / "filou" / f"{e['pose']}-d.webp").exists(), f"{e['lieu']} : pose {e['pose']}"
        e["son"] = [g for g in M.LANGUES if all((audio / f"famille/{g}/{e['lieu']}-{x}.mp3").exists() for x in "rebd")]
    return {"lieux": lieux, "circuits": ex.CIRCUITS, "pratique": ex.PRATIQUE, "mots": mots, "scenes": scenes,
            "famille": fam, "filou": M.FILOU_GENERIQUE,
            "filouSons": [f"{g}/{k}" for g in M.LANGUES for k in M.FILOU_GENERIQUE if (audio / f"famille/{g}/{k}.mp3").exists()]}


def noms_sons(sc):
    """Les sons d'une scène, dans la même convention que montreal_commun.extraits()."""
    n = [f"t{k}" if "dit" in t else f"t{k}c" for k, t in enumerate(sc["tours"])]
    return n + [f"p{i}" for i in range(len(sc["phrases"]))]


def verifier_scenes(scenes, lieux):
    """Ce qui ne lève aucune erreur à l'écran et casse pourtant la scène."""
    ids = [sc["id"] for sc in scenes]
    assert len(ids) == len(set(ids)), "scène en double"
    for sc in scenes:
        i = sc["id"]
        assert sc["lieu"] is None or sc["lieu"] in lieux, f"{i} : lieu inconnu {sc['lieu']}"
        assert sc["lieu"] or (M.MEDIA / "lieux" / f"{i}.jpg").exists(), f"{i} : pas de croquis"
        for k in ("titre", "but", "note"):
            assert all(sc[k].get(g) for g in M.LANGUES), f"{i} : {k}"
        t = sc["tours"]
        assert "dit" in t[0] and "dit" in t[-1], f"{i} : commence et finit par le personnage"
        for a, b in zip(t, t[1:]):
            assert ("dit" in a) != ("dit" in b), f"{i} : les tours doivent alterner"
        for tour in t:
            if "dit" in tour:
                assert tour["sens"].get("en") and tour["sens"].get("es"), f"{i} : sens"
            else:
                ch = tour["choix"]
                assert len(ch) == (2 if sc.get("enfant") else 3), f"{i} : nombre de choix"
                assert ch[0][2] is None and all(c[2] for c in ch[1:]), f"{i} : la bonne d'abord, une rétroaction par erreur"
                assert all(all(c[2].get(g) for g in M.LANGUES) for c in ch[1:]), f"{i} : rétroaction incomplète"


def icones():
    """L'icône : le croquis du Stade (sa tour se lit à 48 px), recadré carré."""
    from PIL import Image
    src = Image.open(M.MEDIA / "lieux" / "parc-olympique.png").convert("RGB")
    w, h = src.size
    carre = src.crop(((w - h) // 2 + int(h * .08), 0, (w - h) // 2 + int(h * .08) + h, h))
    dest = SORTIE.parent / "icones"; dest.mkdir(parents=True, exist_ok=True)
    for nom, cote, part in (("icone-192.png", 192, .98), ("icone-512.png", 512, .98),
                            ("icone-maskable-512.png", 512, .72), ("icone-180.png", 180, .98)):
        im = Image.new("RGB", (cote, cote), "#FFFFFF")
        c = carre.resize((round(cote * part),) * 2, Image.LANCZOS)
        im.paste(c, ((cote - c.width) // 2, (cote - c.height) // 2))
        im.save(dest / nom, optimize=True)
    (SORTIE.parent / "manifest.webmanifest").write_text(json.dumps({
        "name": "Montréal en poche", "short_name": "Montréal",
        "description": "Montreal in your pocket · Montréal en el bolsillo",
        "lang": "fr-CA", "dir": "ltr", "start_url": BASE, "scope": BASE,
        "display": "standalone", "orientation": "portrait",
        "background_color": "#F6F1E7", "theme_color": "#F6F1E7",
        "icons": [{"src": BASE + "icones/icone-192.png", "sizes": "192x192", "type": "image/png", "purpose": "any"},
                  {"src": BASE + "icones/icone-512.png", "sizes": "512x512", "type": "image/png", "purpose": "any"},
                  {"src": BASE + "icones/icone-maskable-512.png", "sizes": "512x512", "type": "image/png", "purpose": "maskable"}],
    }, ensure_ascii=False, indent=2), encoding="utf-8")


def main():
    icones()
    D = donnees()
    page = (PAGE.replace("/*DONNEES*/", json.dumps(D, ensure_ascii=False).replace("</", "<\\/"))
                .replace("%MEDIA%", MEDIA_URL).replace("%V%", MEDIA_V).replace("%BASE%", BASE))
    SORTIE.parent.mkdir(parents=True, exist_ok=True)
    SORTIE.write_text(page, encoding="utf-8")
    n = len(D["lieux"]); s = sum(len(l["son"]) for l in D["lieux"])
    print(f"{SORTIE.relative_to(RACINE)} : {n} lieux, {len(D['circuits'])} circuits, "
          f"{s}/{n * 3} sons de lieux, {len(page) // 1024} Ko")


PAGE = r"""<!doctype html>
<html lang="fr-CA">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="robots" content="noindex">
<title>Montréal en poche</title>
<meta name="theme-color" content="#F6F1E7">
<link rel="manifest" href="%BASE%manifest.webmanifest">
<link rel="apple-touch-icon" href="%BASE%icones/icone-180.png">
<link rel="icon" href="%BASE%icones/icone-192.png">
<link rel="stylesheet" href="/assets/design-system/tokens/fonts.css">
<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Fredoka:wght@500;600;700&display=swap">
<style>
:root{
  --fond:#F6F1E7; --carte:#FFFFFF; --encre:#1E2733; --doux:#5D6572; --filet:#E2D9C6;
  --rouge:#B3262E; --rouge-pale:#F6E3E1; --bleu:#1F4E79;
  --c-voir:#1F4E79; --c-quartier:#2F6B45; --c-manger:#A8432A; --c-boire:#7A4E14;
  --ombre:0 1px 2px rgba(30,39,51,.06),0 4px 14px rgba(30,39,51,.07);
  --r:16px;
}
*{box-sizing:border-box}
[hidden]{display:none!important}
html,body{margin:0;background:var(--fond);color:var(--encre)}
body{font-family:Nunito,system-ui,sans-serif;font-size:17px;line-height:1.5;-webkit-text-size-adjust:100%;
  padding-bottom:calc(76px + env(safe-area-inset-bottom))}
button{font:inherit;color:inherit;cursor:pointer}
a{color:var(--bleu)}
img{max-width:100%;height:auto;display:block}
.col{max-width:720px;margin:0 auto;padding:0 16px}

/* En-tête */
header.barre{position:sticky;top:0;z-index:30;background:rgba(246,241,231,.94);backdrop-filter:blur(8px);
  -webkit-backdrop-filter:blur(8px);border-bottom:1px solid var(--filet);padding-top:env(safe-area-inset-top)}
header.barre .col{display:flex;align-items:center;gap:10px;height:56px}
.marque{font-weight:900;font-size:19px;letter-spacing:-.01em;text-decoration:none;color:var(--encre);display:flex;align-items:center;gap:8px;min-width:0}
.marque .pt{width:10px;height:10px;border-radius:50%;background:var(--rouge);flex:none}
.marque span{white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.retour{border:0;background:none;display:flex;align-items:center;gap:4px;font-weight:800;padding:8px 6px 8px 0;min-height:44px;color:var(--encre)}
.langues{margin-left:auto;display:flex;background:#fff;border:1px solid var(--filet);border-radius:999px;padding:3px;flex:none}
.langues button{border:0;background:none;font-weight:800;font-size:14px;padding:6px 11px;border-radius:999px;min-height:34px;color:var(--doux)}
.langues button[aria-pressed=true]{background:var(--encre);color:#fff}

/* Onglets du bas */
nav.onglets{position:fixed;left:0;right:0;bottom:0;z-index:40;background:#fff;border-top:1px solid var(--filet);
  padding-bottom:env(safe-area-inset-bottom)}
nav.onglets .col{display:grid;grid-template-columns:repeat(5,1fr);padding:0 4px}
nav.onglets a{display:flex;flex-direction:column;align-items:center;gap:2px;padding:9px 0 8px;text-decoration:none;
  color:var(--doux);font-size:11.5px;font-weight:800;min-height:60px}
nav.onglets a svg{width:24px;height:24px}
nav.onglets a[aria-current=page]{color:var(--rouge)}

/* Accueil */
.hero{position:relative;margin:14px 0 6px;border-radius:var(--r);overflow:hidden;background:#fff;box-shadow:var(--ombre)}
.hero img{width:100%;aspect-ratio:3/2;object-fit:cover}
.hero .txt{padding:14px 16px 16px}
.hero h1{margin:0;font-size:28px;line-height:1.1;font-weight:900;letter-spacing:-.02em}
.hero p{margin:6px 0 0;color:var(--doux)}
.progres{display:flex;align-items:center;gap:12px;background:#fff;border-radius:var(--r);padding:12px 14px;margin:12px 0;
  box-shadow:var(--ombre);text-decoration:none;color:inherit}
.progres .rond{flex:none}
.progres b{display:block;font-weight:900}
.progres small{color:var(--doux);font-size:14px}
h2.sec{font-size:21px;font-weight:900;margin:26px 0 10px;letter-spacing:-.01em}
.puces{display:flex;gap:8px;overflow-x:auto;padding:2px 0 8px;margin:0 -16px;padding-left:16px;padding-right:16px;scrollbar-width:none}
.puces::-webkit-scrollbar{display:none}
.puces button{flex:none;border:1.5px solid var(--filet);background:#fff;border-radius:999px;padding:8px 14px;font-weight:800;font-size:15px;min-height:42px;white-space:nowrap}
.puces button[aria-pressed=true]{background:var(--encre);border-color:var(--encre);color:#fff}
.puces button.pres{border-style:dashed}
.puces button.pres[aria-pressed=true]{border-style:solid}
.liste{display:grid;gap:14px;grid-template-columns:1fr}
@media (min-width:640px){.liste{grid-template-columns:1fr 1fr}}
.carte-lieu{display:block;background:#fff;border-radius:var(--r);overflow:hidden;box-shadow:var(--ombre);text-decoration:none;color:inherit;position:relative}
.carte-lieu img{width:100%;aspect-ratio:3/2;object-fit:cover;background:#fff}
.carte-lieu .t{padding:10px 14px 14px}
.carte-lieu h3{margin:4px 0 2px;font-size:19px;line-height:1.2;font-weight:900}
.carte-lieu p{margin:0;color:var(--doux);font-size:15px}
.carte-lieu .dist{position:absolute;top:10px;right:10px;background:rgba(255,255,255,.95);border-radius:999px;padding:3px 10px;font-size:13px;font-weight:800}
.carte-lieu .vu{position:absolute;top:8px;left:8px}
.etq{display:inline-block;font-size:12.5px;font-weight:900;letter-spacing:.04em;text-transform:uppercase}
.etq.voir{color:var(--c-voir)}.etq.quartier{color:var(--c-quartier)}.etq.manger{color:var(--c-manger)}.etq.boire{color:var(--c-boire)}
.meta{color:var(--doux);font-size:14px;margin-top:4px}

/* Lieu */
.lieu-img{margin:14px -16px 0;background:#fff}
@media (min-width:720px){.lieu-img{margin:14px 0 0;border-radius:var(--r);overflow:hidden}}
.lieu-img img{width:100%;aspect-ratio:3/2;object-fit:cover}
.lieu h1{font-size:30px;line-height:1.1;font-weight:900;margin:14px 0 4px;letter-spacing:-.02em}
.lieu .bref{font-size:18px;color:var(--doux);margin:0 0 12px}
.fiche{display:grid;grid-template-columns:auto 1fr;gap:4px 12px;background:#fff;border-radius:var(--r);padding:12px 14px;box-shadow:var(--ombre);font-size:15.5px}
.fiche dt{color:var(--doux);font-weight:700}
.fiche dd{margin:0;font-weight:700}
.ecoute{display:flex;align-items:center;gap:12px;width:100%;border:0;background:var(--encre);color:#fff;border-radius:var(--r);
  padding:12px 14px;margin:14px 0 4px;text-align:left;min-height:64px}
.ecoute .ic{width:40px;height:40px;border-radius:50%;background:var(--rouge);display:grid;place-items:center;flex:none}
.ecoute .ic svg{width:20px;height:20px;fill:#fff}
.ecoute b{display:block;font-weight:900}
.ecoute small{opacity:.8;font-size:14px}
.ecoute .barre-son{height:4px;background:rgba(255,255,255,.25);border-radius:2px;margin-top:6px;overflow:hidden}
.ecoute .barre-son i{display:block;height:100%;width:0;background:#fff}
.vitesse{display:flex;gap:6px;justify-content:flex-end;margin-bottom:6px}
.vitesse button{border:1px solid var(--filet);background:#fff;border-radius:999px;font-size:13px;font-weight:800;padding:4px 10px;min-height:32px}
.vitesse button[aria-pressed=true]{background:var(--encre);color:#fff;border-color:var(--encre)}
.texte p{margin:0 0 14px;font-size:17.5px;line-height:1.62}
.encart{border-radius:var(--r);padding:14px 16px;margin:14px 0;background:#fff;box-shadow:var(--ombre)}
.encart h3{margin:0 0 4px;font-size:14px;font-weight:900;letter-spacing:.05em;text-transform:uppercase}
.encart p{margin:0}
.encart.commander{background:#FFF8EC;border:1.5px solid #EAD7B0;box-shadow:none}
.encart.commander h3{color:var(--c-manger)}
.encart.savoir h3{color:var(--bleu)}
.encart.conseil h3{color:var(--c-quartier)}
.actions{display:grid;gap:10px;margin:18px 0}
.bouton{display:flex;align-items:center;justify-content:center;gap:8px;border-radius:14px;padding:13px 16px;font-weight:900;
  text-decoration:none;min-height:52px;border:2px solid var(--encre);background:#fff;color:var(--encre);text-align:center}
.bouton.plein{background:var(--rouge);border-color:var(--rouge);color:#fff}
.bouton.fait{background:var(--rouge-pale);border-color:var(--rouge);color:var(--rouge)}
.voisins{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin:8px 0 24px}
.voisins a{background:#fff;border-radius:14px;padding:10px 12px;text-decoration:none;color:inherit;box-shadow:var(--ombre);font-size:14px}
.voisins a b{display:block;font-size:15.5px}
.voisins a.suiv{text-align:right}

/* Carte */
#carte{height:calc(100vh - 56px - 76px);height:calc(100dvh - 56px - 76px - env(safe-area-inset-top) - env(safe-area-inset-bottom))}
.mini-carte{height:260px;border-radius:var(--r);overflow:hidden;margin:12px 0;box-shadow:var(--ombre)}
.epingle{width:26px;height:26px;border-radius:50% 50% 50% 0;transform:rotate(-45deg);border:2.5px solid #fff;box-shadow:0 1px 4px rgba(0,0,0,.35)}
.epingle.num{display:grid;place-items:center}
.epingle.num span{transform:rotate(45deg);color:#fff;font:900 12px Nunito,system-ui,sans-serif}
.leaflet-popup-content{font-family:Nunito,system-ui,sans-serif;margin:10px 12px}
.pop img{width:180px;aspect-ratio:3/2;object-fit:cover;border-radius:8px;margin-bottom:6px}
.pop b{display:block;font-size:15px}
.pop a{font-weight:800}
.legende{position:absolute;z-index:500;left:10px;right:10px;bottom:10px;display:flex;gap:6px;flex-wrap:wrap;justify-content:center;pointer-events:none}
.legende span{background:#fff;border-radius:999px;padding:4px 10px;font-size:12.5px;font-weight:800;box-shadow:var(--ombre);display:flex;align-items:center;gap:5px}
.legende i{width:10px;height:10px;border-radius:50%;display:inline-block}

/* Circuits */
.circuit-carte{display:block;background:#fff;border-radius:var(--r);box-shadow:var(--ombre);overflow:hidden;text-decoration:none;color:inherit}
.circuit-carte .imgs{display:grid;grid-template-columns:repeat(3,1fr);gap:2px;background:#fff}
.circuit-carte .imgs img{aspect-ratio:1;object-fit:cover;width:100%}
.circuit-carte .t{padding:12px 14px 14px}
.circuit-carte h3{margin:0 0 2px;font-size:19px;font-weight:900}
.circuit-carte p{margin:4px 0 0;color:var(--doux);font-size:15px}
ol.parcours{list-style:none;padding:0;margin:12px 0 24px}
ol.parcours li.etape a{display:flex;gap:12px;align-items:center;background:#fff;border-radius:14px;padding:8px;box-shadow:var(--ombre);text-decoration:none;color:inherit}
ol.parcours li.etape img{width:84px;aspect-ratio:3/2;object-fit:cover;border-radius:10px;flex:none}
ol.parcours li.etape b{display:block;font-size:16.5px;line-height:1.2}
ol.parcours li.etape small{color:var(--doux);font-size:13.5px}
ol.parcours .n{width:28px;height:28px;border-radius:50%;background:var(--rouge);color:#fff;font-weight:900;font-size:14px;display:grid;place-items:center;flex:none}
ol.parcours li.liaison{margin:0 0 0 22px;padding:10px 0 10px 22px;border-left:3px dotted var(--filet);color:var(--doux);font-size:14.5px}

/* Passeport */
.passeport{background:#FFFDF7;border:1.5px solid var(--filet);border-radius:var(--r);padding:16px 12px;margin:14px 0 24px;
  background-image:repeating-linear-gradient(0deg,transparent 0 31px,rgba(179,38,46,.05) 31px 32px)}
.passeport .grille{display:grid;grid-template-columns:repeat(3,1fr);gap:10px}
@media (min-width:560px){.passeport .grille{grid-template-columns:repeat(4,1fr)}}
.tampon{display:block;text-decoration:none;color:inherit;text-align:center}
.tampon svg{width:100%;height:auto;max-width:120px}
.tampon.vide svg{opacity:.55}
.passeport h2{margin:0 0 4px;font-size:22px;font-weight:900;text-align:center}
.passeport .sous{text-align:center;color:var(--doux);margin:0 0 14px}
.palier{background:var(--rouge-pale);color:var(--rouge);border-radius:14px;padding:10px 14px;font-weight:800;margin:0 0 14px;text-align:center}

/* Pratique, mots */
details.fichep{background:#fff;border-radius:14px;box-shadow:var(--ombre);margin:0 0 10px}
details.fichep summary{list-style:none;padding:14px 16px;font-weight:900;font-size:17px;display:flex;justify-content:space-between;align-items:center;gap:8px;cursor:pointer;min-height:52px}
details.fichep summary::-webkit-details-marker{display:none}
details.fichep summary::after{content:"+";font-size:22px;color:var(--rouge);flex:none}
details.fichep[open] summary::after{content:"–"}
details.fichep p{margin:0;padding:0 16px 16px;line-height:1.6}
.mot{background:#fff;border-radius:14px;box-shadow:var(--ombre);padding:12px 14px;margin:0 0 10px;display:grid;grid-template-columns:1fr auto;gap:2px 10px;align-items:start}
.mot b{font-size:19px;font-weight:900;color:var(--rouge)}
.mot .sens{grid-column:1;margin:0;font-size:15.5px}
.mot .ex{grid-column:1;margin:4px 0 0;font-style:italic;color:var(--doux);font-size:15px}
.mot button{grid-row:1/4;grid-column:2;border:0;background:var(--encre);color:#fff;width:44px;height:44px;border-radius:50%;display:grid;place-items:center}
.mot button svg{width:18px;height:18px;fill:#fff}
.intro{color:var(--doux);margin:4px 0 14px}
.plus-liens{display:grid;gap:10px;margin:14px 0}
.plus-liens a{display:flex;align-items:center;gap:14px;background:#fff;border-radius:14px;padding:14px 16px;box-shadow:var(--ombre);text-decoration:none;color:inherit;font-weight:900;font-size:17px;min-height:64px}
.plus-liens a small{display:block;font-weight:600;color:var(--doux);font-size:14px}
.pied{color:var(--doux);font-size:13px;text-align:center;margin:28px 0 12px}

/* Parler : les scènes */
.scene-carte{display:flex;gap:12px;align-items:center;background:#fff;border-radius:var(--r);box-shadow:var(--ombre);padding:10px;text-decoration:none;color:inherit}
.scene-carte img{width:110px;aspect-ratio:3/2;object-fit:cover;border-radius:10px;flex:none}
.scene-carte b{display:block;font-size:17px;line-height:1.25}
.scene-carte small{color:var(--doux);font-size:14px;display:block;margin-top:2px}
.etoiles{color:#C9A227;font-size:15px;letter-spacing:1px;white-space:nowrap}
.etoiles .v{color:#D9D2C2}
.invite{display:flex;gap:12px;align-items:center;background:#FFF8EC;border:1.5px solid #EAD7B0;border-radius:var(--r);padding:12px 14px;margin:14px 0;text-decoration:none;color:inherit}
.invite b{display:block}
.invite small{color:var(--doux)}
.invite .fl{margin-left:auto;font-weight:900;color:var(--rouge);font-size:22px}
.but{background:#fff;border-radius:var(--r);box-shadow:var(--ombre);padding:12px 14px;margin:12px 0}
.but small{display:block;font-size:12.5px;font-weight:900;letter-spacing:.05em;text-transform:uppercase;color:var(--rouge)}
.fil-scene{display:flex;flex-direction:column;gap:10px;margin:14px 0}
.bulle{max-width:88%;border-radius:18px;padding:10px 14px;position:relative}
.bulle.perso{align-self:flex-start;background:#fff;box-shadow:var(--ombre);border-bottom-left-radius:4px}
.bulle.moi{align-self:flex-end;background:var(--encre);color:#fff;border-bottom-right-radius:4px}
.bulle .qui{display:block;font-size:12.5px;font-weight:900;opacity:.7;margin-bottom:2px}
.bulle .fr{font-size:18px;font-weight:700;line-height:1.35}
.bulle .tr{display:block;font-size:14.5px;opacity:.75;margin-top:3px}
.bulle .rej{display:flex;gap:6px;margin-top:6px}
.bulle .rej button{border:0;border-radius:999px;padding:4px 10px;font-size:13px;font-weight:800;min-height:32px;background:var(--fond);color:var(--encre)}
.bulle.moi .rej button{background:rgba(255,255,255,.15);color:#fff}
.retro{align-self:stretch;background:var(--rouge-pale);color:#6E1A1F;border-radius:14px;padding:10px 14px;font-size:15.5px}
.choix-scene{display:grid;gap:8px;margin:6px 0 18px}
.choix-scene button{text-align:left;border:2px solid var(--encre);background:#fff;border-radius:14px;padding:11px 14px;min-height:52px}
.choix-scene button b{display:block;font-size:17px;line-height:1.3}
.choix-scene button small{display:block;color:var(--doux);font-size:14px;margin-top:2px}
.choix-scene button.faux{border-color:#D9B3B5;background:#FBF3F3;opacity:.7}
.choix-scene .consigne{font-weight:900;margin:4px 0 2px}
.repete{background:#fff;border-radius:14px;box-shadow:var(--ombre);padding:12px 14px;margin:0 0 18px}
.repete p{margin:0 0 10px}
.fin-scene{background:#fff;border-radius:var(--r);box-shadow:var(--ombre);padding:18px 16px;margin:10px 0 24px;text-align:center}
.fin-scene .grandes{font-size:38px;color:#C9A227;letter-spacing:4px}
.fin-scene .grandes .v{color:#E4DDCD}
.fin-scene h2{margin:4px 0 6px;font-size:24px}
.phrases{list-style:none;padding:0;margin:14px 0;text-align:left}
.phrases li{display:flex;gap:10px;align-items:center;padding:8px 0;border-top:1px solid var(--filet)}
.phrases li button{border:0;background:var(--encre);color:#fff;width:40px;height:40px;border-radius:50%;display:grid;place-items:center;flex:none}
.phrases li button svg{width:16px;height:16px;fill:#fff}
.phrases b{display:block}
.phrases small{color:var(--doux)}
.bascule-tr{display:flex;align-items:center;gap:8px;font-size:14.5px;font-weight:800;color:var(--doux);margin:4px 0}
.bascule-tr input{width:20px;height:20px;accent-color:var(--encre)}
.circuits-rangee{display:grid;grid-auto-flow:column;grid-auto-columns:78%;gap:12px;overflow-x:auto;margin:0 -16px;padding:2px 16px 10px;scrollbar-width:none}
.circuits-rangee::-webkit-scrollbar{display:none}
@media (min-width:640px){.circuits-rangee{grid-auto-columns:46%}}

/* ===== Mode famille : habit « Bonbon » (A), choisi le 30 sept. 2026 ===== */
body.famille{--fond:#FFF6D6;--encre:#2B1B4A;--doux:#6E5F8C;--filet:#F0DFA6;--rouge:#FF4F7B;--rouge-pale:#FFE3EA;--bleu:#00897E;
  --framb:#FF4F7B;--turq:#00B8A9;--soleil:#FFC23D;--ombre:0 4px 0 #2B1B4A;--r:24px;font-family:Fredoka,Nunito,system-ui,sans-serif}
body.famille header.barre{background:#FF4F7B;border-bottom:0}
body.famille .marque{color:#fff;font-weight:700}
body.famille .marque img{width:36px;height:36px;object-fit:contain}
body.famille .langues{border:0}
body.famille .langues button[aria-pressed=true]{background:var(--encre)}
body.famille nav.onglets{background:var(--encre);border-top:0}
body.famille nav.onglets a{color:#B9AEDB;font-family:Fredoka,Nunito,sans-serif;font-weight:600}
body.famille nav.onglets a[aria-current=page]{color:var(--soleil)}
body.famille .bouton{border:3px solid var(--encre);box-shadow:0 4px 0 var(--encre);border-radius:18px;font-weight:700}
body.famille .bouton.plein{background:var(--framb);border-color:var(--encre)}
.cadre-b{background:#fff;border:3px solid var(--encre);border-radius:var(--r);box-shadow:0 4px 0 var(--encre)}
.f-hero{display:flex;align-items:flex-end;gap:2px;margin:16px 0 8px;min-height:170px}
.f-hero img{width:44%;max-width:190px;flex:none;margin-bottom:-8px}
.f-bulle{padding:14px 16px;font-size:19px;line-height:1.3;font-weight:600;margin-bottom:40px;position:relative}
.f-bulle button{margin-top:8px}
.btn-son{display:inline-flex;align-items:center;gap:8px;border:3px solid var(--encre);background:var(--framb);color:#fff;border-radius:999px;
  padding:8px 16px;font:700 17px Fredoka,Nunito,sans-serif;box-shadow:0 4px 0 var(--encre);min-height:48px}
.btn-son svg{width:18px;height:18px;fill:#fff}
.btn-son.turq{background:var(--turq)}
.btn-son:active,.rep-f button:active,body.famille .bouton:active{transform:translateY(3px);box-shadow:0 1px 0 var(--encre)}
.f-prog{display:flex;align-items:center;gap:10px;padding:12px 14px;margin:12px 0;text-decoration:none;color:inherit;font-weight:600}
.f-prog .jauge{flex:1;height:18px;border:3px solid var(--encre);border-radius:999px;background:#FFE39A;overflow:hidden}
.f-prog .jauge i{display:block;height:100%;background:var(--turq)}
.f-lieux{display:grid;gap:14px;grid-template-columns:1fr}
@media (min-width:640px){.f-lieux{grid-template-columns:1fr 1fr}}
.f-lieu{display:flex;gap:12px;align-items:center;padding:8px;text-decoration:none;color:inherit;position:relative}
.f-lieu>img{width:120px;aspect-ratio:3/2;object-fit:cover;border-radius:16px;flex:none}
.f-lieu b{display:block;font-size:19px;line-height:1.15}
.f-lieu small{color:var(--doux);font-size:14.5px}
.f-lieu .gagne{position:absolute;right:-6px;top:-10px;width:52px;transform:rotate(10deg)}
.f-titre{font:700 26px/1.1 Fredoka,Nunito,sans-serif;margin:26px 0 12px}
.f-raconte{display:flex;gap:8px;align-items:flex-start;margin:14px 0}
.f-raconte img{width:96px;flex:none}
.f-raconte .f-bulle{margin:0;flex:1;font-size:17.5px}
.f-enigme{background:#D8F6F2;border:3px solid var(--encre);border-radius:var(--r);padding:14px;margin:26px 0 14px;position:relative}
.f-enigme>img{position:absolute;right:6px;top:-40px;width:92px}
.f-enigme h3{margin:0;font:700 24px Fredoka,sans-serif;color:#00796F}
.f-enigme .q{margin:6px 90px 10px 0;font-size:18px;font-weight:600;line-height:1.3}
.rep-f{display:grid;gap:9px;margin-top:10px}
.rep-f button{font:700 18px Fredoka,Nunito,sans-serif;border:3px solid var(--encre);background:#fff;color:var(--encre);border-radius:18px;
  padding:12px;box-shadow:0 4px 0 var(--encre);min-height:54px}
.rep-f button.ok{background:var(--turq);color:#fff}
.rep-f button.non{background:#FFE3EA;border-color:#C98AA0;box-shadow:0 4px 0 #C98AA0;color:#8A5068;animation:secoue .35s}
@keyframes secoue{25%{transform:translateX(-6px)}75%{transform:translateX(6px)}}
.f-bravo{display:flex;gap:10px;align-items:center;margin-top:12px;font-size:17px;font-weight:600}
.f-bravo img{width:80px;flex:none}
.f-defi{background:#FFF0BF;border:3px dashed #E0A21C;border-radius:var(--r);padding:14px;margin:14px 0}
.f-defi h3{margin:0 0 4px;font:700 20px Fredoka,sans-serif;color:#B7791F}
.f-defi p{margin:0 0 8px;font-size:17px}
.f-gagne{text-align:center;padding:16px;margin:14px 0}
.f-gagne h3{margin:6px 0 0;font:700 21px Fredoka,sans-serif}
.autoc{display:inline-grid;place-items:center;position:relative;width:118px;aspect-ratio:1;border-radius:50%;background:#fff;
  border:5px solid var(--soleil);box-shadow:0 4px 0 #E0A21C}
.autoc img{width:80%}
.autoc em{position:absolute;bottom:-10px;left:50%;transform:translateX(-50%);background:var(--framb);color:#fff;font:700 12px Fredoka,sans-serif;
  font-style:normal;border-radius:999px;padding:2px 9px;white-space:nowrap;max-width:130px;overflow:hidden;text-overflow:ellipsis;border:2px solid var(--encre)}
.autoc.vide{background:#FFF0BF;border:3px dashed #E8C765;box-shadow:none}
.autoc.vide span{font:700 30px Fredoka,sans-serif;color:#C9A94A}
.autoc.nouveau{animation:colle .6s cubic-bezier(.3,1.6,.5,1)}
@keyframes colle{0%{transform:scale(.2) rotate(-40deg);opacity:0}100%{transform:scale(1) rotate(0)}}
.carnet-f{display:grid;grid-template-columns:repeat(2,1fr);gap:26px 12px;justify-items:center;margin:18px 0 26px}
@media (min-width:520px){.carnet-f{grid-template-columns:repeat(3,1fr)}}
.carnet-f a{text-decoration:none;color:inherit}
.carnet-f a:nth-child(3n+1) .autoc:not(.vide){transform:rotate(-7deg)}.carnet-f a:nth-child(3n+2) .autoc:not(.vide){transform:rotate(5deg)}
.f-diplome{padding:16px;margin:10px 0 24px;text-align:center}
.f-diplome input{width:100%;max-width:320px;font:600 20px Fredoka,sans-serif;border:3px solid var(--encre);border-radius:14px;padding:10px 12px;margin:10px 0;text-align:center}
.bascule-f{display:flex;gap:14px;align-items:center;padding:12px 14px;margin:14px 0;text-decoration:none;color:#2B1B4A;
  background:#FFF6D6;border:3px solid #2B1B4A;border-radius:22px;box-shadow:0 4px 0 #2B1B4A;font-family:Fredoka,Nunito,sans-serif}
.bascule-f img{width:74px;flex:none}
.bascule-f b{display:block;font-size:20px;font-weight:700;color:#FF4F7B}
.bascule-f small{font-size:15px;color:#6E5F8C}
.lien-grands{display:block;text-align:center;font-weight:600;margin:10px 0 24px;color:var(--doux)}
#diplome{display:none}
@media print{
  body.imprime *{visibility:hidden}
  body.imprime #diplome,body.imprime #diplome *{visibility:visible}
  body.imprime #diplome{display:block;position:fixed;inset:0;padding:40px;text-align:center;font-family:Fredoka,Nunito,sans-serif;color:#2B1B4A}
  body.imprime nav.onglets{display:none}
  #diplome .cadre{border:8px solid #FF4F7B;border-radius:30px;padding:36px 28px;outline:4px solid #00B8A9;outline-offset:6px}
  #diplome h1{font-size:40px;margin:10px 0 0}#diplome .nom{font-size:46px;color:#FF4F7B;margin:18px 0}
  #diplome .st{display:flex;flex-wrap:wrap;justify-content:center;gap:10px;margin:20px 0}#diplome .st img{width:70px}
  #diplome img.f{width:170px}
}

/* Choix de la langue */
.bienvenue{min-height:100vh;display:flex;flex-direction:column;justify-content:center;padding:24px 16px}
.bienvenue img{border-radius:var(--r);margin:0 auto 20px;width:100%;max-width:520px;box-shadow:var(--ombre)}
.bienvenue h1{text-align:center;margin:0;font-size:32px;font-weight:900;letter-spacing:-.02em}
.bienvenue p{text-align:center;color:var(--doux);margin:6px 0 22px}
.bienvenue .choix{display:grid;gap:10px;max-width:380px;margin:0 auto;width:100%}
.bienvenue .choix button{border:2px solid var(--encre);background:#fff;border-radius:14px;padding:14px;font-weight:900;font-size:19px;min-height:58px}
.bienvenue .choix button:hover{background:var(--encre);color:#fff}
.toast{position:fixed;left:50%;bottom:calc(92px + env(safe-area-inset-bottom));transform:translateX(-50%);background:var(--encre);color:#fff;
  padding:10px 18px;border-radius:999px;font-weight:800;z-index:60;box-shadow:var(--ombre);max-width:calc(100% - 32px);text-align:center}
</style>
</head>
<body>
<div id="app"></div>
<nav class="onglets" id="onglets" hidden><div class="col"></div></nav>
<audio id="lecteur" preload="none"></audio>
<div id="diplome" aria-hidden="true"></div>
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
<script>
const D = /*DONNEES*/;
const MEDIA = '%MEDIA%', V = '%V%';
const LANGS = ['fr', 'en', 'es'];
const LOC = {fr: 'fr-CA', en: 'en-CA', es: 'es-MX'};
const COUL = {voir: '#1F4E79', quartier: '#2F6B45', manger: '#A8432A', boire: '#7A4E14'};

const T = {
  titre: {fr: 'Montréal en poche', en: 'Montreal in Your Pocket', es: 'Montreal en el bolsillo'},
  accroche: {fr: 'Les lieux à voir, les quartiers, le smoked meat et les cafés qui font la ville — avec un guide qui vous parle.',
             en: 'The sights, the neighbourhoods, the smoked meat and the cafés that make the city — with a guide who talks to you.',
             es: 'Los lugares, los barrios, el smoked meat y los cafés que hacen la ciudad, con un guía que le habla.'},
  choisir: {fr: 'Choisissez votre langue', en: 'Choose your language', es: 'Elija su idioma'},
  decouvrir: {fr: 'Découvrir', en: 'Discover', es: 'Descubrir'},
  carte: {fr: 'Carte', en: 'Map', es: 'Mapa'},
  circuits: {fr: 'Circuits', en: 'Walks', es: 'Recorridos'},
  passeport: {fr: 'Passeport', en: 'Passport', es: 'Pasaporte'},
  plus: {fr: 'Pratique', en: 'Tips', es: 'Práctico'},
  tout: {fr: 'Tout', en: 'All', es: 'Todo'},
  voir: {fr: 'À voir', en: 'Sights', es: 'Qué ver'},
  quartier: {fr: 'Quartiers', en: 'Neighbourhoods', es: 'Barrios'},
  manger: {fr: 'Manger', en: 'Eat', es: 'Comer'},
  boire: {fr: 'Cafés et bières', en: 'Coffee & beer', es: 'Cafés y cervezas'},
  cat1: {voir: {fr: 'À voir', en: 'Sight', es: 'Qué ver'}, quartier: {fr: 'Quartier', en: 'Neighbourhood', es: 'Barrio'},
         manger: {fr: 'Manger', en: 'Eat', es: 'Comer'}, boire: {fr: 'Café, bière', en: 'Coffee, beer', es: 'Café, cerveza'}},
  pres: {fr: 'Autour de moi', en: 'Near me', es: 'Cerca de mí'},
  presRefus: {fr: 'Position non disponible : la liste reste dans l’ordre du guide.', en: 'Location unavailable: the list keeps the guide’s order.', es: 'Ubicación no disponible: la lista sigue el orden de la guía.'},
  lieux: {fr: 'lieux', en: 'places', es: 'lugares'},
  tampons: {fr: 'tampons', en: 'stamps', es: 'sellos'},
  monPass: {fr: 'Mon passeport de Montréal', en: 'My Montreal passport', es: 'Mi pasaporte de Montreal'},
  passInvite: {fr: 'Un tampon par lieu visité. Touchez « J’y suis allé » sur la page d’un lieu.', en: 'One stamp per place you visit. Tap “I’ve been here” on a place’s page.', es: 'Un sello por lugar visitado. Toque «Ya estuve aquí» en la página de un lugar.'},
  quartierL: {fr: 'Quartier', en: 'Area', es: 'Barrio'},
  metro: {fr: 'Métro', en: 'Metro', es: 'Metro'},
  adresse: {fr: 'Adresse', en: 'Address', es: 'Dirección'},
  duree: {fr: 'Sur place', en: 'Time there', es: 'Tiempo'},
  ecouter: {fr: 'Écouter le guide', en: 'Listen to the guide', es: 'Escuchar la guía'},
  pause: {fr: 'En pause', en: 'Paused', es: 'En pausa'},
  voixAppareil: {fr: 'voix de l’appareil', en: 'device voice', es: 'voz del teléfono'},
  commander: {fr: 'Quoi commander', en: 'What to order', es: 'Qué pedir'},
  savoir: {fr: 'Le saviez-vous ?', en: 'Did you know?', es: '¿Sabía que…?'},
  conseil: {fr: 'Conseil d’ici', en: 'Local tip', es: 'Consejo local'},
  itineraire: {fr: 'Itinéraire', en: 'Directions', es: 'Cómo llegar'},
  surCarte: {fr: 'Voir sur la carte', en: 'Show on the map', es: 'Ver en el mapa'},
  jySuis: {fr: 'J’y suis allé — tamponner', en: 'I’ve been here — stamp it', es: 'Ya estuve aquí: sellar'},
  tamponne: {fr: 'Tamponné le', en: 'Stamped on', es: 'Sellado el'},
  retirer: {fr: 'retirer', en: 'remove', es: 'quitar'},
  nouveauT: {fr: 'Tampon ajouté au passeport', en: 'Stamp added to your passport', es: 'Sello añadido al pasaporte'},
  prec: {fr: 'Précédent', en: 'Previous', es: 'Anterior'},
  suiv: {fr: 'Suivant', en: 'Next', es: 'Siguiente'},
  retour: {fr: 'Retour', en: 'Back', es: 'Volver'},
  circuitsIntro: {fr: 'Quatre promenades pour voir la ville d’un quartier à l’autre, à pied et en métro.', en: 'Four walks to see the city from one neighbourhood to the next, on foot and by metro.', es: 'Cuatro paseos para recorrer la ciudad de un barrio a otro, a pie y en metro.'},
  etapes: {fr: 'étapes', en: 'stops', es: 'paradas'},
  pratique: {fr: 'Le guide pratique', en: 'Practical guide', es: 'Guía práctica'},
  pratiqueS: {fr: 'Métro, pourboire, taxes, saisons : ce qu’il faut savoir.', en: 'Metro, tipping, taxes, seasons: what you need to know.', es: 'Metro, propinas, impuestos, estaciones: lo que hay que saber.'},
  mots: {fr: 'Les mots d’ici', en: 'Local words', es: 'Palabras locales'},
  motsS: {fr: 'Le français de Montréal, pour comprendre et vous faire comprendre.', en: 'Montreal French, to understand and be understood.', es: 'El francés de Montreal, para entender y hacerse entender.'},
  motsIntro: {fr: 'Des mots que vous entendrez partout en ville. Touchez le bouton pour entendre la phrase.', en: 'Words you will hear all over town. Tap the button to hear the sentence in Montreal French.', es: 'Palabras que oirá en toda la ciudad. Toque el botón para oír la frase en francés de Montreal.'},
  min: {fr: 'min', en: 'min', es: 'min'},
  h: {fr: 'h', en: 'h', es: 'h'},
  paliers: {fr: ['Premier tampon ! Le voyage commence.', 'Cinq lieux : vous connaissez déjà la ville mieux que bien des visiteurs.', 'Dix lieux : vous devenez un peu montréalais.', 'La moitié du passeport. Chapeau !', 'Passeport complet. Vous êtes officiellement montréalais de cœur.'],
            en: ['First stamp! The trip begins.', 'Five places: you already know the city better than most visitors.', 'Ten places: you’re becoming a bit of a Montrealer.', 'Half the passport. Well done!', 'Passport complete. You are officially a Montrealer at heart.'],
            es: ['¡Primer sello! Empieza el viaje.', 'Cinco lugares: ya conoce la ciudad mejor que muchos visitantes.', 'Diez lugares: se está volviendo un poco montrealés.', 'La mitad del pasaporte. ¡Bravo!', 'Pasaporte completo. Ya es oficialmente montrealés de corazón.']},
  vie: {fr: 'Rien ne quitte votre téléphone : la langue, les tampons et votre position y restent.', en: 'Nothing leaves your phone: your language, stamps and location stay on it.', es: 'Nada sale de su teléfono: el idioma, los sellos y su ubicación se quedan en él.'},
  parler: {fr: 'Parler', en: 'Speak', es: 'Hablar'},
  parlerTitre: {fr: 'Se débrouiller en français', en: 'Get by in French', es: 'Defenderse en francés'},
  parlerIntro: {fr: 'Douze petites scènes de la vie montréalaise. Le personnage vous parle en français d’ici ; vous choisissez quoi répondre, puis vous le dites à voix haute.',
                en: 'Twelve short scenes from Montreal life. The character speaks Montreal French to you; you pick what to answer, then say it out loud.',
                es: 'Doce escenas cortas de la vida en Montreal. El personaje le habla en francés de aquí; usted elige qué responder y luego lo dice en voz alta.'},
  aucun: {fr: 'Pas encore joué', en: 'Not played yet', es: 'Aún no jugada'},
  pratiquer: {fr: 'Pratiquer ici en français', en: 'Practise here in French', es: 'Practique aquí en francés'},
  votreBut: {fr: 'Votre but', en: 'Your goal', es: 'Su objetivo'},
  commencer: {fr: 'Commencer', en: 'Start', es: 'Empezar'},
  vous: {fr: 'Vous', en: 'You', es: 'Usted'},
  repondre: {fr: 'Que répondez-vous ?', en: 'What do you answer?', es: '¿Qué responde?'},
  reessayer: {fr: 'Essayez encore.', en: 'Try again.', es: 'Inténtelo otra vez.'},
  dites: {fr: 'Bonne réponse. Dites-la maintenant à voix haute, comme la voix l’a dite.', en: 'Right. Now say it out loud, the way you just heard it.', es: 'Correcto. Ahora dígalo en voz alta, como lo acaba de oír.'},
  continuer: {fr: 'Continuer', en: 'Continue', es: 'Continuar'},
  reecouter: {fr: 'Réécouter', en: 'Replay', es: 'Repetir'},
  lent: {fr: 'Plus lent', en: 'Slower', es: 'Más lento'},
  traduction: {fr: 'Afficher la traduction', en: 'Show translation', es: 'Mostrar la traducción'},
  bravo: {fr: ['Continuez de pratiquer', 'Bien joué !', 'Parfait !'], en: ['Keep practising', 'Well done!', 'Perfect!'], es: ['Siga practicando', '¡Bien hecho!', '¡Perfecto!']},
  aRetenir: {fr: 'Phrases à retenir', en: 'Phrases to keep', es: 'Frases para recordar'},
  bonASavoir: {fr: 'Bon à savoir', en: 'Good to know', es: 'Bueno saber'},
  rejouer: {fr: 'Rejouer la scène', en: 'Play again', es: 'Jugar de nuevo'},
  autres: {fr: 'Toutes les scènes', en: 'All scenes', es: 'Todas las escenas'},
  voirLieu: {fr: 'Voir le lieu', en: 'See the place', es: 'Ver el lugar'},
  mesConv: {fr: 'Mes conversations', en: 'My conversations', es: 'Mis conversaciones'},
  etoilesTot: {fr: 'étoiles', en: 'stars', es: 'estrellas'},
  circuitsTous: {fr: 'Tous les circuits', en: 'All walks', es: 'Todos los recorridos'},
  famBouton: {fr: 'En famille avec Filou', en: 'Family mode with Filou', es: 'En familia con Filou'},
  famSous: {fr: 'Des énigmes, des défis et des autocollants pour les 6 à 11 ans.', en: 'Riddles, challenges and stickers for kids aged 6 to 11.', es: 'Adivinanzas, retos y pegatinas para niños de 6 a 11 años.'},
  modeGrands: {fr: 'Revenir au mode adulte', en: 'Back to grown-up mode', es: 'Volver al modo adulto'},
  explorer: {fr: 'Explorer', en: 'Explore', es: 'Explorar'},
  carnetOnglet: {fr: 'Carnet', en: 'Stickers', es: 'Álbum'},
  parents: {fr: 'Parents', en: 'Parents', es: 'Padres'},
  monCarnet: {fr: 'Mon carnet d’explorateur', en: 'My explorer sticker book', es: 'Mi álbum de explorador'},
  ecouteFilou: {fr: 'Écoute Filou', en: 'Listen to Filou', es: 'Escucha a Filou'},
  enigmeT: {fr: 'Énigme !', en: 'Riddle!', es: '¡Adivinanza!'},
  ecouterQ: {fr: 'Écoute la question', en: 'Hear the question', es: 'Escucha la pregunta'},
  defiT: {fr: 'Défi', en: 'Challenge', es: 'Reto'},
  ecouterD: {fr: 'Écoute le défi', en: 'Hear the challenge', es: 'Escucha el reto'},
  tonAutoc: {fr: 'Ton autocollant', en: 'Your sticker', es: 'Tu pegatina'},
  gagneA: {fr: 'Résous l’énigme pour le gagner !', en: 'Solve the riddle to win it!', es: '¡Resuelve la adivinanza para ganarla!'},
  gagne: {fr: 'Il est dans ton carnet !', en: 'It’s in your sticker book!', es: '¡Ya está en tu álbum!'},
  ficheGrands: {fr: 'La fiche des grands', en: 'The grown-ups’ page', es: 'La página de los adultos'},
  parlerEnfants: {fr: 'Parle français comme un grand !', en: 'Speak French like a pro!', es: '¡Habla francés como un grande!'},
  parlerEnfantsS: {fr: 'Commande ta crème glacée, dis bonjour au marchand…', en: 'Order your ice cream, say hello at the market…', es: 'Pide tu helado, saluda al vendedor…'},
  toi: {fr: 'Toi', en: 'You', es: 'Tú'},
  diplomeT: {fr: 'Ton diplôme d’explorateur', en: 'Your explorer certificate', es: 'Tu diploma de explorador'},
  prenom: {fr: 'Ton prénom', en: 'Your first name', es: 'Tu nombre'},
  imprimer: {fr: 'Imprimer mon diplôme', en: 'Print my certificate', es: 'Imprimir mi diploma'},
  diplomeH: {fr: 'Diplôme d’explorateur de Montréal', en: 'Montreal Explorer Certificate', es: 'Diploma de explorador de Montreal'},
  diplomeTx: {fr: 'a trouvé les dix autocollants de Filou.', en: 'found all ten of Filou’s stickers.', es: 'encontró las diez pegatinas de Filou.'},
  prenomVie: {fr: 'Ton prénom reste dans ce téléphone.', en: 'Your name stays on this phone.', es: 'Tu nombre se queda en este teléfono.'},
  encore: {fr: n => `Encore ${n} autocollant${n > 1 ? 's' : ''} et ton diplôme est à toi !`, en: n => `${n} more sticker${n > 1 ? 's' : ''} and your certificate is yours!`, es: n => `¡${n} pegatina${n > 1 ? 's' : ''} más y el diploma es tuyo!`},
  aVerifier: {fr: 'Heures et prix changent : vérifiez avant de vous déplacer.', en: 'Hours and prices change: check before you go.', es: 'Horarios y precios cambian: verifique antes de ir.'},
};

// ---------- état (localStorage seulement) ----------
const CLE = 'montreal-poche';
let S = {lang: null, tampons: {}, filtre: 'tout', pres: false, vit: 1, scenes: {}, trad: true, famille: false, autoc: {}, prenom: ''};
try { Object.assign(S, JSON.parse(localStorage.getItem(CLE) || '{}')); } catch (e) {}
function garder() { try { localStorage.setItem(CLE, JSON.stringify(S)); } catch (e) {} }
const t = k => (T[k] && (T[k][S.lang] ?? T[k].fr)) ?? k;
const L = o => o ? (o[S.lang] ?? o.fr) : '';
const E = s => String(s ?? '').replace(/[&<>"']/g, c => ({'&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;'}[c]));
const byId = Object.fromEntries(D.lieux.map(l => [l.id, l]));
const sceneDuLieu = Object.fromEntries(D.scenes.filter(sc => sc.lieu && !sc.enfant).map(sc => [sc.lieu, sc]));
const sceneEnfantDuLieu = Object.fromEntries(D.scenes.filter(sc => sc.lieu && sc.enfant).map(sc => [sc.lieu, sc]));
const famById = Object.fromEntries(D.famille.map(e => [e.lieu, e]));
const scenesDuMode = () => D.scenes.filter(sc => !!sc.enfant === !!S.famille);
const img = id => `${MEDIA}lieux/${id}.jpg?v=${V}`;
const app = document.getElementById('app');
let position = null;

// ---------- icônes ----------
const IC = {
  decouvrir: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"/><path d="m15.5 8.5-2 5-5 2 2-5z"/></svg>',
  carte: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M9 4 3 6v14l6-2 6 2 6-2V4l-6 2z"/><path d="M9 4v14M15 6v14"/></svg>',
  circuits: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="6" cy="19" r="2"/><circle cx="18" cy="5" r="2"/><path d="M8 19h7a3.5 3.5 0 0 0 0-7H9a3.5 3.5 0 0 1 0-7h7"/></svg>',
  passeport: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="5" y="3" width="14" height="18" rx="2"/><circle cx="12" cy="10" r="3"/><path d="M9 16h6"/></svg>',
  plus: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"/><path d="M12 11v5M12 8h.01"/></svg>',
  parler: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 12a8 8 0 0 1-11.6 7.1L4 20l1-4.6A8 8 0 1 1 21 12z"/><path d="M9 10h6M9 14h4"/></svg>',
  jouer: '<svg viewBox="0 0 24 24"><path d="M8 5v14l11-7z"/></svg>',
  pause: '<svg viewBox="0 0 24 24"><path d="M7 5h4v14H7zM13 5h4v14h-4z"/></svg>',
  hp: '<svg viewBox="0 0 24 24"><path d="M4 9v6h4l5 4V5L8 9zm12.5 3a4.5 4.5 0 0 0-2.5-4v8a4.5 4.5 0 0 0 2.5-4z"/></svg>',
  fleche: '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="m15 18-6-6 6-6"/></svg>',
};

// ---------- cadre ----------
function entete(retour) {
  const lg = LANGS.map(g => `<button aria-pressed="${g === S.lang}" data-lang="${g}" lang="${LOC[g]}">${g.toUpperCase()}</button>`).join('');
  const gauche = retour
    ? `<button class="retour" data-retour="${E(retour)}">${IC.fleche}${t('retour')}</button>`
    : S.famille ? `<a class="marque" href="#"><img src="${MEDIA}filou/salut-d.webp" alt=""><span>Filou</span></a>`
    : `<a class="marque" href="#"><i class="pt"></i><span>${t('titre')}</span></a>`;
  return `<header class="barre"><div class="col">${gauche}<div class="langues" role="group" aria-label="Langue · Language · Idioma">${lg}</div></div></header>`;
}
function onglets(actif) {
  const nav = document.getElementById('onglets');
  nav.hidden = false;
  nav.querySelector('.col').innerHTML = [['', 'decouvrir'], ['#carte', 'carte'], ['#parler', 'parler'], ['#passeport', 'passeport'], ['#plus', 'plus']]
    .map(([h, k]) => `<a href="${h || '#'}" ${actif === k ? 'aria-current="page"' : ''}>${IC[k]}<span>${t(S.famille ? ({decouvrir: 'explorer', passeport: 'carnetOnglet', plus: 'parents'}[k] || k) : k)}</span></a>`).join('');
}
function toast(msg) {
  const d = document.createElement('div'); d.className = 'toast'; d.textContent = msg; d.setAttribute('role', 'status');
  document.body.appendChild(d); setTimeout(() => d.remove(), 2600);
}
function dureeTxt(m) { return m >= 60 ? `${Math.floor(m / 60)} ${t('h')}${m % 60 ? ' ' + (m % 60) : ''}` : `${m} ${t('min')}`; }
function dist(a, b) {
  const R = 6371, r = x => x * Math.PI / 180, dLa = r(b[0] - a[0]), dLo = r(b[1] - a[1]);
  const h = Math.sin(dLa / 2) ** 2 + Math.cos(r(a[0])) * Math.cos(r(b[0])) * Math.sin(dLo / 2) ** 2;
  return 2 * R * Math.asin(Math.sqrt(h));
}
function distTxt(km) { return km < 1 ? `${Math.round(km * 100) * 10} m` : `${km.toFixed(km < 10 ? 1 : 0).replace('.', S.lang === 'en' ? '.' : ',')} km`; }

// ---------- tampon (SVG) ----------
function tampon(l, date, taille = 120) {
  const nom = L(l.nom).toUpperCase();
  const plein = !!date, c = plein ? '#B3262E' : '#9AA0A8';
  const rot = plein ? ((l.id.length * 37) % 17) - 8 : 0;
  const court = nom.length > 18 ? nom.slice(0, 17) + '…' : nom;
  const d = date ? new Date(date).toLocaleDateString(LOC[S.lang], {day: 'numeric', month: 'short', year: 'numeric'}) : '';
  const cat = L(T.cat1[l.cat]).toUpperCase();
  return `<svg viewBox="0 0 120 120" width="${taille}" role="img" aria-label="${E(L(l.nom))}${plein ? ' — ' + E(d) : ''}">
    <g transform="rotate(${rot} 60 60)" fill="none" stroke="${c}" ${plein ? '' : 'stroke-dasharray="4 4"'}>
      <circle cx="60" cy="60" r="54" stroke-width="3"/><circle cx="60" cy="60" r="46" stroke-width="1.2"/>
      <defs><path id="arc-${l.id}" d="M 22 60 A 38 38 0 0 1 98 60"/></defs>
      <text font-family="Nunito,system-ui" font-weight="900" font-size="${court.length > 13 ? 8.5 : 10.5}" letter-spacing="1.2" fill="${c}" stroke="none"><textPath href="#arc-${l.id}" startOffset="50%" text-anchor="middle">${E(court)}</textPath></text>
      <text x="60" y="68" text-anchor="middle" font-family="Nunito,system-ui" font-weight="900" font-size="15" fill="${c}" stroke="none">MTL</text>
      <text x="60" y="84" text-anchor="middle" font-family="Nunito,system-ui" font-weight="800" font-size="7.5" fill="${c}" stroke="none">${E(plein ? d : cat)}</text>
    </g></svg>`;
}
function palier() {
  const n = Object.keys(S.tampons).length, tot = D.lieux.length, p = T.paliers[S.lang];
  if (n >= tot) return p[4];
  if (n >= Math.ceil(tot / 2)) return p[3];
  if (n >= 10) return p[2];
  if (n >= 5) return p[1];
  if (n >= 1) return p[0];
  return '';
}
function anneau(n, tot) {
  const r = 20, c = 2 * Math.PI * r, f = tot ? n / tot : 0;
  return `<svg class="rond" width="52" height="52" viewBox="0 0 52 52"><circle cx="26" cy="26" r="${r}" fill="none" stroke="#EFE7D6" stroke-width="6"/>
    <circle cx="26" cy="26" r="${r}" fill="none" stroke="#B3262E" stroke-width="6" stroke-linecap="round" stroke-dasharray="${c * f} ${c}" transform="rotate(-90 26 26)"/>
    <text x="26" y="31" text-anchor="middle" font-family="Nunito,system-ui" font-weight="900" font-size="14" fill="#1E2733">${n}</text></svg>`;
}

// ---------- vues ----------
function vueBienvenue() {
  document.getElementById('onglets').hidden = true;
  app.innerHTML = `<div class="bienvenue"><img src="${img('accueil')}" alt="" width="1200" height="800">
    <h1>Montréal en poche</h1>
    <p lang="en">Montreal in Your Pocket · <span lang="es">Montreal en el bolsillo</span></p>
    <div class="choix">
      <button data-choisir="fr" lang="fr-CA">Français</button>
      <button data-choisir="en" lang="en-CA">English</button>
      <button data-choisir="es" lang="es">Español</button>
    </div></div>`;
}

function carteLieu(l) {
  const d = position ? `<span class="dist">${distTxt(dist(position, l.geo))}</span>` : '';
  const vu = S.tampons[l.id] ? `<span class="vu">${tampon(l, S.tampons[l.id], 46)}</span>` : '';
  return `<a class="carte-lieu" href="#lieu/${l.id}"><img src="${img(l.id)}" alt="" loading="lazy" width="1200" height="800">${d}${vu}
    <div class="t"><span class="etq ${l.cat}">${E(L(T.cat1[l.cat]))}</span><h3>${E(L(l.nom))}</h3><p>${E(L(l.bref))}</p>
    <div class="meta">${E(l.quartier)}${l.metro ? ' · ' + t('metro') + ' ' + E(l.metro) : ''}</div></div></a>`;
}

function vueAccueil() {
  onglets('decouvrir');
  const n = Object.keys(S.tampons).length;
  let liste = D.lieux.filter(l => S.filtre === 'tout' || l.cat === S.filtre);
  if (S.pres && position) liste = [...liste].sort((a, b) => dist(position, a.geo) - dist(position, b.geo));
  const puces = ['tout', ...['voir', 'quartier', 'manger', 'boire']].map(k =>
    `<button aria-pressed="${S.filtre === k}" data-filtre="${k}">${t(k)}</button>`).join('')
    + `<button class="pres" aria-pressed="${!!(S.pres && position)}" data-pres="1">${t('pres')}</button>`;
  app.innerHTML = entete() + `<main class="col">
    <section class="hero"><img src="${img('accueil')}" alt="" width="1200" height="800"><div class="txt"><h1>${t('titre')}</h1><p>${t('accroche')}</p></div></section>
    ${D.famille.length ? `<button class="bascule-f" data-famille="1" style="width:100%;text-align:left"><img src="${MEDIA}filou/salut-d.webp" alt=""><span><b>${t('famBouton')}</b><small>${t('famSous')}</small></span></button>` : ''}
    <a class="progres" href="#passeport">${anneau(n, D.lieux.length)}<span><b>${t('monPass')}</b><small>${n} / ${D.lieux.length} ${t('tampons')}${palier() ? ' — ' + E(palier()) : ''}</small></span></a>
    <h2 class="sec">${t('circuits')}</h2>
    <div class="circuits-rangee">${D.circuits.map(carteCircuit).join('')}</div>
    <h2 class="sec">${D.lieux.length} ${t('lieux')}</h2>
    <div class="puces" role="group">${puces}</div>
    <div class="liste">${liste.map(carteLieu).join('')}</div>
    <p class="pied">${t('aVerifier')}<br>${t('vie')}</p></main>`;
}

function vueLieu(id) {
  const l = byId[id]; if (!l) { location.hash = ''; return; }
  onglets(null);
  const meme = D.lieux;
  const i = meme.indexOf(l), prec = meme[(i - 1 + meme.length) % meme.length], suiv = meme[(i + 1) % meme.length];
  const aSon = l.son.includes(S.lang);
  const paras = L(l.texte).split(/\n\n+/).map(p => `<p>${E(p)}</p>`).join('');
  const date = S.tampons[l.id];
  const vit = [0.85, 1, 1.15].map(v => `<button aria-pressed="${S.vit === v}" data-vit="${v}">${String(v).replace('.', S.lang === 'en' ? '.' : ',')}×</button>`).join('');
  app.innerHTML = entete('#') + `<main class="col lieu">
    <div class="lieu-img"><img src="${img(l.id)}" alt="" width="1200" height="800"></div>
    <span class="etq ${l.cat}" style="margin-top:14px">${E(L(T.cat1[l.cat]))}</span>
    <h1>${E(L(l.nom))}</h1><p class="bref">${E(L(l.bref))}</p>
    <dl class="fiche"><dt>${t('quartierL')}</dt><dd>${E(l.quartier)}</dd>
      ${l.metro ? `<dt>${t('metro')}</dt><dd>${E(l.metro)}</dd>` : ''}
      ${l.adresse ? `<dt>${t('adresse')}</dt><dd>${E(l.adresse)}</dd>` : ''}
      <dt>${t('duree')}</dt><dd>${dureeTxt(l.duree)}</dd></dl>
    <button class="ecoute" id="ecoute" data-id="${l.id}"><span class="ic">${IC.jouer}</span>
      <span style="flex:1;min-width:0"><b>${t('ecouter')}</b><small id="ecoute-etat">${aSon ? LANGUE_NOM[S.lang] : t('voixAppareil')}</small>
      <span class="barre-son"><i id="ecoute-barre"></i></span></span></button>
    <div class="vitesse" role="group">${vit}</div>
    ${sceneDuLieu[l.id] ? inviteScene(sceneDuLieu[l.id]) : ''}
    <div class="texte">${paras}</div>
    ${l.commander ? `<div class="encart commander"><h3>${t('commander')}</h3><p>${E(L(l.commander))}</p></div>` : ''}
    <div class="encart savoir"><h3>${t('savoir')}</h3><p>${E(L(l.anecdote))}</p></div>
    <div class="encart conseil"><h3>${t('conseil')}</h3><p>${E(L(l.conseil))}</p></div>
    <div class="actions">
      <button class="bouton ${date ? 'fait' : 'plein'}" data-tampon="${l.id}">${date ? `${t('tamponne')} ${new Date(date).toLocaleDateString(LOC[S.lang], {day: 'numeric', month: 'long'})} · ${t('retirer')}` : t('jySuis')}</button>
      <a class="bouton" href="https://www.google.com/maps/dir/?api=1&destination=${l.geo[0]},${l.geo[1]}" target="_blank" rel="noopener">${t('itineraire')}</a>
      <a class="bouton" href="#carte/${l.id}">${t('surCarte')}</a>
    </div>
    <div class="voisins"><a href="#lieu/${prec.id}"><small>← ${t('prec')}</small><b>${E(L(prec.nom))}</b></a><a class="suiv" href="#lieu/${suiv.id}"><small>${t('suiv')} →</small><b>${E(L(suiv.nom))}</b></a></div>
    <p class="pied">${t('aVerifier')}</p></main>`;
  window.scrollTo(0, 0);
}
const LANGUE_NOM = {fr: 'Français', en: 'English', es: 'Español'};

// ---------- audioguide ----------
const lecteur = document.getElementById('lecteur');
let enCours = null;
function arreterSon() {
  lecteur.pause(); if (window.speechSynthesis) speechSynthesis.cancel();
  enCours = null; majEcoute();
}
function majEcoute() {
  const b = document.getElementById('ecoute'); if (!b) return;
  const joue = enCours && enCours.id === b.dataset.id && enCours.joue;
  b.querySelector('.ic').innerHTML = joue ? IC.pause : IC.jouer;
}
function ecouter(id) {
  const l = byId[id];
  if (enCours && enCours.id === id) {            // bascule lecture / pause
    if (enCours.tts) { if (speechSynthesis.paused) { speechSynthesis.resume(); enCours.joue = true; } else { speechSynthesis.pause(); enCours.joue = false; } }
    else if (lecteur.paused) { lecteur.play(); enCours.joue = true; } else { lecteur.pause(); enCours.joue = false; }
    majEcoute(); return;
  }
  arreterSon();
  if (l.son.includes(S.lang)) {
    enCours = {id, joue: true, tts: false};
    lecteur.src = `${MEDIA}audio/${S.lang}/${id}.mp3?v=${V}`;
    lecteur.playbackRate = S.vit;
    lecteur.play().catch(() => { enCours = null; majEcoute(); });
  } else if (window.speechSynthesis) {
    const u = new SpeechSynthesisUtterance(L(l.texte).replace(/\n+/g, ' '));
    u.lang = LOC[S.lang]; u.rate = S.vit;
    u.onend = () => { enCours = null; majEcoute(); };
    enCours = {id, joue: true, tts: true};
    speechSynthesis.speak(u);
  }
  majEcoute();
}
lecteur.addEventListener('timeupdate', () => {
  const i = document.getElementById('ecoute-barre'), e = document.getElementById('ecoute-etat');
  if (!i || !lecteur.duration) return;
  i.style.width = (100 * lecteur.currentTime / lecteur.duration) + '%';
  const r = Math.max(0, Math.round(lecteur.duration - lecteur.currentTime));
  e.textContent = `${LANGUE_NOM[S.lang]} · ${Math.floor(r / 60)}:${String(r % 60).padStart(2, '0')}`;
});
lecteur.addEventListener('ended', () => { enCours = null; majEcoute(); });
function direMot(i) {
  const m = D.mots[i];
  arreterSon();
  if (m.son) { lecteur.src = `${MEDIA}audio/mots/${String(i).padStart(2, '0')}.mp3?v=${V}`; lecteur.playbackRate = 1; lecteur.play().catch(() => {}); }
  else if (window.speechSynthesis) { const u = new SpeechSynthesisUtterance(m.exemple); u.lang = 'fr-CA'; speechSynthesis.speak(u); }
}

// ---------- cartes (Leaflet) ----------
let carteObj = null;
function epingle(cat, num) {
  return L_.divIcon({className: '', iconSize: [26, 26], iconAnchor: [13, 26], popupAnchor: [0, -24],
    html: `<div class="epingle ${num ? 'num' : ''}" style="background:${COUL[cat]}">${num ? `<span>${num}</span>` : ''}</div>`});
}
const L_ = window.L;
function fond(m) {
  L_.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {maxZoom: 19,
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a>'}).addTo(m);
}
function pop(l) {
  return `<div class="pop"><img src="${img(l.id)}" alt=""><span class="etq ${l.cat}">${E(L(T.cat1[l.cat]))}</span><b>${E(L(l.nom))}</b><a href="#lieu/${l.id}">${E(L(l.bref))} →</a></div>`;
}
function vueCarte(cible) {
  onglets('carte');
  app.innerHTML = entete() + `<div style="position:relative"><div id="carte"></div>
    <div class="legende">${['voir', 'quartier', 'manger', 'boire'].map(k => `<span><i style="background:${COUL[k]}"></i>${t(k)}</span>`).join('')}</div></div>`;
  if (!L_) { document.getElementById('carte').innerHTML = '<p class="col">…</p>'; return; }
  carteObj = L_.map('carte', {zoomControl: true}).setView([45.515, -73.585], 12);
  fond(carteObj);
  const marq = {};
  const visibles = S.famille ? D.lieux.filter(l => famById[l.id]) : D.lieux;
  visibles.forEach(l => { marq[l.id] = L_.marker(l.geo, {icon: epingle(l.cat)}).addTo(carteObj).bindPopup(pop(l)); });
  if (cible && marq[cible]) { carteObj.setView(byId[cible].geo, 15); marq[cible].openPopup(); }
  else carteObj.fitBounds(visibles.map(l => l.geo), {padding: [30, 30]});
  if (position) L_.circleMarker(position, {radius: 8, color: '#fff', weight: 3, fillColor: '#1A73E8', fillOpacity: 1}).addTo(carteObj);
}

function carteCircuit(c) {
  return `<a class="circuit-carte" href="#circuit/${c.id}">
      <div class="imgs">${c.etapes.slice(0, 3).map(e => `<img src="${img(e)}" alt="" loading="lazy">`).join('')}</div>
      <div class="t"><h3>${E(L(c.nom))}</h3><div class="meta">${c.etapes.length} ${t('etapes')} · ${E(L(c.duree))}</div><p>${E(L(c.intro))}</p></div></a>`;
}
function vueCircuits() {
  onglets('decouvrir');
  app.innerHTML = entete() + `<main class="col"><h2 class="sec">${t('circuits')}</h2><p class="intro">${t('circuitsIntro')}</p>
    <div class="liste">${D.circuits.map(carteCircuit).join('')}</div></main>`;
}
function vueCircuit(id) {
  const c = D.circuits.find(x => x.id === id); if (!c) { location.hash = '#circuits'; return; }
  onglets('decouvrir');
  const lia = L(c.liaisons);
  let lis = '';
  c.etapes.forEach((e, i) => {
    const l = byId[e];
    lis += `<li class="etape"><a href="#lieu/${e}"><span class="n">${i + 1}</span><img src="${img(e)}" alt="" loading="lazy">
      <span><b>${E(L(l.nom))}</b><small>${E(L(T.cat1[l.cat]))} · ${dureeTxt(l.duree)}${S.tampons[e] ? ' · ✓' : ''}</small></span></a></li>`;
    if (i < lia.length) lis += `<li class="liaison">${E(lia[i])}</li>`;
  });
  app.innerHTML = entete('#circuits') + `<main class="col"><h2 class="sec" style="margin-top:16px">${E(L(c.nom))}</h2>
    <div class="meta">${c.etapes.length} ${t('etapes')} · ${E(L(c.duree))}</div><p>${E(L(c.intro))}</p>
    <div class="mini-carte" id="mini"></div><ol class="parcours">${lis}</ol></main>`;
  window.scrollTo(0, 0);
  if (!L_) return;
  const m = L_.map('mini', {scrollWheelZoom: false}); fond(m);
  const pts = c.etapes.map(e => byId[e].geo);
  L_.polyline(pts, {color: '#B3262E', weight: 3, dashArray: '6 6'}).addTo(m);
  c.etapes.forEach((e, i) => L_.marker(byId[e].geo, {icon: epingle(byId[e].cat, i + 1)}).addTo(m).bindPopup(pop(byId[e])));
  m.fitBounds(pts, {padding: [28, 28]});
}

function vuePasseport() {
  onglets('passeport');
  const n = Object.keys(S.tampons).length, p = palier();
  app.innerHTML = entete() + `<main class="col"><section class="passeport">
    <h2>${t('monPass')}</h2><p class="sous">${n} / ${D.lieux.length} ${t('tampons')}</p>
    ${p ? `<p class="palier">${E(p)}</p>` : `<p class="sous">${t('passInvite')}</p>`}
    <div class="grille">${D.lieux.map(l => `<a class="tampon ${S.tampons[l.id] ? '' : 'vide'}" href="#lieu/${l.id}">${tampon(l, S.tampons[l.id])}</a>`).join('')}</div>
    </section>
    <h2 class="sec">${t('mesConv')} · ${scenesDuMode().reduce((a, sc) => a + ((S.scenes[sc.id] || {}).etoiles || 0), 0)} / ${scenesDuMode().length * 3} ${t('etoilesTot')}</h2>
    <div class="liste">${scenesDuMode().map(carteScene).join('')}</div><p class="pied">${t('vie')}</p></main>`;
}

function vuePlus() {
  onglets('plus');
  app.innerHTML = entete() + `<main class="col"><div class="plus-liens" style="margin-top:18px">
    <a href="#pratique"><span>${t('pratique')}<small>${t('pratiqueS')}</small></span></a>
    <a href="#mots"><span>${t('mots')}<small>${t('motsS')}</small></span></a></div>
    <h2 class="sec">${t('pratique')}</h2>
    ${D.pratique.map(f => `<details class="fichep"><summary>${E(L(f.titre))}</summary>${L(f.texte).split(/\n\n+/).map(p => `<p>${E(p)}</p>`).join('')}</details>`).join('')}
    <p class="pied">${t('aVerifier')}<br>${t('vie')}</p></main>`;
}
function vuePratique() { vuePlus(); const h = document.querySelector('h2.sec'); if (h) h.scrollIntoView(); }
function vueMots() {
  onglets('plus');
  app.innerHTML = entete('#plus') + `<main class="col"><h2 class="sec" style="margin-top:16px">${t('mots')}</h2><p class="intro">${t('motsIntro')}</p>
    ${D.mots.map((m, i) => `<div class="mot"><b lang="fr-CA">${E(m.fr)}</b><button data-mot="${i}" aria-label="${E(m.exemple)}">${IC.hp}</button>
      <p class="sens">${E(L(m.sens))}</p><p class="ex" lang="fr-CA">« ${E(m.exemple)} »</p></div>`).join('')}</main>`;
  window.scrollTo(0, 0);
}

// ---------- Parler : les scènes ----------
// Le personnage parle français ; l'apprenant choisit sa réplique parmi trois
// (la bonne est toujours la première du contenu : l'ordre affiché est mêlé,
// mais de façon stable, pour qu'une reprise ne change pas la place des choix).
const sonScene = (id, n) => `${MEDIA}audio/scenes/${id}/${n}.mp3?v=${V}`;
function etoiles(n, cls = 'etoiles') {
  return `<span class="${cls}" aria-label="${n} / 3">${'★'.repeat(n)}<span class="v">${'★'.repeat(3 - n)}</span></span>`;
}
function carteScene(sc) {
  const r = S.scenes[sc.id];
  return `<a class="scene-carte" href="#scene/${sc.id}"><img src="${img(sc.img)}" alt="" loading="lazy">
    <span><b>${E(L(sc.titre))}</b><small>${E(L(sc.but))}</small>
    ${r ? etoiles(r.etoiles) : `<small>${t('aucun')}</small>`}</span></a>`;
}
function inviteScene(sc) {
  const r = S.scenes[sc.id];
  return `<a class="invite" href="#scene/${sc.id}"><span><b>${t('pratiquer')}</b><small>${E(L(sc.titre))}${r ? ' · ' : ''}</small>${r ? etoiles(r.etoiles) : ''}</span><span class="fl">→</span></a>`;
}
function vueParler() {
  onglets('parler');
  app.innerHTML = entete() + `<main class="col"><h2 class="sec" style="margin-top:18px">${t(S.famille ? 'parlerEnfants' : 'parlerTitre')}</h2>
    <p class="intro">${t(S.famille ? 'parlerEnfantsS' : 'parlerIntro')}</p>
    <div class="liste">${scenesDuMode().map(carteScene).join('')}</div></main>`;
}
function melange(n, graine) {
  const a = [...Array(n).keys()]; let x = graine;
  for (let i = n - 1; i > 0; i--) { x = (x * 9301 + 49297) % 233280; const j = Math.floor(x / 233280 * (i + 1)); [a[i], a[j]] = [a[j], a[i]]; }
  return a;
}
function texteScene(sc, n) {
  const m = n.match(/^([tp])(\d+)(c?)$/), k = +m[2];
  return m[1] === 'p' ? sc.phrases[k][0] : m[3] ? sc.tours[k].choix[0][0] : sc.tours[k].dit;
}
function direScene(sc, n, lent) {
  if (sc.son) return jouerSon(sonScene(sc.id, n), lent);
  arreterSon();
  if (!window.speechSynthesis) return;
  const u = new SpeechSynthesisUtterance(texteScene(sc, n)); u.lang = 'fr-CA'; u.rate = lent ? 0.8 : S.vit; speechSynthesis.speak(u);
}
function jouerSon(url, lent) {
  arreterSon();
  lecteur.src = url; lecteur.playbackRate = lent ? 0.8 : S.vit;
  lecteur.play().catch(() => {});
}
let SC = null;   // la scène en cours : {id, k, erreurs, log, faux, attente}
function avancer() {
  // Pose les répliques du personnage jusqu'au prochain choix, ou jusqu'à la fin.
  const sc = D.scenes.find(x => x.id === SC.id);
  while (SC.k < sc.tours.length && 'dit' in sc.tours[SC.k]) {
    SC.log.push({qui: 'perso', k: SC.k}); SC.k++;
  }
  SC.attente = SC.k < sc.tours.length ? 'choix' : 'fin';
  const dernier = SC.log[SC.log.length - 1];
  if (dernier && dernier.qui === 'perso') direScene(sc, `t${dernier.k}`);
  if (SC.attente === 'fin') {
    const n = SC.erreurs === 0 ? 3 : SC.erreurs <= 2 ? 2 : 1;
    SC.etoiles = n;
    const avant = S.scenes[sc.id];
    if (!avant || avant.etoiles < n) S.scenes[sc.id] = {etoiles: n, date: new Date().toISOString()};
    garder();
  }
}
function bulle(sc, e) {
  const tr = S.trad && S.lang !== 'fr';
  if (e.qui === 'perso') {
    const tour = sc.tours[e.k];
    return `<div class="bulle perso"><span class="qui">${E(sc.perso.nom)}</span><span class="fr" lang="fr-CA">${E(tour.dit)}</span>
      ${tr ? `<span class="tr">${E(tour.sens[S.lang])}</span>` : ''}
      <span class="rej"><button data-son="t${e.k}">${t('reecouter')}</button><button data-son="t${e.k}" data-lent="1">${t('lent')}</button></span></div>`;
  }
  const c = sc.tours[e.k].choix[0];
  return `<div class="bulle moi"><span class="qui">${t(sc.enfant ? 'toi' : 'vous')}</span><span class="fr" lang="fr-CA">${E(c[0])}</span>
    ${tr ? `<span class="tr">${E(c[1][S.lang])}</span>` : ''}
    <span class="rej"><button data-son="t${e.k}c">${t('reecouter')}</button><button data-son="t${e.k}c" data-lent="1">${t('lent')}</button></span></div>`;
}
function vueScene(id) {
  const sc = D.scenes.find(x => x.id === id); if (!sc) { location.hash = '#parler'; return; }
  onglets('parler');
  if (!SC || SC.id !== id) SC = {id, k: 0, erreurs: 0, log: [], faux: [], attente: 'debut'};
  const tr = S.trad && S.lang !== 'fr';
  let bas = '';
  if (SC.attente === 'debut') {
    bas = `<button class="bouton plein" data-scene="go" style="width:100%;margin:8px 0 24px">${t('commencer')}</button>`;
  } else if (SC.attente === 'choix') {
    const tour = sc.tours[SC.k];
    const ordre = melange(tour.choix.length, SC.k * 7 + sc.id.length);
    const retro = SC.faux.length ? `<div class="retro" role="status">${E(L(tour.choix[SC.faux[SC.faux.length - 1]][2]))} ${t('reessayer')}</div>` : '';
    bas = retro + `<div class="choix-scene"><p class="consigne">${t('repondre')}</p>${ordre.map(i => {
      const c = tour.choix[i];
      return `<button data-choix="${i}" class="${SC.faux.includes(i) ? 'faux' : ''}" ${SC.faux.includes(i) ? 'disabled' : ''}><b lang="fr-CA">${E(c[0])}</b>${tr ? `<small>${E(c[1][S.lang])}</small>` : ''}</button>`;
    }).join('')}</div>`;
  } else if (SC.attente === 'repete') {
    bas = `<div class="repete"><p>${t('dites')}</p><button class="bouton plein" data-scene="suite" style="width:100%">${t('continuer')}</button></div>`;
  } else {
    const r = SC.etoiles;
    bas = `<div class="fin-scene">${etoiles(r, 'grandes')}<h2>${E(T.bravo[S.lang][r - 1])}</h2>
      <h3 style="margin:18px 0 0;text-align:left">${t('aRetenir')}</h3>
      <ul class="phrases">${sc.phrases.map((ph, i) => `<li><button data-son="p${i}" aria-label="${E(ph[0])}">${IC.hp}</button>
        <span><b lang="fr-CA">${E(ph[0])}</b>${S.lang !== 'fr' ? `<small>${E(ph[1][S.lang])}</small>` : ''}</span></li>`).join('')}</ul>
      <div class="encart savoir" style="text-align:left"><h3>${t('bonASavoir')}</h3><p>${E(L(sc.note))}</p></div>
      <div class="actions"><button class="bouton plein" data-scene="rejouer">${t('rejouer')}</button>
      ${sc.lieu ? `<a class="bouton" href="#lieu/${sc.lieu}">${t('voirLieu')}</a>` : ''}
      <a class="bouton" href="#parler">${t('autres')}</a></div></div>`;
  }
  app.innerHTML = entete('#parler') + `<main class="col">
    <div class="lieu-img"><img src="${img(sc.img)}" alt="" width="1200" height="800"></div>
    <h2 class="sec" style="margin-top:14px">${E(L(sc.titre))}</h2>
    <div class="but"><small>${t('votreBut')}</small>${E(L(sc.but))}</div>
    ${S.lang !== 'fr' ? `<label class="bascule-tr"><input type="checkbox" id="trad" ${S.trad ? 'checked' : ''}>${t('traduction')}</label>` : ''}
    <div class="vitesse" role="group">${[0.85, 1, 1.15].map(v => `<button aria-pressed="${S.vit === v}" data-vit="${v}">${String(v).replace('.', S.lang === 'en' ? '.' : ',')}×</button>`).join('')}</div>
    <div class="fil-scene" aria-live="polite">${SC.log.map(e => bulle(sc, e)).join('')}</div>
    ${bas}</main>`;
  if (SC.attente !== 'debut') {
    const f = app.querySelector('.fil-scene'); const der = f.lastElementChild;
    (SC.attente === 'fin' ? app.querySelector('.fin-scene') : der || f).scrollIntoView({block: 'start', behavior: 'smooth'});
  }
}
function actionScene(b) {
  const sc = D.scenes.find(x => x.id === SC.id);
  if (b.dataset.scene === 'go') { avancer(); }
  else if (b.dataset.scene === 'suite') { avancer(); }
  else if (b.dataset.scene === 'rejouer') { SC = {id: sc.id, k: 0, erreurs: 0, log: [], faux: [], attente: 'debut'}; avancer(); }
  else if (b.dataset.choix !== undefined) {
    const i = +b.dataset.choix;
    if (i === 0) {
      SC.log.push({qui: 'moi', k: SC.k}); direScene(sc, `t${SC.k}c`);
      SC.k++; SC.faux = []; SC.attente = 'repete';
    } else { SC.faux.push(i); SC.erreurs++; }
  }
  vueScene(sc.id);
}

// ---------- mode famille : Filou ----------
// Un habit (body.famille, l'habit « Bonbon ») et des vues à part ; les
// données restent celles du guide. Rien ne quitte le téléphone : les
// autocollants et le prénom du diplôme vivent dans le localStorage.
const sonFam = (lieu, x) => `${MEDIA}audio/famille/${S.lang}/${lieu}-${x}.mp3?v=${V}`;
const sonFamG = k => `${MEDIA}audio/famille/${S.lang}/${k}.mp3?v=${V}`;
const fil = pose => `${MEDIA}filou/${pose}-d.webp`;
function voixTel(texte, loc) {
  if (!window.speechSynthesis || !texte) return;
  const u = new SpeechSynthesisUtterance(texte); u.lang = loc; speechSynthesis.speak(u);
}
function direFam(url, texte, existe) {
  // Le son de Filou quand il a été produit, sinon la voix du téléphone.
  arreterSon();
  if (existe) { lecteur.src = url; lecteur.playbackRate = 1; lecteur.play().catch(() => voixTel(texte, LOC[S.lang])); }
  else voixTel(texte, LOC[S.lang]);
}
const aSonFam = () => { const e = famById[FE && FE.id]; return !!e && e.son.includes(S.lang); };
const aSonG = k => D.filouSons.includes(`${S.lang}/${k}`);
function autoc(e, date, nouveau) {
  return date ? `<span class="autoc${nouveau ? ' nouveau' : ''}"><img src="${fil(e.pose)}" alt=""><em>${E(L(e.autocollant))}</em></span>`
              : `<span class="autoc vide"><span>?</span></span>`;
}
function famAccueil() {
  onglets('decouvrir');
  const n = D.famille.filter(e => S.autoc[e.lieu]).length, tot = D.famille.length;
  app.innerHTML = entete() + `<main class="col">
    <section class="f-hero"><img src="${fil('salut')}" alt="">
      <div class="f-bulle cadre-b">${E(L(D.filou.salut))}<br><button class="btn-son" data-fsong="salut">${IC.jouer}${t('ecouteFilou')}</button></div></section>
    <a class="f-prog cadre-b" href="#passeport"><span>${t('carnetOnglet')}</span><span class="jauge"><i style="width:${100 * n / tot}%"></i></span><b>${n} / ${tot}</b></a>
    <h2 class="f-titre">${t('explorer')}</h2>
    <div class="f-lieux">${D.famille.map(e => { const l = byId[e.lieu]; return `<a class="f-lieu cadre-b" href="#lieu/${e.lieu}"><img src="${img(e.lieu)}" alt="" loading="lazy">
      <span><b>${E(L(l.nom))}</b><small>${E(L(e.autocollant))}</small></span>${S.autoc[e.lieu] ? `<img class="gagne" src="${fil(e.pose)}" alt="">` : ''}</a>`; }).join('')}</div>
    <h2 class="f-titre">${t('parlerEnfants')}</h2>
    <div class="liste">${scenesDuMode().map(carteScene).join('')}</div>
    <button class="lien-grands" data-famille="0" style="border:0;background:none;width:100%;font:inherit;text-decoration:underline">${t('modeGrands')}</button></main>`;
}
let FE = null;   // la fiche enfant en cours : {id, faux: [], nouveau}
function famLieu(id) {
  const e = famById[id], l = byId[id];
  onglets(null);
  if (!FE || FE.id !== id) FE = {id, faux: [], nouveau: false};
  const g = e.enigme, fait = !!S.autoc[id];
  const reps = g.choix.map((c, i) => {
    const cls = fait && i === g.bonne ? 'ok' : FE.faux.includes(i) ? 'non' : '';
    return `<button data-frep="${i}" class="${cls}" ${fait || FE.faux.includes(i) ? 'disabled' : ''}>${E(L(c))}</button>`;
  }).join('');
  const sc = sceneEnfantDuLieu[id];
  app.innerHTML = entete('#') + `<main class="col">
    <div class="lieu-img"><img src="${img(id)}" alt="" width="1200" height="800"></div>
    <h1 class="f-titre" style="font-size:30px;margin:16px 0 4px">${E(L(l.nom))}</h1>
    <div class="f-raconte"><img src="${fil('raconte')}" alt=""><div class="f-bulle cadre-b">${E(L(e.raconte))}<br>
      <button class="btn-son" data-fson="r">${IC.jouer}${t('ecouteFilou')}</button></div></div>
    <section class="f-enigme"><img src="${fil(fait ? 'bravo' : 'loupe')}" alt="">
      <h3>${t('enigmeT')}</h3><p class="q">${E(L(g.q))}</p>
      <button class="btn-son turq" data-fson="e">${IC.jouer}${t('ecouterQ')}</button>
      <div class="rep-f">${reps}</div>
      ${fait ? `<div class="f-bravo"><img src="${fil('bravo')}" alt=""><span>${E(L(g.bravo))}</span></div>` : ''}</section>
    <section class="f-defi"><h3>${t('defiT')}</h3><p>${E(L(e.defi))}</p><button class="btn-son" data-fson="d">${IC.jouer}${t('ecouterD')}</button></section>
    <section class="f-gagne cadre-b">${autoc(e, S.autoc[id], FE.nouveau)}<h3>${fait ? t('gagne') : t('gagneA')}</h3></section>
    ${sc ? `<a class="invite" href="#scene/${sc.id}"><span><b>${t('parlerEnfants')}</b><small>${E(L(sc.titre))}</small></span><span class="fl">→</span></a>` : ''}
    <a class="lien-grands" href="#grand/${id}">${t('ficheGrands')} →</a></main>`;
  if (!FE.nouveau) window.scrollTo(0, 0);
}
function famRepondre(i) {
  const e = famById[FE.id];
  if (i === e.enigme.bonne) {
    S.autoc[e.lieu] = new Date().toISOString(); garder(); FE.nouveau = true;
    direFam(sonFam(e.lieu, 'b'), L(e.enigme.bravo), aSonFam());
    const y = window.scrollY; famLieu(e.lieu); window.scrollTo(0, y);
    if (D.famille.every(x => S.autoc[x.lieu])) setTimeout(() => toast(L(D.filou.diplome)), 1200);
  } else {
    FE.faux.push(i); direFam(sonFamG('essaie'), L(D.filou.essaie), aSonG('essaie'));
    const y = window.scrollY; famLieu(e.lieu); window.scrollTo(0, y);
  }
}
function famCarnet() {
  onglets('passeport');
  const n = D.famille.filter(e => S.autoc[e.lieu]).length, tot = D.famille.length;
  const dip = n >= tot
    ? `<section class="f-diplome cadre-b"><img src="${fil('bravo')}" alt="" style="width:120px"><h2 class="f-titre" style="margin:6px 0">${t('diplomeT')}</h2>
        <input id="prenom" value="${E(S.prenom)}" placeholder="${t('prenom')}" autocomplete="off" maxlength="30"><br>
        <button class="btn-son" data-imprimer="1">${t('imprimer')}</button><p style="color:var(--doux);font-size:14px">${t('prenomVie')}</p></section>`
    : `<section class="f-diplome cadre-b"><img src="${fil('surprise')}" alt="" style="width:110px"><h3 class="f-titre" style="font-size:21px;margin:6px 0 0">${E(T.encore[S.lang](tot - n))}</h3></section>`;
  app.innerHTML = entete() + `<main class="col"><h2 class="f-titre">${t('monCarnet')}</h2>
    <a class="f-prog cadre-b" href="#"><span>${n} / ${tot}</span><span class="jauge"><i style="width:${100 * n / tot}%"></i></span></a>
    <div class="carnet-f">${D.famille.map(e => `<a href="#lieu/${e.lieu}">${autoc(e, S.autoc[e.lieu])}</a>`).join('')}</div>${dip}</main>`;
}
function imprimerDiplome() {
  const d = document.getElementById('diplome');
  d.innerHTML = `<div class="cadre"><img class="f" src="${fil('bravo')}" alt=""><h1>${t('diplomeH')}</h1>
    <div class="nom">${E(S.prenom || '…')}</div><p style="font-size:22px">${t('diplomeTx')}</p>
    <div class="st">${D.famille.map(e => `<img src="${fil(e.pose)}" alt="">`).join('')}</div>
    <p>${new Date().toLocaleDateString(LOC[S.lang], {day: 'numeric', month: 'long', year: 'numeric'})} · Filou</p></div>`;
  document.body.classList.add('imprime');
  const fin = () => { document.body.classList.remove('imprime'); window.removeEventListener('afterprint', fin); };
  window.addEventListener('afterprint', fin);
  setTimeout(() => window.print(), 300);
}

// ---------- routeur ----------
function route() {
  if (carteObj) { carteObj.remove(); carteObj = null; }
  if (!S.lang) return vueBienvenue();
  document.documentElement.lang = LOC[S.lang];
  document.title = t('titre');
  const [v, a] = location.hash.slice(1).split('/');
  if (v !== 'lieu' && v !== 'scene' && v !== 'grand') arreterSon();
  if (v !== 'scene') SC = null;
  if (v !== 'lieu') FE = null;
  document.body.classList.toggle('famille', !!S.famille);
  if (S.famille) {
    const f = {'': famAccueil, lieu: () => famById[a] ? famLieu(a) : vueLieu(a), passeport: famCarnet}[v || ''];
    if (f) return f();
  }
  ({lieu: () => vueLieu(a), grand: () => vueLieu(a), carte: () => vueCarte(a), circuits: vueCircuits, circuit: () => vueCircuit(a),
    parler: vueParler, scene: () => vueScene(a),
    passeport: vuePasseport, plus: vuePlus, pratique: vuePratique, mots: vueMots}[v] || vueAccueil)();
}
window.addEventListener('hashchange', route);

document.addEventListener('change', ev => {
  if (ev.target.id === 'trad') { S.trad = ev.target.checked; garder(); if (SC) vueScene(SC.id); }
  if (ev.target.id === 'prenom') { S.prenom = ev.target.value.trim().slice(0, 30); garder(); }
});
document.addEventListener('click', ev => {
  const b = ev.target.closest('button'); if (!b) return;
  if (b.dataset.choisir) { S.lang = b.dataset.choisir; garder(); route(); }
  else if (b.dataset.lang) { const ancien = enCours && enCours.id; arreterSon(); S.lang = b.dataset.lang; garder(); route(); }
  else if (b.dataset.retour !== undefined) { if (history.length > 1) history.back(); else location.hash = b.dataset.retour; }
  else if (b.dataset.filtre) { S.filtre = b.dataset.filtre; garder(); vueAccueil(); }
  else if (b.dataset.pres) {
    if (S.pres) { S.pres = false; garder(); vueAccueil(); return; }
    if (!navigator.geolocation) { toast(t('presRefus')); return; }
    navigator.geolocation.getCurrentPosition(p => { position = [p.coords.latitude, p.coords.longitude]; S.pres = true; vueAccueil(); },
      () => { toast(t('presRefus')); }, {timeout: 10000, maximumAge: 120000});
  }
  else if (b.id === 'ecoute') ecouter(b.dataset.id);
  else if (b.dataset.vit) { S.vit = +b.dataset.vit; garder(); lecteur.playbackRate = S.vit;
    document.querySelectorAll('[data-vit]').forEach(x => x.setAttribute('aria-pressed', +x.dataset.vit === S.vit)); }
  else if (b.dataset.tampon) {
    const id = b.dataset.tampon, y = window.scrollY;
    if (S.tampons[id]) delete S.tampons[id];
    else { S.tampons[id] = new Date().toISOString(); toast(t('nouveauT')); }
    garder(); const joue = enCours; vueLieu(id); window.scrollTo(0, y); enCours = joue; majEcoute();
  }
  else if (b.dataset.mot !== undefined) direMot(+b.dataset.mot);
  else if (b.dataset.famille) { S.famille = b.dataset.famille === '1'; garder(); location.hash = ''; route(); window.scrollTo(0, 0); }
  else if (b.dataset.fsong) direFam(sonFamG(b.dataset.fsong), L(D.filou[b.dataset.fsong]), aSonG(b.dataset.fsong));
  else if (FE && b.dataset.fson) { const e = famById[FE.id], x = b.dataset.fson;
    const txt = x === 'r' ? L(e.raconte) : x === 'e' ? `${L(e.enigme.q)} ${e.enigme.choix.map(L).join(', ')}` : x === 'b' ? L(e.enigme.bravo) : L(e.defi);
    direFam(sonFam(e.lieu, x), txt, aSonFam()); }
  else if (FE && b.dataset.frep !== undefined) famRepondre(+b.dataset.frep);
  else if (b.dataset.imprimer) imprimerDiplome();
  else if (SC && (b.dataset.scene || b.dataset.choix !== undefined)) actionScene(b);
  else if (SC && b.dataset.son) direScene(D.scenes.find(x => x.id === SC.id), b.dataset.son, !!b.dataset.lent);
});

route();
if ('serviceWorker' in navigator) window.addEventListener('load', () => navigator.serviceWorker.register('/sw.js').catch(() => {}));
</script>
</body>
</html>
"""

if __name__ == "__main__":
    main()
