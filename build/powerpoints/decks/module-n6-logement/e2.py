# -*- coding: utf-8 -*-
"""E2 · Le courriel, et le bilan
Bloc E « Je me lance » · couleur framboise · 75 min. Production écrite et bilan.
Source : bloc « Je me lance » du module — production écrite — et la section
« Je retiens des mots ». La tâche vient des **attentes de fin de cours** :
« il rédige un court texte en organisant ses idées à l'aide de paragraphes »
et « dans ses relations professionnelles, il rédige un courriel ou une lettre
en respectant les conventions habituelles ».
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='E2', section='framboise',
        titre="Le courriel, et le bilan",
        chapeau="Huit à douze phrases, trois paragraphes, un objet qui se "
                "comprend sans ouvrir le message. Puis on referme le "
                "dossier.",
        duree='75 minutes')

    d.titre(notes="Dernière séance du module. Rendre les billets de C2 et de C5 en "
                  "ouvrant : l'objet et la dernière phrase sont déjà écrits, il reste "
                  "à bâtir le milieu.")

    d.objectifs([
        "écrire un courriel en trois paragraphes séparés ;",
        "y placer le nom, l'adresse et les dates sans en oublier ;",
        "formuler la demande au conditionnel, avec une échéance ;",
        "évaluer ce qu'on sait faire à la fin du module.",
    ], notes="Le troisième objectif est le plus transférable : une demande au "
             "conditionnel avec une date sert à l'école, à la banque, au travail et "
             "au bureau du médecin.")

    d.declencheur(
        'Retour', "Relisez votre objet, écrit en B3. Le comprendriez-vous sans ouvrir le message ?",
        pistes=[
            "Y a-t-il un verbe conjugué ? Il ne devrait pas y en avoir.",
            "Combien de mots ? Cinq ou six suffisent.",
            "Le numéro du logement y est-il ?",
        ],
        notes="Faire corriger l'objet par le voisin avant d'écrire le reste. C'est "
              "deux minutes, et ça évite les objets vagues qu'on ne rattrape plus "
              "ensuite.")

    d.tableau('Le plan', "Trois paragraphes, trois travaux",
              ['Le paragraphe', 'Ce qu\'il contient'],
              [["Premier", "pourquoi vous écrivez, et à quel document"],
               ["Deuxième", "les faits : la personne, les dates, l'engagement"],
               ["Troisième", "ce que vous demandez, et pour quand"]],
              cle=0,
              note="Une ligne blanche entre les trois : le lecteur voit ce qu'on lui dit.",
              notes="Diapositive à photographier. Le même plan est à l'écran dans le "
                    "module, au-dessus du cadre de rédaction.")

    d.cartes('Modèles', "Une phrase pour ouvrir chaque paragraphe", [
        ("Premier", "« Monsieur Tardif, je vous transmets ci-joint mon avis de sous-location pour le logement 2, daté du 18 novembre. »"),
        ("Deuxième", "« La personne proposée est monsieur Nicolas Trudel, domicilié au 745, avenue du Bourg-Royal. La sous-location irait du 5 janvier au 28 juin, et je demeure responsable du loyer. »"),
        ("Troisième", "« Pourriez-vous me confirmer votre réponse par écrit d'ici le 3 décembre ? Il faut que cette réponse soit écrite pour que je puisse en tenir compte. »"),
        ("La signature", "« Farida Belkacem, logement 2, 418 555-0142. » Dans un immeuble de six logements, un prénom ne suffit pas."),
    ], notes="Ces phrases sont des modèles, pas un texte à recopier : le faire dire. "
             "Un courriel identique pour toute la classe ne sera corrigé par personne, "
             "et l'IA le remarquera aussi.")

    d.regle("Une demande sans date n'obtient rien",
            "« Quand vous pourrez » ne fait bouger personne.",
            precision="« Pourriez-vous me répondre d'ici le 3 décembre ? » "
                      "transforme une question en demande. La date n'est pas une "
                      "menace : c'est celle qui figure déjà dans votre avis, et la "
                      "rappeler évite au lecteur d'avoir à la chercher.",
            notes="Diapositive à photographier. Faire vérifier que la date écrite dans "
                  "le courriel est bien celle de l'avis : une incohérence de date "
                  "défait tout le dossier.")

    d.pratique('Autocorrection', "Ce que je vérifie avant d'envoyer",
               "Relisez une fois et cochez.", [
        ("Mon objet tient en cinq ou six mots, sans verbe conjugué.", "oui / à refaire"),
        ("J'ai nommé la personne à qui j'écris, suivie d'une virgule.", "oui / à refaire"),
        ("Mes trois paragraphes sont séparés par une ligne blanche.", "oui / à refaire"),
        ("J'ai écrit le nom, l'adresse et les deux dates.", "oui / à refaire"),
        ("Ma demande est au conditionnel, avec une échéance.", "oui / à refaire"),
        ("J'ai employé « il faut que » ou « je souhaite que » correctement.", "oui / à refaire"),
    ], corrige=False,
       notes="La même liste est dans le module, à côté du cadre de rédaction. La faire "
             "cocher sur papier d'abord : on relit mieux un texte imprimé qu'un texte "
             "à l'écran.")

    d.piege('Attention',
            "écrire ce qu'on pense du locateur",
            "écrire ce qu'on attend de lui",
            "Un jugement sur quelqu'un reste écrit et se retourne toujours. "
            "Une demande datée, elle, appelle une réponse. Ce n'est pas de la "
            "prudence excessive : c'est ce qui distingue un dossier qui avance "
            "d'une chicane qui s'enlise.",
            notes="Dernière mise en garde du module. Elle vaut pour tous les écrits "
                  "administratifs, et c'est souvent celle dont les élèves se "
                  "souviennent le plus longtemps.")

    d.vocabulaire('Bilan', "Les quatre mots qu'on emporte", [
        ("un avis", "Un écrit qui informe et qui fait partir un délai — jamais une demande de permission."),
        ("un délai", "Un temps qui commence à une date précise et qui finit à une date précise."),
        ("un motif sérieux", "Une raison qui regarde la personne ou le logement, et qui peut se montrer."),
        ("un accusé de réception", "La preuve de la date, et rien d'autre. C'est déjà l'essentiel."),
    ], notes="Terminer là-dessus : ces quatre mots servent bien au-delà du logement. "
             "Un avis, un délai, un motif et une preuve de date, c'est la charpente de "
             "presque toute démarche administrative au Québec.")

    d.billet(
        "Qu'est-ce que vous saurez faire, maintenant, que vous ne saviez pas faire il y a quatre semaines ?",
        exemples=[
            "Deux phrases.",
            "Pensez à un papier que vous n'auriez pas lu avant.",
        ],
        notes="Cinq minutes, et c'est la fin. Ces billets sont les meilleurs qu'on "
              "ramasse de tout le module : les garder pour la présentation du module "
              "suivant, ils disent mieux que n'importe quelle consigne à quoi ça sert.")

    return d.save(dossier)
