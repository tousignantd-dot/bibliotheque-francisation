#!/usr/bin/env python3
"""Génère les 20 images de module-n2-colis.

Deux destinations :
  · `images/` — les six illustrations de l'exercice de glisser-déposer ;
  · `vocab/`  — les quatorze photos du banc de vocabulaire, réduites à 800 px.

**Format 3:2 paysage** : la zone de glisser-déposer est un rectangle de
223 x 132 px, un rapport de 1,7. Une image carrée y perd le tiers du haut et
du bas.

**La route n'est plus fixée ici.** Les modules précédents appelaient fal.ai en
dur ; depuis le 21 août 2026, `build/route_images.py` essaie les fournisseurs
dans l'ordre du prix mesuré (Google direct, puis fal.ai, puis WaveSpeed) et
dit lequel a servi. Ce script se contente de lui donner un prompt.

La difficulté propre à ce module est que **tout son univers est couvert
d'écriture** : un timbre, une adresse, un formulaire, un carton d'avis, un
reçu. Or le générateur a l'ordre de ne produire aucun texte lisible. Les
prompts demandent donc des objets dont la **forme** est reconnaissable sans
qu'un mot ne se lise — une enveloppe blanche avec un carré dentelé dans le
coin, une boîte brune fermée au ruban, un carton rectangulaire qui dépasse
d'une fente. L'élève reconnaît l'objet ; c'est l'exercice qui en donne le
contenu, et le bandeau noir du Défi 1 tient le texte exact de l'adresse.

Une image à la fois, journal .json adjacent dans ~/Claude/generations, puis
copie vers le module. Relançable : une image déjà présente est sautée.

  python3 build/contenu/module-n2-colis/gen_images.py
  python3 build/contenu/module-n2-colis/gen_images.py poste-colis
"""
import io
import json
import pathlib
import sys
import time

MODULE = 'module-n2-colis'
BASE = pathlib.Path(__file__).resolve().parent          # build/contenu/<slug>/
RACINE = BASE.parents[2]                                # la racine du dépôt
SORTIE = RACINE / 'assets' / 'interactive' / MODULE
GEN = pathlib.Path.home() / 'Claude' / 'generations'
RATIO = '3:2'

sys.path.insert(0, str(BASE.parent.parent))             # jusqu'à build/
from route_images import generer_image, ESTIMATIONS     # noqa: E402

SANS = ("Aucun texte lisible, aucun mot déchiffrable, aucune écriture "
        "reconnaissable, aucun chiffre, aucun nom, aucun logo, aucune marque, "
        "aucun filigrane, aucun visage, aucune personne identifiable — les "
        "personnes, s'il y en a, sont vues de dos ou cadrées sans le visage. "
        "L'écriture manuscrite et imprimée, quand il y en a, se lit comme des "
        "traits gris flous, hors foyer.")

# Le décor principal : un comptoir postal de quartier, à Montréal.
COMPTOIR = ("Photographie réaliste, format paysage, lumière d'intérieur "
            "douce et neutre. Comptoir postal au fond d'une pharmacie de "
            "quartier, à Montréal : comptoir de mélamine claire, tablettes, "
            "boîtes empilées derrière. Palette sobre, sans marque visible. "
            + SANS)

# Ce qui se photographie de près, à hauteur de main.
PRES = ("Photographie réaliste, format paysage, vue rapprochée en lumière "
        "naturelle douce, faible profondeur de champ, palette neutre. " + SANS)

# La rue : une rue résidentielle de Montréal, hors hiver.
RUE = ("Photographie réaliste, format paysage, lumière du jour douce. Rue "
       "résidentielle de Montréal : immeubles de brique, escaliers "
       "extérieurs de métal, trottoir. Palette sobre. " + SANS)

# L'intérieur d'un logement : la table de cuisine, l'entrée.
DEDANS = ("Photographie réaliste, format paysage, lumière d'intérieur douce "
          "par une fenêtre. Logement ordinaire de Montréal, mobilier simple, "
          "palette calme. " + SANS)

P_EX = "Je découvre · Exercice 3 — Qu'est-ce qu'on voit sur la photo ?"
P_VOC = "Je retiens des mots — banc de vocabulaire"

# (nom, dossier, page, prompt)
IMAGES = [
 # ── Les six images de l'exercice de glisser-déposer ───────────────────
 ('poste-enveloppe', 'images', P_EX, PRES + " Une enveloppe blanche posée à "
  "plat sur une table de bois clair, vue d'en haut, avec un petit carré de "
  "papier dentelé collé dans le coin supérieur droit ; quelques lignes "
  "d'écriture manuscrite au centre, entièrement floues et illisibles."),
 ('poste-colis', 'images', P_EX, PRES + " Une boîte de carton brun fermée "
  "avec du ruban d'emballage transparent, posée sur une table, vue de trois "
  "quarts, coins bien nets, aucune étiquette lisible."),
 ('poste-boite', 'images', P_EX, RUE + " Une boîte aux lettres publique rouge "
  "vif, haute, à fente horizontale, plantée sur le trottoir au coin d'une "
  "rue, vue de trois quarts, immeubles de brique derrière, hors foyer."),
 ('poste-comptoir', 'images', P_EX, COMPTOIR + " Vue large du comptoir "
  "postal : la surface du comptoir au premier plan, une pile de boîtes "
  "brunes et des tablettes derrière, personne au premier plan."),
 ('poste-avis', 'images', P_EX, PRES + " Gros plan sur une rangée de petites "
  "boîtes aux lettres d'immeuble en métal gris, à l'intérieur d'une entrée ; "
  "un carton rectangulaire pâle dépasse de l'une des fentes, son texte "
  "entièrement flou."),
 ('poste-balance', 'images', P_EX, COMPTOIR + " Une boîte de carton brun "
  "posée sur le plateau d'une balance de comptoir, vue de côté, l'écran de "
  "la balance flou et sans chiffre lisible."),

 # ── Les quatorze photos du banc de vocabulaire ────────────────────────
 ('lettre', 'vocab', P_VOC, DEDANS + " Une feuille de papier pliée en trois, "
  "posée à côté d'une enveloppe ouverte sur une table de cuisine, vue d'en "
  "haut, l'écriture entièrement floue."),
 ('enveloppe', 'vocab', P_VOC, PRES + " Une enveloppe blanche fermée, seule, "
  "posée à plat sur une surface neutre, vue d'en haut, coin supérieur droit "
  "vide, aucune écriture lisible."),
 ('timbre', 'vocab', P_VOC, PRES + " Gros plan sur un petit carré de papier "
  "aux bords dentelés collé dans le coin d'une enveloppe blanche, motif "
  "coloré abstrait, aucun mot ni chiffre déchiffrable."),
 ('colis', 'vocab', P_VOC, PRES + " Une boîte de carton brun fermée au ruban, "
  "vue de trois quarts sur une table de bois, sans aucune étiquette."),
 ('boite-aux-lettres', 'vocab', P_VOC, RUE + " Une boîte aux lettres publique "
  "rouge sur un trottoir, vue de face, sa fente bien visible, arbre et "
  "façade de brique derrière, hors foyer."),
 ('comptoir-postal', 'vocab', P_VOC, COMPTOIR + " Le comptoir vu de face "
  "depuis la file, tablettes d'enveloppes et de boîtes derrière, une "
  "silhouette de dos au bout du comptoir."),
 ('adresse', 'vocab', P_VOC, PRES + " Gros plan en plongée sur une main qui "
  "écrit au stylo sur une enveloppe blanche posée à plat ; les lignes "
  "d'écriture sont grises et complètement illisibles."),
 ('code-postal', 'vocab', P_VOC, PRES + " Gros plan sur le bas d'une "
  "enveloppe blanche où une rangée de petites cases carrées vides attend "
  "d'être remplie, faible profondeur de champ."),
 ('rue', 'vocab', P_VOC, RUE + " Vue en enfilade d'une rue résidentielle de "
  "Montréal, escaliers extérieurs de métal en rangée, arbres, trottoir vide."),
 ('appartement', 'vocab', P_VOC, PRES + " Gros plan sur une porte de logement "
  "dans un couloir d'immeuble, avec un petit chiffre de métal fixé dessus, "
  "flou et illisible, poignée et cadre bien nets."),
 ('formulaire', 'vocab', P_VOC, PRES + " Une feuille de papier blanc couverte "
  "de rectangles et de lignes vides, posée sur un comptoir avec un stylo "
  "à côté, vue d'en haut ; aucun mot lisible, seulement la grille des cases."),
 ('signature', 'vocab', P_VOC, PRES + " Gros plan sur une main qui tient un "
  "stylo au-dessus d'une ligne tracée au bas d'une feuille, le geste "
  "suspendu, le reste de la feuille flou."),
 ('avis-de-livraison', 'vocab', P_VOC, PRES + " Un carton rectangulaire pâle "
  "tenu à la main devant une rangée de boîtes aux lettres d'immeuble en "
  "métal, son impression entièrement floue et illisible."),
 ('recu', 'vocab', P_VOC, PRES + " Un petit ruban de papier étroit et "
  "légèrement enroulé, posé sur un comptoir clair, vu d'en haut, son "
  "impression réduite à des traits gris flous."),
]


def reduire(data, largeur=800, qualite=82):
    """Les photos du banc sont vues petites : 1024 px n'y sert à rien."""
    from PIL import Image
    im = Image.open(io.BytesIO(data)).convert('RGB')
    hauteur = max(1, round(largeur * im.height / im.width))
    im = im.resize((largeur, hauteur), Image.LANCZOS)
    tampon = io.BytesIO()
    im.save(tampon, 'JPEG', quality=qualite, optimize=True)
    return tampon.getvalue()


def main():
    voulus = set(sys.argv[1:])
    GEN.mkdir(parents=True, exist_ok=True)
    horodatage = time.strftime('%Y%m%d-%H%M%S')
    faits, sautes, echecs, cout = [], [], [], 0.0

    for nom, dossier, page, prompt in IMAGES:
        etiquette = '%s/%s' % (dossier, nom)
        if voulus and nom not in voulus and etiquette not in voulus:
            continue
        dest = SORTIE / dossier
        dest.mkdir(parents=True, exist_ok=True)
        cible = dest / (nom + '.jpg')
        if cible.exists() and cible.stat().st_size > 1000:
            sautes.append(etiquette)
            continue
        try:
            data, route = generer_image(prompt, ratio=RATIO, module=MODULE,
                                        cible=etiquette)
        except Exception as e:
            echecs.append('%s : %s' % (etiquette, str(e)[:200]))
            continue

        brut = data
        if dossier == 'vocab':
            try:
                data = reduire(data)
            except Exception as e:
                echecs.append('%s : réduction impossible (%s) — image brute '
                              'gardée' % (etiquette, e))

        base = '%s_%s-%s_%s' % (MODULE, dossier, nom, horodatage)
        (GEN / (base + '.jpg')).write_bytes(brut)
        (GEN / (base + '.json')).write_text(json.dumps({
            "route": route,
            "prompt": prompt,
            "refs": [],
            "params": {"aspect_ratio": RATIO, "resolution": "1K",
                       "output_format": "jpeg"},
            "cost_estimate_usd": ESTIMATIONS.get(route, 0.0),
            "created": time.strftime('%Y-%m-%dT%H:%M:%S+00:00', time.gmtime()),
            "projet": "bibliotheque-francisation",
            "module": MODULE,
            "page": page,
            "destination": "assets/interactive/%s/%s/%s.jpg"
                           % (MODULE, dossier, nom),
        }, ensure_ascii=False, indent=2), encoding='utf-8')
        cible.write_bytes(data)
        cout += ESTIMATIONS.get(route, 0.0)
        faits.append(etiquette)
        print('  ✓ %-28s %6.1f Ko  (%s)'
              % (etiquette, len(data) / 1024, route), flush=True)

    print()
    print('%d produite(s), %d sautée(s), %d échec(s) · environ %.2f $'
          % (len(faits), len(sautes), len(echecs), cout))
    for e in echecs:
        print('  !! ' + e)


if __name__ == '__main__':
    main()
