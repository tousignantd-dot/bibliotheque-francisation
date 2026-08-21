# -*- coding: utf-8 -*-
"""D1 · Déplacer, annuler, ne pas venir.
Bloc D « Défi 3 · Déplacer ou annuler » · couleur acier · 75 min.
Source : dialogue `t3`, exercices `t3vf` et `t3etapes`.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n5-rendezvous/images/')


def build(dossier):
    d = Deck(
        code='D1', section='acier',
        titre="Déplacer, annuler, ne pas venir",
        chapeau="Trois mots, trois conséquences. Le premier garde votre "
                "démarche, le deuxième rend la place, le troisième se "
                "paie — et c'est le seul qui laisse une trace au dossier.",
        duree='75 minutes')

    d.titre(notes="Ouverture du défi 3. Demander au groupe qui a déjà manqué un "
                  "rendez-vous sans prévenir, et pourquoi. La réponse la plus fréquente "
                  "est « je ne savais pas quoi dire au téléphone » — c'est le sujet.")

    d.objectifs([
        "distinguer déplacer, annuler et ne pas venir ;",
        "dire les trois choses qu'exige un déplacement ;",
        "connaître le délai d'annulation et savoir le calculer ;",
        "laisser un message d'annulation complet sur une boîte vocale.",
    ])

    d.declencheur(
        'Écoute', "« Bonjour, je peux pas venir demain, merci. » Que peut faire la "
                  "clinique avec ce message ?",
        image=IMG + 'telephone-message.jpg',
        pistes=[
            "Qui est-ce ?",
            "Quel rendez-vous exactement ?",
            "Avec quel professionnel ?",
            "Comment la rappeler ?",
        ],
        notes="Dire le message très vite, comme un vrai. Les quatre questions restent "
              "sans réponse et le groupe le voit tout de suite : ce message n'annule rien "
              "et l'absence sera notée.")

    d.regle("Déplacer, ce n'est pas annuler",
            "Si vous voulez un autre rendez-vous, dites « déplacer ».",
            precision="La clinique annule alors l'ancien elle-même et vous en donne un "
                      "nouveau dans le même appel : vous n'avez pas deux démarches à "
                      "faire. Dire « annuler » ferme le dossier et vous laisse tout "
                      "recommencer.",
            notes="Diapositive à photographier. Le mot employé décide de ce qui est "
                  "inscrit au dossier — c'est le point le plus concret du défi.")

    d.dialogue('Dialogue · 1 de 3', "La demande, et la raison", [
        ("RACHID", "Bonjour madame. Rachid Benali. Je vous appelle pour déplacer mon "
                   "rendez-vous de suivi.", True),
        ("MANON", "Un instant, je vous trouve. Le mardi 8 juillet à onze heures, avec "
                  "la docteure Fongang ?", True),
        ("RACHID", "C'est ça. Mon horaire de travail a changé : je commence à sept "
                   "heures maintenant, et je ne finis qu'à quinze heures.", True),
        ("MANON", "Je comprends. Vous préférez donc en fin de journée.", False),
    ], consigne="Écoutez d'abord, diapositive masquée.",
       notes="Trois choses en trois répliques : quel rendez-vous, pourquoi, et — à la "
             "suivante — quand il est libre. Les faire compter.")

    d.dialogue('Dialogue · 2 de 3', "Les disponibilités, dites d'avance", [
        ("RACHID", "Oui, ou très tôt le matin, avant sept heures, si ça existe.", True),
        ("MANON", "Ça existe : la docteure ouvre à sept heures quinze le mercredi. "
                  "J'ai mercredi le 9, à sept heures quinze.", True),
        ("RACHID", "Il faut que je sois au travail à sept heures ce jour-là. C'est "
                   "trop juste.", True),
        ("MANON", "Alors je regarde en fin de journée… J'ai le jeudi 10 juillet à "
                  "seize heures trente.", True),
    ], notes="Rachid dit ses disponibilités sans qu'on les lui demande. C'est ce qui fait "
             "tenir l'appel en deux minutes au lieu de six.")

    d.dialogue('Dialogue · 3 de 3', "Le délai, et ce qu'il évite", [
        ("RACHID", "Jeudi 10, seize heures trente, je le prends. Vous annulez celui "
                   "du mardi ?", True),
        ("MANON", "Je viens de le faire. Vous n'avez rien d'autre à faire, et il n'y "
                  "a pas de frais : vous m'appelez plus de vingt-quatre heures à "
                  "l'avance.", True),
        ("RACHID", "Une dernière chose. Ma prise de sang est prévue le lundi 7. "
                   "Est-ce que le résultat sera arrivé pour le jeudi ?", True),
        ("MANON", "Trois jours ouvrables, en général. Ce sera juste, mais ça devrait "
                  "entrer.", True),
    ], notes="La dernière question de Rachid est celle qu'on oublie : à quoi sert un "
             "rendez-vous de suivi si le résultat n'est pas arrivé ?")

    d.cartes("Trois mots, trois conséquences", "Et un seul se paie", [
        ("Déplacer",
         "Le rendez-vous survit : on garde la démarche et on change le moment."),
        ("Annuler",
         "On rend la place, à temps. Rien à payer, aucune trace, libre d'en reprendre un."),
        ("Ne pas venir",
         "Le créneau reste vide pour tout le monde, et la clinique facture souvent des frais."),
        ("Le rappel de la veille",
         "Ce n'est pas un simple avis : c'est la dernière fenêtre gratuite pour appeler."),
    ], notes="Faire calculer la limite d'annulation pour un rendez-vous du jeudi seize "
             "heures trente. Réponse : mercredi seize heures trente.")

    d.tableau('Le message d\'annulation', "Six éléments, quarante secondes",
              ['Ce qu\'on donne', 'Pourquoi'],
              [["Nom et date de naissance", "retrouver le bon dossier"],
               ["Date, heure et professionnel", "savoir quel rendez-vous libérer"],
               ["La raison, en une phrase", "ne pas être noté comme absent"],
               ["Un numéro, répété deux fois", "pouvoir vous rappeler"]],
              cle=0,
              note="On ne rappelle personne pour faire répéter un message : il se réussit du premier coup.",
              notes="Faire écrire les six éléments avant d'enregistrer quoi que ce soit. "
                    "C'est le matériau direct de la production orale.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après le dialogue.", [
        ("Rachid appelle parce que son horaire a changé.", "vrai"),
        ("Il dit quand il est libre sans qu'on le lui demande.", "vrai"),
        ("Il accepte le mercredi à sept heures quinze.", "faux — il travaille à sept heures"),
        ("Rachid doit annuler lui-même l'ancien rendez-vous.", "faux — Manon le fait"),
        ("Il n'y a pas de frais : il appelle plus de 24 h à l'avance.", "vrai"),
        ("Sur la boîte vocale, il donne sa date de naissance.", "vrai"),
    ], corrige=True,
       notes="Faire justifier chaque « faux » par la réplique exacte.")

    # `capture` n'existe que dans theme.Deck : les présentations la portent, les
    # fiches imprimées non (build/powerpoints/fiche.py n'a pas la méthode). Une
    # fiche noir et blanc n'a de toute façon rien à faire d'une capture d'écran.
    if hasattr(d, 'capture'):
        d.capture('t3etapes', "Le message d'annulation, phrase par phrase",
                  consigne="Choisissez une phrase du message, puis ce qu'elle apporte.",
                  notes="Projeter avant l'écriture du billet : chaque phrase du message y "
                        "trouve sa raison d'être.")

    d.billet(
        "Écrivez le message que vous laisseriez pour annuler un rendez-vous.",
        exemples=[
            "Les six éléments, dans l'ordre : nom, naissance, quel rendez-vous, pourquoi, la suite, le numéro.",
            "Quarante secondes à voix haute — chronométrez-vous.",
        ],
        notes="Ce billet devient le brouillon de la production orale. Le ramasser, le "
              "corriger, le rendre en E1.")

    return d.save(dossier)
