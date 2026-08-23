"""Écrit `generer_audio_module_n8_recherche.py` à partir de celui du module
voisin (`module-n7-recherche`), en remplaçant l'en-tête et la table des voix.

Cette famille de scripts est le dernier endroit du projet qui duplique un
fichier par module — la skill `module-neuf` le dit et ne demande pas au module
neuf de régler ce chantier. Passer par un script plutôt que par un copier-coller
manuel rend au moins la dérivation relisible : on voit exactement les trois
choses qui changent.

Lancé une fois, le 23 août 2026. Il est gardé pour que la dérivation soit
vérifiable, pas pour être relancé — le fichier produit est la source.
"""
import pathlib

RACINE = pathlib.Path(__file__).resolve().parents[3]
SOURCE = RACINE / 'generer_audio_module_n7_recherche.py'
CIBLE = RACINE / 'generer_audio_module_n8_recherche.py'

ENTETE = '''#!/usr/bin/env python3
"""
Générateur d'audio — module « Passer au travers du processus » (niveau 8)
(module-n8-recherche, activité 119).

Deux familles de fichiers, comme dans les autres modules :

  1. les répliques des quatre extraits → <module>/<dialId>/line_NN_<perso>.mp3
  2. les mots, phrases et mini-leçons  → <module>/sons/<fileId>.mp3

Les dialogues ne sont pas recopiés ici : ils sont lus dans
`build/contenu/module-n8-recherche/dialogues.js`, la source unique.

Niveau 8, donc des **discours étendus** : les quatre extraits font de vingt à
vingt-huit répliques, et l'entrevue du défi 3 est la plus longue — c'est la
seule longueur qui laisse une objection s'installer, être entendue, et recevoir
une réponse. La séance d'information du défi 2 est presque un monologue : douze
répliques d'affilée du même locuteur, coupées par deux questions.

**Quatre personnages, quatre voix distinctes.** Le dépôt n'en a que quatre —
deux féminines, deux masculines — et ce module les prend toutes, une chacune :
il n'y a donc **aucun partage à vérifier**, aucun risque d'entendre la même
voix se répondre à elle-même. C'est le cas le plus confortable, et il a été
obtenu en comptant les personnages par genre **avant** d'écrire les dialogues,
comme `CLAUDE.md` le demande depuis `module-n7-habitation`.

Le relevé des sons (famille 2) n'a **pas** été fait par le navigateur ni par
`build/collecte_sons.py`, qu'il ne faut pas lancer :

    node build/releve_sons.js module-n8-recherche > sons_module_n8_recherche.json

Vingt lignes de node sur `exos.js`, `carrier.js` et `plus.js`, qui reproduisent
les trois endroits du gabarit appelant `playWord`. Pas de port à réserver, pas
de processus à arrêter, pas d'envoi tardif qui écraserait un relevé complet par
un relevé partiel — les deux incidents que `CLAUDE.md` raconte. 334 clés au
relevé du 23 août 2026.

Usage :  python3 generer_audio_module_n8_recherche.py [--force] [--only prefixe,...]
"""
'''

VOIX = '''# Quatre personnages, quatre voix — une chacune. Aucun partage, donc aucune
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
}

'''

src = SOURCE.read_text(encoding='utf-8')
corps = src[src.index('import json'):]
corps = corps.replace('module-n7-recherche', 'module-n8-recherche')
corps = corps.replace('generer_audio_module_n7_recherche.py',
                      'generer_audio_module_n8_recherche.py')

debut = corps.index('# Six personnages pour quatre voix.')
fin = corps.index('# Voix des mots isolés')
corps = corps[:debut] + VOIX + corps[fin:]

CIBLE.write_text(ENTETE + corps, encoding='utf-8')
print('écrit :', CIBLE.name, len(ENTETE + corps), 'octets')
