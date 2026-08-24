#!/usr/bin/env python3
"""Inscrire au catalogue les ateliers de la banque qui sont jouables.

    python3 build/inscrire_ateliers.py            → inscrit ce qui manque
    python3 build/inscrire_ateliers.py --niveau 3 → seulement ce niveau
    python3 build/inscrire_ateliers.py --essai    → dit ce qu'il ferait, n'écrit pas

Pourquoi ce fichier existe
--------------------------
`data/activities.json` est un fichier **partagé** : deux sessions y écrivent,
et la règle du dépôt est d'y toucher une fois, avec des chemins explicites.
Inscrire soixante ateliers à la main, c'est soixante occasions de se tromper
d'une couleur ou d'un libellé de niveau — et `build/banque.py --etat` les
refuserait un par un.

Ici, la fiche du catalogue est **déduite du contenu de l'atelier** : le titre,
le niveau, la couleur de repérage (celle du niveau, jamais choisie à la main),
les savoirs en mots-clés. Le script est idempotent : relancé, il ne change
rien à ce qui est déjà juste.

Deux refus, plutôt qu'un écrasement
-----------------------------------
· un numéro déjà pris par **autre chose** que cet atelier : le script
  s'arrête et le dit. C'est le cas qui perdrait le travail d'une autre
  session ;
· un atelier **injouable** — un atelier d'écoute sans ses MP3 : il resterait
  offert cassé dans un banc qui n'a ni date ni état. C'est la règle du
  niveau 1, et elle vaut pour les sept autres.
"""
import argparse
import io
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
INTER = ROOT / 'assets/interactive'
ACTIVITES = ROOT / 'data/activities.json'
sys.path.insert(0, str(ROOT / 'build'))
from banque import registre, audio_complet, SONORES, palette  # noqa: E402

# Le domaine décide du banc où l'atelier atterrit dans le portail élève. Ces
# quatre-là sont ceux que `eleve.html` range dans « Pour vous exercer seul »,
# sans date et toujours ouverts ; en inventer un cinquième demanderait de
# toucher l'expression régulière en trois endroits.
DOMAINES = {
    'appariement': 'Graphie et sons',
    'oreille': 'Graphie et sons',
    'graphie': 'Graphie et sons',
    'phrase': 'Grammaire transversale',
    'texte': 'Grammaire transversale',
    'conjugaison': 'Grammaire transversale',
}
# Les champs qu'une fiche existante se laisse corriger : le repérage, rien
# d'autre.
STRUCTURE = {'title', 'level', 'interactive', 'categorie',
             'nouveauDesign', 'nouveauDesignColor', 'nouveauDesignTint'}
COMPETENCES = {
    'appariement': ['CE'],
    'oreille': ['CO'],
    'phrase': ['CE', 'PE'],
    'graphie': ['PE'],
    'texte': ['CE'],
    'conjugaison': ['CE', 'PE'],
}


def fiche(e, couleurs):
    """La fiche du catalogue, déduite du contenu de l'atelier."""
    contenu = json.loads(
        io.open(INTER / e['slug'] / 'contenu.json', encoding='utf-8').read())
    accent, doux = couleurs[e['niveau']]
    mots = ['banque niveau %d' % e['niveau'], 'atelier']
    mots += [m for m in contenu.get('motscles', []) if m not in mots]
    mots += [s for s in e['savoirs'] if s not in mots]
    return {
        'id': e['activite'],
        'title': e['titre'],
        'level': 'Niveau %d' % e['niveau'],
        'thumbnail': '',
        'interactive': 'assets/interactive/%s/%s-activite-interactive.html'
                       % (e['slug'], e['slug']),
        'parcours': '',
        'studentDoc': '',
        'slideshow': '',
        'planCours': '',
        'autres': '',
        'keywords': mots,
        'competences': COMPETENCES.get(e['generateur'], ['CE']),
        'tempsVerbaux': contenu.get('tempsVerbaux', []),
        'domaineDeVie': contenu.get('domaine') or DOMAINES.get(e['generateur'], 'Grammaire transversale'),
        'nouveauDesign': True,
        'nouveauDesignColor': accent,
        'nouveauDesignTint': doux,
        'categorie': 'atelier',
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--niveau', type=int)
    ap.add_argument('--essai', action='store_true')
    a = ap.parse_args()

    couleurs = palette()
    acts = json.loads(io.open(ACTIVITES, encoding='utf-8').read())
    par_id = {x['id']: x for x in acts}
    ajouts = majs = 0

    for e in registre(niveau=a.niveau):
        if e['generateur'] == 'polices':
            continue                      # l'atelier d'avant le format commun
        if not e['activite']:
            print('  · %-20s : aucun numéro réservé' % e['slug'])
            continue
        if e['generateur'] in SONORES and not audio_complet(e['slug'], e['items']):
            print('  ⏸ %-20s : injouable sans ses MP3, pas inscrit' % e['slug'])
            continue
        html = INTER / e['slug'] / ('%s-activite-interactive.html' % e['slug'])
        if not html.exists():
            print('  ✗ %-20s : le HTML n\'est pas construit' % e['slug'])
            continue

        neuve = fiche(e, couleurs)
        ancienne = par_id.get(e['activite'])
        if ancienne and ancienne.get('interactive') != neuve['interactive']:
            sys.exit('!! l\'activité %d est déjà prise par « %s » — refus d\'écraser'
                     % (e['activite'], ancienne.get('title')))
        if ancienne is None:
            if not a.essai:
                acts.append(neuve)
                par_id[e['activite']] = neuve
            print('  + %-20s → activité %d' % (e['slug'], e['activite']))
            ajouts += 1
        else:
            # Sur une fiche qui existe déjà, on ne touche qu'au **repérage** —
            # niveau, couleur, catégorie, chemin. Les mots-clés et les
            # compétences ont pu être choisis à la main, atelier par atelier,
            # et les recalculer les remplacerait par une liste plus pauvre.
            # Les identifiants de savoir, eux, s'ajoutent sans rien retirer :
            # c'est par eux que l'enseignante retrouve un atelier.
            change = {k: v for k, v in neuve.items()
                      if k in STRUCTURE and ancienne.get(k) != v}
            manquants = [s for s in e['savoirs']
                         if s not in (ancienne.get('keywords') or [])]
            if manquants:
                change['keywords'] = (ancienne.get('keywords') or []) + manquants
            if change:
                if not a.essai:
                    ancienne.update(change)
                print('  ~ %-20s → activité %d (%s)'
                      % (e['slug'], e['activite'], ', '.join(sorted(change))))
                majs += 1

    if not a.essai and (ajouts or majs):
        acts.sort(key=lambda x: x['id'])
        io.open(ACTIVITES, 'w', encoding='utf-8').write(
            json.dumps(acts, ensure_ascii=False, indent=2) + '\n')
    print('\n%d inscription(s), %d mise(s) à jour%s'
          % (ajouts, majs, ' — essai, rien écrit' if a.essai else ''))
    return 0


if __name__ == '__main__':
    sys.exit(main())
