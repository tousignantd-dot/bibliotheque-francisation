#!/usr/bin/env python3
"""Sort le logotype du bandeau de page et lui donne sa bande blanche.

C'est le verrouillage A de la remise : le nom, le trait et le descripteur sur
du blanc, fermés par un filet mauve de 2 px, **au-dessus** du bandeau teinté.
Le blanc appartient à la plateforme, la teinte au module ou à la page.

Avant, le verrouillage vivait dans le bandeau lui-même : il y prenait la
couleur du module, et son trait devait être forci pour ne pas s'y effacer.

Deux formes à traiter, selon la famille de pages :

  · **modules** — `#hdr` est le bandeau teinté et contient le verrouillage
    (posé là par build/greffe_marque.py) puis le sur-titre et le titre. Le
    verrouillage en sort et passe au-dessus, en pleine largeur comme lui.
  · **ateliers** — `#hdr` ne contient que le verrouillage, à l'intérieur du
    `<header class="band xx-band">`. Il devient la barre, et sort du header.

Idempotent : une page déjà migrée ne bouge plus.

    python3 build/marque_barre.py --essai   # ce qui changerait
    python3 build/marque_barre.py           # écrit
"""
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
IGNORES = ('.claude/worktrees/', 'node_modules/', '.git/')

DEBUT = '<!-- MARQUE-FRANCIS:début — greffé par build/greffe_marque.py -->'
FIN = '<!-- MARQUE-FRANCIS:fin -->'

# Le verrouillage, tel que la greffe et les sept générateurs l'écrivent.
VERROU = re.compile(
    r'<span class="fr-lockup">.*?</span>\s*\n\s*</span>', re.S)

# ── modules ────────────────────────────────────────────────────────────
MODULE = re.compile(
    r'(<div id="hdr">)\n'
    + re.escape(DEBUT) + r'\n'
    r'<div class="fr-bandeau">\n(.*?)\n</div>\n'
    + re.escape(FIN) + r'\n', re.S)

# ── ateliers ───────────────────────────────────────────────────────────
ATELIER = re.compile(
    r'(<header class="band [a-z]{2}-band">)\n'
    r'  <div id="hdr">\n'
    r'    <div class="fr-bandeau">\n(.*?)\n    </div>\n'
    r'  </div>\n', re.S)


def barre(verrou, large, indent='  '):
    """La bande blanche. `large` : pleine largeur (les modules) ou colonne
    centrée (les ateliers et le portail)."""
    classe = 'fr-barre__in fr-barre__in--large' if large else 'fr-barre__in'
    lignes = [l.strip() for l in verrou.strip().split('\n')]
    dedans = '\n'.join(indent + '    ' + l for l in lignes)
    return ('%s<div class="fr-barre">\n%s  <div class="%s">\n%s\n%s  </div>\n%s</div>\n'
            % (indent, indent, classe, dedans, indent, indent))


def migre(html):
    def pour_module(m):
        return (DEBUT + '\n' + barre(m.group(2), True, '') + FIN + '\n' + m.group(1) + '\n')

    def pour_atelier(m):
        return barre(m.group(2), False, '') + '\n' + m.group(1) + '\n'

    html, n1 = MODULE.subn(pour_module, html)
    html, n2 = ATELIER.subn(pour_atelier, html)
    return html, n1 + n2


def fichiers():
    for f in sorted(ROOT.rglob('*.html')):
        rel = f.relative_to(ROOT).as_posix()
        if any(i in rel + '/' for i in IGNORES):
            continue
        yield f


def main(argv):
    essai = '--essai' in argv
    faits, rates = 0, []
    for f in fichiers():
        html = f.read_text(encoding='utf-8')
        if 'fr-bandeau' not in html:
            continue
        neuf, n = migre(html)
        if not n:
            rates.append(f.relative_to(ROOT).as_posix())
            continue
        faits += 1
        if not essai:
            f.write_text(neuf, encoding='utf-8')
    print('%d page(s) %s' % (faits, 'à migrer' if essai else 'migrée(s)'))
    for r in rates:
        print('  !! forme inconnue, à faire à la main : ' + r)


if __name__ == '__main__':
    main(sys.argv[1:])
