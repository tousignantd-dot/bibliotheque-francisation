# -*- coding: utf-8 -*-
"""B2 · Deux articles, une seule séance
Bloc B « Défi 1 » · couleur teal · 75 min.
Source : exercice `t1deux` (type `texte`) — les dépêches du Courant de la
Rive et de La Vigie de la Rive, et son bandeau « Ce qu'on regarde quand on
met deux articles côte à côte ».
"""
from theme import Deck

import pathlib

IMG = str(pathlib.Path(__file__).resolve().parents[4]
          / 'assets' / 'interactive' / 'module-n8-actualite' / 'images') + '/'


def build(dossier):
    d = Deck(
        code='B2', section='teal',
        titre="Ce qui apparaît quand on met les deux côte à côte",
        chapeau="Lus l'un après l'autre, les deux articles semblent tous "
                "deux raisonnables. Lus côte à côte, ligne par ligne, ils "
                "montrent cinq choix que ni l'un ni l'autre n'avoue.",
        duree='75 minutes')

    d.titre(notes="Séance de compréhension écrite. Distribuer les deux dépêches sur "
                  "une seule feuille, en deux colonnes : la mise en page fait la "
                  "moitié du travail, et une lecture successive ne donne rien.")

    d.objectifs([
        "lire deux comptes rendus d'un même fait en parallèle ;",
        "relever le mot choisi pour nommer la même chose ;",
        "comparer ce qui est mis en premier et ce qui est repoussé ;",
        "trouver ce que les deux disent pareil, et savoir pourquoi ça compte.",
    ], notes="Le quatrième objectif est le plus utile pour la lettre du défi 3 : ce "
             "qui est commun aux deux versions est ce sur quoi on peut s'appuyer sans "
             "être contredit.")

    d.declencheur(
        'Observation', "Deux titres, un seul vote",
        image=IMG + 'hotel-de-ville.jpg',
        pistes=[
            "« Quarante-cinq logements abordables à Rivière-aux-Cèdres »",
            "« Onze hectares cédés pour un dollar, à 22 h 50 »",
            "Laquelle des deux phrases est fausse ?",
            "Qu'est-ce que chaque titre vous donne envie de penser avant même l'article ?",
        ],
        notes="Poser la troisième question et attendre. La réponse est : aucune. "
              "C'est le moment où le groupe comprend que le travail de la séance "
              "n'est pas de démasquer un menteur.")

    d.cartes('Analyse', "Cinq choses à regarder, dans cet ordre", [
        ("Le mot choisi pour nommer la chose",
         "« Un terrain municipal sous-utilisé » et « le boisé "
         "Sainte-Perpétue » désignent les mêmes onze hectares. Le lecteur "
         "croit avoir lu un fait ; il a lu un cadrage."),
        ("Ce qui est mis en premier",
         "Un article commence par ce que sa rédaction juge important. Le "
         "même vote ouvre sur quarante-cinq logements ou sur quatre voix "
         "contre trois à vingt-deux heures cinquante. Les deux sont vrais."),
        ("Qui parle, et combien de lignes",
         "Comptez les lignes données à chaque camp. Un article qui cite le "
         "promoteur sur douze lignes et le comité sur deux a fait un choix, "
         "même s'il a cité les deux."),
        ("Le chiffre présent et le chiffre absent",
         "Nombre d'arbres, coût d'entretien, heure du vote, personnes dans "
         "la salle : chacun sert quelqu'un. Ce qui manque d'un côté se "
         "trouve presque toujours dans l'autre."),
    ], notes="Les quatre points se travaillent dans l'ordre sur la feuille à deux "
             "colonnes, au crayon, chacun avec un signe différent dans la marge.")

    d.tableau('Analyse', "Le même terrain, la même séance",
              ['Le Courant de la Rive', 'La Vigie de la Rive'],
              [["« un terrain municipal sous-utilisé »",
                "« le boisé Sainte-Perpétue »"],
               ["ouvre sur les quarante-cinq logements abordables",
                "ouvre sur quatre voix contre trois, devant onze personnes"],
               ["donne le coût d'entretien : onze mille dollars par année",
                "donne le délai : quatre jours après l'évaluation"],
               ["cite le maire et le promoteur",
                "cite le comité et l'absence d'étude sur le terrain de l'aréna"],
               ["quatre-vingt-dix arbres, replantés à deux pour un",
                "trois cent quarante-deux arbres dénombrés"]],
              cle=0,
              notes="Diapositive à photographier. Faire remarquer la cinquième ligne : "
                    "les deux chiffres viennent chacun de la source qui arrange celui "
                    "qui la cite, et aucun des deux journaux ne cite l'autre comptage.")

    d.regle("Cherchez d'abord ce que les deux disent pareil",
            "Les deux journaux rapportent le même nombre d'unités, cent "
            "quatre-vingts, et la même clause de pénalité de deux millions "
            "de dollars. C'est ce qu'il y a de plus solide dans tout le "
            "dossier.",
            precision="Quand deux rédactions qui ne se ressemblent pas écrivent le "
                      "même chiffre, vous pouvez vous appuyer dessus sans crainte "
                      "d'être contredit. Une lettre au courrier des lecteurs qui part "
                      "de ce socle commun est beaucoup plus difficile à attaquer "
                      "qu'une lettre qui part du chiffre de son propre camp.",
            notes="Diapositive à photographier, et à rappeler au défi 3 au moment "
                  "d'écrire la lettre. C'est le conseil le plus rentable du bloc.")

    d.pratique('Pratique 1 de 2', "Dans quel article, et pourquoi ?",
               "Dites de quel article vient le passage, et ce qu'il sert à faire.", [
        ("« a autorisé lundi la cession d'un terrain municipal sous-utilisé »",
         "Le Courant - nomme le terrain du côté du projet"),
        ("« dont quatre hectares sont plantés d'érables de plus de soixante ans »",
         "La Vigie - nomme le terrain du côté du comité"),
        ("« qui coûtait à la Ville près de onze mille dollars par année »",
         "Le Courant - le terrain coûte sans rapporter"),
        ("« Par quatre voix contre trois, devant onze personnes »",
         "La Vigie - les conditions du vote"),
        ("« a été adopté quatre jours après la réception de l'évaluation »",
         "La Vigie - met en cause la rapidité"),
        ("« la même clause de pénalité de deux millions de dollars »",
         "les deux - le socle commun"),
    ], corrige=True,
       notes="Le sixième item est le seul dont la réponse est « les deux », et c'est "
             "celui à souligner. Beaucoup d'élèves l'attribuent au Courant, parce que "
             "la clause sert le projet.")

    d.piege('Piège', "« celui-là est neutre »",
            "les deux ont choisi",
            "Un article qui emploie des mots administratifs paraît neutre, "
            "et il ne l'est pas davantage que l'autre : « un actif "
            "sous-utilisé » est un choix, exactement comme « un poumon "
            "vert ». Ce qui existe, c'est un vocabulaire vérifiable — « onze "
            "hectares, dont quatre boisés » — et il est rare dans les deux.",
            notes="Défaut de lecture très répandu : le ton posé se confond avec "
                  "l'objectivité. Faire relire la première phrase du Courant à voix "
                  "haute, lentement, en s'arrêtant sur « sous-utilisé ».")

    d.pratique('Pratique 2 de 2', "La question qui manque",
               "Après avoir lu les deux, quelle question poseriez-vous à la Ville ?", [
        ("Sur les deux comptages d'arbres", "à partir de quel diamètre avez-vous compté ?"),
        ("Sur l'évaluation du terrain", "pourquoi n'a-t-elle pas été rendue publique ?"),
        ("Sur le terrain de l'aréna", "quelle étude a été faite, et par qui ?"),
        ("Sur les vingt et un mois de rezonage", "sur quoi cette estimation repose-t-elle ?"),
    ], corrige=True,
       notes="Chaque question sort d'un écart relevé entre les deux articles, pas "
             "d'une opinion. Le faire dire explicitement : c'est la méthode, et elle "
             "sert telle quelle à l'assemblée publique du défi 3.")

    d.billet(
        "Trouvez le socle commun : écrivez les trois choses que les deux articles disent pareil.",
        exemples=[
            "Un chiffre, une date, une clause.",
            "Écrivez-les dans une phrase que les deux rédactions signeraient.",
        ],
        notes="Devoir. Ces trois phrases seront reprises telles quelles au défi 3, en "
              "ouverture de la lettre : on commence toujours par ce que personne ne "
              "conteste.")

    return d.save(dossier)
