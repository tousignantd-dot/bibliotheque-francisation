#!/usr/bin/env python3
"""Le jeu de rôle à l'oreille, décidé par l'enseignant pour son groupe.

Le module a son bouton « Écouter sans lire » (`build/greffe_ecouter_sans_lire.py`)
et l'élève en dispose. Cette greffe-ci met le même choix dans la planification :
quand l'enseignant ferme les réponses de l'assistant pour son groupe et ce
module, le texte reste fermé et le bouton disparaît de l'écran de l'élève.

Le réglage vit dans la planification (`jeuDeRole` dans `data/schedule.json`,
valeur "ecoute") et arrive par `/api/student/sections`, que tout module appelle
déjà au démarrage — le même tuyau que le verrou de transcription, et pour la
même raison : lui ajouter un appel réseau pour un booléen coûterait une requête
de plus à chaque poste d'une classe entière.

Ce que la greffe ne prétend pas être : un verrou. Le texte des répliques arrive
par le réseau et le module le connaît — qui ouvre les outils du navigateur le
trouvera. C'est un garde-fou pédagogique, et il est écrit comme tel.

    python3 build/greffe_ecoute_verrou.py            # tous les modules
    python3 build/greffe_ecoute_verrou.py n5-logement
    python3 build/greffe_ecoute_verrou.py --retirer
"""
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
INTERACTIF = ROOT / 'assets' / 'interactive'

DEBUT = '<!-- ECOUTE-VERROU:début — greffé par build/greffe_ecoute_verrou.py -->'
FIN = '<!-- ECOUTE-VERROU:fin -->'

# `%(activite)s` : le numéro d'activité est **gravé**, comme dans
# greffe_transcription — `ACTIVITE` existe dans le module mais reste enfermée
# dans la fermeture de la greffe des sections, invisible d'ici.
GABARIT = DEBUT + """
<script>
(function () {
  var code = (typeof studentCode !== 'undefined' && studentCode) || '';
  if (!code) return;               // hors session : l'élève garde son bouton
  // Le bouton est injecté au DOMContentLoaded, et ce bloc-ci s'exécute à
  // l'analyse de la page : selon que le serveur répond avant ou après, le
  // bouton est là ou pas encore. Plutôt que de parier sur l'ordre — un
  // écouteur DOMContentLoaded posé après l'événement ne se déclenche JAMAIS,
  // et la greffe serait silencieusement inopérante — on attend qu'il paraisse.
  var essais = 0;
  function fermer() {
    var b = document.getElementById('jrEcouteBtn');
    if ((typeof jrSansTexte !== 'function' || !b) && essais++ < 25) {
      setTimeout(fermer, 200);     // cinq secondes au total, puis on renonce
      return;
    }
    if (typeof jrSansTexte !== 'function') return;
    jrSansTexte(true);
    // Le bouton s'en va : ce n'est plus le choix de l'élève. Le haut-parleur
    // de chaque bulle, lui, reste — réécouter EST l'exercice.
    if (b) {
      var l = document.createElement('div');
      l.className = 'jr-choix-l';
      l.textContent = 'Votre enseignante a fermé le texte des réponses : écoutez.';
      b.parentElement.replaceWith(l);
    }
  }
  fetch('/api/student/sections?code=' + encodeURIComponent(code)
        + '&activityId=' + %(activite)s)
    .then(function (r) { return r.ok ? r.json() : null; })
    .then(function (d) {
      // Rien ne se ferme sur un serveur qui ne connaît pas encore le champ :
      // seule la valeur franche « ecoute » retire quelque chose à l'élève.
      if (!d || d.jeuDeRole !== 'ecoute') return;
      fermer();
    })
    .catch(function () {});
}());
</script>
""" + FIN


def degreffe(html):
    return re.sub(re.escape(DEBUT) + r'.*?' + re.escape(FIN) + r'\n?', '',
                  html, flags=re.S)


def greffe(html, activite):
    """Repose la greffe juste avant `</body>`, donc après le script du module :
    `jrSansTexte` doit exister pour être appelée."""
    html = degreffe(html)
    if '</body>' not in html:
        raise ValueError('</body> introuvable')
    return html.replace('</body>', GABARIT % {'activite': int(activite)}
                        + '\n</body>', 1)


def modules():
    for d in sorted(INTERACTIF.glob('module-*')):
        pages = sorted(d.glob('*.html'))
        if pages:
            yield d.name, pages[0]


def main(argv):
    retirer = '--retirer' in argv
    voulus = [a for a in argv if not a.startswith('--')]
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
    from greffe_sections import activites_par_slug
    ids = activites_par_slug()
    faits, sautes, manquants = 0, 0, []
    for nom, page in modules():
        court = nom.replace('module-', '')
        if voulus and nom not in voulus and court not in voulus:
            continue
        avant = page.read_text(errors='replace')
        # Les neuf modules sans jeu de rôle n'ont rien à fermer.
        if not retirer and 'function jrSansTexte(' not in avant:
            sautes += 1
            continue
        if not retirer and nom not in ids:
            manquants.append(nom)
            continue
        apres = degreffe(avant) if retirer else greffe(avant, ids[nom])
        if apres != avant:
            page.write_text(apres)
            faits += 1
    print('%d %s' % (faits, 'dégreffés' if retirer else 'greffés'))
    if sautes:
        print('%d sans jeu de rôle, laissés tels quels' % sautes)
    if manquants:
        print('Absents de data/activities.json : ' + ', '.join(manquants))
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
