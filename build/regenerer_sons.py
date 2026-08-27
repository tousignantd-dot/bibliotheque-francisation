#!/usr/bin/env python3
"""Régénérer la famille « enseignante » de tous les modules, chez Azure.

    python3 build/regenerer_sons.py --plan     # ce qui serait lancé, sans rien faire
    python3 build/regenerer_sons.py            # lance, et reprend où il en était
    python3 build/regenerer_sons.py --seul generer_audio_module_meteo_sons.py

Ce qu'on régénère, et ce qu'on laisse
-------------------------------------
Décidé le 27 août 2026, après écoute : **les mots, phrases et mini-leçons
passent à Azure ; les dialogues restent en ElevenLabs.**

Le motif n'est pas la qualité — les extraits d'ElevenLabs sont bons. C'est
l'identité des voix. 70 personnages du cours apparaissent dans plus d'un module
(Marisol dans neuf, Nadia dans huit), si bien que régénérer des dialogues au
hasard ferait changer une comédienne de voix en cours de parcours. La voix
enseignante, elle, est dans presque tous les modules et ne parle jamais *dans*
un dialogue : on peut la basculer seule sans créer de couture au milieu d'une
conversation. Cette couture-là a été montée et écoutée avant de décider.

Le gain est réel et concentré : l'épellation sort en français d'office, le
débit est exact, et c'est la famille la plus volumineuse du cours.

La voix enseignante *comme personnage* n'est pas touchée
--------------------------------------------------------
Madame Roy et Lin, au module n1-presenter, parlent avec la voix enseignante
mais dans un dialogue. Les régénérer les mettrait en Azure face à une Amina
restée en ElevenLabs — la couture rude qu'on veut éviter. Elles sont donc
laissées, comme toutes les répliques.

Comment chaque générateur est traité
------------------------------------
Les 110 générateurs n'ont pas la même forme, et le nom du fichier ne suffit pas
à savoir ce qu'il produit. On lit donc le code :

* il écrit des `line_*.mp3` **et** des sons, et accepte `--only` → lancé avec
  `--only sons` ;
* il n'écrit que des sons → lancé tel quel ;
* il n'écrit que des répliques → **écarté** ;
* ses sons sortent dans une voix autre que l'enseignante → **écarté**, et dit.

Deux modules tombent dans ce dernier cas : `sante_plus` et `travail_plus`
confient leurs sons au narrateur et à une voix rare. Les basculer aurait changé
la voix, pas seulement le fournisseur.

Quatre de front, et pourquoi
----------------------------
En séquence, les ~14 000 extraits demandent près de huit heures. Chaque module
écrit dans son propre dossier, donc rien ne se marche dessus. Quatre processus
ramènent l'attente sous les deux heures sans approcher les limites d'Azure.

La reprise se fait par module et non par extrait : `.regenerer_sons.json` note
ceux qui ont fini sans échec. Un module interrompu au milieu sera simplement
relancé en entier — les générateurs sont idempotents, et c'est plus sûr que de
tenir un registre extrait par extrait qui pourrait mentir.
"""
import argparse
import concurrent.futures
import json
import pathlib
import re
import subprocess
import sys
import time

RACINE = pathlib.Path(__file__).resolve().parent.parent
REGISTRE = RACINE / ".regenerer_sons.json"
ENSEIGNANTE = "mActWQg9kibLro6Z2ouY"
FRONTS = 4


def classer(f):
    """(action, argument, raison) pour un générateur.

    La règle se lit à l'envers de ce qu'on croit : on ne cherche pas à
    reconnaître la famille enseignante, on cherche **l'absence de dialogue**.
    Chercher le mot « sons » écartait à tort `banque_n1` et `polices_n1`, qui
    sont des bancs de mots en voix enseignante mais écrivent dans
    `audio/<slug>.mp3`. Un fichier qui ne produit aucun `line_*.mp3` ne peut
    pas créer de couture au milieu d'une conversation : on peut le lancer
    entier.
    """
    t = f.read_text(encoding="utf-8")
    # `"--force" in argv` chez les uns, `in sys.argv` chez les autres : chercher
    # la chaîne exacte avait manqué `banque_n1`, qui accepte pourtant l'option.
    # Il a sauté ses 264 extraits en rapportant « 0 · succès ».
    accepte_force = bool(re.search(r'"--force" in (sys\.)?argv', t))
    voix = re.search(r'^VOICE\s*=\s*"([^"]+)"', t, re.M)
    if voix and ENSEIGNANTE not in voix.group(1):
        return "écarté", None, "sons dans une autre voix (%s)" % voix.group(1)[:12]
    if "line_" not in t:
        # `--force` est indispensable ici, et son absence est **silencieuse** :
        # ces générateurs sautent les fichiers déjà présents, or les MP3
        # d'ElevenLabs sont précisément déjà présents. Sans lui, dix modules
        # ont rapporté « 0 extrait · succès » en gardant leur ancien audio.
        arg = ["--force"] if accepte_force else []
        return "lancer", arg, "aucune réplique, tout est en voix enseignante"
    if "--only" in t:
        # `--force` aussi pour les mixtes, et ce n'est pas une redondance :
        # dans 40 générateurs le test s'écrit `exists() and not force` sans
        # `and not only`, si bien que `--only sons` **saute** les MP3 déjà en
        # place — c'est-à-dire ceux d'ElevenLabs. Trois modules (n3-horaire,
        # n3-electro, n3-loisirs) ont ainsi rapporté « 0 extrait · succès » en
        # gardant leur ancien audio. Le commentaire de ces générateurs le dit :
        # « `--only` ne veut pas dire refais-les ». Le filtre `--only`
        # s'applique avant le test, donc `--force` ne déborde pas sur les
        # répliques de dialogue.
        arg = ["--only", "sons"] + (["--force"] if accepte_force else [])
        return "lancer", arg, "mixte, restreint aux sons"
    return "écarté", None, "mixte sans --only, on ne sait pas isoler les sons"


def plan():
    out = []
    for f in sorted(RACINE.glob("generer_audio*.py")):
        action, arg, raison = classer(f)
        out.append((f, action, arg, raison))
    return out


def lancer(f, arg):
    t0 = time.time()
    r = subprocess.run([sys.executable, str(f)] + arg, cwd=RACINE,
                       capture_output=True, text=True)
    txt = r.stdout + r.stderr
    m = re.search(r"(\d+) générés .* (\d+) en échec", txt)
    faits = int(m.group(1)) if m else txt.count("→ ✓")
    rates = int(m.group(2)) if m else txt.count("❌")
    return {"module": f.name, "code": r.returncode, "faits": faits,
            "rates": rates, "secondes": round(time.time() - t0, 1),
            "queue": txt.strip()[-400:] if r.returncode else ""}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--plan", action="store_true")
    ap.add_argument("--seul")
    ap.add_argument("--fronts", type=int, default=FRONTS)
    a = ap.parse_args()

    travaux = plan()
    if a.seul:
        travaux = [x for x in travaux if x[0].name == a.seul]

    if a.plan:
        for action in ("lancer", "écarté"):
            gr = [x for x in travaux if x[1] == action]
            print("\n%s : %d" % (action.upper(), len(gr)))
            for f, _, arg, raison in gr:
                print("   %-46s %-14s %s"
                      % (f.name, " ".join(arg or []), raison))
        return 0

    fait = json.loads(REGISTRE.read_text()) if REGISTRE.exists() else {}
    aFaire = [(f, arg) for f, act, arg, _ in travaux
              if act == "lancer" and f.name not in
              {k for k, v in fait.items() if v.get("rates") == 0}]
    print("%d module(s) à régénérer, %d déjà faits, %d de front"
          % (len(aFaire), len(fait), a.fronts))

    total_faits = total_rates = 0
    with concurrent.futures.ThreadPoolExecutor(a.fronts) as ex:
        futs = {ex.submit(lancer, f, arg): f for f, arg in aFaire}
        for i, fut in enumerate(concurrent.futures.as_completed(futs), 1):
            r = fut.result()
            fait[r["module"]] = r
            REGISTRE.write_text(json.dumps(fait, indent=1, ensure_ascii=False))
            total_faits += r["faits"]; total_rates += r["rates"]
            etat = "✓" if r["code"] == 0 and not r["rates"] else "✗"
            print("  [%3d/%3d] %s %-44s %4d extraits  %5.0f s%s"
                  % (i, len(aFaire), etat, r["module"], r["faits"], r["secondes"],
                     "  ÉCHECS:%d" % r["rates"] if r["rates"] else ""))
            if r["queue"]:
                print("        %s" % r["queue"].replace("\n", "\n        ")[:300])

    print("\n%d extraits produits, %d en échec" % (total_faits, total_rates))
    print("Registre : %s — relancer le script reprend les modules en échec."
          % REGISTRE.name)
    return 1 if total_rates else 0


if __name__ == "__main__":
    sys.exit(main())
