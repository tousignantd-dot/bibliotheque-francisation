#!/usr/bin/env python3
"""Les 17 images de module-n4-etablissement — « Prévenir le centre ».

Deux destinations :
  · `images/` — les six photos de l'exercice 3 « Ce qu'on voit un matin de
    semaine » (1200 px, qualité 85) ;
  · `vocab/`  — les onze photos illustrables du banc de vocabulaire (800 px,
    qualité 82).

**Aucun appel réseau en dur ici.** Le module importe `build/route_images.py`,
qui essaie les routes dans l'ordre du prix mesuré le 21 août 2026 — Google
direct, puis fal.ai, puis WaveSpeed — et rend le nom de celle qui a servi.
C'est aussi lui qui inscrit chaque tentative, réussie ou non, au registre
d'appels de `~/Claude/generations/journal_appels.py` : le mur compte des
appels, pas des fichiers présents.

**Cinq des seize cartes du banc n'ont pas d'image, et c'est voulu.** « Le
signal sonore », « les coordonnées », « un abandon », « un empêchement » et
« un motif » ne se photographient pas : ce sont des idées, pas des
objets. Une image inventée pour elles ferait plus de mal que de bien — un
téléphone de plus, indistinct des quatre autres. Leur champ `img` est vide dans
`fccards.js`, et `node build/coherence.js` ne le compte pas comme un écart.

**La difficulté propre à ce module : quatre photos de téléphone sur
dix-sept.** Un clavier, un répondeur, un poste de bureau, un cellulaire posé
sur une table — quatre objets voisins qui risquent de se ressembler. Les
prompts les séparent délibérément par le cadrage : le clavier en gros plan de
dessus, le répondeur posé sur une étagère et vu de côté, le poste de bureau vu
de trois quarts sur un bureau encombré, le cellulaire à plat sur une table de
cuisine. La cinquième, « la ligne », montre volontairement autre chose : un
fil téléphonique et une prise murale.

Deuxième difficulté : le module se passe dans un établissement plein de monde
et ne doit montrer personne d'identifiable. Toutes les scènes avec présence
humaine la cadrent de dos, de trois quarts arrière, ou aux mains seules.

Relançable : une image déjà présente est sautée. Pour en refaire une, effacer
son fichier d'abord.

  python3 build/contenu/module-n4-etablissement/gen_images.py
  python3 build/contenu/module-n4-etablissement/gen_images.py clavier note
"""
import io
import json
import pathlib
import sys
import time

MODULE = 'module-n4-etablissement'
GEN = pathlib.Path('/Users/danieltousignant/Claude/generations')
BASE = pathlib.Path('/Users/danieltousignant/Claude/bibliotheque-francisation'
                    '/assets/interactive/' + MODULE)
RATIO = "3:2"

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent.parent))
from route_images import generer_image                       # noqa: E402

P_EX = "Je découvre · Exercice 3 — Ce qu'on voit un matin de semaine"
P_VOC = "Je retiens des mots — banc de vocabulaire"

# Quatre décors, repris tels quels d'un prompt à l'autre pour que les
# dix-sept
# images se ressemblent. Le module est hivernal, matinal et institutionnel :
# ni bureau d'entreprise lumineux, ni maison de catalogue.
S_LIEU = ("Photographie réaliste, format paysage, intérieur d'un centre "
          "d'éducation des adultes ordinaire au Québec : murs pâles, "
          "plancher de tuiles, éclairage fluorescent doux, mobilier usé mais "
          "propre. Palette sobre, aucune scène spectaculaire. Aucun texte "
          "lisible, aucun mot déchiffrable, aucun logo, aucun filigrane, "
          "aucune personne identifiable, aucun visage reconnaissable. ")
S_OBJET = ("Photographie réaliste, format paysage, gros plan, lumière "
           "naturelle douce, faible profondeur de champ, arrière-plan neutre "
           "et flou. Objet du quotidien, un peu usé, jamais neuf ni "
           "publicitaire. Aucun texte lisible, aucun mot déchiffrable, aucun "
           "chiffre déchiffrable, aucune marque, aucun logo, aucun "
           "filigrane, aucune personne identifiable. ")
S_PAPIER = ("Photographie réaliste, format paysage, lumière naturelle douce, "
            "faible profondeur de champ. Du papier de bureau ordinaire : on "
            "distingue des lignes grises et parfois un titre plus gras, mais "
            "l'écriture reste floue et illisible. Aucun texte lisible, aucun "
            "mot déchiffrable, aucun logo, aucun filigrane, aucune personne "
            "identifiable, aucun visage reconnaissable. ")
S_GENS = ("Photographie réaliste, format paysage, une ou deux personnes vues "
          "de dos, de trois quarts arrière ou hors cadrage du visage, "
          "lumière douce d'un matin d'hiver, faible profondeur de champ. "
          "Aucun texte lisible, aucun mot déchiffrable, aucun logo, aucun "
          "filigrane, aucune personne identifiable, aucun visage "
          "reconnaissable. ")

# (nom, dossier, page, prompt)
IMAGES = [
 # ── Les six images de l'exercice 3 ────────────────────────────────────
 ('telephone-comptoir-vide', 'images', P_EX, S_LIEU +
  "Un téléphone de bureau noir posé sur un comptoir d'accueil de stratifié "
  "gris, dans un hall désert avant l'ouverture. Le combiné est sur son socle, "
  "un petit voyant rouge est allumé. Chaise vide derrière le comptoir, "
  "lumière du matin par une porte vitrée au fond."),
 ('appel-cage-escalier', 'images', P_EX, S_GENS +
  "Une personne debout dans une cage d'escalier de béton, vue de dos, un "
  "téléphone cellulaire tenu contre l'oreille droite, un sac d'école à "
  "l'épaule. Marches grises, rampe de métal peinte, lumière froide venant "
  "d'une fenêtre haute."),
 ('reveil-avant-aube', 'images', P_EX, S_OBJET +
  "Un réveille-matin numérique posé sur une table de chevet en bois, dans "
  "une chambre encore sombre, vu de trois quarts arrière et de très près, "
  "de sorte que l'afficheur n'est PAS visible : seule sa lueur rouge se "
  "reflète sur le bois de la table et sur un verre d'eau. Aucun chiffre, "
  "aucun segment lumineux, aucune horloge lisible dans le cadre. Faible "
  "lumière bleutée par la fenêtre."),
 ('enfant-malade-lit', 'images', P_EX, S_GENS +
  "Un jeune enfant couché sous une couette épaisse, vu de dos et de haut, "
  "seuls les cheveux et une épaule dépassent. Un thermomètre et un verre "
  "d'eau posés sur la table de chevet, une petite lampe allumée. Chambre "
  "ordinaire, lumière chaude et basse."),
 ('autobus-neige-arret', 'images', P_EX, S_GENS +
  "Un abribus de banlieue sous une neige épaisse, tôt le matin. Trois "
  "personnes emmitouflées attendent debout, vues de dos, dans des manteaux "
  "d'hiver sombres. Bancs de neige au bord de la rue, ciel gris, lampadaire "
  "encore allumé. Aucun autobus en vue."),
 ('note-remise-main', 'images', P_EX, S_PAPIER +
  "Une feuille blanche pliée en deux qui passe d'une main à une autre, "
  "au-dessus d'un bureau de classe. On voit les deux avant-bras seulement, "
  "aucun visage. Sur la feuille, quelques lignes grises floues et une "
  "signature illisible en bas."),

 # ── Les onze photos illustrables du banc de vocabulaire ───────────────
 ('boite-vocale', 'vocab', P_VOC, S_OBJET +
  "Un téléphone de bureau posé de trois quarts sur un meuble, dont un voyant "
  "rouge clignote sur le côté du socle. L'écran est éteint. Pièce sombre en "
  "arrière-plan, une seule source de lumière chaude."),
 ('repondeur', 'vocab', P_VOC, S_OBJET +
  "Un vieux répondeur téléphonique en plastique beige, posé sur une étagère "
  "de bois et vu de trois quarts arrière, en plongée légère : le dessus et "
  "le flanc de l'appareil occupent le cadre, sa face avant est tournée hors "
  "champ. Deux gros boutons ronds parfaitement lisses, SANS aucune "
  "inscription, sans aucune étiquette, sans aucun mot gravé ni imprimé nulle "
  "part sur le boîtier. Un fil torsadé descend derrière l'étagère."),
 ('clavier', 'vocab', P_VOC, S_OBJET +
  "Gros plan vu du dessus sur le clavier à touches carrées d'un téléphone de "
  "bureau noir posé sur une table. Aucune main, aucun doigt, aucune personne "
  "dans le cadre. Les touches sont nettes mais leurs caractères sont effacés "
  "par l'usage. Le combiné repose sur son socle, en haut du cadre."),
 ('ligne', 'vocab', P_VOC, S_OBJET +
  "Un fil de téléphone gris branché dans une prise murale beige, près d'une "
  "plinthe de bois, dans un couloir. Le fil monte hors du cadre en s'enroulant "
  "légèrement. Mur pâle un peu marqué."),
 ('poste', 'vocab', P_VOC, S_LIEU +
  "Un téléphone de bureau à plusieurs touches de ligne, posé de trois quarts "
  "sur un bureau de travail encombré : un porte-crayons, une pile de "
  "chemises, un écran d'ordinateur éteint derrière. Personne."),
 ('message', 'vocab', P_VOC, S_OBJET +
  "Un téléphone cellulaire posé à plat, écran vers le haut, sur une table de "
  "cuisine en bois. L'écran est allumé mais montre seulement une surface "
  "claire uniforme, sans aucun caractère. Une tasse de café à côté."),
 ('retard', 'vocab', P_VOC, S_GENS +
  "Une personne vue de dos qui marche vite dans un corridor institutionnel, "
  "manteau ouvert et sac à l'épaule, légèrement floue par le mouvement. Une "
  "horloge ronde sans chiffre est accrochée au mur du fond, nette."),
 ('absence', 'vocab', P_VOC, S_LIEU +
  "Une salle de classe d'adultes vue de biais, avec une seule chaise vide et "
  "un pupitre libre au milieu d'une rangée occupée par des cahiers fermés et "
  "des sacs. Personne dans la pièce. Tableau blanc vide au fond."),
 ('note', 'vocab', P_VOC, S_PAPIER +
  "Une petite feuille blanche posée sur un bureau de bois, écrite à la main "
  "en cinq ou six lignes grises floues, avec un espace plus grand en bas et "
  "un trait de signature illisible. Un stylo bleu couché en travers."),
 ('signature', 'vocab', P_VOC, S_PAPIER +
  "Le bas d'une feuille déjà signée, posée sur un bureau de bois : une ligne "
  "horizontale et, juste au-dessus, une boucle d'encre bleue parfaitement "
  "illisible. Un stylo bille bleu couché à côté, capuchon retiré. Aucune "
  "main, aucun bras, aucune personne dans le cadre. Le reste de la page ne "
  "montre que des lignes grises floues."),
 ('copie', 'vocab', P_VOC, S_LIEU +
  "Un photocopieur de bureau ouvert, couvercle relevé, une feuille blanche "
  "posée sur la vitre. Lumière verte de balayage sur le côté. Bac de sortie "
  "avec deux ou trois feuilles empilées. Personne dans le cadre."),
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
