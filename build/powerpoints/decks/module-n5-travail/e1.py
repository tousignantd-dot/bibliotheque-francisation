# -*- coding: utf-8 -*-
"""E1 · Entrer dans le bureau, et enregistrer son message
Bloc E « Je me lance » · couleur teal · 75 min. Productions orales.
Source : bloc `appli` — jeu de rôle `conge` et production orale.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n5-travail/images/')


def build(dossier):
    d = Deck(
        code='E1', section='teal',
        titre="Entrer dans le bureau, et enregistrer son message",
        chapeau="Deux productions orales dans la même séance : une demande "
                "de congé menée jusqu'à la confirmation écrite, puis un "
                "message d'accueil de trente secondes, enregistré pour de "
                "vrai.",
        duree='75 minutes')

    d.titre(notes="Avant-dernière séance. Rendre les billets de D2 et en lire deux à voix "
                  "haute, sans nommer les auteurs. Le groupe dit lequel il aurait aimé "
                  "recevoir, et pourquoi. C'est la meilleure entrée en matière possible.")

    d.objectifs([
        "demander un congé en donnant les deux dates dès la première phrase ;",
        "proposer soi-même une solution de remplacement ;",
        "poser ses questions à l'intérieur d'une phrase ;",
        "enregistrer un message d'accueil de trente secondes, en six morceaux.",
    ])

    d.declencheur(
        'Préparation', "Vous entrez dans le bureau de votre chef d'équipe. "
                       "Quelle est votre première phrase ?",
        image=IMG + 'formulaire-rempli.jpg',
        pistes=[
            "Commencez-vous par la raison, ou par les dates ?",
            "Combien de dates faut-il donner ?",
            "Qui répond au téléphone pendant votre absence ?",
            "Que demandez-vous avant de sortir du bureau ?",
        ],
        notes="Laisser deux minutes d'écriture avant de discuter. Presque tout le monde "
              "commence par la raison ; presque tout le monde devrait commencer par les "
              "dates. La démonstration est plus forte si elle vient d'eux.")

    d.cartes("Le jeu de rôle", "L'assistant joue Ghislain Marcoux", [
        ("Trois situations au choix",
         "Déplacer une semaine de vacances · une convocation à l'école lundi matin · "
         "quatre jours sans solde en février."),
        ("Il ne facilite rien",
         "Il ne donne aucun renseignement avant qu'on le lui demande, ni le formulaire, "
         "ni le délai, ni ce qui est payé."),
        ("Il veut deux dates et un remplacement",
         "« La semaine prochaine » ne lui suffit pas, et il attend une proposition "
         "pour l'accueil, pas un haussement d'épaules."),
        ("Il n'accorde jamais rien de vive voix",
         "Il renvoie au formulaire et à la paie, et il dit quand la réponse viendra."),
    ], notes="Faire essayer les deux rôles. Jouer le chef d'équipe apprend autant que "
             "jouer l'employé : c'est en refusant une demande vague qu'on comprend ce "
             "qui manque à la sienne.")

    d.tableau('Sept choses à obtenir', "Avant de sortir du bureau",
              ['Ce qu\'on dit', 'Ce qu\'on demande'],
              [["La demande, en une phrase, avec les dates", "Ce qu'il faut remplir"],
               ["La date du retour au travail", "À qui l'envoyer"],
               ["Qui vous remplace, et quand", "Le délai à respecter"],
               ["", "Ce qui est payé, et ce qui ne l'est pas"],
               ["", "Une confirmation écrite"]],
              cle=1,
              notes="La dernière ligne est celle qui distingue une demande réussie d'une "
                    "demande oubliée. Le rappeler avant de lancer le jeu de rôle.")

    d.pratique('Phrases à réemployer', "Ce que vous avez appris cette semaine",
               "Reprenez ces formes pendant le jeu de rôle.", [
        ("Annoncer avec les deux dates",
         "Je voudrais prendre congé du lundi 19 au vendredi 23, et revenir le lundi 26."),
        ("Poser une question poliment",
         "Je voudrais savoir combien de jours il me reste."),
        ("Demander ce qui est payé",
         "J'aimerais savoir si cette journée-là est payée."),
        ("Annoncer la suite au futur",
         "Kevin prendra les appels de l'avant-midi et Amel répondra l'après-midi."),
        ("Rapporter ce qu'on vous a dit",
         "Sylvie dit que le formulaire doit être signé."),
        ("Réclamer la trace écrite",
         "Est-ce que je recevrai une confirmation par courriel ?"),
    ], corrige=True,
       notes="Projeter cette diapositive pendant tout le jeu de rôle : les élèves y "
             "reviennent d'eux-mêmes quand ils cherchent une formulation.")

    d.regle("Le message d'accueil : six morceaux, trente secondes",
            "L'établissement puis vous · l'absence sans la raison · trois "
            "choses demandées · le rappel au futur · la porte de sortie · "
            "la politesse.",
            precision="On l'écrit d'abord, on le lit à voix haute, puis on "
                      "l'enregistre. Un message qui dépasse quarante secondes perd la "
                      "moitié de ceux qui appellent.",
            notes="Rendre les billets de B1 : c'est le brouillon du message. Laisser dix "
                  "minutes de réécriture avant de passer à l'enregistrement.")

    d.pratique('Avant d\'envoyer', "Écoutez-vous comme si vous appeliez",
               "Six questions à se poser avant d'envoyer l'enregistrement.", [
        ("Sait-on quel établissement on a joint ?", "dans les cinq premières secondes"),
        ("Sait-on à qui on parle ?", "votre nom et votre fonction"),
        ("Dit-on pourquoi vous êtes absent ?", "il ne faut pas — vérifiez"),
        ("Demande-t-on trois choses, pas cinq ?", "nom, numéro, raison"),
        ("Le rappel est-il au futur simple ?", "je vous rappellerai"),
        ("Y a-t-il une porte de sortie ?", "pour une urgence, faites le poste…"),
    ], corrige=True,
       notes="Faire enregistrer dans le module, écouter, corriger, réenregistrer, puis "
             "demander la rétroaction de l'assistant. Les élèves rapides peuvent "
             "enregistrer le second message : celui de la semaine d'absence.")

    d.billet(
        "Après votre enregistrement : notez la chose que vous avez corrigée entre la "
        "première et la deuxième prise.",
        exemples=[
            "Un mot de trop, une phrase trop longue, un morceau oublié.",
            "C'est cette chose-là que vous surveillerez la prochaine fois.",
        ],
        notes="Le billet fait porter l'attention sur le geste de se réécouter, qui est "
              "l'apprentissage réel de la séance. Le relire en E2.")

    return d.save(dossier)
