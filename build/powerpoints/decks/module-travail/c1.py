# -*- coding: utf-8 -*-
"""C1 · Le message de Sofian.
Bloc C · couleur acier (compréhension orale) · 60 min.
Source : exercice `t2chloe` — un élève prévient son enseignante d'un retard.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C1', section='acier',
        titre='Le message de Sofian',
        chapeau="Sofian sera en retard : sa fille a un rendez-vous chez le dentiste. Mais "
                "il y a une évaluation orale cet après-midi. Son message règle les deux "
                "problèmes à la fois.",
        duree='60 minutes')

    d.titre(notes="Ouverture du défi 2. Rappeler la différence entre retard et absence, "
                  "vue en A3. Sofian est en retard, pas absent : ça change tout ce qu'il "
                  "dit.")

    d.objectifs([
        "distinguer un retard d'une absence dans un message ;",
        "repérer ce que la personne propose pour compenser ;",
        "comprendre une preuve annoncée : billet, formulaire, attestation ;",
        "reconnaître un message qui règle un problème plutôt que d'en poser un.",
    ])

    d.cartes('Avant d\'écouter', "Ce que Sofian doit régler", [
        ("Le retard",
         "Sa fille a un rendez-vous chez le dentiste ce matin. Il arrivera après le "
         "début du cours."),
        ("La preuve",
         "Il annonce qu'il apportera un billet du dentiste. Personne ne le lui a "
         "demandé — il le propose."),
        ("L'évaluation",
         "Une évaluation orale est prévue cet après-midi. Il ne veut pas la manquer et "
         "il le dit."),
        ("La préparation",
         "Il dit comment il se préparera : relire ses notes pendant la pause du midi. "
         "C'est la phrase qui rassure l'enseignante."),
    ], notes="Faire remarquer que Sofian anticipe trois questions avant qu'on les lui "
             "pose. C'est ce qui distingue son message.")

    d.pratique('Pratique · 1 de 4', "Le message de Sofian",
               "Écoutez deux fois, puis répondez.", [
        ("Sofian est-il en retard ou absent ? Pour quelle raison ?",
         "en retard — sa fille a un rendez-vous chez le dentiste"),
        ("Qu'est-ce qu'il va apporter à son enseignante ?", "un billet du dentiste"),
        ("Quand a lieu l'évaluation orale ?", "cet après-midi"),
        ("Comment va-t-il se préparer ?", "il va relire ses notes pendant la pause du midi"),
        ("Quand sera-t-il de retour en classe ?", "tout de suite après son rendez-vous"),
    ], corrige=True,
       notes="La première question est double : le type et la raison. Beaucoup ne "
             "répondront qu'à la moitié.")

    d.regle('La règle du défi 2',
            "On annonce le problème et la solution dans le même message.",
            precision="Sofian ne dit pas seulement « je serai en retard ». Il dit "
                      "pourquoi, ce qu'il apportera comme preuve, et comment il se "
                      "préparera quand même à l'évaluation. Trois réponses avant trois "
                      "questions.",
            notes="Diapo centrale de la séance. Écrire au tableau : PROBLÈME + SOLUTION, "
                  "et l'y laisser jusqu'à C4.")

    d.tableau('Analyse', "Ce que Sofian anticipe",
              ['La question qu\'on lui poserait', 'Ce qu\'il dit d\'avance'],
              [["Pourquoi ?", "un rendez-vous chez le dentiste pour sa fille"],
               ["Avez-vous une preuve ?", "j'apporterai un billet du dentiste"],
               ["Et l'évaluation ?", "je serai là cet après-midi"],
               ["Serez-vous prêt ?", "je relirai mes notes pendant la pause"]],
              cle=0,
              props=[0.42, 0.58],
              note="Quatre questions évitées, vingt secondes de plus.",
              notes="Faire chercher au groupe quelles autres questions un enseignant "
                    "pourrait poser. Il y en a peu : Sofian les a presque toutes prises.")

    d.cartes('Analyse', "Les preuves qu'on peut apporter", [
        ("Un billet médical",
         "Du médecin, du dentiste ou de l'hôpital. Il confirme la date et l'heure de la "
         "consultation, sans dire pourquoi."),
        ("Une attestation de présence",
         "D'un organisme, d'un bureau gouvernemental, d'une école. Elle prouve où vous "
         "étiez."),
        ("Un document officiel",
         "Une convocation, un avis de rendez-vous, une lettre. Une photo du document "
         "suffit souvent."),
        ("Demander avant de partir",
         "Le billet se demande sur place, pas trois jours après. À la réception, avant "
         "de sortir : « Pourriez-vous me donner une preuve de présence ? »"),
    ], notes="La quatrième carte est le conseil pratique de la séance. Beaucoup d'élèves "
             "ne savent pas qu'on peut demander une attestation.")

    d.pratique('Pratique · 2 de 4', "Retard ou absence ?",
               "Et quelle preuve apporter ?", [
        ("Rendez-vous chez le dentiste à 8 h, cours à 9 h.",
         "un retard — billet du dentiste"),
        ("Rendez-vous à l'hôpital toute la journée.",
         "une absence — attestation de l'hôpital"),
        ("Autobus manqué, prochain dans vingt minutes.",
         "un retard — aucune preuve possible, mais on prévient"),
        ("Convocation à un bureau gouvernemental à 10 h.",
         "une absence ou un retard — la convocation elle-même"),
    ], corrige=True,
       notes="Le troisième item est important : il n'y a pas toujours de preuve. Cela "
             "n'empêche pas de prévenir — c'est même là que prévenir compte le plus.")

    d.piege("Le piège du problème sans solution",
            "Bonjour, je serai en retard ce matin. Merci.",
            "Bonjour, je serai en retard ce matin, j'arriverai vers dix heures. J'apporterai un billet.",
            "Un message qui annonce seulement un problème laisse toutes les questions "
            "ouvertes : jusqu'à quand ? avec quelle preuve ? et l'évaluation ? Ajouter "
            "deux phrases transforme une mauvaise nouvelle en information utile.",
            notes="Faire compléter le message court par le groupe, phrase par phrase, "
                  "jusqu'à obtenir un message complet.")

    d.pratique('Pratique · 3 de 4', "Ajoutez la solution",
               "Le problème est donné. Ajoutez ce que vous proposez.", [
        ("Je serai en retard ce matin.", "J'arriverai vers dix heures et j'apporterai un billet."),
        ("Je serai absent demain.", "Je vais demander les notes du cours à un collègue."),
        ("Je vais manquer l'évaluation de mardi.",
         "Est-ce que je pourrais la reprendre jeudi ?"),
        ("Je dois partir plus tôt aujourd'hui.",
         "Je peux reprendre les heures vendredi après-midi."),
    ], corrige=True,
       notes="Accepter toute solution raisonnable. Ce qui compte est qu'il y en ait une, "
             "et qu'elle soit concrète.")

    d.pratique('Pratique · 4 de 4', "Écrivez le message complet",
               "Problème, raison, heure d'arrivée, preuve, solution.", [
        ("La situation",
         "Vous accompagnez votre enfant chez le dentiste à 8 h 30. Le cours commence à "
         "9 h."),
        ("Ce que vous annoncez", "l'heure approximative de votre arrivée"),
        ("Ce que vous proposez", "une preuve, et comment vous rattraperez le cours manqué"),
    ], corrige=False,
       notes="Quinze minutes. Ramasser les messages : ils seront comparés à ceux de C4, "
             "produits à l'oral.")

    d.billet(
        "Écrivez un message qui annonce un problème et propose une solution.",
        exemples=[
            "Une phrase pour le problème, une pour la raison, une pour la solution.",
            "La solution doit être concrète : une heure, une preuve, une proposition.",
        ],
        notes="Relever les billets où la solution manque. C'est ce qui manque le plus "
              "souvent, et c'est le sujet du défi 2.")

    return d.save(dossier)
