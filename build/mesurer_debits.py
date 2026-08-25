#!/usr/bin/env python3
"""Mesure le débit d'articulation de chaque voix — la table `DEBIT` de `voix_lente`.

    python3 build/mesurer_debits.py [--n 150]

**Ce qu'on mesure : des caractères par seconde de PAROLE**, silences de tête
et de queue retirés. Les deux mesures plus simples sont fausses, et toutes
deux ont été essayées le 25 août 2026 avant d'arriver ici :

- *Caractères ÷ durée du fichier.* Le silence de tête et de queue vaut 0,33 à
  0,37 s quelle que soit la voix. Sur une réplique de niveau 1 qui fait deux
  secondes, c'est un sixième du fichier ; sur une réplique de niveau 8, un
  vingtième. Le chiffre monte donc avec la longueur du texte sans que personne
  ait parlé plus vite, et deux voix ne sont comparables par ce chiffre que si
  leurs répliques ont la même longueur — ce qui n'arrive jamais.
- *Régression durée ≈ a + b × caractères.* L'ordonnée à l'origine est censée
  absorber les silences, mais elle est mal estimée dès que les distributions
  de longueur diffèrent : elle sort à 0,73 s pour l'enseignante contre −0,16 s
  pour la féminine #2, deux valeurs que la mesure directe dément.

Les répliques de l'enseignante sont lues telles qu'elles sont sur le disque,
donc déjà ralenties : leur durée est remise au brut en la multipliant par
`FACTEUR`. Les voix de dialogue sont lues dans `.audio-originaux/`.

Le script affiche aussi la dispersion. Elle compte autant que la médiane :
tant que l'étendue p10-p90 d'une voix dépasse largement l'écart entre les
médianes, calibrer par voix ne peut corriger que le petit axe.
"""
import os
import random
import re
import statistics
import subprocess
import sys
import tempfile
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RACINE))
sys.path.insert(0, str(RACINE / "build"))
from voix_lente import DEBIT, FACTEUR, VOIX_ENSEIGNANTE   # noqa: E402
from ralentir_dialogues import voix_par_slug, GENERATEUR, slug_gabarit  # noqa: E402

NOMS = {VOIX_ENSEIGNANTE: "enseignante",
        "WW0JfNPk5DgcQdM0d6X6": "féminine #2",
        "93nuHbke4dTER9x2pDwE": "masculin #1",
        "IPgYtHTNLjC7Bq7IPHrm": "narrateur"}
ORIGINAUX = RACINE / ".audio-originaux"


def duree(chemin):
    r = subprocess.run(["ffprobe", "-v", "error", "-show_entries",
                        "format=duration", "-of", "csv=p=0", str(chemin)],
                       capture_output=True, text=True)
    try:
        return float(r.stdout.strip())
    except ValueError:
        return None


def duree_parole(chemin):
    """La durée une fois les silences des deux bouts retirés."""
    tmp = tempfile.mktemp(suffix=".wav")
    coupe = ("silenceremove=start_periods=1:start_threshold=-45dB:"
             "start_silence=0:detection=peak")
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(chemin),
                    "-af", "%s,areverse,%s,areverse" % (coupe, coupe), tmp],
                   capture_output=True)
    d = duree(tmp)
    if os.path.exists(tmp):
        os.unlink(tmp)
    return d


def repliques():
    """(fichier à mesurer, nombre de caractères, voix) pour tout le dépôt."""
    for dossier in sorted((RACINE / "assets/interactive").iterdir()):
        if not dossier.is_dir():
            continue
        dialogues = RACINE / "build/contenu" / dossier.name / "dialogues.js"
        gen = RACINE / GENERATEUR.get(
            dossier.name, "generer_audio_%s.py" % dossier.name.replace("-", "_"))
        if not dialogues.exists() or not gen.exists():
            continue
        par = voix_par_slug(gen)
        if not par:
            continue
        src = dialogues.read_text(encoding="utf-8")
        blocs = list(re.finditer(r'^  (\w+): \{', src, re.M))
        for i, b in enumerate(blocs):
            deb = b.end()
            fin = blocs[i + 1].start() if i + 1 < len(blocs) else len(src)
            for j, (perso, texte) in enumerate(
                    re.findall(r'\["([^"]+)","((?:[^"\\]|\\.)*)"\]', src[deb:fin]), 1):
                f = dossier / b.group(1) / ("line_%02d_%s.mp3" % (j, slug_gabarit(perso)))
                voix = par.get(slug_gabarit(perso))
                if voix not in NOMS or not f.exists():
                    continue
                # l'enseignante est ralentie sur place ; les autres ont leur
                # original. `f` est absolu : le joindre tel quel à ORIGINAUX
                # rendrait `f` lui-même — pathlib écrase à gauche d'un chemin
                # absolu — et on mesurerait le fichier déjà ralenti.
                chemin = (f if voix == VOIX_ENSEIGNANTE
                          else ORIGINAUX / f.relative_to(RACINE))
                if chemin.exists():
                    niv = re.match(r"module-n(\d)-", dossier.name)
                    case = 0 if (niv and int(niv.group(1)) <= 2) else 1
                    yield chemin, len(texte.replace('\\"', '"')), voix, case


def main():
    n = int(sys.argv[sys.argv.index("--n") + 1]) if "--n" in sys.argv else 150
    par_voix = {}
    for chemin, cars, voix, case in repliques():
        par_voix.setdefault((voix, case), []).append((chemin, cars))
    random.seed(5)
    print("Débit d'articulation, silences retirés — %d répliques par voix\n" % n)
    print("  %-8s %-14s %5s %7s %7s %8s %7s %7s" %
          ("palier", "voix", "n", "p10", "p25", "médiane", "p75", "p90"))
    medianes, etendues = {}, []
    for (voix, case), items in sorted(par_voix.items(),
                                      key=lambda kv: (kv[0][1], NOMS[kv[0][0]])):
        taux = []
        for chemin, cars in random.sample(items, min(n, len(items))):
            d = duree_parole(chemin)
            if not d or d < 0.3:
                continue
            if voix == VOIX_ENSEIGNANTE:
                d *= FACTEUR            # revenir au débit brut
            taux.append(cars / d)
        taux.sort()
        q = lambda k: taux[int(k * (len(taux) - 1))]     # noqa: E731
        medianes[(voix, case)] = q(.50)
        etendues.append(q(.90) - q(.10))
        print("  %-8s %-14s %5d %7.1f %7.1f %8.1f %7.1f %7.1f"
              % ("n1-n2" if case == 0 else "n3+", NOMS[voix], len(taux),
                 q(.10), q(.25), q(.50), q(.75), q(.90)))
    par_palier = [max(v for (_, c), v in medianes.items() if c == case)
                  - min(v for (_, c), v in medianes.items() if c == case)
                  for case in (0, 1)]
    inter = max(par_palier)
    intra = statistics.mean(etendues)
    print("\n  écart ENTRE voix (médianes)     : %.1f c/s" % inter)
    print("  étendue DANS une voix (p10-p90) : %.1f c/s — %.1f fois plus"
          % (intra, intra / inter))
    print("\nTable `DEBIT` de voix_lente, à comparer à ce qui précède :")
    for voix, paire in DEBIT.items():
        for case in (0, 1):
            mesure = medianes.get((voix, case))
            marque = ("" if mesure is None or abs(mesure - paire[case]) < 0.4
                      else "   ← à mettre à jour")
            print("    %-8s %-14s table %.1f   mesuré %s%s"
                  % ("n1-n2" if case == 0 else "n3+", NOMS[voix], paire[case],
                     "%.1f" % mesure if mesure else "—", marque))


if __name__ == "__main__":
    main()
