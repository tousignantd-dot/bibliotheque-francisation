#!/usr/bin/env python3
"""Le débit demandé n'est pas le débit obtenu : on mesure, et on retire.

    python3 build/garde_debit.py --calibrer      # relit essai-ralenti, montre les bandes
    python3 build/garde_debit.py --essai         # produit 6 extraits sous garde

Le problème que ça règle
------------------------
Gemini n'a pas de SSML : la lenteur se demande en français (« lentement »,
« très lentement ») et non par un nombre. Les 15 tirages du 26 août 2026 ont
montré que ça marche — les trois paliers ne se recoupaient sur aucun tirage —
mais aussi qu'un tirage sur cinq dérape : `tres-lent-5` est sorti à 20,36 s
quand les quatre autres tenaient entre 15,5 et 16,8. Avec un écart-type de
1,88 s sur ce palier, un tirage à −2σ tomberait à 13,35 s, soit **sous** le
plus lent des « lent » (13,52 s). Sur quinze extraits ça n'arrive pas ; sur
les ~14 100 du cours, ça arrivera — et deux extraits voisins d'une même leçon
sortiraient alors dans le désordre, un « lent » plus rapide qu'un « normal ».

D'où ce garde-fou : on synthétise, on **mesure le MP3 obtenu**, et s'il tombe
du mauvais côté d'une frontière, on retire. Le mécanisme probabiliste redevient
déterministe pour environ un appel de plus sur dix.

Pourquoi les frontières et non un intervalle serré
--------------------------------------------------
La tentation est de borner chaque palier à ±2σ de sa moyenne. C'est une
mauvaise idée : ça fait retirer des extraits parfaitement audibles, seulement
un peu lents, et ça coûte cher pour rien. Ce qu'on veut empêcher n'est pas la
variation — c'est le **croisement**. Les bandes sont donc posées aux
mi-chemins entre les moyennes mesurées, et rien d'autre :

    normal 10,4 c/s ─────┬───── lent 7,6 c/s ─────┬───── très lent 5,6 c/s
                       9,0                      6,6

Un extrait n'est retiré que s'il franchit une de ces deux lignes, c'est-à-dire
s'il aurait vraiment pu passer pour un extrait du palier voisin. Tout le reste
est accepté tel quel.

Pourquoi on retire les silences avant de compter
------------------------------------------------
Un caractère par seconde calculé sur la durée brute du MP3 ne veut rien dire :
le silence de tête et de queue est à peu près constant, si bien qu'il pèse
lourd sur un mot isolé et presque rien sur une phrase longue. Le même débit
d'articulation donnerait alors 3 c/s sur « pain » et 10 c/s sur une phrase —
et le garde-fou retirerait tout le banc de vocabulaire sans raison. On mesure
donc la durée **parlée**, silences de bord retirés (`silencedetect`).

C'est la même leçon qu'au 25 août sur les voix ralenties d'ElevenLabs, où un
c/s brut avait fait conclure n'importe quoi.

Ce que le garde-fou ne fait pas
-------------------------------
Il ne juge ni l'accent, ni la justesse de la prononciation, ni l'épellation —
rien de tout cela ne se lit dans une durée. Il ne garantit que l'ordre des
paliers. Le reste passe par l'oreille.
"""
import json
import pathlib
import re
import subprocess
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))

# Débits mesurés le 26 août 2026 sur 5 tirages par palier (essai_ralenti.py),
# en caractères par seconde **parlée**. Les frontières sont les mi-chemins.
DEBITS = {"normal": 10.4, "lent": 7.6, "tres-lent": 5.6}

# (mini, maxi) en c/s. `None` = pas de borne de ce côté.
BANDES = {
    "normal":    (9.0, None),
    "lent":      (6.6, 9.0),
    "tres-lent": (None, 6.6),
}

# Hors de ces bornes, ce n'est plus un problème de débit mais un accident :
# un extrait vide, un texte avalé, une réponse tronquée. On retire aussi.
ABSURDE = (2.0, 22.0)

RETIRAGES = 3

# `silencedetect` a besoin d'un seuil. −40 dB laisse passer le souffle et la
# réverbération de fin de phrase sans les compter comme du silence ; 0,12 s
# est assez court pour attraper le blanc de tête, assez long pour ne pas
# découper les pauses internes d'une épellation.
SEUIL_DB = -40
DUREE_MIN_SILENCE = 0.12


def duree_totale(chemin):
    out = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "default=nw=1:nk=1", str(chemin)],
        capture_output=True, text=True)
    try:
        return float(out.stdout.strip())
    except ValueError:
        return 0.0


def bornes_parole(chemin, totale=None):
    """(début, fin) de la parole dans un MP3, silences de bord exclus.

    **Ne jamais repérer le silence de queue à ce qu'il soit « non refermé ».**
    C'était la première version, et elle produisait un rognage aléatoire : selon
    le fichier, `silencedetect` referme ou non le dernier silence à la fin du
    flux, si bien que le même extrait sortait tantôt à 1,14 s tantôt à 1,64 s.
    Sur une phrase, invisible ; sur une lettre seule du banc d'alphabet, c'est
    la moitié de la durée. On regarde donc **où** l'intervalle tombe, et non
    s'il est complet.
    """
    import re
    import subprocess
    chemin = str(chemin)
    if totale is None:
        totale = duree_totale(chemin)
    if totale <= 0:
        return 0.0, 0.0
    out = subprocess.run(
        ["ffmpeg", "-hide_banner", "-nostats", "-i", chemin,
         "-af", "silencedetect=noise=%ddB:d=%s" % (SEUIL_DB, DUREE_MIN_SILENCE),
         "-f", "null", "-"], capture_output=True, text=True).stderr
    debuts = [float(x) for x in re.findall(r"silence_start: (-?[\d.]+)", out)]
    fins = [float(x) for x in re.findall(r"silence_end: (-?[\d.]+)", out)]
    # Un silence ouvert et jamais refermé court jusqu'au bout du fichier.
    if len(fins) < len(debuts):
        fins = fins + [totale]
    inter = [(max(0.0, d), min(totale, f)) for d, f in zip(debuts, fins)]

    debut, fin = 0.0, totale
    if inter and inter[0][0] <= 0.05:
        debut = inter[0][1]
    if inter and inter[-1][1] >= totale - 0.05:
        fin = inter[-1][0]
    if fin <= debut:                       # extrait entièrement silencieux
        return 0.0, totale
    return debut, fin


def duree_parlee(chemin):
    """La durée du MP3 moins les silences de début et de fin seulement.

    Les silences internes restent comptés : une épellation est faite de pauses
    voulues, et les retirer donnerait le débit d'articulation au lieu du débit
    perçu — or c'est le temps que l'élève attend qu'on veut mesurer.
    """
    totale = duree_totale(chemin)
    if not totale:
        return 0.0
    d, f = bornes_parole(chemin, totale)
    return max(0.0, f - d)


def debit(chemin, texte):
    """Caractères par seconde parlée. 0 si le fichier ne dit rien."""
    d = duree_parlee(chemin)
    return (len(texte) / d) if d else 0.0


def juge(cs, palier):
    """(accepté, raison). La raison sert au journal, pas à l'utilisateur."""
    if cs <= 0:
        return False, "muet"
    if not (ABSURDE[0] <= cs <= ABSURDE[1]):
        return False, "absurde (%.1f c/s)" % cs
    bas, haut = BANDES[palier]
    if bas is not None and cs < bas:
        return False, "trop lent pour « %s » (%.1f < %.1f)" % (palier, cs, bas)
    if haut is not None and cs > haut:
        return False, "trop rapide pour « %s » (%.1f > %.1f)" % (palier, cs, haut)
    return True, "ok (%.1f c/s)" % cs


def ecart(cs, palier):
    """De combien on s'éloigne du débit visé — pour départager des ratés."""
    return abs(cs - DEBITS[palier])


def sous_garde(produire, texte, palier, dest, journal=None, retirages=RETIRAGES):
    """Produit un extrait et le retire tant qu'il franchit une frontière.

    `produire(dest)` est la fonction qui synthétise dans `dest` — le garde-fou
    ne connaît ni l'API ni la consigne, seulement le résultat. Après
    `retirages` échecs on **garde le tirage le moins mauvais** plutôt que de
    laisser un trou : un extrait un peu hors bande reste préférable à pas
    d'extrait, et le journal dit lesquels revoir.

    Renvoie (chemin, cs, accepté, appels) — `appels` est le nombre de
    synthèses **réellement payées**, et non le rang du meilleur tirage : c'est
    ce chiffre-là qui dit ce que le garde-fou coûte.
    """
    tmp = dest.with_suffix(".essai.mp3")
    meilleur = None
    appels = 0
    for i in range(1, retirages + 2):
        appels += 1
        produire(tmp)
        cs = debit(tmp, texte)
        ok, raison = juge(cs, palier)
        if meilleur is None or ecart(cs, palier) < ecart(meilleur[1], palier):
            tmp.replace(dest)
            meilleur = (dest, cs, ok)
        elif tmp.exists():
            tmp.unlink()
        if journal is not None:
            journal.append({"fichier": dest.name, "palier": palier,
                            "essai": i, "cs": round(cs, 2), "ok": ok,
                            "raison": raison})
        if ok:
            return dest, cs, True, appels
    return meilleur[0], meilleur[1], False, appels


def _calibrer():
    """Relit les 15 tirages de `essai_ralenti.py` et montre où tombent les bandes."""
    from essai_gemini_tts import PHRASE
    dossier = pathlib.Path.home() / "Claude" / "generations" / "essai-ralenti"
    if not dossier.exists():
        print("Lancer d'abord build/essai_ralenti.py")
        return 1
    print("%-14s %8s %8s %8s   %s" %
          ("fichier", "brute", "parlée", "c/s", "verdict"))
    par_palier = {}
    for f in sorted(dossier.glob("*.mp3")):
        palier = f.stem.rsplit("-", 1)[0]
        brute, parlee = duree_totale(f), duree_parlee(f)
        cs = len(PHRASE) / parlee if parlee else 0
        ok, raison = juge(cs, palier)
        par_palier.setdefault(palier, []).append(cs)
        print("%-14s %7.2fs %7.2fs %7.1f   %s %s"
              % (f.name, brute, parlee, cs, "✓" if ok else "✗", raison))
    print("\n%-12s %8s %8s %8s   bande" % ("palier", "moy", "min", "max"))
    for p, cs in par_palier.items():
        bas, haut = BANDES[p]
        print("%-12s %8.1f %8.1f %8.1f   %s – %s"
              % (p, sum(cs) / len(cs), min(cs), max(cs),
                 "%.1f" % bas if bas else "…", "%.1f" % haut if haut else "…"))
    retires = sum(1 for p, cs in par_palier.items()
                  for c in cs if not juge(c, p)[0])
    print("\n%d tirage(s) sur %d auraient été retirés."
          % (retires, sum(len(c) for c in par_palier.values())))
    return 0


def _essai():
    """Produit six extraits sous garde, deux par palier, et montre le journal."""
    from essai_gemini_tts import (PALIERS, PHRASE, Transitoire, avec_reprises,
                                  cle, synthese)
    k = cle()
    if not k:
        print("GOOGLE_API_KEY absente de ~/Claude/.env")
        return 1
    sortie = pathlib.Path.home() / "Claude" / "generations" / "essai-garde"
    sortie.mkdir(parents=True, exist_ok=True)
    journal = []
    for nom, consigne in PALIERS:
        for i in (1, 2):
            dest = sortie / ("%s-%d.mp3" % (nom, i))

            def produire(chemin, c=consigne):
                avec_reprises(lambda: synthese(c, PHRASE, "Kore", k, chemin))

            try:
                _, cs, ok, essais = sous_garde(produire, PHRASE, nom, dest,
                                               journal)
            except (Transitoire, subprocess.CalledProcessError) as e:
                print("  %-14s ÉCHEC %s" % (dest.name, e))
                continue
            print("  %-14s %5.1f c/s  %s  (%d essai%s)"
                  % (dest.name, cs, "✓" if ok else "✗ gardé quand même",
                     essais, "s" if essais > 1 else ""))
    (sortie / "journal.json").write_text(
        json.dumps(journal, ensure_ascii=False, indent=1))
    sup = len(journal) - len({j["fichier"] for j in journal})
    print("\n%d appels pour %d extraits — %d retirage(s), soit %+.0f %% de coût."
          % (len(journal), len({j["fichier"] for j in journal}), sup,
             sup / max(1, len({j["fichier"] for j in journal})) * 100))
    print("Journal : %s/journal.json" % sortie)
    return 0


if __name__ == "__main__":
    if "--calibrer" in sys.argv:
        sys.exit(_calibrer())
    if "--essai" in sys.argv:
        sys.exit(_essai())
    print(__doc__.strip().split("\n\n")[1])
    sys.exit(2)
