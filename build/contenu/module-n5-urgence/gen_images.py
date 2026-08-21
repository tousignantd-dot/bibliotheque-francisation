#!/usr/bin/env python3
"""Génère les 19 images de module-n5-urgence via fal.ai (Nano Banana 2).

Deux destinations :
  · `images/` — les six illustrations de l'exercice `prImg` ;
  · `vocab/`  — les treize photos du banc de vocabulaire, réduites à 800 px.

**Format 3:2 paysage** : la zone de glisser-déposer est un rectangle de
223 x 132 px. Une image carrée y perd le tiers du haut et du bas.

Trois contraintes propres à ce module, plus dures qu'ailleurs :

- **Rien de spectaculaire ni d'angoissant.** Le sujet est une urgence
  médicale ; les images ne doivent ni dramatiser ni effrayer. Pas de sang, pas
  de gyrophare éblouissant, pas de réanimation, pas de personne au sol montrée
  frontalement. Les scènes sont calmes, ordinaires, souvent vides de monde.
- **Aucun visage, aucun uniforme à insigne, aucun logo d'établissement ni de
  service d'urgence.** Les personnes sont vues de dos, de trois quarts arrière
  ou hors cadrage. Rien n'imite l'identité visuelle d'un vrai service
  ambulancier ni d'un vrai hôpital du Québec.
- **Aucun texte lisible**, comme partout. Les documents et les écrans sont
  photographiés de biais ou en faible profondeur de champ, les lignes réduites
  à des traits gris.

Une image à la fois, journal .json adjacent dans ~/Claude/generations, puis
copie vers le module. Relançable : une image déjà présente est sautée.

  python3 build/contenu/module-n5-urgence/gen_images.py
  python3 build/contenu/module-n5-urgence/gen_images.py escalier
"""
import io, json, os, pathlib, sys, time, urllib.request, urllib.error

MODULE = 'module-n5-urgence'
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

NUIT = ("Photographie réaliste, format paysage, scène nocturne éclairée par "
        "une seule source douce, ambiance calme et sobre, faible profondeur de "
        "champ. Rien de dramatique ni d'effrayant. Aucun texte lisible, aucun "
        "logo, aucune personne identifiable.")

ECRAN = ("Photographie réaliste, format paysage, écran de téléphone vu de "
         "trois quarts, éclairage doux, faible profondeur de champ. Le contenu "
         "de l'écran est flou : des rectangles et des traits gris, aucun mot "
         "lisible, aucun logo, aucune couleur de marque reconnaissable.")

PERS = ("Photographie réaliste, format paysage, scène de la vie quotidienne au "
        "Québec avec une ou deux personnes vues de dos, de trois quarts arrière "
        "ou hors cadrage du visage. Lumière naturelle douce, faible profondeur "
        "de champ. Aucun visage reconnaissable, aucun texte, aucun logo, aucun "
        "filigrane.")

SOIN = ("Photographie réaliste, format paysage, matériel ou local de soins "
        "ordinaire et bien rangé, éclairage neutre, faible profondeur de champ. "
        "Aucun visage, aucune blouse à insigne, aucun logo d'établissement, "
        "aucun texte lisible. Rien d'inquiétant ni de spectaculaire : ni sang, "
        "ni réanimation, ni appareil médical impressionnant.")

P_EX1 = "Je découvre · Exercice 3 — Les images de la nuit"
P_VOC = "Je retiens des mots — banc de vocabulaire"

# (nom, dossier, page, prompt)
IMAGES = [
 # ── Je découvre · les six images de `prImg` ───────────────────────────
 ('thermometre', 'images', P_EX1, STYLE + " Un thermomètre numérique posé sur une table "
  "de salon à côté d'un verre d'eau et d'une boîte de mouchoirs, en fin de soirée. "
  "L'écran du thermomètre est flou et illisible."),
 ('telephone-nuit', 'images', P_EX1, PERS + " Une femme debout dans un salon éclairé par "
  "une seule lampe, le téléphone à l'oreille, vue de dos, la nuit. Atmosphère calme, "
  "aucun visage."),
 ('escalier', 'images', P_EX1, NUIT + " Un escalier intérieur étroit d'un logement "
  "ordinaire, marches de bois, main courante, éclairé par le haut. Aucune personne."),
 ('ambulance', 'images', P_EX1, NUIT + " Un véhicule d'ambulance blanc arrêté devant un "
  "immeuble résidentiel, la nuit, vu de trois quarts arrière et à distance. Gyrophares "
  "éteints, aucune inscription lisible, aucun logo, aucune personne."),
 ('triage', 'images', P_EX1, SOIN + " Un comptoir d'accueil de triage vide dans une "
  "urgence d'hôpital : un appareil à mesurer la tension posé sur le comptoir, un écran "
  "éteint, une chaise. Aucune personne, aucune affiche lisible."),
 ('chambre', 'images', P_EX1, SOIN + " Une chambre d'hôpital ordinaire et lumineuse : un "
  "lit fait, une marchette de métal appuyée à côté, une petite table roulante, une "
  "fenêtre. Aucune personne."),

 # ── Je retiens des mots · les treize photos du banc ───────────────────
 ('malaise', 'vocab', P_VOC, PERS + " Une personne âgée assise dans un fauteuil de salon, "
  "penchée en avant, une main appuyée sur l'accoudoir, vue de trois quarts arrière. "
  "Aucun visage, atmosphère calme et non dramatique."),
 ('811', 'vocab', P_VOC, ECRAN + " Un téléphone tenu à la main dans une cuisine le soir, "
  "l'écran d'appel allumé, tout le texte et les chiffres flous et illisibles."),
 ('fievre', 'vocab', P_VOC, STYLE + " Un thermomètre numérique posé sur un drap froissé à "
  "côté d'un verre d'eau, cadrage serré, lumière de lampe de chevet. Aucun chiffre "
  "lisible."),
 ('911', 'vocab', P_VOC, ECRAN + " Un téléphone posé sur une table de salon la nuit, "
  "l'écran allumé montrant un appel en cours, texte et chiffres entièrement flous."),
 ('repartiteur', 'vocab', P_VOC, PERS + " Une personne assise devant plusieurs écrans dans "
  "une salle sombre, casque téléphonique sur la tête, vue de dos. Écrans flous, aucun "
  "visage, aucun logo."),
 ('ambulanciers', 'vocab', P_VOC, PERS + " Deux personnes en uniforme sombre vues de dos "
  "qui déchargent une civière à l'arrière d'un véhicule blanc, le soir. Aucun visage, "
  "aucun insigne, aucune inscription lisible."),
 ('civiere', 'vocab', P_VOC, SOIN + " Une civière à roulettes vide, drap blanc et "
  "courroies, dans un corridor éclairé. Aucune personne, aucune inscription."),
 ('triage', 'vocab', P_VOC, SOIN + " Un poste de triage vu de côté : comptoir, brassard de "
  "tensiomètre posé, moniteur éteint, chaise pour le patient. Aucune personne, aucune "
  "affiche lisible."),
 ('signes-vitaux', 'vocab', P_VOC, SOIN + " Un brassard de tensiomètre, un oxymètre de "
  "doigt et un thermomètre posés côte à côte sur un plateau, cadrage serré, lumière "
  "neutre. Aucun chiffre lisible, aucune personne."),
 ('radiographie', 'vocab', P_VOC, SOIN + " Une image radiographique grise affichée sur un "
  "négatoscope lumineux, vue légèrement de biais, contours flous. Aucun texte lisible, "
  "aucune personne."),
 ('hospitalisation', 'vocab', P_VOC, SOIN + " Un lit d'hôpital occupé vu de loin et de "
  "dos, une couverture, un sac de soluté sur son support, une fenêtre au fond. Aucun "
  "visage, aucune inscription."),
 ('visite', 'vocab', P_VOC, PERS + " Une personne assise sur une chaise près d'un lit "
  "d'hôpital, vue de dos, un petit sac posé par terre, lumière du jour par la fenêtre. "
  "Aucun visage."),
 ('conge', 'vocab', P_VOC, PERS + " Une personne âgée qui sort d'un hôpital avec une "
  "marchette, accompagnée d'une autre personne, vues de dos dans un hall lumineux. "
  "Aucun visage, aucune enseigne lisible."),
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
