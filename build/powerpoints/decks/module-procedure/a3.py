# -*- coding: utf-8 -*-
"""A3 · Le vocabulaire de bureau.
Bloc A · couleur foret (vocabulaire) · 60 min.
Source : exercices `prVocab` et `prVerbe`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A3', section='foret',
        titre='Le vocabulaire de bureau',
        chapeau="Remplir, joindre, soumettre, approuver, signaler, réserver. Six verbes "
                "qui reviennent dans toutes les procédures d'entreprise — et qu'aucun "
                "cours de français général n'enseigne.",
        duree='60 minutes')

    d.titre(notes="Séance de vocabulaire fonctionnel. Beaucoup de ces mots sont "
                  "reconnus mais mal employés. Insister sur les collocations : on "
                  "remplit un formulaire, on joint un reçu.")

    d.objectifs([
        "employer les six verbes des procédures avec le bon complément ;",
        "nommer les parties d'une application : onglet, catégorie, statut ;",
        "comprendre « jour ouvrable » et calculer un délai ;",
        "lire une consigne d'application sans se tromper d'action.",
    ])

    d.tableau('Analyse', "Six verbes et ce qui les suit",
              ['Le verbe', 'Ce qu\'on met après'],
              [["remplir", "un formulaire, une demande, un champ"],
               ["joindre", "un reçu, une photo, un document"],
               ["soumettre", "une demande, un formulaire, un dossier"],
               ["approuver", "une demande, une dépense, un congé"],
               ["signaler", "un bris, un problème, une absence"],
               ["réserver", "un véhicule, une salle, un équipement"]],
              cle=0, props=[0.28, 0.72],
              notes="C'est la colonne de droite qui compte : le verbe seul ne suffit pas, "
                    "c'est le couple verbe + complément qui s'apprend.")

    d.regle('La règle de la séance',
            "Un verbe de procédure s'apprend avec son complément.",
            precision="On ne dit pas « remplir un reçu » ni « joindre un formulaire ». On "
                      "remplit un formulaire et on joint un reçu. Apprendre le verbe seul "
                      "ne sert à rien : c'est la paire qu'il faut retenir.",
            notes="Faire écrire les six paires dans le cahier, en colonne. C'est la fiche "
                  "de référence de tout le module.")

    d.vocabulaire('Vocabulaire · 1 de 2', "Dans l'application", [
        ("un onglet", "Une section cliquable dans une application ou un site."),
        ("une catégorie", "Un groupe dans lequel on classe une dépense ou une demande."),
        ("le statut", "L'état d'une demande : en attente, approuvée, refusée."),
        ("téléverser", "Envoyer un fichier depuis son appareil vers un site."),
        ("un champ", "Une case à remplir dans un formulaire."),
        ("un menu déroulant", "Une liste qui s'ouvre quand on clique dessus."),
    ], notes="« Téléverser » est le mot québécois pour « uploader ». Le signaler : les "
             "applications d'entreprise l'emploient.")

    d.vocabulaire('Vocabulaire · 2 de 2', "Les délais et les papiers", [
        ("un jour ouvrable", "Un jour de la semaine où l'entreprise est ouverte."),
        ("un délai", "Le temps prévu avant une réponse ou un versement."),
        ("un reçu original", "Le papier reçu au moment de l'achat, pas une copie."),
        ("une pièce justificative", "Un document qui prouve une dépense ou une situation."),
        ("un accusé de réception", "Le message qui confirme qu'une demande est arrivée."),
    ], notes="« Accusé de réception » est le mot à retenir : c'est ce qu'on cherche quand "
             "on se demande si la demande est passée.")

    d.regle('Le jour ouvrable',
            "Dix jours ouvrables, ce sont deux semaines complètes.",
            precision="Les samedis, les dimanches et les jours fériés ne comptent pas. "
                      "Une demande envoyée un vendredi et traitée en dix jours ouvrables "
                      "revient le vendredi de la semaine suivante — pas le lundi d'après.",
            notes="Sortir un calendrier et compter avec le groupe. C'est un calcul que "
                  "personne ne fait, et qui explique beaucoup d'impatience inutile.")

    d.pratique('Pratique · 1 de 4', "Complétez avec le bon mot",
               "Un mot de la liste : joindre, jours ouvrables, onglet, approuver, catégorie.", [
        ("Pour être remboursé, il faut ______ une photo du reçu.", "joindre"),
        ("Le remboursement prend environ dix ______.", "jours ouvrables"),
        ("Cliquez sur l'______ Dépenses pour commencer.", "onglet"),
        ("Votre superviseur doit ______ la demande avant l'envoi aux finances.", "approuver"),
        ("Choisissez la bonne ______ dans le menu déroulant.", "catégorie"),
    ], corrige=True,
       notes="Exercice de reconnaissance. Enchaîner tout de suite sur les verbes, qui "
             "sont plus difficiles.")

    d.pratique('Pratique · 2 de 4', "Le bon verbe",
               "Remplir, joindre, soumettre, approuver, signaler, réserver, vérifier, appuyer.", [
        ("N'oubliez pas de ______ votre reçu à la demande.", "joindre"),
        ("Il faut ______ le formulaire avant de l'envoyer.", "remplir"),
        ("Une fois le formulaire prêt, vous devez le ______.", "soumettre / envoyer"),
        ("Votre superviseur doit ______ votre demande.", "approuver"),
        ("Si l'équipement est brisé, il faut le ______ tout de suite.", "signaler"),
        ("Pour utiliser le camion, il faut d'abord le ______.", "réserver"),
    ], corrige=True,
       notes="Faire relire chaque phrase complète après correction. C'est la paire verbe "
             "+ complément qu'on installe, pas le verbe seul.")

    d.pratique('Pratique · 3 de 4', "Trois verbes de plus",
               "Vérifier, appuyer, oublier.", [
        ("N'______ pas votre reçu original avant d'avoir reçu le remboursement.", "oubliez"),
        ("Vous pouvez ______ le statut de votre demande dans l'application.", "vérifier / consulter"),
        ("Il faut ______ sur le bouton Envoyer pour terminer.", "appuyer"),
    ], corrige=True,
       notes="« Appuyer sur » est la formulation des applications québécoises. « Cliquer "
             "sur » s'emploie aussi. Les deux sont acceptés.")

    d.piege("Le piège du verbe interchangeable",
            "Je vais remplir mon reçu et joindre le formulaire.",
            "Je vais remplir le formulaire et joindre mon reçu.",
            "On remplit ce qui a des cases vides : un formulaire, une demande, un champ. "
            "On joint ce qui existe déjà : un reçu, une photo, un document. Inverser les "
            "deux rend la phrase incompréhensible pour un collègue pressé.",
            notes="Erreur fréquente et facile à corriger une fois nommée. Faire répéter "
                  "les deux paires à voix haute.")

    d.pratique('Pratique · 4 de 4', "Calculez le délai",
               "Dix jours ouvrables. Samedis, dimanches et fériés ne comptent pas.", [
        ("Demande envoyée un lundi.", "traitée le vendredi de la deuxième semaine"),
        ("Demande envoyée un vendredi.", "traitée le vendredi de la semaine suivante"),
        ("Demande envoyée un mercredi, avec un férié le lundi suivant.",
         "un jour de plus : le jeudi de la deuxième semaine"),
    ], corrige=True,
       notes="Faire le calcul sur un vrai calendrier, au tableau. Le troisième item "
             "montre pourquoi un délai « d'environ » n'est jamais exact.")

    d.billet(
        "Écrivez six phrases, une avec chacun des six verbes du module.",
        exemples=[
            "Remplir · joindre · soumettre · approuver · signaler · réserver.",
            "Chaque phrase doit contenir le bon complément.",
        ],
        notes="Corriger uniquement la paire verbe + complément. C'est le savoir de la "
              "séance ; le reste viendra plus tard.")

    return d.save(dossier)
