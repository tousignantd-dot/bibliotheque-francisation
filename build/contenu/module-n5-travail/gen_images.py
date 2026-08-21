#!/usr/bin/env python3
"""Génère les 20 images de module-n5-travail via fal.ai (Nano Banana 2).

Deux destinations :
  · `images/` — les six illustrations de l'exercice `prImg` ;
  · `vocab/`  — les quatorze photos du banc de vocabulaire, réduites à 800 px.

**Format 3:2 paysage** : la zone de glisser-déposer est un rectangle de
223 x 132 px. Une image carrée y perd le tiers du haut et du bas.

Trois contraintes propres à ce module :

- **Aucun texte lisible**, et c'est plus dur ici qu'ailleurs : le module parle
  de formulaires, de modes d'emploi, de courriels et d'écrans de photocopieur.
  Tout document est donc photographié de biais ou en faible profondeur de
  champ, et ses lignes se réduisent à des traits gris. Un formulaire dont on
  lirait les cases donnerait la réponse d'un exercice, en plus d'inventer un
  document administratif qui n'existe pas.
- **Aucun logo, aucune marque d'appareil.** Les photocopieurs, les téléphones
  de bureau et les écrans sont vus de biais, sans plaque de marque lisible.
- **Aucun visage.** Les personnes sont vues de dos, de trois quarts arrière ou
  hors cadrage. La plupart des scènes sont simplement vides : un bureau, un
  corridor, un babillard.

Une image à la fois, journal .json adjacent dans ~/Claude/generations, puis
copie vers le module. Relançable : une image déjà présente est sautée.

  python3 build/contenu/module-n5-travail/gen_images.py
  python3 build/contenu/module-n5-travail/gen_images.py babillard
"""
import io, json, os, pathlib, sys, time, urllib.request, urllib.error

MODULE = 'module-n5-travail'
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

BUREAU = ("Photographie réaliste, format paysage, bureau ou local administratif "
          "ordinaire d'un organisme communautaire québécois, mobilier simple et un "
          "peu usé, lumière naturelle de fenêtre, faible profondeur de champ. "
          "Aucun texte lisible, aucun logo, aucune marque d'appareil, aucune "
          "personne identifiable.")

PAPIER = ("Photographie réaliste, format paysage, cadrage serré et oblique sur un "
          "document de papier posé sur un bureau, faible profondeur de champ. Les "
          "lignes du document sont réduites à des traits gris : aucun mot, aucun "
          "chiffre, aucune case remplie n'est lisible. Aucun logo, aucun en-tête "
          "reconnaissable.")

ECRAN = ("Photographie réaliste, format paysage, écran vu de trois quarts, "
         "éclairage doux, faible profondeur de champ. Le contenu de l'écran est "
         "flou : des rectangles et des traits gris, aucun mot lisible, aucun logo, "
         "aucune couleur de marque reconnaissable.")

PERS = ("Photographie réaliste, format paysage, scène de travail de bureau "
        "ordinaire au Québec avec une ou deux personnes vues de dos, de trois "
        "quarts arrière ou hors cadrage du visage. Lumière naturelle douce, faible "
        "profondeur de champ. Aucun visage reconnaissable, aucun texte, aucun "
        "logo, aucun filigrane.")

APPAREIL = ("Photographie réaliste, format paysage, appareil de bureau ordinaire "
            "photographié de trois quarts dans un corridor ou un local de travail, "
            "éclairage neutre, faible profondeur de champ. Aucune plaque de marque "
            "lisible, aucun logo, aucun texte sur l'écran de commande, aucune "
            "personne.")

P_EX1 = "Je découvre · Exercice 3 — Les objets du poste"
P_VOC = "Je retiens des mots — banc de vocabulaire"

# (nom, dossier, page, prompt)
IMAGES = [
 # ── Je découvre · les six images de `prImg` ───────────────────────────
 ('bureau-accueil', 'images', P_EX1, BUREAU + " Un comptoir d'accueil vide dans un petit "
  "organisme : un classeur de métal derrière, une plante verte sur le coin du comptoir, "
  "une chaise. Aucune affiche lisible, aucune personne."),
 ('telephone-poste', 'images', P_EX1, BUREAU + " Cadrage serré sur un téléphone de bureau "
  "noir posé près d'un bloc-notes, un petit voyant rouge allumé sur l'appareil. Aucune "
  "marque lisible, aucun chiffre lisible sur le clavier."),
 ('babillard', 'images', P_EX1, BUREAU + " Un babillard de liège fixé au mur d'un corridor, "
  "couvert de feuilles de papier retenues par des punaises de couleur. Toutes les feuilles "
  "sont vues de biais et floues : aucun mot n'est lisible."),
 ('photocopieur-corridor', 'images', P_EX1, APPAREIL + " Un grand photocopieur multifonction "
  "gris au bout d'un corridor éclairé, vu de trois quarts, avec ses tiroirs fermés et son "
  "chargeur sur le dessus."),
 ('formulaire-rempli', 'images', P_EX1, PAPIER + " Une feuille à cases posée sur un bureau, "
  "un stylo bleu à côté, une signature manuscrite illisible en bas de la page."),
 ('ecran-courriel', 'images', P_EX1, ECRAN + " Un écran d'ordinateur de bureau vu de trois "
  "quarts qui affiche une liste de messages : des rangées grises et des rectangles flous, "
  "aucun mot lisible."),

 # ── Je retiens des mots · les quatorze photos du banc ─────────────────
 ('accueil', 'vocab', P_VOC, BUREAU + " Le comptoir d'accueil d'un petit organisme "
  "communautaire, vu de côté : un comptoir de bois clair, une chaise pour les visiteurs, "
  "une porte vitrée derrière. Aucune personne, aucune affiche lisible."),
 ('tache', 'vocab', P_VOC, PAPIER + " Une liste manuscrite sur un bloc-notes posé à côté "
  "d'une tasse de café, avec des cases à cocher en marge. Les mots de la liste sont des "
  "traits gris, entièrement illisibles."),
 ('directives', 'vocab', P_VOC, PAPIER + " Une feuille plastifiée fixée au mur à côté d'un "
  "appareil de bureau, vue de biais, avec des petits schémas et des lignes. Aucun mot "
  "lisible."),
 ('registre', 'vocab', P_VOC, PAPIER + " Un grand cahier ouvert sur un bureau, avec des "
  "colonnes et des rangées tracées, une règle et un stylo posés dessus. Aucun chiffre ni "
  "mot lisible."),
 ('boite-vocale', 'vocab', P_VOC, BUREAU + " Cadrage serré et oblique sur un téléphone de "
  "bureau dont un voyant de message clignote en rouge, dans un bureau vide le soir. Aucune "
  "marque, aucun texte."),
 ('message-accueil', 'vocab', P_VOC, PERS + " Une personne assise à un bureau, vue de dos, "
  "un combiné téléphonique à l'oreille et une feuille manuscrite devant elle. Aucun visage, "
  "aucun mot lisible sur la feuille."),
 ('abreviation', 'vocab', P_VOC, PAPIER + " Cadrage très serré sur un feuillet autocollant "
  "jaune couvert de courtes notes manuscrites, collé sur le bord d'un écran. Les notes sont "
  "floues et illisibles."),
 ('photocopieur', 'vocab', P_VOC, APPAREIL + " Un photocopieur multifonction gris, couvercle "
  "relevé, vitre visible, vu de trois quarts dans un local de travail."),
 ('mode-emploi', 'vocab', P_VOC, PAPIER + " Un livret épais ouvert à plat sur une tablette, "
  "à côté d'un appareil de bureau, montrant des schémas techniques et des colonnes de "
  "texte entièrement flou."),
 ('bac-papier', 'vocab', P_VOC, APPAREIL + " Le tiroir inférieur d'un photocopieur ouvert, "
  "rempli d'une pile de feuilles blanches bien alignées, cadrage serré en plongée."),
 ('bourrage', 'vocab', P_VOC, APPAREIL + " La porte latérale d'un photocopieur ouverte, "
  "montrant des rouleaux et une feuille de papier froissée coincée entre eux, cadrage "
  "serré. Aucune main, aucune personne."),
 ('formulaire', 'vocab', P_VOC, PAPIER + " Une feuille à cases vierge posée sur un bureau "
  "de bois, un stylo à bille noir en travers. Aucune case remplie, aucun mot lisible."),
 ('paie', 'vocab', P_VOC, PAPIER + " Un relevé de paie plié en deux sur une table de "
  "cuisine, vu de biais, montrant des colonnes de chiffres entièrement floues."),
 ('reponse-auto', 'vocab', P_VOC, ECRAN + " Un écran d'ordinateur portable vu de trois "
  "quarts affichant une courte fenêtre de message de quelques lignes grises, dans un "
  "bureau vide. Aucun mot lisible."),
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
