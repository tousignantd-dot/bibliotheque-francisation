#!/usr/bin/env python3
"""
Retire le vert des couleurs de section des modules.

    python3 build/couleurs_sections.py             # applique
    python3 build/couleurs_sections.py --verifier  # signale, n'écrit rien

Pourquoi ce fichier existe
--------------------------
Chaque section d'un module porte une couleur — `sections.js` la donne, et
`exos.js` la répète sur les exercices qui appartiennent à la section. Cette
palette tourne d'un module à l'autre et n'a rien à voir avec le niveau : elle
sert à distinguer les onglets entre eux.

Deux de ses teintes étaient vertes : la forêt `#166534`, qui coloriait presque
toujours « Je retiens des mots », et le teal-vert `#0F766E`, qui coloriait
« Je me lance » et l'étiquette du jeu de rôle. Elles vivaient sous deux formes
— la clé `color:'#…'` de `sections.js` et `exos.js`, et le style en dur des
cartes écrites à la main dans `custom.js`. Le script prend les deux : dans ces
fichiers, ces deux valeurs hexadécimales n'ont jamais servi à autre chose qu'à
une couleur de section. Le 20 août 2026, le vert est sorti du repérage — voir
`build/couleurs_niveau.py` pour la moitié « niveau » de la même décision. Le
vert du système de design (`--accent` `#0A8F5B` : boutons, pastilles, focus,
rétroaction « correct ») n'est pas concerné et reste en place.

Les deux teintes sont remplacées par des teintes que l'arc-en-ciel des niveaux
porte déjà, pour ne pas ouvrir une troisième échelle. Le script est
re-jouable : il sert autant à corriger l'existant qu'à rattraper un module neuf
dont la palette aurait réintroduit du vert.
"""
import argparse
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
CONTENU = ROOT / 'build/contenu'
INTERACTIF = ROOT / 'assets/interactive'

# La forêt tenait la section du vocabulaire, le teal-vert celle de la
# production. Framboise et pourpre les remplacent : deux teintes franches, déjà
# dans l'échelle des niveaux, et qui ne se confondent ni entre elles ni avec
# l'acier, l'ambre et la sarcelle qui restent dans la palette de section.
VERTS_RETIRES = {
    '#166534': '#A5335F',   # forêt      → framboise
    '#0F766E': '#7E3F98',   # teal-vert  → pourpre
}


def cibles():
    """Les fichiers où vit une couleur de section."""
    for nom in ('sections.js', 'exos.js', 'custom.js'):
        yield from sorted(CONTENU.glob('*/%s' % nom))
    for dossier in sorted(INTERACTIF.iterdir()):
        if not dossier.is_dir() or not dossier.name.startswith('module-'):
            continue
        html = dossier / ('%s-activite-interactive.html' % dossier.name)
        # Les modules générés se reconstruisent : on n'écrit pas dans leur
        # HTML. Les plus anciens n'ont pas de dossier de contenu — leur HTML
        # est leur seule source.
        if (CONTENU / dossier.name).exists():
            continue
        if html.exists():
            yield html


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--verifier', action='store_true')
    args = ap.parse_args()

    touches = []
    for chemin in cibles():
        texte = chemin.read_text(encoding='utf-8')
        neuf = texte
        for vert, remplacant in VERTS_RETIRES.items():
            neuf = re.sub(re.escape(vert), remplacant, neuf, flags=re.I)
        if neuf != texte:
            compte = sum(len(re.findall(re.escape(v), texte, flags=re.I))
                         for v in VERTS_RETIRES)
            touches.append((chemin.relative_to(ROOT), compte))
            if not args.verifier:
                chemin.write_text(neuf, encoding='utf-8')

    verbe = 'à corriger' if args.verifier else 'corrigé(s)'
    total = sum(c for _, c in touches)
    print('%d fichier(s) %s, %d couleur(s) verte(s).' % (len(touches), verbe, total))
    for chemin, compte in touches:
        print('  · %s — %d' % (chemin, compte))
    if args.verifier and touches:
        sys.exit(1)


if __name__ == '__main__':
    main()
