#!/usr/bin/env python3
"""
Le cadre programme d'un module : ce qu'il faut savoir avant d'écrire une ligne.

    python3 build/cadre.py 4 sante            # cherche la situation « santé »
    python3 build/cadre.py 4 "Relations sociales"
    python3 build/cadre.py 4                  # liste les situations du niveau
    python3 build/cadre.py 4 sante --savoirs  # + les points de savoir en entier

Pourquoi ce fichier existe
--------------------------
`~/Claude/programme/programme-francisation.json` fait 600 Ko. Le charger en
entier pour cadrer un module coûte cher et invite à reconstituer de mémoire ce
qu'on aurait dû lire. Ce script en sort **une page** : la situation, ses
intentions de communication avec leurs compétences, son lexique, et les repères
de fin de cours. C'est la spécification ministérielle du module — le contenu,
lui, s'invente (voir la règle « contenu inventé, pas copié »).

Ce que le programme donne et ne donne pas
-----------------------------------------
Il donne la **spécification** : quelle compétence, quelle situation, quels
savoirs, quel lexique, quel critère de réussite. Il ne donne aucun scénario,
aucun personnage, aucun dialogue, aucun exercice. Ceux-là s'écrivent.

Trois défauts connus du dépouillement, traités ici plutôt que tus
-----------------------------------------------------------------
1. **Le lexique vient d'un autre document** que le programme — la « Progression
   du lexique » du CSS de Laval (juin 2020) — et nomme parfois les situations
   autrement. D'où `ALIAS_LEXIQUE`, explicite et commenté.
2. **Une entrée de lexique sans situation continue la précédente** : les
   trente-deux expressions « avoir mal » suivent « Consultation médicale ».
   Le script reporte la situation et le signale par « (rattachée) ».
3. **Trois entrées du niveau 4 sont de la bouillie d'extraction** : des
   consignes de grammaire ou d'orthographe classées en vocabulaire. Elles sont
   écartées par `_est_du_vocabulaire()` et comptées dans l'avertissement final,
   jamais supprimées en silence.
"""
import argparse
import json
import pathlib
import re
import sys
import unicodedata

PROGRAMME = pathlib.Path.home() / 'Claude/programme/programme-francisation.json'

# La « Progression du lexique » nomme quelques situations autrement que le
# programme d'études. Ce ne sont pas des fautes : ce sont deux documents.
ALIAS_LEXIQUE = {
    'Consultation médicale': 'Consultation d’un professionnel de la santé',
    'Orientation dans l’établissement (de formation)':
        'Communication avec le personnel de l’établissement',
}

# Ce qui trahit une cellule de tableau mal découpée : le texte prescrit un
# savoir au lieu de nommer du vocabulaire.
_PAS_DU_VOCABULAIRE = re.compile(
    r'^\s*[•·]|Orthographier|Reconnaître tous les caractères|'
    r'Connaître les termes qui servent')


def _est_du_vocabulaire(entree):
    return not _PAS_DU_VOCABULAIRE.search(entree)


def _pliable(s):
    """Minuscule sans accents, pour chercher « sante » et trouver « santé »."""
    s = unicodedata.normalize('NFD', s or '')
    s = ''.join(c for c in s if unicodedata.category(c) != 'Mn')
    return s.lower()


def charger(niveau):
    if not PROGRAMME.exists():
        sys.exit('!! programme introuvable : %s' % PROGRAMME)
    d = json.loads(PROGRAMME.read_text(encoding='utf-8'))
    for n in d['niveaux']:
        if n['niveau'] == niveau:
            return d, n
    sys.exit('!! niveau %s absent du programme (1 à 8)' % niveau)


def trouver_situation(n, requete):
    """La situation dont le nom contient la requête. Refuse l'ambiguïté."""
    q = _pliable(requete)
    exact = [s for s in n['situations'] if _pliable(s) == q]
    if exact:
        return exact[0]
    trouves = [s for s in n['situations'] if q in _pliable(s)]
    if len(trouves) == 1:
        return trouves[0]
    if not trouves:
        sys.exit('!! aucune situation du niveau %d ne contient %r.\n'
                 '   Lancer sans argument de situation pour voir la liste.'
                 % (n['niveau'], requete))
    sys.exit('!! %r désigne %d situations — préciser :\n%s'
             % (requete, len(trouves), '\n'.join('   · ' + s for s in trouves)))


def lexique_par_situation(n):
    """Le lexique rangé par situation, la règle de continuation appliquée.

    Rend `{situation: [(entree, rattachee)]}` et la liste des entrées écartées.
    """
    par_situation, ecartees, courante = {}, [], None
    for bloc in n['lexique']:
        brute = bloc.get('situation')
        rattachee = brute is None
        if brute:
            courante = ALIAS_LEXIQUE.get(brute, brute)
        if courante is None:
            continue                      # rien à quoi rattacher : on ignore
        for entree in bloc.get('entrees', []):
            if _est_du_vocabulaire(entree):
                par_situation.setdefault(courante, []).append((entree, rattachee))
            else:
                ecartees.append((courante, entree))
    return par_situation, ecartees


def _puce(texte, largeur=76, tete='  · ', suite='    '):
    """Une puce repliée, pour que la sortie tienne dans un terminal."""
    mots, lignes, ligne = texte.split(), [], tete
    for mot in mots:
        if len(ligne) + len(mot) + 1 > largeur and ligne.strip() not in ('·', ''):
            lignes.append(ligne.rstrip())
            ligne = suite
        ligne += mot + ' '
    lignes.append(ligne.rstrip())
    return '\n'.join(lignes)


def lister(n):
    print('Niveau %d — %s (%s, stade %s)\n' % (n['niveau'], n['titre'],
                                               n['code'], n['stade']))
    par_dom = {}
    for i in n['intentions']:
        if i.get('situation'):
            par_dom.setdefault(i['domaine'] or '(sans domaine)', {}) \
                   .setdefault(i['situation'], 0)
            par_dom[i['domaine'] or '(sans domaine)'][i['situation']] += 1
    print('%d situations, %d intentions :\n' % (len(n['situations']),
                                                len(n['intentions'])))
    for dom in sorted(par_dom):
        print('  %s' % dom)
        for sit, k in sorted(par_dom[dom].items(), key=lambda x: -x[1]):
            print('    %2d intention%s  %s' % (k, 's' if k > 1 else ' ', sit))
        print()
    orphelines = [i for i in n['intentions'] if not i.get('situation')]
    if orphelines:
        print('  Hors situation (%d) :' % len(orphelines))
        for i in orphelines:
            print('    · %s [%s]' % (i['intention'], '/'.join(i['competences'])))


def cadre(d, n, situation, avec_savoirs=False):
    noms_comp = {c['id']: c['nom'] for c in d['competences']}
    intentions = [i for i in n['intentions'] if i.get('situation') == situation]
    domaine = next((i['domaine'] for i in intentions if i.get('domaine')), '—')

    print('═' * 78)
    print('CADRE PROGRAMME — %s' % situation)
    print('Niveau %d · %s · %s · stade %s' % (n['niveau'], n['code'],
                                              n['titre'], n['stade']))
    print('Domaine général de formation : %s' % domaine)
    print('═' * 78)

    print('\nINTENTIONS DE COMMUNICATION (%d)\n' % len(intentions))
    par_comp = {}
    for i in intentions:
        for c in i['competences']:
            par_comp.setdefault(c, []).append(i['intention'])
    for cid in ('co', 'po', 'ce', 'pe'):
        if cid in par_comp:
            print('  %s (%d)' % (noms_comp.get(cid, cid), len(par_comp[cid])))
            for texte in par_comp[cid]:
                print(_puce(texte, tete='    · ', suite='      '))
            print()

    lex, ecartees = lexique_par_situation(n)
    entrees = lex.get(situation, [])
    print('LEXIQUE (%d entrées)' % len(entrees))
    if not entrees:
        print('  Aucune entrée pour cette situation.')
        print('  Le lexique vient d\'un autre document que le programme et ne')
        print('  couvre pas les dix-sept situations. À composer soi-même à')
        print('  partir des intentions ci-dessus.')
    else:
        print()
        for texte, rattachee in entrees:
            print(_puce(texte + (' (rattachée)' if rattachee else '')))
    print()

    print('SAVOIRS DU COURS (%d, communs à tout le niveau)\n' % len(n['savoirs']))
    par_cat = {}
    for s in n['savoirs']:
        par_cat.setdefault(s['categorie'], []).append(s)
    noms_cat = {c['id']: c['nom'] for c in d['categoriesSavoirs']}
    for cid, liste in par_cat.items():
        total = sum(len(s.get('points', [])) for s in liste)
        print('  %s — %d savoirs, %d points' % (noms_cat.get(cid, cid),
                                                len(liste), total))
        for s in liste:
            print('      %s (%d)' % (s['titre'], len(s.get('points', []))))
            if avec_savoirs:
                for p in s.get('points', []):
                    print(_puce(p['texte'], tete='        - ', suite='          '))
        print()
    if not avec_savoirs:
        print('  (--savoirs pour les points en entier)\n')

    for cle, titre in (('attentesFinDeCours', 'ATTENTES DE FIN DE COURS'),
                       ('criteresEvaluation', "CRITÈRES D'ÉVALUATION")):
        blocs = n.get(cle) or []
        if blocs:
            print('%s\n' % titre)
            for b in blocs:
                for p in (b.get('points') or [b.get('texte', '')]):
                    if p:
                        print(_puce(p))
            print()

    if ecartees:
        print('─' * 78)
        print('%d entrée(s) de lexique écartée(s) : consignes de grammaire ou '
              'd\'orthographe' % len(ecartees))
        print('classées en vocabulaire par le dépouillement du PDF. '
              'Défaut connu de la source.')

    print('─' * 78)
    print('Le programme donne la spécification, jamais le contenu. Scénario,')
    print('personnages, dialogues et exercices s\'inventent — rien ne se copie')
    print('d\'un manuel.')


def main():
    p = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument('niveau', type=int, help='1 à 8')
    p.add_argument('situation', nargs='?',
                   help='tout ou partie du nom ; absent, liste les situations')
    p.add_argument('--savoirs', action='store_true',
                   help='déplier les points de savoir')
    a = p.parse_args()

    d, n = charger(a.niveau)
    if not a.situation:
        lister(n)
    else:
        cadre(d, n, trouver_situation(n, a.situation), a.savoirs)


if __name__ == '__main__':
    main()
