# -*- coding: utf-8 -*-
"""B3 · Ce qui s'était passé avant
Bloc B « Défi 1 » · couleur ambre · 75 min. Grammaire du récit.
Source : exercice `t1pqp` et sa mini-leçon.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B3', section='ambre',
        titre="Ce qui s'était passé avant",
        chapeau="Raconter, ce n'est pas énumérer. Un seul temps du français "
                "a pour travail de reculer d'un cran, et sans lui tout "
                "arrive en même temps.",
        duree='75 minutes')

    d.titre(notes="Séance de grammaire. Le plus-que-parfait est déjà connu de "
                  "plusieurs élèves sans qu'ils sachent le nommer : commencer par "
                  "leur faire produire la forme avant de l'expliquer.")

    d.objectifs([
        "former le plus-que-parfait avec l'auxiliaire à l'imparfait ;",
        "choisir le bon auxiliaire et accorder le participe ;",
        "placer un évènement avant un autre évènement passé ;",
        "reconnaître à l'écoute qu'un récit vient de reculer d'un cran.",
    ], notes="Le quatrième objectif est celui du niveau : au niveau 6, on suit un "
             "récit avant de le produire. C'est aussi celui qu'on évalue le moins "
             "souvent et qui sert le plus.")

    d.declencheur(
        'Observation', "Deux phrases, laquelle est arrivée en premier ?",
        pistes=[
            "« Elle est venue au rendez-vous. Son médecin avait envoyé la demande. »",
            "Laquelle des deux choses est arrivée d'abord ?",
            "Qu'est-ce qui vous le dit ? Un mot ? La place dans la phrase ?",
        ],
        notes="Trois minutes. Le groupe trouve presque toujours la bonne réponse sans "
              "savoir pourquoi. C'est le meilleur départ possible : la forme est déjà "
              "comprise, il reste à la nommer.")

    d.tableau('Analyse', "Le passé composé et le passé d'avant",
              ['On dit', 'Ce que ça place'],
              [["elle a attendu", "un fait passé, raconté depuis aujourd'hui"],
               ["elle avait attendu", "un fait déjà accompli au moment dont on parle"],
               ["elle est venue", "un fait passé, auxiliaire être"],
               ["elle était venue", "le même fait, un cran plus loin en arrière"]],
              cle=0,
              note="Une seule différence : l'auxiliaire passe au présent ou à l'imparfait.",
              notes="Diapositive à photographier. Faire lire les quatre lignes à voix "
                    "haute : la différence est minime à l'oreille et énorme dans le "
                    "sens.")

    d.regle("C'est votre passé composé, avec l'auxiliaire à l'imparfait",
            "Rien de neuf à apprendre : un seul changement, appliqué partout.",
            precision="Le choix de l'auxiliaire ne change pas, les accords ne changent "
                      "pas, le participe passé ne change pas. Si vous dites « je suis "
                      "venue », vous direz « j'étais venue ». Si vous dites « j'ai "
                      "attendu », vous direz « j'avais attendu ».",
            notes="Diapositive à photographier. C'est la phrase qui désamorce la "
                  "séance : les élèves croient apprendre un temps de plus et ils "
                  "n'apprennent qu'un auxiliaire de plus.")

    d.tableau('Analyse', "Les accords, exactement comme au passé composé",
              ['Avec quel auxiliaire', 'Ce qui arrive au participe'],
              [["avoir", "il ne bouge pas : elle avait attendu"],
               ["être", "il s'accorde avec le sujet : elle était venue"],
               ["être, au pluriel", "ils étaient passés, elles étaient arrivées"]],
              cle=0,
              note="En cas de doute, demandez-vous quel auxiliaire vous auriez mis au passé composé.",
              notes="Diapositive à photographier. Le doute sur l'accord vient presque "
                    "toujours d'un doute sur l'auxiliaire, et non de la règle "
                    "d'accord elle-même.")

    d.cartes('Exemples', "Six récits du dossier de Leyla", [
        ("Elle est arrivée fatiguée.", "Elle avait pourtant dormi neuf heures."),
        ("En novembre, elle a vu la spécialiste.", "Son médecin avait envoyé la demande en avril."),
        ("Elle n'a rien fait au mois de mars.", "Elle avait pensé que c'était l'hiver."),
        ("En août, la femme de Gilles voulait annuler.", "Elle avait perdu le courage d'attendre."),
        ("Tout était au dossier ce matin-là.", "Les prélèvements avaient été faits au printemps."),
        ("Elle a trouvé la salle sans hésiter.", "Elle était venue une fois, en octobre."),
    ], cols=2,
       notes="Une carte à la fois. Faire lire la colonne de gauche par un élève et "
             "celle de droite par un autre : on entend alors le recul dans le temps.")

    d.piege('Grammaire',
            "je dormais neuf heures, ce matin-là",
            "j'avais dormi neuf heures, ce matin-là",
            "L'imparfait décrit une habitude ou un décor : « je dormais neuf "
            "heures, dans ce temps-là ». Le plus-que-parfait raconte une nuit "
            "précise, avant le matin dont on parle. Les deux existent, et ils "
            "ne disent pas la même chose.",
            notes="Le piège le plus fréquent chez les élèves qui ont bien appris "
                  "l'imparfait. Le corriger sans dévaloriser l'imparfait, qui reste "
                  "juste dans son emploi à lui.")

    d.pratique('Grammaire', "Mettez le verbe au plus-que-parfait",
               "La première phrase situe le moment.", [
        ("Le rendez-vous a eu lieu en novembre. Son médecin ___ la demande en avril. (envoyer)", "avait envoyé"),
        ("Elle est arrivée fatiguée. Elle ___ neuf heures, pourtant. (dormir)", "avait dormi"),
        ("Au mois de mars, elle n'a rien fait. Elle ___ que c'était l'hiver. (penser)", "avait pensé"),
        ("Elle savait où aller. Elle ___ une fois, en octobre. (venir)", "était venue"),
        ("Elle a répondu tout de suite. Elle ___ ses trois questions la veille. (écrire)", "avait écrit"),
        ("Gilles n'était pas inquiet. Sa femme et lui ___ par la même attente. (passer)", "étaient passés"),
    ], corrige=True,
       notes="Faire justifier les deux derniers : l'auxiliaire être et l'accord. "
             "Demander à chaque fois quel serait le passé composé — la réponse s'y "
             "trouve déjà.")

    d.billet(
        "Racontez en deux phrases une attente que vous avez vécue.",
        exemples=[
            "Première phrase : ce qui est arrivé.",
            "Deuxième phrase : ce qui s'était passé avant.",
        ],
        notes="Cinq minutes. Ramasser les billets et en corriger trois au tableau à la "
              "séance suivante, sans nommer les auteurs. Le sujet n'a pas à être "
              "médical : une attente d'immigration, de logement, de papiers fait "
              "aussi bien.")

    return d.save(dossier)
