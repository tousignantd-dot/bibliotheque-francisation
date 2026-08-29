#!/usr/bin/env python3
"""Les mots que la voix doit appuyer, phrase par phrase.

    python3 build/insistance.py        # vérifie que chaque phrase existe encore

Certaines mini-leçons enseignent l'**accent d'insistance** : l'élève doit
entendre quel mot est appuyé, et le nommer. Or l'audio sortait plat — une
phrase ordinaire, aucun mot détaché. La leçon ne voulait rien dire.

Pourquoi une table, et pas un marquage dans le contenu
------------------------------------------------------
Le texte lu vient du champ `say:` des blocs de `plus.js`, et ce même champ
sert de **repli au navigateur** quand le MP3 manque : `playWord()` le passe à
`speakText()`. Y écrire `<b>…</b>` ferait prononcer « inférieur b supérieur »
à l'élève le jour où un fichier manque. La marque vit donc ici, du côté de la
synthèse seulement — la page n'en voit jamais rien.

Pourquoi `<prosody>` et pas `<emphasis>`
----------------------------------------
Mesuré le 29 août 2026 : `<emphasis level="strong">` est **ignoré** par les
voix neurales fr-CA. Le fichier revient identique à l'octet près — même
empreinte md5 que la version sans balise. `<prosody>` sur un mot, lui, agit.

Deux pièges de l'API : `volume="+4dB"` est refusé (HTTP 400), il faut le mot
`loud` ; et la balise doit envelopper le mot **dans** la phrase, jamais un
fichier séparé — un mot synthétisé seul repart d'une intonation neutre et
finit sur une chute, ce qui s'entend comme une phrase de plus, pas comme une
insistance.
"""
import pathlib
import re
import sys

RACINE = pathlib.Path(__file__).resolve().parent.parent

# Ce que l'audio contient désormais : la phrase **plate**, un silence, la même
# phrase **appuyée**, un silence, puis le **mot seul** en guise de réponse.
#
# Pourquoi trois temps plutôt qu'un accent unique. Écouté isolément, l'accent
# d'insistance d'Azure ne s'entend pas — vérifié à l'oreille le 29 août 2026,
# après avoir poussé les réglages jusqu'à `-40% / +25% / x-loud` sans résultat
# convaincant. Placé juste après la version plate, il n'a plus besoin d'être
# perceptible dans l'absolu : il n'a qu'à être **différent**. La comparaison
# abaisse le seuil, et c'est elle qui enseigne — un élève ne reconnaît un
# accent qu'en entendant ce à quoi il s'oppose.
#
# Pourquoi ces valeurs-là. Le décalage de hauteur est ce qui met le vocodeur en
# difficulté : à `+20%` sur un mot isolé, la voix grésille — et ce n'est pas un
# écrêtage, la crête restait à -5,8 dBFS avec 5 dB de marge. On allonge et on
# appuie ; on **ne transpose pas**, ou très peu.
RATE, PITCH, VOLUME = "-35%", "+10%", "loud"          # la phrase appuyée
RATE_MOT, VOLUME_MOT = "-20%", "loud"                 # le mot seul, à la fin
PAUSE_ENTRE = "700ms"                                 # entre les trois temps
PAUSE_AVANT = "220ms"                                 # juste avant le mot appuyé

# La table est indexée par **fichier**, pas par phrase. Une première version
# la classait par texte, et c'était faux : « Je le veux, ce poste-là. » sert à
# la fois dans la leçon sur la volonté — où l'insistance a sa place — et dans
# un laboratoire d'intonation, une leçon de syntaxe sur la dislocation à
# droite et un item d'exercice, où une démonstration en trois temps n'a rien
# à faire. Trois fichiers du niveau 8 avaient déjà été gâtés ainsi.
#
#   (module, identifiant du son) → le mot ou groupe à appuyer
TABLE = {
    ("module-n7-emploi", "prProso_savoir_3_0"):    "spectaculaire",
    ("module-n7-emploi", "plus_prProso_ana4"):     "spectaculaire",
    ("module-n7-emploi", "plus_prProso_lab5_b2"):  "spectaculaire",
    ("module-n7-achat", "prProso_pr3"):            "Vous",
    ("module-n7-achat", "plus_prProso_ana3"):      "Vous",
    ("module-n8-oeuvres", "prInto_pid"):           "plus belle",
    ("module-n8-oeuvres", "plus_prInto_ana2"):     "plus belle",
    ("module-n8-actualite", "prInto_pif"):         "veux",
    ("module-n8-actualite", "plus_prInto_ana4"):   "veux",
    ("module-n8-emmenagement", "prInto_pic"):      "conteste",
    ("module-n8-emmenagement", "plus_prInto_ana4"): "conteste",
    ("module-n8-recherche", "plus_prInto_ana4"):   "veux",
}


def marque(chemin):
    """Le mot à appuyer pour ce fichier, ou None.

    `chemin` est la destination du MP3 :
    `assets/interactive/<module>/sons/<identifiant>.mp3`.
    """
    if chemin is None:
        return None
    p = pathlib.Path(chemin)
    if p.parent.name != "sons":
        return None
    try:
        module = p.parent.parent.name
    except (AttributeError, IndexError):
        return None
    return TABLE.get((module, p.stem))


def verifie():
    """Chaque son de la table existe-t-il, et son mot est-il dans son texte ?

    Un identifiant qui disparaît, ou une phrase retouchée d'où le mot a été
    retiré, ferait sortir un fichier bancal en silence. Le contrôle est lancé
    à la main, et devrait l'être après toute retouche des mini-leçons.
    """
    import json
    perdues, ok = [], 0
    for (module, fid), mot in sorted(TABLE.items()):
        manifeste = RACINE / ('sons_%s.json' % module.replace('module-', 'module_').replace('-', '_'))
        if not manifeste.exists():
            perdues.append('%s → manifeste absent' % module)
            continue
        sons = json.loads(manifeste.read_text(encoding='utf-8'))
        texte = sons.get(fid)
        if texte is None:
            perdues.append('%s / %s → identifiant absent du manifeste' % (module, fid))
        elif mot not in texte:
            perdues.append('%s / %s → « %s » absent de « %s »' % (module, fid, mot, texte[:40]))
        elif not (RACINE / 'assets' / 'interactive' / module / 'sons' / (fid + '.mp3')).exists():
            perdues.append('%s / %s → MP3 absent' % (module, fid))
        else:
            ok += 1
    print('%d sons sur %d en place et cohérents' % (ok, len(TABLE)))
    for p in perdues:
        print('   !! %s' % p)
    return not perdues


if __name__ == '__main__':
    sys.exit(0 if verifie() else 1)
