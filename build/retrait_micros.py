#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Retirer les micros de vérification de prononciation des modules.

    python3 build/retrait_micros.py --essai    # dit ce qu'il ferait
    python3 build/retrait_micros.py            # écrit

**La décision.** Un élève avait, un peu partout dans « Je découvre », un petit
micro par mot : il répétait, la reconnaissance vocale du navigateur jugeait.
Ces micros s'en vont. La seule façon de vérifier sa prononciation devient
l'outil « Prononcer » de la barre d'outils, qui fait écouter le modèle,
enregistre et laisse **l'élève** comparer — au lieu de rendre un verdict sur
un accent d'apprenant, ce qu'aucun moteur ne fait honnêtement.

**Ce qui ne bouge pas.** La production orale et le jeu de rôle gardent leur
micro : ce sont des tâches de parole, pas un jugement sur un mot. Ils
partagent `reconnaissanceLocale()` / `recoMessage()` avec le code retiré ici,
et cette plomberie reste donc en place. Les boutons « Écouter » restent
partout, ainsi que `CARRIER_PHRASES` : la phrase porteuse sert maintenant à la
synthèse, pas à la reconnaissance.

**Pourquoi un script et non 88 retouches.** Le gabarit et les 87 modules bâtis
portent le même code, au caractère près. Une retouche à la main, c'est 88
occasions de se tromper et aucune trace de ce qui a été fait. Chaque opération
ci-dessous **compte ce qu'elle trouve et refuse d'écrire** si le compte n'est
pas celui attendu : un motif qui ne correspond plus fait échouer le fichier,
il ne le laisse pas passer en silence.

Relançable : un fichier déjà nettoyé est signalé « déjà fait » et sauté.
"""
import glob
import os
import re
import sys

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GABARIT = os.path.join(RACINE, 'build', 'gabarit', 'module.html')
MODULES = os.path.join(RACINE, 'assets', 'interactive',
                       '*', '*-activite-interactive.html')

# Une règle CSS d'une seule ligne dont le sélecteur porte .pron-fb — le
# retour visuel du micro, qui n'a plus rien à afficher.
RE_CSS_PRONFB = re.compile(r'^[.\w\s\-]*\.pron-fb[\w.:\-()]*\s*\{[^{}]*\}$')

# La phrase porteuse survit au micro, mais plus pour la même raison : elle
# était là pour donner du contexte au moteur de reconnaissance, elle reste
# pour en donner à la synthèse.
COMMENTAIRE_PORTEUSE = """\
// Les mots à écouter sont présentés dans une courte phrase, le mot cible en
// gras, plutôt que seuls. La règle datait de la vérification de prononciation
// — un mot isolé, surtout d'une syllabe, était mal reconnu — et elle lui a
// survécu pour une autre raison, toujours valable : un mot français bref ne
// donne aucun indice de langue au moteur de synthèse et peut se faire lire à
// l'anglaise. La phrase porteuse est ce qu'on affiche et ce qu'on fait lire."""


class Ecart(Exception):
    pass


def _coupe_lignes(lignes, debut, fin, quoi):
    """Retire les lignes [debut, fin[ après avoir vérifié qu'on les tient."""
    if debut is None or fin is None:
        raise Ecart('bloc introuvable : %s' % quoi)
    return lignes[:debut] + lignes[fin:]


def _index(lignes, motif, quoi):
    trouves = [i for i, l in enumerate(lignes) if motif in l]
    if len(trouves) != 1:
        raise Ecart('%d ancre(s) au lieu d\'une pour %s' % (len(trouves), quoi))
    return trouves[0]


def _fin_de_fonction(lignes, debut):
    """L'index de la ligne qui referme la fonction ouverte à `debut`."""
    profondeur = 0
    for i in range(debut, len(lignes)):
        profondeur += lignes[i].count('{') - lignes[i].count('}')
        if i > debut or '{' in lignes[debut]:
            if profondeur <= 0:
                return i + 1
    raise Ecart('accolade jamais refermée à partir de la ligne %d' % debut)


def nettoyer(s):
    """Rend (texte nettoyé, journal des opérations)."""
    journal = []
    lignes = s.split('\n')

    # 1 · Les règles CSS du retour de prononciation.
    avant = len(lignes)
    lignes = [l for l in lignes if not RE_CSS_PRONFB.match(l.strip())]
    n = avant - len(lignes)
    if n < 7:
        raise Ecart('%d règle(s) .pron-fb retirée(s), au moins 7 attendues' % n)
    journal.append('%d règle(s) CSS .pron-fb' % n)

    # 2 · La classe du micro des cartes, seule sur sa ligne.
    avant = len(lignes)
    lignes = [l for l in lignes if l.strip() != '.ph-mic{margin-left:auto;flex-shrink:0}']
    if len(lignes) != avant - 1:
        raise Ecart('la règle .ph-mic n\'a pas été trouvée une fois et une seule')
    journal.append('la règle .ph-mic')

    s = '\n'.join(lignes)

    # 3 · .ph-mic partageait deux sélecteurs avec les pastilles de mots.
    for ancien, neuf, quoi in [
        ('.word-chip .btn,.ph-mic{', '.word-chip .btn{', 'sélecteur .ph-mic'),
        ('.word-chip .btn:hover,.ph-mic:hover{', '.word-chip .btn:hover{',
         'sélecteur .ph-mic:hover'),
        ('/* Icônes seules (haut-parleur, micro) : pas de cadre, juste l\'icône. */',
         '/* Icônes seules (haut-parleur) : pas de cadre, juste l\'icône. */',
         'commentaire des icônes seules'),
        ('// Icônes des boutons son/micro de "Je découvre" — change ces deux valeurs',
         '// Icône du bouton son de "Je découvre" — change cette valeur',
         'commentaire des icônes'),
    ]:
        if s.count(ancien) != 1:
            raise Ecart('%d occurrence(s) au lieu d\'une : %s' % (s.count(ancien), quoi))
        s = s.replace(ancien, neuf, 1)
    journal.append('4 sélecteurs et commentaires recomposés')

    lignes = s.split('\n')

    # 4 · La constante de l'icône : plus personne ne la lit.
    avant = len(lignes)
    lignes = [l for l in lignes if not l.startswith('const ICON_MIC = ')]
    if len(lignes) != avant - 1:
        raise Ecart('la constante ICON_MIC n\'a pas été trouvée une fois et une seule')
    journal.append('la constante ICON_MIC')

    # 5 · normPron, PRON_ALIASES et pronMatches : lus par pronCheck, et par
    #     lui seul. La production orale et le jeu de rôle ne comparent pas.
    debut = _index(lignes, '// ── VÉRIFICATION DE PRONONCIATION', 'l\'en-tête de section')
    fin = _index(lignes, '// RÈGLE (validée par l\'utilisateur', 'le commentaire de la règle')
    lignes = _coupe_lignes(lignes, debut, fin, 'normPron / PRON_ALIASES / pronMatches')
    journal.append('normPron, PRON_ALIASES, pronMatches')

    # 6 · Le commentaire de la règle est réécrit : la phrase porteuse reste,
    #     sa raison change.
    debut = _index(lignes, '// RÈGLE (validée par l\'utilisateur', 'le commentaire de la règle')
    fin = debut
    while fin < len(lignes) and lignes[fin].startswith('//'):
        fin += 1
    lignes = lignes[:debut] + COMMENTAIRE_PORTEUSE.split('\n') + lignes[fin:]
    journal.append('le commentaire de la phrase porteuse, réécrit')

    # 7 · La fonction elle-même.
    debut = _index(lignes, 'async function pronCheck(btn, expected){', 'pronCheck')
    lignes = _coupe_lignes(lignes, debut, _fin_de_fonction(lignes, debut), 'pronCheck')
    journal.append('la fonction pronCheck')

    # 8 · Les trois endroits qui posaient un micro. Chacun est repéré par la
    #     ligne qui appelle pronCheck, puis on remonte à `const mb=` quand le
    #     bouton est construit en plusieurs lignes.
    for _ in range(3):
        appels = [i for i, l in enumerate(lignes) if 'pronCheck(' in l]
        if not appels:
            break
        i = appels[0]
        if lignes[i].lstrip().startswith("h+='<button"):
            lignes = lignes[:i] + lignes[i + 1:]          # une seule ligne
            continue
        debut = i
        while debut > 0 and 'const mb=document.createElement' not in lignes[debut]:
            debut -= 1
        if 'const mb=document.createElement' not in lignes[debut]:
            raise Ecart('bouton micro sans déclaration à la ligne %d' % i)
        fin = i + 1
        while fin < len(lignes) and 'appendChild(mb)' not in lignes[fin]:
            fin += 1
        if fin >= len(lignes):
            raise Ecart('bouton micro jamais posé dans la page, ligne %d' % i)
        lignes = lignes[:debut] + lignes[fin + 1:]
    # 9 · Le commentaire de la règle CSS retirée en 1, resté orphelin.
    orphelin = '/* Le retour de prononciation est inséré après le micro, DANS .ph-top :'
    debut = _index(lignes, orphelin, 'le commentaire du retour de prononciation')
    fin = debut
    while fin < len(lignes) and '*/' not in lignes[fin]:
        fin += 1
    lignes = _coupe_lignes(lignes, debut, fin + 1, 'commentaire orphelin')
    journal.append('un commentaire resté orphelin')

    restant = [l for l in lignes if 'pronCheck' in l or 'ICON_MIC' in l or 'ph-mic' in l]
    if restant:
        raise Ecart('il reste %d trace(s) du micro : %s'
                    % (len(restant), restant[0].strip()[:70]))
    journal.append('les 3 boutons micro')

    return '\n'.join(lignes), journal


def deja_fait(s):
    return 'pronCheck' not in s


def main():
    essai = '--essai' in sys.argv
    fichiers = [GABARIT] + sorted(glob.glob(MODULES))
    faits = sautes = 0
    for f in fichiers:
        s = open(f, encoding='utf-8').read()
        nom = os.path.relpath(f, RACINE)
        if deja_fait(s):
            sautes += 1
            continue
        try:
            neuf, journal = nettoyer(s)
        except Ecart as e:
            print('  ÉCART  %-64s %s' % (nom, e))
            return 1
        if not essai:
            open(f, 'w', encoding='utf-8').write(neuf)
        faits += 1
        if faits == 1:
            for op in journal:
                print('     · %s' % op)
    print('%s%d fichier(s) nettoyé(s), %d déjà fait(s)'
          % ('[essai] ' if essai else '', faits, sautes))
    return 0


if __name__ == '__main__':
    sys.exit(main())
