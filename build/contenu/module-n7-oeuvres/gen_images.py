#!/usr/bin/env python3
"""Les 16 images de module-n7-oeuvres — « Ce que j'en pense, et pourquoi ».

Deux destinations :
  · `images/` — les six photos de « Où l'on rencontre une œuvre » (prImg) et
    les six de « Ce que la chanson montre » (t2img), 1200 px, qualité 85 ;
  · `vocab/`  — les quatre seules cartes illustrables du banc, 800 px,
    qualité 82.

**La difficulté de ce module, et comment elle est résolue.** Une œuvre est
presque toujours accompagnée de texte : une affiche de spectacle, une
couverture de livre, un générique, une pochette, une critique de journal. La
règle 1 de la vague 7 l'interdit dans l'image, et pour une raison qui ne se
négocie pas — le modèle écrit du charabia, et l'élève de niveau 7 le lit. La
sortie est celle qu'a trouvée `module-n7-publicite` : **quand le texte est le
sujet, il se compose en HTML**. Tout le texte de ce module — la transcription
du sketch, les paroles de la chanson, la critique du Courrier — vit dans trois
exercices de type `texte`, où il est correct et relisible. Les images ne
montrent alors que la **scène autour** : la salle vide, le hall désert, la
scène nue, l'escalier, la ruelle.

D'où la constante `SANS_MOT`, posée sur toutes les images sans exception, et
des cadrages choisis pour mettre l'inscription **hors champ** plutôt que pour
l'interdire — la leçon du 23 août : sur un objet dont le modèle *sait* qu'il
porte des inscriptions, la négation ne tient pas, seul le cadrage tient.

· `hall-de-cinema` : les affiches et l'écran de tarifs sont hors champ, le
  cadrage s'arrête sous la ligne des cadres muraux.
· `scene-de-bar` et `scene-de-sketch` : aucun panneau, aucun écran, aucune
  affiche derrière — un rideau noir plein.
· `rayon-de-romans` : les livres sont vus **par la tranche**, hors du plan de
  netteté ; aucun dos lisible, aucune étiquette de cote.
· `long-metrage` : l'écran est une surface claire uniforme, sans image ni
  caractère.
· `boite-de-carton` : aucune étiquette d'expédition, aucun marqueur.

Chaque prompt d'image d'exercice est écrit **à partir de la phrase de sa
rangée `ok`**, recopiée en commentaire juste au-dessus. C'est la règle 4, la
plus fréquemment enfreinte, et la seule qui ne se voie pas sans mettre la
phrase à côté de la photo (`node build/contexte_images.js module-n7-oeuvres`).

Quinze des dix-neuf cartes du banc n'ont pas d'image, et c'est voulu : une
ironie, une chute, une concession, une appréciation, un registre de langue ne
se photographient pas. Leur donner une photo mettrait derrière chaque mot une
vue générique de salle de spectacle — c'est-à-dire le thème du module à la
place de ce que dit la carte, le quatrième défaut commis quinze fois. Le poids
visuel est porté par les deux `imgmatch`, dont les énoncés sont des scènes
concrètes.

Aucun appel réseau en dur : le module importe `build/route_images.py`, qui
essaie Google en direct, puis fal.ai, puis WaveSpeed, et inscrit chaque
tentative au registre d'appels de `~/Claude/generations/journal_appels.py`.

Relançable : une image déjà présente est sautée. Pour en refaire une, effacer
son fichier d'abord — et **corriger le prompt ici**, pas seulement le fichier.

  python3 build/contenu/module-n7-oeuvres/gen_images.py
  python3 build/contenu/module-n7-oeuvres/gen_images.py ruelle-au-vent
"""
import io
import json
import pathlib
import sys
import time

MODULE = 'module-n7-oeuvres'
GEN = pathlib.Path.home() / 'Claude' / 'generations'
# Relatif au fichier, jamais absolu : un agent qui travaille dans un worktree
# doit voir ses images arriver dans SON arborescence, pas dans le dépôt
# principal.
BASE = (pathlib.Path(__file__).resolve().parents[3]
        / 'assets' / 'interactive' / MODULE)
RATIO = "3:2"

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from route_images import generer_image                       # noqa: E402

P_EX = "Je découvre · Exercice 3 — Où l'on rencontre une œuvre"
P_CH = "Défi 2 · Exercice 3 — Ce que la chanson montre"
P_VOC = "Je retiens des mots — banc de vocabulaire"

# Trois décors, repris tels quels d'un prompt à l'autre pour que les seize
# images se ressemblent. Le module se passe à Gatineau, en hiver, dans des
# lieux modestes : sous-sol d'église, cinéma de quartier, escalier extérieur.
# Ni salle de concert prestigieuse, ni cinéma multiplexe.
S_SALLE = ("Photographie réaliste, format paysage, intérieur d'un lieu "
           "culturel modeste au Québec : salle de quartier, sous-sol "
           "communautaire ou petit cinéma de rue, mobilier usé mais propre, "
           "éclairage chaud d'une ou deux sources. Palette sobre, faible "
           "profondeur de champ. Aucune personne dans le cadre. ")
S_RUE = ("Photographie réaliste, format paysage, rue ordinaire de Gatineau en "
         "hiver : neige tassée en bordure, brique rouge, escaliers extérieurs "
         "en métal, fils électriques, ciel bas. Lumière naturelle basse, "
         "palette sobre et froide. Aucune personne identifiable, aucun visage "
         "reconnaissable. ")
S_OBJET = ("Photographie réaliste, format paysage, lumière naturelle douce, "
           "faible profondeur de champ, arrière-plan neutre et flou. Objet du "
           "quotidien, un peu usé, jamais neuf ni décoratif. Aucune main, "
           "aucun doigt, aucune personne dans le cadre. ")

# Posée sur TOUTES les images de ce module sans exception. Le sujet est la
# découverte d'œuvres : chaque scène risque de porter une affiche, un titre,
# une pochette, un générique. Le texte du module vit dans le HTML, jamais dans
# l'image.
SANS_MOT = (" Absolument aucun texte, aucune lettre, aucun mot, aucun chiffre, "
            "aucun titre, aucun logo, aucune affiche lisible, aucune enseigne, "
            "aucune étiquette nulle part dans l'image : toute surface qui "
            "porterait normalement une inscription est un aplat de couleur uni "
            "ou une zone floue. Aucun mot d'anglais nulle part.")

# (nom, dossier, page, prompt)
IMAGES = [
 # ── Les six images de « Où l'on rencontre une œuvre » ─────────────────
 # Chaque prompt est écrit à partir de la phrase de sa rangée `ok`, recopiée
 # ci-dessus en commentaire. C'est la règle 4 de la vague 7.

 # « Une salle de spectacle vue depuis la scène : des rangées de fauteuils
 #   rouges vides et un balcon au fond. »
 ('salle-vue-de-scene', 'images', P_EX, S_SALLE +
  "Une salle de spectacle de quartier photographiée **depuis la scène**, face "
  "au public : des rangées régulières de fauteuils de velours rouge tous "
  "vides, une allée centrale, et au fond un balcon avec sa rampe de bois. "
  "Éclairage de service seulement, doux et inégal. Aucune personne, aucun "
  "panneau de sortie visible : le cadrage s'arrête sous la ligne des murs "
  "latéraux." + SANS_MOT),

 # « Le hall d'un cinéma de quartier un soir de semaine : un comptoir, un
 #   tapis usé, personne dans la file. »
 ('hall-de-cinema', 'images', P_EX, S_SALLE +
  "Le hall d'entrée d'un petit cinéma de quartier, un soir de semaine : un "
  "comptoir de service en mélamine avec sa vitrine à maïs soufflé éteinte, un "
  "tapis à motif usé jusqu'à la corde, un cordon de file d'attente qui ne "
  "retient personne. Le cadrage s'arrête **sous la ligne des cadres muraux** : "
  "aucune affiche, aucun écran de tarifs, aucun panneau dans le champ. "
  "Personne dans la pièce." + SANS_MOT),

 # « Une petite scène de bar avec un tabouret, un micro sur pied et un rideau
 #   noir derrière. »
 ('scene-de-bar', 'images', P_EX, S_SALLE +
  "Une petite scène surélevée de bar de quartier, vue de la salle à quatre "
  "mètres : un tabouret de bois seul au centre, un microphone sur pied incliné "
  "à côté, un verre d'eau posé par terre. Derrière, un **rideau de velours "
  "noir plein**, sans aucun panneau ni décor. Un projecteur chaud éclaire le "
  "tabouret ; le reste est dans l'ombre. Aucune personne." + SANS_MOT),

 # « Un rayon de romans dans une bibliothèque municipale, avec un fauteuil
 #   sous une lampe. »
 ('rayon-de-romans', 'images', P_EX, S_SALLE +
  "Un rayon de bibliothèque municipale vu de trois quarts : trois tablettes de "
  "livres serrés, tous vus **par la tranche et entièrement hors du plan de "
  "netteté** — on ne distingue que des blocs de couleur, aucun dos lisible, "
  "aucune étiquette de cote. Au premier plan net, un fauteuil de tissu usé "
  "sous une lampe sur pied allumée, et une petite table basse vide. Personne." +
  SANS_MOT),

 # « Un sous-sol d'église transformé en salle : des chaises pliantes en
 #   rangées devant une scène montée sur des palettes. »
 ('sous-sol-deglise', 'images', P_EX, S_SALLE +
  "Le sous-sol d'une église transformé en salle de spectacle : une centaine de "
  "chaises pliantes de métal alignées en rangées sur un plancher de tuiles "
  "beiges, face à une petite estrade **montée sur des palettes de bois** avec "
  "un tapis dessus. Plafond bas à tuiles acoustiques, tuyaux apparents, "
  "éclairage au néon. Aucune personne, aucun panneau." + SANS_MOT),

 # « Un studio d'enregistrement : une guitare sur son support, un casque posé
 #   sur la table, une vitre au fond. »
 ('studio-denregistrement', 'images', P_EX, S_SALLE +
  "L'intérieur d'un petit studio d'enregistrement : une guitare acoustique "
  "posée sur son support au premier plan net, un casque d'écoute abandonné sur "
  "une table de bois, un microphone sur pied avec sa bonnette. Au fond, une "
  "vitre qui donne sur la régie, sombre. Murs de mousse acoustique grise. "
  "Aucune personne, aucun écran allumé." + SANS_MOT),

 # ── Les six images de « Ce que la chanson montre » ────────────────────
 # Ce sont les objets que la chanson nomme vraiment — le premier degré du
 # texte. C'est exactement ce qu'il faut : la deuxième chose que dit la
 # chanson ne se photographie pas, et rien n'aurait été pire que d'essayer.

 # « Un escalier extérieur en colimaçon couvert de glace, vu d'en bas depuis
 #   le trottoir. »
 ('escalier-en-colimacon', 'images', P_CH, S_RUE +
  "Un escalier extérieur **en colimaçon** en métal noir, accroché à la façade "
  "de brique rouge d'un immeuble de trois étages, photographié **d'en bas "
  "depuis le trottoir**, en contre-plongée. Les marches et la rampe sont "
  "couvertes d'une couche de glace luisante. Fin d'après-midi d'hiver, ciel "
  "gris. Aucune personne dans l'escalier." + SANS_MOT),

 # « Deux sacs d'épicerie en papier posés sur une marche de béton enneigée. »
 ('sacs-sur-la-marche', 'images', P_CH, S_OBJET +
  "Deux sacs d'épicerie en papier brun, pleins et un peu affaissés, posés côte "
  "à côte sur une **marche de béton enneigée** au pied d'un escalier "
  "extérieur. Un poireau et une boîte de conserve dépassent d'un des sacs. "
  "Neige fondante autour, lumière froide de fin de journée. Aucune main, "
  "aucune personne. Le papier des sacs est **uni, sans aucune impression**." +
  SANS_MOT),

 # « Une rampe de métal toute neuve, encore luisante, boulonnée sur un
 #   escalier vieux et rouillé. »
 ('rampe-neuve', 'images', P_CH, S_OBJET +
  "Gros plan sur la jonction entre une **rampe d'escalier en métal galvanisé "
  "toute neuve, encore luisante et sans une trace de rouille**, et les "
  "montants **vieux, écaillés et rouillés** de l'escalier extérieur sur lequel "
  "elle vient d'être boulonnée. Les boulons neufs sont nets au premier plan. "
  "Neige et brique rouge floues à l'arrière-plan. Aucune main." + SANS_MOT),

 # « Une seule fenêtre allumée au troisième étage d'un immeuble, vue d'en bas,
 #   un soir d'hiver. »
 ('fenetre-allumee', 'images', P_CH, S_RUE +
  "La façade de brique d'un immeuble de trois étages photographiée d'en bas, "
  "le soir : toutes les fenêtres sont sombres sauf **une seule, au troisième "
  "étage**, dont la lumière chaude traverse un rideau tiré. On ne voit "
  "personne derrière. Neige sur les corniches, ciel bleu nuit. Aucune enseigne, "
  "aucun numéro civique dans le champ : le cadrage commence au-dessus du "
  "rez-de-chaussée." + SANS_MOT),

 # « Une boîte de carton fermée avec du ruban, posée seule contre un mur de
 #   corridor. »
 ('boite-de-carton', 'images', P_CH, S_OBJET +
  "Une boîte de carton brun de taille moyenne, **fermée avec du ruban adhésif "
  "transparent**, posée seule au sol contre le mur d'un corridor d'immeuble "
  "locatif : plancher de linoléum usé, plinthe de bois peinte, une porte "
  "d'appartement floue au fond. Un peu de poussière au bas du mur. Le carton "
  "est **entièrement nu — aucune étiquette d'expédition, aucun marqueur, aucun "
  "sigle imprimé**." + SANS_MOT),

 # « Une ruelle étroite entre deux immeubles de brique, où la neige tourne
 #   dans le vent. »
 ('ruelle-au-vent', 'images', P_CH, S_RUE +
  "Une ruelle étroite entre deux murs de brique rouge sans fenêtre, vue depuis "
  "son entrée : de la **neige fine soulevée par le vent** tourne en tourbillons "
  "au ras du sol et brouille le fond de la ruelle. Un conteneur à déchets "
  "métallique contre un mur, des fils électriques au-dessus. Fin de journée, "
  "lumière bleutée. Aucune personne, aucun graffiti lisible : les murs sont "
  "de la brique nue." + SANS_MOT),

 # ── Les quatre photos du banc de vocabulaire ──────────────────────────
 # Quatre sur dix-neuf cartes. Les quinze autres — l'ironie, une chute, une
 # concession, un argument, un registre de langue — sont des idées : une photo
 # leur donnerait le thème du module à la place de leur définition.

 ('salle-de-spectacle', 'vocab', P_VOC, S_SALLE +
  "Une salle de spectacle de quartier vue depuis le fond de la salle, en "
  "légère plongée : des rangées de fauteuils rouges vides, une allée centrale, "
  "et au fond une scène de bois vide sous un éclairage bleuté. Rideau latéral "
  "sombre. Aucune personne, aucun panneau." + SANS_MOT),

 ('tour-de-chant', 'vocab', P_VOC, S_SALLE +
  "Une petite scène vue de la salle : une guitare acoustique posée sur son "
  "support, un microphone sur pied à hauteur de bouche, un tabouret et un "
  "verre d'eau. Un seul projecteur chaud éclaire le cercle où l'artiste se "
  "tiendra ; le fond est un rideau noir plein. Personne sur scène." + SANS_MOT),

 ('long-metrage', 'vocab', P_VOC, S_SALLE +
  "L'intérieur d'un petit cinéma de quartier vu du fond de la salle : quelques "
  "rangées de fauteuils vides et, au bout, un **écran de projection montrant "
  "une surface claire parfaitement uniforme, légèrement bleutée, sans aucune "
  "image et sans aucun caractère**. Sa lueur éclaire faiblement les dossiers. "
  "Aucune personne." + SANS_MOT),

 ('scene-de-sketch', 'vocab', P_VOC, S_SALLE +
  "Une scène nue de petite salle, vue de face à quelques mètres : un tabouret "
  "de bois seul au centre, un microphone sur pied légèrement incliné, une "
  "bouteille d'eau au sol. Derrière, un **rideau de velours noir plein**, sans "
  "aucun décor ni panneau. Un projecteur découpe un cercle de lumière chaude "
  "sur le plancher. Aucune personne." + SANS_MOT),
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
