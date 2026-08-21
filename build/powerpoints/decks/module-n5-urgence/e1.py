# -*- coding: utf-8 -*-
"""E1 · L'appel au 9-1-1 pour de vrai, et les nouvelles au téléphone.
Bloc E « Je me lance » · couleur teal · 75 min. Production orale.
Source : bloc `appli` — jeu de rôle `urgence911` et production orale.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n5-urgence/images/')


def build(dossier):
    d = Deck(
        code='E1', section='teal',
        titre="L'appel pour de vrai, et les nouvelles au téléphone",
        chapeau="Deux productions orales dans la même séance : un appel "
                "d'urgence mené du début à la fin, puis une minute de "
                "nouvelles à quelqu'un qui ne sait encore rien.",
        duree='75 minutes')

    d.titre(notes="Avant-dernière séance. Rendre les billets de D2 et en lire deux à voix "
                  "haute, sans nommer les auteurs. Le groupe dit lequel il aurait aimé "
                  "recevoir, et pourquoi.")

    d.objectifs([
        "mener un appel au 9-1-1 sans perdre le fil ;",
        "donner l'endroit d'abord et répondre court ensuite ;",
        "raconter une nuit en une minute, en quatre temps ;",
        "s'écouter et se corriger avant d'envoyer.",
    ])

    d.declencheur(
        'Écoute', "Une minute pour annoncer à quelqu'un que sa mère est à l'hôpital. "
                  "Par quoi commencez-vous ?",
        image=IMG + 'ambulance.jpg',
        pistes=[
            "Par ce qui est arrivé ?",
            "Par où elle se trouve maintenant ?",
            "Par une phrase qui rassure ?",
            "Que se passe-t-il dans la tête de l'autre pendant vos dix premiers mots ?",
        ],
        notes="La bonne réponse est la troisième, et elle surprend toujours. Tant que la "
              "personne n'est pas rassurée, elle n'écoute rien de ce qui suit.")

    d.regle("Rassurer d'abord, raconter ensuite",
            "« Écoute-moi d'abord : maman va bien. Elle est à l'hôpital, mais elle va bien. »",
            precision="Puis le décor à l'imparfait, les faits au passé composé, ce que le "
                      "personnel a dit, ce qui s'en vient au futur, et enfin le pratique : "
                      "l'étage, les heures de visite, ce qu'il faut apporter.",
            notes="Diapositive à photographier, et à laisser affichée pendant les "
                  "enregistrements.")

    d.cartes("Le jeu de rôle, en trois situations", "L'assistant joue le répartiteur", [
        ("La chute dans l'escalier",
         "Deux heures du matin, votre mère est par terre, consciente, et ne peut pas "
         "se relever."),
        ("La douleur à la poitrine",
         "Votre voisin, soixante ans, refuse l'ambulance parce que « ça coûte cher ». "
         "Troisième étage, sans ascenseur."),
        ("Un inconnu dans la rue",
         "Une personne par terre sur le trottoir, qui ne répond pas. Vous ignorez le "
         "numéro de la rue."),
        ("Ce qu'il faut savoir",
         "Le répartiteur mène l'échange. Il vous coupera si vous racontez, et il ne "
         "vous laissera pas raccrocher."),
    ], notes="Faire essayer les deux rôles à ceux qui vont vite : jouer le répartiteur "
             "oblige à poser les questions dans l'ordre, ce qui apprend à les entendre.")

    d.tableau('Les sept choses à faire pendant l\'appel',
              "La liste que porte le module",
              ['Moment', 'Ce qu\'on dit'],
              [["Ouvrir", "l'endroit exact, avant tout le reste"],
               ["Renseigner", "le numéro d'où l'on appelle, chiffre par chiffre"],
               ["Annoncer", "ce qui se passe, en une seule phrase"],
               ["Répondre", "oui, non, ou « je ne sais pas »"],
               ["Exécuter", "les consignes reçues, et le dire à voix haute"],
               ["Préparer", "déverrouiller, éclairer, faire attendre quelqu'un en bas"],
               ["Rester", "en ligne, jusqu'à ce qu'on vous dise de raccrocher"]],
              cle=0,
              notes="Laisser le tableau affiché pendant le jeu de rôle : c'est la grille "
                    "d'autoévaluation la plus simple qui soit.")

    d.pratique('Production orale', "Donnez des nouvelles, en quatre temps",
               "Une minute. Écoutez-vous ensuite comme si vous étiez au bout du fil.", [
        ("TEMPS 1 · Rassurer.", "« Écoute-moi d'abord : maman va bien. »"),
        ("TEMPS 2 · Le décor et les faits.",
         "« Elle avait de la fièvre depuis deux jours. Cette nuit, elle est tombée. »"),
        ("TEMPS 3 · Ce qu'on vous a dit.",
         "« La docteure dit que la douleur est contrôlée. Elle m'a demandé si… »"),
        ("TEMPS 4 · La suite et le pratique.",
         "« Elle sortira dans trois ou quatre jours. Les visites sont de 11 h à 20 h. »"),
    ], corrige=True,
       notes="Chacun s'enregistre dans le module, s'écoute, corrige, puis envoie. Le "
             "deuxième enregistrement est presque toujours meilleur : exiger qu'on "
             "s'écoute avant d'envoyer.")

    d.piege("Commencer par le drame",
            "« Allô ? Il est arrivé quelque chose de terrible cette nuit… »",
            "« Écoute-moi d'abord : maman va bien. »",
            "La personne au bout du fil n'entendra rien de vos trois phrases suivantes. "
            "Rassurer n'est pas cacher : c'est mettre l'information la plus importante "
            "en premier.",
            notes="Rejouer les deux versions à voix haute si le groupe hésite : la "
                  "différence s'entend en cinq secondes.")

    d.billet(
        "Écoutez votre enregistrement une dernière fois, puis répondez en une phrase.",
        exemples=[
            "La personne est-elle rassurée dans les cinq premières secondes ?",
            "Sait-elle où aller, quand, et quoi apporter ? Si non, refaites-le.",
        ],
        notes="Le contrôle est le même que celui du module. Il rend l'élève capable de se "
              "corriger seul, ce qui est le but de la séance.")

    return d.save(dossier)
