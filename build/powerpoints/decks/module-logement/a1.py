# -*- coding: utf-8 -*-
"""A1 · La visite du 4 ½ de la rue Galt — mise en situation.
Bloc A « Je découvre » · couleur teal · 75 min.
Source du module : dialogue `prep`, exercice `pr1`, cartes mémoire.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A1', section='teal',
        titre='La visite de la rue Galt',
        chapeau="Ibrahim déménage à Sherbrooke pour un poste de préposé. Il visite un "
                "4 ½ au-dessus d'une boulangerie. Il travaille de soir et dort le "
                "matin : une seule question compte vraiment.",
        duree='75 minutes')

    d.titre(notes="Ouverture du module 8. Écrire au tableau : QU'EST-CE QUI COMPTE POUR "
                  "MOI ? C'est la question du module, et elle n'a pas la même réponse "
                  "pour deux personnes.")

    d.objectifs([
        "comprendre une visite de logement ;",
        "repérer ce qui est compris dans le loyer et ce qui ne l'est pas ;",
        "comprendre ce que veut dire « 4 ½ » ;",
        "reconnaître les questions qu'un locataire doit poser.",
    ])

    d.declencheur(
        'Mise en situation', "Vous visitez un logement. Qu'est-ce que vous regardez en premier ?",
        pistes=[
            "Quelles trois choses comptent le plus pour vous ?",
            "Qu'est-ce que vous demandez au propriétaire ?",
            "Qu'est-ce qu'on ne voit pas pendant une visite de dix minutes ?",
            "Est-ce que vous décideriez sur place ?",
        ],
        notes="Cinq minutes en grand groupe. Les réponses varient énormément selon la "
              "situation de chacun : c'est exactement le sujet du défi 3.")

    d.regle("Ce que veut dire « 4 ½ »",
            "Le chiffre compte les pièces fermées. Le demi, c'est la salle de bain.",
            precision="Deux chambres, un salon, une cuisine : quatre pièces. Plus la "
                      "salle de bain, qui ne compte que pour une demie. Un 3 ½ a donc "
                      "une chambre, un 5 ½ en a trois.",
            notes="Notation propre au Québec, absente de toutes les méthodes. Faire "
                  "calculer trois exemples au tableau : 2 ½, 3 ½, 5 ½.")

    d.cartes('La situation', "Ce qu'on sait d'Ibrahim", [
        ("Pourquoi il déménage",
         "Il commence un poste de préposé au centre hospitalier le mois prochain. Il "
         "cherche donc assez vite."),
        ("Ce qui compte le plus pour lui",
         "Il travaille de soir et dort le matin. Le bruit du matin est sa vraie "
         "question, avant même le prix."),
        ("Ce qu'on lui montre",
         "Un 4 ½ au deuxième étage, au-dessus d'une boulangerie de la rue Galt. Libre "
         "le 1er septembre."),
        ("Qui lui fait visiter",
         "Ginette, la propriétaire. Elle répond franchement, y compris sur ce qui "
         "dérange."),
    ], notes="La deuxième carte est la clé du module : ce qui compte dépend de la vie "
             "qu'on mène, pas d'une liste générale.")

    d.dialogue('Dialogue · 1 de 4', "J'ai répondu à votre annonce", [
        ("IBRAHIM", "Bonjour madame Ginette. J'ai répondu à votre annonce pour le 4 ½ "
                    "au-dessus de la boulangerie. Je commence un poste de préposé au "
                    "centre hospitalier le mois prochain, alors je cherche assez vite.",
         True),
        ("GINETTE", "Entrez, entrez. Le logement est au deuxième étage. Il se libère le "
                    "1er septembre et le bail dure douze mois.", True),
    ], consigne="Écoutez d'abord l'enregistrement, diapo masquée. Lisez ensuite.",
       notes="Passer l'audio de « Je découvre ». Faire remarquer qu'Ibrahim dit tout de "
             "suite pourquoi il cherche : cela donne un contexte à la propriétaire.")

    d.dialogue('Dialogue · 2 de 4', "Le loyer, il est de combien ?", [
        ("IBRAHIM", "Et le loyer, il est de combien exactement ?", True),
        ("GINETTE", "Huit cent quatre-vingt-dix dollars par mois. Le chauffage et l'eau "
                    "chaude sont inclus ; l'électricité est à votre charge. La "
                    "buanderie est au sous-sol et vous avez une place de stationnement "
                    "dans la ruelle.", True),
    ], notes="Quatre informations en une réplique : le prix, ce qui est inclus, ce qui "
             "ne l'est pas, et deux services. Les faire compter.")

    d.dialogue('Dialogue · 3 de 4', "Est-ce qu'on entend la boulangerie ?", [
        ("IBRAHIM", "Je travaille de soir et je dors le matin. Est-ce qu'on entend "
                    "beaucoup la boulangerie d'en bas ?", True),
        ("GINETTE", "Je ne vous cacherai rien : le camion de farine arrive vers cinq "
                    "heures, trois matins par semaine. Par contre, la chambre donne sur "
                    "la cour, jamais sur la rue.", True),
    ], notes="Ibrahim explique sa situation AVANT de poser sa question. C'est ce qui "
             "permet à Ginette de répondre précisément. Le souligner.")

    d.dialogue('Dialogue · 4 de 4', "Et si je voulais repeindre ?", [
        ("IBRAHIM", "D'accord. Et si je voulais repeindre le salon ?", True),
        ("GINETTE", "Aucun problème, je fournis la peinture. Les chats sont acceptés, "
                    "mais pas les chiens. Prenez le temps de réfléchir et rappelez-moi "
                    "avant vendredi.", True),
    ], notes="Faire remarquer les trois informations données sans être demandées : la "
             "peinture, les animaux, le délai. Une bonne propriétaire anticipe.")

    d.tableau('Analyse', "Ce qui est inclus et ce qui ne l'est pas",
              ['Compris dans le loyer', 'À la charge du locataire'],
              [["le chauffage", "l'électricité"],
               ["l'eau chaude", "l'assurance habitation"],
               ["la buanderie commune", "la laveuse et la sécheuse (à pièces)"],
               ["une place de stationnement", "le déneigement de sa place, parfois"]],
              cle=0,
              note="Un loyer de 890 $ avec le chauffage inclus n'est pas comparable à un "
                   "loyer de 850 $ sans chauffage.",
              notes="Insister sur la note : c'est le calcul que personne ne fait, et "
                    "c'est celui qui compte pour choisir.")

    d.vocabulaire('Vocabulaire · 1 de 2', "Le contrat et les gens", [
        ("un bail", "Le contrat de location signé entre le locataire et le propriétaire."),
        ("le loyer", "La somme versée chaque mois pour habiter un logement."),
        ("un locataire", "La personne qui loue un logement et qui y habite."),
        ("un propriétaire", "La personne à qui appartient le logement loué."),
        ("l'état des lieux", "La description du logement au début du bail."),
        ("emménager", "S'installer dans un nouveau logement."),
    ], notes="« Bail » et « loyer » sont les deux mots du module. Faire vérifier la "
             "prononciation : « bail » rime avec « travail ».")

    d.vocabulaire('Vocabulaire · 2 de 2', "Le logement lui-même", [
        ("chauffé et éclairé", "Dont le chauffage et l'électricité sont compris."),
        ("insonorisé", "Protégé contre le bruit de la rue ou des voisins."),
        ("lumineux", "Qui reçoit beaucoup de lumière du jour."),
        ("la buanderie", "Le local où se trouvent la laveuse et la sécheuse."),
        ("les électroménagers", "Les gros appareils : réfrigérateur, cuisinière, laveuse."),
        ("un quartier", "Une partie d'une ville, avec ses commerces et ses services."),
    ], notes="« Chauffé et éclairé » est une expression figée des annonces. Elle se "
             "retient en bloc.")

    d.pratique('Pratique', "Vrai ou faux",
               "Répondez sans relire le dialogue.", [
        ("Ibrahim pourra emménager le 1er septembre.", "VRAI"),
        ("Le chauffage est aux frais du locataire.", "FAUX — il est inclus"),
        ("Ibrahim devra acheter la peinture s'il repeint.", "FAUX — Ginette la fournit"),
        ("La chambre donne sur la rue Galt.", "FAUX — sur la cour"),
        ("Un camion vient livrer de la farine très tôt le matin.", "VRAI"),
        ("Le logement se trouve au premier étage.", "FAUX — au deuxième"),
        ("Ibrahim pourrait adopter un chien.", "FAUX — chats seulement"),
    ], corrige=True,
       notes="Cinq énoncés faux sur sept : c'est voulu. Faire chercher, pour chacun, la "
             "phrase exacte qui le contredit.")

    d.piege("Le piège de la visite sans question",
            "Vous visitez, vous regardez, vous partez.",
            "Vous expliquez votre situation, puis vous posez vos questions.",
            "Une visite dure dix minutes. Ce qu'on ne demande pas, on ne le saura pas — "
            "et on le découvrira après avoir signé. Ibrahim explique qu'il dort le "
            "matin, et c'est ce qui lui vaut une réponse précise sur le bruit.",
            notes="Préparer la séance A3, où l'on établira la liste complète des choses "
                  "à vérifier.")

    d.billet(
        "Nommez les trois choses qui comptent le plus pour vous dans un logement.",
        exemples=[
            "Trois seulement, par ordre d'importance.",
            "Expliquez la première en une phrase : pourquoi celle-là ?",
        ],
        notes="Ramasser. Ces trois priorités serviront en C3 et en E1 : chacun choisira "
              "un logement selon ses propres critères, pas selon une liste générale.")

    return d.save(dossier)
