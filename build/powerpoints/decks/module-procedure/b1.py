# -*- coding: utf-8 -*-
"""B1 · Samuel et la commis aux finances.
Bloc B · couleur acier (compréhension orale) · 60 min.
Source : dialogue `t1` et exercice `t1vf`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B1', section='acier',
        titre='Samuel et la commis aux finances',
        chapeau="Six répliques pour obtenir toute la procédure. Samuel pose trois "
                "questions, et chacune produit une information qu'il n'aurait pas eue "
                "autrement.",
        duree='60 minutes')

    d.titre(notes="Ouverture du défi 1. Rappeler ce que Diane a expliqué en A1. Ici, "
                  "Samuel vérifie auprès de la source officielle : ce n'est pas une "
                  "répétition, c'est une bonne pratique.")

    d.objectifs([
        "comprendre une explication de procédure donnée par un service ;",
        "repérer ce qui est obligatoire et ce qui ne l'est pas ;",
        "poser une question sur un délai ;",
        "savoir pourquoi il vaut mieux vérifier auprès du service concerné.",
    ])

    d.dialogue('Dialogue · 1 de 3', "J'aimerais savoir comment faire", [
        ("SAMUEL", "Bonjour, j'aimerais savoir comment faire une demande de "
                   "remboursement pour du matériel de sécurité.", True),
        ("LA COMMIS", "Bonjour. Vous devez remplir le formulaire dans l'application "
                      "Ressources+, sous l'onglet Dépenses.", True),
    ], consigne="Écoutez d'abord l'enregistrement, diapo masquée. Lisez ensuite.",
       notes="Passer l'audio du défi 1. Faire relever la formule de Samuel : "
             "« j'aimerais savoir comment faire ». C'est la question à retenir de tout "
             "le module.")

    d.dialogue('Dialogue · 2 de 3', "Est-ce que je dois joindre mon reçu ?", [
        ("SAMUEL", "D'accord. Est-ce que je dois joindre mon reçu ?", True),
        ("LA COMMIS", "Oui, une photo claire du reçu est obligatoire, sinon la demande "
                      "est refusée.", True),
    ], notes="La réponse contient deux choses : l'obligation et la conséquence. Faire "
             "remarquer que la conséquence n'était pas demandée — et qu'elle est ce qui "
             "compte le plus.")

    d.dialogue('Dialogue · 3 de 3', "Combien de temps faut-il ?", [
        ("SAMUEL", "Combien de temps faut-il pour recevoir le remboursement ?", True),
        ("LA COMMIS", "Environ dix jours ouvrables, une fois que votre superviseur a "
                      "approuvé la demande.", True),
    ], notes="« Une fois que votre superviseur a approuvé » : le délai ne commence pas "
             "tout de suite. C'est la nuance que tout le monde manque.")

    d.tableau('Analyse', "Trois questions, six informations",
              ['La question de Samuel', 'Ce qu\'il obtient'],
              [["Comment faire une demande ?", "l'application, et l'onglet exact"],
               ["Dois-je joindre mon reçu ?", "obligatoire, et la conséquence si on oublie"],
               ["Combien de temps ?", "dix jours ouvrables, et à partir de quand"]],
              cle=0, props=[0.4, 0.6],
              notes="Trois questions, six informations : chaque réponse en contient deux. "
                    "C'est ce qui distingue une bonne réponse de service.")

    d.regle('La règle du défi 1',
            "On demande comment faire, on vérifie ce qui est obligatoire, on demande le délai.",
            precision="Trois questions suffisent pour n'importe quelle procédure. Elles "
                      "fonctionnent au travail, à la banque, au centre de services "
                      "scolaires, partout.",
            notes="Écrire les trois au tableau. Ce sont celles de l'exercice oral de B4, "
                  "et elles reviennent dans le module 4 entier.")

    d.cartes('Ouvrir la mini-leçon', "Quatre choses à savoir en plus", [
        ("Vérifiez toujours à la source",
         "Un collègue peut se tromper ou donner une information périmée. Le service "
         "concerné a la version officielle."),
        ("Demandez le nom de la personne",
         "« À qui est-ce que je parle ? » Si la demande est refusée plus tard, vous "
         "saurez qui vous avait dit quoi."),
        ("Notez la date de l'appel",
         "Les procédures changent. Savoir quand on a demandé permet de dire « on m'a "
         "dit le 3 mars que… »"),
        ("Demandez une confirmation écrite",
         "« Pourriez-vous me l'envoyer par courriel ? » Une procédure écrite ne se "
         "discute pas."),
    ], notes="La quatrième carte est la plus utile et la moins connue. Beaucoup d'élèves "
             "ne savent pas qu'on peut demander cela.")

    d.pratique('Pratique · 1 de 3', "Vrai ou faux — la demande de remboursement",
               "Répondez sans relire le dialogue.", [
        ("Le formulaire se trouve dans l'application Ressources+.", "VRAI"),
        ("Il n'est pas obligatoire de joindre une photo du reçu.", "FAUX — c'est obligatoire"),
        ("Samuel va recevoir son remboursement dans les 48 heures.",
         "FAUX — environ dix jours ouvrables"),
        ("Le formulaire se trouve sous l'onglet Dépenses.", "VRAI"),
        ("Le délai commence dès l'envoi de la demande.",
         "FAUX — après l'approbation du superviseur"),
    ], corrige=True,
       notes="Le cinquième énoncé n'est pas dans l'exercice du module : il est ajouté "
             "ici parce que c'est la nuance la plus souvent manquée.")

    d.pratique('Pratique · 2 de 3', "Obligatoire ou facultatif ?",
               "Et quelle est la conséquence ?", [
        ("La photo du reçu.", "obligatoire — sinon la demande est refusée"),
        ("Le montant exact.", "obligatoire — un montant approximatif fait refuser"),
        ("La catégorie de dépense.", "obligatoire — elle détermine le budget"),
        ("Garder le reçu original.", "fortement conseillé — au cas où on le redemande"),
        ("Appeler pour vérifier avant d'envoyer.", "facultatif — mais cela évite les erreurs"),
    ], corrige=True,
       notes="Faire remarquer que « fortement conseillé » et « facultatif » ne sont pas "
             "la même chose. La nuance compte dans une consigne de travail.")

    d.piege("Le piège du délai mal compris",
            "J'ai envoyé ma demande lundi, je serai payé dans dix jours.",
            "Dix jours ouvrables après l'approbation de mon superviseur.",
            "Le délai ne commence pas à l'envoi : il commence à l'approbation. Si le "
            "superviseur est en vacances une semaine, il faut ajouter cette semaine. "
            "Vérifiez le statut de la demande dans l'application plutôt que de compter "
            "les jours.",
            notes="Faire calculer un exemple concret au tableau : envoi le 3, approbation "
                  "le 10, versement autour du 24.")

    d.pratique('Pratique · 3 de 3', "Posez les trois questions",
               "Pour chaque procédure, écrivez les trois questions à poser.", [
        ("Obtenir un remboursement de frais de déplacement.",
         "Comment faire ? Qu'est-ce qui est obligatoire ? Quel est le délai ?"),
        ("Demander un congé sans solde.",
         "Comment faire ? Quels documents ? Combien de temps à l'avance ?"),
        ("Réserver une salle de réunion.",
         "Comment faire ? Faut-il une approbation ? Combien de temps à l'avance ?"),
    ], corrige=True,
       notes="Les trois questions sont toujours les mêmes, seul le vocabulaire change. "
             "C'est ce qui les rend utiles : elles se transfèrent partout.")

    d.billet(
        "Écrivez les trois questions à poser pour comprendre une procédure.",
        exemples=[
            "Une par ligne, formulées comme vous les diriez vraiment.",
            "Ajoutez une quatrième ligne : ce que vous demanderiez par écrit.",
        ],
        notes="Ces trois questions serviront en B4, où elles seront posées à voix haute "
              "dans un jeu de rôle.")

    return d.save(dossier)
