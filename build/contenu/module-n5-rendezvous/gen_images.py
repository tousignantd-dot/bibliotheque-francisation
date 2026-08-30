#!/usr/bin/env python3
"""Génère les 24 images de module-n5-rendezvous via fal.ai (Nano Banana 2).

Deux destinations :
  · `images/` — les huit illustrations de l'exercice `prImg` ;
  · `vocab/`  — les seize photos du banc de vocabulaire, réduites à 800 px.

**Format 3:2 paysage** : la zone de glisser-déposer est un rectangle de
223 x 132 px. Une image carrée y perd le tiers du haut et du bas.

Deux contraintes propres à ce module, plus dures qu'ailleurs :

- **Aucun texte lisible**, comme partout — mais ici les objets sont des cartes,
  des ordonnances et des calendriers, c'est-à-dire du papier écrit. Les
  documents sont donc photographiés de biais ou en faible profondeur de champ,
  les lignes réduites à des traits gris. Un élève ne doit pas lire une fausse
  carte d'assurance maladie approximative sur une photo.
- **Aucun visage, aucun personnel soignant reconnaissable, aucun logo
  d'établissement.** Le sujet est médical : les personnes sont vues de dos, de
  trois quarts arrière ou hors cadrage, et rien n'imite l'identité visuelle
  d'un vrai réseau de santé. Les scènes restent celles d'une clinique de
  quartier ordinaire, jamais d'un bloc opératoire.

Une image à la fois, journal .json adjacent dans ~/Claude/generations, puis
copie vers le module. Relançable : une image déjà présente est sautée.

  python3 build/contenu/module-n5-rendezvous/gen_images.py
  python3 build/contenu/module-n5-rendezvous/gen_images.py salle-attente
"""
import io, json, os, pathlib, sys, time, urllib.request, urllib.error

MODULE = 'module-n5-rendezvous'
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

STYLE = ("Photographie réaliste, format paysage, lumière naturelle, faible "
         "profondeur de champ. Scène québécoise ordinaire et contemporaine, "
         "ni luxueuse ni délabrée, palette sobre. Aucun texte lisible, aucune "
         "écriture, aucun logo, aucune enseigne, aucun filigrane, aucune "
         "personne identifiable.")

DOC = ("Photographie réaliste, format paysage, vue rapprochée d'un document de "
       "papier posé à plat, éclairage doux et rasant, faible profondeur de "
       "champ. Les lignes de texte apparaissent comme des traits gris "
       "entièrement illisibles. Aucun mot déchiffrable, aucun logo, aucun "
       "filigrane, aucune personne.")

ECRAN = ("Photographie réaliste, format paysage, écran de téléphone ou "
         "d'ordinateur vu de trois quarts, éclairage doux, faible profondeur "
         "de champ. Le contenu de l'écran est flou : des rectangles et des "
         "traits gris, aucun mot lisible, aucun logo, aucune couleur de marque "
         "reconnaissable.")

PERS = ("Photographie réaliste, format paysage, scène de la vie quotidienne au "
        "Québec avec une ou deux personnes vues de dos, de trois quarts arrière "
        "ou hors cadrage du visage. Lumière naturelle douce, faible profondeur "
        "de champ. Aucun visage reconnaissable, aucun texte, aucun logo, aucun "
        "filigrane.")

SOIN = ("Photographie réaliste, format paysage, cabinet de médecin de famille "
        "ordinaire et bien rangé, lumière du jour, faible profondeur de champ. "
        "Aucun visage, aucune blouse à insigne, aucun logo d'établissement, "
        "aucun texte lisible. Rien d'inquiétant ni de spectaculaire : ni bloc "
        "opératoire, ni appareil médical impressionnant.")

P_EX1 = "Je découvre · Exercice 3 — Les images du rendez-vous"
P_VOC = "Je retiens des mots — banc de vocabulaire"

# (nom, dossier, page, prompt)
IMAGES = [
 # ── Je découvre · les huit images de `prImg` ──────────────────────────
 ('salle-attente', 'images', P_EX1, PERS + " Une salle d'attente de clinique de quartier : "
  "des rangées de chaises simples, deux personnes assises au fond vues de dos, une plante "
  "près de la fenêtre. Vue d'ensemble, aucune affiche lisible."),
 ('appel-carnet', 'images', P_EX1, PERS + " Une personne assise à une table de cuisine, "
  "téléphone contre l'oreille, un stylo à la main au-dessus d'un carnet ouvert. Vue de "
  "trois quarts arrière, visage hors cadrage."),
 ('carte-main', 'images', P_EX1, DOC + " Une carte de plastique tenue entre deux doigts "
  "au-dessus d'un comptoir clair, en légère plongée. Aucun caractère lisible, aucun visage "
  "sur la carte."),
 ('brassard-tension', 'images', P_EX1, SOIN + " Un brassard de tensiomètre posé autour d'un "
  "avant-bras, tuyau et poire visibles, sur un bureau clair. Cadrage serré sur le bras et "
  "l'appareil, aucun visage, chiffres de l'écran flous."),
 ('prelevement-bras', 'images', P_EX1, SOIN + " Un avant-bras posé sur un accoudoir de "
  "chaise de prélèvement, garrot et petits tubes de plastique alignés à côté sur un "
  "plateau. Cadrage serré, aucun visage, aucune étiquette lisible."),
 ('ordonnance-papier', 'images', P_EX1, DOC + " Une feuille d'ordonnance posée sur un "
  "bureau, un stylo en travers, une signature réduite à un trait indistinct. Aucun mot "
  "déchiffrable."),
 ('calendrier-rendezvous', 'images', P_EX1, STYLE + " Un calendrier mural accroché près "
  "d'une porte de cuisine, une case entourée au crayon rouge et une note collée à côté. "
  "Chiffres et écriture entièrement flous."),
 ('telephone-message', 'images', P_EX1, PERS + " Une personne debout dans un couloir, le "
  "soir, un téléphone tenu près de la bouche comme pour laisser un message. Vue de dos, "
  "lumière basse, écran du téléphone flou."),

 # ── Les seize photos du banc de vocabulaire ───────────────────────────
 ('gmf', 'vocab', P_VOC, STYLE + " La façade d'une petite clinique de quartier au "
  "rez-de-chaussée d'un immeuble, porte vitrée et fenêtres, un banc devant. Aucune "
  "enseigne, aucune inscription lisible."),
 ('carte-assurance-maladie', 'vocab', P_VOC, DOC + " Une carte de plastique unie vert "
  "pâle et blanche, sans logo ni bande magnétique, posée seule sur un comptoir clair, "
  "en légère plongée. Aucun portefeuille, aucune carte bancaire ni autre carte de "
  "plastique à logo dans le cadre. Aucun caractère lisible, aucun visage sur la carte."),
 ('sans-rendez-vous', 'vocab', P_VOC, PERS + " Une file de quelques personnes debout dans "
  "l'entrée d'une clinique, vues de dos, tôt le matin, lumière rasante par la porte "
  "vitrée. Aucune affiche lisible."),
 ('etourdissement', 'vocab', P_VOC, PERS + " Une personne debout près d'un lit défait, une "
  "main appuyée contre le mur, tête baissée, vue de dos dans une chambre le matin. Aucun "
  "visage, atmosphère calme et non dramatique."),
 ('symptome', 'vocab', P_VOC, PERS + " Une personne assise au bord d'un lit, les épaules "
  "basses, une main sur la nuque, vue de trois quarts arrière dans une chambre claire. "
  "Aucun visage."),
 ('disponibilite', 'vocab', P_VOC, ECRAN + " Un agenda affiché à l'écran : une grille de "
  "cases, quelques-unes grisées et d'autres vides. Tout le texte est flou."),
 ('rendez-vous-suivi', 'vocab', P_VOC, DOC + " Une petite carte de rappel de rendez-vous "
  "posée sur une table à côté d'un trousseau de clés, vue en biais depuis le bas, son "
  "bord supérieur sorti du cadre : seules les lignes remplies et la case à cocher sont "
  "visibles, réduites à des traits gris."),
 ('agente-administrative', 'vocab', P_VOC, PERS + " Une personne assise derrière un "
  "comptoir d'accueil, casque téléphonique sur la tête, vue de trois quarts arrière devant "
  "un écran flou. Aucun visage, aucun logo."),
 ('rappel-automatise', 'vocab', P_VOC, ECRAN + " Un téléphone posé sur une table de "
  "cuisine, une notification affichée à l'écran, tout le texte flou et illisible."),
 ('tension-arterielle', 'vocab', P_VOC, SOIN + " Un tensiomètre à brassard posé sur un "
  "bureau, tuyau enroulé à côté, cadrage serré. Aucun chiffre lisible, aucune personne."),
 ('prise-de-sang', 'vocab', P_VOC, SOIN + " Un plateau de prélèvement sur une table : "
  "petits tubes de plastique bouchés de couleurs différentes, garrot souple, compresse. "
  "Cadrage serré, aucune personne, aucune étiquette lisible."),
 ('a-jeun', 'vocab', P_VOC, STYLE + " Une table de cuisine au petit matin avec un seul "
  "verre d'eau posé au centre, une tasse retournée à côté, lumière froide de l'aube. Rien "
  "à manger sur la table."),
 ('ordonnance', 'vocab', P_VOC, DOC + " Une feuille d'ordonnance pliée en deux posée sur "
  "un comptoir, un stylo à côté. Toutes les lignes sont floues et illisibles."),
 ('deplacer-rendez-vous', 'vocab', P_VOC, STYLE + " Un calendrier de bureau où une case est "
  "barrée d'un trait au crayon et une flèche va vers une autre case, plus loin dans la "
  "semaine. Chiffres et écriture entièrement flous."),
 ('frais-absence', 'vocab', P_VOC, DOC + " Un petit relevé de papier posé sur un comptoir "
  "à côté d'un terminal de paiement, en légère plongée. Aucun montant lisible, aucun "
  "logo."),
 ('boite-vocale', 'vocab', P_VOC, STYLE + " Un vieux téléphone à combiné posé sur une "
  "petite table d'entrée, dans la pénombre du soir, une lumière rouge de messagerie qui "
  "clignote. Aucun texte lisible."),
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
