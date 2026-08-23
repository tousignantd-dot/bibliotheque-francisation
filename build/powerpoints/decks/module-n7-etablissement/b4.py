# -*- coding: utf-8 -*-
"""B4 · Le nom caché sous le verbe
Bloc B « Défi 1 · La lettre de motivation » · couleur teal · 90 min.
Source : exercice `t1nom` et sa mini-leçon (nominalisation, substitution).
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B4', section='teal',
        titre='Le nom caché sous le verbe',
        chapeau="La langue administrative nomme les actions au lieu de les "
                "conjuguer. C'est ce qui la rend neutre — et froide. Sous "
                "chaque nom, il y a un verbe, et sous le verbe, quelqu'un.",
        duree='90 minutes')

    d.titre(notes="Séance qui sert deux fois : à écrire la lettre du bloc B, et à lire "
                  "l'avis de décision du bloc D. Le dire au groupe dès le départ.")

    d.objectifs([
        "former le nom d'un verbe avec -tion, -ment, -ance ;",
        "reconnaître le genre d'un nom d'après son suffixe ;",
        "reprendre une idée par un nom sans répéter la phrase ;",
        "retrouver qui agit sous un nom d'action.",
    ], notes="Le quatrième objectif est une compétence de lecture, pas d'écriture. "
             "« Le refus de votre demande » ne dit pas qui a refusé : c'est là qu'on "
             "apprend à le demander.")

    d.declencheur(
        'Observation', "Pourquoi les documents officiels écrivent-ils ainsi ?",
        pistes=[
            "« À la suite de la réception de votre dossier… »",
            "Qui a reçu le dossier ? Quand ?",
            "Pourquoi ne pas écrire « nous avons reçu votre dossier » ?",
            "Qu'est-ce que le nom cache que le verbe montrerait ?",
        ],
        notes="La bonne réponse est simple : le nom permet de ne nommer personne. Ce "
              "n'est ni bien ni mal, mais il faut le savoir pour lire un avis.")

    d.tableau('Analyse', "Trois suffixes, trois genres",
              ['Le suffixe', 'Ce qu\'il donne'],
              [['-tion', "féminin : admission, sélection, inscription"],
               ['-ment', "masculin : classement, désistement, traitement"],
               ['-ance, -ence', "féminin : reconnaissance, exigence"],
               ['-ure', "féminin : candidature, signature"]],
              cle=0,
              note="Le genre suit le suffixe, presque sans exception : c'est une des "
                   "rares règles de genre qui tiennent.",
              notes="Diapositive à photographier. Faire chercher au groupe trois "
                    "autres noms par suffixe, tirés de leur propre métier.")

    d.regle("Le nom sert aussi à reprendre sans répéter",
            "« Le comité a étudié les dossiers. Cette étude a duré trois jours. »",
            precision="Sans le nom, la deuxième phrase recommence la première. Dans "
                      "une lettre de trois paragraphes, c'est ce qui empêche d'écrire "
                      "« ma candidature » huit fois.",
            notes="Diapositive à photographier. C'est la substitution lexicale du "
                  "programme, et elle ne se voit qu'en comparant deux versions du "
                  "même paragraphe : les écrire au tableau.")

    d.pratique('Grammaire', "Trouvez le nom de la même famille",
               "Complétez avec le nom qui correspond au verbe souligné.", [
        ("Le comité a sélectionné vingt-quatre personnes : la ___ a duré trois jours.", "sélection"),
        ("Elle s'est inscrite au cours du mercredi : son ___ date du 8 janvier.", "inscription"),
        ("Elle a été admise l'an dernier : son ___ a été confirmée par courriel.", "admission"),
        ("Une personne s'est désistée : le ___ est confirmé aujourd'hui.", "désistement"),
        ("Le programme exige un préalable : cette ___ figure sur la fiche.", "exigence"),
        ("Le centre reconnaît ce qu'on sait déjà faire : c'est la ___ des acquis.", "reconnaissance"),
    ], corrige=True,
       notes="Faire dire le nom avec son article : c'est là que le genre s'apprend, "
             "pas dans le tableau.")

    d.piege('Piège', "J'ai appliqué et j'attends leur réponse.",
            "J'ai posé ma candidature et j'attends leur réponse.",
            "« Candidater » n'existe pas en français d'ici, et « appliquer » vient de "
            "l'anglais. On pose sa candidature, on soumet un dossier, on dépose une "
            "demande.",
            notes="Reprendre la faute vue en A3 : elle revient à chaque séance du "
                  "bloc, et c'est normal — elle est ancrée.")

    d.cartes('Lecture', "Sous le nom, quelqu'un", [
        ("« le refus de votre demande »",
         "Qui a refusé ? L'avis ne le dit pas. Si la réponse compte, il faut "
         "téléphoner et la demander."),
        ("« à la suite de la réception »",
         "Reçu par qui, et quand ? La date est ailleurs dans la lettre : la chercher."),
        ("« après étude du dossier »",
         "Étudié par le comité de sélection, mais l'avis ne le nomme pas toujours."),
        ("« sous réserve de vérification »",
         "Quelque chose reste à vérifier : demander quoi, et par qui."),
    ], notes="Quatre formules qui reviendront dans l'avis du bloc D. Les faire "
             "recopier : elles préparent D1 sans le dire.")

    d.billet("Récris cette phrase avec un nom : « Le comité a décidé de retenir ma "
             "candidature. »",
             exemples=["La décision du comité m'a été communiquée le 10 avril.",
                       "Ma candidature a fait l'objet d'une décision favorable."],
             notes="Ramasser les billets. Deux versions correctes existent ; les lire "
                   "toutes les deux, elles montrent que la nominalisation est un "
                   "choix, pas une obligation.")

    return d.save(dossier)
