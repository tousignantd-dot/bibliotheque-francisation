# -*- coding: utf-8 -*-
"""E2 · La lettre, et le bilan
Bloc E « Je me lance » · couleur framboise · production écrite · 75 min.
Source : section `appli` (production écrite) et « Je retiens des mots ».
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='E2', section='framboise',
        titre="La lettre, et le bilan",
        chapeau="La lettre d'accompagnement ne répète pas le curriculum "
                "vitæ. Elle répond à une seule question : pourquoi vous, et "
                "pourquoi ici.",
        duree='75 minutes')

    d.titre(notes="Dernière séance du module. Redistribuer les brouillons de D2 "
                  "annotés, et la feuille à deux colonnes de C4 : la lettre s'écrit "
                  "avec les deux sous les yeux.")

    d.objectifs([
        "rédiger une lettre d'accompagnement en trois paragraphes ;",
        "tenir le même ton du début à la fin ;",
        "réemployer les tournures des cinq séances de grammaire ;",
        "faire le bilan des dix-huit mots et de ce qu'on sait faire.",
    ], notes="Le deuxième objectif est celui qu'on corrige le plus : une lettre qui "
             "commence par « Je souhaiterais » et finit par « à bientôt ! » se lit "
             "comme deux lettres différentes.")

    d.declencheur(
        'Préparation', "Que fait une lettre que le curriculum vitæ ne fait pas ?",
        pistes=[
            "Le curriculum vitæ dit ce que vous avez fait.",
            "La lettre dit pourquoi vous, et pourquoi ici.",
            "Combien de paragraphes suffisent ?",
            "Que met-on dans chacun ?",
        ],
        notes="Réponse : trois paragraphes. Ce que vous demandez, le lien entre votre "
              "expérience et l'entreprise, la demande de rencontre. Les faire "
              "trouver plutôt que les donner.")

    d.regle("Trois paragraphes, et rien de plus",
            "Le premier dit ce que vous demandez et où vous avez vu "
            "l'offre. Le deuxième relie votre expérience à ce que "
            "l'entreprise fait. Le troisième demande la rencontre.",
            precision="N'écrivez rien que votre curriculum vitæ ne puisse confirmer. "
                      "Et dites en une phrase que vous êtes prêt à vous installer "
                      "dans la région : c'est la première question que l'employeur "
                      "se posera, et il saura tout de suite qu'il ne perd pas son "
                      "temps.",
            notes="Diapositive à photographier. C'est le plan à suivre pendant "
                  "l'heure d'écriture qui suit.")

    # Six rangées **et** une note ne tiennent pas sur une diapositive projetée.
    # La longueur attendue passe dans le titre, où elle est plus utile qu'en
    # bas de tableau, et les cellules sont raccourcies.
    d.tableau('Analyse', "Ce que la lettre doit contenir — de 10 à 14 phrases",
              ['Exigence', 'Exemple'],
              [["Le titre exact du poste", "Objet : candidature au poste de..."],
               ["Deux conditionnels de politesse", "je souhaiterais... pourriez-vous..."],
               ["Une mise en avant", "Ce que j'apporte, c'est..."],
               ["Un but au subjonctif", "pour que vous puissiez vérifier..."],
               ["Une tâche avec un chiffre", "quarante lots par semaine"],
               ["Une phrase de disponibilité", "disponible dès janvier"]],
              cle=0,
              notes="Diapositive à photographier. C'est la liste de vérification de la "
                    "production écrite du module interactif : les élèves la "
                    "retrouveront à l'écran. Ajouter à voix haute la règle qui "
                    "ne tient pas sur la diapositive : une mise en avant par "
                    "paragraphe, pas davantage.")

    d.piege('Écriture',
            "« La formation de deux techniciennes a été assurée par moi. »",
            "« J'ai formé deux techniciennes. »",
            "Deux fautes de ton en une phrase : la nominalisation de A4 et "
            "la passive de C3, toutes deux apprises pour être LUES, pas pour "
            "être écrites ici. Une lettre où vous vous présentez s'écrit avec "
            "des verbes, à la première personne.",
            notes="Le rappeler avant l'heure d'écriture : c'est la faute la plus "
                  "prévisible du module, et elle vient de ce qu'on a bien enseigné.")

    d.pratique('Production écrite', "Votre lettre, paragraphe par paragraphe",
               "De 10 à 14 phrases, trois paragraphes.", [
        ("Paragraphe 1", "ce que vous demandez, et où vous avez vu l'offre"),
        ("Paragraphe 2", "votre expérience, reliée à ce que l'entreprise fait"),
        ("Paragraphe 3", "votre disponibilité, et la demande de rencontre"),
        ("Le ton", "le même du début à la fin, sans familiarité finale"),
        ("La relecture", "chaque phrase peut-elle être confirmée par le CV ?"),
    ], notes="Une heure d'écriture, avec le brouillon de D2 et le tableau ci-dessus "
             "affichés. Passer dans les rangées plutôt que corriger au tableau.")

    d.vocabulaire('Bilan', "Les mots qu'il faut emporter", [
        ("le marché du travail", "Dix-sept marchés, pas un seul : c'est la thèse du module."),
        ("un secteur d'activité", "Un même métier sert souvent dans deux ou trois secteurs."),
        ("la transformation", "Ce qui fait vivre les régions de ressources."),
        ("la main-d'œuvre", "Ce qui manque là où personne ne cherche."),
        ("une offre d'emploi", "Deux lectures : est-ce pour moi, quels mots j'y prends."),
        ("un atout", "Ce qui vous distingue — et qui n'élimine jamais personne."),
    ], notes="Six des dix-huit, choisis parce qu'ils portent une idée du module et "
             "pas seulement un sens. Les autres se révisent aux cartes mémoire.")

    d.billet(
        "Qu'est-ce que vous ferez la semaine prochaine que vous n'auriez pas fait il y a quatre semaines ?",
        exemples=[
            "Une action concrète, pas une intention.",
            "Un appel, une région à examiner, un curriculum vitæ à retailler.",
        ],
        notes="Dernier billet du module. Le ramasser et le rendre trois semaines plus "
              "tard : c'est le meilleur suivi possible d'une recherche d'emploi.")

    return d.save(dossier)
