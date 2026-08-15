# -*- coding: utf-8 -*-
"""B2 · La question avec pronom de reprise.
Bloc B · couleur ambre (écriture) · 75 min.
Source : exercices `pr6` et `pr7` et leur mini-leçon.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B2', section='ambre',
        titre='Le bail commence-t-il ?',
        chapeau="« Le bail commence-t-il le 1er septembre ? » Le nom reste devant, un "
                "pronom le reprend après le verbe. C'est la question polie de l'écrit — "
                "et celle qu'on lit dans tous les formulaires.",
        duree='75 minutes')

    d.titre(notes="Écrire au tableau « Est-ce que le bail commence le 1er septembre ? » "
                  "et « Le bail commence-t-il le 1er septembre ? ». Demander laquelle on "
                  "écrirait dans un courriel.")

    d.objectifs([
        "construire une question avec un pronom de reprise ;",
        "choisir entre il, elle, ils et elles ;",
        "ajouter le t quand le verbe se termine par e ou a ;",
        "reconnaître cette construction à la lecture.",
    ])

    d.regle('La règle',
            "Le nom reste devant le verbe, un pronom le reprend après, avec un trait d'union.",
            precision="« Le bail commence-t-il ? » Le groupe sujet « le bail » ne bouge "
                      "pas ; « il » le reprend juste après le verbe. C'est une "
                      "construction de l'écrit soigné et des formulaires.",
            notes="Écrire la formule au tableau : NOM + verbe + trait d'union + PRONOM. "
                  "Elle vaut pour tous les exercices.")

    d.tableau('Analyse', "Le pronom reprend le nom",
              ['La question', 'Le pronom', 'Il reprend'],
              [["Le bail commence-t-il ?", "il", "le bail"],
               ["La buanderie est-elle au sous-sol ?", "elle", "la buanderie"],
               ["Les chats sont-ils acceptés ?", "ils", "les chats"],
               ["Les fenêtres donnent-elles sur la cour ?", "elles", "les fenêtres"]],
              cle=1, props=[0.5, 0.16, 0.34],
              note="Le pronom s'accorde en genre et en nombre avec le nom qu'il "
                   "reprend — comme un adjectif.",
              notes="Faire nommer le genre et le nombre du nom avant de choisir le "
                    "pronom. C'est mécanique.")

    d.regle("Le t qui s'ajoute",
            "Si le verbe se termine par e ou a, on insère un t entre deux traits d'union.",
            precision="« La boulangerie ouvre-t-elle à cinq heures ? » « Le camion "
                      "arrive-t-il avant six heures ? » Sans ce t, deux voyelles se "
                      "heurteraient. Il ne veut rien dire : il sert seulement à séparer.",
            notes="Le mot savant est « t euphonique ». Ne pas l'employer : dire "
                  "simplement que c'est un t de liaison.")

    d.cartes('En apprendre plus', "Quatre choses à savoir en plus", [
        ("Trois façons de poser la même question",
         "« Est-ce que le bail commence… ? » à l'oral. « Le bail commence-t-il… ? » à "
         "l'écrit. « Le bail commence le 1er septembre ? » entre proches."),
        ("Le t seulement après e ou a",
         "Commence-t-il, arrive-t-il, ouvre-t-elle. Mais : commencent-ils (déjà un t), "
         "sont-ils, ont-ils."),
        ("Les traits d'union",
         "Deux traits d'union quand il y a un t : arrive-t-il. Un seul quand il n'y en "
         "a pas : sont-ils."),
        ("Où on la rencontre",
         "Dans les formulaires, les baux, les lettres officielles. On la lit beaucoup "
         "plus qu'on ne la produit — et il faut la comprendre."),
    ], notes="La quatrième carte remet la construction à sa place : c'est d'abord une "
             "compétence de lecture.")

    d.pratique('Pratique · 1 de 4', "Quel pronom reprend le nom ?",
               "Genre et nombre du nom.", [
        ("Le bail commence-t-il le 1er septembre ?", "il — le bail"),
        ("Les chats sont-ils acceptés dans l'immeuble ?", "ils — les chats"),
        ("La buanderie est-elle au sous-sol ?", "elle — la buanderie"),
        ("Les fenêtres de la chambre donnent-elles sur la cour ?", "elles — les fenêtres"),
        ("Le camion de farine arrive-t-il avant six heures ?", "il — le camion"),
        ("Ginette fournit-elle la peinture du salon ?", "elle — Ginette"),
    ], corrige=True,
       notes="Faire souligner le nom repris dans chaque question. Il est toujours au "
             "début, avant le verbe.")

    d.pratique('Pratique · 2 de 4', "Complétez avec le bon pronom",
               "Regardez le nom sujet.", [
        ("Le loyer comprend-___ le chauffage ?", "il"),
        ("La boulangerie ouvre-t-___ à cinq heures ?", "elle"),
        ("Les voisins entendent-___ le camion de farine ?", "ils"),
        ("Les places de stationnement sont-___ déneigées l'hiver ?", "elles"),
        ("Le logement se situe-t-___ au deuxième étage ?", "il"),
    ], corrige=True,
       notes="Faire remarquer les deux items avec un t : ouvre et situe se terminent par "
             "e. C'est le critère.")

    d.piege("Le piège du t manquant",
            "La boulangerie ouvre-elle à cinq heures ?",
            "La boulangerie ouvre-t-elle à cinq heures ?",
            "« Ouvre » se termine par e, « elle » commence par une voyelle : sans le t, "
            "les deux se heurtent et le mot devient impossible à dire. Le t ne veut rien "
            "dire : il sépare, comme le « n' » de « je n'ai pas ».",
            notes="Faire dire la version fautive à voix haute : le groupe entendra "
                  "lui-même que ça ne fonctionne pas.")

    d.piege("Le piège du t en trop",
            "Les chats sont-t-ils acceptés ?",
            "Les chats sont-ils acceptés ?",
            "« Sont » se termine déjà par un t : il n'y a rien à ajouter. Le t "
            "supplémentaire ne s'insère qu'après un e ou un a. Vérifiez la dernière "
            "lettre du verbe avant d'écrire.",
            notes="Faire classer six verbes selon leur dernière lettre. La règle devient "
                  "visible en deux minutes.")

    d.pratique('Pratique · 3 de 4', "Avec ou sans t ?",
               "Regardez la dernière lettre du verbe.", [
        ("Le bail commence___il le 1er septembre ?", "-t-il — commence finit par e"),
        ("Les chats sont___ils acceptés ?", "-ils — sont finit déjà par t"),
        ("La propriétaire fournit___elle la peinture ?", "-elle — fournit finit par t"),
        ("Le camion arrive___il tôt ?", "-t-il — arrive finit par e"),
        ("Les voisins ont___ils déjà déménagé ?", "-ils — ont finit par t"),
    ], corrige=True,
       notes="Cinq items, deux avec le t. Faire nommer la dernière lettre du verbe à voix "
             "haute avant chaque réponse.")

    d.pratique('Pratique · 4 de 4', "Transformez la question",
               "De « est-ce que » vers le pronom de reprise.", [
        ("Est-ce que le bail dure douze mois ?", "Le bail dure-t-il douze mois ?"),
        ("Est-ce que les électroménagers sont fournis ?",
         "Les électroménagers sont-ils fournis ?"),
        ("Est-ce que la cour est clôturée ?", "La cour est-elle clôturée ?"),
        ("Est-ce que les places sont déneigées ?", "Les places sont-elles déneigées ?"),
    ], corrige=True,
       notes="Ces quatre questions sont celles qu'on écrit dans un courriel à une "
             "propriétaire. Les faire copier dans le cahier.")

    d.billet(
        "Écrivez quatre questions avec un pronom de reprise.",
        exemples=[
            "Une avec il, une avec elle, une avec ils, une avec elles.",
            "Au moins une doit avoir un t entre deux traits d'union.",
        ],
        notes="Corriger le pronom et le t. Rendre avant B4 : ces questions seront posées "
              "à voix haute dans le jeu de rôle.")

    return d.save(dossier)
