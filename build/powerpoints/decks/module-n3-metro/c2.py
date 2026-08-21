# -*- coding: utf-8 -*-
"""C2 · Poser sa question au comptoir.
Bloc C « Défi 2 · Demander au guichet » · couleur teal · 75 min.
Source : exercice `t2quest` et sa mini-leçon.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C2', section='teal',
        titre='Poser sa question au comptoir',
        chapeau="Le français pose ses questions de trois façons. Deux sont "
                "faciles, une est difficile. Au guichet, une seule suffit.",
        duree='75 minutes')

    d.titre(notes="Séance centrale du défi 2. Le programme de niveau 3 nomme "
                  "explicitement les phrases interrogatives parmi ses savoirs : c'est "
                  "elles qui rendent possible toute l'intention de production orale du "
                  "module. Ouvrir avec les questions écrites au billet de la séance B2.")

    d.objectifs([
        "poser une question avec « est-ce que » ;",
        "placer un mot de question devant « est-ce que » ;",
        "faire monter la voix quand on garde l'ordre normal ;",
        "poser les quatre questions du guichet sans hésiter.",
    ])

    d.regle("La façon la plus sûre, et la seule à retenir d'abord",
            "« Est-ce que je peux payer par carte ? »",
            precision="On pose « est-ce que » devant la phrase et on ne touche à "
                      "rien d'autre. L'ordre des mots ne change pas. Elle "
                      "fonctionne avec n'importe quelle phrase, sans exception, "
                      "et personne ne la trouvera bizarre.",
            notes="Diapositive à photographier. C'est le seul point de grammaire "
                  "vraiment indispensable du module. Faire transformer trois phrases "
                  "affirmatives du groupe en questions, à voix haute.")

    d.tableau('Analyse', "Les trois façons de poser une question",
              ["La façon", "Exemple"],
              [["la voix qui monte", "C'est combien ?"],
               ["avec est-ce que", "Est-ce que je peux payer comptant ?"],
               ["avec un mot de question", "Combien coûte le mensuel ?"]],
              cle=0,
              note="La deuxième marche partout. Commencez par elle.",
              notes="Diapositive à photographier. Ne pas enseigner l'inversion "
                    "(« puis-je », « coûte-t-il ») : elle est au-dessus du niveau 3 et "
                    "ne sert à rien au comptoir.")

    d.tableau('Analyse', "Les mots de question",
              ["Le mot", "Ce qu'il demande"],
              [["combien", "le prix, le nombre"],
               ["où", "le lieu"],
               ["quand / jusqu'à quand", "le moment, la fin"],
               ["comment", "la façon de faire"]],
              cle=0,
              note="Ils se mettent devant « est-ce que », jamais après.",
              notes="Diapositive à photographier. Devant une voyelle, « est-ce que » "
                    "devient « est-ce qu' » : où est-ce qu'on fait la photo. Le faire "
                    "entendre plutôt que l'écrire.")

    d.tableau('Analyse', "Les quatre questions du guichet",
              ["Ce qu'on veut savoir", "La question"],
              [["le prix", "Combien coûte le mensuel ?"],
               ["la durée", "Jusqu'à quand c'est bon ?"],
               ["le lieu", "Où est-ce qu'on fait la photo ?"],
               ["la permission", "Est-ce que je peux payer par carte ?"]],
              cle=1,
              note="Ces quatre-là couvrent presque tout un achat.",
              notes="Diapositive à photographier. Les faire apprendre par cœur, "
                    "littéralement : quatre phrases, quatre soirs. C'est le devoir le "
                    "plus rentable du module.")

    d.piege('Grammaire',
            "« Est-ce que puis-je payer ? »",
            "« Est-ce que je peux payer ? »",
            "Après « est-ce que », la phrase reste exactement dans l'ordre "
            "normal : sujet, puis verbe. C'est justement pour cela qu'elle est "
            "facile. Mélanger les deux façons produit une phrase que personne "
            "ne dit.",
            notes="Erreur fréquente chez les élèves qui ont vu l'inversion ailleurs. "
                  "Poser la règle simplement : on choisit une façon, on ne les "
                  "additionne pas.")

    d.pratique('Grammaire', "Complétez la question",
               "Écrivez le mot qui manque.", [
        ("___ coûte le titre mensuel ?", "Combien"),
        ("___ est-ce qu'on fait la carte avec photo ?", "Où"),
        ("___ que je peux payer par carte ?", "Est-ce"),
        ("Jusqu'___ quand est-ce que ce titre est bon ?", "à"),
        ("Pouvez-vous ___ , s'il vous plaît ?", "répéter"),
        ("___ est-ce que je vous dois ?", "Combien"),
    ], corrige=True, cols=2,
       notes="C'est l'exercice 2 du défi 2. Faire relire chaque question complétée à "
             "voix haute, en montant la voix à la fin : la forme écrite ne suffit pas.")

    d.pratique('Répétition', "Six questions à avoir dans la bouche",
               "Écoutez, puis répétez en montant la voix à la fin.", [
        ("C'est combien ?", "la voix monte"),
        ("Est-ce que je peux payer comptant ?", "est-ce que"),
        ("Combien coûte le titre mensuel ?", "mot de question"),
        ("Où est-ce qu'on fait la carte avec photo ?", "est-ce qu' devant voyelle"),
        ("Jusqu'à quand est-ce que ce titre est bon ?", "la durée"),
        ("Pardon, pouvez-vous répéter, s'il vous plaît ?", "faire répéter"),
    ], corrige=True,
       notes="Répétition en chœur, puis en binômes : l'un pose la question, l'autre "
             "invente une réponse. Passer dans les rangées et corriger l'intonation "
             "plutôt que la grammaire.")

    d.billet(
        "Écrivez les quatre questions que vous poserez au comptoir.",
        exemples=[
            "Combien ___ ?",
            "Est-ce que je peux ___ ?",
        ],
        notes="Devoir court, mais c'est le plus utile du module : ces quatre questions "
              "serviront à la séance E1 et dans la vraie vie. Vérifier au ramassage que "
              "chacun en a bien quatre.")

    return d.save(dossier)
