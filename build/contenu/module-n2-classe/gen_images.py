#!/usr/bin/env python3
"""Génère les 18 images de module-n2-classe via fal.ai (Nano Banana 2).

Deux destinations :
  · `images/` — les six illustrations de l'exercice de glisser-déposer,
    telles que rendues ;
  · `vocab/`  — les douze photos du banc de vocabulaire, réduites à 800 px.

**Format 3:2 paysage** : la zone de glisser-déposer mesure 223 x 132 px, un
rapport de 1,7. Une image carrée y perdait le tiers du haut et du bas. Voir
`docs/chantier-tous-niveaux.md`.

La difficulté propre à ce module : **tout se passe dans une seule pièce**, et
le générateur a l'ordre de ne montrer aucune personne identifiable. Le risque
n'est donc pas le visage — c'est que dix-huit images de la même salle se
ressemblent. Les prompts changent donc de distance à chaque fois : le gros
plan sur un objet posé, le pupitre vu d'en haut, la salle vue du fond, la
porte vue du corridor.

Deuxième difficulté, propre à une classe : **il y a du texte partout dans une
vraie salle de cours** — au tableau, sur les cahiers, sur l'avis affiché. Les
prompts demandent explicitement des traces d'écriture illisibles, des lignes
grises, des pages blanches : la consigne « aucun texte lisible » est répétée
dans chaque décor.

Une image à la fois, journal .json adjacent dans ~/Claude/generations, puis
copie vers le module. Relançable : une image déjà présente est sautée.

  python3 build/contenu/module-n2-classe/gen_images.py
  python3 build/contenu/module-n2-classe/gen_images.py cahier-ouvert
"""
import io, json, os, pathlib, sys, time, urllib.request, urllib.error

MODULE = 'module-n2-classe'
GEN  = pathlib.Path('/Users/danieltousignant/Claude/generations')
BASE = pathlib.Path('/Users/danieltousignant/Claude/bibliotheque-francisation'
                    '/assets/interactive/' + MODULE)
ENV  = pathlib.Path('/Users/danieltousignant/Claude/.env')
RATIO = "3:2"


def cle(nom):
    for ligne in ENV.read_text(encoding='utf-8').splitlines():
        ligne = ligne.strip()
        if ligne.startswith(nom + '='):
            return ligne.split('=', 1)[1].strip().strip('"\'')
    return ''


FAL = cle('FAL_KEY')
if not FAL:
    sys.exit('FAL_KEY absente de ~/Claude/.env')

SANS = ("Aucun texte lisible, aucun mot déchiffrable, aucune écriture "
        "reconnaissable, aucun chiffre, aucun logo, aucune marque, aucun "
        "filigrane, aucun visage, aucune personne identifiable — les "
        "personnes, s'il y en a, sont vues de dos ou cadrées sans le visage. "
        "L'écriture, quand il y en a, se lit comme des traits gris flous.")

# Le décor principal : une salle de classe d'un centre de formation aux
# adultes, au Québec. Néons doux, mobilier simple, palette neutre.
CLASSE = ("Photographie réaliste, format paysage, lumière de néons doux et "
          "d'une fenêtre. Salle de classe d'un centre de formation pour "
          "adultes au Québec : tables simples, chaises empilables, tableau "
          "blanc, murs pâles, palette neutre et calme. " + SANS)

# Le gros plan sur ce qui est posé sur une table de travail.
TABLE = ("Photographie réaliste, format paysage, faible profondeur de champ, "
         "lumière naturelle rasante. Gros plan sur le dessus d'une table de "
         "classe en stratifié pâle, un peu usée. Palette sobre. " + SANS)

# Le corridor du centre, et ce qui y est affiché.
CORRIDOR = ("Photographie réaliste, format paysage, lumière de néons. "
            "Corridor d'un centre de formation : murs de blocs peints, "
            "planchers de tuiles, portes de bois clair. Palette neutre et "
            "froide. " + SANS)

P_EX  = "Je découvre · Exercice 3 — Ce qu'il y a dans la classe"
P_VOC = "Je retiens des mots — banc de vocabulaire"

# (nom, dossier, page, prompt)
IMAGES = [
 # ── Les six images de l'exercice de glisser-déposer ───────────────────
 ('cahier-ouvert', 'images', P_EX, TABLE + " Un cahier à spirale ouvert au "
  "milieu, ses deux pages lignées presque vides, un crayon posé en travers de "
  "la reliure."),
 ('tableau-classe', 'images', P_EX, CLASSE + " Le tableau blanc vu de face, "
  "presque vide, avec des traces d'effacement grises et deux marqueurs posés "
  "sur la tablette du bas."),
 ('pupitre-eleve', 'images', P_EX, CLASSE + " Un seul pupitre d'élève vu de "
  "trois quarts, sa chaise poussée en dessous, un sac de toile accroché au "
  "dossier, le reste de la salle flou derrière."),
 ('boite-crayons', 'images', P_EX, TABLE + " Une boîte de carton ouverte "
  "remplie de crayons de plomb et de stylos de couleurs différentes, vue "
  "légèrement d'en haut."),
 ('horloge-classe', 'images', P_EX, CLASSE + " Une horloge ronde de salle de "
  "classe, à aiguilles, accrochée haut sur un mur pâle, cadrée en gros plan, "
  "sans chiffres lisibles."),
 ('avis-porte', 'images', P_EX, CORRIDOR + " Une feuille blanche affichée avec "
  "du ruban sur la vitre d'une porte de classe, vue de biais : les lignes "
  "d'écriture se devinent comme des traits gris flous, aucun mot n'est "
  "lisible."),

 # ── Les douze photos du banc de vocabulaire ───────────────────────────
 ('cahier', 'vocab', P_VOC, TABLE + " Un cahier à couverture unie fermé, posé "
  "seul au centre de la table, vu légèrement d'en haut."),
 ('crayon', 'vocab', P_VOC, TABLE + " Gros plan sur trois crayons de plomb "
  "taillés, posés côte à côte, dont un rouge."),
 ('feuille', 'vocab', P_VOC, TABLE + " Une feuille de papier blanche, "
  "entièrement vide, posée seule sur la table, un coin légèrement relevé."),
 ('gomme', 'vocab', P_VOC, TABLE + " Gros plan sur une gomme à effacer blanche "
  "un peu usée, posée à côté de quelques miettes de gomme."),
 ('tableau', 'vocab', P_VOC, CLASSE + " Le coin gauche d'un tableau blanc, avec "
  "sa brosse posée sur la tablette et des traces d'effacement grises."),
 ('pupitre', 'vocab', P_VOC, CLASSE + " Deux rangées de pupitres vides vues "
  "depuis le fond de la salle, chaises rangées dessous."),
 ('page', 'vocab', P_VOC, TABLE + " Gros plan sur une page de cahier lignée, "
  "presque vide, avec un doigt qui tourne le coin de la page."),
 ('effacer', 'vocab', P_VOC, TABLE + " Une main tient une gomme à effacer et "
  "frotte une page de cahier, cadrée au poignet, en mouvement."),
 ('pause', 'vocab', P_VOC, CORRIDOR + " Un banc de bois vide contre un mur de "
  "corridor, avec un gobelet de carton posé dessus et une porte au fond."),
 ('conge', 'vocab', P_VOC, CORRIDOR + " Une porte de classe fermée, lumière "
  "éteinte derrière la vitre, corridor désert, fin de journée."),
 ('calendrier', 'vocab', P_VOC, CLASSE + " Un calendrier mural à grande grille "
  "accroché près d'une porte, vu de biais, ses cases vides, aucun chiffre "
  "lisible."),
 ('retard', 'vocab', P_VOC, CORRIDOR + " Une silhouette de dos, sac à l'épaule, "
  "marche vite vers une porte de classe au bout du corridor, léger flou de "
  "mouvement."),
]


def genere(prompt):
    corps = json.dumps({"prompt": prompt, "num_images": 1, "aspect_ratio": RATIO,
                        "resolution": "1K", "output_format": "jpeg"}).encode()
    req = urllib.request.Request(
        "https://fal.run/fal-ai/nano-banana-2", data=corps,
        headers={"Authorization": "Key " + FAL, "Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=240) as r:
        d = json.loads(r.read())
    with urllib.request.urlopen(d["images"][0]["url"], timeout=240) as r:
        return r.read()


def reduire(data, largeur=800, qualite=82):
    """Les photos du banc sont vues petites : 1024 px n'y sert à rien."""
    from PIL import Image
    im = Image.open(io.BytesIO(data)).convert('RGB')
    hauteur = max(1, round(largeur * im.height / im.width))
    im = im.resize((largeur, hauteur), Image.LANCZOS)
    tampon = io.BytesIO()
    im.save(tampon, 'JPEG', quality=qualite, optimize=True)
    return tampon.getvalue()


voulus = set(sys.argv[1:])
GEN.mkdir(parents=True, exist_ok=True)
horodatage = time.strftime('%Y%m%d-%H%M%S')
faits, sautes, echecs = [], [], []

for nom, dossier, page, prompt in IMAGES:
    etiquette = '%s/%s' % (dossier, nom)
    if voulus and nom not in voulus and etiquette not in voulus:
        continue
    dest = BASE / dossier
    dest.mkdir(parents=True, exist_ok=True)
    cible = dest / (nom + '.jpg')
    if cible.exists() and cible.stat().st_size > 1000:
        sautes.append(etiquette); continue
    try:
        data = genere(prompt)
    except urllib.error.HTTPError as e:
        echecs.append('%s : HTTP %s %s' % (etiquette, e.code, e.read()[:180])); continue
    except Exception as e:
        echecs.append('%s : %s' % (etiquette, e)); continue

    brut = data
    if dossier == 'vocab':
        try:
            data = reduire(data)
        except Exception as e:
            echecs.append('%s : réduction impossible (%s) — image brute gardée'
                          % (etiquette, e))

    base = '%s_%s-%s_%s' % (MODULE, dossier, nom, horodatage)
    (GEN / (base + '.jpg')).write_bytes(brut)
    (GEN / (base + '.json')).write_text(json.dumps({
        "model": "fal-ai/nano-banana-2",
        "prompt": prompt,
        "refs": [],
        "params": {"num_images": 1, "aspect_ratio": RATIO,
                   "resolution": "1K", "output_format": "jpeg"},
        "provider": "fal.ai",
        "cost_estimate_usd": 0.034,
        "created": time.strftime('%Y-%m-%dT%H:%M:%S+00:00', time.gmtime()),
        "projet": "bibliotheque-francisation",
        "module": MODULE,
        "page": page,
        "destination": "assets/interactive/%s/%s/%s.jpg" % (MODULE, dossier, nom),
    }, ensure_ascii=False, indent=2), encoding='utf-8')
    cible.write_bytes(data)
    faits.append(etiquette)
    print('  ✓ %-28s %6.1f Ko' % (etiquette, len(data) / 1024), flush=True)

print()
print('%d produite(s), %d sautée(s), %d échec(s) · environ %.2f $'
      % (len(faits), len(sautes), len(echecs), 0.034 * len(faits)))
for e in echecs:
    print('  !! ' + e)
