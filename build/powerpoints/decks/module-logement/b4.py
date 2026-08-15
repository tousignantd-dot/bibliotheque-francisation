# -*- coding: utf-8 -*-
"""B4 · Jeu de rôle : la visite.
Bloc B · couleur teal (écoute et réponds) · 75 min.
Source : dialogue `prep`, production orale du défi 1.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B4', section='teal',
        titre='Jeu de rôle : la visite',
        chapeau="Dix minutes, une propriétaire pressée, un logement à évaluer et six "
                "questions à poser. C'est la situation la plus courante du module — et "
                "elle se prépare.",
        duree='75 minutes')

    d.titre(notes="Séance de production orale. Rendre les billets de A3 et B1 : chacun a "
                  "déjà ses questions. Disposer la classe en dyades.")

    d.objectifs([
        "poser six questions pendant une visite de dix minutes ;",
        "expliquer sa situation avant de poser sa question ;",
        "reformuler les réponses pour vérifier ;",
        "conclure la visite sans s'engager tout de suite.",
    ])

    d.regle('La règle des dix minutes',
            "Trois questions sur le logement · deux sur les coûts · une sur la vie quotidienne.",
            precision="Six questions suffisent, et elles couvrent tout ce qui compte. "
                      "Les poser prend quatre minutes ; le reste sert à regarder et à "
                      "reformuler.",
            notes="Écrire la répartition au tableau. C'est le plan du jeu de rôle et il "
                  "tient en une ligne.")

    d.cartes('Le modèle', "Comment se déroule une visite", [
        ("Vous vous présentez",
         "« Bonjour, j'ai répondu à votre annonce. » Et vous dites en une phrase "
         "pourquoi vous cherchez : cela donne un contexte."),
        ("Vous écoutez d'abord",
         "La propriétaire présente le logement. Beaucoup de vos questions y trouveront "
         "leur réponse : ne les posez pas deux fois."),
        ("Vous posez ce qui manque",
         "Avec le contexte devant chaque question : « Je dors le matin. Est-ce qu'on "
         "entend la rue ? »"),
        ("Vous concluez sans vous engager",
         "« Je vous rappelle avant vendredi. » On ne signe jamais sur place, même si le "
         "logement plaît."),
    ], notes="La quatrième carte est un conseil important. Beaucoup de gens signent sous "
             "pression : le dire clairement.")

    d.tableau('Analyse', "Six questions, six réponses possibles",
              ['Votre question', 'Ce que vous notez'],
              [["Le loyer comprend quoi ?", "chauffage, eau chaude, stationnement"],
               ["Quand est-ce libre ?", "la date, et la durée du bail"],
               ["Est-ce qu'on entend la rue ?", "ce qui fait du bruit, et quand"],
               ["Les électroménagers restent-ils ?", "oui ou non, et lesquels"],
               ["Les animaux sont-ils acceptés ?", "lesquels, et sous quelles conditions"],
               ["Qui déneige l'entrée ?", "le propriétaire, ou le locataire"]],
              cle=0, props=[0.42, 0.58],
              notes="Faire copier ces six questions dans le cahier. Elles servent telles "
                    "quelles, sans adaptation.")

    d.pratique('Pratique · 1 de 4', "Préparez vos six questions",
               "Trois sur le logement, deux sur les coûts, une sur le quotidien.", [
        ("Question 1", "sur le logement — pièces, luminosité, état"),
        ("Question 2", "sur le logement — bruit, voisins, orientation"),
        ("Question 3", "sur le logement — ce qui reste, ce qui part"),
        ("Question 4", "sur les coûts — ce qui est inclus"),
        ("Question 5", "sur les coûts — l'électricité de l'hiver dernier"),
        ("Question 6", "sur le quotidien — stationnement, déneigement, animaux, buanderie"),
    ], corrige=False,
       notes="Dix minutes d'écriture. Chacun ajoute une phrase de contexte devant deux de "
             "ses questions.")

    d.pratique('Pratique · 2 de 4', "Jeu de rôle · la visite",
               "À deux. L'un fait visiter, l'autre pose ses questions. Puis on échange.", [
        ("Vous vous présentez", "et vous dites pourquoi vous cherchez"),
        ("La propriétaire présente", "le logement, en trois ou quatre phrases"),
        ("Vous posez vos six questions", "avec le contexte devant deux d'entre elles"),
        ("Vous reformulez", "deux réponses, pour vérifier"),
        ("Vous concluez", "« Je vous rappelle avant vendredi. »"),
    ], corrige=False,
       notes="Vingt minutes par personne. Circuler et vérifier une seule chose : les six "
             "questions sont-elles posées ? C'est le critère.")

    d.piege("Le piège de la signature sur place",
            "Le logement me plaît, je signe tout de suite.",
            "Je vous rappelle avant vendredi.",
            "Une propriétaire peut dire « j'ai d'autres visites cet après-midi ». C'est "
            "souvent vrai, et ce n'est pas une raison de signer sans réfléchir. Un bail "
            "engage pour douze mois : deux jours de réflexion ne sont pas de trop.",
            notes="Point important pour des personnes qui cherchent vite et sous "
                  "pression. Le dire sans dramatiser.")

    d.piege("Le piège de la question oubliée",
            "Vous sortez et vous vous rappelez trois questions.",
            "Vous relisez votre liste avant de partir.",
            "Trente secondes de relecture avant de quitter le logement valent mieux qu'un "
            "appel gêné le lendemain. Sortez votre papier : personne ne trouvera cela "
            "étrange, et la propriétaire y verra quelqu'un de sérieux.",
            notes="Faire ajouter cette étape au jeu de rôle : relire sa liste avant de "
                  "conclure.")

    d.pratique('Pratique · 3 de 4', "Reformulez la réponse",
               "Vérifiez que vous avez bien compris.", [
        ("« Le chauffage et l'eau chaude sont inclus, l'électricité est à votre charge. »",
         "Donc je paie seulement l'électricité, c'est bien ça ?"),
        ("« Le camion arrive vers cinq heures, trois matins par semaine. »",
         "Donc trois matins sur sept, vers cinq heures ?"),
        ("« Les chats sont acceptés, mais pas les chiens. »",
         "Donc je peux avoir un chat, mais pas de chien ?"),
        ("« Le bail dure douze mois à partir du 1er septembre. »",
         "Donc jusqu'au 31 août prochain ?"),
    ], corrige=True,
       notes="La quatrième reformulation fait un calcul. C'est la plus utile : elle "
             "vérifie qu'on a compris la durée réelle.")

    d.pratique('Pratique · 4 de 4', "Notez après la visite",
               "Quatre lignes, dans l'auto ou dans l'autobus.", [
        ("Le loyer et ce qui est inclus", "un chiffre, et une liste"),
        ("Ce qui vous a plu", "une chose précise"),
        ("Ce qui vous inquiète", "une chose précise"),
        ("Ce que vous devez encore vérifier", "une question restée sans réponse"),
    ], corrige=False,
       notes="Après trois visites, on ne se souvient plus de rien. Ces quatre lignes "
             "permettent de comparer — et c'est le sujet du défi 2.")

    d.billet(
        "Après le jeu de rôle : quelle question avez-vous oubliée ?",
        exemples=[
            "Une seule, celle qui vous est revenue après.",
            "Écrivez-la comme vous la poseriez la prochaine fois.",
        ],
        notes="Les questions oubliées disent exactement ce qui manque dans la "
              "préparation. En faire une liste collective au tableau.")

    return d.save(dossier)
