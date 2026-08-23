#!/usr/bin/env python3
"""Les 13 images de module-n7-publicite — « Ce que la publicité ne dit pas ».

Deux destinations :
  · `images/` — les six photos de l'exercice 3 « Où la publicité vous rejoint »
    (1200 px, qualité 85) ;
  · `vocab/`  — les sept photos illustrables du banc de vocabulaire (800 px,
    qualité 82).

**La difficulté de ce module, et la façon dont elle est résolue.** La situation
appelle des images qui portent du texte : une publicité *est* du texte. Or la
règle 1 des images de la vague 7 l'interdit, et pour une raison qui ne se
négocie pas — le modèle écrit du charabia, et l'élève de niveau 7 le lit. La
sortie n'est pas de contourner la règle, c'est de **déplacer le texte** : tout
le texte publicitaire du module se compose en HTML dans les exercices (deux
exercices de type `texte`, quatre bandeaux de savoir, deux capsules
transcrites), où il est correct et relisible. Les images, elles, ne montrent
jamais l'annonce : elles montrent la **scène autour**. L'abribus vu du trottoir
d'en face, la boîte aux lettres qui déborde, le téléviseur allumé dans un salon
vide, la console du studio, la structure du panneau vue de l'arrière.

D'où la constante `SANS_MOT`, présente sur **toutes** les images sans exception,
et trois cadrages choisis pour mettre l'inscription hors champ plutôt que pour
l'interdire — la leçon de `module-n4-etablissement` : sur un objet dont le
modèle *sait* qu'il porte des inscriptions, la négation ne tient pas.

· `panneau-autoroute` est vu **de l'arrière** : on ne voit que la structure
  d'acier, l'échelle de service et les projecteurs. La face est hors champ.
· `abribus-soir` et `abribus` montrent le caisson **par la tranche** ou de
  très loin : il ne reste qu'un rectangle de lumière uniforme.
· `vitrine-rue` et `affichage` sont photographiés **de loin et sous la pluie
  ou à contre-jour** : les enseignes sont des aplats de couleur réfléchis.

Chaque prompt d'image d'exercice est écrit **à partir de la phrase de sa
rangée `ok`**, recopiée en commentaire juste au-dessus. C'est la règle 4, la
plus fréquemment enfreinte, et la seule qui ne se voie pas sans mettre la
phrase à côté de la photo (`node build/contexte_images.js module-n7-publicite`).

Douze des dix-neuf cartes du banc n'ont pas d'image, et c'est voulu : « un
message implicite », « la mention légale », « un engagement », « une
commandite » — non, celle-là s'illustre par son décor de tournage —, « un
astérisque », « le prix tout inclus » sont des idées ou des signes
typographiques. Une image inventée pour elles ferait plus de mal que de bien.

Aucun appel réseau en dur : le module importe `build/route_images.py`, qui
essaie Google en direct, puis fal.ai, puis WaveSpeed, et inscrit chaque
tentative au registre d'appels de `~/Claude/generations/journal_appels.py`.

Relançable : une image déjà présente est sautée. Pour en refaire une, effacer
son fichier d'abord — et **corriger le prompt ici**, pas seulement le fichier.

  python3 build/contenu/module-n7-publicite/gen_images.py
  python3 build/contenu/module-n7-publicite/gen_images.py abribus-soir circulaire
"""
import io
import json
import pathlib
import sys
import time

MODULE = 'module-n7-publicite'
GEN = pathlib.Path.home() / 'Claude' / 'generations'
# Relatif au fichier, jamais absolu : un agent qui travaille dans un worktree
# doit voir ses images arriver dans SON arborescence, pas dans le dépôt
# principal.
BASE = (pathlib.Path(__file__).resolve().parents[3]
        / 'assets' / 'interactive' / MODULE)
RATIO = "3:2"

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from route_images import generer_image                       # noqa: E402

P_EX = "Je découvre · Exercice 3 — Où la publicité vous rejoint"
P_VOC = "Je retiens des mots — banc de vocabulaire"

# Trois décors, repris tels quels d'un prompt à l'autre pour que les treize
# images se ressemblent. Le module est urbain, hivernal et ordinaire : rue de
# quartier, escalier extérieur, salon de logement loué. Ni vitrine de centre
# commercial lumineux, ni bureau de catalogue.
S_RUE = ("Photographie réaliste, format paysage, rue ordinaire d'une ville "
         "moyenne du Québec en hiver : neige tassée en bordure, brique rouge, "
         "escaliers extérieurs en métal, fils électriques, ciel bas. Lumière "
         "naturelle basse, palette sobre et froide. Aucune personne "
         "identifiable, aucun visage reconnaissable. ")
S_INT = ("Photographie réaliste, format paysage, intérieur ordinaire au "
         "Québec : logement loué ou petit local de travail, mobilier usé mais "
         "propre, éclairage chaud d'une seule source. Faible profondeur de "
         "champ, palette sobre. Aucune personne dans le cadre. ")
S_OBJET = ("Photographie réaliste, format paysage, gros plan, lumière "
           "naturelle douce, faible profondeur de champ, arrière-plan neutre "
           "et flou. Objet du quotidien, un peu usé, jamais neuf ni "
           "publicitaire. Aucune main, aucun doigt, aucune personne dans le "
           "cadre. ")

# Posée sur TOUTES les images de ce module sans exception : le sujet est la
# publicité, donc chaque scène risque de porter une enseigne, une affiche ou
# un écran. Le texte du module vit dans le HTML, jamais dans l'image.
SANS_MOT = (" Absolument aucun texte, aucune lettre, aucun mot, aucun chiffre, "
            "aucun logo, aucune enseigne lisible, aucun slogan, aucune "
            "étiquette nulle part dans l'image : toute surface qui porterait "
            "normalement une inscription est un aplat de couleur uni ou une "
            "zone floue. Aucun mot d'anglais nulle part.")

# (nom, dossier, page, prompt)
IMAGES = [
 # ── Les six images de l'exercice de glisser-déposer ───────────────────
 # Chaque prompt est écrit à partir de la phrase de sa rangée `ok`, recopiée
 # ci-dessus en commentaire. C'est la règle 4 de la vague 7.

 # « Un abribus éclairé au bord d'une rue enneigée, un soir d'hiver, vu du
 #   trottoir d'en face. »
 ('abribus-soir', 'images', P_EX, S_RUE +
  "Un abribus vitré éclairé de l'intérieur, au bord d'une rue enneigée, "
  "photographié le soir depuis le trottoir d'en face, à une trentaine de "
  "mètres. Le banc est vide. Le caisson lumineux du côté est vu **par la "
  "tranche, presque de profil** : il ne se lit que comme un rectangle de "
  "lumière blanche parfaitement uniforme, sans image et sans caractère. "
  "Traces de pneus dans la neige fondante, lampadaire orangé au-dessus." +
  SANS_MOT),

 # « Une boîte aux lettres de métal si pleine de papier que le couvercle ne
 #   ferme plus. »
 # Refaite une fois : la première version, décrite sans ancrage de lieu, est
 # sortie européenne — crépi de pierre écaillé, porte de bois ancienne, boîte
 # à couvercle bombé. C'est la règle 3, et elle ne se répare pas en ajoutant
 # « au Québec » : il faut nommer les objets du décor. D'où le perron de
 # béton, le revêtement de vinyle et le bloc de boîtes postales communautaires
 # devenu, plus simplement, une boîte à courrier de galerie.
 ('boite-aux-lettres', 'images', P_EX, S_OBJET +
  "Une boîte à courrier rectangulaire en métal peint, vissée sur le "
  "**revêtement de vinyle beige** d'un duplex québécois, juste à côté d'une "
  "porte d'entrée blanche à moustiquaire. Elle est si pleine de papier "
  "journal en couleurs que le couvercle reste entrouvert et qu'une liasse "
  "dépasse et se gondole. Une rampe de métal noir et une marche de béton "
  "enneigée dans le coin du cadre. Le papier est **entièrement hors du plan "
  "de netteté** : on ne distingue que des blocs de couleur flous. Mise au "
  "point sur la charnière du couvercle." + SANS_MOT),

 # « Un téléviseur allumé dans un salon vide, en fin de soirée, personne dans
 #   le fauteuil. »
 ('televiseur-salon', 'images', P_EX, S_INT +
  "Un téléviseur à écran plat allumé dans un salon vide, en fin de soirée. "
  "L'écran ne montre qu'une **surface claire uniforme, légèrement bleutée, "
  "sans aucune image et sans aucun caractère**, et sa lueur éclaire un "
  "fauteuil inoccupé et un tapis. Vue de trois quarts arrière depuis le "
  "corridor, personne dans la pièce." + SANS_MOT),

 # « La console d'un petit studio de radio : le micro suspendu, les curseurs,
 #   la chaise vide. »
 ('console-radio', 'images', P_EX, S_INT +
  "L'intérieur d'un petit studio de radio communautaire : une console de "
  "mixage à curseurs vue en légère plongée, un microphone suspendu à un bras "
  "articulé, un casque posé sur la table, une chaise pivotante vide. Mur de "
  "mousse acoustique gris derrière. Les bandes d'étiquettes de la console "
  "sont **hors du plan de netteté** et ne montrent que des traits gris. Aucune "
  "personne." + SANS_MOT),

 # « La structure d'acier d'un grand panneau au bord de l'autoroute, vue de
 #   l'arrière. »
 ('panneau-autoroute', 'images', P_EX, S_RUE +
  "Un grand panneau d'affichage au bord d'une autoroute, photographié "
  "**strictement de l'arrière**, en contre-plongée : on ne voit que le "
  "treillis d'acier galvanisé, l'échelle de service, la passerelle et la "
  "rampe de projecteurs éteints. La face avant est entièrement hors champ. "
  "Autour, un talus enneigé et une rangée d'épinettes, ciel gris de fin "
  "d'après-midi." + SANS_MOT),

 # « La devanture éclairée d'un commerce de quartier, vue de la rue, un soir
 #   de pluie. »
 ('vitrine-rue', 'images', P_EX, S_RUE +
  "La devanture éclairée d'un petit commerce de quartier, photographiée "
  "depuis le milieu de la rue un soir de pluie, à une vingtaine de mètres. "
  "L'asphalte mouillé renvoie la lumière. La vitrine et l'enseigne au-dessus "
  "sont **des aplats de couleur brouillés par la pluie et les reflets**, sans "
  "une seule lettre discernable. Un vélo attaché à un poteau au premier plan." +
  SANS_MOT),

 # ── Les sept photos du banc de vocabulaire ────────────────────────────
 ('abribus', 'vocab', P_VOC, S_RUE +
  "Un abribus vitré vu de trois quarts en plein jour d'hiver, banc de métal "
  "vide à l'intérieur, neige poussée contre la paroi. Le panneau latéral est "
  "vu **très obliquement** et n'apparaît que comme une surface claire unie. "
  "Un poteau d'arrêt d'autobus sans aucune inscription à côté." + SANS_MOT),

 ('panneau-reclame', 'vocab', P_VOC, S_RUE +
  "Un grand panneau d'affichage monté sur un mât unique, vu **de très loin et "
  "de trois quarts très oblique**, dépassant d'une rangée d'arbres au bord "
  "d'une route de campagne. À cette distance et sous cet angle, la face n'est "
  "qu'un rectangle clair sans détail. Ciel d'hiver, champ enneigé au premier "
  "plan." + SANS_MOT),

 ('capsule-publicitaire', 'vocab', P_VOC, S_OBJET +
  "Gros plan sur un microphone de studio suspendu à un bras articulé, avec "
  "son filtre anti-pop rond, devant un panneau de mousse acoustique gris "
  "flou. Un casque d'écoute noir repose sur le bord d'une table en dessous. "
  "Aucune personne, aucune inscription sur le microphone." + SANS_MOT),

 ('circulaire', 'vocab', P_VOC, S_OBJET +
  "Une liasse de papier journal en couleurs, pliée en deux et gondolée par "
  "l'humidité, posée sur la marche de béton d'un escalier extérieur "
  "québécois, à côté d'une rampe de métal noir. Le papier est **entièrement "
  "hors du plan de netteté** : des blocs de couleur, aucune ligne discernable. "
  "Mise au point sur la marche." + SANS_MOT),

 # Refaite une fois : « une feuille pliée posée à plat » a donné une carte
 # routière dépliée, fanée et pliée en accordéon — un objet qui n'a rien du
 # dépliant commercial que l'énoncé décrit (« la feuille pliée en deux ou en
 # trois qu'un commerce remet en main propre »). C'est la règle 4, et elle se
 # répare en donnant à l'objet sa POSTURE : un dépliant se tient debout sur
 # ses plis, papier glacé et neuf, pas étalé comme une carte.
 ('depliant', 'vocab', P_VOC, S_OBJET +
  "Un dépliant publicitaire de papier glacé **plié en trois et posé debout "
  "sur ses plis**, en accordéon, sur une table de cuisine en bois clair, vu "
  "de face à hauteur de table. Papier neuf et brillant, angles vifs. Les "
  "trois volets ne montrent que des **aplats de couleur vive** et de très "
  "fines lignes grises floues, aucune lettre, aucune image reconnaissable. "
  "Une tasse de café hors du plan de netteté derrière." + SANS_MOT),

 ('commandite', 'vocab', P_VOC, S_INT +
  "Un coin de salon aménagé pour filmer : un anneau lumineux allumé sur son "
  "pied, un téléphone monté sur un petit trépied et vu de dos, une boîte de "
  "carton ouverte avec du papier de soie qui déborde, un objet neuf encore "
  "à moitié emballé posé sur la table basse. Personne dans le cadre, aucune "
  "inscription sur la boîte." + SANS_MOT),

 ('affichage', 'vocab', P_VOC, S_RUE +
  "Une rangée de trois commerces sur une rue commerciale de quartier, "
  "photographiée **de l'autre côté de la rue en fin d'après-midi, à contre-"
  "jour**. Les enseignes au-dessus des portes ne sont que des bandes de "
  "couleur unies, sans une seule lettre. Auvents de toile, escalier extérieur "
  "en colimaçon à l'étage, bancs de neige le long du trottoir." + SANS_MOT),
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
