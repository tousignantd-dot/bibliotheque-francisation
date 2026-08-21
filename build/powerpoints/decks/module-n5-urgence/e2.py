# -*- coding: utf-8 -*-
"""E2 · Le message à la famille, et le bilan.
Bloc E « Je me lance » · couleur framboise · 75 min. Production écrite et bilan.
Source : bloc `appli` — production écrite — et « Je retiens des mots ».
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n5-urgence/images/')


def build(dossier):
    d = Deck(
        code='E2', section='framboise',
        titre="Le message à la famille, et le bilan",
        chapeau="Cinq personnes attendent des nouvelles et vous ne pouvez "
                "pas appeler cinq fois. Un seul message, clair, que chacun "
                "pourra relire — et qui évite cinq appels à l'hôpital.",
        duree='75 minutes')

    d.titre(notes="Dernière séance du module. Commencer par écouter deux enregistrements "
                  "de E1, avec l'accord de leurs auteurs. Le passage de l'oral à l'écrit "
                  "se fait alors tout seul.")

    d.objectifs([
        "écrire un message de nouvelles de sept à onze phrases ;",
        "y employer les quatre outils du module : imparfait, passé composé, discours "
        "rapporté, futur simple ;",
        "donner le pratique : étage, heures de visite, ce qu'il faut apporter ;",
        "faire le bilan de ce qu'on sait faire maintenant.",
    ])

    d.declencheur(
        'Comparaison', "Deux messages annoncent la même chose. Lequel calme la "
                       "famille, lequel la fait téléphoner à l'hôpital ?",
        image=IMG + 'chambre.jpg',
        pistes=[
            "« Ça a été une nuit épouvantable, je n'en peux plus. »",
            "« Maman va bien. Elle a été opérée hier matin et tout s'est bien passé. »",
            "Lequel donne une information ? Lequel donne une émotion ?",
            "Qu'est-ce que la famille fera après avoir lu chacun ?",
        ],
        notes="Les deux messages sont sincères. Le premier est légitime, mais il déclenche "
              "cinq appels inquiets. Le dire sans juger : ce n'est pas une question de "
              "politesse, c'est une question d'effet.")

    d.regle("Des faits, pas des impressions",
            "« Elle a été opérée hier matin et tout s'est bien passé. »",
            precision="Un message factuel calme ; un message d'émotion inquiète. Vous "
                      "aurez tout le temps de dire votre fatigue à quelqu'un en "
                      "particulier — mais pas dans le message qui informe tout le monde.",
            notes="Diapositive à photographier, et à laisser affichée pendant l'écriture.")

    d.cartes("Les six éléments du message", "À cocher avant de demander la correction", [
        ("Une phrase qui rassure",
         "En premier, toujours. « Maman va bien. »"),
        ("Ce qui est arrivé",
         "L'imparfait pour le décor, le passé composé pour les faits."),
        ("Ce que le personnel a dit",
         "« La docteure dit que… », « elle m'a demandé si… »."),
        ("Ce qui s'en vient",
         "Au futur simple : elle sortira, il faudra, une intervenante viendra."),
        ("Le pratique",
         "L'étage, l'unité, les heures de visite, ce qu'il faut apporter."),
        ("Une demande précise",
         "À quelqu'un en particulier, et un moment où vous joindre."),
    ], cols=3,
       notes="Les six éléments sont cochables dans le module : les élèves peuvent "
             "vérifier leur propre texte avant de demander la correction.")

    d.tableau('Le cadre du message', "Ce qui se met où",
              ['Ligne', 'Contenu'],
              [["À", "la famille — les personnes qui attendent"],
               ["Objet", "Des nouvelles de maman — hôpital, 5e étage, unité B"],
               ["Première phrase", "Bonjour à tous. D'abord, maman va bien."],
               ["Dernière phrase", "une demande, un numéro, un moment"]],
              cle=0,
              note="Un objet qui porte déjà l'essentiel évite la moitié des réponses.",
              notes="L'objet est la partie que les élèves négligent le plus, et c'est la "
                    "seule que tout le monde lit à coup sûr.")

    d.piege("Tout raconter",
            "Un message de vingt phrases avec chaque examen et chaque heure d'attente.",
            "Sept à onze phrases, et le reste à la visite.",
            "Un message trop long ne se lit pas jusqu'au bout : le pratique, qui est à la "
            "fin, se perd. Gardez le détail pour ceux qui rappelleront.",
            notes="Faire compter les phrases avant d'envoyer. Le module le fait aussi, "
                  "mais compter soi-même vaut mieux.")

    d.pratique('Production écrite', "Votre message, sept à onze phrases",
               "Vérifiez les six éléments avant de demander la correction.", [
        ("Votre première phrase rassure-t-elle ?", "avant tout récit"),
        ("Le décor est-il à l'imparfait, les faits au passé composé ?", "elle avait · elle est tombée"),
        ("Rapportez-vous ce qu'on vous a dit ?", "la docteure dit que… · elle m'a demandé si…"),
        ("Ce qui s'en vient est-il au futur simple ?", "elle sortira · il faudra"),
        ("Donnez-vous l'étage et les heures de visite ?", "et ce qu'il faut apporter"),
        ("Demandez-vous quelque chose à quelqu'un ?", "et laissez-vous un numéro ?"),
    ], corrige=True,
       notes="Faire écrire dans le module, puis demander la correction de l'assistant. "
             "Les élèves rapides peuvent écrire le second message : celui du jour du congé.")

    d.vocabulaire('Bilan', "Ce que vous savez faire maintenant", [
        ("Choisir le numéro", "Est-ce que ça peut attendre dix minutes ? Et les cinq signes."),
        ("Appeler le 9-1-1", "L'endroit d'abord, une phrase ensuite, des réponses courtes."),
        ("Comprendre un ordre", "L'impératif, et le pronom avant ou après le verbe."),
        ("Raconter au triage", "L'imparfait pour le décor, le passé composé pour les faits."),
        ("Rapporter", "Elle m'a demandé si… · la docteure dit que…"),
        ("Annoncer la suite", "Le futur simple, et les questions posées avant le congé."),
    ], notes="Faire relire cette liste dans le module, section « Je retiens des mots », et "
             "compléter l'autoévaluation avant de terminer.")

    d.billet(
        "En une phrase : qu'est-ce que vous ferez différemment si ça arrive chez vous ?",
        exemples=[
            "Une seule chose, précise, que vous ferez vraiment.",
            "« Je donnerai l'adresse en premier », « j'appellerai le 8-1-1 au lieu d'attendre »…",
        ],
        notes="Dernier billet du module. Les lire à voix haute, sans nommer les auteurs : "
              "c'est la meilleure révision possible en cinq minutes.")

    return d.save(dossier)
