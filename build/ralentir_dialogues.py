#!/usr/bin/env python3
"""Repasse les MP3 **déjà produits** au facteur que `voix_lente` leur donne.

Pourquoi ce script existe
-------------------------
`voix_lente` s'applique au moment où un extrait est synthétisé. Quand la règle
change — une voix s'ajoute, un facteur bouge — les milliers de fichiers déjà
sur le disque gardent l'ancien débit, et les régénérer coûterait le prix de
tout l'audio du cours. Ce script les retraite sur place, sans un seul appel à
l'API.

Le 18 août 2026, la même opération avait été faite à la main pour la voix
enseignante, et le script n'avait pas été gardé : il a fallu le réécrire de
zéro le 25 août pour la voix féminine #2. D'où ce fichier.

    python3 build/ralentir_dialogues.py --essai       # inventaire, sans rien écrire
    python3 build/ralentir_dialogues.py               # applique aux nouveaux
    python3 build/ralentir_dialogues.py --recalibrer  # repart des originaux

`--recalibrer` sert quand la **règle** change et non le corpus : il remet
chaque extrait à son original avant d'appliquer le facteur courant, au lieu de
ralentir un fichier déjà ralenti. Sans lui, changer 0,85 en 0,88 donnerait
0,75. Il ne peut agir que sur les extraits dont l'original est dans
`.audio-originaux/` — c'est le cas de toutes les voix de dialogue, mais pas de
l'enseignante, ralentie à la synthèse dans la plupart des modules.

Deux pièges, tous deux payés comptant
-------------------------------------
1. **Ralentir deux fois est invisible.** Deux passes à 0,90 donnent 0,81, et
   rien dans le MP3 ne dit que c'est arrivé. Il faut donc un registre — et la
   présence d'une sauvegarde dans `.audio-originaux/` n'en est pas un :
   `voix_lente.ralentir()` **ne sauvegarde rien** quand il agit au moment de
   la synthèse, si bien qu'un extrait ralenti à la génération n'a aucune
   sauvegarde. S'y fier proposerait de repasser 434 répliques de l'enseignante
   déjà à 0,85, pour les descendre à 0,72. Le registre est donc un fichier à
   part, `.audio-ralentis.json`, tenu explicitement.

2. **Les noms de fichiers suivent deux règles, pas une.** Les modules bâtis
   par le gabarit passent par `charSlug()`, qui retire les accents et les
   apostrophes : « MADAME CÔTÉ » → `madame_cote`. Les modules plus anciens
   (`je-demenage`, `parler-de-sa-sante`, `visite-vieux-montreal`,
   `module-travail`…) font un simple `.lower().replace(' ', '_')` et gardent
   les accents : « M. BÉLANGER » → `m._bélanger`. N'essayer que la règle
   moderne fait manquer ces personnages-là — et comme deux de ces générateurs
   ont un `VOICE_ASSOC.get(perso, "feminin_2")`, le personnage manqué tombe
   sur la voix par défaut et se fait ralentir alors qu'il ne devait pas
   l'être. C'est exactement ce qui est arrivé à M. Bélanger. On essaie donc
   les deux règles, et **on refuse de traiter un personnage qu'aucune des deux
   ne résout** plutôt que de se rabattre sur le défaut du générateur.

Comment le script sait quelle voix parle
----------------------------------------
Il lit chaque `generer_audio_*.py` et y trouve deux dictionnaires, quel que
soit leur nom (`VOIX`/`VOIX_PERSO` dans les modules récents,
`VOICES`/`VOICE_ASSOC` dans les anciens) : celui dont toutes les valeurs sont
des identifiants ElevenLabs, et celui dont toutes les valeurs sont des clés du
premier. Le module de sortie se déduit du slug du dossier.
"""
import ast
import json
import re
import shutil
import sys
import unicodedata
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RACINE))
from voix_lente import ralentir, facteur_pour   # noqa: E402

ID_VOIX = re.compile(r"^[A-Za-z0-9]{20}$")
ORIGINAUX = RACINE / ".audio-originaux"

# Le registre : la liste des extraits dont le débit est déjà celui de la règle,
# qu'ils l'aient été à la synthèse ou par une passe de ce script. Il est semé
# une première fois par `--sceller`, et tenu à jour à chaque passe.
REGISTRE = RACINE / ".audio-ralentis.json"

# Les trois modules dont le générateur ne porte pas le nom du slug.
GENERATEUR = {
    "je-demenage":           "generer_audio_dialogues.py",
    "parler-de-sa-sante":    "generer_audio_dialogues.py",
    "visite-vieux-montreal": "generer_audio_vieux_montreal.py",
}


def slug_gabarit(nom):
    """`charSlug()` du gabarit : sans accents ni apostrophes."""
    s = unicodedata.normalize("NFD", nom.lower())
    s = "".join(c for c in s if unicodedata.category(c) != "Mn")
    return s.replace("'", "").replace(" ", "_")


def slug_ancien(nom):
    """La règle des générateurs d'avant le gabarit : les accents restent."""
    return nom.lower().replace(" ", "_")


def _dicts(chemin):
    """Les dictionnaires littéraux définis au niveau module."""
    out = {}
    for n in ast.parse(chemin.read_text(encoding="utf-8")).body:
        if isinstance(n, ast.Assign) and isinstance(n.value, ast.Dict):
            for cible in n.targets:
                if isinstance(cible, ast.Name):
                    try:
                        out[cible.id] = ast.literal_eval(n.value)
                    except Exception:
                        pass
    return out


def voix_par_slug(generateur):
    """slug de fichier → identifiant de voix, ou None si le générateur est illisible."""
    ds = _dicts(generateur)
    table = next((d for d in ds.values()
                  if d and all(isinstance(v, str) and ID_VOIX.match(v)
                               for v in d.values())), None)
    if not table:
        return None
    assoc = next((d for d in ds.values()
                  if d is not table and d
                  and all(isinstance(v, str) and v in table for v in d.values())), {})
    par = {}
    for perso, cle in assoc.items():
        par.setdefault(slug_gabarit(perso), table[cle])
        par.setdefault(slug_ancien(perso), table[cle])
    return par


def inventaire():
    """(fichiers à traiter, personnages non résolus)."""
    cibles, orphelins = [], []
    for d in sorted((RACINE / "assets/interactive").iterdir()):
        lignes = sorted(d.glob("*/line_*.mp3")) if d.is_dir() else []
        if not lignes:
            continue
        gen = RACINE / GENERATEUR.get(d.name,
                                      "generer_audio_%s.py" % d.name.replace("-", "_"))
        if not gen.exists():
            orphelins.append((d.name, "générateur introuvable")); continue
        par = voix_par_slug(gen)
        if par is None:
            orphelins.append((d.name, "table de voix illisible")); continue
        for f in lignes:
            s = re.match(r"line_\d+_(.+)\.mp3$", f.name).group(1)
            vid = par.get(s)
            if vid is None:
                orphelins.append((d.name, "personnage « %s » non associé" % s)); continue
            rel = str(f.relative_to(RACINE))
            if facteur_pour(vid, rel) is not None:
                cibles.append((rel, facteur_pour(vid, rel)))
    return cibles, orphelins


def lire_registre():
    if not REGISTRE.exists():
        sys.exit("❌ %s absent. Semer le registre avec --sceller après avoir "
                 "vérifié que l'audio en place est au bon débit." % REGISTRE.name)
    return set(json.loads(REGISTRE.read_text(encoding="utf-8")))


def ecrire_registre(faits):
    REGISTRE.write_text(json.dumps(sorted(faits), indent=1, ensure_ascii=False),
                        encoding="utf-8")


def recalibrer():
    """Repart de l'original et applique le facteur courant. Le seul moyen sûr
    de changer un facteur : ralentir par-dessus du ralenti se compose."""
    cibles, orphelins = inventaire()
    if orphelins:
        for m, r in orphelins[:40]:
            print("   %-26s %s" % (m, r))
        sys.exit("❌ des personnages ne sont pas résolus. Rien n'a été écrit.")
    faits = sautes = 0
    deja = lire_registre() if REGISTRE.exists() else set()

    # Un extrait qui SORT de la règle — le narrateur au-dessus du niveau 2
    # depuis la calibration par voix — resterait ralenti par la passe
    # précédente si on se contentait d'ignorer ce qui n'est plus une cible.
    # On lui rend son original.
    plus_cible = {r for r in deja if r not in {c for c, _ in cibles}}
    for rel in sorted(plus_cible):
        sauve = ORIGINAUX / rel
        if sauve.exists():
            shutil.copy2(sauve, RACINE / rel)
        deja.discard(rel)
    if plus_cible:
        print("rendus au débit d'origine (plus visés par la règle) : %d"
              % len(plus_cible))
    for i, (rel, f) in enumerate(cibles, 1):
        src, sauve = RACINE / rel, ORIGINAUX / rel
        if not sauve.exists():
            sautes += 1                       # pas d'original : on n'y touche pas
            continue
        shutil.copy2(sauve, src)              # retour au brut
        if ralentir(src, f):
            faits += 1; deja.add(rel)
        else:
            print("   ✗ %s" % rel)
        if i % 300 == 0:
            print("   … %d/%d" % (i, len(cibles)), flush=True)
    ecrire_registre(deja)
    print("\nrecalibrés : %d   sans original, laissés tels quels : %d" % (faits, sautes))
    print("N'oublie pas d'incrémenter AUDIO_V dans les modules touchés.")


def main():
    essai = "--essai" in sys.argv
    if "--recalibrer" in sys.argv:
        recalibrer(); return
    if "--sceller" in sys.argv:
        # À n'employer qu'après avoir vérifié à l'oreille ou au débit que
        # l'audio en place est déjà celui de la règle.
        cibles, _ = inventaire()
        ecrire_registre({r for r, _ in cibles})
        print("registre semé : %d extraits déclarés déjà au bon débit" % len(cibles))
        return
    deja = lire_registre()
    cibles, orphelins = inventaire()
    restants = [(r, f) for r, f in cibles if r not in deja]
    par_facteur = {}
    for _, f in restants:
        par_facteur[f] = par_facteur.get(f, 0) + 1
    print("%d extraits relèvent d'un facteur ; %d déjà traités, %d à faire"
          % (len(cibles), len(cibles) - len(restants), len(restants)))
    for f, n in sorted(par_facteur.items()):
        print("   facteur %.2f : %4d" % (f, n))
    if orphelins:
        print("\n⚠️  non résolus — À CORRIGER avant d'appliquer :")
        for m, r in orphelins[:40]:
            print("   %-26s %s" % (m, r))
        if not essai:
            sys.exit("\n❌ un personnage non résolu est un fichier qu'on "
                     "ralentirait au hasard. Rien n'a été écrit.")
    if essai or not restants:
        return
    faits = 0
    for i, (rel, f) in enumerate(restants, 1):
        src, sauve = RACINE / rel, ORIGINAUX / rel
        sauve.parent.mkdir(parents=True, exist_ok=True)
        if not sauve.exists():          # ne jamais écraser un original par un
            shutil.copy2(src, sauve)    # fichier déjà traité par une autre passe
        if ralentir(src, f):
            faits += 1
            deja.add(rel)
            ecrire_registre(deja)     # écrit à chaque extrait : une
                                      # interruption ne perd pas le registre
        else:
            shutil.copy2(sauve, src); sauve.unlink()
            print("   ✗ %s" % rel)
        if i % 200 == 0:
            print("   … %d/%d" % (i, len(restants)), flush=True)
    print("\nralentis : %d / %d" % (faits, len(restants)))
    print("N'oublie pas d'incrémenter AUDIO_V dans les modules touchés : les "
          "MP3 sont servis sans Cache-Control.")


if __name__ == "__main__":
    main()
