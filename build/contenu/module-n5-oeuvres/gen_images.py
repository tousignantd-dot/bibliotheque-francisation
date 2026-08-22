#!/usr/bin/env python3
"""Les 22 images de module-n5-oeuvres.

Deux destinations :
  · `images/` — les six photos de l'exercice 3 « Ce qu'on trouve à la
    bibliothèque de quartier » ;
  · `vocab/`  — les seize photos du banc de vocabulaire, réduites à 800 px.

**Aucun appel réseau en dur ici.** Le générateur importe `generer_image` de
`build/route_images.py`, qui essaie les routes dans l'ordre du prix mesuré le
21 août 2026 — Google direct, puis fal.ai, puis WaveSpeed —, rend le nom de
celle qui a servi, et inscrit **chaque tentative** au registre des appels de
`~/Claude/generations/journal_appels.py`. Une image régénérée est payée deux
fois : le mur doit le voir.

Une difficulté propre à ce module : la moitié du vocabulaire porte sur des
objets couverts d'écriture — un roman, un album, une planche de bande
dessinée, une bulle. La consigne de style interdit tout texte lisible, et pour
de bonnes raisons : un mot déchiffrable dans une image serait du contenu que
personne n'a écrit. Les prompts demandent donc partout des lignes de texte
floues, des bulles vides et des lettres illisibles — on reconnaît la forme,
jamais les mots. Pour l'onomatopée, seule image où de grosses lettres sont le
sujet, le prompt demande des formes de lettres inventées, sans mot réel.

Relançable : une image déjà présente est sautée. Pour en refaire une, efface
son fichier d'abord.

  python3 build/contenu/module-n5-oeuvres/gen_images.py
  python3 build/contenu/module-n5-oeuvres/gen_images.py bulle
"""
import io, json, pathlib, sys, time

MODULE = 'module-n5-oeuvres'
GEN  = pathlib.Path('/Users/danieltousignant/Claude/generations')
BASE = pathlib.Path('/Users/danieltousignant/Claude/bibliotheque-francisation'
                    '/assets/interactive/' + MODULE)
RATIO = "3:2"

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent.parent))
from route_images import generer_image                       # noqa: E402

P_EX  = "Je découvre · Exercice 3 — Ce qu'on trouve à la bibliothèque de quartier"
P_VOC = "Je retiens des mots — banc de vocabulaire"

# Les trois moules de style. Ils imposent la cohérence visuelle du module et
# interdisent partout texte, logo, filigrane et personne identifiable.
INTERDITS = ("Aucun texte lisible, aucun mot déchiffrable, aucun titre "
             "reconnaissable, aucun logo, aucun filigrane, aucune personne "
             "identifiable, aucun visage reconnaissable. ")
LIEU = ("Photographie réaliste, format paysage, intérieur ordinaire d'une "
        "bibliothèque de quartier au Québec, lumière naturelle douce mêlée "
        "d'éclairage au plafond, palette sobre et chaude, faible profondeur "
        "de champ. " + INTERDITS)
OBJET = ("Photographie réaliste, format paysage, gros plan sur une table de "
         "bois clair, lumière naturelle douce venant d'une fenêtre, faible "
         "profondeur de champ, fond neutre. " + INTERDITS)
PAPIER = ("Photographie réaliste, format paysage, gros plan en plongée sur du "
          "papier imprimé : on distingue des blocs de lignes grises serrées "
          "et parfois une image, mais l'écriture reste floue et parfaitement "
          "illisible. " + INTERDITS)

# (nom, dossier, page, prompt)
IMAGES = [
 # ── Les six images de l'exercice 3 ────────────────────────────────────
 ('affiche-club', 'images', P_EX,
  LIEU + "Une feuille de papier blanc scotchée sur la porte vitrée d'une "
         "petite salle, vue légèrement de biais. On voit trois lignes de "
         "caractères flous et un liséré de couleur, rien de déchiffrable. "
         "Derrière la vitre, une salle sombre et vide."),
 ('salle-du-fond', 'images', P_EX,
  LIEU + "Une dizaine de chaises de bois placées en cercle dans une petite "
         "salle aux murs beiges, une table basse au centre avec une carafe "
         "d'eau et des verres, personne dans la pièce. Fin de journée, "
         "lumière basse par une fenêtre à droite."),
 ('rayon-romans', 'images', P_EX,
  LIEU + "Un rayon de bibliothèque vu de face, rempli de livres serrés du "
         "plancher au plafond, dos de toutes les couleurs, étiquettes "
         "blanches en bas de chaque dos, aucun titre déchiffrable. Le "
         "plancher de linoléum au premier plan, flou."),
 ('comptoir-coups-de-coeur', 'images', P_EX,
  LIEU + "Un comptoir de bois clair sur lequel une dizaine de livres sont "
         "posés debout, appuyés sur de petits supports transparents. Devant "
         "chaque livre, un carton blanc plié, écrit à la main, dont les "
         "lignes d'écriture restent floues. Personne au comptoir."),
 ('planche-ouverte', 'images', P_EX,
  PAPIER + "Un grand livre ouvert à plat, dont la page de droite est "
           "découpée en neuf carrés dessinés de tailles inégales, séparés "
           "par des lignes blanches. À l'intérieur des carrés, des dessins "
           "au trait en couleurs douces et deux formes ovales blanches "
           "vides, sans une seule lettre à l'intérieur."),
 ('ecoute-au-casque', 'images', P_EX,
  LIEU + "Une femme assise de dos près d'une grande fenêtre, un casque "
         "d'écoute noir sur les oreilles, un livre fermé sur les genoux. "
         "Vue de trois quarts arrière, visage hors cadre, contre-jour doux."),

 # ── Les seize photos du banc de vocabulaire ───────────────────────────
 ('oeuvre', 'vocab', P_VOC,
  OBJET + "Quatre objets posés côte à côte : un livre relié fermé, un "
          "boîtier de disque, un grand album cartonné et une paire "
          "d'écouteurs enroulés. Couvertures unies, sans un seul mot."),
 ('roman', 'vocab', P_VOC,
  OBJET + "Un livre épais ouvert au deux tiers, posé à plat, les pages "
          "couvertes de lignes de texte grises et floues, un signet de "
          "tissu rouge qui dépasse. Couverture souple unie."),
 ('serie', 'vocab', P_VOC,
  OBJET + "Un écran de téléviseur plat éteint dans un salon ordinaire, "
          "reflet doux d'une fenêtre dessus, une télécommande et une tasse "
          "posées sur la table basse au premier plan."),
 ('coup-de-coeur', 'vocab', P_VOC,
  LIEU + "Gros plan sur un livre debout au bout d'un rayon, appuyé sur un "
         "petit support, avec devant lui un carton blanc plié couvert d'une "
         "écriture manuscrite floue et d'un petit cœur dessiné au crayon."),
 ('intrigue', 'vocab', P_VOC,
  OBJET + "Une boîte de carton ancienne ouverte sur une table, remplie de "
          "vieilles enveloppes attachées par un ruban, une enveloppe posée "
          "à côté, adresse manuscrite complètement floue."),
 ('personnage', 'vocab', P_VOC,
  OBJET + "Un dessin au trait noir sur papier blanc représentant une "
          "silhouette de femme de dos, manteau et foulard, sans aucun "
          "détail de visage. Le papier est posé de biais sur la table, un "
          "crayon à côté."),
 ('denouement', 'vocab', P_VOC,
  OBJET + "La toute dernière page d'un livre ouvert : quelques lignes de "
          "texte flou en haut, puis un grand blanc, et le doigt d'une main "
          "qui tient le bord de la page. Lumière rasante."),
 ('extrait', 'vocab', P_VOC,
  PAPIER + "Deux pages d'un livre ouvert dont un seul paragraphe, au "
           "milieu de la page de droite, est net et surligné en jaune "
           "pâle, tout le reste étant flou et illisible."),
 ('case', 'vocab', P_VOC,
  PAPIER + "Gros plan sur un seul carré dessiné d'une page de bande "
           "dessinée, entouré d'un trait noir épais et d'une marge blanche "
           "large. À l'intérieur, un dessin au trait d'une porte de bois "
           "fermée, en couleurs douces, sans aucune lettre."),
 ('bulle', 'vocab', P_VOC,
  PAPIER + "Gros plan sur une forme ovale blanche cernée d'un trait noir, "
           "avec une petite pointe triangulaire qui descend vers le bas, "
           "posée sur un dessin au trait en couleurs douces. L'intérieur de "
           "l'ovale est entièrement vide, sans une seule lettre."),
 ('planche', 'vocab', P_VOC,
  PAPIER + "Une page complète de bande dessinée vue de face, découpée en "
           "neuf carrés dessinés de tailles inégales séparés par des lignes "
           "blanches, dessins au trait en couleurs douces, toutes les "
           "formes ovales de dialogue laissées vides."),
 ('onomatopee', 'vocab', P_VOC,
  PAPIER + "Gros plan sur un carré dessiné de bande dessinée occupé au "
           "tiers par de grosses formes de lettres inventées, jaunes cernées "
           "de noir, en biais, qui ne composent aucun mot d'aucune langue. "
           "Derrière, un dessin au trait très simple."),
 ('album', 'vocab', P_VOC,
  OBJET + "Trois grands livres cartonnés à couverture unie posés en pile "
          "légèrement décalée, format à l'italienne, dos toilé, aucun titre "
          "ni aucun chiffre visible sur les couvertures."),
 ('emouvant', 'vocab', P_VOC,
  OBJET + "Un livre fermé posé sur une couverture de laine, à côté d'une "
          "tasse vide et d'un mouchoir de papier froissé, lumière chaude "
          "de fin de soirée venant d'une lampe hors cadre."),
 ('previsible', 'vocab', P_VOC,
  OBJET + "Un livre ouvert dont les dernières pages sont soulevées d'une "
          "main, laissant voir qu'il ne reste que quelques feuillets, une "
          "horloge murale floue en arrière-plan."),
 ('recommander', 'vocab', P_VOC,
  LIEU + "Deux personnes vues de dos au comptoir d'une bibliothèque, l'une "
         "tendant un livre à l'autre par-dessus le comptoir, visages hors "
         "cadre, rayons flous derrière."),
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
    print('  ✓ %-24s %6.1f Ko  par %s' % (etiquette, len(data) / 1024, route),
          flush=True)

print()
print('%d produite(s), %d sautée(s), %d échec(s)'
      % (len(faits), len(sautes), len(echecs)))
for route, n in sorted(routes.items()):
    print('   · %-18s %d image(s)' % (route, n))
for e in echecs:
    print('   ✗ ' + e)
