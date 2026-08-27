#!/usr/bin/env python3
"""Pose le garde-fou du confinement vocal sur les modules NON générés.

Les soixante-dix-sept modules bâtis par `build/module.py` reçoivent le
confinement du gabarit : `confiner_reconnaissance()` s'applique une fois dans
`build/gabarit.py`, et chaque reconstruction le reprend. Douze modules ne
passent pas par là — les deux sources du gabarit (`module-consultation` et
`module-logement`, qu'on ne peut pas régénérer sans tourner en rond) et dix
modules plus anciens qui ont leur propre HTML.

Ce script leur applique **exactement** les mêmes substitutions, importées de
`gabarit.py` plutôt que recopiées ici. Deux définitions du même garde-fou
finiraient par diverger, et la divergence est précisément ce qu'on ne peut pas
se permettre sur ce sujet : un module resté sur l'ancien geste enverrait la
voix de ses élèves sans que personne le voie.

    python3 build/greffe_confinement.py            # les modules non générés
    python3 build/greffe_confinement.py --un SLUG
    python3 build/greffe_confinement.py --etat     # qui est confiné, qui ne l'est pas

Chaque site est posé s'il existe, ignoré s'il est déjà là, et le script refuse
d'écrire un fichier où subsisterait un constructeur direct.
"""
import argparse
import io
import pathlib
import sys

BASE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(BASE))
ROOT = BASE.parent

import gabarit                                          # noqa: E402

# Les modules qui n'ont pas de `build/contenu/<slug>/` : leur HTML est la
# source, pas un produit. La liste est calculée, pas figée — un module neuf
# généré normalement n'a pas à être ajouté ici.
def non_generes():
    contenu = {p.name for p in (ROOT / "build/contenu").iterdir() if p.is_dir()}
    for d in sorted((ROOT / "assets/interactive").iterdir()):
        f = d / ("%s-activite-interactive.html" % d.name)
        if not d.is_dir() or not f.exists():
            continue
        if "SpeechRecognition" not in f.read_text(encoding="utf-8", errors="replace"):
            continue
        if d.name not in contenu:
            yield d.name


# Les sites, dans l'ordre où le gabarit les pose. Le premier porte le bloc
# commun : il est le seul obligatoire, puisque sans lui `reconnaissanceLocale`
# n'existe pas.
SITES = [
    ("prononciation", gabarit.OLD_PRON, gabarit.HELPER_RECO + gabarit.NEW_PRON),
    ("production orale", gabarit.OLD_ORAL, gabarit.NEW_ORAL),
    ("constante SR", "const SR = window.SpeechRecognition || window.webkitSpeechRecognition;\n", ""),
    ("constante jrSRC", "const jrSRC = () => window.SpeechRecognition || window.webkitSpeechRecognition;\n", ""),
    ("mode voix du jeu de rôle", gabarit.OLD_MODE, gabarit.NEW_MODE),
    ("micro du jeu de rôle", gabarit.OLD_PARLER, gabarit.NEW_PARLER),
]


# ── Les deux modules bâtis autrement ──────────────────────────────────────
# `cabine-sante` et `corrige-moi` n'ont pas de section de prononciation : le
# bloc commun n'a donc pas son point de chute habituel, et leur reconnaissance
# ne suit pas la forme du gabarit. Ils sont traités nommément plutôt
# qu'ignorés — deux modules laissés dehors, ce sont deux modules qui envoient
# la voix de leurs élèves pendant qu'on croit le flux fermé.
CAS_PARTICULIERS = {
    # La cabine reprend la forme du gabarit (MediaRecorder + reconnaissance en
    # parallèle), mais avec ses propres noms. Le bloc commun se pose à la place
    # du constructeur, et `canRecognize` devient une question au portail.
    "cabine-sante": [
        ("bloc commun",
         "const SR = window.SpeechRecognition || window.webkitSpeechRecognition;\n"
         "const canRecognize = !!SR;\n",
         None),                      # rempli plus bas : dépend de HELPER_RECO
        ("transcription en parallèle",
         """  mediaRecorder.start();

  // Transcription en parallèle (si disponible)
  if (canRecognize) {
    recognition = new SR();
    recognition.lang = 'fr-CA';
    recognition.continuous = true;
""",
         """  // Préparé AVANT mediaRecorder.start() : lancer la reconnaissance après
  // coup lui ferait manquer les premiers mots de l'élève.
  const reco = await reconnaissanceLocale('dictation');
  if (!reco.rec) {
    showError(recoMessage(reco.etat) + " L'enregistrement fonctionne quand même : écris ton texte à la main.");
  }
  mediaRecorder.start();

  // Transcription en parallèle, et seulement si elle reste sur l'appareil
  if (reco.rec) {
    recognition = reco.rec;
    recognition.continuous = true;
"""),
    ],
    # « Corrige-moi ! » construit sa reconnaissance une fois, au chargement, et
    # la réutilise. On garde ce cycle de vie — le refaire à chaque touche
    # perdrait ses écouteurs — et on pose la contrainte juste avant `start()`,
    # qui est le seul moment où elle est lue.
    "corrige-moi": [
        ("bloc commun",
         "const Ctor = window.SpeechRecognition || window.webkitSpeechRecognition;\n",
         None),
        ("démarrage du micro",
         """  if (!reco) return;
  if (state.ecoute) { reco.stop(); return; }
  state.erreur = '';
  try { reco.start(); } catch (e) { /* déjà démarré */ }
  renderZone();
""",
         """  if (!reco) return;
  if (state.ecoute) { reco.stop(); return; }
  state.erreur = '';
  // Le confinement se pose ici, pas à la construction : processLocally n'est
  // lu qu'au démarrage, et l'état du paquet de langue peut changer entre deux
  // touches (téléchargement en cours).
  const etat = await recoEtat('command');
  if (etat !== 'local' && etat !== 'distant') {
    state.erreur = recoMessage(etat);
    state.micDisponible = false;
    state.reponseVisible = true;
    renderZone();
    return;
  }
  try { reco.processLocally = (etat === 'local'); } catch (e) {}
  try { reco.start(); } catch (e) { /* déjà démarré */ }
  renderZone();
"""),
    ],
}

# Le remplacement du bloc commun dépend de HELPER_RECO : on le complète ici
# pour que la table reste lisible.
CAS_PARTICULIERS["cabine-sante"][0] = (
    "bloc commun",
    CAS_PARTICULIERS["cabine-sante"][0][1],
    gabarit.HELPER_RECO + "const canRecognize = !!RECO_SRC();\n")
CAS_PARTICULIERS["corrige-moi"][0] = (
    "bloc commun",
    CAS_PARTICULIERS["corrige-moi"][0][1],
    gabarit.HELPER_RECO + "const Ctor = RECO_SRC();\n")

# Ces deux modules appellent le portail depuis un écouteur : il doit attendre.
A_RENDRE_ASYNC = {
    "corrige-moi": ("$('micBtn').addEventListener('click', () => {",
                    "$('micBtn').addEventListener('click', async () => {"),
}


def confiner(html):
    """Rend (html, posés, absents). Ne décide rien : l'appelant tranche."""
    poses, absents = [], []
    for nom, ancien, neuf in SITES:
        if neuf and neuf in html:
            continue                       # déjà posé
        if html.count(ancien) == 1:
            html = html.replace(ancien, neuf)
            poses.append(nom)
        elif ancien not in html:
            absents.append(nom)
        else:
            raise ValueError("« %s » apparaît %d fois — ancre ambiguë"
                             % (nom, html.count(ancien)))
    return html, poses, absents


def chemin(slug):
    return ROOT / "assets/interactive" / slug / ("%s-activite-interactive.html" % slug)


def poser(slug):
    f = chemin(slug)
    s = io.open(f, encoding="utf-8").read()
    if "reconnaissanceLocale" in s:
        return "déjà confiné", []
    if slug in CAS_PARTICULIERS:
        poses = []
        for nom, ancien, neuf in CAS_PARTICULIERS[slug]:
            if s.count(ancien) != 1:
                return "ancre « %s » introuvable ou ambiguë" % nom, poses
            s = s.replace(ancien, neuf)
            poses.append(nom)
        if slug in A_RENDRE_ASYNC:
            ancien, neuf = A_RENDRE_ASYNC[slug]
            if s.count(ancien) != 1:
                return "écouteur à rendre async introuvable", poses
            s = s.replace(ancien, neuf)
            poses.append("écouteur asynchrone")
    elif gabarit.OLD_PRON not in s:
        # Sans le site de prononciation ni cas nommé, le bloc commun n'a pas de
        # point de chute : ce module-là demande une main, pas une greffe.
        return "structure différente", []
    else:
        s, poses, _ = confiner(s)
    reste = (s.count("new SRC()") + s.count("new SR()")
             + s.count("new Ctor()") - (1 if slug == "corrige-moi" else 0))
    if reste:
        return "refusé : %d constructeur(s) restant(s)" % reste, poses
    io.open(f, "w", encoding="utf-8").write(s)
    return "confiné", poses


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--un", metavar="SLUG")
    ap.add_argument("--etat", action="store_true",
                    help="dire qui est confiné sans rien écrire")
    args = ap.parse_args()

    if args.etat:
        inter = ROOT / "assets/interactive"
        nus = []
        for d in sorted(inter.iterdir()):
            f = d / ("%s-activite-interactive.html" % d.name)
            if not d.is_dir() or not f.exists():
                continue
            s = f.read_text(encoding="utf-8", errors="replace")
            if "SpeechRecognition" not in s:
                continue
            if "reconnaissanceLocale" not in s:
                nus.append(d.name)
        print("%d module(s) encore sans confinement" % len(nus))
        for n in nus:
            print("   ", n)
        return 1 if nus else 0

    cibles = [args.un] if args.un else list(non_generes())
    ennui = 0
    for slug in cibles:
        etat, poses = poser(slug)
        print("%-24s %-32s %s" % (slug, etat, ", ".join(poses)))
        if etat.startswith("refusé") or etat == "structure différente":
            ennui = 1
    return ennui


if __name__ == "__main__":
    sys.exit(main())
