# -*- coding: utf-8 -*-
"""C4 · Autrement dit, combien ?
Bloc C « Défi 2 » · couleur teal · écoute et réponds · 75 min.
Source : exercices `t2refo` et `t2prix`, mini-leçons `t2refo` et `t2prix`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C4', section='teal',
        titre="Autrement dit, combien ?",
        chapeau="« Terme minimal de douze mois » et « vous payez pendant un "
                "an même si vous cessez d'y aller » disent la même chose. La "
                "deuxième phrase est celle à écrire dans la marge.",
        duree='75 minutes')

    d.titre(notes="Dernière séance du Défi 2. Deux choses : reformuler en français "
                  "ordinaire, et calculer. La calculatrice est permise et même "
                  "recommandée.")

    d.objectifs([
        "reformuler une condition écrite en français ordinaire ;",
        "employer les connecteurs de reformulation à l'écrit et à l'oral ;",
        "connaître la règle du prix tout inclus et ses deux exceptions ;",
        "calculer le total réel d'une offre annoncée par semaine.",
    ], notes="Le troisième objectif est une règle de droit, à donner exactement : "
             "seules la TPS et la TVQ peuvent s'ajouter, rien d'autre.")

    d.declencheur(
        'Observation', "Que veut dire cette ligne, en français ordinaire ?",
        pistes=[
            "« Le tarif hebdomadaire est prélevé aux quatre semaines. »",
            "Combien de prélèvements y a-t-il dans une année ?",
            "Est-ce douze, comme un loyer ?",
            "Qu'est-ce que ça change au total ?",
        ],
        notes="Cinquante-deux semaines divisées par quatre : treize prélèvements, et "
              "non douze. Le groupe répond presque toujours douze, et la découverte "
              "vaut la séance.")

    d.tableau('Analyse', "Les connecteurs de reformulation",
              ['Le connecteur', 'Ce qu\'il annonce'],
              [["autrement dit", "ce qui suit répète, en plus clair"],
               ["c'est-à-dire", "même emploi, même place"],
               ["en d'autres mots", "même emploi, un peu plus long"],
               ["en somme, bref", "il reformule et il conclut"],
               ["si je comprends bien", "à l'oral, pour faire confirmer"]],
              cle=0,
              note="« En somme » ne se met pas au milieu : il annonce la fin.",
              notes="Diapositive à photographier. Le dernier est le plus utile au "
                    "téléphone, et il sera exigé dans l'appel de E1.")

    d.pratique('Pratique', "Traduisez la condition",
               "Écrivez ce que ça veut dire, en français ordinaire.", [
        ("Terme minimal de douze mois", "vous payez un an, même sans y aller"),
        ("Frais uniques exigibles à la signature", "une somme de plus, tout de suite"),
        ("Le tarif est prélevé aux quatre semaines", "treize fois par année, pas douze"),
        ("Les taxes ne sont pas comprises", "ajoutez environ quinze pour cent"),
        ("L'offre peut être modifiée sans préavis", "rien de ceci n'est garanti demain"),
        ("Certaines conditions s'appliquent", "des règles qu'on ne dira qu'en succursale"),
    ], corrige=True,
       notes="Exercice `t2refo` du module. Faire écrire les traductions dans la marge "
             "des vrais dépliants apportés en A3 : le geste doit devenir un réflexe.")

    d.regle("Le prix annoncé est le prix payé",
            "Au Québec, le prix qu'un commerçant annonce doit être le montant "
            "total à débourser. Seules la TPS et la TVQ peuvent s'ajouter.",
            precision="Frais d'administration, frais de dossier, frais de "
                      "préparation : tout doit être compris dans le prix affiché. Et "
                      "le prix total doit ressortir plus nettement que les montants "
                      "qui le composent.",
            notes="Diapositive à photographier. La dernière phrase vise exactement les "
                  "annonces qui affichent en gros un petit versement et en petit le "
                  "total.")

    d.tableau('Analyse', "Le calcul, pas à pas",
              ['L\'étape', 'Le montant'],
              [["9,99 $ par semaine", "le chiffre annoncé, en gros"],
               ["multiplié par 52", "519,48 $"],
               ["plus 60 $ d'adhésion", "579,48 $"],
               ["plus les taxes", "environ 666 $ la première année"],
               ["ce que l'annonce disait", "« neuf quatre-vingt-dix-neuf »"]],
              cle=0,
              notes="Diapositive à photographier. Faire refaire le calcul par le "
                    "groupe avant de la montrer : le résultat frappe plus quand on "
                    "l'a trouvé soi-même.")

    d.pratique('Pratique', "Faites le calcul",
               "Calculatrice permise. Répondez en chiffres ou en mots.", [
        ("9,99 $ par semaine sur cinquante-deux semaines ?", "519,48 $"),
        ("Plus les frais d'adhésion : total avant taxes ?", "579,48 $"),
        ("À quelle fréquence l'argent est-il vraiment prélevé ?", "aux quatre semaines"),
        ("Combien de prélèvements de quatre semaines dans une année ?", "treize"),
        ("Quelles taxes peuvent s'ajouter au prix annoncé ?", "la TPS et la TVQ"),
        ("Quitter avant le terme coûte combien de mensualités ?", "deux"),
    ], corrige=True,
       notes="Exercice `t2prix` du module. Le troisième item est celui qu'on oublie : "
             "le prix est annoncé par semaine et prélevé aux quatre semaines.")

    d.billet(
        "Prenez une offre vue cette semaine et calculez son total sur un an.",
        exemples=[
            "Un abonnement, un forfait, un service à la maison.",
            "Écrivez le chiffre annoncé et le chiffre réel, l'un sous l'autre.",
        ],
        notes="Devoir de calcul. Les deux chiffres l'un sous l'autre : c'est la "
              "présentation qui parle, et plusieurs élèves la montreront chez eux.")

    return d.save(dossier)
