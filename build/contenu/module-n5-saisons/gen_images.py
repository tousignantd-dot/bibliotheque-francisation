#!/usr/bin/env python3
"""Les 19 images de module-n5-saisons.

Deux destinations :
  · `images/` — les six photos de l'exercice `prImg` « Ce que la météo laisse
    au sol » ;
  · `vocab/`  — les treize photos du banc de vocabulaire, réduites à 800 px.

**Format 3:2 paysage** : la zone de glisser-déposer est un rectangle de
223 x 132 px. Une image carrée y perd le tiers du haut et du bas.

**Aucun appel réseau en dur ici.** `generer_image` de `build/route_images.py`
essaie les routes dans l'ordre du prix mesuré le 21 août 2026 — Google direct,
puis fal.ai, puis WaveSpeed — et rend le nom de celle qui a servi, inscrit au
journal de chaque image. Le registre des appels compte les **tentatives**, pas
les fichiers : une image régénérée est payée chaque fois.

Quatre contraintes propres à ce module :

- **Aucun texte lisible nulle part.** Le module travaille les mots de l'avis
  météo — veille, avertissement, degrés, indice UV. Un panneau, un écran de
  téléphone ou une bannière de télévision portant un chiffre donnerait la
  réponse d'un exercice. Les prompts le redisent chaque fois.
- **Aucun visage reconnaissable, aucune personne identifiable.** Les scènes
  où quelqu'un est présent le montrent de dos, de loin, ou cadré aux mains et
  aux bottes. Le module met en scène un groupe de personnes âgées : une photo
  de visage ferait de l'image le portrait de quelqu'un.
- **Aucune scène de catastrophe.** Le verglas, la crue et la canicule
  existent au Québec et abîment de vraies vies. Les images montrent ce qu'un
  élève verra en sortant de chez lui — un trottoir luisant, un sentier sous
  vingt centimètres d'eau, une promenade vide à quinze heures — jamais un
  drame, jamais un dégât spectaculaire, jamais une personne en détresse.
- **Deux des dix-neuf images se recoupent par le sujet** — le verglas et les
  crampons existent en version « exercice » et en version « banc de mots ».
  Les prompts diffèrent volontairement par l'angle, l'heure et le cadrage,
  pour qu'on ne se retrouve pas avec deux fois la même photo dans le même
  module.

Une image à la fois, journal .json adjacent dans ~/Claude/generations, puis
copie vers le module. Relançable : une image déjà présente est sautée. Pour en
refaire une, effacer son fichier d'abord.

  python3 build/contenu/module-n5-saisons/gen_images.py
  python3 build/contenu/module-n5-saisons/gen_images.py crampons
"""
import io, json, pathlib, sys, time

MODULE = 'module-n5-saisons'
GEN  = pathlib.Path('/Users/danieltousignant/Claude/generations')
BASE = pathlib.Path('/Users/danieltousignant/Claude/bibliotheque-francisation'
                    '/assets/interactive/' + MODULE)
RATIO = "3:2"

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent.parent))
from route_images import generer_image                       # noqa: E402

# Trois décors, repris tels quels d'un prompt à l'autre pour que les
# dix-neuf images se ressemblent assez pour tenir dans le même module.
VILLE = ("Photographie réaliste, format paysage, rue ou trottoir d'une petite "
         "ville du Bas-Saint-Laurent au Québec, maisons de bois et de brique, "
         "poteaux et fils électriques, lumière naturelle. Faible profondeur de "
         "champ. Aucun texte lisible, aucune enseigne lisible, aucune plaque "
         "d'immatriculation, aucun visage reconnaissable, aucun logo.")

FLEUVE = ("Photographie réaliste, format paysage, bord du fleuve Saint-Laurent "
          "en aval de Rimouski : galets, herbes hautes, promenade de bois, "
          "horizon très large et très bas. Lumière naturelle. Aucun texte "
          "lisible, aucune enseigne, aucun visage reconnaissable, aucun logo.")

NATURE = ("Photographie réaliste, format paysage, sentier de terre battue "
          "dans une forêt mixte de conifères et de feuillus du Bas-"
          "Saint-Laurent, sous-bois, racines, lumière naturelle diffuse. "
          "Aucun texte lisible, aucun panneau lisible, aucun visage "
          "reconnaissable, aucun logo.")

P_EX  = "Je découvre · Exercice 3 — Ce que la météo laisse au sol"
P_VOC = "Je retiens des mots — banc de vocabulaire"

# (nom, dossier, page, prompt)
IMAGES = [
 # ── Je découvre · les six images de `prImg` ───────────────────────────
 ('verglas-trottoir', 'images', P_EX, VILLE + " Un trottoir de béton "
  "entièrement couvert d'une couche de glace transparente et luisante après "
  "une pluie verglaçante, vu en plongée à hauteur de poitrine, un matin gris. "
  "Les reflets du ciel se voient dans la glace. Aucune personne, aucune "
  "empreinte."),
 ('poudrerie-route', 'images', P_EX, VILLE + " De la neige sèche soulevée par "
  "un vent latéral qui traverse une route de campagne en longues traînées "
  "blanches, vue de loin et de face, fin d'après-midi d'hiver, visibilité très "
  "réduite. Aucun véhicule au premier plan, aucune personne."),
 ('crue-sentier', 'images', P_EX, NATURE + " Un sentier de bord de rivière "
  "recouvert par une trentaine de centimètres d'eau brune et immobile au "
  "printemps, troncs et branches nues reflétés à la surface, neige fondante "
  "en plaques sur les côtés. Aucune personne, aucun panneau."),
 ('canicule-promenade', 'images', P_EX, FLEUVE + " Une promenade de bois "
  "totalement vide écrasée de soleil en plein milieu d'un après-midi d'été, "
  "ombres très courtes, air qui tremble au-dessus des planches, ciel blanc de "
  "chaleur. Aucune personne."),
 ('crampons-botte', 'images', P_EX, VILLE + " Cadrage serré, à hauteur de "
  "cheville, sur une botte d'hiver noire posée sur un trottoir glacé, avec des "
  "crampons de métal attachés par-dessus la semelle au moyen d'un élastique "
  "de caoutchouc. On ne voit que la botte et le sol. Aucun visage, aucune "
  "marque de fabricant."),
 ('eclaircie-fleuve', 'images', P_EX, FLEUVE + " Le ciel qui s'ouvre en une "
  "trouée lumineuse au-dessus du fleuve après une journée couverte, rayons "
  "obliques sur l'eau grise, nuages sombres tout autour, fin d'après-midi. "
  "Aucune personne, aucune embarcation."),

 # ── Je retiens des mots · les treize photos du banc ───────────────────
 ('veille', 'vocab', P_VOC, VILLE + " Un ciel d'hiver lourd et bas, chargé de "
  "nuages gris foncé qui n'ont pas encore commencé à donner, au-dessus de "
  "toits enneigés vus de loin. Rien ne tombe encore. Aucune personne."),
 ('avertissement', 'vocab', P_VOC, VILLE + " Une tempête déjà commencée : "
  "neige dense et oblique poussée par le vent devant des maisons dont on ne "
  "distingue plus les contours, en fin de journée. Aucune personne, aucun "
  "véhicule au premier plan."),
 ('eclaircie', 'vocab', P_VOC, FLEUVE + " Une bande de ciel bleu qui apparaît "
  "entre deux masses de nuages gris, avec un rayon de soleil qui touche l'eau "
  "en contrebas. Cadrage large et calme. Aucune personne."),
 ('pluie-verglacante', 'vocab', P_VOC, VILLE + " Cadrage serré sur une branche "
  "d'arbre et un fil électrique entièrement gainés d'une couche de glace "
  "transparente et épaisse, gouttes gelées suspendues en dessous, ciel gris en "
  "arrière-plan flou. Aucune personne, aucun dégât spectaculaire."),
 ('poudrerie', 'vocab', P_VOC, NATURE + " De la neige fine soulevée en nappes "
  "par le vent au-dessus d'un champ ouvert bordé d'épinettes, vue au ras du "
  "sol, lumière blanche et plate d'un après-midi d'hiver. Aucune personne, "
  "aucune construction."),
 ('refroidissement-eolien', 'vocab', P_VOC, VILLE + " Une personne vue de dos "
  "et de loin, emmitouflée, capuchon relevé et visage couvert d'un cache-cou, "
  "marchant tête baissée contre un vent d'hiver qui plaque son manteau contre "
  "elle. Le visage n'est pas visible du tout. Aucun texte, aucun logo."),
 ('bordee-de-neige', 'vocab', P_VOC, VILLE + " Un escalier extérieur et une "
  "galerie de bois couverts d'une trentaine de centimètres de neige fraîche et "
  "lisse, tombée pendant la nuit, au petit matin. Aucune trace de pas, aucune "
  "personne."),
 ('crue-printaniere', 'vocab', P_VOC, NATURE + " Une petite rivière sortie de "
  "son lit au printemps : l'eau brune et rapide couvre les berges et le pied "
  "des arbres, restes de neige sale sur les côtés, ciel gris. Vue de la rive, "
  "de loin. Aucune maison, aucune personne."),
 ('degel', 'vocab', P_VOC, VILLE + " Une bordure de trottoir au printemps : "
  "neige grise et poreuse en train de fondre, filet d'eau qui coule le long du "
  "caniveau, asphalte mouillé et découvert par plaques. Cadrage en plongée. "
  "Aucune personne."),
 ('chaleur-extreme', 'vocab', P_VOC, VILLE + " Une rue résidentielle déserte "
  "en plein soleil de midi au cœur de l'été, ombres très courtes sous les "
  "arbres, air qui tremble au-dessus de l'asphalte, ciel blanc et sans nuage. "
  "Aucune personne, aucun véhicule au premier plan."),
 ('indice-uv', 'vocab', P_VOC, FLEUVE + " Le soleil très haut et très blanc "
  "vu à travers des herbes hautes en contre-jour, reflets durs sur l'eau, "
  "aucune ombre profonde nulle part. Ciel entièrement dégagé. Aucune "
  "personne, aucun texte."),
 ('coup-de-chaleur', 'vocab', P_VOC, FLEUVE + " Une gourde d'eau en métal et "
  "un chapeau de toile à large bord posés sur un banc de bois à l'ombre d'un "
  "arbre, un après-midi d'été très lumineux, la promenade écrasée de soleil "
  "en arrière-plan flou. Aucune personne, aucune marque de fabricant."),
 ('crampons', 'vocab', P_VOC, VILLE + " Une paire de crampons à glace pour "
  "bottes posée seule sur une table de bois clair, vue de trois quarts : "
  "sangle de caoutchouc noir et petites pointes de métal, éclairage naturel "
  "doux. Aucun texte, aucune marque, aucune personne."),
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


voulus = set(sys.argv[1:])
GEN.mkdir(parents=True, exist_ok=True)
horodatage = time.strftime('%Y%m%d-%H%M%S')
faits, sautes, echecs, routes = [], [], [], {}

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
        data, route = generer_image(prompt, ratio=RATIO, resolution="1K",
                                    module=MODULE, cible=etiquette)
    except Exception as e:
        echecs.append('%s : %s' % (etiquette, e)); continue

    brut = data
    # La route Google directe rend des JPEG bien plus lourds que fal.ai. À
    # l'écran, l'image d'exercice occupe 223 x 132 px et la photo du banc
    # encore moins : les deux se réduisent, seulement pas au même format.
    try:
        data = reduire(data, *((800, 82) if dossier == 'vocab' else (1200, 85)))
    except Exception as e:
        echecs.append('%s : réduction impossible (%s) — image brute gardée'
                      % (etiquette, e))

    base = '%s_%s-%s_%s' % (MODULE, dossier, nom, horodatage)
    (GEN / (base + '.jpg')).write_bytes(brut)
    (GEN / (base + '.json')).write_text(json.dumps({
        "model": "nano-banana-2 (Gemini 3.1 Flash Image)",
        "prompt": prompt,
        "refs": [],
        "params": {"num_images": 1, "aspect_ratio": RATIO,
                   "resolution": "1K", "output_format": "jpeg"},
        "provider": route,
        "created": time.strftime('%Y-%m-%dT%H:%M:%S+00:00', time.gmtime()),
        "projet": "bibliotheque-francisation",
        "module": MODULE,
        "page": page,
        "destination": "assets/interactive/%s/%s/%s.jpg" % (MODULE, dossier, nom),
    }, ensure_ascii=False, indent=2), encoding='utf-8')
    cible.write_bytes(data)
    faits.append(etiquette)
    routes[route] = routes.get(route, 0) + 1
    print('  ✓ %-26s %6.1f Ko  par %s' % (etiquette, len(data) / 1024, route),
          flush=True)

print()
print('%d produite(s), %d sautée(s), %d échec(s)'
      % (len(faits), len(sautes), len(echecs)))
for route, n in sorted(routes.items()):
    print('   · %-18s %d image(s)' % (route, n))
for e in echecs:
    print('   ✗ ' + e)
