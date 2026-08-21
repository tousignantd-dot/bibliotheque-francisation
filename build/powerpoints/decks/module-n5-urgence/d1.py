# -*- coding: utf-8 -*-
"""D1 · L'étage, l'opération, le congé.
Bloc D « Défi 3 · L'étage et le congé » · couleur acier · 75 min.
Source : dialogue `t3`, exercices `t3vf` et `t3etapes`.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n5-urgence/images/')


def build(dossier):
    d = Deck(
        code='D1', section='acier',
        titre="L'étage, l'opération, le congé",
        chapeau="L'urgence est finie ; l'hospitalisation commence. Une "
                "chambre, des heures de visite, une opération, et une date "
                "de sortie que personne ne promet. C'est maintenant qu'on "
                "pose les questions du retour à la maison.",
        duree='75 minutes')

    d.titre(notes="Ouverture du défi 3. Trois jours ont passé depuis la nuit du bloc B. "
                  "Le dire : les élèves suivent le récit, et le saut de temps se signale.")

    d.objectifs([
        "comprendre ce qu'un médecin annonce sur une hospitalisation ;",
        "poser les questions du congé avant le jour du départ ;",
        "dire sa situation réelle : escalier, horaire, personne à la maison ;",
        "connaître les documents remis à la sortie.",
    ])

    d.declencheur(
        'Observation', "Une chambre, un lit, une marchette. Qu'est-ce qu'il faut "
                       "avoir réglé avant que cette personne rentre chez elle ?",
        image=IMG + 'chambre.jpg',
        pistes=[
            "Qui sera à la maison pendant la journée ?",
            "Y a-t-il un escalier ? Un ascenseur ?",
            "Qui va à la pharmacie, et quand ?",
            "Quand doit-on revenir à l'urgence ?",
        ],
        notes="Faire lister au tableau. La liste du groupe est presque toujours plus "
              "longue que celle qu'on croit : c'est l'argument de la séance.")

    d.dialogue('Dialogue · 1 de 3', "Ce qui s'est passé, et ce qui s'en vient", [
        ("DRE LAMONTAGNE", "Madame Quintero ? Docteure Lamontagne. Je m'occupe de "
                           "votre mère depuis son opération.", True),
        ("MARISOL", "Bonjour docteure. Comment est-ce qu'elle va ?", True),
        ("DRE LAMONTAGNE", "Bien. La radiographie a montré une fracture de la hanche, "
                           "et elle a été opérée hier matin. Tout s'est bien passé.", True),
        ("DRE LAMONTAGNE", "La fièvre est tombée : c'était une infection urinaire, on "
                           "la traite.", True),
    ], consigne="Écoutez d'abord, diapositive masquée.",
       notes="Faire remarquer que la fièvre du premier soir avait bien une cause. Le "
             "8-1-1 avait raison de dire que ça pouvait attendre le matin ; la chute, "
             "elle, n'était pas prévisible.")

    d.dialogue('Dialogue · 2 de 3', "La date qu'on ne promet pas", [
        ("MARISOL", "Elle va rester ici combien de temps ?", True),
        ("DRE LAMONTAGNE", "Trois ou quatre jours, si elle se lève avec la "
                           "physiothérapeute comme prévu. Elle sortira quand elle "
                           "marchera quinze pas avec une marchette.", True),
        ("MARISOL", "Et après ? Elle habite chez moi, mais je travaille de jour.", True),
        ("DRE LAMONTAGNE", "C'est exactement la question à poser aujourd'hui, et pas "
                           "le matin du congé. Une intervenante du CLSC passera vous "
                           "voir avant sa sortie.", True),
    ], notes="Le point pivot du défi : la sortie se prépare deux jours avant. Faire "
             "répéter la phrase de la docteure.")

    d.dialogue('Dialogue · 3 de 3', "L'escalier, et les visites", [
        ("MARISOL", "Il y a un escalier chez nous. C'est là qu'elle est tombée.", True),
        ("DRE LAMONTAGNE", "Dites-le-lui. Ça change tout : elle pourra demander une "
                           "barre d'appui et une évaluation à domicile.", True),
        ("DRE LAMONTAGNE", "Les visites sont de onze heures à vingt heures. Deux "
                           "personnes à la fois.", True),
        ("DRE LAMONTAGNE", "Au congé, vous recevrez un résumé, les ordonnances et le "
                           "rendez-vous de suivi. Notez vos questions d'ici là.", False),
    ], notes="« Dites-le-lui » reprend la construction à deux pronoms de la séance B4. "
             "La signaler en passant : elle est revenue toute seule.")

    d.regle("Le congé se prépare deux jours à l'avance",
            "Le matin du départ, tout va vite — et il est trop tard pour organiser.",
            precision="Le transport, l'escalier, les repas, qui sera à la maison : ces "
                      "questions se posent pendant l'hospitalisation, quand quelqu'un a "
                      "encore le temps d'y répondre.",
            notes="Diapositive à photographier. Ajouter le fait qui convainc : une "
                  "personne qui rentre sans que rien ne soit préparé revient souvent à "
                  "l'urgence dans la semaine.")

    d.cartes("Ce qu'on vous remet au départ", "Quatre choses, à demander par écrit", [
        ("Le résumé du séjour", "Ce qui s'est passé et ce qui a été fait."),
        ("Les ordonnances", "Les médicaments, et surtout ce qui change."),
        ("Le rendez-vous de suivi", "La date, et qui doit accompagner."),
        ("La demande de services", "Ce qui part vers le CLSC : aide, soins, évaluation "
                                   "du logement."),
    ], notes="Insister sur « par écrit » : personne ne retient huit consignes dites une "
             "fois, debout dans un corridor, en pleine émotion.")

    d.tableau('Les questions à poser', "Et pourquoi les poser tôt",
              ['La question', 'Pourquoi maintenant'],
              [["Quel jour prévoyez-vous le congé ?",
                "pour organiser le transport et le travail"],
               ["Est-ce qu'elle pourra monter un escalier ?",
                "parce que la chambre est à l'étage"],
               ["Qui va la voir à la maison ?",
                "pour que la demande au CLSC parte avant la sortie"],
               ["Est-ce que les médicaments changent ?",
                "pour aller à la pharmacie avant son arrivée"],
               ["Qu'est-ce qui doit m'inquiéter à la maison ?",
                "pour savoir quels signes ramènent à l'urgence"]],
              cle=0,
              notes="Suggérer de copier ces cinq questions dans le téléphone. Le jour du "
                    "congé, il n'y aura qu'à les lire.")

    d.piege("Cacher les difficultés du logement",
            "Non non, ça va aller, on s'organisera.",
            "Il y a un escalier, et je travaille de jour.",
            "Ce sont des faits, pas des plaintes, et ce sont eux qui déclenchent les "
            "services. Les taire par gêne les empêche.",
            notes="Point sensible : beaucoup de familles croient qu'avouer une difficulté "
                  "sera jugé. Dire clairement que c'est l'inverse.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après le dialogue.", [
        ("Amparo a été opérée d'une fracture de la hanche.", "vrai"),
        ("La fièvre venait d'une infection urinaire.", "vrai"),
        ("La docteure promet une date de sortie exacte.", "faux — trois ou quatre jours"),
        ("Une intervenante du CLSC passera avant la sortie.", "vrai"),
        ("Il faut attendre le matin du congé pour poser ses questions.", "faux — deux jours avant"),
        ("Les visites sont permises de onze heures à vingt heures.", "vrai"),
    ], corrige=True,
       notes="Faire justifier chaque « faux » par la réplique exacte.")

    d.billet(
        "Écrivez les trois questions que vous poseriez aujourd'hui, à la place de Marisol.",
        exemples=[
            "Une sur la date, une sur le logement, une sur ce qui doit inquiéter.",
            "Des questions complètes, avec « est-ce que » ou l'inversion.",
        ],
        notes="Ramasser : elles serviront d'exemples à la séance D2, où l'on mettra la "
              "réponse au futur simple.")

    return d.save(dossier)
