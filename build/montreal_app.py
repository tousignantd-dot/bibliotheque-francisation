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
    return {"lieux": lieux, "circuits": ex.CIRCUITS, "pratique": ex.PRATIQUE, "mots": mots}


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
  plus: {fr: 'Pratique', en: 'Good to know', es: 'Práctico'},
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
  aVerifier: {fr: 'Heures et prix changent : vérifiez avant de vous déplacer.', en: 'Hours and prices change: check before you go.', es: 'Horarios y precios cambian: verifique antes de ir.'},
};

// ---------- état (localStorage seulement) ----------
const CLE = 'montreal-poche';
let S = {lang: null, tampons: {}, filtre: 'tout', pres: false, vit: 1};
try { Object.assign(S, JSON.parse(localStorage.getItem(CLE) || '{}')); } catch (e) {}
function garder() { try { localStorage.setItem(CLE, JSON.stringify(S)); } catch (e) {} }
const t = k => (T[k] && (T[k][S.lang] ?? T[k].fr)) ?? k;
const L = o => o ? (o[S.lang] ?? o.fr) : '';
const E = s => String(s ?? '').replace(/[&<>"']/g, c => ({'&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;'}[c]));
const byId = Object.fromEntries(D.lieux.map(l => [l.id, l]));
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
    : `<a class="marque" href="#"><i class="pt"></i><span>${t('titre')}</span></a>`;
  return `<header class="barre"><div class="col">${gauche}<div class="langues" role="group" aria-label="Langue · Language · Idioma">${lg}</div></div></header>`;
}
function onglets(actif) {
  const nav = document.getElementById('onglets');
  nav.hidden = false;
  nav.querySelector('.col').innerHTML = [['', 'decouvrir'], ['#carte', 'carte'], ['#circuits', 'circuits'], ['#passeport', 'passeport'], ['#plus', 'plus']]
    .map(([h, k]) => `<a href="${h || '#'}" ${actif === k ? 'aria-current="page"' : ''}>${IC[k]}<span>${t(k)}</span></a>`).join('');
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
    <a class="progres" href="#passeport">${anneau(n, D.lieux.length)}<span><b>${t('monPass')}</b><small>${n} / ${D.lieux.length} ${t('tampons')}${palier() ? ' — ' + E(palier()) : ''}</small></span></a>
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
  D.lieux.forEach(l => { marq[l.id] = L_.marker(l.geo, {icon: epingle(l.cat)}).addTo(carteObj).bindPopup(pop(l)); });
  if (cible && marq[cible]) { carteObj.setView(byId[cible].geo, 15); marq[cible].openPopup(); }
  else carteObj.fitBounds(D.lieux.map(l => l.geo), {padding: [30, 30]});
  if (position) L_.circleMarker(position, {radius: 8, color: '#fff', weight: 3, fillColor: '#1A73E8', fillOpacity: 1}).addTo(carteObj);
}

function vueCircuits() {
  onglets('circuits');
  app.innerHTML = entete() + `<main class="col"><h2 class="sec">${t('circuits')}</h2><p class="intro">${t('circuitsIntro')}</p>
    <div class="liste">${D.circuits.map(c => `<a class="circuit-carte" href="#circuit/${c.id}">
      <div class="imgs">${c.etapes.slice(0, 3).map(e => `<img src="${img(e)}" alt="" loading="lazy">`).join('')}</div>
      <div class="t"><h3>${E(L(c.nom))}</h3><div class="meta">${c.etapes.length} ${t('etapes')} · ${E(L(c.duree))}</div><p>${E(L(c.intro))}</p></div></a>`).join('')}</div></main>`;
}
function vueCircuit(id) {
  const c = D.circuits.find(x => x.id === id); if (!c) { location.hash = '#circuits'; return; }
  onglets('circuits');
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
    </section><p class="pied">${t('vie')}</p></main>`;
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

// ---------- routeur ----------
function route() {
  if (carteObj) { carteObj.remove(); carteObj = null; }
  if (!S.lang) return vueBienvenue();
  document.documentElement.lang = LOC[S.lang];
  document.title = t('titre');
  const [v, a] = location.hash.slice(1).split('/');
  if (v !== 'lieu') arreterSon();
  ({lieu: () => vueLieu(a), carte: () => vueCarte(a), circuits: vueCircuits, circuit: () => vueCircuit(a),
    passeport: vuePasseport, plus: vuePlus, pratique: vuePratique, mots: vueMots}[v] || vueAccueil)();
}
window.addEventListener('hashchange', route);

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
});

route();
if ('serviceWorker' in navigator) window.addEventListener('load', () => navigator.serviceWorker.register('/sw.js').catch(() => {}));
</script>
</body>
</html>
"""

if __name__ == "__main__":
    main()
