#!/usr/bin/env python3
"""La banque du niveau 1 — construction et contrôle d'ensemble.

Vingt ateliers, trois générateurs, un seul point d'entrée. Ce fichier ne
produit rien lui-même : il appelle les trois autres et rapporte l'état de la
banque en une page.

    python3 build/banque_n1.py             → reconstruit les vingt ateliers
    python3 build/banque_n1.py --verifier  → contrôle sans écrire (code 1 sur écart)
    python3 build/banque_n1.py --etat      → l'état de la banque, en clair

Pourquoi ce fichier existe
--------------------------
`docs/plan-exercices-niveau-1.md` annonce vingt-deux exercices en quatre
familles. Rien, dans le dépôt, ne disait si on y était — il fallait lancer
trois scripts, lire `data/activities.json` et compter les MP3 à la main. Un
plan qu'on ne peut pas confronter au disque devient faux sans qu'on s'en
aperçoive.

`--verifier` sort en code 1 sur écart, comme les six contrôles de `CLAUDE.md`,
et s'enchaîne donc avec eux dans un `&&`.

Les quatre contrôles
--------------------
1. **Les HTML sont à jour** — chaque générateur compare son rendu au fichier
   sur le disque. Un contenu modifié sans reconstruction est un écart.
2. **Le catalogue dit vrai** — toute activité de la banque inscrite dans
   `data/activities.json` pointe vers un fichier qui existe, et tout atelier
   construit et jouable est inscrit.
3. **Rien d'injouable n'est offert** — un atelier de la famille B sans ses MP3
   ne doit PAS être au catalogue : le banc des exercices libres est toujours
   ouvert, donc l'y mettre l'offrirait cassé, sans issue pour l'élève.
4. **Le repérage est celui du niveau 1** — framboise, et la catégorie est
   `atelier`. Un atelier qui sort avec la couleur d'un autre niveau se voit
   tout de suite au portail, et jamais avant.
"""
import io
import json
import pathlib
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
BUILD = ROOT / 'build'
INTER = ROOT / 'assets/interactive'
ACTIVITES = ROOT / 'data/activities.json'

FRAMBOISE = '#A5335F'
MOT_CLE = 'banque niveau 1'

# Les trois générateurs, et l'atelier livré avant eux qui garde le sien.
GENERATEURS = ['polices.py', 'appariement.py', 'phrase.py', 'oreille.py', 'graphie.py']

# Ce que le plan annonce, famille par famille. C'est la seule liste écrite à
# la main de ce fichier : tout le reste se déduit du disque.
FAMILLES = {
    'A · apparier':   ['polices-n1', 'heure-n1', 'abreviations-n1', 'dates-n1',
                       'chiffres-n1', 'panneaux-n1', 'lettres-n1'],
    'B · écouter':    ['voyelles-n1', 'consonnes-n1', 'e-muet-n1', 'intonation-n1',
                       'formes-rapides-n1', 'jean-dit-n1'],
    'C · construire': ['phrase-ordre-n1', 'question-n1', 'negatif-n1', 'possessifs-n1',
                       'feminin-n1', 'nombres-phrase-n1', 'syllabes-n1'],
    'D · écrire':     ['recopier-n1'],
}


def contenu_de(slug):
    """Le contenu d'un atelier, quel que soit le nom de son fichier.

    `polices-n1` porte le sien dans `mots.json` : il est antérieur au format
    commun, et le renommer casserait une activité livrée et vérifiée.
    """
    for nom, cle in (('contenu.json', 'items'), ('mots.json', None)):
        f = INTER / slug / nom
        if f.exists():
            brut = json.loads(io.open(f, encoding='utf-8').read())
            items = brut if isinstance(brut, list) else brut.get('items', [])
            savoirs = [] if isinstance(brut, list) else brut.get('savoirs', [])
            return items, savoirs
    return None, None


def audio_complet(slug, items):
    return all((INTER / slug / it['audio']).exists() for it in items if it.get('audio'))


def etat():
    acts = {x['id']: x for x in json.loads(io.open(ACTIVITES, encoding='utf-8').read())}
    par_slug = {}
    for x in acts.values():
        chemin = x.get('interactive') or ''
        if chemin.startswith('assets/interactive/'):
            par_slug[chemin.split('/')[2]] = x

    ecarts, lignes = [], []
    total = jouables = catalogues = 0
    savoirs_vus = set()

    for famille, slugs in FAMILLES.items():
        lignes.append('')
        lignes.append(famille)
        for slug in slugs:
            total += 1
            items, savoirs = contenu_de(slug)
            if items is None:
                lignes.append('  ✗ %-18s contenu absent' % slug)
                ecarts.append('%s : pas de contenu' % slug)
                continue
            savoirs_vus |= set(savoirs)
            html = INTER / slug / ('%s-activite-interactive.html' % slug)
            act = par_slug.get(slug)
            son = audio_complet(slug, items)
            besoin_son = famille.startswith('B')
            pret = son or not besoin_son
            if pret:
                jouables += 1
            if act:
                catalogues += 1

            marque = '✓' if (pret and act) else ('·' if pret else '⏸')
            lignes.append('  %s %-18s %2d items · %s · %s · %s'
                          % (marque, slug, len(items),
                             'html' if html.exists() else 'PAS DE HTML',
                             ('audio complet' if son else 'audio à produire'),
                             ('activité %d' % act['id'] if act else 'hors catalogue')))

            if not html.exists():
                ecarts.append('%s : le HTML n\'est pas construit' % slug)
            # Contrôle 3 : rien d'injouable ne doit être offert.
            if act and besoin_son and not son:
                ecarts.append('%s : au catalogue SANS ses MP3 — il serait offert '
                              'cassé dans le banc des exercices libres' % slug)
            # Contrôle 2 : tout ce qui est jouable doit être offert.
            if pret and not act:
                ecarts.append('%s : jouable mais absent de data/activities.json' % slug)
            # Contrôle 4 : le repérage du niveau 1.
            if act:
                if act.get('nouveauDesignColor') != FRAMBOISE:
                    ecarts.append('%s : couleur %s au lieu de la framboise du niveau 1'
                                  % (slug, act.get('nouveauDesignColor')))
                if act.get('categorie') != 'atelier':
                    ecarts.append('%s : catégorie « %s » au lieu d\'atelier'
                                  % (slug, act.get('categorie')))
                if act.get('level') != 'Niveau 1':
                    ecarts.append('%s : niveau « %s »' % (slug, act.get('level')))

    print('\n'.join(lignes))
    print('\n%d ateliers · %d jouables · %d au catalogue' % (total, jouables, catalogues))
    print('%d savoirs du programme touchés : %s'
          % (len(savoirs_vus), ' '.join(sorted(savoirs_vus))))
    if ecarts:
        print('\nÉCARTS :')
        for e in ecarts:
            print('  !! ' + e)
    else:
        print('\nAucun écart.')
    return 1 if ecarts else 0


def lancer(args):
    """Passe la main aux trois générateurs, et rend le pire code de sortie."""
    pire = 0
    for g in GENERATEURS:
        print('── %s' % g)
        r = subprocess.run([sys.executable, str(BUILD / g)] + args, cwd=str(ROOT))
        pire = max(pire, r.returncode)
    return pire


def main(argv):
    if '--etat' in argv:
        return etat()
    code = lancer(['--verifier'] if '--verifier' in argv else [])
    print()
    return max(code, etat())


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
