# -*- coding: utf-8 -*-
"""A3 · Les mots des services publics.
Bloc A « Je découvre » · couleur framboise · 75 min. Vocabulaire.
Source : exercices `prVocab` et `prImg`, banc FC_CARDS.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n5-services/images/')


def build(dossier):
    d = Deck(
        code='A3', section='framboise',
        titre="Les mots des services publics",
        chapeau="Seize mots, et la plupart ne s'apprennent nulle part "
                "ailleurs : on les rencontre pour la première fois le jour "
                "où on en a besoin, au téléphone, sans dictionnaire.",
        duree='75 minutes')

    d.titre(notes="Séance de vocabulaire. Commencer par ramasser le devoir A1 : quel jour "
                  "de collecte chacun a-t-il trouvé ? Trois ou quatre réponses suffisent "
                  "pour montrer que les jours diffèrent d'une rue à l'autre.")

    d.objectifs([
        "nommer les seize mots du module et leur donner une définition ;",
        "associer chaque mot à une situation concrète ;",
        "distinguer les mots des bacs, de l'appel, de l'écran et du guichet ;",
        "employer cinq de ces mots dans une phrase à soi.",
    ])

    d.declencheur(
        'Observation', "Que se passe-t-il sur cette photo ?",
        image=IMG + 'ecocentre-depot.jpg',
        pistes=[
            "Où sommes-nous ?",
            "Pourquoi ces gens attendent-ils en auto ?",
            "Qu'est-ce qu'ils apportent ?",
            "Faut-il payer pour entrer ?",
        ],
        notes="Beaucoup d'élèves n'ont jamais vu d'écocentre. Laisser décrire longuement "
              "avant de nommer : le mot se retient mieux après l'image.")

    d.vocabulaire('Vocabulaire · 1 de 4', "La brochure et les collectes", [
        ("une brochure",
         "Un petit document imprimé de quelques pages, envoyé pour informer la population."),
        ("les matières résiduelles",
         "Le mot officiel pour tout ce qu'on jette : ordures, recyclage et restes de table."),
        ("le bac brun",
         "Le bac où l'on met les restes de table et les résidus de jardin."),
        ("un écocentre",
         "Un lieu public où l'on apporte ce qui n'entre dans aucun bac."),
        ("une preuve de résidence",
         "Un papier à votre nom qui montre où vous habitez : un bail, une facture."),
    ], notes="« Matières résiduelles » est le premier mot d'administration du module. "
             "Faire remarquer qu'on ne le dit jamais à son voisin, mais qu'il est le seul "
             "qui figure dans un règlement.")

    d.vocabulaire('Vocabulaire · 2 de 4', "Au téléphone", [
        ("un préposé",
         "La personne employée par un service pour répondre au public."),
        ("une requête",
         "Une demande enregistrée par un service, qui reçoit un numéro et qu'on peut suivre."),
        ("un jour ouvrable",
         "Un jour où les bureaux sont ouverts : du lundi au vendredi, sauf les fériés."),
        ("épeler",
         "Dire un mot lettre par lettre, pour que l'autre personne l'écrive sans erreur."),
    ], notes="« Requête » est le mot le plus utile du module entier. Le dire, et faire "
             "répéter la question qui l'emploie : « Est-ce que vous ouvrez une requête ? »")

    d.vocabulaire('Vocabulaire · 3 de 4', "Devant l'écran", [
        ("un formulaire",
         "Un document à remplir, avec des champs à compléter dans un ordre imposé."),
        ("en vigueur",
         "Se dit d'une règle, d'un tarif ou d'un horaire qui s'applique en ce moment."),
        ("une matière refusée",
         "Une chose qu'un lieu de dépôt n'accepte pas, même si vous l'avez apportée."),
        ("un encadré",
         "Un court texte entouré d'un cadre, mis à part parce qu'il est plus important."),
    ], notes="« En vigueur » revient dans toutes les pages officielles du Québec, bien "
             "au-delà de ce module. Insister : c'est un mot qui sert toute la vie.")

    d.vocabulaire('Vocabulaire · 4 de 4', "Au guichet", [
        ("un guichet",
         "Le comptoir où l'on se présente pour faire une démarche en personne."),
        ("un billet de file d'attente",
         "Le papier numéroté qu'on prend en entrant, et qui donne son tour."),
        ("une pièce d'identité",
         "Un document officiel qui prouve qui vous êtes, souvent avec une photo."),
    ], notes="Demander qui, dans le groupe, a déjà pris un billet numéroté quelque part. "
             "Presque tout le monde — mais peu savent le nommer en français.")

    d.tableau('Quatre mots qui se ressemblent', "Et qui ne disent pas la même chose",
              ['Le mot', 'Ce qu\'il désigne exactement'],
              [["une demande", "ce que vous formulez — cela peut rester sans trace"],
               ["une requête", "la demande une fois enregistrée, avec un numéro"],
               ["une pièce d'identité", "qui vous êtes — souvent avec photo"],
               ["une preuve de résidence", "où vous habitez — avec votre adresse"]],
              cle=0,
              note="Au guichet, on demande souvent les deux dernières : ce sont deux papiers, pas un.",
              notes="Diapositive à photographier. La distinction des deux dernières lignes "
                    "est la cause la plus fréquente d'un deuxième déplacement.")

    d.pratique('Vocabulaire', "Le mot juste",
               "Quel mot du module convient ?", [
        ("La personne qui vous répond au comptoir.", "un préposé"),
        ("Le papier numéroté qu'on prend en entrant.", "un billet de file d'attente"),
        ("Une demande enregistrée qui porte un numéro.", "une requête"),
        ("Du lundi au vendredi, sauf les fériés.", "un jour ouvrable"),
        ("Le tarif qui s'applique aujourd'hui.", "le tarif en vigueur"),
        ("Le lieu où l'on apporte un vieux réfrigérateur.", "un écocentre"),
        ("Le bail ou la facture qui montre votre adresse.", "une preuve de résidence"),
        ("Le bloc de texte encadré, plus important que le reste.", "un encadré"),
    ], corrige=True,
       notes="Faire employer chaque réponse dans une phrase complète, pas seulement "
             "nommer le mot. C'est là que se voit la maîtrise réelle.")

    # `capture` n'existe que dans theme.Deck : les présentations la portent, les
    # fiches imprimées non (build/powerpoints/fiche.py n'a pas la méthode). Une
    # fiche noir et blanc n'a de toute façon rien à faire d'une capture d'écran.
    if hasattr(d, 'capture'):
        d.capture('prImg', "L'exercice à l'écran",
                  consigne="Glissez chaque photo sur la phrase qui la décrit.",
                  notes="Travail individuel, dix minutes. Les huit photos reprennent les "
                        "quatre familles de mots dans l'ordre du module.")

    d.billet(
        "Écrivez cinq phrases avec cinq mots du module, tirées de votre vie.",
        exemples=[
            "« La dernière fois que je suis allé au guichet, j'avais oublié ma preuve de résidence. »",
            "Si un mot ne vous sert jamais, choisissez-en un autre et dites pourquoi.",
        ],
        notes="La deuxième consigne est volontaire : elle permet à un élève sans auto ni "
              "logement à lui de ne pas inventer une situation qu'il n'a pas vécue.")

    return d.save(dossier)
