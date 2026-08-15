# -*- coding: utf-8 -*-
"""C2 · Pendant que.
Bloc C · couleur ambre (écriture) · 60 min.
Source : exercice `t2pendant` et sa mini-leçon.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C2', section='ambre',
        titre='Pendant que',
        chapeau="Deux actions en même temps, une seule phrase. « Je remplis le "
                "formulaire pendant que tu prends la photo. » Deux personnes, deux "
                "tâches, et le travail avance deux fois plus vite.",
        duree='60 minutes')

    d.titre(notes="Écrire deux actions au tableau et demander comment les relier en une "
                  "phrase. Certains proposeront « et » : c'est correct mais cela ne dit "
                  "pas que c'est en même temps.")

    d.objectifs([
        "relier deux actions simultanées avec « pendant que » ;",
        "employer « pendant que » au présent, au passé et au futur ;",
        "distinguer « pendant » et « pendant que » ;",
        "écrire une phrase à deux sujets différents.",
    ])

    d.regle('La règle',
            "« Pendant que » relie deux actions qui se font en même temps.",
            precision="« Je remplis le formulaire pendant que tu prends la photo. » Deux "
                      "actions, deux sujets, un seul moment. « Pendant que » est "
                      "toujours suivi d'un sujet et d'un verbe conjugué.",
            notes="Écrire la règle au tableau. Le repère « suivi d'un sujet et d'un "
                  "verbe » distingue « pendant que » de « pendant ».")

    d.tableau('Analyse', "Aux trois temps",
              ['Le temps', 'La phrase'],
              [["présent", "Je remplis le formulaire pendant que tu prends la photo."],
               ["passé", "Pendant que je remplissais la demande, Diane a vérifié le montant."],
               ["futur", "Nous soumettrons la demande pendant que le superviseur sera au bureau."]],
              cle=0, props=[0.2, 0.8],
              note="La position de « pendant que » ne change rien : au début ou au "
                   "milieu, la phrase dit la même chose.",
              notes="Faire remarquer la virgule quand « pendant que » ouvre la phrase. "
                    "C'est la seule différence de ponctuation.")

    d.regle('Pendant, ou pendant que',
            "Pendant + un nom. Pendant que + un sujet et un verbe.",
            precision="« Pendant la réunion » — un nom. « Pendant que la réunion avait "
                      "lieu » — un sujet et un verbe. C'est exactement la même "
                      "distinction qu'entre « à cause de » et « parce que ».",
            notes="Lier au module 1, séance B2 : le motif est identique. Les élèves qui "
                  "l'ont vu là-bas le retrouveront ici sans effort.")

    d.cartes('En apprendre plus', "Quatre choses à savoir en plus", [
        ("Deux sujets différents",
         "« Pendant que » sert surtout quand les deux actions ont des sujets "
         "différents : je remplis, tu prends. Avec le même sujet, on préfère le "
         "gérondif — c'est la séance suivante."),
        ("Au passé, souvent l'imparfait",
         "« Pendant que je remplissais… » : l'action longue prend l'imparfait, "
         "l'action brève le passé composé. C'est le motif habituel."),
        ("« Pendant ce temps » sépare les phrases",
         "« Je remplis le formulaire. Pendant ce temps, tu prends la photo. » Même "
         "sens, deux phrases au lieu d'une."),
        ("« Tandis que » existe aussi",
         "Même sens, registre plus écrit. On le lit dans les directives, on le dit "
         "rarement."),
    ], notes="La deuxième carte annonce l'imparfait, qui n'a pas encore été enseigné. La "
             "mentionner sans l'exiger.")

    d.pratique('Pratique · 1 de 4', "Pendant ou pendant que ?",
               "Un nom, ou un sujet et un verbe ?", [
        ("___ la réunion, personne n'a parlé du remboursement.", "Pendant — un nom"),
        ("___ la réunion avait lieu, j'ai rempli ma demande.", "Pendant que — sujet et verbe"),
        ("Il a pris la photo ___ que j'inscrivais le montant.", "pendant"),
        ("___ dix jours ouvrables, la demande est en traitement.", "Pendant — un nom"),
    ], corrige=True,
       notes="Faire chercher le verbe conjugué avant de choisir. C'est le même test "
             "qu'au module 1 pour « parce que » et « à cause de ».")

    d.pratique('Pratique · 2 de 4', "Reliez les deux actions",
               "Employez « pendant que ». Choisissez le temps qui convient.", [
        ("expliquer la procédure / prendre des notes",
         "La commis explique la procédure pendant que Samuel prend des notes."),
        ("remplir le formulaire / chercher le reçu",
         "Je remplis le formulaire pendant que tu cherches le reçu."),
        ("attendre l'approbation / continuer le travail",
         "Il attend l'approbation pendant qu'il continue son travail."),
        ("vérifier le montant / téléverser la photo",
         "Diane vérifie le montant pendant que Samuel téléverse la photo."),
    ], corrige=True,
       notes="Le troisième item a le même sujet dans les deux moitiés. C'est correct, "
             "mais moins naturel : le signaler et annoncer le gérondif de C3.")

    d.piege("Le piège du « pendant » suivi d'une phrase",
            "Pendant je remplissais le formulaire, tu as pris la photo.",
            "Pendant que je remplissais le formulaire, tu as pris la photo.",
            "« Pendant » ne peut être suivi que d'un nom. Devant un sujet et un verbe, "
            "il faut « pendant que ». C'est la même règle qu'« à cause de » et « parce "
            "que », et c'est la même erreur.",
            notes="Faire relire les phrases de l'exercice précédent en vérifiant "
                  "uniquement la présence de « que ».")

    d.piege("Le piège de l'élision",
            "pendant que il continue son travail",
            "pendant qu'il continue son travail",
            "« Que » perd son e devant une voyelle, ici comme partout. « Pendant qu'il », "
            "« pendant qu'elle », « pendant qu'on ». C'est la même élision qu'au pronom "
            "« que » de la séance B2.",
            notes="Point rapide. Faire écrire les trois formes élidées au tableau et "
                  "passer.")

    d.pratique('Pratique · 3 de 4', "Complétez la phrase",
               "Le début est donné. Ajoutez la seconde action.", [
        ("Je prends la photo du reçu pendant que…", "…tu remplis le formulaire."),
        ("Pendant que le superviseur approuve la demande,…", "…je continue mon travail."),
        ("La commis vérifiera le dossier pendant que…", "…nous serons en réunion."),
        ("Pendant qu'il attendait l'approbation,…", "…il a rangé ses reçus."),
    ], corrige=True,
       notes="Accepter toute suite logique. Vérifier deux choses : un sujet, et un verbe "
             "conjugué.")

    d.pratique('Pratique · 4 de 4', "Décrivez votre journée de travail",
               "Trois phrases avec « pendant que ». Deux sujets différents chaque fois.", [
        ("Le matin", "Je prépare mon poste pendant que mon collègue ouvre l'entrepôt."),
        ("Pendant la journée", "Je remplis les formulaires pendant que la commis répond au téléphone."),
        ("En fin de journée", "Je range le matériel pendant que le superviseur vérifie les commandes."),
    ], corrige=True,
       notes="Les corrigés sont des modèles. Faire écrire des phrases réelles : les "
             "élèves qui travaillent en auront de meilleures que celles-ci.")

    d.billet(
        "Écrivez trois phrases avec « pendant que ».",
        exemples=[
            "Deux sujets différents dans chaque phrase.",
            "Une au présent, une au passé, une au futur.",
        ],
        notes="Corriger la présence de « que » et le verbe conjugué qui suit. Rendre "
              "avant C3, où le gérondif offrira l'autre solution.")

    return d.save(dossier)
