# -*- coding: utf-8 -*-
"""A3 · Les mots de l'information
Bloc A « Je découvre » · couleur framboise · vocabulaire · 75 min.
Source : exercices `prVocab` et `prGenres`, banc FC_CARDS.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n7-actualite/images/')


def build(dossier):
    d = Deck(
        code='A3', section='framboise',
        titre="Les mots de l'information",
        chapeau="Dix-huit mots tiennent tout le dossier. Les connaître, ce "
                "n'est pas du décor : sans eux, impossible de dire ce qu'on a "
                "compris ni de demander une précision.",
        duree='75 minutes')

    d.titre(notes="Séance de vocabulaire. Le banc du module compte dix-huit mots ; on "
                  "en voit douze aujourd'hui et six reviendront au fil des défis, "
                  "quand ils serviront.")

    d.objectifs([
        "associer chaque genre de texte à ce qu'il fait, et à lui seul ;",
        "employer les mots de la source et de l'annonce officielle ;",
        "nommer les lieux et les gestes de l'information ;",
        "employer chaque mot avec son article.",
    ], notes="Le premier objectif reprend le tableau de A1 sous forme d'exercice. Les "
             "élèves qui l'ont photographié le retrouveront.")

    d.declencheur(
        'Observation', "Que se passe-t-il sur cette image ?",
        image=IMG + 'micro-trottoir.jpg',
        pistes=[
            "Qui tend le micro, et qui répond ?",
            "Est-ce que la personne interrogée était prévenue ?",
            "Ce qu'elle dira, sera-t-il un fait ou une opinion ?",
            "Comment appelle-t-on ce court passage enregistré ?",
        ],
        notes="Amener le mot « extrait sonore » sans le donner tout de suite. La "
              "quatrième piste prépare A4 : la passante donnera son avis, et c'est "
              "légitime.")

    d.vocabulaire('Vocabulaire · 1 de 2', "Les genres et les sources", [
        ("un reportage", "Le compte rendu d'un journaliste qui va sur place et interroge des gens."),
        ("une chronique", "Un texte où quelqu'un donne régulièrement son point de vue signé."),
        ("un éditorial", "Le texte qui exprime la position du journal lui-même."),
        ("un billet de blogue", "Un texte court publié en ligne, que les lecteurs commentent."),
        ("une manchette", "Le titre principal, mis bien en vue."),
        ("une source", "La personne ou le document qui permet de vérifier une information."),
    ], notes="Faire répéter avec l'article. Demander à chaque fois : est-ce que ce "
             "genre-là donne un avis, oui ou non ?")

    d.vocabulaire('Vocabulaire · 2 de 2', "Ce qui vient des institutions", [
        ("un communiqué", "Le texte officiel qu'un organisme envoie aux médias pour annoncer quelque chose."),
        ("un porte-parole", "La personne chargée de parler au nom d'un organisme."),
        ("une entrevue", "L'échange où un journaliste pose des questions à quelqu'un."),
        ("un extrait sonore", "Le court passage enregistré où on entend parler la personne interrogée."),
        ("une séance du conseil", "La réunion publique où les élus d'une ville décident devant les citoyens."),
        ("la période de questions", "Le moment où les personnes présentes peuvent interroger les élus."),
    ], notes="Les deux derniers mots seront utiles bien au-delà du module : tout adulte "
             "qui habite une municipalité peut se présenter à une séance du conseil et "
             "poser sa question. Le dire clairement.")

    d.tableau('Analyse', "Un communiqué n'est pas un reportage",
              ['Le texte', 'Qui l\'écrit', 'Ce qu\'il vise'],
              [["Un communiqué", "l'organisme lui-même", "annoncer ce qui l'arrange"],
               ["Un reportage", "un journaliste", "rapporter ce qu'il a constaté"],
               ["Une chronique", "une personne qui signe", "convaincre"],
               ["Un billet de blogue", "n'importe qui", "dire ce qu'on pense, et en discuter"]],
              cle=0,
              note="Aucun des quatre n'est malhonnête. Mais aucun ne fait le travail des trois autres.",
              notes="Diapositive à photographier. C'est la grille qui servira toute la "
                    "vie de l'élève, bien au-delà de ce dossier.")

    d.regle("L'article fait partie du mot",
            "On apprend « une source », pas « source ».",
            precision="Le genre de ces mots ne se devine pas : « un communiqué », mais "
                      "« une entrevue » ; « un éditorial », mais « une manchette ». "
                      "Apprendre le mot seul oblige à deviner à chaque emploi, et une "
                      "fois sur deux on se trompe.",
            notes="Règle valable partout, rappelée ici parce que la séance est une "
                  "séance de vocabulaire.")

    d.pratique('Association', "Chaque genre a son travail",
               "Reliez le genre à ce qu'il fait.", [
        ("un reportage", "rapporter ce qu'un journaliste a constaté sur place"),
        ("une chronique", "donner l'avis signé d'une personne, semaine après semaine"),
        ("un éditorial", "exprimer la position du journal lui-même"),
        ("un communiqué", "annoncer officiellement quelque chose au nom d'un organisme"),
        ("un billet de blogue", "publier en ligne un texte court que les lecteurs commentent"),
        ("une entrevue", "faire parler quelqu'un en lui posant des questions"),
    ], corrige=True,
       notes="Reprendre le même exercice dans l'activité interactive, en glisser-déposer. "
             "Faire justifier chaque association d'une phrase.")

    d.billet(
        "Écrivez deux mots d'aujourd'hui que vous n'aviez jamais employés.",
        exemples=[
            "Écrivez-les avec leur article.",
            "Pour chacun, écrivez une phrase de votre vie, pas du module.",
        ],
        notes="Deux minutes. Les phrases personnelles fixent le mot bien mieux qu'une "
              "définition recopiée.")

    return d.save(dossier)
