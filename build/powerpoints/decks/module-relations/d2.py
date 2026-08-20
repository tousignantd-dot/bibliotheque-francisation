# -*- coding: utf-8 -*-
"""D2 · La carte postale et la carte de vœux.
Bloc D · couleur ambre (écriture) · 90 min.
Source : mini-leçons `t3carte` et `t3cause`, exercices `t3carte`, `t3ordre`,
`t3cause` et `t3form`, dialogue `t3b`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='D2', section='ambre',
        titre='La carte postale et la carte de vœux',
        chapeau="Deux cartes, quelques lignes chacune, et deux buts opposés : "
                "l'une raconte où vous êtes, l'autre parle de la personne à qui "
                "vous écrivez. Se tromper de genre se remarque.",
        duree='90 minutes')

    d.titre(notes="Séance d'écriture, la plus longue du bloc D. Apporter si possible de "
                  "vraies cartes — une postale, une de vœux — à faire circuler.")

    d.objectifs([
        "distinguer une carte postale d'une carte de vœux ;",
        "écrire les quatre parties d'une carte postale ;",
        "employer la formule figée qui convient à l'occasion ;",
        "dire la cause avec grâce à ou à cause de, selon le résultat.",
    ])

    d.dialogue('Dialogue', 'Une carte pour Chantal', [
        ("MARIAMA", "Chez nous, on écrit toujours une carte quand un enfant naît. Est-ce que ça se fait ici ?", True),
        ("CHANTAL", "Oui, ça se fait beaucoup. Les gens en envoient pour les naissances, les mariages, le Nouvel An.", True),
        ("MARIAMA", "Et qu'est-ce qu'on écrit ? Je ne veux pas me tromper.", False),
        ("CHANTAL", "Pas grand-chose. Trois lignes suffisent : tu félicites, tu souhaites quelque chose, tu signes.", True),
    ], consigne="Écoutez, puis repérez la réponse à la question de Mariama.",
       notes="La question « est-ce que ça se fait ici ? » est celle que beaucoup d'élèves "
             "n'osent pas poser. La valoriser explicitement devant le groupe.")

    d.tableau('Analyse', "Deux cartes, deux buts",
              ['', 'Carte postale', 'Carte de vœux'],
              [["Le but", "raconter où je suis", "féliciter ou souhaiter"],
               ["De qui on parle", "de soi", "de l'autre"],
               ["Longueur", "quatre à six phrases", "trois lignes"],
               ["Temps des verbes", "présent et passé composé", "présent"]],
              cle=1,
              note="La deuxième ligne est le vrai test : parle-t-on de soi, ou de l'autre ?",
              notes="Diapo centrale. Faire recopier avant de passer à l'écriture.")

    d.cartes('La carte postale', "Ses quatre parties, dans l'ordre", [
        ("1 · La salutation",
         "« Bonjour Fatou, » ou « Chère Fatou, ». Une virgule, et on va à la ligne."),
        ("2 · Où je suis",
         "« Je t'écris de Québec, il neige depuis hier. » Au présent : c'est maintenant."),
        ("3 · Ce que j'ai fait",
         "« Hier, on a visité le Vieux-Port. » Au passé composé : les évènements du voyage."),
        ("4 · La fin",
         "« Tu me manques. Je t'embrasse. Mariama. » On signe de son prénom, sans formule "
         "longue."),
    ], notes="Les parties 2 et 3 réutilisent exactement le présent et le passé composé du "
             "bloc C. Le dire : rien de nouveau à apprendre ici, seulement à replacer.")

    d.tableau('Les formules figées', "Une occasion, une formule",
              ['Occasion', 'Ce qu\'on écrit'],
              [["Une naissance", "Bienvenue au petit ! Toutes nos félicitations."],
               ["Un mariage", "Beaucoup de bonheur à vous deux."],
               ["Le Nouvel An", "Meilleurs vœux pour la nouvelle année."],
               ["Un décès", "Mes sincères condoléances."]],
              cle=0,
              note="Ces formules ne s'inventent pas : on les réutilise telles quelles. "
                   "Il y en a une dizaine à connaître, pas plus.",
              notes="Bonne nouvelle à annoncer au groupe : c'est une liste finie. La faire "
                    "recopier et conserver.")

    d.regle('grâce à ou à cause de',
            "grâce à annonce un résultat heureux, à cause de un résultat ennuyeux.",
            precision="« Grâce à cette voisine, j'ai aimé l'hiver. » · « On est partis à "
                      "cause du bruit. » Les deux répondent à « pourquoi ? », mais ils ne "
                      "sont pas neutres. Le test : remplacez par heureusement ou "
                      "malheureusement.",
            notes="Écrire les deux phrases au tableau et faire trouver le test par le "
                  "groupe avant de le donner.")

    d.piege('Oublier la fusion',
            "à cause de le bruit · grâce à le covoiturage",
            "à cause du bruit · grâce au covoiturage",
            "de + le donne du, de + les donne des ; à + le donne au, à + les donne aux. "
            "La fusion est obligatoire en français : « de le » et « à le » n'existent "
            "jamais. C'est mécanique, et ça se corrige en une séance.",
            notes="Écrire les quatre fusions au tableau. Les laisser jusqu'à la fin du "
                  "module — elles servent partout.")

    d.pratique('Pratique · 1 de 2', "grâce à ou à cause de ?",
               "Complétez. Attention aux fusions.", [
        ("___ cette voisine, Mariama a aimé l'hiver.", "Grâce à"),
        ("Ils sont partis ___ bruit du bar.", "à cause du"),
        ("___ covoiturage, elle n'attend plus l'autobus.", "Grâce au"),
        ("Elle a manqué deux entraînements ___ son horaire.", "à cause de"),
        ("Le déménagement a été long ___ pluie.", "à cause de la"),
        ("___ ses coéquipières, elle s'est fait des amies.", "Grâce à"),
    ], corrige=True,
       notes="Faire dire le test à voix haute — heureusement ou malheureusement — avant "
             "chaque réponse.")

    d.pratique('Pratique · 2 de 2', "Postale ou vœux ?",
               "Dites de quelle carte vient chaque phrase.", [
        ("Nous sommes à Québec depuis deux jours et il neige sans arrêt.", "carte postale"),
        ("Félicitations à vous deux pour cette belle nouvelle !", "carte de vœux"),
        ("Hier, on a marché dans le Vieux-Port toute la journée.", "carte postale"),
        ("Je vous souhaite beaucoup de bonheur avec le petit.", "carte de vœux"),
        ("Il fait moins quinze, mais le soleil est magnifique.", "carte postale"),
    ], corrige=True, cols=1,
       notes="Appliquer le test de la deuxième ligne du tableau : parle-t-on de soi ou de "
             "l'autre ?")

    d.piege('Parler de soi sur une carte de vœux',
            "Félicitations ! Moi, cette année, j'ai déménagé et j'ai changé d'emploi.",
            "Félicitations ! Je vous souhaite beaucoup de bonheur avec le petit.",
            "La carte de vœux est tournée vers l'autre. Raconter sa propre année à "
            "l'occasion d'une naissance déplace l'attention au mauvais endroit. Gardez vos "
            "nouvelles pour une lettre ou un courriel.",
            notes="Faute très fréquente et jamais signalée aux élèves. C'est un point "
                  "culturel autant que linguistique.")

    d.billet(
        "Écrivez une carte : postale ou de vœux, à votre choix. Cinq à huit phrases.",
        exemples=[
            "Carte postale : les quatre parties, dans l'ordre.",
            "Carte de vœux : la formule de l'occasion, un souhait, votre prénom.",
            "Employez au moins une fois qui, que ou où, et un verbe au passé composé.",
        ],
        notes="C'est la production écrite du module. Ramasser, corriger, rendre avant E1 : "
              "les élèves reprendront ce texte dans l'activité interactive.")

    return d.save(dossier)
