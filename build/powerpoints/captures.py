#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Captures d'écran des exercices interactifs
===========================================

    python3 captures.py module-sante        → les captures d'un module
    python3 captures.py --tous              → tous les modules du registre
    python3 captures.py module-sante pr1    → n'en refait qu'une

Produit une image par exercice à banc de réponses, dans
`_captures/<slug>/<idExercice>.png`. Les decks les posent ensuite par
`Deck.capture('pr1')` ; le nom du fichier EST l'identifiant d'exercice cité
dans l'en-tête des séances (« Source du module : … exercice `pr1` »).

L'écran est capturé **vierge** : zones de dépôt vides, banc complet. C'est
l'état que l'élève découvre, donc celui qu'on projette avant d'ouvrir
l'activité.

Comment
-------
Le poste n'a ni Node ni Puppeteer : on pilote Chrome sans interface. Comme
`--screenshot` ne sait pas exécuter de script à nous, une page d'appoint
(`_capture_harness.html`, écrite puis effacée à la racine du dépôt) charge le
module dans un cadre, neutralise ce qui gênerait, puis découpe la carte
voulue. Deux passes par module :

  1. une passe de relevé → le manifeste (identifiants et tailles des cartes) ;
  2. `--screenshot` par carte, la fenêtre étant réglée à la taille exacte.

La passe 1 **renvoie son manifeste au serveur** (`POST /_manifeste`) au lieu de
passer par `--dump-dom` : sur ces modules, `--dump-dom` ne rend jamais la main
— la page charge entièrement, puis Chrome reste suspendu jusqu'à ce qu'on le
tue. `--screenshot` revient, lui, en quelques secondes ; on s'en sert donc
comme minuterie et on récupère les mesures par le réseau.

Trois neutralisations, sans lesquelles la capture mentirait :
  · `#chrome` et `#tabs` sont `sticky` : une fois défilé jusqu'à la carte,
    ils se poseraient PAR-DESSUS le haut de l'exercice ;
  · le banc de réponses est `sticky` lui aussi, avec un décalage calé sur la
    hauteur de ces barres — collé en haut de la fenêtre, il apparaîtrait
    décroché de ses zones de dépôt, exactement le défaut qu'on vient de
    corriger. On le repasse en `static`, c'est-à-dire à sa place naturelle ;
  · les animations de survol, qui décaleraient la carte d'un pixel.

Le rail « Mes outils » n'est PAS masqué : il occupe sa place et la carte
garde donc la largeur qu'elle a pour l'élève. Il tombe hors du cadre.
"""
import functools
import http.server
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import threading
import time

ICI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ICI)
RACINE = os.path.abspath(os.path.join(ICI, '..', '..'))
SORTIE = os.path.join(ICI, '_captures')
HARNAIS = os.path.join(RACINE, '_capture_harness.html')

CHROME = ('/Applications/Google Chrome.app/Contents/MacOS/Google Chrome')
LARGEUR = 1400      # largeur de fenêtre : le module en usage courant
BUDGET  = 9000      # temps virtuel accordé au chargement, en ms
ECHELLE = 2         # écran Retina — les captures sont projetées
REPOS   = 6         # secondes entre « c'est cadré » et l'arrêt de Chrome

HARNAIS_HTML = r"""<!doctype html><meta charset="utf-8"><title>capture</title>
<style>
  html,body{margin:0;padding:0;background:#F7F7F5}
  #clip{position:relative;overflow:hidden}
  #clip iframe{position:absolute;border:0}
  #manifeste{font:12px monospace;white-space:pre-wrap}
</style>
<div id="clip"></div><pre id="manifeste"></pre>
<script>
const P = new URLSearchParams(location.search);
const SLUG = P.get('m'), IDX = P.get('i'), MARGE = 14;
const clip = document.getElementById('clip');
const f = document.createElement('iframe');
f.width = %(W)d; f.height = 4000;
f.src = '/assets/interactive/' + SLUG + '/' + SLUG + '-activite-interactive.html';
clip.appendChild(f);

function preparer(){
  const d = f.contentDocument;
  const st = d.createElement('style');
  st.textContent = [
    '#chrome,#tabs{display:none!important}',
    '.bsec.b1{position:static!important;max-height:none!important;overflow:visible!important}',
    '.card{transition:none!important;transform:none!important}',
    'html{scroll-behavior:auto!important}'
  ].join('\n');
  d.head.appendChild(st);
  d.querySelectorAll('.sec').forEach(s => s.classList.add('on'));
  return [...d.querySelectorAll('.card')].filter(c => c.querySelector('.exo-row'));
}

function cadrer(carte){
  const d = f.contentDocument, w = f.contentWindow;
  w.scrollTo(0, 0);
  const r = carte.getBoundingClientRect();
  const x = Math.round(r.left + w.scrollX) - MARGE;
  const y = Math.round(r.top + w.scrollY) - MARGE;
  const cw = Math.ceil(r.width) + MARGE * 2, ch = Math.ceil(r.height) + MARGE * 2;
  clip.style.width = cw + 'px'; clip.style.height = ch + 'px';
  f.style.left = (-x) + 'px'; f.style.top = (-y) + 'px';
  f.height = y + ch + 100;
  return [cw, ch];
}

f.onload = () => setTimeout(() => {
  const cartes = preparer();
  if (IDX === null) {
    const m = cartes.map(c => {
      const [w, h] = cadrer(c);
      return {id: c.id.replace(/^exo-/, ''), w: w, h: h};
    });
    fetch('/_manifeste?m=' + SLUG, {method: 'POST', body: JSON.stringify(m)});
    clip.style.display = 'none';
  } else {
    cadrer(cartes[+IDX]);
    document.getElementById('manifeste').style.display = 'none';
    fetch('/_pret?m=' + SLUG);
  }
}, 900);
</script>
"""


# ── serveur de fichiers local ────────────────────────────────────────
MANIFESTES = {}
PRETS = set()


class Serveur(http.server.SimpleHTTPRequestHandler):
    """Sert le dépôt, recueille les manifestes et le signal « cadré »."""

    def log_message(self, *a):
        pass

    def do_GET(self):
        if self.path.startswith('/_pret'):
            PRETS.add(self.path.partition('m=')[2])
            self.send_response(204)
            return self.end_headers()
        return super().do_GET()

    def do_POST(self):
        if not self.path.startswith('/_manifeste'):
            return self.send_error(404)
        n = int(self.headers.get('Content-Length', 0))
        corps = self.rfile.read(n).decode('utf-8')
        slug = self.path.partition('m=')[2]
        MANIFESTES[slug] = json.loads(corps)
        self.send_response(204)
        self.end_headers()


def servir():
    """Les modules chargent leurs feuilles de style en chemin absolu
    (`/assets/…`) : un `file://` ne les trouverait pas. On sert le dépôt."""
    h = functools.partial(Serveur, directory=RACINE)
    # ThreadingHTTPServer, pas TCPServer : un module ouvre une dizaine de
    # requêtes en parallèle (styles, scripts, sons, images). Servi en file
    # unique, le chargement se bloque et Chrome ne rend jamais la page.
    srv = http.server.ThreadingHTTPServer(('127.0.0.1', 0), h)
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    return srv, srv.server_address[1]


def attendre(condition, limite):
    fin = time.time() + limite
    while time.time() < fin:
        if condition():
            return True
        time.sleep(0.2)
    return False


def chrome(url, taille, sortie, signal, artefact=None, limite=60):
    """Lance Chrome, attend que la page d'appoint dise « c'est cadré », puis
    le coupe.

    Sa sortie n'est pas un signal exploitable ici : tantôt il s'arrête avant
    que le module chargé dans le cadre ait fini de se rendre — capture
    blanche — tantôt il reste suspendu indéfiniment, page pourtant complète.
    C'est donc la page qui prévient (`/_pret`, `/_manifeste`).

    Et **la capture n'est écrite qu'à l'arrêt** : couper Chrome n'est pas un
    abandon, c'est ce qui déclenche l'écriture. D'où l'ordre : signal, court
    répit pour laisser le rendu se poser, arrêt, puis attente du PNG."""
    profil = tempfile.mkdtemp(prefix='cap-chrome-')
    cmd = [CHROME, '--headless', '--disable-gpu', '--hide-scrollbars',
           '--no-first-run', '--user-data-dir=' + profil,
           '--force-device-scale-factor=%d' % ECHELLE,
           '--window-size=%d,%d' % taille, '--virtual-time-budget=%d' % BUDGET,
           '--screenshot=' + sortie, url]
    p = subprocess.Popen(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    try:
        vu = attendre(lambda: signal() or p.poll() is not None, limite)
        if not vu:
            return False
        if artefact is None:
            return True
        # Chrome ne rendra pas la main : les modules gardent des chargements
        # en attente (les <audio> des dialogues) et la page n'est jamais
        # « terminée » à ses yeux. C'est l'arrêt qui écrit la capture — mais
        # le couper trop tôt n'écrit RIEN : mesuré, il lui faut quelques
        # secondes après le cadrage pour être en mesure de la prendre.
        time.sleep(REPOS)
        if p.poll() is None:
            p.terminate()
            try:
                p.wait(timeout=15)
            except subprocess.TimeoutExpired:
                p.kill()
        return attendre(artefact, 20)
    finally:
        if p.poll() is None:
            p.kill()
        shutil.rmtree(profil, ignore_errors=True)


def png_complet(chemin):
    """Un PNG se termine par son bloc IEND : tant qu'il n'y est pas, Chrome
    est encore en train d'écrire et l'image serait tronquée."""
    try:
        if os.path.getsize(chemin) < 1024:
            return False
        with open(chemin, 'rb') as f:
            # Les huit derniers octets d'un PNG : le nom du bloc final et son
            # empreinte. (Le bloc en fait douze ; les quatre premiers sont sa
            # longueur, qui vaut zéro et ne prouve rien.)
            f.seek(-8, os.SEEK_END)
            return f.read() == b'IEND\xae\x42\x60\x82'
    except OSError:
        return False


def manifeste(port, slug):
    MANIFESTES.pop(slug, None)
    jetable = os.path.join(tempfile.mkdtemp(prefix='cap-'), 'x.png')
    ok = chrome('http://127.0.0.1:%d/_capture_harness.html?m=%s' % (port, slug),
                (LARGEUR, 800), jetable, lambda: slug in MANIFESTES)
    if not ok:
        raise SystemExit('%s : aucun manifeste reçu — le module s\'est-il '
                         'chargé ?' % slug)
    return MANIFESTES[slug]


def produire(port, slug, cibles=None):
    fiches = manifeste(port, slug)
    dossier = os.path.join(SORTIE, slug)
    os.makedirs(dossier, exist_ok=True)
    faites = []
    for i, fi in enumerate(fiches):
        if cibles and fi['id'] not in cibles:
            continue
        png = os.path.join(dossier, fi['id'] + '.png')
        if os.path.exists(png):
            os.remove(png)
        PRETS.discard(slug)
        if not chrome('http://127.0.0.1:%d/_capture_harness.html?m=%s&i=%d'
                      % (port, slug, i), (fi['w'], fi['h']), png,
                      lambda: slug in PRETS,
                      artefact=lambda: png_complet(png)):
            raise SystemExit('%s / %s : capture non écrite' % (slug, fi['id']))
        controler(png, fi)
        faites.append(fi['id'])
        print('  %-12s %4d × %4d px' % (fi['id'], fi['w'], fi['h']))
    if cibles:
        manquants = set(cibles) - set(faites)
        if manquants:
            raise SystemExit('%s : exercice(s) introuvable(s) : %s'
                             % (slug, ', '.join(sorted(manquants))))
    return faites


def controler(png, fiche):
    """Une capture ratée est une capture uniforme : cadre mal posé, module
    pas encore rendu. On la refuse ici plutôt que de la découvrir projetée."""
    from PIL import Image
    with Image.open(png) as im:
        if im.size != (fiche['w'] * ECHELLE, fiche['h'] * ECHELLE):
            raise SystemExit('%s : taille inattendue %s' % (png, im.size,))
        # `getcolors` rend None au-delà du plafond : c'est le signe d'une
        # image RICHE, donc d'une capture réussie. Seule une palette courte
        # trahit un aplat — page pas encore peinte, cadre mal posé.
        palette = im.convert('RGB').getcolors(maxcolors=64)
        if palette is not None and len(palette) < 8:
            raise SystemExit('%s : image quasi uniforme — rendu incomplet' % png)


def main(argv):
    args = [a for a in argv if not a.startswith('--')]
    import modules
    if '--tous' in argv:
        slugs, cibles = list(modules.MODULES), None
    elif args:
        slugs, cibles = [args[0]], (args[1:] or None)
    else:
        raise SystemExit('Usage : python3 captures.py <module|--tous> [exos…]')
    for s in slugs:
        if s not in modules.MODULES:
            raise SystemExit('module inconnu : %s' % s)

    srv, port = servir()
    open(HARNAIS, 'w', encoding='utf-8').write(HARNAIS_HTML % {'W': LARGEUR})
    total = 0
    try:
        for slug in slugs:
            print(slug)
            total += len(produire(port, slug, cibles))
    finally:
        os.remove(HARNAIS)
        srv.shutdown()
    print('\nOK · %d capture(s) · %s' % (total, SORTIE))


if __name__ == '__main__':
    main(sys.argv[1:])
