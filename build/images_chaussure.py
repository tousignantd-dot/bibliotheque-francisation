#!/usr/bin/env python3
"""Le visuel de l'offre « détail » — un magasin de chaussures.

    python3 build/images_chaussure.py --essai     # ne dépense rien
    python3 build/images_chaussure.py             # ce qui manque
    python3 build/images_chaussure.py reserve     # une seule

CINQ IMAGES, et chacune montre **un moment nommé** de la liste des dix
situations de `vendre-au-comptoir.html` — jamais « le thème de l'offre ».
C'est le défaut le plus fréquent des images du dépôt, et le seul qui ne se
voie pas sans mettre l'image et la phrase côte à côte.

LE MÊME REGISTRE QUE BELRIVE, exprès : photographie réaliste, 3:2, lumière
douce. Les deux secteurs sont la même ligne de produits ; deux registres
feraient deux offres.

PERSONNE DANS LE CADRE. Convention héritée de Belrive, et elle n'est pas
qu'esthétique : elle évite les visages, les mains et l'identifiable, et elle
oblige à faire porter le moment par **les objets**. Une boîte repoussée sur un
comptoir raconte un retour ; un trou dans un mur de boîtes raconte « je vais
voir en arrière ».

LA DIFFICULTÉ PROPRE À CE PLANCHER, et elle est pire qu'à l'usine : tout y est
écrit ET marqué. Boîtes à la marque du fabricant, étiquettes de prix, affiches
de rabais, logos sur les semelles et les languettes. La parade est celle du
17 septembre : **on ne l'interdit pas, on cadre.** Boîtes de carton uni vues de
côté, chaussures sans logo ni bande reconnaissable, murs nus, papier plié côté
blanc. Décrire ce qu'on veut, pas ce qu'on ne veut pas.

Sortie : assets/presentations/chaussure/
"""
import io, json, pathlib, sys, time

RACINE = pathlib.Path(__file__).resolve().parents[1]
GEN  = pathlib.Path.home() / 'Claude' / 'generations'
BASE = RACINE / 'assets' / 'presentations' / 'chaussure'
RATIO = "3:2"
MODULE = 'offre-chaussure'

sys.path.insert(0, str(RACINE / 'build'))
from route_images import generer_image, ESTIMATIONS

# Le décor commun. Un magasin ordinaire, pas une boutique de luxe : c'est un
# employeur qui engage au salaire minimum qu'on veut reconnaître.
MAGASIN = ("Photographie réaliste, format paysage, objectif 35 mm, lumière "
           "douce et chaude de commerce, faible profondeur de champ. Un magasin "
           "de chaussures ordinaire de quartier, au Québec : plancher de bois "
           "clair, murs blancs nus, étagères de bois blond, quelques plantes. "
           "Ni luxe ni boutique de mode. ")

SANS = ("Aucun texte, aucun mot, aucun chiffre, aucune lettre, aucune étiquette "
        "de prix, aucune affiche, aucune pancarte, aucun écriteau, aucun logo, "
        "aucune marque de fabricant, aucun autocollant, aucun code-barres. Les "
        "boîtes sont de carton uni et lisse, sans impression. Les chaussures "
        "sont unies, sans logo, sans bande latérale, sans motif reconnaissable. "
        "Aucun visage, aucune personne, aucune main dans le cadre.")

IMAGES = [
    ('magasin', 'l\'ouverture — où ça se passe',
     MAGASIN +
     "Vue d'ensemble du plancher de vente, prise de l'entrée à hauteur d'yeux. "
     "Sur la gauche, un mur d'étagères de bois portant des chaussures posées "
     "une par une sur de petits supports inclinés, bien espacées. Au centre, "
     "deux bancs d'essayage bas en bois avec un miroir au sol. Au fond à "
     "droite, un comptoir de bois clair, flou. Le magasin est vide et ouvert, "
     "en début de journée. " + SANS),

    ('essayage', 'situation 2 — la pointure et la largeur',
     MAGASIN +
     "Gros plan de trois quarts sur un banc d'essayage bas en bois, vu de "
     "dessus en légère plongée. Sur le banc : une boîte de carton uni ouverte, "
     "son couvercle posé à côté, du papier de soie blanc replié à l'intérieur, "
     "et une seule chaussure de cuir brun unie posée à plat, sans logo. Par "
     "terre devant le banc, un chausse-pied métallique et une deuxième boîte "
     "fermée. Le fond est flou. " + SANS),

    ('reserve', 'situation 6 — « je vais voir en arrière »',
     "Photographie réaliste, format paysage, objectif 35 mm, lumière crue de "
     "néon au plafond. L'arrière-boutique d'un magasin de chaussures : une "
     "allée étroite entre deux hautes étagères de métal chargées du sol au "
     "plafond de boîtes de carton uni empilées de côté, toutes identiques, "
     "lisses et sans impression. À mi-hauteur sur l'étagère de gauche, **un "
     "trou** : une boîte manque dans la rangée, l'espace vide est net et bien "
     "visible. L'allée s'enfonce vers le fond, floue. Personne dans le champ. "
     + SANS),

    ('comptoir', 'situation 3 — le retour et l\'échange',
     MAGASIN +
     "Gros plan à hauteur du comptoir, vu depuis la place du client. Sur le "
     "dessus de bois clair : une boîte de carton uni fermée, poussée de biais "
     "vers l'avant comme si on venait de la faire glisser, et un sac de papier "
     "brun plié à côté. Un petit terminal de paiement est tourné de dos, son "
     "écran hors de vue. Derrière le comptoir, le mur blanc nu et une étagère "
     "floue. Personne. " + SANS),

    ('fiche-poche', 'ce qu\'on laisse sur le comptoir',
     "Photographie réaliste, format paysage, objectif 50 mm, lumière douce de "
     "fin de journée. Un tablier de travail en toile bleu foncé suspendu à un "
     "crochet sur un mur blanc, cadré sur la poche ventrale : une feuille de "
     "papier pliée en deux dépasse de la poche, on n'en voit que le dos, "
     "entièrement blanc et vierge. La toile est propre, un peu froissée. Le "
     "tablier est vide, personne ne le porte. " + SANS),
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


essai = '--essai' in sys.argv
voulus = set(a for a in sys.argv[1:] if not a.startswith('--'))
if not essai:
    GEN.mkdir(parents=True, exist_ok=True)
    BASE.mkdir(parents=True, exist_ok=True)
horodatage = time.strftime('%Y%m%d-%H%M%S')
faits, sautes, echecs, cout = [], [], [], 0.0

for nom, moment, prompt in IMAGES:
    if voulus and nom not in voulus:
        continue
    cible = BASE / (nom + '.jpg')
    if cible.exists() and cible.stat().st_size > 1000:
        sautes.append(nom); continue
    if essai:
        print('  %-12s %4d caractères · %s' % (nom, len(prompt), moment))
        continue
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
        "page": moment,
        "destination": "assets/presentations/chaussure/%s.jpg" % nom,
    }, ensure_ascii=False, indent=2), encoding='utf-8')
    cible.write_bytes(data)
    faits.append(nom)
    cout += ESTIMATIONS.get(route, 0.08)
    print('  ✓ %-12s %6.1f Ko   %s' % (nom, len(data) / 1024, route), flush=True)

print()
if essai:
    print('  À BLANC — rien n\'a été engendré, rien n\'a été payé.')
else:
    print('%d produite(s), %d sautée(s), %d échec(s) · environ %.2f $'
          % (len(faits), len(sautes), len(echecs), cout))
    for e in echecs:
        print('  ✗ ' + e)
