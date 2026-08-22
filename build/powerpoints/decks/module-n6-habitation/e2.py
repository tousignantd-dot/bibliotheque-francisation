# -*- coding: utf-8 -*-
"""E2 · Le courriel du soir, et le bilan
Bloc E « Je me lance » · couleur framboise · 75 min. Production écrite et
autoévaluation. Source : bloc « Je me lance » de custom.js, exercice
`t3courriel` et sa mini-leçon, section « Je retiens des mots ».

La tâche écrite ne vient pas de la situation, qui n'a aucune intention de
production écrite : elle vient des attentes de fin de cours du niveau 6 —
« dans ses relations professionnelles, il rédige un courriel ou une lettre en
respectant les conventions habituelles » et « il rédige un court texte en
organisant ses idées à l'aide de paragraphes ».
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='E2', section='framboise',
        titre="Le courriel du soir, et le bilan",
        chapeau="Quatre personnes ont parlé quarante minutes. Le soir, il en "
                "reste ce que chacun a retenu — et ce n'est pas la même "
                "chose chez les quatre.",
        duree='75 minutes')

    d.titre(notes="Dernière séance du module. Prévoir quarante-cinq minutes pour le "
                  "courriel et trente pour le bilan et l'autoévaluation.")

    d.objectifs([
        "écrire un objet de courriel précis, sans phrase complète ;",
        "organiser trois paragraphes, une idée chacun ;",
        "redire ce qu'on a compris avec ses chiffres ;",
        "formuler une demande avec une date.",
    ], notes="Le quatrième objectif est celui qu'on corrige le plus : « quand vous "
             "pourrez » veut dire jamais.")

    d.declencheur(
        'Observation', "Pourquoi écrire ce qui vient d'être dit de vive voix ?",
        pistes=[
            "Est-ce de la méfiance ?",
            "Qu'est-ce qui arrive si personne ne l'écrit ?",
            "À qui ça sert, à vous ou à l'entrepreneur ?",
        ],
        notes="La réponse à la troisième question est : aux deux. Un entrepreneur "
              "sérieux est content qu'on lui confirme par écrit ce qu'il a dit — ça "
              "le protège autant que le client. Le dire clairement enlève le "
              "malaise que plusieurs élèves ressentent devant cette tâche.")

    d.tableau('Analyse', "Les six morceaux du courriel",
              ['Le morceau', 'Son travail'],
              [["l'objet", "qu'on sache de quoi il s'agit sans ouvrir"],
               ["l'appel", "nommer la personne"],
               ["le rappel", "dire d'où l'on part, dès la première ligne"],
               ["ce qu'on a compris", "pour que l'autre puisse corriger"],
               ["la demande", "une chose, avec une date"]],
              cle=0,
              note="La signature ferme le message : le nom, et à quel titre on écrit.",
              notes="Diapositive à photographier. La sixième partie est dans la note "
                    "plutôt que dans le tableau : six rangées avec une note passent "
                    "mal, et la signature est la moins difficile des six.")

    d.tableau('Analyse', "Trois paragraphes, une idée chacun",
              ['Le paragraphe', 'Ce qu\'il contient'],
              [["le premier", "pourquoi j'écris, et de quelle rencontre je parle"],
               ["le deuxième", "les deux solutions, avec prix et délais"],
               ["le troisième", "ce que je demande, et pour quand"]],
              cle=0,
              note="Une ligne vide entre les paragraphes, pas un alinéa : c'est l'usage du courriel.",
              notes="Diapositive à photographier. Le découpage se voit avant qu'on "
                    "lise, et c'est ce que les attentes de fin de cours appellent "
                    "organiser ses idées à l'aide de paragraphes.")

    d.regle("Une seule demande, et toujours une date",
            "Trois demandes dans un courriel obtiennent au mieux une réponse.",
            precision="Si vous avez trois choses à demander, écrivez trois courriels, "
                      "ou numérotez-les 1, 2, 3 — mais ne les mêlez pas dans une "
                      "phrase. Et remplacez « quand vous pourrez » par une date : "
                      "« aujourd'hui », « avant vendredi », « d'ici le 15 ». Une "
                      "date se répond, ou se refuse, et un refus est déjà un "
                      "renseignement.",
            notes="Diapositive à photographier. C'est la règle de la séance, et c'est "
                  "le critère de correction le plus simple à appliquer.")

    d.pratique('Modèle', "À éviter, à écrire",
               "Comparez les deux versions de chaque morceau.", [
        ("Objet : question", "Objet : imprévu du 8 avril, confirmation des deux options"),
        ("Vous m'avez dit qu'il y avait un problème.", "Vous m'avez présenté deux solutions : 6 800 $ et neuf jours, ou 1 900 $ et deux jours."),
        ("Pourriez-vous me revenir là-dessus ?", "J'aimerais que vous m'écriviez les deux prix aujourd'hui."),
        ("Merci beaucoup encore une fois.", "Doïna Petrescu, propriétaire, rue des Mésanges"),
    ], corrige=True,
       notes="Faire chercher au groupe ce que les quatre versions de droite ont en "
             "commun : un chiffre ou une date. C'est la découverte à ne pas donner "
             "trop vite.")

    d.pratique('Écriture', "Ton courriel, huit à douze phrases",
               "Trois paragraphes. Un objet. Une demande. Une date.", [
        ("premier paragraphe", "de quelle rencontre tu parles, en une ou deux phrases"),
        ("deuxième paragraphe", "les deux solutions, avec leurs prix et leurs délais"),
        ("troisième paragraphe", "ce que tu demandes, avec une date précise"),
        ("un subjonctif", "j'aimerais que vous m'écriviez, il faut que je sache"),
        ("une hypothèse", "si le permis sort dans dix jours, …"),
    ], corrige=True,
       notes="Trente minutes d'écriture. Passer dans les rangées et corriger deux "
             "choses seulement chez chacun : l'objet, et la demande. Le reste se "
             "corrigera à la rétroaction de l'assistant.")

    d.piege('Piège', "écrire un seul bloc de douze phrases",
            "faire trois paragraphes",
            "Un bloc ne se lit pas, il se survole, et c'est toujours la demande qui "
            "se perd au milieu. Une ligne vide entre les paragraphes coûte une "
            "seconde à taper et change la façon dont le message est reçu.",
            notes="Montrer les deux formes côte à côte au tableau, sans lire le "
                  "contenu. La différence se voit à trois mètres.")

    d.billet(
        "Qu'est-ce que tu sais faire maintenant que tu ne savais pas faire il y a quatre semaines ?",
        exemples=[
            "Une phrase.",
            "Puis remplis l'autoévaluation du module.",
        ],
        notes="Fin du module. Faire remplir l'autoévaluation en ligne — seize énoncés "
              "— puis conclure sur la phrase du bloc A : une étape dont il ne reste "
              "rien d'écrit n'a pas eu lieu. C'est ce qui reste quand tout le reste "
              "est oublié.")

    return d.save(dossier)
