# -*- coding: utf-8 -*-
"""B2 · Les six parties d'un message.
Bloc B · couleur ambre (écriture) · 75 min.
Source : exercices `t1ord1` et `t1ord2` — remettre un message dans l'ordre.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B2', section='ambre',
        titre="Les six parties d'un message",
        chapeau="Un message téléphonique suit toujours le même plan. Le connaître permet "
                "de le construire sans réfléchir — et surtout de ne rien oublier quand "
                "on est pressé.",
        duree='75 minutes')

    d.titre(notes="Écrire les six parties au tableau dans le désordre et demander au "
                  "groupe de les remettre en ordre avant toute explication. Ils y "
                  "arriveront presque : c'est encourageant.")

    d.objectifs([
        "connaître les six parties d'un message téléphonique ;",
        "les placer dans le bon ordre ;",
        "reconnaître une partie manquante ;",
        "écrire un message complet en six phrases.",
    ])

    d.tableau('Analyse', "Les six parties, dans l'ordre",
              ['Rang', 'La partie', 'Exemple'],
              [["1", "la salutation", "Bonjour, Madame Girard."],
               ["2", "qui vous êtes", "C'est Julien Fortin, directeur."],
               ["3", "la raison de l'appel", "J'appelle pour vous dire que…"],
               ["4", "ce que vous demandez", "Pourriez-vous me rappeler ?"],
               ["5", "le remerciement", "Je vous remercie."],
               ["6", "la salutation finale", "Bonne journée."]],
              cle=1,
              notes="Les six sont dans cet ordre dans tous les messages professionnels. "
                    "Les faire copier dans le cahier : c'est le plan de tout le module.")

    d.regle("La règle d'ordre",
            "On se nomme avant d'expliquer, et on demande avant de remercier.",
            precision="Un message qui commence par la raison oblige l'auditeur à "
                      "attendre la fin pour savoir qui parle. Un message qui remercie "
                      "avant de demander laisse la demande sans réponse.",
            notes="Faire écouter un message dans le désordre — improvisé par vous — et "
                  "demander ce qui gêne. Le groupe le sentira sans savoir le nommer.")

    d.cartes('Analyse', "Le message du directeur, découpé", [
        ("Salutation et identité",
         "« Bonjour, Madame Girard. C'est Julien Fortin, directeur de l'école "
         "Sainte-Marie. » Le nom ET la fonction : la fonction dit pourquoi il appelle."),
        ("La raison",
         "« J'appelle pour vous dire que votre fils s'est blessé au genou pendant la "
         "récréation. Il faut venir le chercher. » La nouvelle, puis l'action attendue."),
        ("La demande",
         "« Pourriez-vous me rappeler dès que possible, s'il vous plaît ? » Une demande "
         "polie, avec un délai."),
        ("La clôture",
         "« Je vous remercie. Bonne journée. » Deux formules courtes. On ne s'excuse "
         "pas d'avoir appelé."),
    ], notes="Insister sur la fonction dans la première carte : « directeur de l'école » "
             "explique déjà à moitié pourquoi il appelle.")

    d.pratique('Pratique · 1 de 4', "Remettez le message dans l'ordre",
               "Un directeur d'école laisse ce message. Numérotez de 1 à 6.", [
        ("Pourriez-vous me rappeler dès que possible, s'il vous plaît ?", "4"),
        ("Bonjour, Madame Girard.", "1"),
        ("Je vous remercie.", "5"),
        ("C'est Julien Fortin, directeur de l'école Sainte-Marie.", "2"),
        ("Bonne journée.", "6"),
        ("J'appelle pour vous dire que votre fils s'est blessé au genou.", "3"),
    ], corrige=True,
       notes="Laisser chercher seul cinq minutes, puis corriger en grand groupe en "
             "nommant chaque partie.")

    d.pratique('Pratique · 2 de 4', "Un deuxième message à remettre en ordre",
               "Un employé laisse ce message à sa superviseure. Numérotez de 1 à 6.", [
        ("J'aurai donc environ trente minutes de retard.", "4"),
        ("Bonjour, Madame Bélisle.", "1"),
        ("Merci beaucoup.", "6"),
        ("Ici Karim Haddad.", "2"),
        ("Pouvez-vous me rappeler au 514 555-0134, s'il vous plaît ?", "5"),
        ("Je vous appelle pour vous informer que ma voiture est tombée en panne.", "3"),
    ], corrige=True,
       notes="Ici, la conséquence (« trente minutes de retard ») vient après la raison "
             "(« la voiture est tombée en panne »). C'est l'ordre logique : cause, puis "
             "effet.")

    d.tableau('Analyse', "Trois formules pour chaque partie",
              ['La partie', 'Trois façons de le dire'],
              [["se nommer", "Ici… · C'est… · Je m'appelle…"],
               ["donner la raison", "J'appelle pour… · Je vous appelle parce que… · Je vous informe que…"],
               ["demander", "Pourriez-vous… · Pouvez-vous… · J'aimerais que…"],
               ["remercier", "Merci beaucoup. · Je vous remercie. · Merci de votre compréhension."]],
              cle=0, props=[0.3, 0.7],
              notes="Trois formules par partie : chacun choisit celle qui lui vient le "
                    "plus facilement. Ne pas imposer une seule formulation.")

    d.piege("Le piège du numéro non répété",
            "Rappelez-moi au 514 555-0134.",
            "Rappelez-moi au 514 555-0134. Je répète : 514 555-0134.",
            "Un numéro de téléphone dit une seule fois dans une boîte vocale est presque "
            "toujours perdu : la personne écoute sans papier. Répéter le numéro "
            "lentement, à la fin du message, est la règle professionnelle.",
            notes="Faire pratiquer : chacun dit son numéro deux fois, lentement, à voix "
                  "haute. La plupart le disent beaucoup trop vite.")

    d.piege("Le piège de la partie manquante",
            "Bonjour, ma voiture est tombée en panne. Merci.",
            "Bonjour, ici Karim Haddad. Ma voiture est tombée en panne…",
            "La partie qu'on saute le plus souvent est la deuxième : on oublie de se "
            "nommer, parce qu'on croit que la personne reconnaîtra la voix. Sur une "
            "boîte vocale, elle ne la reconnaît pas.",
            notes="Demander qui a déjà reçu un message sans nom. Presque toutes les mains "
                  "se lèvent.")

    d.pratique('Pratique · 3 de 4', "Quelle partie manque ?",
               "Chaque message est incomplet.", [
        ("« Bonjour, Madame Bélisle. Ma voiture est en panne. Merci. »",
         "l'identité, la demande, la salutation finale"),
        ("« Ici Karim Haddad. J'aurai trente minutes de retard. Merci. Bonne journée. »",
         "la salutation du début"),
        ("« Bonjour, ici Karim Haddad. Rappelez-moi. Merci. »",
         "la raison de l'appel"),
        ("« Bonjour, ici Karim. Ma voiture est en panne. J'aurai du retard. »",
         "le nom de famille, le remerciement, la salutation finale"),
    ], corrige=True,
       notes="Exercice de diagnostic. Faire dire chaque message à voix haute avant "
             "d'identifier ce qui manque : l'oreille repère mieux que l'œil.")

    d.pratique('Pratique · 4 de 4', "Écrivez le message complet",
               "Six phrases, une par partie, dans l'ordre.", [
        ("La situation",
         "Vous serez en retard de quarante minutes à cause d'une panne d'autobus."),
        ("À qui vous écrivez", "à la secrétaire du centre de formation"),
        ("À ne pas oublier", "votre nom complet et votre numéro, répété deux fois"),
    ], corrige=False,
       notes="Quinze minutes d'écriture. Circuler et vérifier la présence des six "
             "parties, pas la qualité du style.")

    d.billet(
        "Écrivez les six parties d'un message, dans l'ordre, avec un exemple pour chacune.",
        exemples=[
            "Une ligne par partie.",
            "Vos exemples doivent tous parler de la même situation.",
        ],
        notes="Ce billet est la fiche de référence du module. Suggérer de le garder dans "
              "le cahier jusqu'à la fin.")

    return d.save(dossier)
