#!/usr/bin/env python3
"""Les 16 images de module-n7-emploi (niveau 7, activité 109).

Deux destinations :
  · `images/` — les six photos de l'exercice 1 de « Je découvre », réduites à
    1200 px qualité 85 ;
  · `vocab/`  — les dix photos du banc de vocabulaire, réduites à 800 px
    qualité 82. Six des seize mots du banc n'ont pas d'image : « un projet »,
    « une évaluation sommaire », « une étape », « la mise en œuvre »,
    « un correctif » et « un accusé de réception » sont des abstractions
    qu'une photo n'éclaire pas — elle ajouterait un contresens plutôt qu'un
    appui.

**Aucun appel réseau en dur ici.** `generer_image` de `build/route_images.py`
essaie les routes dans l'ordre du prix mesuré le 21 août 2026 — Google direct,
puis fal.ai, puis WaveSpeed — rend le nom de celle qui a servi, et inscrit
chaque tentative au registre `~/Claude/generations/journal_appels.py`. Un
fournisseur facture des **appels**, pas des fichiers présents : une image
régénérée est payée chaque fois.

**La racine se déduit de `__file__`**, jamais d'un chemin absolu écrit à la
main : ce fichier vit dans `build/contenu/<slug>/`, donc trois niveaux sous la
racine du dépôt. Un chemin en dur cesse de fonctionner dès qu'on travaille
dans un worktree, et la vague 7 travaille en worktrees.

**Le sujet est l'usine et le papier de bureau** — un ordre du jour, un
échéancier au mur, une soumission, une note de service. Chaque prompt exige
donc que toute ligne de texte soit réduite à un trait gris. Une image où l'on
peut lire un mot — un mot d'anglais surtout — est à refaire.

**Aucune enseigne, aucun logo, aucun visage.** Meubles Rive-du-Nord et
Équipements Sorel sont inventés ; une image qui porterait le nom d'une vraie
entreprise ferait passer une fiction pour un document.

Relançable : une image déjà présente est sautée. Pour en refaire une, effacer
son fichier d'abord.

  python3 build/contenu/module-n7-emploi/gen_images.py
  python3 build/contenu/module-n7-emploi/gen_images.py poste-emballage
  python3 build/contenu/module-n7-emploi/gen_images.py vocab/soumission
"""
import io
import json
import pathlib
import sys
import time

MODULE = 'module-n7-emploi'
RACINE = pathlib.Path(__file__).resolve().parents[3]   # …/bibliotheque-francisation
BUILD = pathlib.Path(__file__).resolve().parents[2]    # …/build
GEN = pathlib.Path.home() / 'Claude' / 'generations'
BASE = RACINE / 'assets' / 'interactive' / MODULE
RATIO = "3:2"

sys.path.insert(0, str(BUILD))
from route_images import generer_image                       # noqa: E402

P_EX = "Je découvre · Exercice 1 — Le vocabulaire de l'usine"
P_VOC = "Je retiens des mots — banc de vocabulaire"

# Le style commun : une PME de fabrication de meubles en banlieue de Montréal,
# soixante-deux personnes, propre mais sans luxe. Rien de spectaculaire.
STYLE = ("Photographie réaliste, format paysage, lumière naturelle, faible "
         "profondeur de champ. Petite usine de fabrication de meubles au "
         "Québec, soixante employés, locaux propres et ordinaires, sans luxe "
         "et sans esthétique publicitaire. Palette sobre, béton, bois clair, "
         "acier peint. Aucun texte lisible, aucun mot déchiffrable, aucun "
         "logo, aucune marque, aucun filigrane, aucune personne "
         "identifiable, aucun visage reconnaissable.")

PERS = ("Photographie réaliste, format paysage, scène ordinaire dans une "
        "petite usine de meubles au Québec, avec une ou deux personnes vues "
        "de dos, de trois quarts arrière ou hors cadrage du visage. Lumière "
        "naturelle douce, faible profondeur de champ. Vêtements de travail "
        "ordinaires. Aucun visage reconnaissable, aucun texte, aucun logo, "
        "aucun filigrane.")

# Presque toutes ces images contiennent du papier imprimé, et un modèle
# d'image écrit volontiers de l'anglais dessus.
SANS_MOTS = (" Strictly no letters, no words, no readable characters anywhere "
             "in the image: every line of text, including any heading, label, "
             "handwriting, form field or sign, must be an abstract grey "
             "stroke. Aucun mot d'anglais nulle part, aucun nom d'entreprise, "
             "aucun nom de ville.")

# (nom, dossier, page, prompt)
IMAGES = [
 # ── Les six images de l'exercice 1 ────────────────────────────────────
 ('poste-emballage', 'images', P_EX, STYLE + " Un poste d'emballage industriel vu de "
  "trois quarts : une table de travail à hauteur de taille, un rouleau de pellicule "
  "d'emballage sur son support, et au sol, juste à côté, une palette de bois portant "
  "une pile de caisses de carton brun vides et pliées. Personne dans le cadre. Le "
  "contraste entre la table haute et la palette au sol doit être visible." + SANS_MOTS),
 ('table-elevatrice', 'images', P_EX, STYLE + " Une table élévatrice à ciseaux "
  "industrielle, plateau d'acier peint, mécanisme en ciseaux bien visible sous le "
  "plateau, portant une palette de bois chargée de caisses de carton. Le plateau est "
  "remonté à hauteur de taille. Atelier en arrière-plan, flou." + SANS_MOTS),
 ('quai-expedition', 'images', P_EX, STYLE + " Un quai d'expédition d'usine vu de "
  "l'extérieur, en fin de journée grise : deux portes de quai relevées, un niveleur de "
  "quai, un camion semi-remorque blanc reculé contre l'une des portes. Cour d'asphalte, "
  "marquage au sol effacé. Aucune inscription sur le camion." + SANS_MOTS),
 ('salle-reunion', 'images', P_EX, STYLE + " Une petite salle de réunion d'usine, vide : "
  "une table rectangulaire en mélamine, huit chaises dépareillées, un tableau blanc au "
  "mur, une cafetière sur un comptoir latéral. Fenêtre donnant sur l'atelier. Le tableau "
  "blanc ne porte que des traits gris." + SANS_MOTS),
 ('babillard', 'images', P_EX, STYLE + " Gros plan sur un babillard de liège dans un "
  "couloir de cafétéria d'usine, couvert de feuilles blanches punaisées en désordre et "
  "légèrement gondolées. Toutes les feuilles ne portent que des traits gris horizontaux, "
  "aucun mot." + SANS_MOTS),
 ('transpalette', 'images', P_EX, STYLE + " Un transpalette manuel à timon, laissé dans "
  "une allée d'entrepôt, fourches engagées sous une palette vide. Rayonnage d'acier "
  "bleu de chaque côté, plancher de béton peint. Personne dans le cadre." + SANS_MOTS),

 # ── Les dix photos du banc de vocabulaire ─────────────────────────────
 ('ordre-du-jour', 'vocab', P_VOC, STYLE + " Gros plan en plongée sur une feuille de "
  "papier blanche posée sur une table de réunion, à côté d'un crayon et d'une tasse. La "
  "feuille présente clairement une structure de liste numérotée, mais chaque ligne n'est "
  "qu'un trait gris." + SANS_MOTS),
 # Reprise du 23 août 2026 : la première version montrait les visages des cinq
 # personnes assises, malgré la consigne. Le cadrage est donc imposé — appareil
 # posé derrière la dernière chaise, à hauteur d'épaule, toutes les têtes vues
 # par l'arrière du crâne.
 ('reunion-production', 'vocab', P_VOC, PERS + " Vue prise depuis le fond d'une salle de "
  "réunion d'usine, appareil placé derrière la dernière chaise, à hauteur d'épaule : on "
  "voit l'arrière de la tête et les épaules de cinq personnes assises autour d'une table, "
  "toutes tournées vers l'avant de la salle. Une sixième personne est debout au fond, "
  "près d'un tableau blanc, également de dos. Aucun visage n'est visible, pas même de "
  "profil. Feuilles et tasses sur la table." + SANS_MOTS),
 ('echeancier', 'vocab', P_VOC, STYLE + " Gros plan sur un grand calendrier mural de "
  "planification, quadrillé, punaisé au mur d'un bureau d'usine, avec des bandes de "
  "couleur horizontales qui traversent plusieurs colonnes. Les cases et les étiquettes ne "
  "portent que des traits gris." + SANS_MOTS),
 ('budget', 'vocab', P_VOC, STYLE + " Gros plan en plongée sur un bureau : une "
  "calculatrice de bureau à rouleau de papier, un tableau imprimé en colonnes de "
  "chiffres flous, un stylo posé en travers. Lumière de fenêtre. Les chiffres sont "
  "illisibles, les en-têtes sont des traits gris." + SANS_MOTS),
 ('manutention', 'vocab', P_VOC, PERS + " Une personne en vêtements de travail, vue de "
  "dos et de côté, penchée en avant pour soulever une caisse de carton posée sur une "
  "palette au sol, dans un atelier. Le dos courbé doit être bien visible. Aucun visage." +
  SANS_MOTS),
 ('poste-travail', 'vocab', P_VOC, STYLE + " Un poste de travail d'atelier vu de face : "
  "établi de bois, tapis antifatigue au sol, bacs de pièces alignés, lampe articulée, "
  "outils suspendus à un panneau perforé. Personne dans le cadre." + SANS_MOTS),
 ('programme-prevention', 'vocab', P_VOC, STYLE + " Gros plan sur un cartable à anneaux "
  "ouvert, posé sur une étagère métallique de bureau d'usine, avec des intercalaires de "
  "couleur qui dépassent. Les pages ne portent que des traits gris et des tableaux "
  "vides." + SANS_MOTS),
 ('soumission', 'vocab', P_VOC, STYLE + " Gros plan en plongée sur une enveloppe ouverte "
  "et deux feuilles imprimées à en-tête, posées sur un bureau de bois, avec un tableau de "
  "prix en colonnes dont les chiffres sont flous et illisibles. Une paire de lunettes "
  "posée à côté." + SANS_MOTS),
 # Reprise du 23 août 2026 : la première version montrait deux collègues dans
 # l'atelier de meubles — c'est-à-dire le thème du module, et non l'énoncé de
 # la carte, qui dit « l'entreprise qui vend à une autre entreprise ce dont
 # elle a besoin ». Le défaut le plus fréquent de la vague. Le lieu change
 # donc : ce n'est plus notre atelier, c'est le stock de quelqu'un d'autre.
 ('fournisseur', 'vocab', P_VOC, STYLE.replace(
  "Petite usine de fabrication de meubles au Québec, soixante employés, locaux "
  "propres et ordinaires, sans luxe et sans esthétique publicitaire.",
  "Entrepôt-magasin d'un distributeur d'équipement industriel au Québec, très haut "
  "plafond, allées larges, tout est neuf et rangé.") +
  " Une allée de distributeur d'équipement industriel : au premier plan, deux tables "
  "élévatrices à ciseaux neuves, encore sur leur palette et partiellement emballées de "
  "pellicule, alignées côte à côte. Derrière, un rayonnage d'acier jaune sur trois "
  "niveaux chargé de caisses de bois neuves et de matériel emballé. Aucune personne "
  "dans le cadre. On doit comprendre qu'il s'agit du stock d'un vendeur, pas d'un "
  "atelier de fabrication : rien de bois travaillé, aucun établi, aucun copeau." +
  SANS_MOTS),
 ('note-service', 'vocab', P_VOC, STYLE + " Gros plan sur une feuille blanche unique "
  "punaisée au centre d'un babillard de liège, un peu de travers. La feuille présente une "
  "structure d'en-tête à quatre lignes courtes puis trois paragraphes, mais chaque ligne "
  "n'est qu'un trait gris." + SANS_MOTS),
]


def reduire(data, largeur, qualite):
    """Les photos du banc sont vues petites : 1024 px n'y sert à rien.

    La hauteur suit le rapport de l'image reçue au lieu d'être forcée à un
    carré — c'est tout l'objet du passage au 3:2.
    """
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
    print('  ✓ %-28s %6.1f Ko  par %s' % (etiquette, len(data) / 1024, route),
          flush=True)

print()
print('%d produite(s), %d sautée(s), %d échec(s)'
      % (len(faits), len(sautes), len(echecs)))
for route, n in sorted(routes.items()):
    print('   · %-18s %d image(s)' % (route, n))
for e in echecs:
    print('   ✗ ' + e)
