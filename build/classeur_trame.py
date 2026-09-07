#!/usr/bin/env python3
"""Engendre `presentations-trame.html` : le classeur habillé du système « Trame ».

    python3 build/classeur_trame.py

Un ESSAI, pour trancher si le système de la maison doit passer partout. Le
classeur en service (`presentations.html`) n'est pas touché ; la variante se
régénère depuis lui, si bien qu'une fiche ajoutée au classeur se retrouve dans
les deux sans recopie. Le jour où la réponse est « oui », ce script devient la
migration ; le jour où elle est « non », il suffit de supprimer deux fichiers.

Ce qui change, et rien d'autre :
  1. les VALEURS des jetons — les noms restent, donc toute la feuille du
     classeur continue de fonctionner et le retour en arrière tient dans un bloc ;
  2. une surcouche pour ce qu'un jeton ne porte pas : la police de lecture,
     les angles, l'absence d'ombre, le motif du bandeau ;
  3. la barre de marque, qui passe de francis à Trame.

Les jetons viennent de ~/Claude/systemes-design/trame/tokens.css et sont
RECOPIÉS, jamais importés — voir le README de ce système.
"""
import pathlib, re, sys
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from _trame_morceaux import JETONS, SURCOUCHE, BARRE

RACINE = pathlib.Path(__file__).resolve().parent.parent
SOURCE = RACINE / 'presentations.html'
CIBLE  = RACINE / 'presentations-trame.html'

def transformer(s):
    def une_fois(avant, apres, quoi):
        n = s.count(avant)
        if n != 1:
            raise SystemExit("« %s » : %d occurrence(s) au lieu d'une. Le classeur "
                             "a changé de forme ; corriger le script." % (quoi, n))
        return s.replace(avant, apres, 1)

    s = une_fois('<title>Le classeur — francis</title>',
                 '<title>Le classeur — Trame</title>', 'titre')
    s = une_fois('<link rel="stylesheet" href="https://fonts.googleapis.com/css2?'
                 'family=Nunito:wght@400;600;700;800;900&display=swap">',
                 '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?'
                 'family=Manrope:wght@500;700;800&family=Source+Serif+4:ital,opsz,'
                 'wght@0,8..60,400;0,8..60,600;1,8..60,400&display=swap">', 'polices')
    s = une_fois('<link rel="stylesheet" href="assets/design-system/marque-francis.css">\n',
                 '', 'feuille de marque')
    s = une_fois('<link rel="icon" type="image/svg+xml" href="assets/design-system/marque-francis-favicon.svg">',
                 '<link rel="icon" type="image/svg+xml" href="assets/presentations/trame/favicon.svg">',
                 'favicon')

    # 1. les jetons
    d = s.index('  :root{'); f = s.index('  }\n', d) + 4
    s = s[:d] + JETONS + s[f:]

    # 2. la surcouche, juste avant la fin de la feuille
    anc = '  @media (prefers-reduced-motion:reduce){*{transition-duration:0ms!important}}\n</style>'
    if s.count(anc) != 1:
        raise SystemExit("l'ancre de la surcouche a disparu de la feuille du classeur.")
    s = s.replace(anc, anc.replace('</style>', '') + '\n' + SURCOUCHE + '</style>', 1)

    # 3. la barre de marque, en tête et au pied
    d = s.index('<div class="fr-barre">'); f = s.index('</div>\n</div>\n', d) + len('</div>\n</div>\n')
    s = s[:d] + BARRE + s[f:]
    pied_francis = ('    <span class="fr-nom" role="img" aria-label="francis">franc'
                    '<span class="fr-i" aria-hidden="true">ı<span class="fr-point"></span></span>s</span>')
    verrou = re.search(r'<span class="tr-logo".*?</span></span>', BARRE, re.S).group(0)
    s = une_fois(pied_francis, '    ' + verrou.replace('class="tr-logo"',
                 'class="tr-logo" style="font-size:1.05rem"', 1), 'logotype du pied')

    # 4. la colonne des dates : Manrope est plus large que Nunito
    s = s.replace('</style>', """  table.index .c-date{width:8.75rem}
  table.index .c-fam{width:7rem}
  table.index .c-type{width:7.5rem}
  table.index td.c-date{font-size:var(--fs-label)}
  table.index .t-lien{font-size:var(--fs-label)}
</style>""", 1)
    return s

if __name__ == '__main__':
    CIBLE.write_text(transformer(SOURCE.read_text(encoding='utf-8')), encoding='utf-8')
    print('écrit %s (%d Ko) depuis %s' % (CIBLE.name, CIBLE.stat().st_size // 1024, SOURCE.name))
