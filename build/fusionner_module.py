#!/usr/bin/env python3
"""Fusionner la branche d'un agent sans refaire trente fois le même geste.

    python3 build/fusionner_module.py worktree-agent-abc123
    python3 build/fusionner_module.py origin/cloud-act-85

Produire un module en parallèle finit toujours par le même conflit : deux
agents ajoutent une entrée au même endroit d'un fichier partagé. En une nuit,
la même résolution a été refaite dix fois à la main. Chaque fois, la tentation
est de recoller les deux moitiés — et c'est ainsi qu'on fabrique une activité
chimère, avec le titre de l'un et les mots-clés de l'autre, que rien ne
signale ensuite.

Trois familles de fichiers, trois traitements :

· **`data/activities.json`** — fusionné **par identifiant**, jamais par texte.
  Git voit deux objets ajoutés au même rang du tableau et rend un conflit
  ligne à ligne qui mélange les champs. On relit les deux versions, on garde
  toutes les activités des deux côtés, et on refuse un identifiant en double.

· **`data/sections.json` et `data/materiel.json`** — ce sont des relevés, pas
  des sources. On ne les fusionne pas : on les **régénère**. (Leur champ
  `majLe` vient de la date des fichiers, qu'un worktree neuf redate tous : le
  conflit est du bruit à 90 %.)

· **`server.py` et `build/powerpoints/modules.py`** — les deux côtés ajoutent
  un bloc, et git coupe au milieu de la structure : la ligne qui ferme le
  dernier bloc se retrouve en contexte commun **après** le marqueur. La
  résolution est donc « le nôtre + la fermeture + le leur ». C'est une
  heuristique, et elle ne serait pas acceptable seule — d'où la **vérification
  systématique** : le fichier doit se compiler, et tout nom de premier niveau
  ajouté par l'un ou l'autre côté doit se retrouver dans le résultat. Un
  recollage raté échoue bruyamment au lieu de passer.

Le script s'arrête net sur tout conflit qu'il ne sait pas traiter, sans rien
commiter : mieux vaut la main que le hasard.
"""
import ast
import json
import pathlib
import re
import subprocess
import sys

RACINE = pathlib.Path(__file__).resolve().parent.parent
RELEVES = {'data/sections.json': 'build/sections.py',
           'data/materiel.json': 'build/materiel.py'}
PYTHON_PARTAGES = ('server.py', 'build/powerpoints/modules.py')
# Les journaux du chantier : on y écrit à la suite, jamais on n'y arbitre.
JOURNAUX = ('docs/vagues-suivantes.md', 'docs/verification-originalite.md')


def git(*args, verifier=True):
    r = subprocess.run(['git'] + list(args), cwd=RACINE,
                       capture_output=True, text=True)
    if verifier and r.returncode:
        raise RuntimeError('git %s : %s' % (' '.join(args), r.stderr.strip()))
    return r


def noms_premier_niveau(source):
    """Les noms assignés au premier niveau du module — ce qu'un bloc ajoute."""
    try:
        arbre = ast.parse(source)
    except SyntaxError:
        return set()
    noms = set()
    for n in arbre.body:
        if isinstance(n, ast.Assign):
            for c in n.targets:
                if isinstance(c, ast.Name):
                    noms.add(c.id)
    return noms


def cles_de_dictionnaires(source):
    """Les clés littérales de dictionnaire — « horaire », « guichet »…

    Un scénario de jeu de rôle n'est pas un nom de premier niveau : c'est une
    clé dans un grand dictionnaire. Le perdre est exactement le genre de
    disparition silencieuse que ce script existe pour empêcher.
    """
    return set(re.findall(r'^\s{4}[\'"]([a-z0-9_-]+)[\'"]\s*:\s*\{', source,
                          re.MULTILINE))


def fusionner_catalogue(branche):
    """Toutes les activités des deux côtés, aucun identifiant en double."""
    def lire(ref):
        return json.loads(git('show', ref + ':data/activities.json').stdout)
    notre, leur = lire('HEAD'), lire(branche)
    connus = {a['id'] for a in notre}
    ajouts = [a for a in leur if a['id'] not in connus]
    fusion = sorted(notre + ajouts, key=lambda a: a['id'])
    ids = [a['id'] for a in fusion]
    if len(ids) != len(set(ids)):
        raise RuntimeError('identifiant en double dans le catalogue fusionné')
    chemin = RACINE / 'data' / 'activities.json'
    chemin.write_text(json.dumps(fusion, ensure_ascii=False, indent=2) + '\n',
                      encoding='utf-8')
    return [a['id'] for a in ajouts]


def fusionner_journal(chemin):
    """Deux sections ajoutées au même endroit d'un journal : on garde les deux.

    `docs/vagues-suivantes.md` est un journal — on y écrit à la suite. Quand
    deux agents livrent le même jour, git voit deux ajouts au même rang et
    rend un conflit, alors qu'il n'y a rien à arbitrer : les deux sections
    doivent y être, dans l'ordre. Fait à la main trois fois en une journée.

    L'ordre choisi est « le nôtre, puis le leur », c'est-à-dire l'ordre
    d'arrivée sur `main`. Et le résultat est **vérifié** : toute ligne présente
    d'un côté ou de l'autre doit se retrouver dans le texte final. Un
    recollage qui perdrait le compte rendu d'un agent échoue bruyamment plutôt
    que de l'effacer en silence.
    """
    f = RACINE / chemin
    lignes = f.read_text(encoding='utf-8').split('\n')
    attendues = [l for l in lignes if not l.startswith(('<<<<<<<', '=======',
                                                        '>>>>>>>'))]
    while True:
        debuts = [i for i, l in enumerate(lignes) if l.startswith('<<<<<<<')]
        if not debuts:
            break
        d = debuts[-1]
        m = next(i for i in range(d, len(lignes)) if lignes[i].startswith('======='))
        fin = next(i for i in range(m, len(lignes)) if lignes[i].startswith('>>>>>>>'))
        lignes = lignes[:d] + lignes[d + 1:m] + lignes[m + 1:fin] + lignes[fin + 1:]
    resultat = '\n'.join(lignes)
    manquantes = [l for l in attendues if l.strip() and l not in lignes]
    if manquantes:
        raise RuntimeError('%s : le recollage perdrait %d ligne(s), dont : %r'
                           % (chemin, len(manquantes), manquantes[0][:70]))
    f.write_text(resultat, encoding='utf-8')


def fusionner_python(chemin, branche):
    """« Le nôtre + la fermeture + le leur », puis on vérifie que c'est vrai."""
    f = RACINE / chemin
    lignes = f.read_text(encoding='utf-8').split('\n')
    attendus = (noms_premier_niveau(git('show', 'HEAD:' + chemin).stdout)
                | noms_premier_niveau(git('show', branche + ':' + chemin).stdout))
    cles = (cles_de_dictionnaires(git('show', 'HEAD:' + chemin).stdout)
            | cles_de_dictionnaires(git('show', branche + ':' + chemin).stdout))

    while True:
        debuts = [i for i, l in enumerate(lignes) if l.startswith('<<<<<<<')]
        if not debuts:
            break
        d = debuts[-1]                       # du bas vers le haut : les index
        m = next(i for i in range(d, len(lignes))    # du haut restent valides
                 if lignes[i].startswith('======='))
        fin = next(i for i in range(m, len(lignes))
                   if lignes[i].startswith('>>>>>>>'))
        # La fermeture est la suite de lignes qui suit le marqueur et qui ne
        # fait que fermer des structures : elles appartiennent aux deux côtés.
        queue = []
        for l in lignes[fin + 1:]:
            if re.fullmatch(r'\s*[\]\}\),]+\s*', l) and l.strip():
                queue.append(l)
            else:
                break
        # Puis la respiration : les lignes vides qui suivent la fermeture
        # appartiennent au bloc qu'on vient de refermer. Sans elles, deux
        # affectations de premier niveau se retrouvent collées l'une à
        # l'autre — le fichier marche, il se lit mal, et le prochain diff est
        # sale pour rien.
        for l in lignes[fin + 1 + len(queue):]:
            if l.strip() == '' and len(queue) < 8:
                queue.append(l)
            else:
                break
        if not queue:
            raise RuntimeError(
                '%s : conflit sans fermeture commune repérable (ligne %d) — '
                'à résoudre à la main' % (chemin, d + 1))
        lignes = (lignes[:d] + lignes[d + 1:m] + queue
                  + lignes[m + 1:fin] + lignes[fin + 1:])

    resultat = '\n'.join(lignes)
    try:
        ast.parse(resultat)
    except SyntaxError as e:
        raise RuntimeError('%s : le recollage ne compile pas (%s)' % (chemin, e))
    manquants = attendus - noms_premier_niveau(resultat)
    if manquants:
        raise RuntimeError('%s : le recollage a perdu %s'
                           % (chemin, ', '.join(sorted(manquants))))
    perdues = cles - cles_de_dictionnaires(resultat)
    if perdues:
        raise RuntimeError('%s : le recollage a perdu les clés %s'
                           % (chemin, ', '.join(sorted(perdues))))
    f.write_text(resultat, encoding='utf-8')


def main():
    if len(sys.argv) != 2:
        print(__doc__.split('\n\n')[1].strip())
        return 2
    branche = sys.argv[1]
    # `--untracked-files=no` : un dossier non suivi qui traîne à côté ne
    # gêne aucune fusion, et refuser de travailler pour ça obligeait à
    # commiter n'importe quoi en vitesse — exactement ce qu'on veut
    # éviter juste avant de toucher à des fichiers partagés.
    if git('status', '--porcelain', '--untracked-files=no').stdout.strip():
        print('✗ l’arbre de travail n’est pas propre — commite ou range d’abord')
        return 2

    fusion = git('merge', '--no-edit', branche, verifier=False)
    en_conflit = [l for l in git('diff', '--name-only', '--diff-filter=U')
                  .stdout.split('\n') if l.strip()]
    if not en_conflit:
        if fusion.returncode:
            print('✗ la fusion a échoué sans conflit de fichier :\n' + fusion.stderr)
            return 1
        print('✓ %s fusionnée sans conflit' % branche)
        return 0

    inconnus = [c for c in en_conflit
                if c not in RELEVES and c != 'data/activities.json'
                and c not in PYTHON_PARTAGES and c not in JOURNAUX]
    if inconnus:
        print('✗ conflits que ce script ne sait pas traiter, rien n’est '
              'commité :\n    ' + '\n    '.join(inconnus))
        print('  (`git merge --abort` pour revenir en arrière)')
        return 1

    try:
        traites = []
        if 'data/activities.json' in en_conflit:
            ajouts = fusionner_catalogue(branche)
            traites.append('catalogue : %d activité(s) ajoutée(s) %s'
                           % (len(ajouts), ajouts))
        for chemin in PYTHON_PARTAGES:
            if chemin in en_conflit:
                fusionner_python(chemin, branche)
                traites.append('%s : les deux blocs gardés, compilation et '
                               'clés vérifiées' % chemin)
        for chemin in JOURNAUX:
            if chemin in en_conflit:
                fusionner_journal(chemin)
                traites.append('%s : les deux sections gardées, aucune ligne '
                               'perdue' % chemin)
        for chemin, script in RELEVES.items():
            if chemin in en_conflit:
                git('checkout', '--theirs', '--', chemin, verifier=False)
                subprocess.run([sys.executable, script], cwd=RACINE,
                               capture_output=True)
                traites.append('%s : régénéré par %s' % (chemin, script))
    except RuntimeError as e:
        print('✗ %s' % e)
        print('  rien n’est commité — `git merge --abort` pour revenir en arrière')
        return 1

    git('add', '--', *en_conflit)
    restants = git('diff', '--name-only', '--diff-filter=U').stdout.strip()
    if restants:
        print('✗ conflits restants : ' + restants)
        return 1
    git('commit', '--no-edit')
    print('✓ %s fusionnée' % branche)
    for t in traites:
        print('    · ' + t)
    return 0


if __name__ == '__main__':
    sys.exit(main())
