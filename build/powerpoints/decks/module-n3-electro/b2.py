# -*- coding: utf-8 -*-
"""B2 · Lire un prix de trois ou quatre chiffres.
Bloc B « Défi 1 · Lire la circulaire » · couleur ambre (écriture) · 60 min.
Source : exercice `t1prix`, mini-leçon `t1prix`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B2', section='ambre',
        titre='Huit cent quarante-neuf dollars',
        chapeau="À l'épicerie, les prix ont deux chiffres. Un appareil en "
                "demande trois ou quatre, et le magasin les dit vite. Le "
                "papier, lui, ne parle pas vite.",
        duree='60 minutes')

    d.titre(notes="Séance d'écriture et de nombres. Prévoir d'écrire beaucoup au "
                  "tableau : les élèves doivent voir le chiffre et entendre le mot en "
                  "même temps.")

    d.objectifs([
        "lire à voix haute un prix de trois ou quatre chiffres ;",
        "écrire en chiffres un prix qu'on entend ;",
        "dire soixante-dix, quatre-vingts et quatre-vingt-dix ;",
        "écrire un prix à la québécoise : 849 $, 129,99 $.",
    ])

    d.regle("On dit les centaines d'abord",
            "849 $  se dit  « huit cent quarante-neuf dollars »",
            precision="Le chiffre des centaines, puis le mot « cent », puis le "
                      "reste. Rien à ajouter devant, rien à ajouter derrière.",
            notes="Diapo à photographier. Écrire trois autres prix au tableau et faire "
                  "lire par trois élèves différents.")

    d.tableau('Analyse', "Les nombres qui font peur",
              ['On écrit', 'On dit'],
              [["70", "soixante-dix"],
               ["80", "quatre-vingts"],
               ["90", "quatre-vingt-dix"],
               ["879", "huit cent soixante-dix-neuf"]],
              cle=1,
              note="Ici, on ne dit ni septante ni nonante : ces trois formes-là, "
                   "et seulement elles.",
              notes="Diapo à photographier. Ces trois nombres reviennent dans tous les "
                    "prix : les faire répéter jusqu'à ce qu'ils sortent sans réfléchir.")

    d.tableau('Analyse', "Au-dessus de mille",
              ['On écrit', 'On dit'],
              [["1 049 $", "mille quarante-neuf dollars"],
               ["1 200 $", "mille deux cents dollars"],
               ["2 000 $", "deux mille dollars"]],
              cle=1,
              note="Jamais « un mille » : le mot mille se dit seul.",
              notes="Faire remarquer l'espace entre le chiffre des milliers et le reste. "
                    "C'est une règle d'écriture française, pas une virgule.")

    d.pratique('Écriture', "Écrivez le prix en chiffres",
               "Écrivez seulement les chiffres.", [
        ("huit cent quarante-neuf dollars", "849 $"),
        ("mille quarante-neuf dollars", "1 049 $"),
        ("cent vingt-neuf dollars", "129 $"),
        ("six cent soixante-quinze dollars", "675 $"),
        ("quatre-vingt-dix dollars", "90 $"),
        ("deux cent quatre-vingts dollars", "280 $"),
    ], corrige=True,
       notes="Dicter les prix plutôt que de les projeter : c'est ainsi qu'ils arrivent "
             "à la caisse. Projeter le corrigé après.")

    d.piege("Confondre 849 et 840",
            "huit cent quarante",
            "huit cent quarante-neuf",
            "La différence est au dernier mot, et c'est là qu'on écoute le moins. Au "
            "magasin, une seule phrase règle la question : « Huit cent quarante ou "
            "quarante-neuf ? » Personne ne trouve la question étrange.",
            notes="Faire pratiquer la question de vérification à voix haute. Elle "
                  "reviendra dans le jeu de rôle de E1.")

    d.cartes("Écrire un prix comme ici", "Trois habitudes d'écriture", [
        ("Le signe est à droite",
         "On écrit 849 $, avec une espace avant le signe. Jamais « $ 849 » : c'est "
         "l'ordre de l'anglais."),
        ("La virgule est pour les cents",
         "129,99 $ se lit « cent vingt-neuf et quatre-vingt-dix-neuf ». La virgule "
         "sépare les dollars des cents, jamais les milliers."),
        ("L'espace est pour les milliers",
         "1 049 $, et non 1,049 $. Une espace, pas une virgule : c'est la règle "
         "française."),
    ], cols=3,
       notes="Écrire les trois formes fautives au tableau et faire venir corriger. "
             "L'erreur la plus fréquente est la virgule des milliers, prise à l'anglais.")

    d.pratique('Lecture', "Lisez le prix à voix haute",
               "Un élève lit, un autre écrit au tableau.", [
        ("99 $", "quatre-vingt-dix-neuf dollars"),
        ("175 $", "cent soixante-quinze dollars"),
        ("399 $", "trois cent quatre-vingt-dix-neuf dollars"),
        ("1 299 $", "mille deux cent quatre-vingt-dix-neuf dollars"),
    ], corrige=True,
       notes="Travail en paires. Celui qui écrit ne voit pas le chiffre : c'est "
             "l'exercice de la caisse, exactement.")

    d.billet(
        "Relevez quatre prix dans votre circulaire et écrivez-les en lettres.",
        exemples=[
            "849 $ : huit cent quarante-neuf dollars",
            "Choisissez au moins un prix de plus de mille dollars.",
        ],
        notes="Devoir d'écriture. Ramasser : les erreurs de « quatre-vingts » et de "
              "l'espace des milliers se corrigent une fois pour toutes ici.")

    return d.save(dossier)
