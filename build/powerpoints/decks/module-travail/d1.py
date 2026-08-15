# -*- coding: utf-8 -*-
"""D1 · Le courriel de Nour : les cinq parties.
Bloc D · couleur ambre (écriture) · 75 min.
Source : exercices `t3parties` et `t3jasmine`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='D1', section='ambre',
        titre='Les cinq parties du courriel',
        chapeau="Nour doit accompagner sa mère à un rendez-vous médical. Elle écrit à son "
                "enseignant plutôt que d'appeler — et son courriel suit un plan que tout "
                "message professionnel suit.",
        duree='75 minutes')

    d.titre(notes="Ouverture du défi 3. Demander pourquoi on écrit plutôt que d'appeler. "
                  "Réponses attendues : trace écrite, hors des heures d'ouverture, "
                  "possibilité de relire avant d'envoyer.")

    d.objectifs([
        "connaître les cinq parties d'un courriel professionnel ;",
        "écrire un objet court et précis ;",
        "annoncer le but du message dès la première phrase ;",
        "donner un moyen d'être joint.",
    ])

    d.tableau('Analyse', "Les cinq parties, dans l'ordre",
              ['La partie', 'Le contenu de Nour'],
              [["l'objet", "Retard demain matin"],
               ["la formule d'appel", "Bonjour Monsieur Simard,"],
               ["le but du message", "Je vous écris pour vous aviser que j'arriverai en retard."],
               ["la formule de politesse", "Merci de votre compréhension,"],
               ["la signature", "Nour Haidar"]],
              cle=0, props=[0.35, 0.65],
              notes="Cinq parties, contre six pour le message téléphonique : le courriel "
                    "n'a pas de salutation finale séparée. Le faire remarquer.")

    d.regle("La règle de l'objet",
            "L'objet dit de quoi il s'agit, en trois ou quatre mots.",
            precision="« Retard demain matin » : on sait tout avant d'ouvrir. « Bonjour » "
                      "ou « Question » ne disent rien et finissent au bas de la pile. "
                      "L'objet est la partie la plus lue d'un courriel.",
            notes="Faire écrire cinq objets au tableau, à partir de situations données. "
                  "Corriger la longueur : plus de six mots, c'est trop.")

    d.cartes('Analyse', "Le courriel de Nour, phrase par phrase", [
        ("Le but, en première phrase",
         "« Je vous écris pour vous aviser que j'arriverai en retard demain matin. » "
         "Le destinataire sait tout dès la première ligne."),
        ("La raison, en une phrase",
         "« Je dois accompagner ma mère à un rendez-vous médical tôt le matin. » Une "
         "seule phrase, sans détail inutile."),
        ("L'heure prévue, avec une réserve",
         "« Je prévois arriver vers 10 heures, selon la durée du rendez-vous. » "
         "L'heure ET l'incertitude : c'est honnête et c'est utile."),
        ("Le moyen d'être joint",
         "« Vous pouvez me joindre sur mon cellulaire, au 438 555-0182. » Sans "
         "numéro, on ne peut pas vous prévenir d'un changement."),
    ], notes="La troisième carte est celle qui distingue un bon courriel : annoncer une "
             "heure tout en disant qu'elle peut bouger.")

    d.pratique('Pratique · 1 de 4', "Associez la partie et son contenu",
               "Les cinq parties du courriel de Nour.", [
        ("L'objet", "Retard demain matin"),
        ("La formule d'appel", "Bonjour Monsieur Simard,"),
        ("Le but du message", "Je vous écris pour vous aviser que j'arriverai en retard."),
        ("La formule de politesse", "Merci de votre compréhension,"),
        ("La signature", "Nour Haidar"),
    ], corrige=True, cols=1,
       notes="Exercice de reconnaissance. Enchaîner tout de suite sur les questions de "
             "compréhension.")

    d.pratique('Pratique · 2 de 4', "Le message de Nour",
               "Relisez le courriel, puis répondez.", [
        ("Pour quelle raison Nour sera-t-elle en retard ?",
         "elle accompagne sa mère à un rendez-vous médical"),
        ("À quelle heure prévoit-elle arriver ?", "vers 10 heures"),
        ("Pour quelle raison cette heure peut-elle changer ?",
         "selon la durée du rendez-vous médical"),
        ("Comment l'enseignant peut-il la joindre ?", "sur son cellulaire, au 438 555-0182"),
    ], corrige=True,
       notes="La troisième question est la plus fine : elle porte sur la réserve, que "
             "beaucoup n'auront pas remarquée.")

    d.tableau('Analyse', "Cinq objets, bons et mauvais",
              ['Mauvais objet', 'Bon objet'],
              [["Bonjour", "Retard demain matin"],
               ["Question", "Documents pour l'inscription"],
               ["Urgent !!!", "Absence du 12 au 15 mars"],
               ["De la part de Karim", "Abandon du cours — Karim Haddad"],
               ["(vide)", "Demande de changement d'horaire"]],
              cle=1,
              note="Un bon objet contient un nom d'action et une date quand c'est "
                   "pertinent.",
              notes="Faire remarquer le dernier : un courriel sans objet est souvent "
                    "classé comme indésirable par le serveur.")

    d.piege("Le piège de l'objet vague",
            "Objet : Bonjour",
            "Objet : Retard demain matin — Nour Haidar",
            "Une secrétaire reçoit cinquante courriels par jour. « Bonjour » ne dit ni "
            "de quoi il s'agit ni si c'est urgent : le message attend. Un objet précis "
            "est lu et traité le jour même.",
            notes="Montrer une boîte de réception simulée au tableau, avec cinq objets "
                  "vagues et un précis. Demander lequel on ouvrirait en premier.")

    d.piege("Le piège du but caché à la fin",
            "Trois paragraphes d'explications, et la demande à la dernière ligne.",
            "Le but dans la première phrase, les détails ensuite.",
            "Un courriel professionnel se lit en diagonale. Si la demande arrive à la "
            "fin, elle risque de ne pas être lue du tout. On annonce d'abord, on "
            "explique ensuite — c'est l'inverse d'une lettre personnelle.",
            notes="Point culturel utile : dans plusieurs traditions épistolaires, on "
                  "prépare longuement avant de demander. Ici, c'est le contraire.")

    d.pratique('Pratique · 3 de 4', "Écrivez l'objet",
               "Trois ou quatre mots, précis.", [
        ("Vous serez en retard demain matin.", "Retard demain matin"),
        ("Vous serez absent du 12 au 15 mars.", "Absence du 12 au 15 mars"),
        ("Vous abandonnez le cours parce que vous déménagez.", "Abandon du cours — déménagement"),
        ("Vous voulez changer votre horaire de cours.", "Demande de changement d'horaire"),
        ("Vous envoyez votre billet médical.", "Billet médical — absence du 3 mars"),
    ], corrige=True,
       notes="Corriger la longueur avant le contenu. Plus de six mots, on coupe.")

    d.pratique('Pratique · 4 de 4', "Écrivez le courriel complet",
               "Les cinq parties. Le but en première phrase.", [
        ("La situation",
         "Vous accompagnez un proche à un rendez-vous médical demain matin et vous "
         "arriverez en retard."),
        ("À annoncer", "l'heure prévue, et qu'elle peut changer"),
        ("À ne pas oublier", "l'objet, votre nom complet et votre numéro"),
    ], corrige=False,
       notes="Vingt-cinq minutes d'écriture. Ramasser : ces courriels sont l'évaluation "
             "écrite du défi 3.")

    d.billet(
        "Écrivez les cinq parties d'un courriel, avec un exemple pour chacune.",
        exemples=[
            "Une ligne par partie.",
            "Vos exemples doivent tous parler de la même situation.",
        ],
        notes="Ce billet est la fiche de référence du défi 3. Suggérer de le garder dans "
              "le cahier pour E1.")

    return d.save(dossier)
