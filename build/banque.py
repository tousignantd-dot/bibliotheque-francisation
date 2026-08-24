#!/usr/bin/env python3
"""La banque d'exercices — le registre, la construction, le contrôle. Tous niveaux.

    python3 build/banque.py                 → reconstruit toute la banque
    python3 build/banque.py --niveau 3      → seulement le niveau 3
    python3 build/banque.py --verifier      → contrôle sans écrire (code 1 sur écart)
    python3 build/banque.py --etat          → l'état de la banque, en clair
    python3 build/banque.py --etat --niveau 5

Ce fichier remplace `build/banque_n1.py`, qui ne savait compter qu'un niveau.
Il ne produit rien lui-même : il appelle les générateurs et rapporte.

Le registre n'est pas une liste
-------------------------------
La version niveau 1 tenait ses vingt et un ateliers dans deux tables écrites à
la main — une dans `banque_n1.py`, une dans chaque générateur. À sept niveaux,
ces tables auraient menti au premier oubli, exactement comme un plan qu'on met
à jour à la main.

Ici, **un atelier se déclare lui-même**, dans son propre `contenu.json` :

    "slug": "question-n1", "niveau": 1, "generateur": "phrase", "activite": 131

Le registre est le balayage de `assets/interactive/*/contenu.json`. Ajouter un
atelier, c'est déposer un fichier de contenu ; rien à inscrire ailleurs, rien
à tenir synchronisé. La clé `generateur` est l'opt-in : un `contenu.json` qui
ne la porte pas (il en existe d'autres dans le dépôt) n'entre pas dans la
banque.

`activite` est le **numéro réservé**, pas une promesse de catalogue : les six
ateliers d'écoute portent 140 à 145 depuis le premier jour et restent hors de
`data/activities.json` tant que leurs MP3 n'existent pas. La différence entre
« réservé » et « offert » est justement ce que `--etat` vérifie.

`polices-n1` (124) est le seul atelier hors registre : son contenu est une
**liste** dans `mots.json`, antérieure au format commun, et son générateur
`build/polices.py` calcule ses faces au lieu de les lire. Il est compté par
`HORS_REGISTRE` plutôt que réécrit — c'est une activité livrée et vérifiée.

Les quatre contrôles (inchangés depuis le niveau 1)
---------------------------------------------------
1. Les HTML sont à jour — chaque générateur compare son rendu au disque.
2. Tout ce qui est jouable est offert au catalogue.
3. Rien d'injouable n'est offert : un atelier d'écoute sans MP3 est offert
   cassé, sans issue, dans un banc qui n'a ni date ni état.
4. Le repérage est celui du niveau — couleur, catégorie « atelier », libellé.
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
sys.path.insert(0, str(BUILD))

# Une famille = une forme d'exercice = un générateur. L'ordre est celui de la
# progression : on apparie avant de construire, on construit avant de lire un
# texte. Il gouverne l'affichage de --etat et l'ordre de construction.
FAMILLES = [
    ('appariement', 'A · apparier'),
    ('oreille',     'B · écouter'),
    ('phrase',      'C · construire'),
    ('graphie',     'D · écrire'),
    ('texte',       'E · lire un texte'),
    ('conjugaison', 'F · conjuguer'),
]
NOM_FAMILLE = dict(FAMILLES)
# `polices-n1` n'est pas une famille : c'est l'atelier d'avant le format
# commun, gardé pour l'affichage de --etat.
NOM_FAMILLE['polices'] = 'A · apparier (avant le format commun)'
ORDRE_FAMILLE = {g: i for i, (g, _) in enumerate(FAMILLES)}

# Les familles dont l'extrait *est* la question : sans MP3, elles n'ont pas de
# contenu, elles ne sont pas « muettes ».
SONORES = {'oreille'}

# L'atelier d'avant le format commun. (slug, niveau, générateur, activité).
HORS_REGISTRE = [('polices-n1', 1, 'polices', 124)]


def palette():
    """Les huit couleurs de repérage, lues dans le système de design."""
    from couleurs_niveau import palette as p
    return p()


def registre(generateur=None, niveau=None):
    """Les ateliers déclarés sur le disque, triés par niveau puis famille."""
    trouves = []
    for dossier in sorted(INTER.iterdir()):
        fichier = dossier / 'contenu.json'
        if not fichier.is_dir() and fichier.exists():
            try:
                c = json.loads(io.open(fichier, encoding='utf-8').read())
            except (ValueError, UnicodeDecodeError):
                continue
            if not isinstance(c, dict) or 'generateur' not in c:
                continue
            if c.get('slug') != dossier.name:
                sys.exit('!! %s : le slug du contenu dit « %s »'
                         % (dossier.name, c.get('slug')))
            if c['generateur'] not in NOM_FAMILLE:
                sys.exit('!! %s : générateur inconnu « %s »'
                         % (dossier.name, c['generateur']))
            if not isinstance(c.get('niveau'), int):
                sys.exit('!! %s : le niveau manque ou n\'est pas un entier'
                         % dossier.name)
            trouves.append({
                'slug': dossier.name,
                'niveau': c['niveau'],
                'generateur': c['generateur'],
                'activite': c.get('activite'),
                'titre': c.get('titre', ''),
                'savoirs': c.get('savoirs', []),
                'items': c.get('items', []),
            })
    for slug, niv, gen, num in HORS_REGISTRE:
        items, savoirs = contenu_hors_format(slug)
        trouves.append({'slug': slug, 'niveau': niv, 'generateur': gen,
                        'activite': num, 'titre': slug, 'savoirs': savoirs,
                        'items': items})
    if generateur:
        trouves = [t for t in trouves if t['generateur'] == generateur]
    if niveau:
        trouves = [t for t in trouves if t['niveau'] == niveau]
    trouves.sort(key=lambda t: (t['niveau'],
                                ORDRE_FAMILLE.get(t['generateur'], 9),
                                t['activite'] if t['activite'] else 9999,
                                t['slug']))
    return trouves


def contenu_hors_format(slug):
    """Le contenu de `polices-n1`, qui vit dans une liste, pas dans un objet."""
    f = INTER / slug / 'mots.json'
    if not f.exists():
        return [], []
    brut = json.loads(io.open(f, encoding='utf-8').read())
    if isinstance(brut, list):
        return brut, []
    return brut.get('items', []), brut.get('savoirs', [])


def option_niveau(argv):
    """Retire `--niveau N` de la ligne de commande et rend (niveau, argv).

    Sans ça, le « 3 » de `--niveau 3` serait pris pour un filtre de slug par
    les générateurs, qui traitent tout argument nu comme un nom d'atelier.
    """
    if '--niveau' not in argv:
        return None, argv
    i = argv.index('--niveau')
    if i + 1 >= len(argv):
        sys.exit('!! --niveau attend un chiffre de 1 à 8')
    return int(argv[i + 1]), argv[:i] + argv[i + 2:]


def paires_pour(generateur, niveau=None):
    """Ce que les générateurs consomment : [(slug, numéro d'activité), …]."""
    return [(e['slug'], e['activite']) for e in registre(generateur, niveau)]


def audio_complet(slug, items):
    return all((INTER / slug / it['audio']).exists()
               for it in items if isinstance(it, dict) and it.get('audio'))


def etat(niveau=None):
    acts = {x['id']: x for x in json.loads(io.open(ACTIVITES, encoding='utf-8').read())}
    par_slug = {}
    for x in acts.values():
        chemin = x.get('interactive') or ''
        if chemin.startswith('assets/interactive/'):
            par_slug[chemin.split('/')[2]] = x
    couleurs = palette()

    entrees = registre(niveau=niveau)
    if not entrees:
        print('Aucun atelier%s.' % (' au niveau %d' % niveau if niveau else ''))
        return 0

    ecarts, lignes = [], []
    total = jouables = catalogues = 0
    savoirs_par_niveau = {}
    niveau_courant = famille_courante = None

    for e in entrees:
        slug, niv, gen = e['slug'], e['niveau'], e['generateur']
        if niv != niveau_courant:
            lignes.append('')
            lignes.append('━━ Niveau %d' % niv)
            niveau_courant, famille_courante = niv, None
        if gen != famille_courante:
            lignes.append('')
            lignes.append('  ' + NOM_FAMILLE.get(gen, gen))
            famille_courante = gen

        total += 1
        savoirs_par_niveau.setdefault(niv, set()).update(e['savoirs'])
        html = INTER / slug / ('%s-activite-interactive.html' % slug)
        act = par_slug.get(slug)
        son = audio_complet(slug, e['items'])
        besoin_son = gen in SONORES
        pret = son or not besoin_son
        jouables += 1 if pret else 0
        catalogues += 1 if act else 0

        marque = '✓' if (pret and act) else ('·' if pret else '⏸')
        lignes.append('    %s %-20s %2d items · %s · %s · %s'
                      % (marque, slug, len(e['items']),
                         'html' if html.exists() else 'PAS DE HTML',
                         'audio complet' if son else 'audio à produire',
                         ('activité %s' % act['id'] if act
                          else 'réservé %s' % (e['activite'] or '—'))))

        if not html.exists():
            ecarts.append('%s : le HTML n\'est pas construit' % slug)
        if act and besoin_son and not son:
            ecarts.append('%s : au catalogue SANS ses MP3 — il serait offert '
                          'cassé dans le banc des exercices libres' % slug)
        if pret and not act:
            ecarts.append('%s : jouable mais absent de data/activities.json' % slug)
        if act:
            attendue = couleurs[niv][0]
            if (act.get('nouveauDesignColor') or '').upper() != attendue:
                ecarts.append('%s : couleur %s au lieu de %s, le repérage du niveau %d'
                              % (slug, act.get('nouveauDesignColor'), attendue, niv))
            if act.get('categorie') != 'atelier':
                ecarts.append('%s : catégorie « %s » au lieu d\'atelier'
                              % (slug, act.get('categorie')))
            if act.get('level') != 'Niveau %d' % niv:
                ecarts.append('%s : niveau « %s » au catalogue, %d dans le contenu'
                              % (slug, act.get('level'), niv))
        if e['activite'] and act and act['id'] != e['activite']:
            ecarts.append('%s : réservé %s, publié sous %s'
                          % (slug, e['activite'], act['id']))

    print('\n'.join(lignes))
    print('\n%d ateliers · %d jouables · %d au catalogue' % (total, jouables, catalogues))
    for niv in sorted(savoirs_par_niveau):
        vus = savoirs_par_niveau[niv]
        print('  niveau %d — %d savoirs touchés : %s'
              % (niv, len(vus), ' '.join(sorted(vus)) if vus else '—'))
    if ecarts:
        print('\nÉCARTS :')
        for x in ecarts:
            print('  !! ' + x)
    else:
        print('\nAucun écart.')
    return 1 if ecarts else 0


def lancer(args, niveau=None):
    """Passe la main aux générateurs qui ont du contenu, rend le pire code."""
    pire = 0
    for gen, nom in FAMILLES:
        if not registre(gen, niveau):
            continue
        script = BUILD / ('%s.py' % gen)
        if not script.exists():
            continue
        print('── %s' % nom)
        sys.stdout.flush()   # sinon l'en-tête sort après la sortie du sous-processus
        supp = ['--niveau', str(niveau)] if niveau else []
        r = subprocess.run([sys.executable, str(script)] + args + supp, cwd=str(ROOT))
        pire = max(pire, r.returncode)
    return pire


def main(argv):
    niveau = None
    if '--niveau' in argv:
        i = argv.index('--niveau')
        if i + 1 >= len(argv):
            sys.exit('!! --niveau attend un chiffre de 1 à 8')
        niveau = int(argv[i + 1])
        argv = argv[:i] + argv[i + 2:]
    if '--etat' in argv:
        return etat(niveau)
    code = lancer(['--verifier'] if '--verifier' in argv else [], niveau)
    print()
    return max(code, etat(niveau))


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
