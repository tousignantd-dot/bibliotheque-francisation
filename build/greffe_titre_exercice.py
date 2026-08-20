#!/usr/bin/env python3
"""Les signaux d'aide nomment l'exercice par son titre, plus par son code.

Les modules envoient deux journaux à l'enseignante, et ils ne nommaient pas
l'exercice de la même façon : l'analyse d'erreurs y met son titre (`ex.tit`),
les cinq signaux d'aide y mettaient l'identifiant court (`t1pc`, `l1`). La
colonne « Exercice » de la progression et de la fiche de l'élève affichait
donc des codes, illisibles pour qui n'a pas le module sous les yeux.

    python3 build/greffe_titre_exercice.py
    python3 build/greffe_titre_exercice.py --retirer

La greffe est idempotente : elle se repose sans dommage, et un module déjà
greffé est laissé tel quel. module-probleme est généré à partir de
module-consultation : la greffe posée sur le gabarit le suit à la
reconstruction, mais on la pose aussi sur le fichier produit pour ne pas
attendre le prochain build.
"""

import argparse
import glob
import io
import sys

ANCRE = "function evaluerAide(exId, nbErreurs){"

AIDE = """/* Les deux journaux de l'enseignante nomment le même exercice : l'analyse
   d'erreurs y met son titre, les signaux d'aide y mettaient l'identifiant
   court. Deux noms pour une seule chose, et une colonne « Exercice » qu'on ne
   peut pas lire sans le module ouvert à côté. Le titre part des deux côtés.
   Repli sur l'identifiant : un exercice sans titre vaut mieux qu'un vide. */
function titreExo(exId){
  const ex = (typeof EXOS !== 'undefined') && EXOS.find(e => e.id === exId);
  if(ex && ex.tit) return ex.tit;
  if(typeof PLUS !== 'undefined' && PLUS[exId] && PLUS[exId].tit) return PLUS[exId].tit;
  return exId;
}

"""

# (avant, après) — les cinq points d'envoi, identiques dans les onze modules.
ENVOIS = [
    ("lmsTrack('aide_proposee', {exercice: exId, erreurs: n, analysable: analysable});",
     "lmsTrack('aide_proposee', {exercice: titreExo(exId), erreurs: n, analysable: analysable});"),
    ("lmsTrack('aide_acceptee', {exercice: exId, erreurs: AIDE.err[exId]});",
     "lmsTrack('aide_acceptee', {exercice: titreExo(exId), erreurs: AIDE.err[exId]});"),
    ("lmsTrack('aide_analysee', {exercice: exId, erreurs: AIDE.err[exId]});",
     "lmsTrack('aide_analysee', {exercice: titreExo(exId), erreurs: AIDE.err[exId]});"),
    ("lmsTrack('aide_refusee', {exercice: exId, erreurs: AIDE.err[exId]});",
     "lmsTrack('aide_refusee', {exercice: titreExo(exId), erreurs: AIDE.err[exId]});"),
    ("lmsTrack('plus_open', {savoir: exId, cible: cible || ''});",
     "lmsTrack('plus_open', {savoir: titreExo(exId), cible: cible || ''});"),
]

MODULES = "assets/interactive/module-*/module-*-activite-interactive.html"


def poser(chemin):
    s = io.open(chemin, encoding="utf-8").read()
    nom = chemin.split("/")[2]
    if "function titreExo(exId){" in s:
        return nom, False
    if s.count(ANCRE) != 1:
        sys.exit(f"!! {nom} : evaluerAide introuvable ou en double ({s.count(ANCRE)})")
    for avant, apres in ENVOIS:
        if s.count(avant) != 1:
            sys.exit(f"!! {nom} : {avant[:34]}… introuvable ou en double ({s.count(avant)})")
        s = s.replace(avant, apres, 1)
    s = s.replace(ANCRE, AIDE + ANCRE, 1)
    io.open(chemin, "w", encoding="utf-8").write(s)
    return nom, True


def retirer(chemin):
    s = io.open(chemin, encoding="utf-8").read()
    nom = chemin.split("/")[2]
    if "function titreExo(exId){" not in s:
        return nom, False
    for avant, apres in ENVOIS:
        s = s.replace(apres, avant, 1)
    s = s.replace(AIDE + ANCRE, ANCRE, 1)
    io.open(chemin, "w", encoding="utf-8").write(s)
    return nom, True


def main():
    parseur = argparse.ArgumentParser(description=__doc__)
    parseur.add_argument("--retirer", action="store_true",
                         help="remettre les modules dans leur état d'avant la greffe")
    args = parseur.parse_args()

    action = retirer if args.retirer else poser
    fichiers = sorted(glob.glob(MODULES))
    if not fichiers:
        sys.exit("!! aucun module trouvé — lancer depuis la racine du projet")

    faits, laisses = [], []
    for chemin in fichiers:
        nom, change = action(chemin)
        (faits if change else laisses).append(nom)

    verbe = "dégreffés" if args.retirer else "greffés"
    etat = "déjà propres" if args.retirer else "déjà greffés"
    print(f"{verbe} : {len(faits)}  {' '.join(faits)}")
    if laisses:
        print(f"{etat} : {' '.join(laisses)}")
    if not args.retirer:
        print("\nmodule-probleme est généré : python3 build/module.py module-probleme "
              "le refera à partir du gabarit déjà greffé.")


if __name__ == "__main__":
    main()
