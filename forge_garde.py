"""Garde de la forge — refuse les gestes qui sortiraient du dossier de commande.

La forge lance le CLI en `bypassPermissions` : sans cela, chaque `ffmpeg`,
chaque `python3` attendrait une approbation que personne n'est là pour donner.
Le prix de ce confort, c'est qu'aucune permission n'est demandée — y compris
pour réécrire un module de la bibliothèque. Or `--add-dir` ouvre la
bibliothèque EN ÉCRITURE, pas en lecture : une commande qui se trompe de
dossier peut écraser le travail de dix modules.

Ce fichier est branché comme hook `PreToolUse`. Les hooks ne passent pas par le
système de permissions : ils s'exécutent quel que soit le mode. C'est le seul
verrou qui tienne sous `bypassPermissions`.

Il reçoit l'appel d'outil en JSON sur l'entrée standard et répond par son code
de sortie : 0 laisse passer, 2 refuse (la raison, sur stderr, est renvoyée au
modèle, qui comprend et fait autrement).

Ce qu'il sait faire et ce qu'il ne sait pas faire :
  - Write / Edit / NotebookEdit : le chemin est un champ, la décision est
    exacte.
  - Bash : la commande est du texte libre. On y cherche les écritures visibles
    (redirections, mv/cp/rm, sed -i, git qui modifie…). C'est une heuristique :
    elle attrape l'erreur de dossier, pas quelqu'un qui chercherait à passer.
    La vérification d'après-coup dans forge.py est là pour le reste.

Toute décision est écrite dans `garde.log`, à côté de la commande : si le hook
ne se déclenche jamais, le fichier reste vide et cela se voit.
"""

import json
import os
import re
import sys
from datetime import datetime
from pathlib import Path

BIBLIO = Path(os.environ.get("FORGE_BIBLIO") or Path(__file__).resolve().parent)
DOSSIER = Path(os.environ.get("FORGE_DOSSIER") or ".")

# Les outils qui écrivent par un champ « chemin », et le nom de ce champ.
CHAMPS = {"Write": "file_path", "Edit": "file_path", "NotebookEdit": "notebook_path"}

# Les formes d'écriture repérables dans une ligne de commande.
REDIRECTION = re.compile(r">>?\s*['\"]?([^\s'\";|&]+)")
TEE = re.compile(r"\btee\b(?:\s+-\w+)*\s+['\"]?([^\s'\";|&]+)")
SED_EN_PLACE = re.compile(r"\b(?:sed|perl)\b[^|;&]*\s-i")
DEPLACEMENTS = ("mv", "cp", "install", "ln")
DESTRUCTIONS = ("rm", "rmdir", "truncate", "shred", "chmod", "chown")
GIT_QUI_MODIFIE = re.compile(r"\bgit\b[^|;&]*\b(add|commit|checkout|restore|reset|clean|rm|mv|push|stash)\b")


def _dans_biblio(chemin):
    """Vrai si `chemin` désigne un fichier de la bibliothèque."""
    if not chemin:
        return False
    try:
        p = Path(os.path.expanduser(str(chemin)))
        p = p if p.is_absolute() else (Path(os.environ.get("FORGE_CWD") or ".") / p)
        p = p.resolve()
    except (OSError, RuntimeError, ValueError):
        return False
    return p == BIBLIO.resolve() or BIBLIO.resolve() in p.parents


def _arguments(commande):
    """Les fragments d'une ligne de commande qui ressemblent à des chemins."""
    return [m for m in re.split(r"[\s;|&()]+", commande) if m and not m.startswith("-")]


def examiner(outil, entree):
    """(refus, raison). `refus` faux veut dire : rien vu à redire."""
    if outil in CHAMPS:
        cible = entree.get(CHAMPS[outil])
        if _dans_biblio(cible):
            return True, (f"{outil} vers la bibliothèque refusé : {cible}. La forge "
                          "écrit dans son dossier de commande, jamais dans la "
                          "bibliothèque. Lire y est permis, écrire non.")
        return False, ""

    if outil != "Bash":
        return False, ""

    commande = entree.get("command") or ""
    # Une commande qui ne nomme jamais la bibliothèque ne peut pas l'atteindre —
    # sauf par un chemin relatif, mais le travail se fait dans le dossier de
    # commande, qui est ailleurs.
    if str(BIBLIO) not in commande and "bibliotheque-francisation" not in commande:
        return False, ""

    coupables = []
    for motif in (REDIRECTION, TEE):
        coupables += [c for c in motif.findall(commande) if _dans_biblio(c)]
    if SED_EN_PLACE.search(commande) and any(_dans_biblio(a) for a in _arguments(commande)):
        coupables.append("sed -i")
    if GIT_QUI_MODIFIE.search(commande):
        coupables.append("git")
    mots = _arguments(commande)
    for i, mot in enumerate(mots):
        base = Path(mot).name
        if base in DESTRUCTIONS and any(_dans_biblio(a) for a in mots[i + 1:]):
            coupables.append(base)
        # Pour mv/cp, seule la destination compte : recopier un fichier de la
        # bibliothèque VERS le dossier de commande est le geste normal.
        if base in DEPLACEMENTS and mots[i + 1:] and _dans_biblio(mots[-1]):
            coupables.append(base)

    if coupables:
        return True, ("Écriture dans la bibliothèque refusée (" + ", ".join(sorted(set(coupables)))
                      + "). La forge travaille dans son dossier de commande. "
                        "Pour lire la bibliothèque : cat, head, sed -n — sans -i.")
    return False, ""


def _tracer(ligne):
    try:
        with open(DOSSIER / "garde.log", "a", encoding="utf-8") as f:
            f.write(f"{datetime.now():%H:%M:%S}  {ligne}\n")
    except OSError:
        pass


def main():
    # Le garde ne doit jamais faire échouer une commande par sa propre faute :
    # tout ce qu'il ne comprend pas passe, et laisse une trace.
    try:
        appel = json.loads(sys.stdin.read() or "{}")
    except ValueError:
        _tracer("entrée illisible — laissé passer")
        return 0
    outil = appel.get("tool_name") or ""
    entree = appel.get("tool_input") or {}
    try:
        refus, raison = examiner(outil, entree)
    except Exception as e:                                   # noqa: BLE001
        _tracer(f"{outil} : garde en panne ({e}) — laissé passer")
        return 0
    if refus:
        apercu = (entree.get("command") or entree.get("file_path") or "")[:120]
        _tracer(f"REFUSÉ  {outil}  {apercu}")
        print(raison, file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
