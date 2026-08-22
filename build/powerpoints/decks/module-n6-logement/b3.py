# -*- coding: utf-8 -*-
"""B3 · Ce que la page dit avant ses phrases
Bloc B « Défi 1 · Ce que dit le site » · couleur teal · 75 min.
Source : exercice `t1mise` et sa mini-leçon ; retour sur `t1page`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B3', section='teal',
        titre="Ce que la page dit avant ses phrases",
        chapeau="Trois secondes de survol donnent la carte du texte. Sans "
                "elle, on lit sans savoir où l'on va.",
        duree='75 minutes')

    d.titre(notes="Séance de méthode. Elle sert autant à lire qu'à écrire : les six "
                  "repères d'une page se retrouvent, à l'envers, dans le courriel du "
                  "bloc E. Le dire dès l'ouverture.")

    d.objectifs([
        "nommer les six repères d'une page Web officielle ;",
        "dire ce que chacun apprend avant la lecture ;",
        "juger de la fiabilité d'une page en deux indices ;",
        "appliquer les mêmes repères à un texte qu'on écrit soi-même.",
    ], notes="Le troisième objectif dépasse le module : c'est celui qui servira le "
             "jour où quelqu'un tombera sur une page de conseils douteux.")

    d.declencheur(
        'Observation', "Regardez la page trois secondes, écran éteint ensuite. Qu'avez-vous retenu ?",
        pistes=[
            "Combien d'étapes la page décrit-elle ?",
            "Quel mot était en gras ?",
            "Y avait-il un encadré ? Où ?",
        ],
        notes="Faire l'exercice pour vrai : projeter la page trois secondes, couper, "
              "puis interroger. Le groupe retient toujours plus qu'il ne croit, et "
              "c'est la démonstration de la séance.")

    d.tableau('Analyse', "Six repères, et ce qu'ils apprennent",
              ['Le repère', 'Ce qu\'il vous dit'],
              [["le titre", "de quoi ça parle, et si vous êtes au bon endroit"],
               ["la mise à jour", "si ce que vous lisez tient encore"],
               ["les intertitres", "combien d'étapes, et dans quel ordre"],
               ["l'encadré", "ce que les gens oublient le plus souvent"]],
              cle=0,
              note="Le gras marque le terme exact à recopier dans vos papiers.",
              notes="Diapositive à photographier. Deux repères de plus sont dans "
                    "l'exercice interactif : le gras et le lien souligné. Les nommer "
                    "à l'oral pour ne pas charger le tableau.")

    d.regle("Le gras n'est pas une décoration",
            "Dans une fiche de droits, il marque les mots qui ont une valeur précise.",
            precision="« Motif sérieux », « dépenses raisonnables », « réputé "
                      "avoir consenti » : ce sont les mots à recopier tels quels "
                      "dans un avis ou un courriel. Les remplacer par un synonyme "
                      "affaiblit la phrase — et parfois change ce qu'elle demande.",
            notes="Diapositive à photographier. Faire relever les mots en gras de la "
                  "page projetée et les écrire au tableau : ce sont ceux que l'élève "
                  "réemploiera en C2 et en E2.")

    d.cartes('Fiabilité', "Deux indices avant de faire confiance", [
        ("Qui écrit ?", "Un organisme public, un cabinet, un forum, une personne ? Une page sans nom d'auteur n'est pas fausse — elle est seulement invérifiable."),
        ("Depuis quand ?", "Une date de mise à jour ancienne n'est pas rédhibitoire, mais elle demande vérification : les règles de logement changent."),
        ("Le doute utile", "Deux pages qui se contredisent, c'est normal : l'une est peut-être périmée. Le téléphone tranche en quatre minutes, gratuitement."),
        ("La page de ce module", "Elle imite la forme d'une fiche officielle et elle est écrite pour le cours. Pour un vrai dossier, on ouvre celle du Tribunal."),
    ], notes="La dernière carte est une honnêteté nécessaire. Le dire clairement : ce "
             "qu'on lit ici est vrai, mais ce n'est pas le document officiel, et "
             "l'élève doit savoir où est le vrai.")

    d.pratique('Pratique', "Quel repère répond à la question ?",
               "Dites quel élément de la page vous renseigne.", [
        ("Suis-je au bon endroit ?", "le titre"),
        ("Est-ce encore à jour ?", "la ligne « mise à jour »"),
        ("Combien y a-t-il d'étapes ?", "les intertitres numérotés"),
        ("Quel mot dois-je recopier dans mon avis ?", "le mot en gras"),
        ("Qu'est-ce que je ne dois surtout pas manquer ?", "l'encadré"),
        ("Où en lire plus long sur ce point ?", "le lien souligné"),
    ], corrige=True,
       notes="Corriger vite : l'exercice est facile et il doit le rester. Ce qui "
             "compte, c'est le réflexe de regarder avant de lire.")

    d.tableau('Retour', "Les mêmes repères, quand c'est vous qui écrivez",
              ['Dans la page', 'Dans votre courriel'],
              [["le titre", "l'objet du message"],
               ["les intertitres", "un paragraphe par idée"],
               ["le gras", "les dates et les noms"],
               ["l'encadré", "la demande, seule, à la fin"]],
              cle=0,
              notes="C'est le pont vers le bloc E. Le poser maintenant fait gagner une "
                    "demi-séance en E2 : l'élève aura déjà vu que lire et écrire se "
                    "servent des mêmes repères.")

    d.billet(
        "Écrivez l'objet d'un courriel qui annonce une sous-location.",
        exemples=[
            "Cinq ou six mots, sans verbe conjugué.",
            "Quelqu'un doit comprendre sans ouvrir le message.",
        ],
        notes="Deux minutes. Ramasser et lire trois objets à voix haute, sans nommer "
              "personne : la classe juge lequel se comprend le mieux. L'exercice "
              "revient en E2, corrigé.")

    return d.save(dossier)
