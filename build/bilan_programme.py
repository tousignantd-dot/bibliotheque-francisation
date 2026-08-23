#!/usr/bin/env python3
"""Ce que le programme demande, ce qui existe, ce qui manque.

    python3 build/bilan_programme.py           # le bilan
    python3 build/bilan_programme.py --reste   # la liste nue de ce qui manque

La question « il reste quoi ? » a été posée trois fois en deux jours et
recalculée de tête trois fois, dont une fois faux — « les activités 75 à 82 du
niveau 5 » étaient des activités du niveau 3, déjà faites. Le compte vit ici
maintenant.

Le rattachement d'un module à sa situation se lit dans le champ `theme` de son
manifeste. Deux réserves, écrites plutôt que corrigées en douce :

· **Neuf modules du niveau 4 sont d'avant le gabarit** et n'ont pas de
  manifeste du tout. Sans la table ci-dessous, le bilan les déclarerait
  manquants alors qu'ils sont en ligne depuis des mois.
· **Trois manifestes abrègent le libellé du programme** (« Actualité » pour
  « Suivi de l'actualité »). Plutôt que de réécrire trois manifestes — et de
  reconstruire trois modules pour un mot — la table les rattache aussi.
"""
import json
import pathlib
import re
import sys
import unicodedata
import importlib.util

RACINE = pathlib.Path(__file__).resolve().parent.parent
PROGRAMME = (pathlib.Path.home() / 'Claude' / 'programme'
             / 'programme-francisation.json')
sys.path.insert(0, str(RACINE / 'build' / 'powerpoints'))
from modules import MODULES                                  # noqa: E402

# Les modules que le champ `theme` ne suffit pas à rattacher : ceux d'avant le
# gabarit, et ceux dont le manifeste abrège le libellé du programme.
RATTACHEMENTS = {
    'module-consultation': "Consultation d'un professionnel de la santé",
    'module-urgence': 'Urgence et hospitalisation',
    'module-sante': "Consultation d'un professionnel de la santé",
    'module-travail': 'Emploi',
    'module-procedure': 'Transactions bancaires',
    'module-nouvelles': "Suivi de l'actualité",
    'module-meteo': 'Météo',
    'module-pub': 'Publicité',
    'module-logement': "Location d'un logement",
    'module-probleme': "Problèmes reliés à l'habitation",
    # Même abrègement que son voisin du niveau 4 : le manifeste annonce
    # « Logement », le programme dit « Problèmes reliés à l'habitation ».
    'module-n6-habitation': "Problèmes reliés à l'habitation",
    # Le niveau 7 est le seul dont la situation nomme les deux gestes ;
    # le manifeste, lui, abrège comme partout ailleurs.
    'module-n7-logement': "Location ou achat d'un logement",
    # Le manifeste abrège le titre à rallonge du programme, comme le font
    # déjà les modules d'œuvres des niveaux 5 et 6.
    'module-n7-oeuvres': ('Découverte d’œuvres littéraires, musicales, '
                          'cinématographiques et télévisuelles'),
    'module-n5-oeuvres': ('Découverte d’œuvres littéraires, musicales, '
                          'cinématographiques ou télévisuelles'),
    'module-n7-actualite': "Suivi de l'actualité",
    'module-n6-oeuvres': ('Découverte d’œuvres littéraires, musicales, '
                          'cinématographiques et télévisuelles'),
    'module-n8-oeuvres': ('Découverte d’œuvres littéraires, musicales, '
                          'cinématographiques et télévisuelles'),
}


def norme(s):
    """Deux libellés qui ne diffèrent que par une apostrophe sont le même."""
    s = s.replace("\\'", "'").replace('’', "'")
    s = unicodedata.normalize('NFKD', s)
    s = ''.join(c for c in s if not unicodedata.combining(c))
    return re.sub(r'\s+', ' ', s).strip().lower()


def theme_du_manifeste(slug):
    f = RACINE / 'build' / 'contenu' / slug / 'manifest.py'
    if not f.exists():
        return None
    spec = importlib.util.spec_from_file_location('mf_' + slug.replace('-', '_'), f)
    mod = importlib.util.module_from_spec(spec)
    try:
        spec.loader.exec_module(mod)
        return mod.MANIFESTE.get('theme')
    except Exception:
        return None


def bilan():
    prog = json.loads(PROGRAMME.read_text(encoding='utf-8'))
    par_niveau = {}
    for niv in prog['niveaux']:
        libelles = [s if isinstance(s, str) else (s.get('situation') or s.get('titre'))
                    for s in niv['situations']]
        par_niveau[niv['niveau']] = {norme(l): l for l in libelles}

    couvert, hors = {}, []
    for slug, m in MODULES.items():
        niveau = m.get('niveau')
        libelle = RATTACHEMENTS.get(slug) or theme_du_manifeste(slug)
        if not libelle:
            hors.append((slug, niveau, 'aucun thème lisible'))
            continue
        cle = norme(libelle)
        if cle in par_niveau.get(niveau, {}):
            couvert.setdefault(niveau, set()).add(cle)
        else:
            hors.append((slug, niveau, 'thème hors programme : « %s »' % libelle))
    return par_niveau, couvert, hors


def main():
    par_niveau, couvert, hors = bilan()
    nu = '--reste' in sys.argv
    total_reste = 0
    for niveau in sorted(par_niveau):
        tout = par_niveau[niveau]
        fait = couvert.get(niveau, set())
        reste = [tout[k] for k in tout if k not in fait]
        total_reste += len(reste)
        if nu:
            for r in reste:
                print('%d\t%s' % (niveau, r))
            continue
        etat = '· complet' if not reste else '· %d à produire' % len(reste)
        print('Niveau %d — %d/%d %s' % (niveau, len(fait), len(tout), etat))
        for r in reste:
            print('    · ' + r)
    if nu:
        return 0
    print('\n%d module(s) à produire.' % total_reste)
    if hors:
        print('\n%d module(s) que le bilan ne sait pas rattacher — à ajouter à '
              'RATTACHEMENTS :' % len(hors))
        for slug, niveau, quoi in hors:
            print('    · %-28s niveau %s · %s' % (slug, niveau, quoi))
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main())
