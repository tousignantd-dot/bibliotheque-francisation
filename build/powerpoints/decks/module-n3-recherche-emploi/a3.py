# -*- coding: utf-8 -*-
"""A3 · Où on cherche du travail.
Bloc A « Je découvre » · couleur teal · 60 min. Vocabulaire et lieux.
Source du module : exercice `prImg`, banc `FC_CARDS`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A3', section='teal',
        titre='Où on cherche du travail',
        chapeau="Une affiche dans une vitrine, un carton punaisé près des "
                "paniers, un bureau de quartier. Trois endroits ordinaires, "
                "et c'est là que se trouvent la plupart des premiers emplois.",
        duree='60 minutes')

    d.titre(notes="Séance de vocabulaire et de repérage. Si le quartier de l'école a "
                  "un babillard ou des vitrines, prévoir dix minutes de marche à la "
                  "fin : rien ne remplace d'aller voir.")

    d.objectifs([
        "nommer les endroits où le travail s'affiche ;",
        "distinguer une affiche, une offre d'emploi et une petite annonce ;",
        "nommer les mots du banc de vocabulaire avec leur article ;",
        "dire où l'on cherchera cette semaine.",
    ])

    d.declencheur(
        'Repérage', "Sur le chemin de l'école, où pourrait-on voir du travail affiché ?",
        pistes=[
            "Quels commerces vous passez chaque jour ?",
            "Lesquels ont un babillard à l'entrée ?",
            "Avez-vous déjà lu ce qui y était punaisé ?",
            "Qui, dans le groupe, a trouvé du travail par une affiche ?",
        ],
        notes="Faire dresser la liste au tableau, avec les noms de rues. Elle servira "
              "de devoir en E1 : chacun ira voir un endroit de la liste.")

    d.cartes("Trois papiers, trois choses différentes", "Ne pas les confondre", [
        ("L'affiche d'embauche",
         "Deux ou trois mots, en gros, dans une vitrine : « On embauche ». Elle dit "
         "qu'on cherche quelqu'un, et rien d'autre. On entre pour le reste."),
        ("L'offre d'emploi",
         "Six à dix lignes, punaisée ou imprimée : le poste, l'horaire, le salaire, "
         "ce qu'il faut, à qui s'adresser. Tout est écrit ; il faut savoir la lire."),
        ("La petite annonce",
         "Un carton écrit à la main, souvent avec des languettes découpées en bas. "
         "C'est quelqu'un qui offre ses services — c'est ce que vous écrirez en E2."),
        ("Le babillard",
         "Le panneau de liège où tout cela se punaise, près de l'entrée ou des "
         "paniers. Gratuit, et personne ne demande la permission d'y lire."),
    ], notes="Faire tenir en main, si possible, un exemple de chaque. Sinon les "
             "dessiner au tableau : la forme se retient mieux que la définition.")

    d.vocabulaire('Vocabulaire · 1 de 2', "Les mots de l'affiche et du métier", [
        ("un emploi", "Le travail qu'une personne fait pour recevoir de l'argent."),
        ("embaucher", "Prendre quelqu'un pour travailler dans son commerce."),
        ("un métier", "Le genre de travail qu'on sait faire : cuisinier, concierge."),
        ("un patron", "La personne qui dirige le commerce et qui décide qui travaille."),
        ("une affiche", "Un papier collé bien en vue pour annoncer quelque chose."),
        ("offrir ses services", "Aller dire à quelqu'un qu'on est prêt à travailler pour lui."),
    ], notes="Faire répéter chaque mot avec son article. L'article fait partie du mot.")

    d.vocabulaire('Vocabulaire · 2 de 2', "Les mots du poste et du papier", [
        ("un commis", "La personne qui sert les clients et remplit les tablettes."),
        ("l'expérience", "Tout ce qu'une personne a déjà fait comme travail."),
        ("les disponibilités", "Les jours et les heures où on est libre pour travailler."),
        ("une offre d'emploi", "Un texte court qui dit qu'un travail est à prendre."),
        ("un babillard", "Le panneau où les gens punaisent leurs annonces."),
        ("un formulaire", "Une feuille avec des cases vides qu'il faut remplir."),
    ], notes="Six mots de plus. Les douze de ces deux diapos sont ceux du banc du "
             "module : ce sont eux que les cartes mémoire feront réviser.")

    d.tableau('Analyse', "Chaque endroit, ce qu'on y trouve et ce qu'on y fait",
              ["L'endroit", "Ce qu'on y trouve", "Ce qu'on y fait"],
              [["La vitrine d'un commerce", "une affiche « On embauche »", "on entre"],
               ["Le babillard d'une épicerie", "des offres et des annonces", "on prend en note"],
               ["Le centre communautaire", "des postes d'entretien, de cuisine", "on demande à qui parler"],
               ["Le bureau d'aide à l'emploi", "une personne qui aide", "on prend rendez-vous"]],
              cle=0,
              note="Trois de ces quatre endroits n'exigent aucun rendez-vous.",
              notes="Diapo à photographier. Insister sur la dernière colonne : le geste "
                    "change selon l'endroit, et c'est ce que le module enseigne.")

    d.piege("Regarder l'affiche et repartir",
            "Je reviendrai un autre jour.",
            "J'entre maintenant, ou je note le nom et l'heure.",
            "Une affiche reste rarement collée deux semaines. Si l'on ne peut pas "
            "entrer tout de suite, on note au moins le nom du commerce et son adresse, "
            "et on revient le lendemain matin. Repartir sans rien, c'est n'avoir rien vu.",
            notes="Beaucoup de gens font ce geste-là. Le nommer sans reproche : le but "
                  "est de donner une solution de rechange, pas de culpabiliser.")

    d.pratique('Vocabulaire', "Quel mot manque ?",
               "Complétez avec un mot du banc.", [
        ("Une ___ « On embauche » est collée dans la vitrine.", "affiche"),
        ("J'ai pris deux annonces sur le ___ de l'épicerie.", "babillard"),
        ("Le ___ de la boulangerie s'appelle Gilles.", "patron"),
        ("Elle entre à la boulangerie pour ___ ses services.", "offrir"),
        ("Boulanger, c'est un ___ qui commence très tôt.", "métier"),
        ("Hugo lui donne un ___ de demande d'emploi.", "formulaire"),
    ], corrige=True,
       notes="Le même exercice existe en glisser-déposer dans le module : cette diapo "
             "sert à le préparer à l'oral, pas à le remplacer.")

    d.billet(
        "Nommez un endroit de votre quartier où vous irez regarder cette semaine.",
        exemples=[
            "Le nom du commerce et la rue.",
            "Le jour et l'heure où vous comptez y aller.",
        ],
        notes="Ce billet devient un engagement. Le relire en E1 : demander qui y est "
              "allé, et ce qui était affiché.")

    return d.save(dossier)
