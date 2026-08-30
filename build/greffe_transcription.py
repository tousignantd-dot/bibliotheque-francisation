#!/usr/bin/env python3
"""Greffe le verrou de transcription dans les modules interactifs.

L'enseignant peut fermer la transcription d'un dialogue pour son groupe, sur un
module donné : l'élève écoute alors sans pouvoir lire. Le réglage vit dans la
planification (`transcription` dans `data/schedule.json`) et arrive par
`/api/student/sections`, que tout module appelle déjà au démarrage.

Une greffe plutôt qu'une modification du gabarit, pour deux raisons mesurées :
dix des quatre-vingt-sept modules n'ont pas de `build/contenu/<slug>/` et ne se
régénèrent pas, et `build/module.py` ne rejoue que cinq greffes sur les dix-sept
du dossier — reconstruire aurait fait tomber les douze autres.

    python3 build/greffe_transcription.py            # tous les modules
    python3 build/greffe_transcription.py meteo pub  # seulement ceux-là
    python3 build/greffe_transcription.py --retirer

Ce que la greffe ne prétend pas être : un verrou. Le texte du dialogue est dans
le fichier du module — c'est lui qui l'affiche et qui le lit à voix haute — donc
un élève qui ouvre les outils du navigateur le trouvera. C'est un garde-fou
pédagogique, et il est écrit comme tel.
"""
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
INTERACTIF = ROOT / 'assets' / 'interactive'

DEBUT = '<!-- TRANSCRIPTION:début — greffé par build/greffe_transcription.py -->'
FIN = '<!-- TRANSCRIPTION:fin -->'

# `%(activite)s` : le numéro d'activité est **gravé** dans le bloc, pas lu dans
# une variable du module. `ACTIVITE` existe bien, mais enfermée dans la fermeture
# de la greffe des sections : invisible d'ici. C'est exactement ce que
# `greffe_sections` fait de son côté, et pour la même raison.
GABARIT = DEBUT + """
<script>
(function () {
  var OUVERTE = true;      // le défaut : on n'enlève rien à l'élève
  var NOTE = 'Ton enseignante a fermé la transcription : écoute le dialogue.';

  /* Les deux endroits où un module montre le texte d'un dialogue :
     — la section de mise en situation, bouton « Lire la transcription » et
       bloc `#script-<sectionId>` ;
     — un exercice bâti sur un dialogue, avec son `<details>` « Afficher le
       texte du dialogue ».
     Les deux sont redessinés à chaque `render()`, donc on repasse après lui
     plutôt que de nettoyer une fois. */
  function retirer() {
    if (OUVERTE) return;
    var boutons = document.querySelectorAll(
      'button[onclick^="toggleScript"], [onclick^="toggleScript"]');
    for (var i = 0; i < boutons.length; i++) {
      var b = boutons[i];
      var note = document.createElement('span');
      note.className = 'transcription-fermee';
      note.textContent = NOTE;
      note.style.cssText = 'font-size:13px;font-weight:700;color:var(--ink-500,'
        + '#64748b);align-self:center';
      b.parentNode.replaceChild(note, b);
    }
    // Le bloc de texte lui-même, et le `<details>` des exercices.
    var textes = document.querySelectorAll('.dial-txt');
    for (var j = 0; j < textes.length; j++) {
      var t = textes[j];
      var det = t.closest ? t.closest('details') : null;
      var mort = det || t;
      if (det) {
        var note2 = document.createElement('div');
        note2.className = 'transcription-fermee';
        note2.style.cssText = 'font-size:13px;font-weight:700;margin-bottom:12px;'
          + 'color:var(--ink-500,#64748b)';
        note2.textContent = NOTE;
        mort.parentNode.replaceChild(note2, mort);
      } else {
        mort.parentNode.removeChild(mort);
      }
    }
  }

  /* Ceinture : si un bouton nous échappe, il ne doit rien ouvrir. */
  if (typeof window.toggleScript === 'function') {
    var toggleOrig = window.toggleScript;
    window.toggleScript = function () {
      if (!OUVERTE) return;
      return toggleOrig.apply(this, arguments);
    };
  }

  function surveiller() {
    if (typeof render === 'function') {
      var rendreOrig = render;
      render = function () {
        var r = rendreOrig.apply(this, arguments);
        retirer();
        return r;
      };
    }
    retirer();
  }

  function demarrer() {
    var code = (typeof studentCode !== 'undefined' && studentCode) || '';
    if (!code) return;   // hors session : le module s'ouvre en entier
    fetch('/api/student/sections?code=' + encodeURIComponent(code)
          + '&activityId=' + %(activite)s)
      .then(function (r) { return r.ok ? r.json() : null; })
      .then(function (d) {
        // `undefined` sur un serveur qui ne connaît pas encore le champ :
        // seul un `false` franc ferme quelque chose.
        if (d && d.transcription === false) { OUVERTE = false; surveiller(); }
      })
      .catch(function () { /* serveur muet : la transcription reste offerte */ });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', demarrer);
  } else {
    demarrer();
  }
})();
</script>
""" + FIN


def degreffe(html):
    return re.sub(re.escape(DEBUT) + r'.*?' + re.escape(FIN) + r'\n?', '',
                  html, flags=re.S)


def greffe(html, activite):
    """Repose la greffe juste avant `</body>`, donc après le script du module :
    `render` et `toggleScript` doivent exister pour être enveloppés.

    `activite` est le numéro d'activité du module — un slug, ici, ne servirait
    à rien : c'est au serveur qu'on parle."""
    html = degreffe(html)
    if '</body>' not in html:
        raise ValueError('</body> introuvable')
    bloc = GABARIT % {'activite': int(activite)}
    return html.replace('</body>', bloc + '\n</body>', 1)


def modules():
    for d in sorted(INTERACTIF.glob('module-*')):
        page = d / 'index.html'
        if not page.exists():
            pages = sorted(d.glob('*.html'))
            if not pages:
                continue
            page = pages[0]
        yield d.name, page


def main(argv):
    retirer = '--retirer' in argv
    voulus = [a for a in argv if not a.startswith('--')]
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
    from greffe_sections import activites_par_slug
    ids = activites_par_slug()
    faits = 0
    manquants = []
    for nom, page in modules():
        court = nom.replace('module-', '')
        if voulus and nom not in voulus and court not in voulus:
            continue
        if not retirer and nom not in ids:
            # Sans numéro d'activité, le bloc ne saurait pas quoi demander au
            # serveur. On le dit au lieu de greffer un module muet.
            manquants.append(nom)
            continue
        avant = page.read_text(errors='replace')
        apres = degreffe(avant) if retirer else greffe(avant, ids[nom])
        if apres != avant:
            page.write_text(apres)
            print(('dégreffé  ' if retirer else 'greffé    ') + nom)
        else:
            print('inchangé  ' + nom)
        faits += 1
    if manquants:
        print('\nAbsents de data/activities.json, donc non greffés : '
              + ', '.join(manquants))
    if voulus and not faits:
        print('Aucun module de ce nom.')
        return 1
    print('\n%d module(s).' % faits)
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
