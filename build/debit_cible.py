#!/usr/bin/env python3
"""Ramener chaque extrait parlé sous un débit cible, extrait par extrait.

    python3 build/debit_cible.py module-probleme --etat
    python3 build/debit_cible.py module-probleme --cible 14
    python3 build/debit_cible.py --tous --cible 14

`voix_lente.py` calibre **par voix** : un facteur unique par locuteur et par
palier, qui vise 0,90 × 19,4 ≈ 17,5 c/s au niveau 4. Deux choses lui échappent.

1. La cible elle-même est un débit de conversation, pas d'apprentissage.
2. Surtout, ElevenLabs décide du débit d'après le *texte* autant que d'après le
   locuteur. Dans le dialogue « Je découvre » du module 9, mesuré le 29 août
   2026 : 14,4 c/s à la réplique 1 et **21,0 à la réplique 4**, même actrice,
   même scène — 46 % d'écart. Aucun facteur global ne rattrape ça : il
   descend tout le monde d'autant et laisse la réplique 4 la plus rapide.

D'où le plafond par réplique, identifié le 25 août et jamais posé : on mesure
chaque extrait et on ne freine que ceux qui dépassent.

    facteur = min(1, cible / débit mesuré)

Un extrait déjà sous la cible n'est pas touché — on ne presse jamais une voix
posée, et on ne l'étire pas non plus pour « faire pareil ».

**Le mesurage.** Un débit en caractères ÷ durée du fichier ne veut rien dire :
le silence de tête et de queue vaut 0,33-0,37 s quel que soit l'extrait, donc
un sixième d'une réplique courte et un vingtième d'une longue. On retire donc
les silences aux deux bouts avant de diviser.

**Les textes trop courts ne sont pas mesurables.** Sur « deux » ou « odeur »,
le rapport caractères/seconde ne dit rien de la vitesse d'élocution : il dit
la longueur du mot. Les extraits sous `--mini-caracteres` sont laissés tels
quels — ce sont d'ailleurs des mots isolés, prononcés exprès avec soin.

**On repart toujours de l'original.** Étirer un fichier déjà étiré additionne
les artefacts. Les originaux sont dans `.audio-originaux/` ; à défaut, le
fichier livré fait foi. Ce qui a été produit est noté dans `.audio-debit.json`
— relancer l'outil avec la même cible ne refait rien.
"""

import argparse
import io
import json
import os
import re
import shutil
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
INTERACTIF = BASE / "assets" / "interactive"
ORIGINAUX = BASE / ".audio-originaux"
REGISTRE = BASE / ".audio-debit.json"

CIBLE_DEFAUT = 14.0
MINI_CARACTERES = 40


# ── Les textes ────────────────────────────────────────────────────────────

def _dejs(brut):
    """Déséchappe une chaîne littérale JS sans toucher aux accents.

    `texte.encode().decode("unicode_escape")` lit les octets en latin-1 :
    « degrés » en ressort « degrÃ©s », soit un caractère de plus par accent,
    donc un débit surestimé sur tout texte français. `json.loads` connaît les
    mêmes échappements et respecte l'unicode.
    """
    try:
        return json.loads('"%s"' % brut)
    except ValueError:
        return brut


def textes_dialogues(slug):
    """{(bloc, rang) : texte} d'après build/contenu/<slug>/dialogues.js.

    Le rang vient du **nom du fichier**, jamais du compte : des dossiers
    commencent à `line_02`, et compter les fichiers décale tout le dialogue.
    """
    f = BASE / "build" / "contenu" / slug / "dialogues.js"
    if not f.is_file():
        return {}
    src = io.open(f, encoding="utf-8").read()
    out = {}
    # Chaque bloc : `nom: { ... lines: [ ["PERSO","texte"], ... ] }`
    for bloc, corps in re.findall(r"(\w+)\s*:\s*\{(.*?)\n  \}", src, re.S):
        lignes = re.findall(r'\[\s*"[^"]+"\s*,\s*"((?:[^"\\]|\\.)*)"\s*\]', corps)
        for rang, texte in enumerate(lignes, 1):
            out[(bloc, rang)] = _dejs(texte)
    return out


def textes_sons(slug):
    """{clé : texte} d'après le manifeste, quand il existe."""
    # Les manifestes nomment le module avec des tirets **bas** :
    # `module-n5-oeuvres` → `sons_module_n5_oeuvres.json`. Chercher avec le
    # slug tel quel ne trouve rien, et l'outil saute alors tout le dossier
    # `sons/` sans le dire — un module entier peut paraître traité.
    court = slug[len("module-"):] if slug.startswith("module-") else slug
    for nom in ("sons_%s.json" % slug.replace("-", "_"),
                "sons_module_%s.json" % court.replace("-", "_"),
                "sons_%s.json" % slug, "sons_module_%s.json" % court):
        f = BASE / nom
        if f.is_file():
            return json.load(io.open(f, encoding="utf-8"))
    return {}


def texte_de(chemin, dial, sons):
    """Le texte dit dans ce MP3, ou None si on ne sait pas le retrouver."""
    bloc, nom = chemin.parent.name, chemin.stem
    m = re.match(r"line_(\d+)_", nom)
    if m:
        return dial.get((bloc, int(m.group(1))))
    if bloc == "sons":
        return sons.get(nom)
    return None


# ── La mesure ─────────────────────────────────────────────────────────────

# Tous les silences, pas seulement ceux des bouts. Une réplique de quatre
# phrases contient des pauses entre les phrases ; une phrase d'exemple n'en a
# aucune. En ne retirant que la tête et la queue, la première mesurait 16 c/s
# et la seconde 28 — non parce qu'elle est dite plus vite, mais parce qu'elle
# ne respire pas. Comparer les deux sur ce chiffre-là et freiner la seconde de
# moitié aurait donné une phrase d'exemple grotesque. Ce qu'on veut cadrer est
# la vitesse d'articulation ; les pauses, elles, aident et doivent rester.
_SILENCE = ("silenceremove=start_periods=1:stop_periods=-1:"
            "start_threshold=-40dB:stop_threshold=-40dB:"
            "start_duration=0:stop_duration=0.12:detection=peak")


def duree_utile(chemin):
    """Durée de parole, silences de tête et de queue retirés. None si échec."""
    r = subprocess.run(["ffmpeg", "-i", str(chemin), "-af", _SILENCE, "-f", "null", "-"],
                       capture_output=True, text=True)
    temps = re.findall(r"time=(\d+):(\d+):([\d.]+)", r.stderr)
    if not temps:
        return None
    h, m, s = temps[-1]
    d = int(h) * 3600 + int(m) * 60 + float(s)
    return d if d > 0.15 else None


def original(chemin):
    """Le fichier d'avant tout ralentissement, à défaut celui qui est livré."""
    o = ORIGINAUX / chemin.relative_to(BASE)
    return o if o.is_file() else chemin


# ── L'application ─────────────────────────────────────────────────────────

def etirer(src, dst, facteur):
    part = dst.with_name(dst.name + ".part-%d" % os.getpid())
    try:
        if facteur >= 0.999:
            shutil.copyfile(src, part)      # déjà sous la cible : l'original
        else:
            # `atempo` n'accepte qu'entre 0,5 et 100 : en deçà, il faut
            # l'enchaîner avec lui-même. Sans ça, un extrait très rapide
            # échoue au lieu d'être ralenti.
            f = facteur
            chaine = []
            while f < 0.5:
                chaine.append("atempo=0.5")
                f /= 0.5
            chaine.append("atempo=%.4f" % f)
            subprocess.run(
                ["ffmpeg", "-y", "-loglevel", "error", "-i", str(src),
                 "-filter:a", ",".join(chaine),
                 "-ac", "1", "-ar", "24000", "-b:a", "128k",
                 "-f", "mp3", str(part)],
                check=True, capture_output=True, timeout=120)
        part.replace(dst)
        return True
    except Exception as e:
        part.unlink(missing_ok=True)
        print("   !! %s : %s" % (dst.name, e), file=sys.stderr)
        return False


def examiner(chemin, dial, sons, cible, mini):
    """(chemin, débit, facteur, raison) — facteur None quand on ne touche pas."""
    texte = texte_de(chemin, dial, sons)
    if texte is None:
        return chemin, None, None, "texte introuvable"
    if len(texte) < mini:
        return chemin, None, None, "trop court pour être mesuré"
    src = original(chemin)
    d = duree_utile(src)
    if not d:
        return chemin, None, None, "durée non mesurable"
    debit = len(texte) / d
    return chemin, debit, min(1.0, cible / debit), ""


def modules(args):
    if args.tous:
        return sorted(p.name for p in INTERACTIF.iterdir() if p.is_dir())
    if not args.slugs:
        sys.exit("!! nommer au moins un module, ou --tous")
    return args.slugs


def main():
    p = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    p.add_argument("slugs", nargs="*", help="modules à traiter")
    p.add_argument("--tous", action="store_true")
    p.add_argument("--cible", type=float, default=CIBLE_DEFAUT,
                   help="débit visé en caractères par seconde (défaut : %s)" % CIBLE_DEFAUT)
    p.add_argument("--mini-caracteres", type=int, default=MINI_CARACTERES,
                   help="en deçà, l'extrait n'est pas mesurable (défaut : %s)" % MINI_CARACTERES)
    p.add_argument("--etat", action="store_true", help="mesurer et dire, sans rien écrire")
    p.add_argument("--taches", type=int, default=os.cpu_count() or 4)
    args = p.parse_args()

    if not shutil.which("ffmpeg"):
        sys.exit("!! ffmpeg est absent")

    registre = json.load(io.open(REGISTRE, encoding="utf-8")) if REGISTRE.is_file() else {}

    for slug in modules(args):
        dossier = INTERACTIF / slug
        if not dossier.is_dir():
            print("!! %s : dossier absent" % slug)
            continue
        dial, sons = textes_dialogues(slug), textes_sons(slug)
        fichiers = sorted(dossier.rglob("*.mp3"))
        if not fichiers:
            continue

        with ThreadPoolExecutor(max_workers=args.taches) as ex:
            examens = list(ex.map(
                lambda f: examiner(f, dial, sons, args.cible, args.mini_caracteres),
                fichiers))

        mesures = [(c, d, fa) for c, d, fa, _ in examens if d]
        sautes = [r for _, d, _, r in examens if not d]
        a_faire = [(c, d, fa) for c, d, fa in mesures
                   if registre.get(str(c.relative_to(BASE)), {}).get("cible") != args.cible]

        if mesures:
            debits = sorted(d for _, d, _ in mesures)
            print("\n%s — %d extraits mesurables, %d non mesurables"
                  % (slug, len(mesures), len(sautes)))
            print("   débit avant : médiane %.1f  min %.1f  max %.1f c/s"
                  % (debits[len(debits) // 2], debits[0], debits[-1]))
            print("   au-dessus de la cible %.0f : %d extraits"
                  % (args.cible, sum(1 for d in debits if d > args.cible)))
        if args.etat or not a_faire:
            if not args.etat:
                print("   rien à refaire pour cette cible")
            continue

        with ThreadPoolExecutor(max_workers=args.taches) as ex:
            faits = list(ex.map(lambda t: etirer(original(t[0]), t[0], t[2]), a_faire))
        for (c, d, fa), ok in zip(a_faire, faits):
            if ok:
                registre[str(c.relative_to(BASE))] = {
                    "cible": args.cible, "debit": round(d, 2), "facteur": round(fa, 4)}
        print("   réécrits : %d    ratés : %d" % (sum(faits), len(faits) - sum(faits)))

    if not args.etat:
        io.open(REGISTRE, "w", encoding="utf-8").write(
            json.dumps(registre, ensure_ascii=False, indent=1, sort_keys=True))
        print("\nregistre : %s (%d extraits)" % (REGISTRE.name, len(registre)))


if __name__ == "__main__":
    main()
