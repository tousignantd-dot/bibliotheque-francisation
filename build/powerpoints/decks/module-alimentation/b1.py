# -*- coding: utf-8 -*-
"""B1 · Ça se garde combien de temps ?
Bloc B « Défi 1 · S'informer sur un produit » · couleur acier · 75 min.
Source : dialogue `t1`, exercices `t1vf` et `t1conserv`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B1', section='acier',
        titre='Ça se garde combien de temps ?',
        chapeau="Farida veut du poisson frais, mais pas pour ce soir. Combien "
                "de temps ça se garde ? Où le mettre dans le frigo ? Trois "
                "questions qui évitent de jeter.",
        duree='75 minutes')

    d.titre(notes="Ouverture du bloc B. Question d'entrée : « qui a déjà jeté un aliment "
                  "parce qu'il ne savait pas combien de temps le garder ? ». Beaucoup de "
                  "mains.")

    d.objectifs([
        "demander combien de temps un aliment se garde ;",
        "demander comment le conserver, et où ;",
        "demander d'où il vient et comment il se cuisine ;",
        "comprendre une réponse qui donne une durée et une condition.",
    ])

    d.declencheur(
        'Mise en situation', "Vous achetez du poisson frais un lundi. Vous le cuisinez jeudi. Est-ce possible ?",
        pistes=[
            "Combien de temps le poisson frais se garde-t-il au réfrigérateur ?",
            "Que faut-il faire si on ne le cuisine pas tout de suite ?",
            "Où le placer dans le réfrigérateur ?",
            "Comment savoir tout cela avant d'acheter ?",
        ],
        notes="Cinq minutes. La réponse est non — deux jours seulement. La dernière piste "
              "est la clé : il suffit de demander au comptoir.")

    d.dialogue('Dialogue · 1 de 3', "Combien de temps", [
        ("FARIDA", "J'aimerais acheter du poisson frais, mais je ne le cuisine pas ce soir.", True),
        ("JOHANNE", "Ça se garde deux jours au réfrigérateur, pas plus. Après, il faut le congeler.", True),
        ("FARIDA", "Et si je le congèle tout de suite ?", True),
        ("JOHANNE", "Trois mois, facilement. Emballez-le bien, sinon il sèche.", False),
    ], consigne="Écoutez d'abord, diapo masquée.",
       notes="« Ça se garde » : première apparition de la construction du bloc B. La "
             "signaler sans l'expliquer — c'est la séance B3.")

    d.dialogue('Dialogue · 2 de 3', "D'où ça vient, comment ça se cuisine", [
        ("FARIDA", "Est-ce qu'il y a de la truite aujourd'hui ?", True),
        ("JOHANNE", "Oui, de la truite d'élevage, du Québec. Il y a aussi du saumon, mais lui vient de l'Atlantique.", True),
        ("FARIDA", "Je prends de la truite. Elle est comment, à la cuisson ?", True),
        ("JOHANNE", "Plus délicate que le saumon. Ne la faites pas trop cuire : dix minutes suffisent.", False),
    ], notes="Trois « de la » dans quatre répliques. Les faire compter par le groupe : la "
             "forme sera expliquée en B2.")

    d.dialogue('Dialogue · 3 de 3', "Comment le conserver", [
        ("FARIDA", "Et pour la conserver, je fais quoi exactement ?", True),
        ("JOHANNE", "Vous la sortez du papier, vous la mettez dans un contenant fermé, et vous la placez dans le bas du frigo.", True),
        ("FARIDA", "Dans le bas, d'accord. Pourquoi le bas ?", True),
        ("JOHANNE", "C'est l'endroit le plus froid. Et ça évite que le jus coule sur le reste.", False),
    ], notes="« Je fais quoi exactement ? » est la question qui obtient trois étapes "
             "précises. Le mot « exactement » revient encore : c'est un fil du module.")

    d.tableau('Analyse', "Les quatre questions du comptoir",
              ['La question', "Ce qu'elle évite"],
              [["Ça se garde combien de temps ?", "de jeter"],
               ["Comment le conserver ?", "de le perdre en deux jours"],
               ["Ça vient d'où ?", "d'acheter sans savoir"],
               ["C'est comment à la cuisson ?", "de rater le plat"]],
              cle=0,
              note="Quatre questions, quatre pertes évitées. Aucune n'est indiscrète.",
              notes="Diapo centrale. Faire recopier : c'est la liste de vérification du bloc.")

    d.cartes('Les durées à connaître', "Ce qui se garde le moins longtemps", [
        ("Le poisson frais et le bœuf haché",
         "Deux jours au réfrigérateur. Ce sont les deux aliments les plus fragiles du "
         "comptoir."),
        ("Le jambon tranché, une fois ouvert",
         "Trois jours, dans un contenant fermé."),
        ("Les viandes en morceaux",
         "Trois à cinq jours, selon la coupe. Toujours dans le bas du frigo."),
        ("Au congélateur",
         "Trois mois pour le poisson, jusqu'à six mois pour la viande — à condition d'être "
         "bien emballé."),
    ], notes="Faire noter ces durées : elles ne s'inventent pas et elles évitent de vrais "
             "gaspillages.")

    d.regle("Le bas du réfrigérateur",
            "C'est l'endroit le plus froid — et celui où le jus ne coule sur rien.",
            precision="La viande et le poisson vont en bas, toujours. Deux raisons : c'est "
                      "plus froid, et si l'emballage fuit, rien ne tombe sur les autres "
                      "aliments. C'est une règle d'hygiène de base, rarement expliquée.",
            notes="Diapo à photographier. Beaucoup d'élèves rangent la viande sur la "
                  "tablette du haut, où il fait le moins froid.")

    d.piege("Acheter sans demander",
            "Je le cuisinerai dans trois ou quatre jours.",
            "Ça se garde combien de temps ?",
            "Le poisson frais tient deux jours. Acheter le lundi pour cuisiner le jeudi "
            "veut dire jeter — ou congeler tout de suite, ce qui n'est possible que si on "
            "le sait le lundi.",
            notes="Le calcul est concret : le prix du poisson jeté vaut plusieurs fois le "
                  "temps de la question.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après le dialogue.", [
        ("Le poisson frais se garde deux jours au réfrigérateur.", "vrai"),
        ("Congelé, il se garde environ trois mois.", "vrai"),
        ("On peut le congeler dans son papier.", "faux — il faut bien l'emballer"),
        ("La truite vendue ce jour-là vient de l'Atlantique.", "faux — du Québec"),
        ("La truite demande une cuisson plus longue que le saumon.", "faux — plus délicate"),
        ("Il faut la placer dans le bas du réfrigérateur.", "vrai"),
    ], corrige=True,
       notes="Faire justifier chaque « faux » par la réplique exacte.")

    d.billet(
        "Notez trois aliments que vous achetez souvent et combien de temps ils se gardent.",
        exemples=[
            "Si vous ne savez pas, écrivez la question que vous poserez au comptoir.",
            "Indiquez aussi où vous les rangez dans le réfrigérateur.",
        ],
        notes="Ramasser. Ces questions servent au jeu de rôle de E1.")

    return d.save(dossier)
