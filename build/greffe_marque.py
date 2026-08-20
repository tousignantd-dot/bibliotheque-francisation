#!/usr/bin/env python3
"""Greffe l'identité de marque SAAF dans l'en-tête des modules interactifs.

Trois morceaux, encadrés par des marqueurs de commentaire : la feuille de
style de la marque, le favicon du monogramme, et le verrouillage horizontal
(pilule « SAAF » · filet · descripteur) posé en première ligne de `#hdr`,
au-dessus du sur-titre du module.

Le script est idempotent : il retire d'abord une greffe existante, puis la
repose. On peut donc le relancer après toute modification du gabarit.

    python3 build/greffe_marque.py            # tous les modules
    python3 build/greffe_marque.py meteo pub  # seulement ceux-là
    python3 build/greffe_marque.py --retirer  # dégreffe tout

Les modules construits par `build/module.py` reçoivent cette greffe pendant
leur construction : ne pas les greffer à la main ici, ils seraient écrasés à
la reconstruction suivante.

Ce que la greffe NE fait pas, volontairement : elle ne touche ni à la couleur
d'accent du module, ni au sur-titre, ni au score. Le violet reste réservé à la
marque — il ne va sur aucun bouton, aucun état, aucune rétroaction.
"""
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
INTERACTIF = ROOT / 'assets' / 'interactive'

def modules_generes():
    """Les modules qui se construisent par build/module.py — ceux qui ont un
    manifeste dans build/contenu/. Leur greffe est posée pendant la
    construction : la poser ici serait écrasé à la reconstruction suivante.
    On lit le dossier plutôt que d'en tenir une liste, qui vieillirait."""
    contenu = ROOT / 'build' / 'contenu'
    if not contenu.exists():
        return set()
    return {d.name for d in contenu.iterdir() if (d / 'manifest.py').exists()}

DEBUT = '<!-- MARQUE-SAAF:début — greffé par build/greffe_marque.py -->'
FIN = '<!-- MARQUE-SAAF:fin -->'
TETE_DEBUT = '<!-- MARQUE-SAAF-TETE:début -->'
TETE_FIN = '<!-- MARQUE-SAAF-TETE:fin -->'

TETE = (TETE_DEBUT + '\n'
        '<link rel="stylesheet" href="/assets/design-system/marque-saaf.css">\n'
        '<link rel="icon" type="image/svg+xml" '
        'href="/assets/design-system/marque-saaf-favicon.svg">\n'
        + TETE_FIN + '\n')

# Le descripteur va **à droite** du contour, séparé par le filet, jamais en
# dessous : sous 320 px de large, c'est la feuille de style qui l'empile.
LOCKUP = DEBUT + """
<div class="saaf-bandeau">
  <span class="saaf-lockup">
    <span class="saaf-pilule"><span class="saaf-nom">SAAF</span></span>
    <span class="saaf-filet" aria-hidden="true"></span>
    <span class="saaf-desc">Système d'aide à l'apprentissage du français</span>
  </span>
</div>
""" + FIN

ANCRE = '<div id="hdr">'


def degreffe(html):
    """Retire une greffe précédente. Sans elle, relancer le script poserait
    deux logotypes l'un sur l'autre."""
    for debut, fin in ((re.escape(DEBUT), re.escape(FIN)),
                       (re.escape(TETE_DEBUT), re.escape(TETE_FIN))):
        html = re.sub(debut + r'.*?' + fin + r'\n?', '', html, flags=re.S)
    return html


def greffe(html, slug=None):
    """Repose la greffe. Renvoie le HTML, ou lève ValueError si les points
    d'ancrage manquent — mieux vaut un échec bruyant qu'un module sans marque.

    `slug` n'est pas utilisé : la marque est la même partout. Le paramètre
    existe pour que la fonction ait la signature des autres greffes et entre
    dans la liste de build/module.py.
    """
    html = degreffe(html)
    if '</head>' not in html:
        raise ValueError('</head> introuvable')
    html = html.replace('</head>', TETE + '</head>', 1)

    if html.count(ANCRE) != 1:
        raise ValueError('%s absent ou en double' % ANCRE)
    return html.replace(ANCRE, ANCRE + '\n' + LOCKUP, 1)


def fichier_du_module(dossier):
    fichiers = list(dossier.glob('*-activite-interactive.html'))
    return fichiers[0] if fichiers else None


def main(argv):
    retirer = '--retirer' in argv
    noms = [a for a in argv if not a.startswith('--')]

    dossiers = sorted(d for d in INTERACTIF.glob('module-*') if d.is_dir())
    if noms:
        voulus = {n if n.startswith('module-') else 'module-' + n for n in noms}
        dossiers = [d for d in dossiers if d.name in voulus]
        introuvables = voulus - {d.name for d in dossiers}
        if introuvables:
            sys.exit('!! module(s) introuvable(s) : ' + ', '.join(sorted(introuvables)))

    generes = modules_generes()
    faits, sautes = 0, []
    for dossier in dossiers:
        if dossier.name in generes and not noms:
            sautes.append(dossier.name + ' (généré — voir build/module.py)')
            continue
        f = fichier_du_module(dossier)
        if f is None:
            sautes.append(dossier.name + ' (aucun fichier interactif)')
            continue
        html = f.read_text(encoding='utf-8')
        try:
            neuf = degreffe(html) if retirer else greffe(html, dossier.name)
        except ValueError as e:
            sautes.append('%s (%s)' % (dossier.name, e))
            continue
        if neuf != html:
            f.write_text(neuf, encoding='utf-8')
            faits += 1
            print('%-24s %s' % (dossier.name, 'dégreffé' if retirer else 'greffé'))
        else:
            print('%-24s inchangé' % dossier.name)

    print('\n%d module(s) modifié(s)' % faits)
    for s in sautes:
        print('  sauté : ' + s)


if __name__ == '__main__':
    main(sys.argv[1:])
