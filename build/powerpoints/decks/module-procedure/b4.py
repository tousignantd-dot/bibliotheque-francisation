# -*- coding: utf-8 -*-
"""B4 · Demander comment faire.
Bloc B · couleur teal (écoute et réponds) · 75 min.
Source : dialogue `t1`, production orale du défi 1.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B4', section='teal',
        titre='Demander comment faire',
        chapeau="Poser la question est plus difficile que comprendre la réponse. Trois "
                "formules suffisent, et elles fonctionnent partout : au travail, à la "
                "banque, au centre de services.",
        duree='75 minutes')

    d.titre(notes="Séance de production orale. Disposer la classe en dyades dès le "
                  "début. Rendre les billets de B1 : les trois questions y sont déjà.")

    d.objectifs([
        "demander comment faire une démarche, poliment ;",
        "demander ce qui est obligatoire ;",
        "demander un délai ;",
        "reformuler la réponse pour vérifier qu'on a compris.",
    ])

    d.regle('Les trois questions',
            "Comment faire ? · Qu'est-ce qui est obligatoire ? · Combien de temps ?",
            precision="Ces trois questions couvrent n'importe quelle procédure. La "
                      "première donne les étapes, la deuxième évite un refus, la "
                      "troisième évite d'attendre pour rien.",
            notes="Écrire les trois au tableau et les y laisser toute la séance. Les "
                  "élèves les regarderont pendant les jeux de rôle : c'est voulu.")

    d.tableau('Analyse', "Trois formules pour chaque question",
              ['La question', 'Trois façons de la poser'],
              [["comment faire", "Comment est-ce qu'on fait pour… · J'aimerais savoir comment… · Quelle est la procédure pour…"],
               ["ce qui est obligatoire", "Est-ce que je dois… · Qu'est-ce qu'il faut apporter ? · C'est obligatoire ?"],
               ["le délai", "Combien de temps faut-il ? · Ça prend combien de temps ? · Quand est-ce que je recevrai…"]],
              cle=0, props=[0.28, 0.72],
              notes="Trois formules par question : chacun choisit celle qui lui vient le "
                    "plus facilement. Ne pas en imposer une seule.")

    d.cartes('Analyse', "Quatre réflexes qui font gagner du temps", [
        ("Annoncez votre sujet d'abord",
         "« Bonjour, c'est au sujet d'une demande de remboursement. » La personne sait "
         "tout de suite si elle peut vous aider ou si elle doit transférer."),
        ("Une question à la fois",
         "Trois questions posées d'un coup produisent une réponse partielle. Posez-en "
         "une, écoutez, puis passez à la suivante."),
        ("Reformulez la réponse",
         "« Donc je remplis le formulaire, je joins une photo du reçu, et j'attends "
         "l'approbation. C'est bien ça ? » Trente secondes qui évitent un refus."),
        ("Notez pendant, pas après",
         "Un papier et un crayon avant de composer le numéro. On ne retient pas trois "
         "étapes et un délai de mémoire."),
    ], notes="Le troisième réflexe est celui qui manque le plus. Le faire pratiquer "
             "systématiquement dans les jeux de rôle.")

    d.pratique('Pratique · 1 de 4', "Formulez la question",
               "Trois façons possibles pour chacune.", [
        ("Vous voulez connaître les étapes d'une demande.",
         "Comment est-ce qu'on fait pour faire une demande de remboursement ?"),
        ("Vous voulez savoir s'il faut joindre un reçu.",
         "Est-ce que je dois joindre mon reçu ?"),
        ("Vous voulez connaître le délai.",
         "Combien de temps faut-il pour recevoir le remboursement ?"),
        ("Vous voulez savoir qui approuve.",
         "Qui doit approuver la demande ?"),
    ], corrige=True,
       notes="Accepter toute formulation polie et claire. Ce qui compte est que la "
             "question porte sur une seule chose.")

    d.pratique('Pratique · 2 de 4', "Reformulez la réponse",
               "Vérifiez que vous avez compris, en une phrase.", [
        ("« Remplissez le formulaire sous l'onglet Dépenses, avec une photo du reçu. »",
         "Donc je remplis le formulaire sous Dépenses et j'ajoute une photo du reçu, "
         "c'est bien ça ?"),
        ("« Environ dix jours ouvrables après l'approbation du superviseur. »",
         "Donc environ deux semaines après que mon superviseur a approuvé ?"),
        ("« La photo doit être claire, sinon la demande est refusée. »",
         "Donc si la photo est floue, la demande est refusée ?"),
        ("« Gardez votre reçu original au cas où. »",
         "Donc je garde le papier même après avoir envoyé la photo ?"),
    ], corrige=True,
       notes="Faire remarquer que la reformulation transforme souvent l'information : "
             "« dix jours ouvrables » devient « deux semaines ». C'est bon signe.")

    d.piege("Le piège des trois questions d'un coup",
            "Comment je fais, qu'est-ce qu'il faut apporter, et ça prend combien de temps ?",
            "Comment est-ce qu'on fait pour… (écouter) … Et est-ce qu'il faut un reçu ?",
            "Trois questions à la fois obtiennent une réponse à la première et rien pour "
            "les deux autres. La personne au bout du fil ne peut pas tout traiter en "
            "même temps, et vous non plus.",
            notes="Faire l'expérience : poser les trois d'un coup à un élève et demander "
                  "au groupe combien de réponses il a retenues.")

    d.piege("Le piège du silence après la réponse",
            "— Environ dix jours ouvrables. — D'accord, merci, au revoir.",
            "— Environ dix jours ouvrables. — Donc deux semaines environ ? Merci.",
            "Raccrocher sur un « d'accord » laisse toutes les incompréhensions en place. "
            "Reformuler prend dix secondes et donne à l'autre personne l'occasion de "
            "corriger — ce qu'elle fera volontiers.",
            notes="Lier au module 2, séance D1 : c'est le même geste que répéter une "
                  "indication de chemin.")

    d.pratique('Pratique · 3 de 4', "Jeu de rôle · l'appel au service",
               "À deux. L'un est au service, l'autre appelle. Puis on échange.", [
        ("Vous annoncez votre sujet", "Bonjour, c'est au sujet d'une demande de remboursement."),
        ("Première question", "comment faire — puis vous écoutez et vous notez"),
        ("Deuxième question", "ce qui est obligatoire"),
        ("Troisième question", "le délai"),
        ("Vous reformulez", "les trois réponses en une phrase, avant de raccrocher"),
    ], corrige=False,
       notes="Vingt minutes. Circuler et vérifier une seule chose : est-ce que la "
             "reformulation finale est faite ? C'est le critère de la séance.")

    d.pratique('Pratique · 4 de 4', "Une procédure que vous ne connaissez pas",
               "Choisissez une démarche réelle et posez les trois questions.", [
        ("Renouveler une carte d'assurance maladie", "les trois questions, adaptées"),
        ("Demander un relevé d'emploi", "les trois questions, adaptées"),
        ("Inscrire un enfant à l'école", "les trois questions, adaptées"),
        ("Ouvrir un compte bancaire", "les trois questions, adaptées"),
    ], corrige=False,
       notes="Dix minutes. C'est l'exercice de transfert : les mêmes questions, hors du "
             "contexte du travail. Encourager chacun à choisir une démarche qui "
             "l'attend vraiment.")

    d.billet(
        "Écrivez les trois questions, adaptées à une démarche qui vous attend.",
        exemples=[
            "Une démarche réelle : une inscription, un renouvellement, une demande.",
            "Ajoutez la phrase de reformulation que vous diriez à la fin.",
        ],
        notes="Ces billets sont utiles au-delà du cours. Suggérer de les garder dans le "
              "téléphone plutôt que dans le cahier.")

    return d.save(dossier)
