#!/usr/bin/env python3
"""Greffe le rail « Mes outils » dans les modules interactifs.

Deux balises et un appel à Outils.init(), encadrés par des marqueurs de
commentaire. Le script est idempotent : il retire d'abord une greffe existante,
puis la repose. On peut donc le relancer après toute modification du gabarit.

    python3 build/greffe_outils.py            # tous les modules
    python3 build/greffe_outils.py meteo pub  # seulement ceux-là
    python3 build/greffe_outils.py --retirer  # dégreffe tout

module-probleme est **généré** par build/module.py module-probleme, qui appelle
ces mêmes fonctions : ne pas le greffer à la main ici, il serait écrasé à la
reconstruction suivante.
"""
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
INTERACTIF = ROOT / 'assets' / 'interactive'

DEBUT = '<!-- OUTILS-ELEVE:début — greffé par build/greffe_outils.py -->'
FIN = '<!-- OUTILS-ELEVE:fin -->'
CSS_DEBUT = '<!-- OUTILS-ELEVE-CSS:début -->'
CSS_FIN = '<!-- OUTILS-ELEVE-CSS:fin -->'

CSS = (CSS_DEBUT
       + '\n<link rel="stylesheet" href="/assets/design-system/outils-eleve.css">\n'
       + CSS_FIN + '\n')

# `blocs` : ce que la barre marque d'un bouton de traduction et ce qu'elle
# envoie à l'assistant comme contexte. Les modules partagent ces deux classes.
GABARIT_JS = DEBUT + """
<script src="/assets/design-system/outils-eleve.js"></script>
<script>
(function () {
  function sectionCourante() {
    if (typeof SECTIONS === 'undefined' || typeof curSec === 'undefined') return null;
    return SECTIONS.filter(function (s) { return s.id === curSec; })[0] || null;
  }
  var depart = sectionCourante();
  Outils.init({
    code: typeof studentCode !== 'undefined' ? studentCode : '',
    module: '%(slug)s',
    section: depart ? depart.title : '',
    blocs: '.card, .savoir'
  });
  // Le titre de section suit les onglets : l'assistant doit savoir où en est
  // l'élève. render() est une fonction globale du module ; on l'enveloppe
  // plutôt que d'ajouter un écouteur sur chaque onglet.
  if (typeof render === 'function') {
    var rendreOrig = render;
    render = function () {
      var r = rendreOrig.apply(this, arguments);
      var s = sectionCourante();
      if (s) Outils.setSection(s.title);
      return r;
    };
  }
})();
</script>
""" + FIN


def degreffe(html):
    """Retire une greffe précédente. Sans elle, relancer le script empilerait
    deux rails l'un sur l'autre."""
    for debut, fin in ((re.escape(DEBUT), re.escape(FIN)),
                       (re.escape(CSS_DEBUT), re.escape(CSS_FIN))):
        html = re.sub(debut + r'.*?' + fin + r'\n?', '', html, flags=re.S)
    return html


def greffe(html, slug):
    """Repose la greffe. Renvoie le HTML, ou lève ValueError si les points
    d'ancrage manquent — mieux vaut un échec bruyant qu'un module muet."""
    html = degreffe(html)
    if '</head>' not in html:
        raise ValueError('</head> introuvable')
    html = html.replace('</head>', CSS + '</head>', 1)

    fin_doc = re.search(r'</body>\s*</html>\s*$', html)
    if not fin_doc:
        raise ValueError('fin de document </body></html> introuvable')
    return (html[:fin_doc.start()]
            + (GABARIT_JS % {'slug': slug}) + '\n'
            + html[fin_doc.start():])


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

    faits, sautes = 0, []
    for dossier in dossiers:
        if dossier.name == 'module-probleme' and not noms:
            # Généré : sa greffe est posée par son propre build.
            sautes.append('module-probleme (généré — voir son build.py)')
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
