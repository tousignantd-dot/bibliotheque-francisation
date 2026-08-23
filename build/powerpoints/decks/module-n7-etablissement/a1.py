# -*- coding: utf-8 -*-
"""A1 · Le dîner de midi et quart
Bloc A « Je découvre » · couleur acier · 75 min. Séance d'ouverture.
Source : dialogue `prep`, exercice `prVF` et son bandeau de quatre mots.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A1', section='acier',
        titre='Le dîner de midi et quart',
        chapeau="Rania veut le diplôme. Elle croyait remplir un formulaire et "
                "attendre une lettre. Sa collègue lui apprend en trois "
                "minutes qu'il y a plus de candidats que de places.",
        duree='75 minutes')

    d.titre(notes="Première séance du module. Ouvrir par une question au groupe : qui "
                  "a déjà voulu s'inscrire quelque part et s'est fait dire qu'il "
                  "manquait un papier ? La plupart. C'est le sujet du bloc, et il ne "
                  "s'agit de faire la leçon à personne.")

    d.objectifs([
        "comprendre ce qu'un programme contingenté demande de plus ;",
        "nommer les trois pièces d'un dossier de candidature ;",
        "distinguer une inscription d'une candidature ;",
        "employer quatre mots de l'admission avec leur article.",
    ], notes="Le troisième objectif est celui qui surprend : beaucoup d'élèves croient "
             "que s'inscrire à un programme est un geste administratif. Le poser dès "
             "la première séance.")

    d.declencheur(
        'Observation', "Qu'est-ce qui décide qui entre dans une formation ?",
        pistes=[
            "Les notes ? L'ordre d'arrivée ? Autre chose ?",
            "Avez-vous déjà passé une entrevue pour étudier ?",
            "Qu'est-ce qu'un établissement peut demander de plus ?",
            "Que se passe-t-il quand il y a trop de demandes ?",
        ],
        notes="Question sans mauvaise réponse. Beaucoup répondront « les notes » : "
              "laisser dire, le dialogue corrigera. Noter au tableau les réponses, on "
              "y revient à la fin de la séance.")

    d.dialogue('Dialogue · 1 de 3', "Je veux le faire", [
        ("RANIA", "Ghyslaine, tu as deux minutes ? Je voudrais te demander quelque chose.", True),
        ("GHYSLAINE", "Assis-toi. J'ai jusqu'à moins vingt. Qu'est-ce qui se passe ?", True),
        ("RANIA", "C'est pour le diplôme. Santé, assistance et soins infirmiers. Je veux le faire.", True),
        ("GHYSLAINE", "Ah oui ? Ça fait combien de temps que tu es préposée, toi, cinq ans ?", True),
    ], consigne="Écouter d'abord, diapositive masquée.",
       notes="Écrire au tableau les trois nombres du module et les y laisser toute la "
             "séance : 5 ans, 68 demandes, 24 places. Ils reviennent dans les quatre "
             "blocs.")

    d.dialogue('Dialogue · 2 de 3', "Il y a une entrevue", [
        ("RANIA", "Je pensais que je remplissais un formulaire et que j'attendais une lettre.", True),
        ("RANIA", "Mais j'ai appelé, et la dame m'a dit qu'il y avait une entrevue.", True),
        ("GHYSLAINE", "Une entrevue de sélection. Oui. Le programme est contingenté.", True),
        ("RANIA", "Contingenté, ça veut dire quoi exactement ?", True),
    ], notes="Faire répéter la question de Rania par deux élèves. Demander un mot "
             "n'est pas un aveu de faiblesse : c'est le geste que tout le module "
             "enseigne, et il commence ici.")

    d.dialogue('Dialogue · 3 de 3', "Soixante-dix pour vingt-quatre", [
        ("GHYSLAINE", "Il y a plus de monde qui demande que de places. Soixante-dix demandes pour vingt-quatre places.", True),
        ("RANIA", "Donc ils en refusent deux sur trois.", True),
        ("GHYSLAINE", "Et ce n'est pas juste les notes qui décident. Il y a le dossier, la lettre, puis la rencontre.", True),
        ("RANIA", "La lettre ? Quelle lettre ?", True),
    ], notes="C'est la réplique qui ouvre le bloc B. La laisser en suspens : la lettre "
             "de motivation est le défi 1, et personne ne l'a encore vue.")

    d.tableau('Analyse', "Les trois pièces qui décident",
              ['La pièce', 'Ce qu\'elle apporte au comité'],
              [['le dossier', "les papiers : relevés, attestations, préalables"],
               ['la lettre', "la seule page que la personne écrit elle-même"],
               ["l'entrevue", "ce qu'aucun papier ne montre"],
               ['le préalable', "une case à remplir, jamais négociable"],
               ['le contingent', "le nombre de places, qui décide du reste"]],
              cle=0,
              notes="Diapositive à photographier. C'est le tableau de référence du "
                    "bloc A, et il revient en A4 sur la fiche du programme.")

    d.regle("Contingenté veut dire classé, pas difficile",
            "Un programme contingenté compare les dossiers entre eux, jamais à une "
            "note de passage.",
            precision="On n'est pas refusé parce qu'on est mauvais : on est refusé "
                      "parce qu'on est cinquième pour quatre places. C'est une nuance "
                      "de mot, et c'est celle qui décide si une personne recommence "
                      "l'année suivante ou si elle abandonne.",
            notes="Diapositive à photographier. Insister : dans ce module, personne "
                  "n'échoue. Une candidate excellente reste sur une liste d'attente, "
                  "et c'est un fait d'arithmétique, pas de valeur.")

    d.vocabulaire('Vocabulaire', "Quatre mots de l'admission", [
        ("un préalable", "Le cours ou le niveau qu'il faut avoir réussi avant d'être admis."),
        ("un programme contingenté", "Une formation où il y a plus de demandes que de places offertes."),
        ("une entrevue de sélection", "La rencontre où l'établissement décide qui il retient."),
        ("un relevé de notes", "Le document officiel qui montre les cours suivis et les résultats."),
    ], notes="Faire répéter chaque mot avec son article. « Un préalable » est masculin "
             "et se dit souvent au pluriel dans les documents : le faire remarquer.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après la conversation de Rania et de Ghyslaine.", [
        ("Rania est préposée aux bénéficiaires depuis cinq ans.", "vrai"),
        ("Elle a terminé ses études en soins infirmiers en Syrie.", "faux - deux ans faits, aucun diplôme"),
        ("Elle pensait qu'il suffisait de remplir un formulaire.", "vrai"),
        ("Le programme accepte tout le monde.", "faux - vingt-quatre places pour soixante-huit demandes"),
        ("Selon Ghyslaine, la plupart des lettres se ressemblent.", "vrai"),
        ("Le relevé de notes de Rania est en français.", "faux - en arabe, avec une traduction"),
    ], corrige=True,
       notes="Faire justifier chaque « faux » par la réplique exacte. Le deuxième "
             "compte : une formation interrompue n'est pas un échec, et il faut que "
             "le groupe l'entende dès la première séance.")

    d.billet("Écris en deux phrases ce qu'un programme contingenté demande de plus "
             "qu'une simple inscription.",
             exemples=["Il demande une lettre de motivation.",
                       "Il demande une entrevue devant un comité."],
             notes="Ramasser les billets. Ils disent en une minute qui a saisi la "
                   "différence entre s'inscrire et poser sa candidature, et c'est elle "
                   "qui porte tout le bloc B.")

    return d.save(dossier)
