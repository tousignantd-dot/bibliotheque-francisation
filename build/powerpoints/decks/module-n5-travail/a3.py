# -*- coding: utf-8 -*-
"""A3 · Les seize mots du poste
Bloc A « Je découvre » · couleur framboise · 75 min. Vocabulaire.
Source : `fccards`, exercices `prVocab`, `prImg` et `prMots`.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n5-travail/images/')


def build(dossier):
    d = Deck(
        code='A3', section='framboise',
        titre="Les seize mots du poste",
        chapeau="Le programme ne fournit aucune liste de vocabulaire pour "
                "cette situation. Les seize mots viennent donc de ce que le "
                "poste exige vraiment : un comptoir, un téléphone, un "
                "appareil, un formulaire.",
        duree='75 minutes')

    d.titre(notes="Séance de vocabulaire. Commencer par la photo du babillard : demander "
                  "au groupe de nommer ce qu'on y voit. Les mots manquants sont ceux de "
                  "la séance. Ne pas donner la liste d'avance.")

    d.objectifs([
        "nommer les objets et les documents d'un poste d'accueil ;",
        "distinguer une tâche de directives ;",
        "distinguer les deux sens du mot « poste » ;",
        "employer chaque mot dans une phrase de travail.",
    ])

    d.declencheur(
        'Observation', "Un babillard couvert de feuilles. Qu'est-ce qui est "
                       "affiché là, dans un lieu de travail ?",
        image=IMG + 'babillard.jpg',
        pistes=[
            "Qu'est-ce qu'on y punaise, et qu'est-ce qu'on n'y punaise pas ?",
            "Y a-t-il un babillard à votre travail ? Où est-il ?",
            "Qui a le droit d'y afficher quelque chose ?",
            "Qu'est-ce qu'on y prend quand on veut demander un congé ?",
        ],
        notes="La quatrième piste amène le formulaire, qui est le mot du défi 3. La "
              "deuxième fait souvent sortir des exemples précis : le babillard de la "
              "cuisine, celui du vestiaire, celui du corridor.")

    d.vocabulaire('Vocabulaire · 1 de 4', "Le poste, les tâches, les directives", [
        ("l'accueil", "L'endroit d'un établissement où arrivent les gens et les appels."),
        ("une tâche", "Un travail précis à faire, qui a un début et une fin."),
        ("des directives", "Ce qu'on vous dit de faire, dans un ordre précis."),
        ("le registre des heures", "Le document où l'employeur inscrit les heures faites."),
    ], notes="Insister sur la paire tâche / directives : la tâche est ce qu'il y a à "
             "faire, les directives disent comment le faire. La liste des tâches change "
             "chaque semaine, les directives d'un appareil presque jamais.")

    d.vocabulaire('Vocabulaire · 2 de 4', "La boîte vocale et la note", [
        ("une boîte vocale", "Le service qui enregistre les appels quand personne ne répond."),
        ("un message d'accueil", "Les phrases enregistrées entendues avant de parler."),
        ("rappeler", "Téléphoner à son tour à quelqu'un qui a téléphoné avant."),
        ("une abréviation", "Un mot écrit plus court, pour aller plus vite."),
    ], notes="« Rappeler » a deux sens en français : téléphoner de nouveau, et remettre "
             "en mémoire. Ici, c'est le premier. Le préciser tout de suite évite une "
             "confusion au défi 1.")

    d.vocabulaire('Vocabulaire · 3 de 4', "Le matériel et son mode d'emploi", [
        ("un photocopieur", "L'appareil qui refait une copie d'une feuille."),
        ("un mode d'emploi", "Le texte qui explique comment se sert d'un appareil."),
        ("le bac à papier", "Le tiroir dans lequel on place les feuilles blanches."),
        ("un bourrage de papier", "Une feuille restée coincée, qui arrête l'appareil."),
    ], notes="Le bac à papier et le chargeur se confondent : le préciser dès maintenant "
             "avec un geste, un tiroir en bas et un plateau en haut. C'est le piège de la "
             "séance C2.")

    d.vocabulaire('Vocabulaire · 4 de 4', "La démarche, le congé, l'absence", [
        ("un formulaire", "Une feuille avec des cases à remplir et une place pour signer."),
        ("une autorisation d'absence", "La permission écrite de ne pas être au travail."),
        ("la paie", "Le service qui calcule les salaires, et le montant reçu."),
        ("une réponse automatique", "Le courriel qui repart tout seul pendant votre absence."),
    ], notes="« La paie » désigne à la fois le service et l'argent reçu : les deux emplois "
             "sont corrects et courants. Le dire, sinon les élèves croient qu'ils se "
             "trompent.")

    d.tableau('Un mot, deux sens', "Le mot « poste » au travail",
              ['Ce qu\'on dit', 'Ce que ça veut dire'],
              [["Elle a obtenu un poste permanent", "un emploi"],
               ["Faites le poste vingt-deux", "un numéro interne"],
               ["Je suis à mon poste", "à ma place de travail"],
               ["Elle est absente de son poste", "de son emploi, ce jour-là"]],
              cle=1,
              notes="Ce tableau règle une confusion réelle : dans le même immeuble, le "
                    "même mot désigne un emploi et un numéro de téléphone. Faire produire "
                    "une phrase de chaque sorte par le groupe.")

    d.piege("Confondre la tâche et les directives",
            "Ghislain m'a donné les directives du mois.",
            "Ghislain m'a donné les tâches du mois.",
            "Une tâche est ce qu'il y a à faire ; des directives disent comment le "
            "faire. On reçoit des tâches chaque semaine, et on suit toujours les mêmes "
            "directives.",
            notes="Faire chercher dans le dialogue de A1 les deux mots employés par "
                  "Ghislain. Il les emploie correctement, dans la même réplique.")

    d.pratique('Vocabulaire', "Le mot juste",
               "Complétez avec le mot qui convient.", [
        ("Le calendrier de l'équipe est punaisé au ___ .", "babillard"),
        ("Pour joindre le service technique, faites le ___ dix-neuf.", "poste"),
        ("Placez la feuille à copier dans le ___ , sur le dessus.", "chargeur"),
        ("Il n'y a plus de feuilles blanches : remplissez le ___ .", "bac à papier"),
        ("Ghislain vérifie le ___ des heures avant de répondre.", "registre"),
        ("Répondre au téléphone est sa première ___ de la journée.", "tâche"),
        ("Les ___ de l'appareil sont collées sur le mur.", "directives"),
        ("Depuis lundi, elle travaille à l' ___ de la coopérative.", "accueil"),
    ], cols=2, corrige=True,
       notes="Les huit énoncés sont ceux de l'exercice interactif. Faire répondre à "
             "l'oral, puis laisser les élèves les refaire seuls sur les postes.")

    d.billet(
        "Choisissez quatre mots de la séance et écrivez une phrase avec chacun.",
        exemples=[
            "Une phrase de votre travail à vous, pas de celui de Dorine.",
            "Si vous ne travaillez pas en ce moment, prenez un lieu que vous connaissez : "
            "une école, une clinique, un centre communautaire.",
        ],
        notes="Ramasser les billets et relever les phrases justes : elles serviront "
              "d'exemples au bloc B, et elles valent mieux que celles du module.")

    return d.save(dossier)
