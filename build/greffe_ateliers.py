#!/usr/bin/env python3
"""Rend utilisables sur téléphone les ateliers de la première époque.

Vingt-sept activités de `assets/interactive/` sont antérieures au système de
design : un seul fichier HTML de 1,4 à 1,8 Mo, sans gabarit, sans
`build/contenu/<slug>/`. Vingt d'entre elles sortent d'un bundler et portent
leur CSS **à l'intérieur du JavaScript** — on ne les reskinne pas en posant une
feuille de style par-dessus. Ce que cette greffe répare est ce qui se répare de
l'extérieur, et c'est ce qui empêchait la séance sans compte de marcher :

  1. le `<meta name="viewport">` absent — sans lui, iOS met en page sur 980 px
     et l'élève reçoit l'atelier en timbre-poste ;
  2. `user-scalable=no` — le pincer-pour-agrandir bloqué, sur un public qui
     lit le français en apprenant à le lire ;
  3. `min-height: 100vh` — sur iPhone, `100vh` vaut la fenêtre barres masquées,
     donc le bas passe sous la barre de Safari (même bug que le cadre des
     modules, viewer.html) ;
  4. la langue du document, que le lecteur d'écran a besoin d'entendre ;
  5. le favicon de la marque.

Idempotent : retire une greffe existante avant de reposer.

    python3 build/greffe_ateliers.py             # les 27
    python3 build/greffe_ateliers.py la-poutine  # seulement celui-là
    python3 build/greffe_ateliers.py --liste     # dire lesquels, sans écrire
    python3 build/greffe_ateliers.py --retirer

Ce que `--retirer` ne remet pas : `user-scalable=no`. On ne réinstalle pas un
bug d'accessibilité par symétrie.
"""
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
INTERACTIF = ROOT / 'assets' / 'interactive'

DEBUT = '<!-- ATELIERS-MOBILE:début — greffé par build/greffe_ateliers.py -->'
FIN = '<!-- ATELIERS-MOBILE:fin -->'

VIEWPORT = ('<meta name="viewport" '
            'content="width=device-width, initial-scale=1, viewport-fit=cover">')

# `viewport-fit=cover` va avec les encoches : sans lui, iOS laisse deux bandes
# blanches. Le texte ne se laisse pas gonfler par Safari en paysage
# (`text-size-adjust`) — un atelier calé au pixel se disloque sinon.
STYLE = """<style>
  html { -webkit-text-size-adjust: 100%; text-size-adjust: 100%; }
</style>"""

# Le cœur de la greffe, et la seule part qui doit tourner.
#
# Deux choses se sont vues à l'écran et ne se voyaient pas dans le fichier :
#
# 1. Ces applications **réinjectent leur propre `meta viewport`** au démarrage,
#    `user-scalable=no` compris. Une balise statique se fait doubler : il faut
#    reprendre la main après elles, et la garder (MutationObserver).
#
# 2. Leur feuille de style ne contient **aucune media query** — pas une seule.
#    Elles sont mises en page pour un écran large et rien ne les repliera. Le
#    remède générique n'est pas de les rendre fluides (c'est une réécriture,
#    pas une greffe) mais de dire au navigateur la largeur qu'elles occupent
#    vraiment : `width=776` fait tenir la page entière dans l'écran, mise à
#    l'échelle par le navigateur lui-même. Nativement, sans toucher aux
#    coordonnées — un `zoom` ou un `transform: scale` déplacerait le
#    glisser-déposer, qui est le geste principal de ces ateliers.
#
# La largeur se mesure au lieu de se deviner : chaque atelier a la sienne.
SCRIPT = """<script>
(function () {
  var MIN = 320, MAX = 1200;   // hors de ces bornes, on ne croit pas la mesure

  function balise() {
    var m = document.querySelector('meta[name="viewport"][data-greffe]');
    if (!m) {
      m = document.createElement('meta');
      m.name = 'viewport';
      m.setAttribute('data-greffe', '1');
      (document.head || document.documentElement).appendChild(m);
    }
    return m;
  }

  function poser(contenu) {
    var m = balise();
    if (m.content !== contenu) m.content = contenu;
    // Les balises de l'application : on les neutralise plutôt que de les
    // retirer, pour ne pas surprendre un code qui les relit.
    var autres = document.querySelectorAll('meta[name="viewport"]:not([data-greffe])');
    for (var i = 0; i < autres.length; i++) autres[i].name = 'viewport-remplace';
    if (m !== document.head.lastElementChild) document.head.appendChild(m);
  }

  var FIXE = '';

  function ajuster() {
    if (FIXE) { poser(FIXE); return; }
    poser('width=device-width, initial-scale=1, viewport-fit=cover');
    var d = document.documentElement;
    var large = Math.max(d.scrollWidth, document.body ? document.body.scrollWidth : 0);
    if (large > d.clientWidth + 4 && large >= MIN && large <= MAX) {
      FIXE = 'width=' + Math.ceil(large) + ', viewport-fit=cover';
      poser(FIXE);
    }
  }

  // L'application se dessine après nous : mesurer trop tôt donne la largeur
  // d'une page vide. Trois rendez-vous valent mieux qu'un pari.
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', ajuster);
  }
  window.addEventListener('load', function () { setTimeout(ajuster, 150); });
  setTimeout(ajuster, 1200);
  window.addEventListener('orientationchange', function () {
    FIXE = ''; setTimeout(ajuster, 200);
  });

  // Et si l'application repose la sienne plus tard, on repasse derrière.
  if (window.MutationObserver && document.head) {
    new MutationObserver(function (muts) {
      for (var i = 0; i < muts.length; i++) {
        var aj = muts[i].addedNodes;
        for (var j = 0; j < aj.length; j++) {
          if (aj[j].nodeName === 'META' && aj[j].name === 'viewport') {
            poser(FIXE || 'width=device-width, initial-scale=1, viewport-fit=cover');
            return;
          }
        }
      }
    }).observe(document.head, { childList: true });
  }
})();
</script>"""

FAVICON = ('<link rel="icon" type="image/svg+xml" '
           'href="/assets/design-system/marque-francis-favicon.svg">')


def sans_systeme_de_design(html):
    return not re.search(r'design-system|ds-bundle|ds\.css', html, re.I)


def tete(html):
    """Le `<head>` seul. Les bundles contiennent des bouts de HTML dans leurs
    chaînes JavaScript : chercher un `<meta viewport>` dans tout le fichier
    répond oui pour de mauvaises raisons."""
    m = re.search(r'<head\b.*?</head>', html, re.S)
    return m.group(0) if m else html[:4000]


def degreffe(html):
    html = re.sub(re.escape(DEBUT) + r'.*?' + re.escape(FIN) + r'\n?', '',
                  html, flags=re.S)
    html = re.sub(r'(<html\b[^>]*?) lang="fr" data-greffe-lang="1"', r'\1', html)
    html = re.sub(r'(min-height\s*:\s*100vh)\s*;\s*min-height\s*:\s*100dvh',
                  r'\1', html)
    return html


def greffe(html):
    """Repose la greffe. Lève ValueError si le point d'ancrage manque — mieux
    vaut un échec bruyant qu'un atelier resté en 980 px."""
    html = degreffe(html)
    if '<head' not in html:
        raise ValueError('<head> introuvable')

    # 1. Le pincer-pour-agrandir, sur les métas déjà présentes.
    def deverrouille(m):
        c = m.group(0)
        c = re.sub(r',?\s*user-scalable\s*=\s*no', '', c)
        c = re.sub(r',?\s*maximum-scale\s*=\s*[\d.]+', '', c)
        return c
    debut_tete = tete(html)
    nouvelle_tete = re.sub(r'<meta[^>]*name=["\']viewport["\'][^>]*>',
                           deverrouille, debut_tete)
    html = html.replace(debut_tete, nouvelle_tete, 1)

    # 2. Le bloc greffé, juste après l'ouverture du `<head>`.
    a_deja_un_viewport = bool(
        re.search(r'name=["\']viewport["\']', tete(html)))
    bloc = [DEBUT]
    if not a_deja_un_viewport:
        bloc.append(VIEWPORT)
    bloc += [FAVICON, STYLE, SCRIPT, FIN]
    html = re.sub(r'(<head\b[^>]*>)', lambda m: m.group(1) + '\n'
                  + '\n'.join(bloc), html, count=1)

    # 3. La hauteur dynamique, en gardant `100vh` d'abord pour les navigateurs
    #    qui ignorent `dvh`.
    html = re.sub(r'min-height\s*:\s*100vh',
                  lambda m: m.group(0) + ';min-height:100dvh', html)

    # 4. La langue, marquée pour être retirable au caractère près.
    if not re.search(r'<html[^>]{0,200}\slang=', html[:400]):
        html = re.sub(r'<html\b([^>]*)>',
                      r'<html\1 lang="fr" data-greffe-lang="1">', html, count=1)
    return html


def ateliers():
    """Les activités antérieures au système de design, une seule page chacune.

    Le repérage se fait sur le fichier **dégreffé**. La greffe pose elle-même un
    lien vers `/assets/design-system/` (le favicon) : cherché à l'aveugle, ce
    lien fait passer un atelier greffé pour un module moderne, et le script
    perd ses propres fichiers — plus de second passage, plus de `--retirer`."""
    for d in sorted(INTERACTIF.iterdir()):
        if not d.is_dir():
            continue
        pages = sorted(d.glob('*.html'))
        if not pages:
            continue
        brut = pages[0].read_text(errors='replace')
        if DEBUT in brut or sans_systeme_de_design(degreffe(brut)):
            yield d.name, pages[0]


def main(argv):
    retirer = '--retirer' in argv
    lister = '--liste' in argv
    voulus = [a for a in argv if not a.startswith('--')]

    faits = 0
    for nom, page in ateliers():
        if voulus and nom not in voulus:
            continue
        if lister:
            print(f'{nom}  ({page.stat().st_size / 1e6:.1f} Mo)  {page.name}')
            faits += 1
            continue
        avant = page.read_text(errors='replace')
        apres = degreffe(avant) if retirer else greffe(avant)
        if apres != avant:
            page.write_text(apres)
            print(('dégreffé  ' if retirer else 'greffé    ') + nom)
        else:
            print('inchangé  ' + nom)
        faits += 1

    if voulus and not faits:
        print('Aucun atelier de ce nom. `--liste` dit lesquels existent.')
        return 1
    print(f'\n{faits} atelier(s).')
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
