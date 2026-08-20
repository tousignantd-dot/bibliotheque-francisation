#!/usr/bin/env python3
"""Une explication au survol sur les deux repères de l'en-tête des modules.

L'en-tête porte deux choses qu'on ne peut pas déduire en les regardant :
l'étoile chiffrée (« ⭐ 3 / 24 » — trois quoi, sur vingt-quatre quoi ?) et le
bouton « Réinitialiser », dont personne ne sait ce qu'il efface au juste. Un
élève n'ose pas cliquer un bouton qui pourrait lui faire perdre son travail —
et il a raison de ne pas oser tant qu'on ne le lui a pas dit.

    python3 build/greffe_infobulles.py
    python3 build/greffe_infobulles.py --retirer

Le style vient du système de design (`components/infobulle.css`), déjà lié par
les onze modules : la greffe ne pose que l'attribut `data-info` et le
`tabindex` qui rend le repère atteignable au doigt et au clavier. Rien à
copier dans les modules, donc rien à regreffer si le style change.

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

# L'étoile compte les zones RÉUSSIES (`TR.correct`), pas les tentatives, et le
# dénominateur est le nombre total de zones du module (`TOTAL_ZONES`).
# « Réinitialiser » vide `S.pl`, `S.sel`, `S.fb` et `S.vfSel` — les réponses
# placées et leur rétroaction — et ne touche ni aux champs de texte, ni à
# `TR`, donc ni aux textes écrits ni à l'étoile. C'est ce que disent les deux
# phrases ci-dessous ; si le code change, elles changent.
PAIRES = [
    ('<div id="prog-chip" aria-live="polite">',
     '<div id="prog-chip" aria-live="polite" tabindex="0"'
     ' data-info="Le nombre de réponses justes que vous avez trouvées,'
     ' sur le nombre total de réponses du module.">'),
    ('<button id="btn-reset">',
     '<button id="btn-reset"'
     ' data-info="Vide les réponses placées pour recommencer les exercices.'
     ' Vos textes écrits et votre étoile ne sont pas effacés.">'),
]

TEMOIN = 'id="prog-chip" aria-live="polite" tabindex="0"'

MODULES = "assets/interactive/module-*/module-*-activite-interactive.html"


def greffe(html):
    """Pose les infobulles dans le texte d'un module. Rend (texte, changé).

    Séparée de la lecture du fichier pour que le build de module-probleme
    puisse l'appeler sur le gabarit qu'il tient déjà en mémoire."""
    if TEMOIN in html:
        return html, False
    for avant, _ in PAIRES:
        if html.count(avant) != 1:
            raise SystemExit(
                "!! repère introuvable ou en double : %s (%d)"
                % (avant[:40], html.count(avant)))
    for avant, apres in PAIRES:
        html = html.replace(avant, apres, 1)
    return html, True


def degreffe(html):
    if TEMOIN not in html:
        return html, False
    for avant, apres in PAIRES:
        html = html.replace(apres, avant, 1)
    return html, True


def _sur_fichier(chemin, action):
    s = io.open(chemin, encoding="utf-8").read()
    nom = chemin.split("/")[2]
    try:
        s2, change = action(s)
    except SystemExit as e:
        sys.exit("%s %s" % (nom, e))
    if change:
        io.open(chemin, "w", encoding="utf-8").write(s2)
    return nom, change


def main():
    parseur = argparse.ArgumentParser(description=__doc__)
    parseur.add_argument("--retirer", action="store_true",
                         help="remettre les modules dans leur état d'avant la greffe")
    args = parseur.parse_args()

    action = degreffe if args.retirer else greffe
    fichiers = sorted(glob.glob(MODULES))
    if not fichiers:
        sys.exit("!! aucun module trouvé — lancer depuis la racine du projet")

    faits, laisses = [], []
    for chemin in fichiers:
        nom, change = _sur_fichier(chemin, action)
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
