# -*- coding: utf-8 -*-
"""B4 · Dans la soute, ou avec moi ?
Bloc B « Défi 1 » · couleur ambre · 75 min. Écriture, puis récapitulation.
Source : exercices `t1bag` et `t1red`, mini-leçon des bagages.
"""
import os
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n5-quebec/vocab/')


def img(nom):
    chemin = IMG + nom
    return chemin if os.path.exists(chemin) else None


def build(dossier):
    d = Deck(
        code='B4', section='ambre',
        titre="Dans la soute, ou avec moi ?",
        chapeau="Deux bagages en soute par personne, plus un bagage à main "
                "de cinq kilos qu'on garde avec soi. Ce qui dépasse part par "
                "le service de messagerie et se paie au poids. Ce sont des "
                "règles précises, et elles se demandent avant de partir.",
        duree='75 minutes')

    d.titre(notes="Dernière séance du défi 1. Elle ferme le bloc en reprenant la "
                  "demande complète de B1, enrichie de tout ce qui a été vu depuis. "
                  "Prévoir vingt minutes à la fin pour la récapitulation : c'est la "
                  "partie qui sert au jeu de rôle de E1.")

    d.objectifs([
        "distinguer le bagage à main du bagage en soute ;",
        "comprendre une règle chiffrée dite à l'oral ;",
        "demander ce qu'on a le droit d'emporter ;",
        "reprendre sa demande complète, avec les bagages et le retour.",
    ], notes="Le deuxième objectif est un travail d'écoute pur : cinq kilos, cent "
             "quinze centimètres, deux bagages. Les chiffres dits vite sont ce que les "
             "élèves manquent le plus souvent.")

    d.declencheur(
        'Observation', "La trappe est ouverte. Qu'est-ce qui va là-dedans, "
                       "et qu'est-ce qui reste avec vous ?",
        image=img('soute.jpg'),
        pistes=[
            "Où mettriez-vous vos papiers et votre téléphone ?",
            "Où mettriez-vous une grosse valise de vêtements ?",
            "Qu'est-ce qu'on ne peut pas récupérer pendant le trajet ?",
            "Combien de bagages avez-vous le droit d'emporter, à votre avis ?",
        ],
        notes="La troisième piste est celle qui compte : ce qui va en soute est "
              "inaccessible pendant huit heures. Médicaments, papiers, chargeur et "
              "manteau restent avec soi. C'est un conseil de voyage autant qu'un point "
              "de langue.")

    d.tableau('Les règles', "Ce qu'on a le droit d'emporter",
              ['Le bagage', 'La règle'],
              [["En soute", "Deux par personne"],
               ["À main", "Un seul, cinq kilos"],
               ["Trop gros", "Par messagerie, au poids"],
               ["Le chargement", "Avant le départ, pas après"]],
              cle=1,
              notes="Ces chiffres sont ceux d'Orléans Express et ils sont réels. Les "
                    "prix, eux, ne sont pas dans le module : ils changent, et le module "
                    "apprend à les demander plutôt qu'à les retenir.")

    d.cartes("Ce qui reste avec soi", "Huit heures sans pouvoir ouvrir la soute", [
        ("Les papiers",
         "Billet, pièce d'identité, carte d'assurance maladie."),
        ("Les médicaments",
         "Tout ce qu'on prend à heure fixe."),
        ("Le manteau",
         "Il fait plus froid à Rimouski qu'à Montréal."),
        ("De quoi manger",
         "Les arrêts sont courts et ne tombent pas à l'heure des repas."),
    ], notes="Faire ajouter par le groupe ce qu'il mettrait d'autre. Les réponses "
             "diffèrent selon les pays d'origine et la discussion est bonne : elle fait "
             "parler de voyages réels, ce que le module cherche.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après le dialogue de la séance B1.", [
        ("On peut mettre deux valises en soute.", "vrai"),
        ("Le bagage à main peut peser dix kilos.", "faux — cinq kilos"),
        ("Ce qui dépasse voyage gratuitement.", "faux — au poids, par messagerie"),
        ("On peut ouvrir la soute pendant le trajet.", "faux — les valises se chargent avant"),
        ("Le tarif économique permet de changer la date.", "faux — c'est ferme"),
        ("Il faut se présenter vingt minutes avant.", "vrai"),
    ], corrige=True,
       notes="Faire justifier chaque réponse. La cinquième prépare la discussion de la "
             "récapitulation : payer dix-huit dollars de plus pour pouvoir changer une "
             "date est une décision, et elle se justifie.")

    d.regle("Votre demande, d'un seul tenant",
            "Où · quand · combien de temps · combien de personnes · les "
            "bagages · le retour.",
            precision="Six informations. C'est la version complète de la règle de "
                      "B1, et c'est celle du jeu de rôle.",
            notes="Diapositive à photographier. Rendre ici les billets de sortie de B1 : "
                  "chacun reprend sa phrase et y ajoute les deux informations qui "
                  "manquaient.")

    d.piege("Attendre d'être au comptoir pour décider",
            "Je verrai sur place ce que je prends comme tarif.",
            "Je sais avant d'arriver si je veux pouvoir changer ma date.",
            "Au comptoir, il y a quelqu'un derrière soi et on choisit vite. La "
            "seule question qui demande vraiment à être pesée — un tarif ferme ou "
            "un tarif qui se change — se décide tranquillement, la veille.",
            notes="Thuy prend le tarif modifiable et elle dit pourquoi : elle ne connaît "
                  "pas la région et ne sait pas ce qu'elle voudra faire. C'est un bon "
                  "raisonnement, et il se dit en une phrase.")

    d.pratique('Production', "Reprenez votre demande, complète",
               "Debout, deux par deux : l'un demande, l'autre est au comptoir.", [
        ("Avez-vous dit où vous allez, et dans quelle région ?", "sinon, le préposé cherche"),
        ("Avez-vous donné les deux dates ?", "départ et retour, en chiffres"),
        ("Avez-vous dit combien de personnes ?", "une seule phrase suffit"),
        ("Avez-vous demandé pour les bagages ?", "avant de payer, pas après"),
        ("Avez-vous répété l'heure et le quai ?", "c'est ce qui évite l'erreur"),
    ], corrige=True,
       notes="Faire changer les rôles à mi-parcours. Celui qui joue le préposé apprend "
             "autant : il voit ce qui lui manque pour répondre, et il le redemande.")

    d.billet(
        "Notez la question sur les bagages que vous poseriez pour votre propre voyage.",
        exemples=[
            "Une question précise, pas « c'est quoi les règles ? ».",
            "Pensez à ce que vous emporteriez vraiment.",
        ],
        notes="Ramasser les billets et les garder pour E1 : ils entrent tels quels dans "
              "le jeu de rôle avec l'assistant.")

    return d.save(dossier)
