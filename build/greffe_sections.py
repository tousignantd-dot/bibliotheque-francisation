#!/usr/bin/env python3
"""Greffe le verrou de sections dans les modules interactifs.

L'enseignante peut donner une date à chaque section d'un module (« Défi 2 »).
Le module, lui, est un fichier que l'élève ouvre directement : c'est donc lui
qui demande au serveur ce qui est ouvert, et qui verrouille le reste.

    python3 build/greffe_sections.py            # tous les modules
    python3 build/greffe_sections.py meteo pub  # seulement ceux-là
    python3 build/greffe_sections.py --retirer  # dégreffe tout

Comme `greffe_outils.py`, le script est idempotent : il retire une greffe
existante avant de la reposer. Il refuse un module absent de
`data/activities.json` — sans numéro d'activité, il n'y a rien à demander.

Trois précautions, parce qu'un verrou qui se trompe ferme la classe :

1. **Le silence ouvre tout.** Pas de code élève, serveur muet, module sans
   découpage : on ne verrouille rien et le module se comporte comme avant.
2. **La section verrouillée reste visible**, avec sa date d'ouverture. L'élève
   voit ce qui l'attend au lieu de trouver un module amputé.
3. **On n'abandonne jamais l'élève sur une section fermée** : si la sienne
   vient de se verrouiller, on le pose sur la première section ouverte.

module-probleme est **généré** (`build/module-probleme/build.py`) : ne pas le
greffer à la main, il serait écrasé à la reconstruction suivante.
"""
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
INTERACTIF = ROOT / 'assets' / 'interactive'
ACTIVITES = ROOT / 'data' / 'activities.json'

DEBUT = '<!-- SECTIONS-DATEES:début — greffé par build/greffe_sections.py -->'
FIN = '<!-- SECTIONS-DATEES:fin -->'

GABARIT = DEBUT + """
<style>
  .tab.verrouillee { opacity: .55; cursor: not-allowed; }
  .tab.verrouillee .tchk { visibility: visible; opacity: 1; }
  #verrou-avis {
    margin: 10px 0 0; padding: 10px 14px; border-radius: 10px;
    background: #FDF3E3; color: #7A4A12; border: 1px solid #E8CDA0;
    font-size: 15px; font-weight: 700;
  }
</style>
<script>
(function () {
  var ACTIVITE = %(activite)d;

  function joli(iso) {
    if (!iso) return '';
    var p = iso.split('-');
    var mois = ['janvier','février','mars','avril','mai','juin','juillet',
                'août','septembre','octobre','novembre','décembre'];
    return Number(p[2]) + ' ' + mois[Number(p[1]) - 1];
  }

  function avis(texte) {
    var el = document.getElementById('verrou-avis');
    if (!el) {
      var tabs = document.getElementById('tabs');
      if (!tabs || !tabs.parentNode) return;
      el = document.createElement('p');
      el.id = 'verrou-avis';
      tabs.parentNode.insertBefore(el, tabs.nextSibling);
    }
    el.textContent = texte;
    el.hidden = !texte;
  }

  function appliquer(sections) {
    var parId = {};
    sections.forEach(function (s) { parId[s.id] = s; });

    SECTIONS.forEach(function (sec) {
      var etat = parId[sec.id];
      var bouton = document.getElementById('tab-' + sec.id);
      if (!bouton || !etat) return;
      var fermee = !etat.ouverte;
      bouton.classList.toggle('verrouillee', fermee);
      bouton.setAttribute('aria-disabled', fermee ? 'true' : 'false');
      var chk = bouton.querySelector('.tchk');
      if (chk && fermee) chk.textContent = '🔒';
      bouton.title = fermee
        ? (etat.datePrevue ? 'Cette partie s’ouvre le ' + joli(etat.datePrevue)
                           : 'Cette partie n’est pas encore ouverte.')
        : '';
    });

    // Capture : l'écouteur du module est posé sur le bouton lui-même, il faut
    // donc arrêter le clic avant lui plutôt qu'après.
    var tabs = document.getElementById('tabs');
    if (tabs && !tabs.dataset.verrou) {
      tabs.dataset.verrou = '1';
      tabs.addEventListener('click', function (e) {
        var b = e.target.closest ? e.target.closest('.tab') : null;
        if (!b || !b.classList.contains('verrouillee')) return;
        e.stopPropagation();
        e.preventDefault();
        avis(b.title || 'Cette partie n’est pas encore ouverte.');
      }, true);
    }

    var ouvertes = sections.filter(function (s) { return s.ouverte; });
    if (!ouvertes.length) {
      avis('Aucune partie de ce module n’est ouverte pour l’instant. '
           + 'Ton enseignante les ouvrira une à une.');
      return;
    }
    var courante = parId[curSec];
    if (courante && !courante.ouverte) {
      curSec = ouvertes[0].id;
      avis('Cette partie n’est pas encore ouverte : voici celle que tu peux faire.');
    }
    if (typeof render === 'function') render();
  }

  function demarrer() {
    if (typeof SECTIONS === 'undefined' || typeof curSec === 'undefined') return;
    var code = (typeof studentCode !== 'undefined' && studentCode) || '';
    if (!code) return;   // hors session : le module s'ouvre en entier
    fetch('/api/student/sections?code=' + encodeURIComponent(code)
          + '&activityId=' + ACTIVITE)
      .then(function (r) { return r.ok ? r.json() : null; })
      .then(function (d) {
        if (d && d.decoupe && d.sections && d.sections.length) appliquer(d.sections);
      })
      .catch(function () { /* serveur muet : on n'enlève rien à l'élève */ });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', demarrer);
  } else {
    demarrer();
  }
})();
</script>
""" + FIN


def activites_par_slug():
    """{slug de dossier: id d'activité} — le catalogue est la seule autorité
    sur ce numéro, qu'on ne veut surtout pas écrire en dur dans un module."""
    activites = json.loads(ACTIVITES.read_text(encoding='utf-8'))
    out = {}
    for a in activites:
        chemin = (a.get('interactive') or '').strip()
        m = re.match(r'assets/interactive/([^/]+)/', chemin)
        if m:
            out[m.group(1)] = a['id']
    return out


def degreffe(html):
    return re.sub(re.escape(DEBUT) + r'.*?' + re.escape(FIN) + r'\n?', '',
                  html, flags=re.S)


def greffe(html, activite_id):
    html = degreffe(html)
    fin_doc = re.search(r'</body>\s*</html>\s*$', html)
    if not fin_doc:
        raise ValueError('fin de document </body></html> introuvable')
    return (html[:fin_doc.start()]
            + (GABARIT % {'activite': activite_id}) + '\n'
            + html[fin_doc.start():])


def fichier_du_module(dossier):
    fichiers = list(dossier.glob('*-activite-interactive.html'))
    return fichiers[0] if fichiers else None


def main(argv):
    retirer = '--retirer' in argv
    noms = [a for a in argv if not a.startswith('--')]

    par_slug = activites_par_slug()
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
            sautes.append('module-probleme (généré — voir son build.py)')
            continue
        f = fichier_du_module(dossier)
        if f is None:
            sautes.append(dossier.name + ' (aucun fichier interactif)')
            continue
        if not retirer and dossier.name not in par_slug:
            sautes.append(dossier.name + ' (absent de data/activities.json)')
            continue
        html = f.read_text(encoding='utf-8')
        try:
            neuf = degreffe(html) if retirer else greffe(html, par_slug[dossier.name])
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
