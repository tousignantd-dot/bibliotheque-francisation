# -*- coding: utf-8 -*-
"""D1 · Sept cent quatre-vingts dollars
Bloc D « Défi 3 · Une opération que je n'ai pas faite » · couleur acier · 90 min.
Source : dialogue `t3`, exercices `t3vf` et `t3doc`, et leurs mini-leçons.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='D1', section='acier',
        titre='Sept cent quatre-vingts dollars',
        chapeau="Une opération apparaît au relevé, chez un commerçant "
                "inconnu, et la carte n'a jamais quitté le portefeuille. "
                "C'est le seul moment du module où la cliente parle le plus.",
        duree='90 minutes')

    d.titre(notes="Ouverture du bloc D. Le ton change : les deux blocs précédents "
                  "étaient de la compréhension, celui-ci est de l'action. Le dire.")

    d.objectifs([
        "signaler une opération non autorisée dans le bon ordre ;",
        "dire quelle somme maximale la loi laisse à la charge du titulaire ;",
        "reconnaître un message d'hameçonnage ;",
        "noter les quatre renseignements qui valent une preuve.",
    ], notes="Le quatrième objectif est le plus concret de tout le module : numéro de "
             "dossier, date, heure, nom de la personne.")

    d.declencheur(
        'Observation', "Qu'est-ce que tu ferais en premier, en voyant un achat que tu "
                       "n'as pas fait ?",
        pistes=[
            "Appeler tout de suite, ou attendre le prochain relevé ?",
            "Que dirais-tu en premier au téléphone ?",
            "Est-ce que tu paierais le montant en attendant ?",
            "Qu'est-ce que tu noterais pendant l'appel ?",
        ],
        notes="Beaucoup de gens attendent « pour être sûrs ». C'est exactement ce qu'il "
              "ne faut pas faire, et la règle du jour l'explique.")

    d.dialogue('Dialogue · 1 de 3', "La carte est encore dans mon portefeuille", [
        ("MARLÈNE", "Il y a une opération sur mon relevé que je n'ai pas faite. Sept cent quatre-vingts dollars, le quatorze.", True),
        ("STEVE", "Avant tout : est-ce que vous avez encore votre carte en main ?", True),
        ("MARLÈNE", "Oui, elle est dans mon portefeuille. Je ne l'ai jamais perdue.", True),
        ("STEVE", "Donc c'est un achat à distance. Vous n'avez rien acheté chez ce commerçant ?", True),
    ], consigne="Écouter d'abord, diapositive masquée.",
       notes="Faire remarquer la première question de l'agent. Elle décide de tout le "
             "reste du dossier, et l'élève doit savoir y répondre en une phrase.")

    d.dialogue('Dialogue · 2 de 3', "Ce que le blocage entraîne", [
        ("STEVE", "Je bloque la carte immédiatement et je vous en fais émettre une nouvelle.", True),
        ("MARLÈNE", "Attendez, vous la bloquez tout de suite ? Et mes paiements automatiques ?", True),
        ("STEVE", "Ils vont tomber. Vous devrez donner le nouveau numéro à chaque commerçant.", True),
        ("MARLÈNE", "Bon. Bloquez-la. Mais les sept cent quatre-vingts dollars, je les paie ou pas ?", True),
    ], notes="La question de Marlène sur les paiements automatiques est le geste que "
             "personne ne pense à poser. Le souligner : elle interrompt pour vérifier.")

    d.dialogue('Dialogue · 3 de 3', "Un écrit laisse une trace", [
        ("STEVE", "Vous ne les payez pas. J'ouvre un dossier de contestation et le montant est retiré pendant l'enquête.", True),
        ("MARLÈNE", "Est-ce que je peux avoir quelque chose par écrit ? Un numéro de dossier ?", True),
        ("STEVE", "Notez aussi l'heure de cet appel-ci et mon nom.", True),
        ("STEVE", "Si le montant n'a pas disparu dans trente jours, écrivez-nous plutôt que de rappeler. Un écrit laisse une trace ; un appel, non.", True),
    ], notes="La dernière réplique ouvre la lettre du bloc E. La lire deux fois, "
             "lentement.")

    d.regle("Cinquante dollars, à une condition",
            "La responsabilité du titulaire est limitée à 50 $, s'il avise l'émetteur "
            "sans délai.",
            precision="Après l'avis, il n'est plus responsable d'aucune opération. "
                      "« Sans délai » n'a pas de nombre, mais il en a l'effet : celui "
                      "qui attend trois semaines devra expliquer pourquoi. La "
                      "négligence dans la protection du NIP, elle, peut coûter "
                      "davantage.",
            notes="Fait vérifié auprès de l'Office de la protection du consommateur. Le "
                  "dire au groupe : ce n'est pas une politique de banque, c'est la loi.")

    d.tableau('Analyse', "Les gestes, dans l'ordre",
              ['Quand', 'Quoi'],
              [['tout de suite', 'faire bloquer la carte'],
               ['dans la minute', 'prévoir les paiements automatiques'],
               ["pendant l'appel", 'noter dossier, date, heure, nom'],
               ["après l'appel", 'garder le relevé où le montant paraît'],
               ['après trente jours', 'écrire une lettre datée']],
              cle=0,
              notes="Diapositive à photographier. C'est la fiche de référence du bloc "
                    "D, et elle est reprise dans la lettre de E2.")

    d.vocabulaire('Vocabulaire', "Quatre mots de la contestation", [
        ("une opération non autorisée", "Une entrée ou une sortie d'argent que le titulaire du compte n'a pas faite et n'a pas permise."),
        ("une contestation", "La démarche par laquelle on demande à l'institution de retirer une opération du relevé et d'enquêter."),
        ("l'hameçonnage", "Le faux message qui imite une institution pour faire donner un numéro ou un mot de passe."),
        ("un numéro de dossier", "Le code que l'institution attribue à une démarche et qui permet de la retrouver plus tard."),
    ], notes="« Une opération non autorisée » plutôt qu'« une erreur » : le mot juste "
             "change la façon dont la demande est traitée. Le dire.")

    d.piege('Le piège', "rappeler au numéro donné dans le message",
            "rappeler au numéro imprimé sur la carte",
            "Le numéro fourni par le fraudeur mène au fraudeur. Aucune institution ne "
            "demande par message, par courriel ou par téléphone entrant le numéro "
            "complet de la carte, le NIP ou le code à trois chiffres. Cette règle-là "
            "n'a aucune exception.",
            notes="C'est la seule chose de la séance que les élèves doivent retenir "
                  "même s'ils oublient tout le reste. Le dire ainsi.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après l'appel au service de la sécurité des cartes.", [
        ("Marlène a encore sa carte dans son portefeuille.", "vrai"),
        ("Les paiements automatiques continueront comme avant.", "faux - ils vont tomber"),
        ("Le montant contesté est retiré du solde pendant l'enquête.", "vrai"),
        ("Marlène a donné son numéro de carte dans la page du message.", "faux - elle a fermé la page"),
        ("L'institution demande parfois le NIP par message texte.", "faux - jamais"),
        ("Si rien n'a bougé dans trente jours, il vaut mieux rappeler.", "faux - il faut écrire"),
    ], corrige=True,
       notes="Faire justifier le dernier par la réplique de l'agent. Il annonce la "
             "tâche d'écriture du bloc E.")

    d.billet("Écris les quatre renseignements qu'il faut noter pendant l'appel.",
             exemples=["le numéro de dossier, la date, l'heure, le nom de la personne"],
             notes="Une minute. Vérifier les quatre : c'est la seule chose de la séance "
                   "qui se retienne par coeur.")

    return d.save(dossier)
