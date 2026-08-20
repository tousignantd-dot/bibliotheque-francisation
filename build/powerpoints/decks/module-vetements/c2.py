# -*- coding: utf-8 -*-
"""C2 · Demander et donner un avis.
Bloc C « Défi 2 » · couleur ambre · 60 min.
Source : mini-leçon `t2opinion`, exercice `t2opinion`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C2', section='ambre',
        titre='Demander et donner un avis',
        chapeau="« Je trouve que… », « il me semble que… », « à mon avis… ». "
                "Trois entrées en matière qui transforment un jugement en "
                "opinion — c'est-à-dire en quelque chose qui se discute.",
        duree='60 minutes')

    d.titre(notes="Séance de langue. Elle donne les formules que C1 a fait entendre.")

    d.objectifs([
        "employer je trouve que, il me semble que, à mon avis ;",
        "poser une question d'opinion ;",
        "nuancer avec un peu, plutôt, moins sûr ;",
        "employer le pronom te, vous, lui devant le verbe aller.",
    ])

    d.declencheur(
        'Écoute', "Quelle phrase est la plus facile à recevoir ?",
        pistes=[
            "« Il est trop court. »",
            "« Je trouve qu'il est un peu court. »",
            "« Il me semble un peu court. »",
            "Pourquoi la différence ?",
        ],
        notes="Les trois disent la même chose. Les deux dernières la présentent comme une "
              "opinion, donc discutable — et donc audible.")

    d.tableau('Analyse', "Trois façons de donner un avis",
              ['La formule', 'Ce qui suit'],
              [["Je trouve que…", "une phrase complète : … qu'il te va bien"],
               ["Il me semble…", "un adjectif : … un peu court"],
               ["À mon avis,…", "une phrase : …, le long est mieux"],
               ["Je suis moins sûr de…", "un nom : … la longueur"]],
              cle=0,
              note="« Je trouve que » est la plus courante et la plus sûre.",
              notes="Diapo à photographier. Faire produire une phrase par formule.")

    d.regle("Poser la question",
            "« Qu'est-ce que tu en penses ? »",
            precision="Le petit <b>en</b> remplace « de ce manteau ». On peut aussi dire "
                      "« Comment tu trouves ça ? » ou, plus formel, « Qu'en pensez-vous ? ». "
                      "La formule avec « en » est de loin la plus fréquente à l'oral.",
            notes="Diapo à photographier. Ne pas expliquer le pronom « en » en profondeur : "
                  "il s'apprend ici en bloc.")

    d.cartes("Le verbe « aller » et le pronom", "Trois personnes", [
        ("Il te va bien",
         "Tu parles à la personne. C'est la forme la plus fréquente entre amis."),
        ("Il vous va bien",
         "Tu vouvoies, ou tu parles à une conseillère qui te répond. C'est la forme du "
         "magasin."),
        ("Il lui va bien",
         "Tu parles d'une troisième personne : « Ce manteau lui va bien. »"),
    ], notes="Le pronom se place devant le verbe. C'est la seule difficulté, et elle est "
             "mécanique.")

    d.tableau('Analyse', "Nuancer",
              ['Le mot', "L'effet"],
              [["un peu", "adoucit : un peu court"],
               ["plutôt", "atténue : plutôt long"],
               ["vraiment", "renforce : vraiment beau"],
               ["moins sûr", "réserve : je suis moins sûr de la couleur"]],
              cle=3,
              note="« Je suis moins sûr de… » dit un doute sans dire un non.",
              notes="La dernière ligne est la plus utile pour un désaccord partiel.")

    d.piege("Le jugement sans formule",
            "Il est laid.",
            "Je trouve que la couleur ne te va pas.",
            "Sans formule d'opinion, la phrase devient un fait — et un fait ne se discute "
            "pas. La personne n'a plus qu'à se défendre ou se taire. « Je trouve que » "
            "rend l'avis discutable, donc utile.",
            notes="Insister sur l'effet, pas sur la politesse : c'est une question "
                  "d'efficacité.")

    d.pratique('Pratique · 1 de 2', "Transformez en opinion",
               "Employez une formule.", [
        ("Il est trop court.", "Je trouve qu'il est un peu court."),
        ("Cette couleur ne va pas.", "À mon avis, cette couleur ne te va pas."),
        ("Le prix est trop élevé.", "Il me semble un peu cher."),
        ("La coupe est mauvaise.", "Je suis moins sûr de la coupe."),
    ], corrige=True, cols=1,
       notes="Accepter toute formule d'opinion correcte.")

    d.pratique('Pratique · 2 de 2', "Le bon pronom",
               "Complétez avec te, vous ou lui.", [
        ("Ce manteau ___ va bien. (à ton ami, tutoiement)", "te"),
        ("Cette veste ___ va très bien, madame.", "vous"),
        ("Le rouge ___ va bien, à Diane.", "lui"),
        ("Est-ce qu'il ___ va ? (à toi)", "te"),
    ], corrige=True, cols=1,
       notes="Exercice mécanique et rapide. Dix minutes suffisent.")

    d.billet(
        "Écrivez trois avis avec trois formules différentes.",
        exemples=[
            "Une avec « je trouve que », une avec « il me semble », une avec « à mon avis ».",
            "Chacune sur un vêtement différent.",
        ],
        notes="Ramasser et corriger l'emploi du pronom.")

    return d.save(dossier)
