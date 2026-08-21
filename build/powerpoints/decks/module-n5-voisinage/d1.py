# -*- coding: utf-8 -*-
"""D1 · « Quelle bonne nouvelle ! »
Bloc D « Défi 3 · Les nouvelles et les félicitations » · couleur acier · 75 min.
Source : dialogue `t3`, exercices `t3a`, `t3exc` et `t3fel`.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n5-voisinage/vocab/')


def build(dossier):
    d = Deck(
        code='D1', section='acier',
        titre="« Quelle bonne nouvelle ! »",
        chapeau="Quand quelqu'un vous annonce une bonne nouvelle, vous avez "
                "environ trois secondes. Une question posée en premier donne "
                "l'impression d'un interrogatoire ; une exclamation "
                "accompagne la personne.",
        duree='75 minutes')

    d.titre(notes="Ouverture du défi 3. Commencer par annoncer au groupe une fausse bonne "
                  "nouvelle vous concernant et compter ce qui vient en premier : une "
                  "question, ou une félicitation. C'est une démonstration de trente "
                  "secondes, et elle porte.")

    d.objectifs([
        "réagir à une bonne nouvelle avant de poser des questions ;",
        "employer quel, quelle, comme et que dans une exclamation ;",
        "accorder « quel » avec le nom qui suit ;",
        "distinguer une nouvelle qu'on félicite d'une nouvelle qu'on accompagne.",
    ], notes="Le troisième objectif est le seul point vraiment grammatical de la séance, "
             "et il ne s'entend pas : les quatre formes de « quel » se prononcent pareil. "
             "Il se voit dans un courriel, ce qui est justement la production de D2.")

    d.dialogue('Dialogue · 1 de 3', "« J'avais une raison »", [
        ("MARISOL", "Madame Faye ! Je ne vous ai pas vue depuis deux semaines.", True),
        ("NDEYE", "Bonjour madame Vergara. J'étais en congé, figurez-vous.", True),
        ("MARISOL", "En congé ? Vous qui travaillez toujours de nuit ?", True),
        ("NDEYE", "J'ai pris trois jours. J'avais une raison.", True),
    ], consigne="Écoutez d'abord, diapositive masquée.",
       notes="Faire remarquer la conduite de Ndeye : elle annonce qu'elle a une raison "
             "mais ne la donne pas encore. C'est une façon très ordinaire d'inviter "
             "l'autre à demander, et l'élève doit savoir la reconnaître.")

    d.dialogue('Dialogue · 2 de 3', "Sept ans d'attente", [
        ("NDEYE", "J'ai eu ma citoyenneté canadienne. Mercredi dernier.", True),
        ("MARISOL", "Quelle bonne nouvelle ! Félicitations, madame Faye !", True),
        ("NDEYE", "Merci. Ça faisait sept ans que j'attendais ce papier-là.", True),
        ("MARISOL", "Sept ans ! Comme je suis contente pour vous. Comment ça "
                    "s'est passé ?", True),
    ], notes="C'est le modèle de la séance, en quatre répliques : exclamation, "
             "félicitation, remerciement, sentiment, puis seulement la question. Faire "
             "compter l'ordre au tableau. Attention à la sensibilité du sujet : plusieurs "
             "élèves attendent le même papier.")

    d.dialogue('Dialogue · 3 de 3', "La salle, les drapeaux, la chemise blanche", [
        ("NDEYE", "On était deux cents dans une grande salle, au centre-ville. "
                  "Il y avait des drapeaux partout.", True),
        ("MARISOL", "Et vous étiez seule ?", True),
        ("NDEYE", "Non, mon fils était là. Il avait mis sa chemise blanche, "
                  "celle des grandes occasions.", True),
        ("MARISOL", "Que c'est beau. Vous avez pleuré ?", False),
    ], notes="Tout le décor est à l'imparfait, les deux événements au passé composé. Le "
             "faire relever sans encore expliquer : la règle vient en D2, et elle est plus "
             "facile à donner quand on a déjà vu le phénomène.")

    d.regle("La réaction d'abord, la question ensuite",
            "Quelle bonne nouvelle ! Félicitations ! Comme je suis contente "
            "pour vous. Puis : comment ça s'est passé ?",
            precision="Une question posée en premier — « ça a pris combien de "
                      "temps ? » — donne l'impression d'un interrogatoire. Une "
                      "exclamation dit que vous êtes du côté de la personne.",
            notes="Diapositive à photographier. C'est la règle sociale la plus "
                  "transférable du module : elle vaut au travail, à l'école, en famille.")

    d.cartes("Quatre exclamations", "Quand employer laquelle", [
        ("quel, quelle, quels, quelles",
         "Devant un nom : quelle bonne nouvelle, quel beau projet."),
        ("comme",
         "Devant une phrase complète : comme je suis contente pour vous."),
        ("que",
         "Devant une phrase, un ton plus soutenu : que c'est beau."),
        ("les formules toutes faites",
         "Félicitations ! Bravo ! Vous devez être fière. Il faut fêter ça."),
    ], notes="La distinction utile est celle des deux premières cartes : après « comme », "
             "il faut un sujet et un verbe. « Comme bonne nouvelle » n'existe pas.")

    d.pratique('Grammaire', "Quel mot exclamatif ?",
               "Complétez chaque félicitation.", [
        ("___ bonne nouvelle ! Félicitations, madame Faye !", "Quelle"),
        ("___ je suis contente pour vous !", "Comme"),
        ("___ c'est beau, cette photo de la cérémonie.", "Que"),
        ("___ beau projet vous avez là !", "Quel"),
        ("___ belles photos vous avez rapportées !", "Quelles"),
        ("Félicitations ___ votre citoyenneté !", "pour"),
    ], corrige=True,
       notes="Exercice t3exc de l'activité. Le dernier item n'est pas un mot exclamatif : "
             "on félicite « pour » quelque chose. C'est l'erreur écrite la plus fréquente "
             "du défi, et elle se corrige une fois pour toutes.")

    d.declencheur(
        'Jugement', "Toutes les nouvelles ne se félicitent pas. Comment "
                    "reconnaître laquelle est laquelle ?",
        image=IMG + 'felicitations.jpg',
        pistes=[
            "J'ai eu ma citoyenneté mercredi dernier.",
            "Mon mari a perdu son emploi le mois passé.",
            "Je commence un nouvel emploi lundi.",
            "Mon frère est reparti au pays, il ne reviendra pas.",
        ],
        notes="Exercice t3fel de l'activité. Insister sur les cas ambigus : un "
              "déménagement, une retraite, un retour au pays peuvent être une joie ou une "
              "épreuve. On ne devine pas, on demande : « et vous, comment vous le "
              "prenez ? »")

    d.piege("Ramener la nouvelle à soi",
            "Moi, ça m'a pris deux ans seulement.",
            "Quelle bonne nouvelle ! Comme je suis contente pour vous.",
            "Une félicitation vit seule pendant au moins une phrase. Vos nouvelles, vos "
            "questions et vos comparaisons peuvent attendre trente secondes.",
            notes="Les trois façons de gâcher une félicitation : la ramener à soi, "
                  "minimiser (« ce n'est qu'un papier »), enchaîner sur un problème. Les "
                  "nommer toutes les trois, elles se reconnaissent immédiatement.")

    d.billet(
        "Écrivez ce que vous répondriez à une vraie bonne nouvelle d'un voisin.",
        exemples=[
            "Trois phrases : une exclamation, une félicitation, une question ouverte.",
            "La question doit venir en dernier.",
        ],
        notes="Ramasser. Les billets où la question est en premier montrent que le réflexe "
              "n'est pas encore pris : y revenir en D2, brièvement.")

    return d.save(dossier)
