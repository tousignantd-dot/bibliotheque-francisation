#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Les quatre captures réelles du film de 90 secondes.

    PORT=55711 python3 build/film_90_captures.py

Le film montre le produit **tel qu'il est** : quatre de ses quatorze plans sont
donc des captures, pas des dessins. Elles vieilliront avec lui, c'est voulu.

**On ne passe par aucune API.** Le jeu de rôle appelle `/api/jeu-de-role` et
`/api/voix`, qui exigent un code d'élève valide et coûtent de l'argent à chaque
appel. Or tout ce qu'on veut photographier est du DOM : `jrDemarrer()` ouvre la
conversation, `jrBulle()` y pose une réplique, `renderCorr()` dessine la carte
de rétroaction. On met donc la scène en place à la main, avec du contenu écrit
pour l'occasion — et aucun vrai nom, comme partout ailleurs.

Le cadrage se fait en **masquant ce qui précède la cible**, jamais en faisant
défiler : sous `--virtual-time-budget`, l'horloge de Chrome avance plus vite
que le rendu et un défilement n'arrive jamais à destination.
"""

import pathlib
import sys

RACINE = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RACINE / "build"))
from capture_ecran import capture           # noqa: E402

SORTIE = RACINE / "assets" / "presentations" / "film-90-secondes"
MODULE = ("assets/interactive/module-n8-habitation/"
          "module-n8-habitation-activite-interactive.html")

# Le décor : la contestation d'un refus de réclamation, niveau 8. C'est le
# module que l'utilisateur avait sous les yeux quand le défaut de son a été
# trouvé — autant que le film montre celui-là.
MOI = ("Bonjour, j'appelle au sujet de ma réclamation. J'ai reçu une lettre "
       "qui refuse le remboursement du dégât d'eau.")
ELLE = ("Je comprends. Pouvez-vous me donner votre numéro de dossier ? "
        "Je vais regarder ce qui a été décidé, et pourquoi.")

# ── La mise en scène, apprise à l'écran et non devinée ─────────────────────
# Trois obstacles, dans cet ordre, et aucun ne lève d'erreur :
#
#  1. Le module ne rend QUE la section courante ; le jeu de rôle vit dans
#     « Je me lance ». Il faut poser `curSec` puis appeler `render()` — qui ne
#     prend aucun argument, c'est écrit dans CLAUDE.md.
#  2. **Sans code d'élève, le module se replie en mode sans assistance** : le
#     `body` porte `sans-ia`, et la carte du jeu de rôle est masquée. C'est le
#     repli voulu, et c'est lui qui rendait la première capture BLANCHE.
#  3. Le cadrage ne se fait ni par défilement (l'horloge de Chrome avance plus
#     vite que le rendu) ni par masquage des ancêtres (on masque sa propre
#     cible) : on **sort l'élément visé** dans le `body` et on retire le reste.
#     La capture prend le viewport, donc le haut de l'élément.
SCENE = """
  document.body.classList.remove('sans-ia', 'depot-ferme');
  var sec = document.getElementById('jrChat').closest('.sec');
  if (sec) { curSec = sec.id.replace(/^sec-/, ''); render(); }
  document.getElementById('jeu-de-role').style.display = '';
  // On neutralise le tour de parole AVANT d'ouvrir la conversation : sans
  // code d'élève, /api/jeu-de-role répond 401 et la carte affiche un bandeau
  // rouge « Non autorisé » — qui est apparu sur la première planche. Le
  // neutraliser vaut mieux que masquer l'erreur après coup : aucun appel ne
  // part, donc rien à cacher et rien à payer.
  window.jrTour = function () {};
  jrDemarrer();
"""

def cadrer(js_cible):
    return """
  var cible = %s;
  document.body.appendChild(cible);
  Array.prototype.slice.call(document.body.children).forEach(function (n) {
    if (n !== cible) n.remove();
  });
  // Centré dans le cadre : la capture prend le viewport en 16:9, et un bloc\n  // collé en haut laisse un tiers de vide que le montage ne peut pas rattraper.\n  document.body.style.cssText = 'margin:0;padding:40px;background:#F7F7F5;'\n    + 'min-height:100vh;display:flex;align-items:center;justify-content:center';
  cible.style.margin = '0 auto'; cible.style.maxWidth = '1020px';
  window.scrollTo(0, 0);
""" % js_cible


PLANS = [
    ("05", "Il choisit, et il parle", SCENE + """
        document.getElementById('jrFil').style.display = 'none';
        document.getElementById('jrMicZone').classList.remove('hidden');
        """ + cadrer("document.getElementById('jeu-de-role')")),
    ("06", "Quelqu'un répond", SCENE + """
        jrBulle('moi', %s);
        jrBulle('ia', %s);
        document.getElementById('jrMicZone').classList.remove('hidden');
        document.getElementById('jrMic').classList.add('rec');
        """ % (repr(MOI), repr(ELLE)) + cadrer("document.getElementById('jrChat')")),
    ("08", "Ce qu'il a dit, et comment", SCENE + """
        jrBulle('moi', %s);
        renderCorr('jrFb', {corrige: %s,
          erreurs: [{explication: "On dit « au sujet de », pas « à propos que » : devant un nom, c'est la forme juste."},
                    {explication: "« une lettre qui refuse » se dit mieux « une lettre de refus » — plus court, et c'est le mot qu'emploie l'assureur."}]}, '');
        """ % (repr(MOI), repr(
        "Bonjour, j'appelle au sujet de ma réclamation. J'ai reçu une lettre "
        "de refus pour le remboursement du dégât d'eau.")) +
     cadrer("document.getElementById('jrFb')")),
]


# ── Le plan 11 : le tableau du groupe ─────────────────────────────────────
# Celui-ci ne vit pas dans un module : c'est `progression.html`, derrière la
# connexion enseignante. Deux choses le rendent capturable :
#
#  · **un jeton de session posé dans le `localStorage` avant que la page ne
#    lise**, donc suivi d'un rechargement — la mise en scène se rejoue au
#    chargement suivant, d'où le garde qui l'empêche de boucler ;
#  · **la classe de présentation** (`build/demo_classe.py --install`), sans
#    laquelle le tableau s'affiche parfaitement… et entièrement vide, ce qui
#    ferait un mauvais plan pour un film qui dit « l'enseignante voit son
#    groupe ». Ses quinze élèves portent des pseudonymes — Alouette, Bambou,
#    Cactus — comme le veut le portail : aucun vrai nom n'entre dans le film.
#
# Le jeton se lit dans data/prof_sessions.json ; il n'est jamais écrit ici.
PROGRESSION = "progression.html"


def scene_progression():
    """Ne fait plus que cadrer : le jeton est posé dans l'ENTÊTE, voir plus bas."""
    return """
  var t = document.querySelector('.pg-scroll') || document.querySelector('table');
  if (t) {
    document.body.appendChild(t);
    Array.prototype.slice.call(document.body.children).forEach(function (n) {
      if (n !== t) n.remove();
    });
    document.body.style.cssText = 'margin:0;padding:34px;background:#F7F7F5;'
      + 'min-height:100vh;display:flex;align-items:center;justify-content:center';
    t.style.margin = '0 auto'; t.style.maxWidth = '1500px';
    window.scrollTo(0, 0);
  }
"""


def copie_connectee(jeton):
    """`progression.html` avec la session déjà ouverte, posée DANS L'ENTÊTE.

    Le premier essai posait le jeton dans la mise en scène, que
    `capture_ecran.py` injecte avant `</body>` — donc APRÈS `js/prof.js`, qui
    voit une session absente, appelle le serveur, prend un 401 et **redirige
    vers l'écran de connexion**. La planche est revenue avec le formulaire de
    connexion, parfaitement nette et parfaitement inutile. Le `localStorage`
    doit donc être écrit avant que le premier script de la page ne lise.
    """
    src = RACINE / PROGRESSION
    copie = RACINE / "_film90-progression.html"
    t = src.read_text(encoding="utf-8")
    pose = ("<script>try{localStorage.setItem('prof_token',%s);"
            "localStorage.setItem('prof_groupe_actif','1');}catch(e){}</script>"
            % repr(jeton))
    i = t.lower().index("<head>") + len("<head>")
    copie.write_text(t[:i] + "\n" + pose + t[i:], encoding="utf-8")
    return copie


def jeton_local():
    """Une session enseignante encore valide, prise sur le disque."""
    import datetime
    import json
    f = RACINE / "data" / "prof_sessions.json"
    if not f.exists():
        return None
    now = datetime.datetime.now().isoformat(timespec="seconds")
    for j, v in json.loads(f.read_text()).items():
        if v.get("expiresAt", "") > now:
            return j
    return None


def main():
    SORTIE.mkdir(parents=True, exist_ok=True)
    for num, titre, scene in PLANS:
        dest = SORTIE / ("plan-%s.png" % num)
        print("  %s · %s …" % (num, titre), end="", flush=True)
        capture(MODULE, dest, mise_en_scene=scene, largeur=1600, hauteur=900,
                echelle=1.5, delai_js=1800)
        ok = dest.exists() and dest.stat().st_size > 20000
        print(" %s" % ("%d ko" % (dest.stat().st_size // 1000) if ok else "ÉCHEC"))

    jeton = jeton_local()
    print("  11 · C'est elle qui décide …", end="", flush=True)
    if not jeton:
        print(" SAUTÉ — aucune session enseignante valide sur le disque")
        return 1
    dest = SORTIE / "plan-11.png"
    copie = copie_connectee(jeton)
    try:
        capture(copie.name, dest, mise_en_scene=scene_progression(),
                largeur=1600, hauteur=900, echelle=1.5, delai_js=5000)
    finally:
        copie.unlink(missing_ok=True)
    ok = dest.exists() and dest.stat().st_size > 20000
    print(" %s" % ("%d ko" % (dest.stat().st_size // 1000) if ok else "ÉCHEC"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
