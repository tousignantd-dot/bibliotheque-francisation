#!/usr/bin/env python3
"""Greffe de quoi installer le site depuis n'importe quelle page d'élève.

Le manifeste, l'icône d'iOS et l'enregistrement du service worker vivaient
seulement dans `eleve.html` et `seance.html`. Or un élève qui reçoit de son
enseignant le lien d'un point express arrive **droit sur un module** : il ne
passe ni par le portail ni par la séance, et n'enregistrait donc jamais le
service worker. Il n'avait ni le hors-ligne, ni la proposition d'installer.

    python3 build/greffe_installable.py            # tout
    python3 build/greffe_installable.py meteo pub  # ces modules-là
    python3 build/greffe_installable.py --retirer  # dégreffe tout

**Une greffe et non le gabarit**, pour la même raison que
`greffe_transcription.py` : dix des 87 modules n'ont pas de
`build/contenu/<slug>/` et ne se régénèrent pas, et `build/module.py` ne rejoue
qu'une partie des greffes du dossier — reconstruire ferait tomber les autres.

**Les points express, eux, passent bien par le gabarit** : ils sont tous
produits par `build/storyline.py` depuis `build/gabarit/storyline.html`, où la
greffe est posée à demeure. Ce script ne les touche pas.

Idempotent : il retire d'abord une greffe existante, puis la repose. Le retrait
va d'un marqueur à l'autre, jamais par chaîne exacte — une chaîne qui a bougé
échoue en silence.
"""
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
INTERACTIF = ROOT / 'assets' / 'interactive'
PAGES = ('eleve.html', 'seance.html')

DEBUT = '<!-- INSTALLABLE:début — greffé par build/greffe_installable.py -->'
FIN_M = '<!-- INSTALLABLE:fin -->'

# L'ancienne greffe, posée à la main dans eleve.html et seance.html avant que ce
# script existe. On la reconnaît pour la remplacer, sans quoi les deux pages
# porteraient deux fois le même bloc.
VIEUX = ('<!-- installable:début — greffe PWA, retirée d\'un marqueur à l\'autre -->',
         '<!-- installable:fin -->')

BLOC = DEBUT + """
<link rel="manifest" href="/manifest.webmanifest">
<meta name="theme-color" content="#6B4FBB">
<!-- iOS ignore les icônes du manifeste pour l'écran d'accueil : il lui faut
     celle-ci, et elle doit être un PNG opaque. -->
<link rel="apple-touch-icon" href="/assets/design-system/icones/icone-180.png">
<meta name="apple-mobile-web-app-title" content="francis">
<script>
  // Après `load` : le service worker ne doit jamais retarder le premier
  // affichage. Un échec est silencieux — la page marche sans lui.
  if ('serviceWorker' in navigator) {
    window.addEventListener('load', function () {
      navigator.serviceWorker.register('/sw.js').catch(function () {});
    });
  }
</script>
""" + FIN_M + "\n"


def degreffe(html):
    for d, f in ((DEBUT, FIN_M), VIEUX):
        html = re.sub(re.escape(d) + r'.*?' + re.escape(f) + r'\n?', '', html, flags=re.S)
    return html


def greffe(html, _=None):
    """Le second argument existe pour que `build/module.py` puisse appeler
    toutes ses greffes de la même façon — celle-ci n'a besoin de rien."""
    html = degreffe(html)
    if '</head>' not in html:
        raise ValueError('</head> introuvable')
    return html.replace('</head>', BLOC + '</head>', 1)


def fichier_du_module(dossier):
    f = list(dossier.glob('*-activite-interactive.html'))
    return f[0] if f else None


def traiter(chemin, retirer, etiquette):
    html = chemin.read_text(encoding='utf-8')
    neuf = degreffe(html) if retirer else greffe(html)
    if neuf == html:
        print('%-40s inchangé' % etiquette)
        return 0
    chemin.write_text(neuf, encoding='utf-8')
    print('%-40s %s' % (etiquette, 'dégreffé' if retirer else 'greffé'))
    return 1


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

    faits, sautes = 0, []
    for dossier in dossiers:
        f = fichier_du_module(dossier)
        if f is None:
            sautes.append(dossier.name + ' (aucun fichier interactif)')
            continue
        try:
            faits += traiter(f, retirer, dossier.name)
        except ValueError as e:
            sautes.append('%s (%s)' % (dossier.name, e))

    if not noms:                      # les deux portails, seulement en passe complète
        for nom in PAGES:
            faits += traiter(ROOT / nom, retirer, nom)

    print('\n%d fichier(s) modifié(s)' % faits)
    for s in sautes:
        print('  sauté : ' + s)


if __name__ == '__main__':
    main(sys.argv[1:])
