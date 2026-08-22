# -*- coding: utf-8 -*-
"""D2 · Du dit à l'écrit
Bloc D « Défi 3 » · couleur ambre · 75 min. Langue de l'écrit administratif.
Source : exercices `t3mots`, `t3nom`, `t3ps` et `t3ponct`, leurs mini-leçons.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='D2', section='ambre',
        titre="Du dit à l'écrit",
        chapeau="« Fatigue persistante d'apparition progressive » : c'est "
                "Leyla qui a dit ça. Rien n'a été ajouté, rien n'a été "
                "retiré — le même contenu a changé de vocabulaire.",
        duree='75 minutes')

    d.titre(notes="Séance dense : quatre points en soixante-quinze minutes. Le "
                  "premier et le deuxième sont le cœur ; le passé simple et la "
                  "ponctuation se traitent en vingt minutes à eux deux.")

    d.objectifs([
        "retrouver sa propre phrase sous les mots du dossier ;",
        "faire un nom avec un verbe, et un adjectif avec un nom ;",
        "reconnaître un passé simple et le traduire en passé composé ;",
        "lire ce que disent le tiret, la virgule et les guillemets.",
    ], notes="Le premier objectif est celui qui apaise : les mots savants ne "
             "contiennent aucune information que l'élève n'ait lui-même donnée.")

    d.declencheur(
        'Observation', "Deux phrases qui disent la même chose",
        pistes=[
            "« Je suis fatiguée et ça ne part pas. »",
            "« Fatigue persistante. »",
            "Qu'est-ce qui a changé ? Qu'est-ce qui n'a pas changé ?",
        ],
        notes="Trois minutes. Amener le groupe à dire lui-même que rien n'a été "
              "ajouté. C'est le point de départ de toute la séance, et il vaut mieux "
              "qu'il vienne d'eux.")

    d.tableau('Analyse', "Le mot dit et le mot écrit",
              ['Ce que Leyla a dit', 'Ce que la lettre écrit'],
              [["Ça ne part pas.", "fatigue persistante"],
               ["Je pensais que c'était l'hiver.", "d'apparition progressive"],
               ["Je montais en parlant.", "réduction de la tolérance à l'effort"],
               ["On ne sait pas pourquoi.", "d'étiologie à préciser"],
               ["Elle ne m'a pas donné de réponse.", "aucun diagnostic retenu à ce stade"]],
              cle=0,
              note="Ces mots ne sont pas plus savants : ils sont plus courts, et ils veulent dire la même chose partout au pays.",
              notes="Diapositive à photographier. Faire lire dans les deux sens : de "
                    "gauche à droite pour comprendre un document, de droite à gauche "
                    "pour l'expliquer à quelqu'un.")

    d.regle("Gardez vos mots pour vos proches",
            "Les mots de la lettre servent au laboratoire ; les vôtres servent chez vous.",
            precision="Dire « j'ai une réduction de la tolérance à l'effort » à sa "
                      "sœur ne communique rien. Un mot qu'on peut redire dans sa "
                      "propre langue courante est un mot compris ; un mot qu'on ne "
                      "peut que répéter ne l'est pas encore.",
            notes="Diapositive à photographier. Annoncer E2 : la lettre personnelle "
                  "devra être écrite avec les mots de l'élève, et l'emploi du "
                  "vocabulaire du dossier y sera contre-productif.")

    d.tableau('Analyse', "Faire un nom avec un verbe",
              ['Le verbe', 'Le nom'],
              [["prélever", "le prélèvement"],
               ["consulter", "la consultation"],
               ["apparaître", "l'apparition"],
               ["attendre", "l'attente"],
               ["répondre", "la réponse"],
               ["suivre", "le suivi"]],
              cle=0,
              notes="Les trois premiers sont réguliers : -ment, -tion, -tion. Les "
                    "trois derniers sont irréguliers et s'apprennent en paires. "
                    "Faire noter le nom avec son article, toujours.")

    d.piege('Grammaire',
            "l'attendement, le répondement",
            "l'attente, la réponse",
            "Six verbes courants n'ont pas de nom en -ment : attendre, "
            "répondre, suivre, partir, choisir, venir. Ils s'apprennent en "
            "paires, comme un mot et son genre. Tout le reste se devine "
            "raisonnablement.",
            notes="Faire écrire les six paires au cahier, avec l'article. C'est le "
                  "seul apprentissage par cœur du module, et il tient en six lignes.")

    d.tableau('Analyse', "Un temps qu'on lit et qu'on n'écrit jamais",
              ['On lit', 'On dirait'],
              [["elle attendit onze mois", "elle a attendu onze mois"],
               ["elle comprit ce jour-là", "elle a compris ce jour-là"],
               ["l'association naquit ainsi", "l'association est née ainsi"],
               ["il fallut deux ans", "il a fallu deux ans"]],
              cle=0,
              note="Le programme demande de le reconnaître, jamais de l'écrire. Traduisez-le et continuez à lire.",
              notes="Diapositive à photographier. Rassurer explicitement : personne ne "
                    "sera évalué sur la production du passé simple. Le temps gagné "
                    "ici sert au plus-que-parfait, qui s'emploie tous les jours.")

    d.tableau('Analyse', "Trois signes qui portent du sens",
              ['Le signe', 'Ce qu\'il fait'],
              [["Le tiret", "ouvre une étape du plan, ou change de personne"],
               ["Les deux virgules", "encadrent un ajout qu'on pourrait retirer"],
               ["Les guillemets", "disent que le mot est celui de quelqu'un d'autre"]],
              cle=0,
              note="Un texte administratif ne met presque rien en gras : il ponctue. Comptez d'abord les tirets.",
              notes="Diapositive à photographier. C'est le réflexe le plus rentable de "
                    "tout le module : compter les tirets de la conduite proposée "
                    "avant de lire quoi que ce soit d'autre.")

    d.pratique('Grammaire', "Du verbe au nom",
               "Écrivez le nom qui manque.", [
        ("Elle a attendu sept mois. Cette ___ a été la partie la plus dure.", "attente"),
        ("On lui a prélevé du sang. Le ___ date de mars.", "prélèvement"),
        ("Son médecin l'a envoyée consulter. Cette ___ a eu lieu le 12 novembre.", "consultation"),
        ("On la reverra. Ce ___ est prévu dans six à huit semaines.", "suivi"),
        ("La fatigue est venue peu à peu. Son ___ a été progressive.", "apparition"),
        ("Elle a de la fièvre depuis deux jours. Elle est ___.", "fiévreuse"),
    ], corrige=True,
       notes="Le dernier est un adjectif et non un nom : c'est voulu, le programme "
             "demande les deux dans la même ligne. Faire remarquer l'accent qui "
             "change entre fièvre et fiévreuse.")

    d.pratique('Lecture', "Quel signe fait ce travail ?",
               "Le tiret, la virgule, ou les guillemets ?", [
        ("Il ouvre chacune des trois étapes du plan.", "le tiret"),
        ("Elle encadre « 41 ans » dans la première phrase.", "la virgule"),
        ("Ils entourent le mot « correcte », qui est celui de la patiente.", "les guillemets"),
        ("Il marque le changement de personne dans un dialogue.", "le tiret"),
        ("Elle encadre « aide à domicile » au milieu de la phrase.", "la virgule"),
    ], corrige=True,
       notes="Corriger vite : le point est simple et il a été vu à l'analyse. Garder "
             "du temps pour le billet, qui prépare la production écrite.")

    d.billet(
        "Traduisez pour votre famille : « aucun diagnostic retenu à ce stade ».",
        exemples=[
            "Une phrase, avec vos mots à vous.",
            "Imaginez que vous le dites au téléphone, ce soir.",
        ],
        notes="Cinq minutes. Lire trois billets à voix haute sans nommer les auteurs. "
              "C'est l'exercice qui prépare le mieux la lettre personnelle de E2.")

    return d.save(dossier)
