# -*- coding: utf-8 -*-
"""A4 · Quatre écrits, quatre travaux
Bloc A « Je découvre » · couleur teal · 75 min. Révision du bloc.
Source : exercices `prEcrits` et `prImg`, mini-leçon `prEcrits`, les seize
cartes de FC_CARDS pour les quatre premières.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A4', section='teal',
        titre="Quatre écrits, quatre travaux",
        chapeau="Dernière séance du bloc. On rassemble ce que le bloc a "
                "montré, et on s'entraîne à choisir le bon papier avant de "
                "lire une seule phrase.",
        duree='75 minutes')

    d.titre(notes="Séance de révision. Reprendre les billets d'A1 et d'A2 : ils "
                  "disent quel écrit intimide le groupe et quels mots reprendre. "
                  "Commencer par là plutôt que par le programme prévu.")

    d.objectifs([
        "associer chaque écrit du travail à son travail propre ;",
        "trouver le bon papier à partir d'une question ;",
        "réemployer les quatre mots du bloc et les trois cas de "
        "graphie-phonie ;",
        "annoncer ce qui vient au Défi 1 : une démarche en cinq étapes.",
    ], notes="Le deuxième objectif est celui qui se mesure : donner une question, "
             "faire nommer le papier. C'est le geste que le module veut installer.")

    d.declencheur(
        'Retour', "Qu'est-ce qui t'a le plus surpris dans le bloc A ?",
        pistes=[
            "Qu'on n'ait pas besoin de la permission de son chef d'équipe ?",
            "Qu'un affichage disparaisse après dix jours ouvrables ?",
            "Que « technicien » se prononce avec un k ?",
        ],
        notes="Trois minutes, pas plus. Le premier point est celui qui revient le "
              "plus souvent, et c'est celui qui décide qui osera se présenter.")

    d.tableau('Révision', "Une question, un papier",
              ['Ta question', 'Où chercher'],
              [["Jusqu'à quand ?", "l'affichage — c'est le seul qui porte la date limite"],
               ["Quoi faire, dans quel ordre ?", "la note de service — ses puces sont des gestes"],
               ["Est-ce permis ?", "la politique — cherchez l'article et son numéro"],
               ["Qu'est-ce qui a été décidé ?", "le compte rendu — allez droit aux décisions"]],
              cle=0,
              note="Le compte rendu ne donne jamais de règle : il donne des décisions.",
              notes="Diapositive à photographier. C'est la version utile du tableau "
                    "d'A1 : celui-là partait du papier, celui-ci part de la question. "
                    "C'est ainsi qu'on s'en sert dans la vraie vie.")

    d.pratique('Pratique', "Quel papier vas-tu chercher ?",
               "Une question, une réponse. À l'oral, en équipes de deux.", [
        ("Est-ce que je peux encore me présenter ?", "l'affichage — la date limite"),
        ("Combien de temps dure la période d'essai ?", "la politique, article 4.5"),
        ("Quel formulaire faut-il remplir ?", "la note de service"),
        ("Qu'est-ce qu'on a répondu sur l'ancienneté ?", "le compte rendu"),
        ("Est-ce que l'ancienneté compte dans le choix ?", "la politique, article 4.3"),
        ("Où et quand est la rencontre d'information ?", "la note de service"),
    ], corrige=True,
       notes="Deux réponses sont défendables pour la dernière : la note l'annonce, le "
             "compte rendu la rapporte après. Accepter les deux si l'élève explique.")

    d.cartes('Analyse', "Ce qu'un papier ne fait jamais", [
        ("L'affichage n'explique pas",
         "Il tient en une demi-page. La démarche complète est ailleurs — dans la note et dans la politique."),
        ("La note ne décide pas",
         "Elle explique une règle qui existe ailleurs. Le jour où elle contredit la politique, c'est la politique qui s'applique."),
        ("La politique ne s'adresse à personne",
         "Elle dit « l'employé », jamais « vous ». C'est la différence la plus visible avec une note de service."),
        ("Le compte rendu ne fait pas de règle",
         "Il rapporte ce qui a été dit un jour donné. Une phrase de rencontre n'est pas un texte officiel."),
    ], notes="Diapositive à photographier. Les quatre phrases sont les quatre "
             "confusions les plus fréquentes. Les faire reformuler par le groupe, "
             "chacune en une phrase à soi.")

    d.regle("Le poids des papiers",
            "En cas de contradiction, la politique l'emporte sur tout le reste.",
            precision="Une note explique, un affichage annonce, un compte rendu "
                      "rapporte. Un seul de ces textes crée la règle, et c'est la "
                      "politique. Le savoir évite de citer, dans une discussion, une "
                      "phrase entendue dans un corridor comme si elle avait force "
                      "d'obligation.",
            notes="Diapositive à photographier. Rappeler aussi ce que le module dira "
                  "au bloc C : une politique interne vient de l'employeur, pas de la "
                  "loi. Ce n'est ni plus ni moins qu'un engagement d'entreprise.")

    d.vocabulaire('Vocabulaire', "Ce qui arrive au Défi 1", [
        ("les ressources humaines", "Le service qui s'occupe des employés : dossiers, formulaires, embauches."),
        ("un formulaire", "La feuille toute faite qu'on remplit pour demander quelque chose officiellement."),
        ("un comité de sélection", "Le petit groupe de personnes qui rencontre les candidats et qui choisit."),
        ("une période d'essai", "Le temps où l'on fait le nouveau travail pour voir si ça convient."),
    ], notes="Ces quatre mots ouvrent le bloc B. Les donner à la fin d'A4 plutôt "
             "qu'au début de B1 : le groupe arrive alors en terrain déjà nommé.")

    d.billet(
        "En une phrase : où irais-tu chercher la démarche complète ?",
        exemples=[
            "Nomme le papier, et dis pourquoi.",
            "Il y a deux bonnes réponses, et l'une est plus sûre que l'autre.",
        ],
        notes="Deux minutes. La réponse attendue : la politique, parce qu'elle fixe "
              "la règle ; la note, parce qu'elle l'explique. Accepter les deux et "
              "faire nommer la différence. C'est le pont vers le bloc B, où c'est "
              "une personne qui explique de vive voix.")

    return d.save(dossier)
