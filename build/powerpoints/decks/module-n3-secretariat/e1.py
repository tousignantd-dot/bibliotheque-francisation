# -*- coding: utf-8 -*-
"""E1 · Je me lance.
Bloc E « Je me lance » · couleur teal · 75 min.
Source : jeu de rôle `secretariat`, production orale et production écrite du module.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='E1', section='teal',
        titre='Je me lance',
        chapeau="Tout le module tient dans un échange de deux minutes au "
                "comptoir : se nommer, annoncer, dater, expliquer, demander. "
                "Puis l'écrire en cinq phrases.",
        duree='75 minutes')

    d.titre(notes="Séance d'évaluation formative. Prévoir les tablettes ou les portables "
                  "pour le jeu de rôle avec l'assistant, et un casque par élève si "
                  "possible.")

    d.objectifs([
        "tenir un échange court au comptoir du secrétariat ;",
        "couvrir les sept sujets dans l'ordre utile ;",
        "s'enregistrer, s'écouter et se corriger ;",
        "écrire un courriel d'absence au secrétariat.",
    ])

    d.regle("La secrétaire ne devine rien",
            "ce qu'on ne dit pas ne s'inscrit pas",
            precision="Dans le jeu de rôle, l'assistant commence toujours par "
                      "le nom, le prénom et le groupe, et il ne rappelle jamais "
                      "ce qu'on a oublié. Si la date manque, il la demande — "
                      "c'est le renseignement sans lequel il ne peut rien "
                      "écrire.",
            notes="Diapo à photographier. Prévenir le groupe avant de commencer : le jeu "
                  "de rôle vouvoie et reste sobre, comme un vrai comptoir.")

    d.cartes("Les trois situations du jeu de rôle", "À choisir dans le module", [
        ("L'enfant malade",
         "Votre fils de cinq ans a fait de la fièvre toute la nuit et la garderie ne le "
         "prendra pas demain. Vous venez le dire avant."),
        ("Le billet de la clinique",
         "Vous avez manqué trois jours la semaine passée. Vous revenez avec un papier de "
         "la clinique dans votre sac."),
        ("Le travail à temps plein",
         "Vous commencez un emploi le premier du mois prochain. Vous venez le dire et "
         "demander votre attestation."),
    ], cols=3,
       notes="Faire choisir avant de commencer. Un élève qui hésite prend la première : "
             "c'est celle qui reprend le plus de choses du défi 1.")

    d.tableau('Analyse', "Les sept sujets à couvrir",
              ["Dans l'ordre", "Ce qu'on dit"],
              [["1. Saluer", "Bonjour, madame."],
               ["2. Se nommer", "Nawel Belkacem, groupe 12."],
               ["3. Annoncer", "Je vais être absente."],
               ["4. Dater", "Jeudi prochain, le 12 mars, l'avant-midi."]],
              cle=1,
              note="Les trois derniers sujets sont sur la diapositive suivante.",
              notes="Diapo à photographier. Un tableau de sept lignes ne se lit pas de "
                    "loin : c'est pour ça qu'il est coupé en deux.")

    d.tableau('Analyse', "Les sept sujets à couvrir (suite)",
              ["Dans l'ordre", "Ce qu'on dit"],
              [["5. Expliquer", "parce que ma fille a un rendez-vous."],
               ["6. Demander", "Est-ce que je dois apporter un papier ?"],
               ["7. Répéter et remercier", "Jeudi le 12 mars. Merci. Bonne journée."]],
              cle=1,
              note="Sept sujets, deux minutes. Ce n'est pas une conversation : "
                   "c'est une démarche.",
              notes="Faire cocher les sept sujets par un observateur pendant que deux "
                    "élèves jouent la scène devant le groupe.")

    d.pratique('Production orale', "Ce qu'on écoute en vous corrigeant",
               "Quatre choses, et rien d'autre.", [
        ("La formule d'ouverture", "bonjour madame, puis nom, prénom, groupe"),
        ("Le futur proche", "je vais être absente, dit sans hésiter"),
        ("La date", "le jour, la date, le moment de la journée"),
        ("La demande finale", "une question sur le papier, puis merci"),
    ], corrige=False,
       notes="Donner ces quatre critères avant l'enregistrement, pas après. L'élève "
             "s'écoute une première fois seul, puis envoie.")

    d.regle("S'écouter avant d'envoyer",
            "je m'enregistre, je m'écoute, je recommence",
            precision="La première prise sert à entendre ce qui manque — "
                      "presque toujours la date ou le groupe. On peut "
                      "recommencer autant de fois qu'on veut : c'est le seul "
                      "endroit du module où c'est possible.",
            notes="Insister : les élèves envoient volontiers la première prise. La "
                  "deuxième est presque toujours meilleure d'un cran.")

    d.pratique('Production écrite', "Le courriel au secrétariat",
               "Cinq à huit phrases, avec cinq choses obligatoires.", [
        ("La formule d'appel", "Bonjour madame,"),
        ("Qui vous êtes", "votre nom, votre prénom, votre groupe"),
        ("Quand", "le ou les jours, avec la date"),
        ("Pourquoi", "une phrase courte avec parce que"),
        ("La salutation finale", "Merci. Bonne journée."),
    ], corrige=False,
       notes="Rappeler l'écriture des dates : le 12 mars, jamais « mars 12 », et pas de "
             "majuscule aux jours. C'est ce qui se corrige le plus souvent.")

    d.piege("Écrire un courriel trop long",
            "raconter toute l'histoire du rendez-vous",
            "qui, quand, pourquoi, merci",
            "Le secrétariat a besoin de quatre renseignements. Un message de dix lignes "
            "se lit mal et retarde la réponse. Court et complet vaut mieux que long et "
            "vague.",
            notes="Montrer un exemple trop long et un exemple juste, côte à côte au "
                  "tableau. La différence se voit immédiatement.")

    d.billet(
        "Terminez votre courriel et envoyez-le.",
        exemples=[
            "Relisez-le une fois avant d'envoyer.",
            "Vérifiez la date et votre numéro de groupe.",
        ],
        notes="Ce qui n'est pas fini en classe se termine à la maison. Les productions "
              "envoyées apparaissent dans le portail enseignant.")

    return d.save(dossier)
