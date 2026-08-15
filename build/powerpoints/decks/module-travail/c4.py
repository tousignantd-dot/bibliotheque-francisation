# -*- coding: utf-8 -*-
"""C4 · Expliquer un retard à voix haute.
Bloc C · couleur teal (écoute et réponds) · 75 min.
Source : exercice `t2jeu` — quatre situations à expliquer à la secrétaire.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C4', section='teal',
        titre='Expliquer un retard à voix haute',
        chapeau="Cette fois, quelqu'un répond au bout du fil. On ne peut plus lire son "
                "papier : il faut expliquer, répondre aux questions, et proposer une "
                "solution en direct.",
        duree='75 minutes')

    d.titre(notes="Séance de production orale en interaction. Disposer la classe en "
                  "dyades dès le début. Rendre les messages écrits de C1 : ils servent "
                  "de point de départ.")

    d.objectifs([
        "expliquer une raison en une phrase, à voix haute ;",
        "répondre aux questions de la personne au bout du fil ;",
        "proposer une solution sans qu'on la demande ;",
        "garder un ton calme même quand la situation est urgente.",
    ])

    d.regle('La phrase de dix secondes',
            "Qui je suis · ce qui arrive · à quelle heure j'arrive.",
            precision="Trois informations, dites d'un seul trait. Tout le reste est "
                      "répondu ensuite, aux questions. Commencer par se nommer évite la "
                      "question « à qui est-ce que je parle ? »",
            notes="Écrire les trois au tableau. Chronométrer un exemple : dix secondes, "
                  "c'est court, et c'est suffisant.")

    d.cartes('Analyse', "Quatre raisons, quatre formulations", [
        ("Une migraine",
         "« Bonjour, ici Karim Haddad. J'ai une forte migraine aujourd'hui, je ne "
         "pourrai pas venir au cours. » Une absence, dite simplement."),
        ("Un déménagement",
         "« Ma famille et moi déménageons loin d'ici. Je dois malheureusement abandonner "
         "le cours. » Un abandon : le mot juste, et le regret dit une fois."),
        ("Une panne de voiture",
         "« Ma voiture est tombée en panne, j'attends la dépanneuse. Je serai en retard "
         "ce matin. » La cause, puis la conséquence."),
        ("Un réveil qui n'a pas sonné",
         "« Il y a eu une panne d'électricité chez moi et mon réveil ne s'est pas "
         "déclenché. Je serai en retard. » Une cause extérieure, pas une excuse."),
    ], notes="Faire remarquer que les quatre tiennent en deux phrases. Aucune ne "
             "s'excuse plus d'une fois.")

    d.tableau('Analyse', "Ce que la secrétaire va demander",
              ['Sa question', 'Votre réponse'],
              [["Votre nom, s'il vous plaît ?", "prénom et nom, épelés si besoin"],
               ["Dans quel groupe êtes-vous ?", "le numéro ou le nom de l'enseignant"],
               ["Vous arriverez à quelle heure ?", "une heure précise, même approximative"],
               ["Avez-vous une preuve ?", "oui, avec la date, ou non, honnêtement"]],
              cle=0,
              note="Quatre questions, toujours les mêmes. Les préparer d'avance rend "
                   "l'appel facile.",
              notes="Faire écrire les quatre réponses personnelles dans le cahier : nom, "
                    "groupe, enseignant. Beaucoup ne savent pas dire leur groupe.")

    d.pratique('Pratique · 1 de 4', "Que dites-vous ?",
               "Une ou deux phrases, à voix haute.", [
        ("Vous avez une forte migraine et devez rester couché toute la journée.",
         "Bonjour, ici… J'ai une forte migraine, je ne pourrai pas venir au cours "
         "aujourd'hui."),
        ("Votre famille déménage dans une autre région, loin du centre.",
         "Bonjour, ici… Ma famille déménage loin d'ici, je dois abandonner le cours."),
        ("Votre voiture est en panne sur l'autoroute, vous attendez la dépanneuse.",
         "Bonjour, ici… Ma voiture est tombée en panne, je serai en retard ce matin."),
        ("Panne d'électricité, votre réveil n'a pas sonné.",
         "Bonjour, ici… Il y a eu une panne d'électricité, mon réveil n'a pas sonné. "
         "J'arriverai vers dix heures."),
    ], corrige=True,
       notes="Faire dire chaque phrase debout, par un élève différent. Ne corriger que "
             "le mot retard/absence/abandon et la présence d'une heure.")

    d.piege("Le piège du ton d'excuse",
            "Je suis vraiment, vraiment désolé, c'est de ma faute…",
            "Il y a eu une panne d'électricité, mon réveil n'a pas sonné.",
            "Une explication n'est pas un aveu. Dire les faits calmement, une fois, "
            "suffit. Un ton d'excuse répétée met la personne au bout du fil mal à "
            "l'aise et fait perdre du temps à tout le monde.",
            notes="Point culturel à traiter avec soin, comme en A1. Ce n'est pas que "
                  "l'excuse soit malvenue : c'est sa longueur qui pose problème.")

    d.piege("Le piège de l'heure non donnée",
            "Je serai en retard.",
            "Je serai en retard, j'arriverai vers dix heures.",
            "Sans heure, la personne ne peut rien organiser : elle ne sait pas si elle "
            "doit vous attendre, commencer sans vous, ou vous rayer de la liste. Même "
            "une heure approximative vaut mieux que rien.",
            notes="Faire ajouter une heure à chacune des quatre phrases de l'exercice "
                  "précédent. La différence est immédiate.")

    d.pratique('Pratique · 2 de 4', "Jeu de rôle · l'appel au centre",
               "À deux. L'un est à la réception, l'autre appelle. Puis on échange.", [
        ("La réception ouvre", "Centre de formation, bonjour."),
        ("Vous vous nommez et expliquez", "trois informations, dix secondes"),
        ("La réception demande", "Dans quel groupe êtes-vous ?"),
        ("La réception demande", "Vous arriverez à quelle heure ?"),
        ("Vous proposez", "une preuve, ou une façon de rattraper"),
    ], corrige=False,
       notes="Quinze minutes par personne. Circuler avec une feuille et noter les deux "
             "manques les plus fréquents. Ne pas interrompre les dyades.")

    d.pratique('Pratique · 3 de 4', "Répondez à la question difficile",
               "La secrétaire pose une question à laquelle on ne s'attendait pas.", [
        ("« C'est votre troisième absence ce mois-ci. »",
         "Oui, je sais. C'est une période difficile. Je peux rattraper les cours manqués."),
        ("« Avez-vous une preuve ? »",
         "Non, pas pour aujourd'hui. Mais je peux en apporter une pour les autres fois."),
        ("« Vous auriez dû appeler hier. »",
         "Vous avez raison. Je l'ai su seulement ce matin."),
        ("« Est-ce que vous comptez continuer le cours ? »",
         "Oui, absolument. C'est seulement une absence, pas un abandon."),
    ], corrige=True,
       notes="Ces quatre réponses valent d'être travaillées : elles reconnaissent le "
             "problème sans s'effondrer en excuses. C'est un équilibre difficile.")

    d.pratique('Pratique · 4 de 4', "Jeu de rôle · la question difficile",
               "La personne à la réception pose une des questions ci-dessus. Répondez.", [
        ("Règle du jeu", "la réception choisit une question sans prévenir"),
        ("Vous répondez", "en une ou deux phrases, sans vous excuser longuement"),
        ("Vous proposez", "une solution concrète"),
        ("On échange", "et on recommence avec une autre question"),
    ], corrige=False,
       notes="Dix minutes. C'est l'exercice le plus difficile du module : la réponse "
             "n'est pas préparée. Encourager les hésitations, elles sont normales.")

    d.billet(
        "Écrivez ce que vous répondriez à « C'est votre troisième absence ce mois-ci. »",
        exemples=[
            "Deux phrases : reconnaître, puis proposer.",
            "Sans excuse longue, sans se justifier plus d'une fois.",
        ],
        notes="Lire quelques billets à voix haute, sans nommer les auteurs. C'est la "
              "situation que tout le monde redoute et que personne n'a préparée.")

    return d.save(dossier)
