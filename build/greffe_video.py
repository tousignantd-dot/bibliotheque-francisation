#!/usr/bin/env python3
"""Greffe la capsule vidéo d'un module dans sa section « Je découvre ».

    python3 build/greffe_video.py
    python3 build/greffe_video.py --retirer

Une greffe et non le gabarit : dix des quatre-vingt-sept modules n'ont pas de
`build/contenu/<slug>/` et ne se régénèrent pas. Voir build/greffe_transcription.py,
même raison, même patron.

**La capsule se place avant le dialogue**, pas après : on regarde la scène,
puis on l'écoute. L'inverse en ferait une redite.

**Sans sous-titres**, décidé par l'utilisateur. Deux conséquences assumées, et
elles sont écrites ici parce que c'est ici qu'on viendra les défaire : la
capsule ne rouvre pas la transcription qu'un enseignant vient de fermer
(`greffe_transcription.py`) puisqu'elle n'écrit rien ; et elle n'est pas
accessible à un élève sourd — le dialogue, lui, garde sa transcription.
"""
import pathlib
import re
import sys

RACINE = pathlib.Path(__file__).resolve().parent.parent
INTERACTIF = RACINE / 'assets' / 'interactive'

DEBUT = '<!-- VIDEO-MODULE:début — greffé par build/greffe_video.py -->'
FIN = '<!-- VIDEO-MODULE:fin -->'

# Un seul module pour l'instant : c'est une expérimentation, et la question
# qu'elle pose — est-ce qu'une capsule, à cet endroit, aide l'élève ? — se
# tranche sur un module avant de se poser sur quatre-vingt-sept.
CIBLES = {'module-n5-logement': "Ce dont Nadège et Samuel vont parler"}

GABARIT = DEBUT + """
<script>
(function () {
  var SLUG = '%(slug)s';
  var TITRE = %(titre)s;

  var css = document.createElement('style');
  css.textContent =
    '.capsule{margin:0 0 22px}' +
    '.capsule h3{font-size:15px;font-weight:800;letter-spacing:.02em;margin:0 0 8px;' +
      'color:var(--ws-ink,#17181A)}' +
    '.capsule video{width:100%%;max-width:720px;display:block;border-radius:14px;' +
      'background:#000;border:1px solid var(--ws-line,#EAEAE8)}' +
    '.capsule p{font-size:13px;color:var(--ws-ink-3,#6B6F76);margin:8px 0 0;max-width:720px}';
  document.head.appendChild(css);

  /* Le rendu redessine la section : on repose la capsule après lui plutôt que
     de la poser une fois. Même patron que les autres greffes de ce dossier. */
  function poser() {
    var sec = document.getElementById('sec-prep');
    if (!sec || sec.querySelector('.capsule')) return;
    var dial = sec.querySelector('.dial-sec');
    if (!dial) return;

    var bloc = document.createElement('div');
    bloc.className = 'capsule';
    var h = document.createElement('h3');
    h.textContent = TITRE;
    bloc.appendChild(h);

    var v = document.createElement('video');
    v.controls = true;
    v.preload = 'none';          /* trente élèves n'en tirent pas trente */
    v.playsInline = true;
    v.poster = '/assets/interactive/' + SLUG + '/video/' + SLUG + '.jpg';
    var src = document.createElement('source');
    src.src = '/assets/interactive/' + SLUG + '/video/' + SLUG + '.mp4';
    src.type = 'video/mp4';
    v.appendChild(src);
    /* Le navigateur qui ne sait pas lire ne doit pas laisser un carré noir. */
    var secours = document.createElement('a');
    secours.href = src.src;
    secours.textContent = 'Télécharger la vidéo';
    v.appendChild(secours);
    bloc.appendChild(v);

    var note = document.createElement('p');
    note.textContent = 'Trente secondes, sans sous-titres : regardez d’abord, '
      + 'écoutez le dialogue ensuite.';
    bloc.appendChild(note);

    dial.parentNode.insertBefore(bloc, dial);
  }

  function surveiller() {
    if (typeof render === 'function') {
      var rendreOrig = render;
      render = function () {
        var r = rendreOrig.apply(this, arguments);
        poser();
        return r;
      };
    }
    poser();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', surveiller);
  } else {
    surveiller();
  }
})();
</script>
""" + FIN


def degreffe(html):
    return re.sub(re.escape(DEBUT) + r'.*?' + re.escape(FIN) + r'\n?', '',
                  html, flags=re.S)


def greffe(html, slug, titre):
    html = degreffe(html)
    if '</body>' not in html:
        raise ValueError('</body> introuvable')
    bloc = GABARIT % {'slug': slug, 'titre': '"%s"' % titre.replace('"', '\\"')}
    return html.replace('</body>', bloc + '\n</body>', 1)


def page(slug):
    d = INTERACTIF / slug
    pages = sorted(d.glob('*.html'))
    for p in pages:
        if 'activite-interactive' in p.name:
            return p
    return pages[0] if pages else None


def main(argv):
    retirer = '--retirer' in argv
    faits = 0
    for slug, titre in sorted(CIBLES.items()):
        p = page(slug)
        if p is None:
            print('page introuvable : ' + slug)
            continue
        film = INTERACTIF / slug / 'video' / (slug + '.mp4')
        if not retirer and not film.exists():
            print('vidéo absente (%s) — lancez build/video_module.py' % film.name)
            continue
        avant = p.read_text(errors='replace')
        apres = degreffe(avant) if retirer else greffe(avant, slug, titre)
        if apres != avant:
            p.write_text(apres)
            print(('dégreffé  ' if retirer else 'greffé    ') + slug)
        else:
            print('inchangé  ' + slug)
        faits += 1
    print('\n%d module(s).' % faits)
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
