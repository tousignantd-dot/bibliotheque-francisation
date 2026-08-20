#!/usr/bin/env python3
"""Greffe le dépôt de la production écrite dans les modules interactifs.

L'oral avait son bouton « Envoyer à mon enseignant », pas l'écrit : la
correction s'affichait puis disparaissait avec l'onglet. Cette greffe pose le
bouton manquant et la fonction qui l'accompagne, sur le modèle exact de
poSend(). Comme greffe_outils.py, elle est idempotente : elle retire une greffe
existante avant de la reposer.

    python3 build/greffe_depot_ecrit.py            # tous les modules
    python3 build/greffe_depot_ecrit.py consultation urgence
    python3 build/greffe_depot_ecrit.py --retirer  # dégreffe tout

module-probleme est **généré** par build/module.py module-probleme : le greffer
ici serait écrasé à la reconstruction suivante. Le script le saute quand on ne
le nomme pas explicitement.
"""
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
INTERACTIF = ROOT / 'assets' / 'interactive'

HTML_DEBUT = '<!-- DEPOT-ECRIT:début — greffé par build/greffe_depot_ecrit.py -->'
HTML_FIN = '<!-- DEPOT-ECRIT:fin -->'
JS_DEBUT = '<!-- DEPOT-ECRIT-JS:début — greffé par build/greffe_depot_ecrit.py -->'
JS_FIN = '<!-- DEPOT-ECRIT-JS:fin -->'

# Point d'ancrage du bouton : la zone de rétroaction écrite, identique dans les
# onze modules. Le bloc reste caché jusqu'à ce qu'une correction ait été
# demandée — on ne dépose pas un texte qu'on n'a pas relu.
ANCRE = '<div class="fb" id="peFb" aria-live="polite"></div>'

BOUTON = (ANCRE + '\n       ' + HTML_DEBUT + """
       <div id="peSend" style="display:none;gap:10px;flex-wrap:wrap;align-items:center">
         <button class="btn btn-send" id="peSendBtn" onclick="peSend()">Envoyer à mon enseignant</button>
       </div>
       """ + HTML_FIN)

# On enveloppe renderCorr() au lieu de modifier peCheck() : le module garde son
# code intact, et la greffe se retire sans laisser de trace. Le libellé de la
# tâche et la consigne se lisent dans la carte elle-même — pas de table à tenir
# à jour module par module.
GABARIT_JS = JS_DEBUT + """
<script>
(function () {
  var texteDepose = '', retroDeposee = '';

  function carteEcrite() {
    var t = document.getElementById('peText');
    return t ? t.closest('.card') : null;
  }
  function libelle() {
    var c = carteEcrite(), h = c && c.querySelector('.prod-tit');
    return h ? h.textContent.trim() : 'Production écrite';
  }
  function consigne() {
    var c = carteEcrite(), p = c && c.querySelector('.prod-lead');
    return p ? p.textContent.trim() : '';
  }

  // renderCorr est globale au module et sert aussi à l'oral : on n'ouvre le
  // dépôt que pour la zone écrite.
  if (typeof renderCorr === 'function') {
    var rendreOrig = renderCorr;
    renderCorr = function (elId, data, orig) {
      var r = rendreOrig.apply(this, arguments);
      if (elId === 'peFb') {
        texteDepose = orig || '';
        retroDeposee = (typeof corrSummary === 'function') ? corrSummary(data, orig) : '';
        var zone = document.getElementById('peSend');
        if (zone) zone.style.display = 'flex';
      }
      return r;
    };
  }

  window.peSend = async function () {
    var btn = document.getElementById('peSendBtn');
    var texte = (document.getElementById('peText') || {}).value || texteDepose;
    texte = (texte || '').trim();
    if (!texte) { showErr('peErr', "Écris ton message d'abord."); return; }
    hideErr('peErr');
    btn.disabled = true; btn.textContent = 'Envoi…';
    try {
      var res = await fetch('/api/ecrit/submit', {
        method: 'POST', headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({
          code: typeof studentCode !== 'undefined' ? studentCode : '',
          theme: '%(theme)s', taskId: '%(slug)s-pe',
          taskLabel: libelle(), question: consigne(),
          texte: texte, feedback: retroDeposee,
        }),
      });
      var data = await res.json();
      if (!res.ok) {
        showErr('peErr', data.error || "L'envoi a échoué.");
        btn.disabled = false; btn.textContent = 'Envoyer à mon enseignant';
        return;
      }
      document.getElementById('peSend').innerHTML =
        '<span class="sent">✅ Envoyé à ton enseignant !</span>';
    } catch (e) {
      showErr('peErr', "Impossible d'envoyer.");
      btn.disabled = false; btn.textContent = 'Envoyer à mon enseignant';
    }
  };
})();
</script>
""" + JS_FIN

# Le thème sert au classement côté enseignant, comme pour l'oral.
THEMES = {
    'module-consultation': 'Santé', 'module-urgence': 'Santé', 'module-sante': 'Santé',
    'module-travail': 'Monde du travail', 'module-procedure': 'Monde du travail',
    'module-nouvelles': 'Culture et médias', 'module-pub': 'Culture et médias',
    'module-meteo': 'Vie quotidienne',
    'module-logement': 'Logement', 'module-probleme': 'Logement',
    'module-banque': 'Consommation',
}


def theme_du_module(html, slug):
    """Le thème LMS du module, lu là où il est déjà écrit.

    L'envoi de l'oral porte `fd.append('theme','…')`, rempli par le jeton
    `%%THEME%%` du gabarit — donc par le manifeste du module. Le relire ici
    évite une seconde source : la table `THEMES` ne servait plus qu'à laisser
    un thème vide aux modules qu'on oubliait d'y inscrire, et c'est
    exactement ce qui est arrivé aux sept modules du niveau 4 produits en
    août 2026. Elle reste en repli pour un module bâti hors de la chaîne.
    """
    m = re.search(r"fd\.append\('theme','((?:[^'\\]|\\.)*)'\)", html)
    if m:
        return m.group(1)
    return THEMES.get(slug, '')


def degreffe(html):
    for debut, fin in ((HTML_DEBUT, HTML_FIN), (JS_DEBUT, JS_FIN)):
        html = re.sub(r'\s*' + re.escape(debut) + r'.*?' + re.escape(fin), '',
                      html, flags=re.S)
    return html


def greffe(html, slug):
    """Renvoie le HTML greffé, ou lève ValueError si un ancrage manque : mieux
    vaut un échec bruyant qu'un bouton qui n'envoie nulle part."""
    html = degreffe(html)
    if ANCRE not in html:
        raise ValueError('zone de rétroaction écrite (id="peFb") introuvable')
    if 'function corrSummary' not in html:
        raise ValueError('corrSummary() introuvable')
    html = html.replace(ANCRE, BOUTON, 1)

    fin_doc = re.search(r'</body>\s*</html>\s*$', html)
    if not fin_doc:
        raise ValueError('fin de document </body></html> introuvable')
    js = GABARIT_JS % {'slug': slug, 'theme': theme_du_module(html, slug)}
    return html[:fin_doc.start()] + js + '\n' + html[fin_doc.start():]


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
