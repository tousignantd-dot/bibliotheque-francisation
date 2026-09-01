#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Refait les dialogues des niveaux 3, 6 et 7 au bon débit.

    python3 build/regen_debit.py --etalonner     # mesure les facteurs, n'écrit rien
    python3 build/regen_debit.py --plan          # dit ce qui serait refait
    python3 build/regen_debit.py --produire      # écrit pour de vrai

POURQUOI
Ces trois niveaux n'ont jamais été régénérés depuis l'échelle de débit décidée
le 29 août : ils tournent au `+15%` d'avant, soit 22 c/s au niveau 3 (cible 20)
et 25,7 au niveau 6 (cible 22). Le module 7 du niveau 3 porte le personnage le
plus rapide du corpus, à 28,9 c/s.

QUELLE VOIX
Les dialogues où un seul personnage de chaque genre parle passent en HD —
Sylvie et Thierry, les deux seules voix HD du français canadien. Les autres
restent en neurale : deux personnages du même genre s'y confondraient, et
c'est la moitié du corpus. Le niveau 7 reste entièrement en neurale : poussée
pour y atteindre 24 c/s, la voix HD sort à 27,8 avec une étendue de 17 c/s
d'une réplique à l'autre — un rythme qui change à chaque phrase.

LE FACTEUR NE SE DÉDUIT PAS, IL SE MESURE
On pourrait croire le débit proportionnel au taux et calculer une fois pour
toutes. C'est faux à deux titres : les voix n'articulent pas à la même densité,
et un c/s ne se compare qu'à texte comparable — les phrases de niveau 7 sont
plus denses que celles de niveau 3. Chaque couple (voix, niveau) est donc
étalonné sur de vraies répliques de ce niveau, synthétisées à un taux témoin.

CE QUI EST PROTÉGÉ
Rien de ce qui vient d'ElevenLabs n'est touché (`fournisseur.est_elevenlabs`),
rien hors des niveaux 3, 6 et 7, et rien de la famille « sons » — les mots
isolés ont leur propre étalonnage, et personne ne s'en est plaint.
"""
import argparse, collections, json, random, statistics as st, sys
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE / "build"))
import fournisseur as F
from azure_voix import parle

CIBLE = {3: 20, 6: 22, 7: 24}
NIVEAUX = set(CIBLE)
HD_NIVEAUX = {3, 6}          # le 7 reste en neurale : voir la docstring
GENRE = {"enseignante": "F", "feminin_2": "F",
         "masculin_1": "M", "narrateur": "M", "masculin_3": "M"}
HD_ROLE = {"F": "hd_feminin", "M": "hd_masculin"}
TEMOIN = "-10%"              # taux d'étalonnage, arbitraire mais unique
DEBITS = BASE / "build" / ".debits.json"
FACTEURS = BASE / "build" / ".facteurs_debit.json"


def duree_parlee(mp3):
    """Secondes de parole, silences retirés — ffmpeg le dit, on le lui demande."""
    import re, subprocess
    p = subprocess.run(["ffmpeg", "-i", str(mp3), "-af",
                        "silencedetect=noise=-35dB:d=0.15", "-f", "null", "-"],
                       capture_output=True, text=True)
    e = p.stderr
    m = re.search(r"Duration:\s*(\d+):(\d+):([\d.]+)", e)
    if not m: return None
    total = int(m.group(1))*3600 + int(m.group(2))*60 + float(m.group(3))
    deb = [float(x) for x in re.findall(r"silence_start:\s*(-?[\d.]+)", e)]
    fin = [float(x) for x in re.findall(r"silence_end:\s*([\d.]+)", e)]
    sil = sum(max(0.0, min(fin[i] if i < len(fin) else total, total) - max(0.0, d))
              for i, d in enumerate(deb))
    return max(0.01, total - sil)


def repliques():
    """Les répliques des trois niveaux, telles que le relevé de débit les connaît."""
    d = json.loads(DEBITS.read_text(encoding="utf-8"))
    return [r for r in d if r.get("niveau") in NIVEAUX and r.get("texte") and r.get("f")]


def dialogues(reps):
    """{module/section: {persos, répliques}} — le dialogue est l'unité de décision.

    C'est le dialogue, et non la réplique, qui choisit sa voix : deux
    personnages du même genre ne peuvent pas partager la seule voix HD de leur
    genre, et la question ne se pose qu'à l'échelle de la scène.
    """
    out = collections.defaultdict(lambda: {"persos": {}, "reps": [], "niv": None})
    for r in reps:
        cle = r["f"].rsplit("/", 1)[0]
        e = out[cle]
        e["persos"][r["perso"]] = r["role"]
        e["reps"].append(r)
        e["niv"] = r["niveau"]
    return out


def en_hd(e):
    g = collections.Counter(GENRE.get(v, "?") for v in e["persos"].values())
    return e["niv"] in HD_NIVEAUX and g["F"] <= 1 and g["M"] <= 1


def etalonner(reps, combos, n=8, graine=7):
    """{(role, niveau): taux} — mesuré sur les textes du corpus, pas sur d'autres.

    PREMIÈRE VERSION, FAUSSE. Elle synthétisait six répliques au hasard à un
    taux témoin, mesurait le débit obtenu, et en déduisait le taux visant la
    cible. Le résultat prescrivait d'ACCÉLÉRER le narrateur de 30 % alors qu'il
    est déjà à sa cible. La raison : un c/s dépend du texte autant que de la
    voix, et l'échantillon n'avait pas la densité du niveau. Viser « 20 c/s »
    sur six phrases choisies ne vise pas 20 c/s sur le corpus.

    LA BONNE MÉTHODE tient en deux temps, et la densité s'y annule :
      1. Sur les MÊMES répliques, comparer le débit déjà en ligne (relevé dans
         .debits.json) au débit obtenu au taux témoin. Leur rapport donne le
         taux auquel le corpus a été fabriqué — sans jamais lire un c/s absolu.
      2. Partir du débit MÉDIAN de cette voix à ce niveau dans le corpus entier,
         qui est ce dont on se plaint, et calculer le taux qui l'amène à la
         cible.
    """
    tmp = BASE / "build" / ".etalonnage"
    tmp.mkdir(exist_ok=True)
    rng = random.Random(graine)
    par_combo = collections.defaultdict(list)
    for r in reps:
        if r.get("cps"):
            par_combo[(r["role"], r["niveau"])].append(r)

    facteurs = {}
    for role, niveau in sorted(combos):
        # Le rôle employé peut être HD alors que le corpus porte l'ancien : on
        # étalonne la voix NEUVE sur les textes du dialogue, et on vise la
        # médiane du corpus pour ce niveau, toutes voix confondues s'il le faut.
        source = par_combo.get((role, niveau)) or [
            r for r in reps if r["niveau"] == niveau and r.get("cps")]
        if not source:
            print("  %-14s niveau %d : aucune référence" % (role, niveau)); continue
        ech = rng.sample(source, min(n, len(source)))
        rapports = []
        for i, r in enumerate(ech):
            f = tmp / ("%s-%d-%d.mp3" % (role, niveau, i))
            parle(r["texte"], role, f, reference=TEMOIN)
            d = duree_parlee(f)
            if d:
                rapports.append(r["cps"] / (len(r["texte"]) / d))
        if not rapports:
            print("  %-14s niveau %d : ÉCHEC de l'étalonnage" % (role, niveau)); continue
        # (1 + taux du corpus) = (1 + témoin) × débit_corpus / débit_témoin
        rapport = st.median(rapports)
        taux_corpus = 0.90 * rapport - 1
        mediane = st.median([r["cps"] for r in source])
        r_pct = ((1 + taux_corpus) * CIBLE[niveau] / mediane - 1) * 100
        r_pct = max(-40, min(40, r_pct))
        facteurs["%s|%d" % (role, niveau)] = round(r_pct)
        print("  %-14s niveau %d : corpus %5.1f c/s (fabriqué à %+d%%) "
              "⇒ taux %+d%% pour viser %d"
              % (role, niveau, mediane, round(taux_corpus*100), round(r_pct), CIBLE[niveau]))
    return facteurs


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--etalonner", action="store_true")
    ap.add_argument("--plan", action="store_true")
    ap.add_argument("--produire", action="store_true")
    a = ap.parse_args()

    reps = repliques()
    dlg = dialogues(reps)
    travail = []          # (replique, role_a_employer, niveau)
    protege = ignore = 0
    for cle, e in dlg.items():
        hd = en_hd(e)
        for r in e["reps"]:
            f = BASE / "assets" / "interactive" / r["f"]
            if not f.exists(): ignore += 1; continue
            if F.est_elevenlabs(f): protege += 1; continue
            role = HD_ROLE[GENRE.get(r["role"], "M")] if hd else r["role"]
            travail.append((r, role, r["niveau"]))

    combos = {(role, niv) for _, role, niv in travail}
    print("%d dialogues · %d répliques à refaire · %d protégées (ElevenLabs) · %d introuvables"
          % (len(dlg), len(travail), protege, ignore))
    par = collections.Counter((role, niv) for _, role, niv in travail)
    print()
    for (role, niv), n in sorted(par.items()):
        print("  %-14s niveau %d : %4d répliques" % (role, niv, n))

    if a.plan:
        return 0

    if a.etalonner or a.produire:
        if FACTEURS.exists() and not a.etalonner:
            facteurs = json.loads(FACTEURS.read_text(encoding="utf-8"))
            print("\nfacteurs relus dans %s" % FACTEURS.name)
        else:
            print("\n── étalonnage ──")
            facteurs = etalonner(reps, combos)
            FACTEURS.write_text(json.dumps(facteurs, ensure_ascii=False, indent=1),
                                encoding="utf-8")
        if not a.produire:
            return 0

    print("\n── production ──", flush=True)
    faits = rates = 0
    for i, (r, role, niv) in enumerate(travail, 1):
        taux = facteurs.get("%s|%d" % (role, niv))
        if taux is None:
            rates += 1; continue
        f = BASE / "assets" / "interactive" / r["f"]
        try:
            parle(r["texte"], role, f, reference="%+d%%" % taux)
            faits += 1
        except Exception as e:                                  # noqa: BLE001
            rates += 1
            print("  échec %s : %s" % (r["f"], e), flush=True)
        if i % 100 == 0:
            print("  %d / %d" % (i, len(travail)), flush=True)
    print("terminé : %d refaites, %d échecs" % (faits, rates))
    return 0


if __name__ == "__main__":
    sys.exit(main())
