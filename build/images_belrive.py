#!/usr/bin/env python3
"""Les trois images du bloc 3 — démonstration entreprise (Aliments Belrive).

    python3 build/images_belrive.py           # ce qui manque
    python3 build/images_belrive.py palette   # une seule

Trois images, pas davantage, et **chacune montre ce que dit son écran** —
jamais « le thème du module ». C'est le défaut le plus fréquent des images du
dépôt, et le seul qui ne se voie pas sans mettre l'image et la phrase côte à
côte : ici, la palette de l'écran 1, la chemise jaune de l'écran 3, la fiche
dans la poche de l'écran 8.

La difficulté propre à une usine, c'est **le texte partout** : affiches de
sécurité, étiquettes de lot, caisses moulées à la marque du fabricant, pancartes
de zone. La parade n'est pas de l'interdire — un modèle écrit le mot quand même,
en charabia — mais de **cadrer** : murs de béton nus, caisses lisses vues de
côté, chemise fermée, papier plié côté blanc. Décrire ce qu'on veut, pas ce
qu'on ne veut pas.

Format 3:2 : le bloc `.fig` de la storyline est un rectangle, comme les zones
de dépôt des modules. Réduction à 1200 px, qualité 85 — l'image occupe toute la
largeur du texte et se regarde de près.

L'appel passe par `build/route_images.py`, jamais par un fournisseur en dur :
Google en direct, puis fal.ai, puis WaveSpeed — l'ordre du prix. La route qui a
servi est écrite dans le journal .json adjacent, pour qu'un repli ne passe
jamais inaperçu.

Sortie : assets/interactive/entreprise-belrive/images/
"""
import io, json, pathlib, sys, time

MODULE = 'entreprise-belrive'
RACINE = pathlib.Path(__file__).resolve().parents[1]
GEN  = pathlib.Path.home() / 'Claude' / 'generations'
BASE = RACINE / 'assets' / 'interactive' / MODULE / 'images'
RATIO = "3:2"

sys.path.insert(0, str(RACINE / 'build'))
from route_images import generer_image, ESTIMATIONS

# Le décor commun. Nommé, québécois, et **sans une seule surface écrite** :
# c'est le cadrage qui tient la règle, pas l'interdiction.
USINE = ("Photographie réaliste, format paysage, objectif 35 mm, lumière "
         "industrielle froide au plafond. Une usine de conditionnement et de "
         "surgélation de légumes au Québec : sol de béton peint gris, murs de "
         "béton nus et clairs, équipement en acier inoxydable. ")

SANS = ("Aucun texte, aucun mot, aucun chiffre, aucune lettre, aucune "
        "étiquette imprimée, aucune affiche, aucune pancarte, aucun logo, "
        "aucune marque de fabricant, aucun autocollant, aucun pochoir sur le "
        "sol. Aucun visage, aucune main en gros plan, aucune personne "
        "identifiable. Toutes les surfaces sont lisses et nues.")

IMAGES = [
    ('palette', 'écran 1 — « la deux est pleine, tu la vides »',
     USINE +
     "Une allée de travail vue à hauteur d'yeux, en légère plongée. Au premier "
     "plan à droite, une palette de bois chargée de caisses de plastique gris "
     "uni empilées sur quatre rangs, vues de côté : les caisses sont lisses, "
     "sans inscription moulée ni étiquette. Derrière, l'allée s'enfonce, floue, "
     "vers un convoyeur d'acier inoxydable. Les murs sont de béton nu, sans "
     "affiche ni pancarte. Personne dans le champ. " + SANS),

    ('chemise-jaune', 'écran 3 — « celles-là, dans la chemise jaune »',
     USINE +
     "Gros plan de trois quarts sur un plan de travail en acier inoxydable "
     "brossé. Au centre, une chemise cartonnée jaune vif, **fermée**, posée à "
     "plat, légèrement de biais : sa couverture est entièrement lisse et vierge. "
     "À côté, un crayon de bois couché. Le fond est flou, un mur de béton clair. "
     "Aucune feuille ne dépasse, aucune main n'entre dans le cadre. " + SANS),

    ('sarrau', 'écran 8 — ce qu\'on emporte dans la poche',
     "Photographie réaliste, format paysage, objectif 50 mm, lumière douce de "
     "vestiaire. Un sarrau de travail blanc suspendu à un crochet d'acier sur "
     "un mur de béton clair, cadré sur la poitrine et la poche de poitrine : "
     "une feuille de papier pliée en deux dépasse de la poche, on n'en voit que "
     "le dos, entièrement blanc et vierge. Le tissu est propre, un peu froissé. "
     "Aucune personne, le sarrau est vide. " + SANS),
]


def reduire(data, largeur=1200, qualite=85):
    """L'image occupe la largeur du texte et se regarde de près."""
    from PIL import Image
    im = Image.open(io.BytesIO(data)).convert('RGB')
    hauteur = max(1, round(largeur * im.height / im.width))
    im = im.resize((largeur, hauteur), Image.LANCZOS)
    tampon = io.BytesIO()
    im.save(tampon, 'JPEG', quality=qualite, optimize=True)
    return tampon.getvalue()


voulus = set(sys.argv[1:])
GEN.mkdir(parents=True, exist_ok=True)
BASE.mkdir(parents=True, exist_ok=True)
horodatage = time.strftime('%Y%m%d-%H%M%S')
faits, sautes, echecs, cout = [], [], [], 0.0

for nom, page, prompt in IMAGES:
    if voulus and nom not in voulus:
        continue
    cible = BASE / (nom + '.jpg')
    if cible.exists() and cible.stat().st_size > 1000:
        sautes.append(nom); continue
    try:
        data, route = generer_image(prompt, ratio=RATIO, resolution="1K",
                                    module=MODULE, cible=nom)
    except Exception as e:
        echecs.append('%s : %s' % (nom, e)); continue

    brut = data
    try:
        data = reduire(data)
    except Exception as e:
        echecs.append('%s : réduction impossible (%s) — image brute gardée' % (nom, e))

    base = '%s_images-%s_%s' % (MODULE, nom, horodatage)
    (GEN / (base + '.jpg')).write_bytes(brut)
    (GEN / (base + '.json')).write_text(json.dumps({
        "model": "nano-banana-2",
        "prompt": prompt,
        "refs": [],
        "params": {"num_images": 1, "aspect_ratio": RATIO,
                   "resolution": "1K", "output_format": "jpeg"},
        "provider": route,
        "cost_estimate_usd": ESTIMATIONS.get(route, 0.08),
        "created": time.strftime('%Y-%m-%dT%H:%M:%S+00:00', time.gmtime()),
        "projet": "bibliotheque-francisation",
        "module": MODULE,
        "page": page,
        "destination": "assets/interactive/%s/images/%s.jpg" % (MODULE, nom),
    }, ensure_ascii=False, indent=2), encoding='utf-8')
    cible.write_bytes(data)
    faits.append(nom)
    cout += ESTIMATIONS.get(route, 0.08)
    print('  ✓ %-16s %6.1f Ko   %s' % (nom, len(data) / 1024, route), flush=True)

print()
print('%d produite(s), %d sautée(s), %d échec(s) · environ %.2f $'
      % (len(faits), len(sautes), len(echecs), cout))
for e in echecs:
    print('  !! ' + e)
