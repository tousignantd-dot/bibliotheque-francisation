#!/usr/bin/env python3
"""Copie les données du volume vers Postgres, une fois pour toutes.

    DATABASE_URL=… python3 build/migrer_postgres.py --etat     # ce qu'il y a
    DATABASE_URL=… python3 build/migrer_postgres.py --essai    # sans écrire
    DATABASE_URL=… python3 build/migrer_postgres.py            # migre

**Elle refuse d'écraser une base déjà peuplée** sans `--forcer` : rejouer une
migration sur une base en service remettrait les fichiers du volume — donc
l'état d'avant — par-dessus le travail fait depuis. C'est le seul geste
vraiment irréversible du chantier.

Elle **ne supprime aucun fichier**. Le volume reste tel quel : c'est le filet,
et il ne coûte rien à garder. Retirer `DATABASE_URL` fait revenir le serveur
aux fichiers, à l'octet près.
"""
import json
import os
import pathlib
import sys

RACINE = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RACINE))

import db  # noqa: E402


def dossier_donnees():
    return pathlib.Path(os.environ.get("STORAGE_DIR", str(RACINE))) / "data"


def lire(fichier):
    chemin = dossier_donnees() / fichier
    if not chemin.exists():
        return None
    try:
        with open(chemin, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError as e:
        print(f"  ! {fichier} illisible ({e}) — sauté")
        return None


def etat_base():
    try:
        return db.compter()
    except Exception as e:
        print(f"Base injoignable : {e}")
        return None


def main():
    if not db.disponible():
        print("DATABASE_URL absente ou pilote manquant — rien à faire.")
        print("Sans elle, le serveur écrit dans les fichiers, comme avant.")
        return 1

    essai = "--essai" in sys.argv
    forcer = "--forcer" in sys.argv
    db.init_schema()

    avant = etat_base()
    if avant is None:
        return 1
    if "--etat" in sys.argv:
        print("Dans la base :")
        print(f"  documents : {avant['documents']}")
        for t in ("progression", "journal_acces", "signaux_aide", "vocab_progression"):
            print(f"  {t:20} {avant[t]} lignes")
        return 0

    peuplee = bool(avant["documents"]) or any(
        avant[t] for t in ("progression", "journal_acces", "signaux_aide",
                           "vocab_progression"))
    if peuplee and not forcer and not essai:
        print("La base contient déjà des données. Migrer par-dessus remettrait")
        print("l'état des fichiers du volume et effacerait ce qui a été fait")
        print("depuis. Relancez avec --forcer si c'est bien ce que vous voulez,")
        print("ou avec --etat pour voir ce qu'elle contient.")
        return 1

    print(f"Source : {dossier_donnees()}")
    print("Essai — rien ne sera écrit." if essai else "Migration.")
    total = 0
    for fichier in sorted(db.DOCUMENTS):
        donnees = lire(fichier)
        if donnees is None:
            continue
        n = len(donnees) if isinstance(donnees, list) else 1
        print(f"  document  {fichier:26} {n}")
        if not essai:
            db.ecrire_document(fichier, donnees)
        total += n
    for fichier in sorted(db.JOURNAUX):
        donnees = lire(fichier)
        if donnees is None:
            continue
        print(f"  journal   {fichier:26} {len(donnees)}")
        if not essai:
            db.remplacer_journal(fichier, donnees)
        total += len(donnees)

    if essai:
        print(f"\n{total} enregistrements seraient copiés. Rien n'a été écrit.")
        return 0

    apres = etat_base()
    print("\nAprès migration :")
    print(f"  documents : {apres['documents']}")
    for t in ("progression", "journal_acces", "signaux_aide", "vocab_progression"):
        print(f"  {t:20} {apres[t]} lignes")
    print("\nLes fichiers du volume n'ont pas été touchés : retirer DATABASE_URL")
    print("ramène le serveur à eux, exactement comme avant.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
