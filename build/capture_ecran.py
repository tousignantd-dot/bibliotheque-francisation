#!/usr/bin/env python3
"""Capture d'un écran réel du portail, via Chrome sans interface.

Le volet d'aperçu rend en 800 px de large : trop peu pour une planche de
storyboard. Chrome accepte un facteur d'échelle, donc on passe par lui.

Le montage : on dépose à côté du fichier visé une copie portant un script de
mise en scène (ouvrir le bon onglet, cliquer, faire défiler), on la
photographie, on la supprime. La copie vit dans le même dossier pour que les
chemins relatifs — sons, icônes — continuent de résoudre.

`--headless=new` ne rend jamais la main sur ces pages ; `--headless=old`
écrit le fichier puis s'attarde. On attend donc l'apparition du fichier et on
tue le processus, plutôt que d'attendre sa sortie.
"""
import os, pathlib, shutil, subprocess, sys, tempfile, time

CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
BASE = pathlib.Path.home() / "Claude" / "bibliotheque-francisation"
PORT = os.environ.get("PORT", "64171")


def capture(source_rel, sortie, mise_en_scene="", largeur=1600, hauteur=900,
            echelle=1.5, delai_js=1400, attente=70):
    src = BASE / source_rel
    copie = src.with_name("_capture-temporaire.html")
    sortie = pathlib.Path(sortie)
    sortie.unlink(missing_ok=True)
    # Sous `--virtual-time-budget`, l'horloge avance plus vite que le rendu :
    # un défilement doux n'arrive jamais à destination et la capture attrape
    # une bande vide. On coupe donc toute transition et tout défilement animé
    # avant de mettre en scène.
    script = ("\n<style>*{transition:none!important;animation:none!important}"
              "html,body{scroll-behavior:auto!important}</style>"
              "<script>window.addEventListener('load',function(){setTimeout(function(){"
              "try{" + mise_en_scene + "}catch(e){console.error(e)}"
              "},%d)});</script>\n" % delai_js)
    copie.write_text(src.read_text(encoding="utf-8").replace("</body>", script + "</body>"),
                     encoding="utf-8")
    url = "http://localhost:%s/%s" % (PORT, copie.relative_to(BASE).as_posix())
    tmp = tempfile.mkdtemp()
    proc = subprocess.Popen([CHROME, "--headless=old", "--disable-gpu", "--no-sandbox",
                             "--mute-audio", "--hide-scrollbars", "--no-first-run",
                             "--window-size=%d,%d" % (largeur, hauteur),
                             "--force-device-scale-factor=%s" % echelle,
                             "--virtual-time-budget=%d" % (delai_js + 4000),
                             "--screenshot=%s" % sortie,
                             "--user-data-dir=%s" % tmp, url],
                            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    try:
        for _ in range(attente * 2):
            if sortie.exists() and sortie.stat().st_size > 5000:
                time.sleep(0.6)
                break
            time.sleep(0.5)
    finally:
        proc.kill()
        copie.unlink(missing_ok=True)
        shutil.rmtree(tmp, ignore_errors=True)
    if not sortie.exists():
        raise RuntimeError("aucune capture pour %s" % source_rel)
    from PIL import Image
    im = Image.open(sortie)
    print("  %s  %dx%d" % (sortie.name, im.width, im.height))
    return sortie
