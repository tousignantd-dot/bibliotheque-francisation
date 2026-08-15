# -*- coding: utf-8 -*-
"""B1 · Les questions de la visite.
Bloc B · couleur acier (compréhension orale) · 60 min.
Source : exercices `pr2` et `pr4` — questions sur le dialogue, et questions à inventer.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B1', section='acier',
        titre='Les questions de la visite',
        chapeau="Ibrahim pose quatre questions en dix minutes, et chacune lui rapporte "
                "une information qu'il n'aurait pas eue autrement. C'est ce qui "
                "distingue une visite d'une promenade.",
        duree='60 minutes')

    d.titre(notes="Ouverture du défi 1. Rendre les billets de A3 : chacun a déjà écrit "
                  "six questions. On va les mettre à l'épreuve.")

    d.objectifs([
        "retrouver l'information donnée en réponse à une question ;",
        "reconstruire la question à partir de la réponse ;",
        "poser une question précise plutôt qu'une question générale ;",
        "expliquer sa situation avant de poser sa question.",
    ])

    d.tableau('Analyse', "Les quatre questions d'Ibrahim",
              ['Sa question', "Ce qu'il obtient"],
              [["Le loyer, il est de combien ?", "890 $, et ce qui est inclus"],
               ["Est-ce qu'on entend la boulangerie ?", "le camion de cinq heures, et la cour"],
               ["Et si je voulais repeindre ?", "la peinture fournie, et les animaux"],
               ["(implicite) Quand est-ce libre ?", "le 1er septembre, bail de douze mois"]],
              cle=0, props=[0.42, 0.58],
              notes="Faire compter les informations obtenues : neuf, pour quatre "
                    "questions. Chaque réponse en contient plus d'une.")

    d.regle('La règle du défi 1',
            "Expliquez votre situation, puis posez votre question.",
            precision="« Je travaille de soir et je dors le matin. Est-ce qu'on entend "
                      "beaucoup la boulangerie ? » La première phrase permet à Ginette "
                      "de répondre précisément — sur le camion, et sur la cour.",
            notes="Diapo centrale du défi. Sans la première phrase, Ginette aurait "
                  "répondu « non, ça va » et Ibrahim n'aurait rien appris.")

    d.pratique('Pratique · 1 de 4', "Six questions sur la visite",
               "Répondez d'après le dialogue.", [
        ("Combien Ibrahim paiera-t-il de loyer ?", "890 $ par mois"),
        ("Qu'est-ce qui est compris dans le loyer ?", "le chauffage et l'eau chaude"),
        ("Où se trouve la buanderie ?", "au sous-sol"),
        ("Pourquoi le bruit du matin l'inquiète-t-il ?",
         "parce qu'il travaille de soir et dort le matin"),
        ("Quel animal la propriétaire accepte-t-elle ?", "le chat ; les chiens sont refusés"),
        ("Jusqu'à quand peut-il réfléchir ?", "il doit rappeler avant vendredi"),
    ], corrige=True,
       notes="Six réponses courtes. Faire répondre cahier fermé : le dialogue est court "
             "et l'information est dense.")

    d.pratique('Pratique · 2 de 4', "Inventez la question",
               "La réponse est donnée. Quelle était la question ?", [
        ("« Oui, elle est comprise dans le loyer. »",
         "Est-ce que l'eau chaude est comprise dans le loyer ?"),
        ("« Non, seulement les chats. »",
         "Est-ce que les chiens sont acceptés dans l'immeuble ?"),
        ("« Au sous-sol, juste à côté du local à vélos. »", "Où se trouve la buanderie ?"),
        ("« À partir du 1er septembre, à midi. »", "À partir de quand puis-je emménager ?"),
    ], corrige=True,
       notes="Exercice inverse et difficile. Faire remarquer que la forme de la réponse "
             "donne le type de question : oui/non, ou mot interrogatif.")

    d.cartes('Analyse', "Quatre façons de mieux poser sa question", [
        ("Expliquez d'abord",
         "« Je travaille de soir. » Une phrase de contexte, et la réponse devient dix "
         "fois plus utile."),
        ("Demandez un chiffre",
         "« Le camion passe combien de fois par semaine ? » plutôt que « c'est "
         "bruyant ? ». Un chiffre ne se discute pas."),
        ("Demandez à voir",
         "« Est-ce que je peux voir la buanderie ? » Ce qu'on voit vaut mieux que ce "
         "qu'on nous dit."),
        ("Reformulez la réponse",
         "« Donc le chauffage est inclus, mais pas l'électricité, c'est bien ça ? » "
         "Trente secondes qui évitent un malentendu de douze mois."),
    ], notes="La quatrième carte est le réflexe du module 4. Le signaler : c'est le même "
             "geste, dans une autre situation.")

    d.piege("Le piège de la question vague",
            "C'est bruyant ?",
            "Le camion de farine passe combien de fois par semaine ?",
            "« C'est bruyant ? » appelle un « non » automatique : personne ne dit que son "
            "logement est bruyant. Une question chiffrée oblige à une réponse "
            "vérifiable — et Ginette répond « trois matins par semaine ».",
            notes="Faire transformer trois questions vagues en questions chiffrées. C'est "
                  "l'exercice le plus utile de la séance.")

    d.pratique('Pratique · 3 de 4', "Rendez la question précise",
               "Demandez un chiffre ou un fait vérifiable.", [
        ("C'est bruyant ?", "Le camion passe combien de fois par semaine ?"),
        ("C'est cher, l'électricité ?", "Combien coûtait l'électricité en janvier dernier ?"),
        ("C'est bien isolé ?", "Quand les fenêtres ont-elles été changées ?"),
        ("C'est proche de tout ?", "L'arrêt d'autobus est à combien de minutes à pied ?"),
    ], corrige=True,
       notes="Faire remarquer que les quatre questions précises appellent une réponse "
             "qu'on peut noter. Les vagues, non.")

    d.pratique('Pratique · 4 de 4', "Ajoutez le contexte",
               "Une phrase d'explication avant chaque question.", [
        ("Est-ce qu'on entend la rue ?",
         "Je dors le jour parce que je travaille de nuit. Est-ce qu'on entend la rue ?"),
        ("Est-ce qu'il y a un ascenseur ?",
         "Ma mère habite avec nous et elle monte mal les escaliers. Y a-t-il un ascenseur ?"),
        ("Les chats sont acceptés ?",
         "J'ai un vieux chat très tranquille. Est-ce que les chats sont acceptés ?"),
        ("La cour est clôturée ?",
         "J'ai deux jeunes enfants. Est-ce que la cour est clôturée ?"),
    ], corrige=True,
       notes="Faire dire les quatre à voix haute, avec le contexte. La différence de ton "
             "est frappante : la question devient une conversation.")

    d.billet(
        "Écrivez trois questions avec leur phrase de contexte.",
        exemples=[
            "Une phrase qui explique votre situation, puis la question.",
            "Vos questions doivent être précises : un chiffre, une date, un fait.",
        ],
        notes="Ces trois questions serviront directement en B4, dans le jeu de rôle de "
              "la visite.")

    return d.save(dossier)
