# -*- coding: utf-8 -*-
"""A2 · Ou ou u ?
Bloc A « Je découvre » · couleur indigo · 75 min. Séance de graphie-phonie.
Source : exercice `prSon` et sa mini-leçon « Ou et u : deux sons, deux mots ».

Le programme du niveau 2 demande le système vocalique et la graphie-phonie.
Deux sons décident de la moitié des mots du centre : celui de « bonjour » et
celui de « une ». L'élève qui les confond dit « le boureau » et demande le
« culoir ». La séance les sépare par la langue avant de les séparer par
l'écriture.

Aucun alphabet phonétique sur les diapositives : le gabarit est en Verdana,
et le programme du niveau 2 n'en demande pas. Les sons se nomment par un mot
connu — « le son de bonjour », « le son de une ».
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A2', section='indigo',
        titre="Ou ou u ?",
        chapeau="Entendre et écrire les deux sons : « bonjour » et « une ».",
        duree='75 minutes')

    d.titre(notes="Deuxième séance. Commencer par dire quatre mots à voix haute — le "
                  "cours, le bureau, le couloir, une minute — et demander lesquels vont "
                  "ensemble. Personne ne se trompe complètement, et personne n'a tout "
                  "bon.")

    d.objectifs([
        "entendre la différence entre « bonjour » et « une » ;",
        "dire les deux sons avec la bonne langue ;",
        "lire et écrire ou, u et û ;",
        "ne plus dire « le boureau » pour « le bureau ».",
    ])

    d.regle("Les lèvres avancent dans les deux cas.",
            "C'est la langue qui décide, pas les lèvres.",
            precision="Pour le son de <b>bonjour</b>, la langue recule au fond de la "
                      "bouche. Pour le son de <b>une</b>, elle monte en avant, derrière "
                      "les dents du bas. Les lèvres, elles, font la même chose.",
            notes="Diapositive à photographier. C'est le point qui fait toute la "
                  "séance : les élèves cherchent la différence dans les lèvres, où il "
                  "n'y en a pas.")

    d.tableau('Analyse · 1 de 2', "La famille du son de « bonjour »",
              ["On écrit", "Exemples"],
              [["ou", "bonjour · le cours · le couloir"],
               ["ou", "ouvert · ouvrir · vous"],
               ["La langue", "elle recule au fond de la bouche"],
               ["On ne dit pas", "« le curs » ni « le culoir »"]],
              cle=1,
              note="Une seule façon de l'écrire. C'est la famille la plus simple.",
              notes="Diapositive à photographier. Faire lire la colonne de droite à voix "
                    "haute, en série, sans commenter. La plupart des élèves possèdent "
                    "déjà ce son.")

    d.tableau('Analyse · 2 de 2', "La famille du son de « une »",
              ["On écrit", "Exemples"],
              [["u", "une · le bureau · le numéro"],
               ["u", "lundi · une minute · sur la porte"],
               ["û", "bien sûr — le petit chapeau ne s'entend pas"],
               ["L'astuce", "dire « i », puis avancer les lèvres sans bouger la langue"]],
              cle=1,
              note="Beaucoup de langues n'ont pas ce son : il s'apprend, il ne se devine pas.",
              notes="Diapositive à photographier. L'astuce de la dernière ligne marche "
                    "avec presque tout le monde. La faire essayer trois fois avant de "
                    "passer à l'écoute.")

    d.piege('Prononciation', "le boureau", "le bureau",
            "C'est le piège numéro un du module. La langue reste au fond, et le mot "
            "bascule dans l'autre famille. Faire dire « bi-reau », puis avancer les "
            "lèvres sans bouger la langue : on obtient « bureau ».",
            notes="Ce piège revient à chaque séance du module, parce que le mot "
                  "« bureau » y revient. Le corriger ici coûte une minute ; plus tard, "
                  "il est installé.")

    d.pratique('Écoute', "Ou ou u ?",
               "Écoutez chaque mot. Levez une main pour « ou », deux pour « u ».", [
        ("le cours", "ou"),
        ("le bureau", "u"),
        ("le couloir", "ou"),
        ("une minute", "u"),
        ("ouvert", "ou"),
        ("lundi", "u"),
        ("bonjour", "ou"),
        ("le numéro", "u"),
    ], corrige=True, cols=2,
       notes="Les mains levées disent tout de suite qui suit et qui devine. Reprendre "
             "seulement les mots où le groupe se sépare en deux.")

    d.pratique('Prononciation', "Quatre paires à dire",
               "Répétez après l'enseignant, puis entre vous.", [
        ("le cours / bien sûr", "la paire à réussir en premier"),
        ("le couloir / le bureau", "les deux mots du centre"),
        ("vous / vu", "« vous » revient dans chaque phrase du comptoir"),
        ("tout / tu", "une seule lettre, deux mots différents"),
    ], cols=1,
       notes="Faire produire les paires en cachant l'écrit. L'oreille passe avant la "
             "lettre : un élève qui lit la paire la réussit sans l'entendre.")

    d.pratique('Pratique · dictée courte', "Six mots à écrire",
               "L'enseignant dit le mot deux fois. Écrivez-le.", [
        ("le cours", "ou"),
        ("le bureau", "u"),
        ("le couloir", "ou"),
        ("lundi", "u"),
        ("ouvert", "ou"),
        ("une minute", "u"),
    ], corrige=True, cols=2,
       notes="Corriger au tableau, un mot à la fois. Demander à chaque fois quel son on "
             "a entendu : la lettre suit le son, jamais l'inverse.")

    d.billet(
        "Écrivez trois mots avec le son de « bonjour » et trois mots avec le son de « une ».",
        exemples=[
            "le cours, le couloir, ouvert",
            "le bureau, lundi, une minute",
        ],
        notes="Devoir court. Accepter les mots trouvés ailleurs que dans le module : un "
              "élève qui rapporte « la soupe » ou « la rue » a compris.")

    return d.save(dossier)
