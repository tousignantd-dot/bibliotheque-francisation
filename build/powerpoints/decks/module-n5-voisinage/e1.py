# -*- coding: utf-8 -*-
"""E1 · « Descendre dans l'escalier »
Bloc E « Je me lance » · couleur teal · 75 min.
Source : jeu de rôle `voisinage`, production orale (message sur répondeur).
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='E1', section='teal',
        titre="« Descendre dans l'escalier »",
        chapeau="Deux productions orales. D'abord la conversation avec le "
                "voisin, jouée avec l'assistant : il ne dit rien qu'on ne "
                "lui demande. Ensuite le message laissé sur le répondeur "
                "d'une voisine, enregistré et déposé.",
        duree='75 minutes')

    d.titre(notes="Séance de production. Le jeu de rôle vient en premier parce qu'il sert "
                  "de répétition : c'est là que l'élève découvre qu'un « on verra » ne "
                  "passe pas, et qu'il faut poser les cinq questions de B1 avant de "
                  "répondre.")

    d.objectifs([
        "mener une conversation de voisinage du début à la fin ;",
        "poser les cinq questions avant de donner sa réponse ;",
        "accepter ou refuser clairement, avec une raison en une phrase ;",
        "laisser un message téléphonique complet en quarante-cinq secondes.",
    ], notes="Les quatre objectifs sont ceux de l'évaluation du module. Les projeter au "
             "début et les relire à la fin.")

    d.cartes("Trois situations", "Choisissez la vôtre dans l'activité", [
        ("L'invitation dans l'escalier",
         "Le voisin vous invite à la fête. Il ne dit rien d'autre : demandez tout."),
        ("Le souper du vendredi",
         "Vous travaillez jusqu'à vingt et une heures. Refusez sans fermer la porte."),
        ("Devant les boîtes aux lettres",
         "Votre voisine a obtenu sa citoyenneté. Félicitez avant de questionner."),
        ("Les deux rôles",
         "Essayez aussi celui du voisin qui invite : au niveau 5, on doit savoir mener."),
    ], notes="Insister sur la quatrième carte. Beaucoup d'élèves ne jouent que le rôle de "
             "celui qui répond ; c'est le rôle facile. Celui qui invite doit donner ses "
             "renseignements dans le bon ordre et réclamer une réponse claire.")

    d.tableau('Le jeu de rôle', "Ce que l'assistant fera, et ce qu'il ne fera pas",
              ['Il fait', 'Il ne fait pas'],
              [["Il vous invite, chaleureusement", "Il ne donne pas la date d'avance"],
               ["Il répond à vos questions", "Il ne dit pas quoi apporter tout seul"],
               ["Il redemande une réponse claire", "Il n'accepte pas un « on verra »"],
               ["Il accepte un refus poli", "Il n'insiste pas plus d'une fois"],
               ["Il vouvoie du début à la fin", "Il ne corrige pas votre langue"]],
              cle=1,
              notes="Projeter avant d'ouvrir l'activité. Savoir que l'assistant ne donnera "
                    "rien spontanément change complètement la façon dont les élèves "
                    "abordent la conversation.")

    d.regle("Cinq morceaux dans un message téléphonique",
            "Qui vous êtes et d'où · pourquoi vous appelez · les faits, "
            "lentement · ce que vous attendez · le numéro et le moment.",
            precision="Bonjour madame Faye, c'est Marisol Vergara, votre voisine "
                      "du deuxième. Je vous appelle au sujet de la fête de la "
                      "ruelle. C'est le samedi 7 juin, de midi à quatre heures. "
                      "Rappelez-moi au 514 555-0112, après quatre heures.",
            notes="Diapositive à photographier, et à laisser au tableau pendant "
                  "l'enregistrement. Faire écrire le message avant de l'enregistrer : "
                  "personne n'improvise un bon message de quarante-cinq secondes.")

    d.cartes("Trois étapes de l'enregistrement", "Ce que dit le panneau de l'activité", [
        ("Je m'enregistre",
         "De trente à quarante-cinq secondes, après avoir écrit son texte."),
        ("Je m'écoute et je corrige",
         "Comme si vous étiez la voisine, réveillée à trois heures de l'après-midi."),
        ("J'envoie à mon enseignant",
         "Rien ne part sans un geste de l'élève : la correction reste privée."),
    ], notes="Le deuxième temps est celui qu'on saute. Trois questions à se poser en "
             "s'écoutant : sait-on qui parle ? peut-on noter la date sans faire répéter ? "
             "a-t-on un numéro et une heure ?")

    d.pratique('Autocorrection', "Écoutez-vous, et vérifiez",
               "Six questions à se poser avant d'envoyer.", [
        ("Est-ce que je me nomme dans la première phrase ?", "sinon, on ne vous rappelle pas"),
        ("Est-ce que je dis d'où j'appelle ?", "l'étage, ou le lien de voisinage"),
        ("Est-ce que la date et l'heure sont dites lentement ?", "un répondeur ne répète pas"),
        ("Est-ce que je dis ce qu'il faut apporter ?", "un détail concret par phrase"),
        ("Est-ce que je donne mon numéro à la fin ?", "chiffre par chiffre"),
        ("Est-ce que je dis quand on peut me joindre ?", "sinon on appelle au mauvais moment"),
    ], corrige=True,
       notes="Faire cocher les six points en s'écoutant, avant l'envoi. La rétroaction de "
             "l'assistant reprendra les mêmes critères : l'élève ne doit pas la découvrir "
             "en même temps que sa note.")

    d.piege("Improviser son message en appuyant sur la touche",
            "Euh... bonjour, c'est moi, euh, je voulais vous dire...",
            "Bonsoir madame Faye, c'est Marisol Vergara, du deuxième.",
            "Un message se rate en quatre secondes. Écrivez-le, lisez-le une fois à "
            "voix haute, puis enregistrez : c'est trois minutes de plus et un rappel "
            "de gagné.",
            notes="Faire écrire le message sur papier avant d'ouvrir le micro. Aucune "
                  "exception : les élèves les plus à l'aise à l'oral sont ceux qui ratent "
                  "le plus souvent la première phrase.")

    d.billet(
        "Notez une chose que l'assistant a demandée et que vous n'aviez pas prévue.",
        exemples=[
            "Une seule chose, en une phrase.",
            "Notez aussi ce que vous direz différemment la prochaine fois.",
        ],
        notes="Les billets de cette séance sont les plus utiles du module : ils disent "
              "exactement ce qui manque encore, juste avant la production écrite de E2.")

    return d.save(dossier)
