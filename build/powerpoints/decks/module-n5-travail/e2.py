# -*- coding: utf-8 -*-
"""E2 · Le courriel qui répond à votre place, et le bilan
Bloc E « Je me lance » · couleur framboise · 75 min. Production écrite et bilan.
Source : bloc `appli` — production écrite, section « Je retiens des mots ».
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n5-travail/images/')


def build(dossier):
    d = Deck(
        code='E2', section='framboise',
        titre="Le courriel qui répond à votre place",
        chapeau="Vous partez une semaine et vous ne lirez pas vos "
                "courriels. Cinq lignes, écrites une fois, qui "
                "travailleront à votre place pendant sept jours.",
        duree='75 minutes')

    d.titre(notes="Dernière séance. Commencer en lisant deux réponses automatiques "
                  "réelles, trouvées dans sa propre boîte de courriels — une bonne et une "
                  "mauvaise, anonymisées. Le groupe dit tout de suite laquelle l'aide.")

    d.objectifs([
        "écrire une réponse automatique en cinq lignes ;",
        "donner la date du retour plutôt que la durée de l'absence ;",
        "nommer une personne à joindre, avec de quoi la joindre ;",
        "faire le bilan de ce qu'on sait faire maintenant.",
    ])

    d.declencheur(
        'Observation', "Vous écrivez à quelqu'un et ce message revient. "
                       "Qu'est-ce que vous voulez y trouver ?",
        image=IMG + 'ecran-courriel.jpg',
        pistes=[
            "Combien de temps donnez-vous à ce message avant de passer à autre chose ?",
            "Qu'est-ce qui vous ferait attendre pour rien ?",
            "Qu'est-ce qui vous permettrait d'agir tout de suite ?",
            "Avez-vous besoin de savoir pourquoi la personne est absente ?",
        ],
        notes="La dernière piste règle la question des excuses : une réponse automatique "
              "ne s'excuse pas, elle empêche d'attendre. La raison de l'absence ne "
              "regarde personne, exactement comme dans le message d'accueil.")

    d.cartes("Les cinq lignes", "Aucune n'est facultative", [
        ("1 · La salutation",
         "Bonjour. Une seule ligne, et elle suffit."),
        ("2 · Les dates de l'absence",
         "Je suis absente du 19 au 23 août."),
        ("3 · Que vous ne lirez pas vos courriels",
         "Au futur simple. C'est la ligne qu'on oublie, et elle évite qu'on attende."),
        ("4 · La personne à joindre",
         "Écrivez à Kevin Dorais ou faites le poste dix-neuf — un nom et un moyen."),
        ("5 · La date du retour, et la signature",
         "Je répondrai à mon retour, le lundi 26 août. Dorine Kabeya, accueil."),
    ], notes="Insister sur la ligne 3 : sans elle, la personne suppose que vous lisez vos "
             "courriels le soir, et elle attend. C'est l'ajout qui rend le message utile.")

    d.piege("Donner une durée au lieu d'une date",
            "Je suis absente une semaine.",
            "Je serai de retour le lundi 26 août.",
            "Une semaine à partir de quand ? Le lecteur calcule à partir du jour où il "
            "lit, et il se trompe. Le jour de la semaine, en plus de la date, évite "
            "l'autre erreur : croire que le 26 est un lundi alors que c'est un dimanche.",
            notes="Faire le calcul au tableau avec deux dates réelles. La démonstration "
                  "dure quinze secondes et elle se retient.")

    d.tableau('Trois autres absences', "La même structure, adaptée",
              ['La situation', 'Ce qui change'],
              [["Une journée seulement", "Trois lignes suffisent"],
               ["Sans date de retour connue", "On écrit qu'on ne la connaît pas"],
               ["Un départ définitif", "On dit que les messages ne seront pas transférés"],
               ["Le matin du retour", "On l'éteint avant toute autre chose"]],
              cle=1,
              notes="La troisième ligne est celle qu'on voit rarement et qui manque "
                    "cruellement : quelqu'un qui écrit à une adresse abandonnée doit "
                    "savoir que son message se perd.")

    d.pratique('Avant d\'envoyer', "Six vérifications",
               "Relisez votre courriel et répondez.", [
        ("Y a-t-il une salutation ?", "une ligne, pas trois"),
        ("Les deux dates de l'absence sont-elles écrites ?", "le premier jour et le dernier"),
        ("Dites-vous que vous ne lirez pas vos courriels ?", "au futur simple"),
        ("Donnez-vous un nom et un moyen de le joindre ?", "un poste ou un courriel"),
        ("La date du retour porte-t-elle le jour de la semaine ?", "le lundi 26 août"),
        ("Avez-vous signé avec votre fonction ?", "Dorine Kabeya, accueil"),
    ], corrige=True,
       notes="Faire écrire dans le module, puis demander la correction de l'assistant. "
             "Les élèves rapides écrivent la deuxième version : celle d'une absence sans "
             "date de retour connue.")

    d.vocabulaire('Bilan', "Ce que vous savez faire maintenant", [
        ("Tenir le bon registre", "Vouvoyer au téléphone, tutoyer dans le corridor."),
        ("Enregistrer un message", "Six morceaux, trente secondes, sans dire pourquoi."),
        ("Prendre une note d'appel", "Six lignes, des abréviations partagées, signée et datée."),
        ("Rapporter", "Elle dit que… · elle demande si… · elle demande de…"),
        ("Lire et écrire un mode d'emploi", "Chercher sa page, puis ordonner ses gestes."),
        ("Mener une démarche", "Six étapes, et la confirmation écrite qu'on réclame."),
    ], notes="Faire relire cette liste dans le module, section « Je retiens des mots », et "
             "compléter l'autoévaluation avant de terminer. Les seize énoncés y sont plus "
             "détaillés que ces six-ci.")

    d.billet(
        "En une phrase : qu'est-ce que vous ferez différemment à votre travail ?",
        exemples=[
            "Une seule chose, précise, que vous ferez vraiment.",
            "« Je noterai le numéro pendant que la personne parle », « je demanderai "
            "une confirmation par courriel »…",
        ],
        notes="Dernier billet du module. Les lire à voix haute, sans nommer les auteurs : "
              "c'est la meilleure révision possible en cinq minutes, et c'est aussi ce "
              "qui montre ce que le module a réellement changé.")

    return d.save(dossier)
