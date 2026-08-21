# -*- coding: utf-8 -*-
"""C3 · Il est nécessaire de : la langue des avis.
Bloc C « Défi 2 · L'avis » · couleur ambre · 75 min. Grammaire et écriture.
Source : exercice `t2imperso`, mini-leçon `t2imperso`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C3', section='ambre',
        titre="Il est nécessaire de : la langue des avis",
        chapeau="Trois tournures tiennent tout document administratif. Savoir "
                "les lire vous protège ; savoir les écrire vous ouvre des "
                "portes.",
        duree='75 minutes')

    d.titre(notes="La séance retourne l'exercice de C2 : là on traduisait de "
                  "l'administratif vers l'ordinaire, ici on fait l'inverse. C'est ce "
                  "renversement qui rend le point utile pour les lettres du défi 3.")

    d.objectifs([
        "reconnaître et former la phrase impersonnelle ;",
        "former le passif et accorder son participe ;",
        "employer « veuillez » + infinitif ;",
        "réutiliser ces tournures dans ses propres lettres.",
    ])

    d.regle("Un avis ne dit jamais « vous devez »",
            "L'obligation paraît venir de la situation, pas d'une personne.",
            precision="« Il est nécessaire de libérer l'accès » : personne ne s'adresse à "
                      "personne, et pourtant vous êtes tenu de faire quelque chose. Ce "
                      "n'est pas de la politesse et ce n'est pas de la lâcheté : c'est "
                      "une langue faite pour s'appliquer à tout le monde de la même "
                      "façon.",
            notes="Répondre d'avance à la question qui vient toujours : « pourquoi ils "
                  "n'écrivent pas simplement ? ». Parce qu'un avis s'adresse à six "
                  "logements à la fois.")

    d.tableau('Les trois tournures', "La charpente de tout document officiel",
              ['La tournure', 'Comment elle se fait'],
              [["la phrase impersonnelle",
                "« il » qui ne désigne personne : il est nécessaire de, il est interdit de"],
               ["le passif",
                "être au temps voulu + participe passé : les travaux seront effectués"],
               ["« veuillez » + infinitif",
                "l'impératif poli des écrits : veuillez prévoir, veuillez nous aviser"],
               ["les formules de conséquence",
                "à défaut, faute de quoi, le cas échéant"]],
              cle=0,
              note="Quatre lignes, et vous lisez n'importe quel avis du Québec.",
              notes="Faire retrouver chacune des quatre dans l'avis de C1. Elles y sont "
                    "toutes, ce qui n'est pas un hasard.")

    d.cartes("La phrase impersonnelle de près", "Deux constructions", [
        ("il est nécessaire DE + infinitif",
         "Quand personne n'est visé en particulier : « il est nécessaire de libérer l'accès »."),
        ("il est nécessaire QUE + subjonctif",
         "Quand on précise qui : « il est nécessaire que vous libériez l'accès »."),
        ("Les autres tournures du même type",
         "il est interdit de, il est important de, il est possible de, il y aura."),
        ("Ce qu'elle n'est pas",
         "Elle n'est pas plus faible qu'un ordre. « Il est interdit de » a la même force."),
    ], notes="La deuxième carte annonce la séance C4 : le subjonctif. Ne pas le traiter "
             "ici, seulement le signaler.")

    d.regle("Le passif, et son accord",
            "Être + participe passé, accordé avec le sujet.",
            precision="« Les travaux seront effectués. » « Vous serez avisés. » « La "
                      "porte sera ouverte. » Le participe s'accorde toujours avec le "
                      "sujet, ce qui distingue immédiatement un écrit soigné. Et le "
                      "passif sert aussi dans vos lettres : « aucune réponse ne m'a été "
                      "transmise » est plus ferme et moins accusateur que « vous ne "
                      "m'avez pas répondu ».",
            notes="La dernière phrase est l'argument qui convainc le groupe : la tournure "
                  "administrative n'est pas seulement à subir, elle est à utiliser.")

    d.pratique('Pratique · exercice t2imperso', "Récrivez comme le ferait un avis",
               "Employez la tournure demandée entre parenthèses.",
               [("Vous devez libérer l'accès au mur. (impersonnel)",
                 "Il est nécessaire de libérer l'accès au mur."),
                ("On fera les travaux du 12 au 14 novembre. (passif)",
                 "Les travaux seront effectués du 12 au 14 novembre."),
                ("Ne fumez pas dans les corridors. (impersonnel)",
                 "Il est interdit de fumer dans les corridors."),
                ("Prévoyez un accès, s'il vous plaît. (veuillez)",
                 "Veuillez prévoir un accès au logement."),
                ("Si vous ne le faites pas, nous appellerons. (conséquence)",
                 "À défaut, nous communiquerons avec le propriétaire."),
                ("On vous préviendra la veille. (passif)",
                 "Vous serez avisés vingt-quatre heures d'avance.")],
               corrige=True, cols=1,
               notes="Faire vérifier l'accord du participe dans les deux phrases au "
                     "passif. C'est là que se fait l'erreur.")

    d.piege("Conjuguer « veuillez »",
            "Veux-tu prévoir un accès ? / Veuilles nous aviser.",
            "Veuillez prévoir un accès. Veuillez nous aviser.",
            "La forme est figée : « veuillez », et rien d'autre. C'est la façon la plus "
            "courtoise et la plus neutre de demander quelque chose par écrit. Elle ne "
            "vieillit pas et ne choque personne, ce qui en fait un outil précieux quand "
            "on écrit à quelqu'un qu'on ne connaît pas.",
            notes="Faire écrire trois demandes avec « veuillez » adressées à trois "
                  "destinataires différents : un propriétaire, une école, un assureur.")

    d.tableau('À réutiliser dans vos lettres', "Le passif au service du locataire",
              ['Ce qu\'on dirait', 'Ce qu\'on écrit'],
              [["Vous ne m'avez pas répondu.",
                "Aucune réponse ne m'a été transmise à ce jour."],
               ["Vous n'avez rien réparé.",
                "Aucun travail n'a été effectué depuis le 10 novembre."],
               ["Vous m'aviez promis mercredi.",
                "Une intervention m'avait été confirmée pour le mercredi 12."]],
              cle=1,
              note="Même contenu, aucune accusation — et rien n'est perdu.",
              notes="C'est la diapositive que les élèves photographient le plus dans "
                    "cette séance. Prévoir le temps de la laisser affichée.")

    d.billet(
        "Écrivez une phrase de votre choix dans une tournure d'avis.",
        exemples=[
            "« Il est nécessaire de libérer le corridor avant vendredi. »",
            "« Vous serez avisés vingt-quatre heures d'avance. »",
        ],
        notes="Deux minutes. Corriger l'accord du participe si la phrase est au passif.")

    return d.save(dossier)
