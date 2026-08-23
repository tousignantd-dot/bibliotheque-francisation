# -*- coding: utf-8 -*-
"""Écrit `generer_audio_module_n8_habitation.py` à partir de celui de l'activité 119.

Le corps d'un générateur d'audio est identique d'un module à l'autre — la
reprise sur coupure réseau, la lecture des dialogues, le manifeste, la boucle.
Ce qui change tient en trois endroits : le slug, la table `VOIX_PERSO`, et le
docstring. Recopier à la main les deux cent cinquante lignes, c'est se donner
une occasion de diverger sur la reprise réseau ou sur `slug()`, dont
`CLAUDE.md` dit expressément qu'elle ne doit pas être « améliorée ».

Ce script se relance sans danger : il écrase le générateur produit.

    python3 build/contenu/module-n8-habitation/_forger_generateur.py
"""
import pathlib

RACINE = pathlib.Path(__file__).resolve().parents[3]
MODELE = RACINE / 'generer_audio_module_n8_recherche.py'
CIBLE = RACINE / 'generer_audio_module_n8_habitation.py'

src = MODELE.read_text(encoding='utf-8')
corps = src[src.index('"""', src.index('"""') + 3) + 3:]

corps = corps.replace('module-n8-recherche', 'module-n8-habitation')
# Le générateur de l'activité 119 pointe son MANIFESTE sur
# `sons_module_n7_recherche.json` — le nom du module du niveau 7. C'est un
# défaut chez lui, signalé à part ; ici on écrit le bon nom.
corps = corps.replace('sons_module_n7_recherche.json',
                      'sons_module_n8_habitation.json')

ANCIEN_CASTING = """# Quatre personnages, quatre voix — une chacune. Aucun partage, donc aucune
# contrainte de croisement à vérifier :
#
#   prep  SHIRIN, ALEXANDRE          t1  DANIELLE, SHIRIN
#   t2    RÉAL, SHIRIN               t3  DANIELLE, SHIRIN, RÉAL
#
# Le défi 3 réunit trois personnages, dont deux femmes : c'est la limite exacte
# du dépôt, et elle tient parce que Danielle prend `enseignante` et Shirin
# `feminin_2`. Une troisième femme aurait été impossible.
#
# Le choix de qui prend `enseignante` n'est pas neutre : c'est la seule voix
# que `voix_lente` ralentit à 0,85. Elle va à DANIELLE, la conseillère en
# acquisition de talents, qui mène l'appel de présélection et énonce les trois
# étapes du processus — exactement le rôle pour lequel un débit posé a été
# introduit. RÉAL garde `narrateur`, qui n'est pas ralentie : sa séance
# d'information **est** l'exercice d'écoute longue du module, et la ralentir en
# retirerait la difficulté que le niveau 8 vise.
VOIX_PERSO = {
    "SHIRIN":    "feminin_2",
    "DANIELLE":  "enseignante",
    "ALEXANDRE": "masculin_1",
    "RÉAL":      "narrateur",
}"""

NOUVEAU_CASTING = """# Quatre personnages, quatre voix — une chacune. Aucun partage, donc aucune
# contrainte de croisement à vérifier :
#
#   prep  TEODORA, MARJOLAINE        t1  TEODORA, NORMAND
#   t2    TEODORA, MARJOLAINE        t3  FABIEN, TEODORA
#
# Aucun extrait ne réunit plus de deux personnes, et jamais deux femmes autres
# que Teodora et Marjolaine : le dépôt n'a que deux voix féminines, et ça se
# compte **avant** d'écrire les dialogues, comme `CLAUDE.md` le demande depuis
# `module-n7-habitation`.
#
# Le choix de qui prend `enseignante` n'est pas neutre : c'est la seule voix
# que `voix_lente` ralentit à 0,85. Elle va à MARJOLAINE, l'agente au règlement
# des sinistres, dont les répliques sont courtes et administratives. Elle ne
# pouvait surtout pas aller à FABIEN, qui porte le **monologue** du défi 3 :
# quinze répliques d'affilée ralenties seraient interminables, et la note de
# l'activité 119 le dit en toutes lettres. FABIEN garde donc `narrateur`.
VOIX_PERSO = {
    "TEODORA":    "feminin_2",
    "MARJOLAINE": "enseignante",
    "NORMAND":    "masculin_1",
    "FABIEN":     "narrateur",
}"""

assert ANCIEN_CASTING in corps, "la table VOIX_PERSO du modèle a changé de forme"
corps = corps.replace(ANCIEN_CASTING, NOUVEAU_CASTING)

ENTETE = '''#!/usr/bin/env python3
"""
Générateur d'audio — module « Faire renverser une décision » (niveau 8)
(module-n8-habitation, activité 121).

Deux familles de fichiers, comme dans les autres modules :

  1. les répliques des quatre extraits → <module>/<dialId>/line_NN_<perso>.mp3
  2. les mots, phrases et mini-leçons  → <module>/sons/<fileId>.mp3

Les dialogues ne sont pas recopiés ici : ils sont lus dans
`build/contenu/module-n8-habitation/dialogues.js`, la source unique. Ce fichier
lui-même est **produit** par
`build/contenu/module-n8-habitation/_forger_generateur.py`, à partir du
générateur de l'activité 119 : seuls le slug, la table `VOIX_PERSO` et ce
docstring diffèrent d'un module à l'autre, et recopier le reste à la main
serait une occasion de diverger sur la reprise réseau ou sur `slug()`.

**Le défi 3 est un monologue**, et c'est ce que le niveau 8 réclame de neuf :
quinze répliques d'affilée d'un même locuteur, coupées par deux questions —
« suivre le déroulement d'exposés bien structurés », que le programme demande
et qu'aucun module des niveaux inférieurs n'a. Conséquence directe sur les
voix, et ce n'est pas un détail : ce locuteur prend `narrateur` et **jamais**
`enseignante`, que `voix_lente` ralentit à 0,85. Quinze répliques ralenties
d'affilée seraient interminables.

**Quatre personnages, quatre voix distinctes.** Le dépôt n'en a que quatre —
deux féminines, deux masculines — et ce module les prend toutes, une chacune :
aucun partage, donc aucun risque d'entendre la même voix se répondre à
elle-même. Compté par extrait et par genre **avant** d'écrire les dialogues.

Le relevé des sons (famille 2) n'a **pas** été fait par le navigateur ni par
`build/collecte_sons.py`, qu'il ne faut pas lancer :

    node build/releve_sons.js module-n8-habitation > sons_module_n8_habitation.json

Vingt lignes de node sur `exos.js`, `carrier.js` et `plus.js`, qui reproduisent
les trois endroits du gabarit appelant `playWord`. Pas de port à réserver, pas
de processus à arrêter, pas d'envoi tardif qui écraserait un relevé complet par
un relevé partiel — les deux incidents que `CLAUDE.md` raconte.

**Ce générateur n'a pas encore été lancé** : une production audio complète
tournait sur le poste au moment de la livraison du module. Il s'importe sans
erreur, retrouve ses 85 répliques sur quatre dialogues (22, 23, 23 et 17)
et son manifeste de 151 sons — 236 extraits en tout ; il attend son tour.

Usage :  python3 generer_audio_module_n8_habitation.py [--force] [--only prefixe,...]
"""'''

CIBLE.write_text(ENTETE + corps, encoding='utf-8')
print('écrit %s (%d octets)' % (CIBLE.name, CIBLE.stat().st_size))
