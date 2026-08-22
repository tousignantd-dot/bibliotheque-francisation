# -*- coding: utf-8 -*-
"""B2 · L'ordre quand « ensuite » n'est pas là
Bloc B « Défi 1 · On m'explique la démarche » · couleur teal · 75 min.
Source : exercice `t1indices` et sa mini-leçon, exercice `t1ordre`. Savoir du
programme : comprendre l'ordre des étapes d'une consigne à partir d'indices
linguistiques autres que les connecteurs de temps.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B2', section='teal',
        titre="L'ordre quand « ensuite » n'est pas là",
        chapeau="« Remettez votre demande après avoir obtenu votre "
                "attestation. » La demande est écrite en premier ; "
                "l'attestation se fait en premier.",
        duree='75 minutes')

    d.titre(notes="Séance d'écoute et de lecture fine. C'est la difficulté la plus "
                  "coûteuse du bloc : on fait les choses dans l'ordre où on les a "
                  "lues, et une étape saute.")

    d.objectifs([
        "reconnaître les mots qui annoncent une action antérieure ;",
        "reconnaître ceux qui annoncent une suite ;",
        "réécrire une consigne en étapes numérotées ;",
        "poser la question du délai quand il manque.",
    ], notes="Le troisième objectif est le geste à installer : trois lignes "
             "reformulées en 1, 2, 3 valent dix relectures.")

    d.declencheur(
        'Observation', "« Avant de signer, lisez la politique. » Que fait-on en premier ?",
        pistes=[
            "Quelle action est écrite en premier ?",
            "Quelle action se fait en premier ?",
            "Quel petit mot fait toute la différence ?",
        ],
        notes="Laisser le groupe se tromper : la moitié répondra « signer », parce "
              "que c'est le premier verbe lu. C'est le meilleur départ possible.")

    d.tableau('Analyse', "Les mots qui reculent : ce qui suit vient AVANT",
              ['Le mot', 'Un exemple'],
              [["avant de + infinitif", "Avant de rencontrer le comité, remplissez le formulaire."],
               ["après avoir + participe", "Remettez la demande après avoir obtenu l'attestation."],
               ["une fois + participe", "Une fois le formulaire rempli, apportez-le au bureau 12."],
               ["sans + nom", "Sans attestation, la demande n'est pas reçue."]],
              cle=0,
              note="Le test : mettez la phrase au passé et demandez-vous ce qui s'est passé en premier.",
              notes="Diapositive à photographier. Insister sur « après avoir » : c'est "
                    "le plus trompeur des quatre, parce que « après » fait penser à "
                    "une suite alors qu'il annonce une antériorité.")

    d.tableau('Analyse', "Les mots qui avancent : ce qui suit vient APRÈS",
              ['Le mot', 'Un exemple'],
              [["dès que", "Dès que le comité a terminé, la réponse est envoyée."],
               ["tant que", "Tant que l'affichage est là, on peut se présenter."],
               ["alors, par la suite", "Le poste vous sera alors confirmé."],
               ["le futur simple", "Vous ferez trente jours d'essai ; le poste sera confirmé."]],
              cle=0,
              note="« Tant que » dit une durée qui se termine : ce qui arrive à la fin vient après.",
              notes="Diapositive à photographier. « Tant que » est le plus difficile des "
                    "quatre ; y revenir en fin de séance si le temps le permet.")

    d.regle("L'ordre des mots n'est pas l'ordre des choses",
            "Ce qui est écrit en premier n'est pas toujours ce qui se fait en premier.",
            precision="Une consigne écrite met souvent l'action principale en tête et "
                      "sa condition en second. Les mots avant, après avoir, une fois, "
                      "sans, dès que, tant que sont là pour rétablir l'ordre réel. "
                      "Quand aucun « ensuite » n'apparaît, ce sont eux qu'il faut "
                      "chercher.",
            notes="Diapositive à photographier. C'est la règle du bloc, et elle "
                  "resservira au bloc C : une politique est écrite exactement ainsi.")

    d.pratique('Pratique', "Qu'est-ce qui vient en premier ?",
               "Lisez la consigne, puis nommez l'action qui se fait d'abord.", [
        ("Avant de rencontrer le comité, remplissez le formulaire.", "remplir le formulaire"),
        ("Remettez la demande après avoir obtenu l'attestation.", "obtenir l'attestation"),
        ("Une fois le formulaire reçu, votre chef est avisé.", "recevoir le formulaire"),
        ("Sans six mois d'ancienneté, la candidature n'est pas admissible.", "avoir six mois d'ancienneté"),
        ("Dès que le comité a terminé, la réponse est envoyée.", "la fin du comité"),
        ("Le formulaire se remplit après la lecture de la note.", "lire la note"),
    ], corrige=True,
       notes="Faire dire la réponse à voix haute avant de corriger. La quatrième "
             "surprend : « sans » ne ressemble pas à un mot de temps, et c'en est un.")

    d.piege('Piège', "lire « après » comme « ensuite »",
            "regarder s'il y a « avoir » derrière",
            "« Après avoir rempli » veut dire « une fois que c'est rempli » : ça vient "
            "AVANT le reste de la phrase. « Après, remplissez » veut dire le "
            "contraire. Le petit mot « avoir » change tout, et il passe inaperçu à "
            "l'écoute comme à la lecture.",
            notes="L'écrire au tableau côte à côte, les deux phrases, et faire "
                  "entourer « avoir ». C'est le moment de la séance à ne pas presser.")

    d.pratique('Écriture', "Réécrire en étapes numérotées",
               "Transformez chaque consigne en une liste 1, 2, 3.", [
        ("Avant de remettre le RH-04, vérifiez votre ancienneté et joignez votre attestation.",
         "1. vérifier l'ancienneté 2. joindre l'attestation 3. remettre le RH-04"),
        ("Une fois la demande reçue, le chef est avisé et le comité est convoqué.",
         "1. recevoir la demande 2. aviser le chef 3. convoquer le comité"),
        ("Dès que la rencontre est terminée, la réponse est rédigée puis envoyée.",
         "1. terminer la rencontre 2. rédiger la réponse 3. envoyer la réponse"),
        ("Sans réponse écrite, la mutation ne prend pas effet ; le poste reste affiché.",
         "1. envoyer la réponse écrite 2. la mutation prend effet"),
    ], corrige=True,
       notes="Exercice central de la séance. Accepter toute formulation qui met les "
             "actions dans le bon ordre ; ne pas corriger le style ici. C'est "
             "exactement le geste qu'on demandera en E1, à voix haute.")

    d.billet(
        "Écris une consigne de ton travail où l'ordre n'est pas celui des mots.",
        exemples=[
            "Une phrase suffit.",
            "Souligne le mot qui donne l'ordre réel.",
        ],
        notes="Trois minutes. Les exemples rapportés du milieu de travail des élèves "
              "sont meilleurs que ceux du module : les reprendre au tableau en B3.")

    return d.save(dossier)
