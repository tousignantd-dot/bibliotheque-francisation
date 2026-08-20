# -*- coding: utf-8 -*-
"""A1 · Ma semaine, heure par heure — mise en situation.
Bloc A « Je découvre » · couleur teal · 75 min.
Source du module : dialogue `prep`, exercices `prVocab` et `pr1`, cartes mémoire.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-relations/images/')


def build(dossier):
    d = Deck(
        code='A1', section='teal',
        titre='Ma semaine, heure par heure',
        chapeau="Mariama est arrivée de Guinée il y a quatorze mois. Depuis "
                "l'automne, elle joue au volleyball le jeudi soir. Ce soir-là, "
                "elle arrive en avance — et une conversation commence.",
        duree='75 minutes')

    d.titre(notes="Ouverture du module. Ne pas commencer par une liste de mots : la "
                  "séance part d'une situation. Écrire au tableau : jeudi, 16 h, "
                  "centre communautaire.")

    d.objectifs([
        "dire à quelle heure je me lève, je travaille et je finis ;",
        "nommer les tâches de ma semaine avec le mot juste, pas avec « je fais des choses » ;",
        "poser une question simple à quelqu'un sur son horaire ;",
        "comprendre une conversation informelle entre deux personnes qui se connaissent peu.",
    ], notes="Lire chaque objectif à voix haute. Y revenir au billet de sortie.")

    d.declencheur(
        'Mise en situation', "Et vous, votre semaine ressemble à quoi ?",
        image=IMG + 'reveil.jpg',
        pistes=[
            "À quelle heure vous levez-vous ? Est-ce pareil tous les jours ?",
            "Quel jour faites-vous le ménage ? Et le lavage ?",
            "Qu'est-ce que vous faites le soir, après le souper ?",
            "Avez-vous une activité qui revient chaque semaine ?",
        ],
        notes="Cinq minutes en grand groupe, sans corriger. Noter au tableau les mots que "
              "le groupe utilise — on comparera avec les mots justes à la diapo du "
              "vocabulaire. Beaucoup diront « je fais le lavage » : garder la formule, "
              "elle est juste.")

    d.cartes('La situation', "Ce qu'on sait de Mariama", [
        ("D'où elle vient",
         "De Guinée. Elle est arrivée au Québec il y a quatorze mois, un douze janvier."),
        ("Ce qu'elle fait de ses journées",
         "Elle travaille à la buanderie d'un hôpital. Son quart commence à sept heures, "
         "alors elle se lève à cinq heures et quart."),
        ("Pourquoi le jeudi",
         "C'est le seul soir où elle finit à quatre heures. Les autres jours, elle sort "
         "à six heures et n'arrive jamais à temps."),
        ("Qui est Chantal",
         "Une coéquipière qui joue dans cette ligue depuis six ans. C'est elle qui engage "
         "la conversation."),
    ], notes="Insister sur la troisième carte : l'horaire de travail décide de tout le "
             "reste. C'est vrai pour beaucoup d'élèves du groupe.")

    d.dialogue('Dialogue · 1 de 3', 'Jeudi soir, au vestiaire', [
        ("CHANTAL", "Tu es arrivée avant tout le monde ce soir. D'habitude, tu entres en courant à la dernière minute.", False),
        ("MARIAMA", "Le jeudi, je finis mon quart à quatre heures. Les autres soirs, je sors à six heures et je n'arrive jamais à temps.", True),
        ("CHANTAL", "Tu travailles où, déjà ?", False),
        ("MARIAMA", "À la buanderie de l'hôpital. Je commence à sept heures, alors je me lève à cinq heures et quart.", True),
    ], consigne="Écoutez d'abord l'enregistrement, diapo masquée. Lisez ensuite.",
       notes="Passer l'audio du module (section « Je découvre ») avant d'afficher le texte. "
             "Les deux répliques teintées contiennent tout l'horaire : les faire relire.")

    d.dialogue('Dialogue · 2 de 3', "Le soir, c'est plus dur que le matin", [
        ("CHANTAL", "Cinq heures et quart ! Moi, je me lève à six heures et je trouve déjà ça dur.", False),
        ("MARIAMA", "Le matin, ça va. C'est le soir qui est difficile. Je fais le souper, je fais une brassée, et là il est neuf heures.", True),
        ("CHANTAL", "Et le ménage, tu le fais quand ?", False),
        ("MARIAMA", "Le samedi matin. Je passe l'aspirateur, je sors les ordures, et après je suis libre.", True),
    ], notes="Vocabulaire à expliquer ici : une brassée, passer l'aspirateur (ou la "
             "balayeuse), sortir les ordures. Faire mimer chaque geste — c'est plus rapide "
             "qu'une traduction.")

    d.dialogue('Dialogue · 3 de 3', "Deux façons d'organiser sa semaine", [
        ("CHANTAL", "Nous, on fait ça le dimanche. Mon chum lave le plancher pendant que je m'occupe du lavage.", False),
        ("MARIAMA", "Le dimanche, moi, je cuisine pour la semaine. Je fais un grand chaudron et je congèle.", True),
        ("CHANTAL", "C'est intelligent, ça. Moi, je décide à cinq heures et demie ce qu'on va manger, et c'est toujours la panique.", False),
        ("MARIAMA", "Chez nous, on cuisinait toujours pour beaucoup de monde. J'ai gardé l'habitude.", True),
    ], notes="La dernière réplique annonce le bloc C : « chez nous, on cuisinait » — "
             "l'imparfait du souvenir. Ne pas l'expliquer maintenant, seulement la faire "
             "remarquer.")

    d.vocabulaire('Vocabulaire · 1 de 3', "Le ménage et le lavage", [
        ("une brassée", "Une quantité de linge qu'on lave en une seule fois."),
        ("la balayeuse", "L'appareil qui aspire la poussière. On dit aussi « l'aspirateur »."),
        ("le bac de recyclage", "Le grand bac où on met le papier, le carton et le plastique."),
        ("sortir les ordures", "Mettre les déchets au bord de la rue avant le passage du camion."),
        ("un grand chaudron", "Une grande casserole, pour cuisiner en quantité."),
    ], notes="Faire répéter chaque mot avec son article. « Balayeuse » est le mot québécois "
             "courant ; « aspirateur » se comprend partout. Les deux sont bons.")

    d.vocabulaire('Vocabulaire · 2 de 3', "Le travail et le temps", [
        ("un quart de travail", "Les heures qu'on travaille dans une journée : jour, soir ou nuit."),
        ("un congé", "Une journée où on ne travaille pas."),
        ("l'horaire", "La liste des heures où on doit être quelque part."),
        ("être libre", "N'avoir rien de prévu, pouvoir faire ce qu'on veut."),
        ("à temps", "Ni en retard, ni trop tôt."),
    ], notes="« Quart de travail » est très employé au Québec — un élève qui cherche du "
             "travail l'entendra dès la première entrevue.")

    d.vocabulaire('Vocabulaire · 3 de 3', "Le loisir qui revient", [
        ("un centre communautaire", "Un endroit du quartier où on fait du sport et des activités."),
        ("une coéquipière", "Une personne qui joue dans la même équipe que soi."),
        ("un entraînement", "La séance où on pratique un sport, avant les matchs."),
        ("le covoiturage", "Voyager à plusieurs dans la même voiture."),
        ("un tournoi", "Une compétition où plusieurs équipes jouent l'une contre l'autre."),
    ], notes="Ces cinq mots reviendront à toutes les séances du bloc B. Les laisser au "
             "tableau jusqu'à la fin du module.")

    d.regle("Ce qu'il faut retenir",
            "Pour parler de sa semaine, on donne une heure, un jour et une action précise.",
            precision="« Je travaille » ne dit presque rien. « Je commence à sept heures, "
                      "je finis à quatre heures le jeudi » situe la personne dans le temps "
                      "et permet à l'autre de proposer quelque chose — un covoiturage, "
                      "une activité, une invitation.",
            notes="Faire répéter la phrase par deux élèves différents. C'est la diapo à "
                  "photographier.")

    d.piege('Parler de son horaire',
            "Je travaille beaucoup et je suis souvent fatiguée.",
            "Je commence à sept heures et je finis à quatre heures, sauf le jeudi.",
            "Les deux phrases sont correctes. Mais seule la deuxième permet à l'autre "
            "personne de répondre quelque chose d'utile : « alors tu es libre le jeudi soir ? ». "
            "Donner une heure, c'est ouvrir la conversation.",
            notes="Ne pas présenter la colonne de gauche comme une faute : c'est une phrase "
                  "juste, mais qui ferme l'échange. La nuance compte pour des adultes.")

    d.billet(
        "Écrivez trois phrases sur votre semaine : une heure, un jour, une tâche.",
        exemples=[
            "Exemple : « Je me lève à cinq heures et quart du lundi au vendredi. »",
            "Employez au moins un mot de la diapo du ménage et un mot du travail.",
        ],
        notes="Ramasser les billets. Ils serviront de point de départ à la séance A2 sur "
              "les adverbes de fréquence.")

    return d.save(dossier)
