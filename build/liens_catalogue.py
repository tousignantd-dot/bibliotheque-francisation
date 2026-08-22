#!/usr/bin/env python3
"""Le catalogue ne doit offrir que ce qui existe.

    python3 build/liens_catalogue.py            # dit ce qui cloche
    python3 build/liens_catalogue.py --reparer  # décroche et raccroche

Un module se livre en trois morceaux qui n'arrivent pas ensemble : l'activité
de l'élève, les diaporamas de l'enseignante, les fiches à imprimer. Quand un
agent est coupé en vol — sommeil de l'ordinateur, limite de session, jeton
expiré — l'activité est là et les deux autres manquent. Le catalogue, lui,
annonce déjà les trois. L'enseignante clique et tombe sur un 404, en classe.

Ce script règle les deux sens :

· **Décrocher** ce qui n'existe pas. Un champ vide est prévu par le portail —
  trente-cinq activités en ont déjà — et il dit la vérité : le diaporama
  n'existe pas encore. Un lien mort, lui, ment.
· **Raccrocher les fiches** apparues depuis. `studentDoc` n'a aucun repli :
  si le champ est vide, la ligne du catalogue dit « absent » même quand le
  fichier est là. Le jour où les séances manquantes sont construites, le lien
  revient sans que personne ait à s'en souvenir — c'est tout l'intérêt d'une
  dette qui se règle seule.

· **Signaler seulement** un diaporama présent que le champ n'annonce pas.
  `slideshow`, lui, A un repli : le catalogue compte les présentations dans
  l'inventaire du dépôt, parce qu'un cours en a seize et qu'un champ n'en
  porte qu'une, et il offre l'archive des seize. Remplir le champ
  remplacerait cette archive par un lien vers une seule page — un changement
  d'affichage que personne n'a demandé. On le dit, on ne le fait pas.

Les chemins se déduisent du slug, comme le fait `build/powerpoints`. Sortie en
code 1 s'il reste des liens morts après réparation — ce qui n'arrive que si le
chemin attendu n'est pas celui qu'on croit.
"""
import json
import pathlib
import re
import sys

RACINE = pathlib.Path(__file__).resolve().parent.parent
CATALOGUE = RACINE / 'data' / 'activities.json'

# (champ, gabarit de chemin) — les deux morceaux qui arrivent après coup.
MORCEAUX = (
    ('slideshow',  'assets/powerpoints/{slug}/presentations.html'),
    ('studentDoc', 'assets/documents/{slug}-fiches-eleves.html'),
)


def slug_de(activite):
    """Le slug se lit dans le lien du module interactif, seul champ toujours là."""
    m = re.search(r'assets/interactive/([^/]+)/', activite.get('interactive') or '')
    return m.group(1) if m else None


def examiner():
    activites = json.loads(CATALOGUE.read_text(encoding='utf-8'))
    morts, absents = [], []
    for a in activites:
        slug = slug_de(a)
        for champ, gabarit in MORCEAUX:
            lien = a.get(champ) or ''
            if lien and not (RACINE / lien).exists():
                morts.append((a, champ, lien))
            elif not lien and slug:
                attendu = gabarit.format(slug=slug)
                if (RACINE / attendu).exists():
                    absents.append((a, champ, attendu))
    return activites, morts, absents


def main():
    reparer = '--reparer' in sys.argv
    activites, morts, absents = examiner()

    if morts:
        print('%d lien(s) qui ne mènent nulle part :' % len(morts))
        for a, champ, lien in morts:
            print('   %-4s %-34s %-11s %s' % (a['id'], (a.get('title') or '')[:34],
                                              champ, lien))
    if absents:
        print('%d fichier(s) présent(s) que le champ n’annonce pas '
              '(pour information — le catalogue les trouve par l’inventaire) :' % len(absents))
        for a, champ, lien in absents:
            print('   %-4s %-34s %-11s %s' % (a['id'], (a.get('title') or '')[:34],
                                              champ, lien))
    # Il reste du travail tant qu'un lien est mort OU qu'une fiche existante
    # n'est pas annoncée. Sortir sur le seul compte des liens morts annonçait
    # « tout va bien » et rentrait sans raccrocher les fiches — c'est ce qui a
    # laissé les seize fiches de module-n5-actualite invisibles au catalogue
    # alors qu'elles étaient sur le disque.
    a_faire = morts + [x for x in absents if x[1] == 'studentDoc']
    if not a_faire:
        print('✓ rien à décrocher, rien à raccrocher')
        return 0
    if not reparer:
        print('\n(`--reparer` pour décrocher les liens morts et raccrocher les fiches)')
        return 1

    for a, champ, _ in morts:
        a[champ] = ''
    raccroches = [x for x in absents if x[1] == 'studentDoc']
    for a, champ, lien in raccroches:
        a[champ] = lien
    CATALOGUE.write_text(json.dumps(activites, ensure_ascii=False, indent=2) + '\n',
                         encoding='utf-8')
    print('\n%d lien(s) mort(s) décroché(s), %d fiche(s) raccrochée(s).\n'
          '%d diaporama(s) présent(s) laissés tels quels : voir l’en-tête.'
          % (len(morts), len(raccroches), len(absents) - len(raccroches)))
    _, restants, _ = examiner()
    if restants:
        print('✗ %d lien(s) morts subsistent' % len(restants))
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main())
