# -*- coding: utf-8 -*-
"""C3 · Les petits mots qui portent les dates
Bloc C « Défi 2 · Lire l'avis du centre » · couleur ambre · 75 min.
Source du module : exercice `t2prep` et sa mini-leçon.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C3', section='ambre',
        titre="Les petits mots qui portent les dates",
        chapeau="Retirez d'un avis les mots « à partir du », « jusqu'au », "
                "« d'ici le », « avant le », « dès » et « en cas de », et il "
                "ne reste qu'une liste de chiffres. Ce sont eux qui disent "
                "lequel commence, lequel finit, et lequel vous concerne.",
        duree='75 minutes')

    d.titre(notes="Séance de grammaire. Le programme du niveau 5 accorde douze points de "
                  "savoir aux prépositions : c'est le plus gros bloc du niveau, et c'est "
                  "là que se joue la compréhension d'un document officiel.")

    d.objectifs([
        "employer « à partir du » et « jusqu'au » en paire, jamais seuls ;",
        "reconnaître une échéance à « d'ici le » et « au plus tard le » ;",
        "distinguer « avant le » de « jusqu'au » ;",
        "employer « dès » et « en cas de » devant un nom.",
    ], notes="Le premier objectif est celui qui sert à écrire ; les trois autres servent "
             "à lire. Les deux compétences sont dans le même point de grammaire, ce qui "
             "est rare — le dire au groupe.")

    d.regle("Le début et la fin vont par paire",
            "« À partir du 9 mars » ouvre. « Jusqu'au 27 mars inclusivement » "
            "ferme.",
            precision="« Inclusivement » n'est pas un ornement : sans lui, personne "
                      "ne sait si le 27 est dedans ou dehors.",
            notes="Diapositive à photographier. Le mot « inclusivement » manquait dans "
                  "presque tous les billets de B1 : c'est ici qu'on le récupère, et il "
                  "faut le faire écrire trois fois.")

    d.cartes("Six mots, six sens", "Ce que chacun fait à une date", [
        ("à partir du · dès",
         "Ça commence là. « Dès » ajoute : aussitôt que, sans attendre."),
        ("jusqu'au",
         "Ça finit là, ce jour-là compris si on écrit « inclusivement »."),
        ("d'ici le · au plus tard le",
         "Vous avez jusqu'à cette date pour agir. C'est l'échéance."),
        ("avant le · en cas de",
         "Strictement avant cette date. Et : si cela arrive, suivi d'un nom."),
    ], notes="Faire répéter les six avec une date réelle, celle du jour. « À partir "
             "d'aujourd'hui », « d'ici vendredi » : la date connue fait sentir la "
             "différence mieux qu'un exemple abstrait.")

    d.pratique('Emploi', "Le bon petit mot",
               "Complétez à l'oral, puis à l'écrit.", [
        ("Je serai absente ___ 9 mars, et je reviendrai le 30.", "à partir du"),
        ("Mon absence court ___ 27 mars inclusivement.", "jusqu'au"),
        ("Le formulaire signé doit vous parvenir ___ 6 mars.", "d'ici le"),
        ("Veuillez communiquer avec le secrétariat ___ 27 mars.", "avant le"),
        ("___ mon retour, je m'inscrirai au rattrapage.", "Dès"),
        ("___ prolongation, je vous appellerai tout de suite.", "En cas de"),
    ], corrige=True,
       notes="Faire dire la phrase entière. La cinquième et la sixième sont les seules "
             "qui commencent la phrase : la virgule qui suit est obligatoire, et elle "
             "manque presque toujours.")

    d.tableau('Deux mots proches', "« Avant le » et « jusqu'au »",
              ['Avant le 27', 'Jusqu'"'"'au 27'],
              [["Le 27 n'est plus dedans", "Le 27 est dedans, si « inclusivement »"],
               ["Vous agissez au plus tard le 26", "Vous êtes concerné le 27 aussi"],
               ["Annonce une action de votre part", "Annonce une période"],
               ["En cas de doute : deux jours plus tôt", "En cas de doute : demandez"]],
              cle=1,
              notes="Beaucoup d'avis emploient les deux pour la même idée, et ce n'est "
                    "pas rigoureux. La consigne pratique tient en une phrase : en cas de "
                    "doute, faites la chose deux jours plus tôt.")

    d.piege("Lire « d'ici le 6 » comme « le 6 »",
            "L'échéance est le 6 : j'irai porter le formulaire le 6.",
            "L'échéance est le 6 : j'irai le porter le 3 ou le 4.",
            "Un formulaire remis le jour même de l'échéance ne laisse aucune marge. "
            "S'il manque une case, une signature ou une date, il est trop tard pour "
            "revenir — et vous aurez pourtant respecté la limite.",
            notes="Cette remarque n'est pas de la grammaire, et elle vaut plus que la "
                  "grammaire. La dire, puis revenir au point de langue.")

    d.pratique('Écriture', "Vos propres dates",
               "Écrivez quatre phrases avec vos dates à vous, vraies ou inventées.", [
        ("Une phrase avec « à partir du » et « jusqu'au ».",
         "n'oubliez pas « inclusivement »"),
        ("Une phrase avec « d'ici le », pour une chose que vous devez faire.",
         "l'échéance"),
        ("Une phrase avec « dès », en tête de phrase.", "attention à la virgule"),
        ("Une phrase avec « en cas de », suivie d'un nom.",
         "jamais un verbe conjugué derrière"),
    ], corrige=False,
       notes="Passer dans les rangées. L'erreur la plus fréquente est « en cas de que je "
             "reste » : rappeler qu'on écrit alors « si je dois rester ».")

    d.regle("« En cas de » veut un nom",
            "En cas de prolongation. En cas d'absence. En cas de retard.",
            precision="Si vous n'avez qu'un verbe sous la main, écrivez « si » : "
                      "« si vous devez rester plus longtemps ».",
            notes="Diapositive à photographier. C'est la seule règle de la séance qui "
                  "porte sur ce qui suit le mot plutôt que sur son sens, et c'est celle "
                  "qu'on oublie en écrivant.")

    d.billet(
        "Écrivez la période de votre absence et son échéance, en deux phrases.",
        exemples=[
            "La période avec « à partir du » et « jusqu'au... inclusivement ».",
            "L'échéance avec « d'ici le ».",
        ],
        notes="Ramasser les billets. Ils reprennent ceux de B1 en les complétant : "
              "comparer les deux versions avec les élèves concernés vaut mieux qu'une "
              "correction écrite.")

    return d.save(dossier)
