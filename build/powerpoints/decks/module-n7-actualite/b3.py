# -*- coding: utf-8 -*-
"""B3 · Ce qui est confirmé et ce qui ne l'est pas
Bloc B « Défi 1 · Le reportage » · couleur ambre · 75 min.
Source : exercice `t1cond` et sa mini-leçon — le conditionnel de
l'information non confirmée.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B3', section='ambre',
        titre="Ce qui est confirmé et ce qui ne l'est pas",
        chapeau="« Le local est loué » et « le local serait loué » ne disent "
                "pas la même chose. Une syllabe sépare une information "
                "garantie d'une information que le journaliste n'a pas "
                "vérifiée.",
        duree='75 minutes')

    d.titre(notes="Troisième écoute du reportage, et premier point de grammaire du "
                  "défi. Commencer par écrire les deux phrases au tableau et demander "
                  "au groupe s'il voit une différence de sens.")

    d.objectifs([
        "reconnaître le conditionnel présent à l'oreille ;",
        "comprendre qu'il signale une information non vérifiée ;",
        "former le conditionnel présent des verbes courants ;",
        "distinguer ce conditionnel de celui de la politesse et de l'hypothèse.",
    ], notes="Le quatrième objectif évite un malentendu durable : l'élève connaît déjà "
             "« pourriez-vous » et croira que c'est le même emploi.")

    d.declencheur(
        'Écoute', "Une syllabe, et tout change",
        pistes=[
            "« Le local est loué pour cinq ans. »",
            "« Le local serait loué pour cinq ans. »",
            "Dans quel cas le journaliste répond-il de l'information ?",
            "Quel mot, juste avant, vous met sur la piste ?",
        ],
        notes="Faire écouter les deux versions dans le laboratoire de la mini-leçon. "
              "La différence s'entend à la fin du verbe, et nulle part ailleurs.")

    d.regle("Le conditionnel de l'information non confirmée",
            "Un verbe en -ait, sans « si » dans la phrase : le journaliste n'a pas vérifié.",
            precision="Ce n'est ni de la politesse ni de l'hésitation : c'est une règle "
                      "de métier. Affirmer sans avoir vérifié est une faute "
                      "professionnelle, alors on met le verbe au conditionnel et "
                      "l'auditeur est prévenu. L'information se révèle souvent exacte "
                      "par la suite ; elle n'est simplement pas garantie.",
            notes="Diapositive à photographier. Insister sur « non vérifié » et non "
                  "« faux » : c'est la nuance que les élèves manquent le plus.")

    d.tableau('Analyse', "Comment il se forme",
              ['Ce qu\'on prend', 'Ce que ça donne'],
              [["le radical du futur simple", "ouvrir : il ouvrira"],
               ["les terminaisons de l'imparfait", "-ais, -ais, -ait, -ions, -iez, -aient"],
               ["le résultat", "il ouvrirait, ils ouvriraient"],
               ["les quatre verbes du journaliste", "il serait, il aurait, il pourrait, il devrait"]],
              cle=0,
              note="« Il ouvrira » et « il ouvrirait » ne diffèrent que par la fin. C'est peu, et c'est décisif.",
              notes="Diapositive à photographier. Faire apprendre les quatre verbes de "
                    "la dernière ligne par coeur : ils couvrent la grande majorité des "
                    "cas entendus à la radio.")

    d.cartes("Les formules qui annoncent le conditionnel", "À guetter à l'écoute", [
        ("Selon nos informations",
         "La plus fréquente. Le verbe qui suit sera presque toujours au conditionnel."),
        ("Selon une source proche du dossier",
         "Quelqu'un a parlé au journaliste, mais ne veut pas être nommé."),
        ("Il semble que",
         "Plus prudent encore : même la source n'est pas certaine."),
        ("La Ville indique que",
         "Une institution parle, sans personne nommée. À traiter avec la même prudence."),
    ], notes="Faire relever ces formules dans le reportage. Elles sont le signal "
             "d'alarme : l'élève qui les entend sait qu'il ne doit pas répéter la suite "
             "comme une certitude.")

    d.piege("Lire le conditionnel comme un doute quand il y a un « si »",
            "S'il ouvrait, ce serait mieux qu'un rideau baissé.",
            "Selon nos informations, le local serait loué pour cinq ans.",
            "La première phrase est une hypothèse : le conditionnel dépend d'un « si » "
            "imaginaire, et Marjolaine ne doute de rien, elle imagine. La seconde est "
            "une information non confirmée. Le repère est simple : cherchez un « si » "
            "dans la phrase. S'il n'y en a pas, c'est de l'information non vérifiée.",
            notes="Les deux phrases viennent du même reportage, ce qui rend la "
                  "comparaison concrète. Le piège est fréquent et se corrige vite avec "
                  "ce repère.")

    d.pratique('Application', "Confirmé, ou pas ?",
               "Mettez le verbe au présent si l'information est confirmée, au conditionnel sinon.", [
        ("La Ville confirme qu'elle (étudier) le local de la rue Boisjoli.", "étudie - confirmé"),
        ("Selon nos informations, le local (être) loué pour cinq ans.", "serait - non confirmé"),
        ("Toujours selon nos sources, les travaux (commencer) au printemps.", "commenceraient"),
        ("Il semble que le dépôt (pouvoir) accueillir trois mille personnes.", "pourrait"),
        ("La Ville indique qu'un dépôt de cette taille (être) ouvert six jours sur sept.", "serait"),
        ("Le communiqué précise que la décision (revenir) au conseil municipal.", "revient - c'est écrit"),
    ], corrige=True,
       notes="Faire justifier chaque réponse par le mot déclencheur : « confirme », "
             "« selon nos informations », « il semble que », « précise ». C'est le mot "
             "qui décide, pas le sens général.")

    d.billet(
        "Écrivez une information que vous avez entendue sans pouvoir la vérifier.",
        exemples=[
            "Mettez le verbe au conditionnel.",
            "Par exemple : « Il paraît que le dépôt ouvrirait au printemps. »",
        ],
        notes="Deux minutes. Un excellent révélateur : ceux qui écrivent le présent "
              "n'ont pas encore fait le lien entre la forme et l'engagement.")

    return d.save(dossier)
