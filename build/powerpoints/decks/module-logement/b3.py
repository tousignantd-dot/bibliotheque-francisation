# -*- coding: utf-8 -*-
"""B3 · Reprendre un nom sans le répéter.
Bloc B · couleur ambre (écriture) · 60 min.
Source : exercice `pr5` et sa mini-leçon — la reprise par un groupe nominal.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B3', section='ambre',
        titre='Reprendre sans répéter',
        chapeau="« Ibrahim a visité un 4 ½. Ce 4 ½ lui plaît beaucoup. » Le même nom, "
                "un autre déterminant : c'est ainsi qu'un texte avance sans se répéter.",
        duree='60 minutes')

    d.titre(notes="Écrire deux phrases répétitives au tableau — « Ibrahim a visité un "
                  "logement. Le logement est au deuxième » — et demander ce qui gêne. Le "
                  "groupe le sentira.")

    d.objectifs([
        "reprendre un nom en changeant son déterminant ;",
        "passer de un, une, des à ce, cette, ces ;",
        "ne pas répéter l'expansion du nom ;",
        "écrire deux phrases qui s'enchaînent.",
    ])

    d.regle('La règle',
            "On reprend le nom en changeant seulement le déterminant.",
            precision="« un 4 ½ » devient « ce 4 ½ ». « une place » devient « cette "
                      "place ». « des fenêtres » devient « ces fenêtres ». Le nom ne "
                      "change pas ; le déterminant, oui.",
            notes="Écrire les trois transformations au tableau : un devient ce, une "
                  "devient cette, des devient ces. C'est toute la règle.")

    d.tableau('Analyse', "Trois déterminants qui changent",
              ['Première phrase', 'Reprise'],
              [["un 4 ½", "ce 4 ½"],
               ["une place de stationnement", "cette place"],
               ["des fenêtres neuves", "ces fenêtres"],
               ["un camion de farine", "ce camion"]],
              cle=1,
              note="Remarquez : l'expansion — « de stationnement », « neuves », « de "
                   "farine » — ne se répète pas dans la reprise.",
              notes="C'est le point le plus fin de la séance. Faire souligner l'expansion "
                    "dans la première colonne : elle disparaît dans la seconde.")

    d.cartes('En apprendre plus', "Quatre choses à savoir en plus", [
        ("Pourquoi ce, cette, ces",
         "Ces déterminants disent « celui dont je viens de parler ». Ils font le lien "
         "entre les deux phrases : sans eux, on ne saurait pas qu'il s'agit du même."),
        ("L'expansion ne se répète pas",
         "« Une place de stationnement dans la ruelle » devient « cette place ». Répéter "
         "« de stationnement dans la ruelle » alourdirait la phrase pour rien."),
        ("On peut aussi changer de mot",
         "« Un 4 ½ » peut devenir « ce logement » ou « cet appartement ». Le nom change, "
         "et c'est encore mieux : le texte se répète moins."),
        ("Le déterminant possessif aussi",
         "« Ibrahim a signé un bail. Son bail commence le 1er septembre. » « Son » fait "
         "le même travail que « ce »."),
    ], notes="La troisième carte ouvre sur une compétence plus fine. La montrer sans "
             "l'exiger : elle vient avec la pratique.")

    d.pratique('Pratique · 1 de 4', "Reprenez le nom",
               "Changez le déterminant, gardez le nom.", [
        ("Ibrahim a visité un 4 ½ au-dessus d'une boulangerie.", "Ce 4 ½ lui plaît beaucoup."),
        ("Ginette lui a montré une place de stationnement dans la ruelle.",
         "Cette place est réservée au locataire du deuxième."),
        ("Leyla a remarqué des fenêtres neuves dans la chambre.",
         "Ces fenêtres arrêtent bien le bruit."),
        ("Un camion de farine réveille parfois les voisins.",
         "Ce camion recule dans la ruelle vers cinq heures."),
    ], corrige=True,
       notes="Faire vérifier que l'expansion n'est pas répétée. C'est le seul point à "
             "corriger dans cet exercice.")

    d.pratique('Pratique · 2 de 4', "Deux de plus",
               "Même travail.", [
        ("Ibrahim va signer un bail de douze mois.", "Ce bail commence le 1er septembre."),
        ("La propriétaire fournit une peinture blanche pour le salon.",
         "Cette peinture couvre bien le vert olive."),
        ("Ibrahim a trouvé des rideaux épais au magasin.",
         "Ces rideaux bloquent la lumière du matin."),
    ], corrige=True,
       notes="Trois items, trois déterminants différents. Faire remarquer la régularité.")

    d.piege("Le piège de la répétition complète",
            "Ibrahim a visité un 4 ½ au-dessus d'une boulangerie. Ce 4 ½ au-dessus d'une boulangerie lui plaît.",
            "Ce 4 ½ lui plaît beaucoup.",
            "L'expansion a déjà été dite : la répéter alourdit la phrase sans rien "
            "ajouter. Le déterminant « ce » suffit à dire de quel logement on parle. "
            "C'est justement son rôle.",
            notes="Faire lire les deux versions à voix haute. La différence de fluidité "
                  "est immédiate.")

    d.piege("Le piège du déterminant inchangé",
            "Ibrahim a visité un 4 ½. Un 4 ½ lui plaît beaucoup.",
            "Ce 4 ½ lui plaît beaucoup.",
            "Garder « un » laisse croire qu'il s'agit d'un autre logement, quelconque. "
            "« Ce » dit qu'il s'agit du même, celui dont on vient de parler. Le "
            "déterminant porte à lui seul le lien entre les deux phrases.",
            notes="Erreur logique plus que grammaticale. Le sens change complètement, "
                  "et c'est ce qu'il faut faire sentir.")

    d.pratique('Pratique · 3 de 4', "Ce, cette ou ces ?",
               "Genre et nombre du nom.", [
        ("un bail", "ce bail"),
        ("une buanderie", "cette buanderie"),
        ("des électroménagers", "ces électroménagers"),
        ("un appartement", "cet appartement — devant une voyelle"),
        ("une annonce", "cette annonce"),
    ], corrige=True,
       notes="Le quatrième item introduit « cet » devant une voyelle. Le signaler : "
             "c'est la même logique que « mon » devant une voyelle.")

    d.pratique('Pratique · 4 de 4', "Écrivez deux phrases qui s'enchaînent",
               "La deuxième reprend un nom de la première.", [
        ("Sur un logement", "J'ai visité un 3 ½ rue Sherbrooke. Ce logement est très clair."),
        ("Sur un bail", "J'ai signé un bail de douze mois. Ce bail se termine en août."),
        ("Sur des voisins", "Des voisins habitent au-dessus. Ces voisins sont très tranquilles."),
        ("Sur une propriétaire", "Une propriétaire m'a fait visiter. Cette propriétaire est très franche."),
    ], corrige=True,
       notes="Faire vérifier trois choses : le déterminant a changé, le nom est repris, "
             "l'expansion n'est pas répétée.")

    d.billet(
        "Écrivez quatre phrases : deux paires qui s'enchaînent.",
        exemples=[
            "Dans chaque paire, la deuxième phrase reprend un nom de la première.",
            "Soulignez le déterminant qui a changé.",
        ],
        notes="Corriger le déterminant et la non-répétition de l'expansion. C'est le "
              "savoir de la séance.")

    return d.save(dossier)
