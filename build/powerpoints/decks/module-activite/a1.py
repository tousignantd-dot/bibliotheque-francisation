# -*- coding: utf-8 -*-
"""A1 · Au comptoir du centre sportif — mise en situation.
Bloc A « Je découvre » · couleur teal · 75 min.
Source du module : dialogue `prep`, exercices `prVocab` et `pr1`.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-activite/images/')


def build(dossier):
    d = Deck(
        code='A1', section='teal',
        titre='Au comptoir du centre sportif',
        chapeau="Rosa est arrivée de Colombie il y a un an. Son garçon Mateo, "
                "neuf ans, veut apprendre à nager. Elle se présente au comptoir "
                "sans savoir ce qu'il faut demander.",
        duree='75 minutes')

    d.titre(notes="Ouverture du module. Demander d'entrée : « qui a déjà inscrit quelqu'un "
                  "à une activité ici ? ». Souvent une ou deux mains seulement — c'est "
                  "exactement le besoin.")

    d.objectifs([
        "me présenter à un comptoir de service et dire ce que je veux ;",
        "poser les six questions qui font le tour d'une inscription ;",
        "comprendre un tarif, un horaire et une durée ;",
        "répéter les informations avant de partir.",
    ], notes="Le deuxième objectif est le cœur du module : savoir quoi demander vaut mieux "
             "que tout comprendre.")

    d.declencheur(
        'Mise en situation', "Vous êtes ici. Que demandez-vous en premier ?",
        image=IMG + 'comptoir.jpg',
        pistes=[
            "Comment commencez-vous la phrase ?",
            "Quelle est la première information dont vous avez besoin ?",
            "Qu'est-ce qui vous ferait revenir une deuxième fois pour rien ?",
            "Y a-t-il un centre comme celui-là dans votre quartier ?",
        ],
        notes="Cinq minutes. La troisième piste est la bonne : le document oublié et le "
              "matériel obligatoire sont les deux causes de retour. Noter les réponses.")

    d.cartes('La situation', "Ce qu'on sait de Rosa", [
        ("D'où elle vient",
         "De Colombie. Elle habite la ville depuis un an."),
        ("Ce qu'elle veut",
         "Inscrire Mateo, neuf ans, à un cours de natation. Il ne sait pas nager."),
        ("Ce qu'elle ignore",
         "Ce qu'il faut apporter, ce qui sert de preuve d'adresse, et combien ça coûte "
         "vraiment."),
        ("Ce qu'elle fait de bien",
         "Elle répète tout à la fin : « samedi neuf heures, quatre-vingt-cinq dollars, "
         "une preuve d'adresse, et le bonnet ». C'est ce qui lui évite un deuxième "
         "déplacement."),
    ], notes="La quatrième carte est la leçon de la séance, comme dans plusieurs modules. "
             "La répétition entre modules est voulue.")

    d.dialogue('Dialogue · 1 de 3', "Le jour et l'heure", [
        ("ROSA", "Bonjour. Je voudrais inscrire mon garçon à un cours de natation. Il a neuf ans.", True),
        ("LOUISE", "Bonjour. Neuf ans, parfait. On a deux groupes : le samedi matin et le mardi après l'école.", False),
        ("ROSA", "Le samedi matin, ce serait mieux. À quelle heure exactement ?", True),
        ("LOUISE", "De neuf heures à dix heures. Douze semaines, de septembre à décembre.", False),
    ], consigne="Écoutez d'abord l'enregistrement, diapo masquée. Lisez ensuite.",
       notes="La première réplique est la formule complète : « je voudrais » + ce qu'on "
             "veut + l'âge. La faire répéter par le groupe. « Exactement » dans la "
             "troisième réplique est le mot qui obtient une heure précise.")

    d.dialogue('Dialogue · 2 de 3', "Le prix et le papier", [
        ("ROSA", "Et ça coûte combien ?", True),
        ("LOUISE", "Quatre-vingt-cinq dollars pour les résidents. Cent dix pour les autres.", False),
        ("ROSA", "J'habite ici depuis un an. Qu'est-ce que je dois apporter comme preuve ?", True),
        ("LOUISE", "Une facture d'électricité ou un bail à votre nom. N'importe quel document récent avec l'adresse.", False),
    ], notes="Vingt-cinq dollars d'écart entre les deux tarifs : c'est ce qui rend la "
             "preuve de résidence intéressante. Le faire calculer au groupe.")

    d.dialogue('Dialogue · 3 de 3', "Le matériel obligatoire", [
        ("ROSA", "D'accord. Et il faut apporter quoi, pour le cours ?", True),
        ("LOUISE", "Maillot, serviette, et des sandales pour le bord de la piscine. Le bonnet de bain est obligatoire.", False),
        ("ROSA", "Le bonnet est obligatoire. Vous en vendez ici ?", True),
        ("LOUISE", "Oui, cinq dollars au comptoir. Prenez-en un tout de suite, ça évite un retour.", False),
    ], notes="« Obligatoire » est le mot à retenir : sans bonnet, l'enfant ne peut pas "
             "entrer dans l'eau. Faire la différence avec « recommandé ».")

    d.vocabulaire('Vocabulaire · 1 de 2', "S'inscrire", [
        ("une inscription", "L'action de s'enregistrer pour participer à une activité."),
        ("le tarif", "Le prix demandé."),
        ("un résident", "Une personne qui habite la ville ; elle paie moins cher."),
        ("une preuve de résidence", "Un document récent à son nom, avec l'adresse."),
        ("une session", "La période pendant laquelle l'activité a lieu."),
    ], notes="« Résident » est un mot administratif que les élèves rencontreront partout : "
             "bibliothèque, piscine, camp de jour, stationnement.")

    d.vocabulaire('Vocabulaire · 2 de 2', "Ce qu'on apporte", [
        ("un maillot de bain", "Le vêtement pour se baigner."),
        ("un bonnet de bain", "Obligatoire dans plusieurs piscines du Québec."),
        ("une serviette", "Pour se sécher en sortant de l'eau."),
        ("un vestiaire", "La pièce où on se change."),
        ("obligatoire", "Sans cela, on ne peut pas participer. À distinguer de « recommandé »."),
    ], notes="Faire répéter chaque mot avec son article. Le bonnet de bain surprend "
             "beaucoup de gens : c'est une particularité locale qui mérite d'être dite.")

    d.regle("Ce qu'il faut retenir",
            "Répétez les informations avant de partir. Toujours.",
            precision="« Samedi neuf heures, quatre-vingt-cinq dollars, une preuve "
                      "d'adresse, et le bonnet. » Quatre choses, une phrase. C'est ce qui "
                      "distingue une inscription réussie d'un deuxième déplacement.",
            notes="Faire répéter la phrase de la carte blanche par deux élèves. C'est la "
                  "diapo à photographier.")

    d.piege('Repartir sans avoir tout demandé',
            "Merci, je vais y penser.",
            "Alors : samedi neuf heures, quatre-vingt-cinq dollars, une preuve d'adresse, et le bonnet.",
            "Repartir sans avoir vérifié coûte un aller-retour complet — souvent une heure "
            "d'autobus et une journée de congé. Les quatre secondes que prend la "
            "récapitulation sont le meilleur investissement de la conversation.",
            notes="Ne pas présenter la gauche comme impolie : c'est simplement inefficace.")

    d.billet(
        "Notez les six questions que vous poserez la prochaine fois que vous inscrirez quelqu'un.",
        exemples=[
            "Une par ligne : l'horaire, le tarif, la durée, le matériel, les documents, l'inscription.",
            "Écrivez-les comme vous les diriez, pas comme dans un manuel.",
        ],
        notes="Ramasser. Ces questions serviront de banque commune au jeu de rôle de E1.")

    return d.save(dossier)
