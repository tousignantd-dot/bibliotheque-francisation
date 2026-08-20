#!/usr/bin/env python3
"""Génère les 16 images du module-probleme via fal.ai (Nano Banana 2).

Une image à la fois, journal .json adjacent, puis copie vers le module.
Relançable : une image déjà présente dans generations/ est sautée.
"""
import base64, json, os, pathlib, sys, time, urllib.request, urllib.error

GEN  = pathlib.Path('/Users/danieltousignant/Claude/generations')
DEST = pathlib.Path('/Users/danieltousignant/Claude/bibliotheque-francisation'
                    '/assets/interactive/module-probleme/images')
ENV  = pathlib.Path('/Users/danieltousignant/Claude/.env')

def cle(nom):
    for ligne in ENV.read_text(encoding='utf-8').splitlines():
        ligne = ligne.strip()
        if ligne.startswith(nom + '='):
            return ligne.split('=', 1)[1].strip().strip('"\'')
    return ''

FAL = cle('FAL_KEY')
if not FAL:
    sys.exit('FAL_KEY absente de ~/Claude/.env')

STYLE = ("Photographie réaliste, format carré, lumière naturelle douce, faible "
         "profondeur de champ. Palette sobre et froide. Aucun texte, aucune "
         "écriture, aucun logo, aucun filigrane, aucune personne identifiable.")

PORTRAIT = ("Photographie réaliste, format carré, portrait en buste d'une personne "
            "au travail dans un logement québécois ordinaire. Lumière naturelle douce, "
            "faible profondeur de champ, arrière-plan flou. Expression calme et "
            "professionnelle. Aucun texte, aucune écriture, aucun logo, aucun filigrane.")

PAGE_PB  = "Je découvre · Exercice 3 — Reconnaître un problème"
PAGE_PRO = "Je découvre · Exercice 4 — Qui faut-il appeler ?"

IMAGES = [
 # ── Les huit problèmes ────────────────────────────────────────────────
 ('moisissure', PAGE_PB, STYLE + " Gros plan sur le coin supérieur d'un mur de salle de "
  "bain : de la moisissure noire et grise s'est étendue en taches irrégulières sur la "
  "peinture blanche et le long du joint de silicone. La peinture cloque légèrement."),
 ('robinet', PAGE_PB, STYLE + " Gros plan sur un robinet de cuisine en acier brossé "
  "au-dessus d'un évier en inox. Une goutte d'eau est suspendue au bec, une autre vient "
  "de tomber et éclabousse le fond de l'évier. Le métal est marqué de traces de calcaire."),
 ('serrure', PAGE_PB, STYLE + " Gros plan sur une serrure de porte d'entrée en laiton "
  "abîmée : le cadre de bois est éclaté autour de la gâche, le pêne est tordu et la porte "
  "ne ferme plus complètement. Éclats de bois clair visibles."),
 ('plancher', PAGE_PB, STYLE + " Gros plan en plongée sur un plancher de bois franc dont "
  "plusieurs lattes ont gondolé et se soulèvent au niveau des joints, formant une bosse. "
  "Le vernis est terni et blanchi par l'eau à cet endroit."),
 ('prise', PAGE_PB, STYLE + " Gros plan sur une prise de courant murale blanche, de type "
  "nord-américain à deux fentes verticales et une broche de mise à la terre ronde. Le "
  "plastique est noirci et fondu autour des fentes, trace nette de surchauffe."),
 ('souris', PAGE_PB, STYLE + " Gros plan au ras du sol sur une plinthe de bois blanche "
  "percée d'un trou rond irrégulier de la taille d'une pièce de monnaie. Des copeaux de "
  "gypse et de la poussière sont éparpillés devant le trou sur le plancher."),
 ('plafond', PAGE_PB, STYLE + " Vue en contre-plongée d'un plafond blanc de chambre, "
  "marqué d'une grande auréole brune irrégulière aux bords plus foncés, causée par une "
  "infiltration d'eau. La peinture s'écaille légèrement au centre de la tache."),
 ('ordures', PAGE_PB, STYLE + " Le coin d'un local à ordures d'immeuble : deux bacs "
  "roulants pleins, couvercles entrouverts, et plusieurs sacs de plastique noirs et des "
  "boîtes de carton détrempées empilés par terre à côté, bloquant le passage. Éclairage "
  "de sous-sol, murs de béton."),
 # ── Les huit professionnels ───────────────────────────────────────────
 ('plombiere', PAGE_PRO, PORTRAIT + " Une plombière d'une quarantaine d'années, cheveux "
  "attachés, salopette de travail bleu marine, agenouillée sous un évier de cuisine. Elle "
  "serre un raccord de tuyau avec une clé à molette. Une lampe de travail éclaire le "
  "dessous de l'armoire."),
 ('electricien', PAGE_PRO, PORTRAIT + " Un électricien d'une trentaine d'années, chemise "
  "de travail grise et ceinture à outils, debout devant un panneau électrique ouvert dans "
  "un couloir. Il tient un multimètre et regarde les disjoncteurs alignés."),
 ('menuisiere', PAGE_PRO, PORTRAIT + " Une menuisière d'une cinquantaine d'années, "
  "lunettes de sécurité relevées sur le front, tablier de travail brun, en train de raboter "
  "le bord d'une porte de chambre posée sur deux tréteaux. Copeaux de bois au sol."),
 ('serrurier', PAGE_PRO, PORTRAIT + " Un serrurier d'une quarantaine d'années, veste de "
  "travail bleu foncé, accroupi devant une porte d'entrée. Il installe un cylindre de "
  "serrure neuf, un trousseau de clés neuves posé à côté de lui sur le seuil."),
 ('exterminatrice', PAGE_PRO, PORTRAIT + " Une exterminatrice d'une trentaine d'années, "
  "combinaison de travail blanche et gants, accroupie près d'une plinthe de cuisine. Elle "
  "place un petit piège discret le long du mur, une lampe de poche à la main."),
 ('couvreur', PAGE_PRO, PORTRAIT + " Un couvreur d'une quarantaine d'années, casque de "
  "sécurité orange et harnais, agenouillé sur une toiture en bardeaux d'asphalte gris. Il "
  "soulève un bardeau abîmé. Ciel couvert au-dessus de toits d'immeubles."),
 ('peintre', PAGE_PRO, PORTRAIT + " Une peintre d'une trentaine d'années, salopette blanche "
  "tachée, cheveux sous un bandana, applique au rouleau une couche de peinture claire sur "
  "un mur de salon fraîchement réparé. Toile de protection au sol."),
 ('installatrice', PAGE_PRO, PORTRAIT + " Une installatrice d'une quarantaine d'années, "
  "polo de travail et ceinture à outils, sur un escabeau dans une salle de bain. Elle visse "
  "au plafond le boîtier blanc d'un ventilateur d'extraction neuf."),
]

def genere(nom, prompt):
    corps = json.dumps({"prompt": prompt, "num_images": 1, "aspect_ratio": "1:1",
                        "resolution": "1K", "output_format": "jpeg"}).encode()
    req = urllib.request.Request(
        "https://fal.run/fal-ai/nano-banana-2", data=corps,
        headers={"Authorization": "Key " + FAL, "Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=180) as r:
        d = json.loads(r.read())
    url = d["images"][0]["url"]
    with urllib.request.urlopen(url, timeout=180) as r:
        return r.read()

GEN.mkdir(parents=True, exist_ok=True)
DEST.mkdir(parents=True, exist_ok=True)
horodatage = time.strftime('%Y%m%d-%H%M%S')
faits, sautes, echecs = [], [], []

for nom, page, prompt in IMAGES:
    cible = DEST / (nom + '.jpg')
    if cible.exists() and cible.stat().st_size > 1000:
        sautes.append(nom); continue
    try:
        data = genere(nom, prompt)
    except urllib.error.HTTPError as e:
        echecs.append('%s : HTTP %s %s' % (nom, e.code, e.read()[:180])); continue
    except Exception as e:
        echecs.append('%s : %s' % (nom, e)); continue

    base = 'module-probleme_%s_%s' % (nom, horodatage)
    (GEN / (base + '.jpg')).write_bytes(data)
    (GEN / (base + '.json')).write_text(json.dumps({
        "model": "fal-ai/nano-banana-2",
        "prompt": prompt,
        "refs": [],
        "params": {"num_images": 1, "aspect_ratio": "1:1",
                   "resolution": "1K", "output_format": "jpeg"},
        "provider": "fal.ai",
        "cost_estimate_usd": 0.034,
        "created": time.strftime('%Y-%m-%dT%H:%M:%S+00:00', time.gmtime()),
        "projet": "bibliotheque-francisation",
        "module": "module-probleme",
        "page": page,
        "destination": "assets/interactive/module-probleme/images/%s.jpg" % nom,
    }, ensure_ascii=False, indent=2), encoding='utf-8')
    cible.write_bytes(data)
    faits.append(nom)
    print('  ✓ %-16s %6.1f Ko' % (nom, len(data) / 1024), flush=True)

print('\n%d générées, %d déjà présentes, %d en échec' % (len(faits), len(sautes), len(echecs)))
for e in echecs:
    print('  ✗ ' + e)
print('coût estimé : %.2f $' % (len(faits) * 0.034))
