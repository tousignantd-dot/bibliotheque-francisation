#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Les captures de la trousse qui demandent un geste avant d'exister.

    python3 build/captures_trousse.py            # toutes
    python3 build/captures_trousse.py minilecon  # une seule

Les 45 captures de `assets/presentations/captures-*/` montrent des écrans **au
repos** : on ouvre une page, on photographie. Certaines choses n'existent
pourtant qu'après un geste — la mini-leçon ne s'ouvre pas toute seule, elle
s'ouvre quand l'élève s'est trompé. Or c'est précisément l'idée que le
diaporama F1 doit montrer.

**Comment.** `--screenshot` de Chrome ne sait pas exécuter de script à nous. On
charge donc le module dans un cadre, depuis une page d'appoint de même origine
qui peut appeler ses fonctions (`plusOpen`, `render`), puis on prévient le
serveur que c'est cadré. C'est exactement la mécanique de
`build/powerpoints/captures.py`, dont ce script **réemploie le serveur et le
lanceur** plutôt que d'en écrire une seconde version : les trois pièges de
Chrome sans interface y sont déjà payés (il ne rend jamais la main sur ces
modules, la capture ne s'écrit qu'à l'arrêt, et le couper trop tôt n'écrit
rien).

Les images vont dans `assets/presentations/captures-cas/`, avec les autres
captures d'écran du portail — c'est leur nature, pas leur provenance, qui
décide du dossier.
"""

import os
import pathlib
import sys

ICI = pathlib.Path(__file__).resolve().parent
RACINE = ICI.parent
sys.path.insert(0, str(ICI / 'powerpoints'))

import captures as cap  # noqa: E402

SORTIE = RACINE / 'assets' / 'presentations' / 'captures-cas'
LARGEUR_MAX = 1200      # la largeur des autres captures du dossier

# Une entrée = un nom de fichier, un module, la taille de la fenêtre, et le
# geste à faire dans le cadre. Le geste est du JavaScript exécuté **dans** le
# module : il a accès à ses fonctions globales.
CAPTURES = {
    'minilecon': dict(
        nom='14-minilecon',
        module='module-probleme/module-probleme-activite-interactive.html',
        taille=(1200, 1500),
        # « Leur ou leurs : ce qui décide vraiment ». Sa première section
        # s'appelle « L'erreur de départ à corriger » : c'est la mini-leçon
        # qui illustre le mieux « la règle arrive quand l'élève s'est trompé ».
        geste="w.curSec='t1'; w.render(); w.plusOpen('t1leur');",
    ),
}

APPOINT = """<!doctype html>
<meta charset="utf-8">
<title>appoint</title>
<style>html,body{margin:0;height:100%%;overflow:hidden;background:#fff}
 iframe{border:0;display:block;width:100vw;height:100vh}</style>
<iframe id="f" src="/assets/interactive/%(module)s"></iframe>
<script>
  var f = document.getElementById('f');
  f.onload = function(){
    /* Le module charge ses sons et ses images après son script : deux secondes
       et demie avant d'agir, sinon `render()` court sur une page à moitié
       montée et la mini-leçon s'ouvre sur du vide. */
    setTimeout(function(){
      try { var w = f.contentWindow; %(geste)s } catch (e) {}
      /* Puis on laisse la surimpression finir son ouverture avant de dire
         « c'est cadré » — sans quoi on photographie son fondu. */
      setTimeout(function(){ fetch('/_pret?m=%(cle)s'); }, 1400);
    }, 2500);
  };
</script>
"""


def produire(cle, spec, port):
    appoint = RACINE / ('_capture_%s.html' % cle)
    appoint.write_text(APPOINT % dict(module=spec['module'], geste=spec['geste'],
                                      cle=cle), encoding='utf-8')
    cible = SORTIE / (spec['nom'] + '.png')
    url = 'http://127.0.0.1:%d/%s' % (port, appoint.name)
    try:
        ok = cap.chrome(url, spec['taille'], str(cible),
                        signal=lambda: cle in cap.PRETS,
                        artefact=lambda: cible.exists() and cible.stat().st_size > 0)
    finally:
        appoint.unlink(missing_ok=True)
    if not ok or not cible.exists():
        print('  !! %s : rien produit' % cle)
        return None
    # Le dossier est en JPEG : une capture d'écran de portail y pèse 60 à
    # 200 Ko au lieu de 900. Le PNG intermédiaire ne survit pas.
    #
    # Et on la ramène à la largeur de ses voisines. `captures.py` tire à
    # l'échelle 2 — bon pour un exercice projeté plein cadre, deux fois trop
    # pour une capture qui occupe un tiers d'écran dans un diaporama. Sans
    # cette réduction, elle pesait 449 Ko contre 60 pour les autres.
    from PIL import Image
    jpg = cible.with_suffix('.jpg')
    with Image.open(cible) as im:
        if im.width > LARGEUR_MAX:
            h = round(im.height * LARGEUR_MAX / im.width)
            im = im.resize((LARGEUR_MAX, h), Image.LANCZOS)
        im.convert('RGB').save(jpg, quality=86, optimize=True)
    taille = jpg.stat().st_size
    cible.unlink()
    print('  %-14s %s  (%d Ko)' % (cle, jpg.name, taille // 1024))
    return jpg


def main(argv):
    voulues = argv or sorted(CAPTURES)
    inconnues = [c for c in voulues if c not in CAPTURES]
    if inconnues:
        raise SystemExit('!! capture inconnue : %s\n   Connues : %s'
                         % (', '.join(inconnues), ', '.join(sorted(CAPTURES))))
    srv, port = cap.servir()
    try:
        faites = [produire(c, CAPTURES[c], port) for c in voulues]
    finally:
        srv.shutdown()
    return 0 if all(faites) else 1


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
