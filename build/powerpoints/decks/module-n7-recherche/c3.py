# -*- coding: utf-8 -*-
"""C3 · Quand personne ne semble agir : la phrase passive
Bloc C « Défi 2 » · couleur ambre · écriture · 75 min.
Source : exercice `t2passif`, mini-leçon `t2passif`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C3', section='ambre',
        titre="Quand personne ne semble agir",
        chapeau="« L'usine a été agrandie en 2021. » Par qui ? Le texte ne "
                "le dit pas, et c'est délibéré. La phrase passive rapporte "
                "un événement en laissant son auteur dans l'ombre.",
        duree='75 minutes')

    d.titre(notes="Deuxième point de grammaire du Défi 2. Il se travaille sur le "
                  "portrait de C2 : faire chercher les passives dans le texte "
                  "imprimé avant d'ouvrir la théorie.")

    d.objectifs([
        "reconnaître une phrase passive au passé composé ;",
        "accorder le participe avec le sujet, sans exception ;",
        "savoir qui la passive ne nomme pas ;",
        "employer la voix active dans sa propre lettre.",
    ], notes="Le quatrième objectif est un contrepoids, comme en A4 : on apprend à "
             "lire la passive, on n'apprend pas à s'en servir pour se présenter.")

    d.declencheur(
        'Observation', "Qui a agrandi l'usine ?",
        pistes=[
            "« On a agrandi l'usine en 2021. »",
            "« L'usine a été agrandie en 2021. »",
            "Laquelle des deux nomme celui qui a payé ?",
            "Pourquoi un document officiel choisit-il la seconde ?",
        ],
        notes="Réponse : aucune des deux ne le nomme vraiment, mais la première "
              "laisse au moins entendre qu'il y a quelqu'un. La passive efface même "
              "cette trace.")

    d.regle("Être au passé composé, plus le participe passé",
            "On a agrandi l'usine devient : l'usine a été agrandie. Deux "
            "participes de suite — « été », puis celui du verbe.",
            precision="Le participe du verbe s'accorde toujours avec le sujet : "
                      "l'usine a été agrandie, les postes ont été affichés, les "
                      "candidatures ont été reçues. « Été » reste invariable. C'est "
                      "la faute la plus fréquente, et elle se voit à l'œil nu.",
            notes="Diapositive à photographier. Le signal sonore est « a été », en "
                  "deux syllabes bien détachées : le faire entendre.")

    d.cartes('Analyse', "L'accord se fait avec le sujet", [
        ("L'usine a été agrandie.", "féminin singulier : -e"),
        ("Les deux postes ont été affichés.", "masculin pluriel : -és"),
        ("Onze candidatures ont été reçues.", "féminin pluriel : -ues"),
        ("Le portrait a été publié.", "masculin singulier : rien"),
        ("Sa candidature a été retenue par le comité.", "avec agent : « par »"),
        ("Il est respecté de ses collègues.", "verbe de sentiment : « de », pas « par »"),
    ], cols=1,
       notes="Les deux dernières cartes portent le complément d'agent. Le « de » ne "
             "concerne qu'une poignée de verbes — respecter, aimer, connaître, "
             "accompagner, suivre — et se reconnaît plus qu'il ne se produit.")

    d.tableau('Analyse', "Pourquoi l'auteur choisit la passive",
              ['La raison', 'Ce que ça donne'],
              [["Il ignore qui a agi", "« Le poste a été comblé. »"],
               ["Ça n'intéresse personne", "« L'usine a été agrandie en 2021. »"],
               ["Il préfère ne pas le dire", "« La décision a été prise en avril. »"],
               ["L'agent est une vraie information", "« ...par le comité de sélection. »"]],
              cle=0,
              note="Dans un portrait économique, l'agent est absent neuf fois sur dix.",
              notes="Diapositive à photographier. Demander laquelle des quatre "
                    "raisons doit rendre un lecteur méfiant : la troisième, et elle "
                    "ne se distingue pas des autres à la lecture.")

    d.piege('Lecture',
            "compléter une passive avec ce qu'on imagine",
            "s'en tenir à ce qu'elle dit",
            "« Le poste a été comblé » ne dit ni quand il a été affiché, ni "
            "par qui il a été comblé, ni s'il l'a été à l'interne. Trois "
            "informations que le lecteur ajoute tout seul, et qui ne sont "
            "nulle part dans la phrase.",
            notes="Faire relire la phrase et faire lister ce qu'elle ne dit pas. "
                  "L'exercice est court et il marque.")

    d.pratique('Grammaire', "Mettez au passif, au passé composé",
               "Écrivez seulement le groupe verbal.", [
        ("On a agrandi l'usine en 2021. L'usine ___ en 2021.", "a été agrandie"),
        ("On a affiché les deux postes en février. Les deux postes ___ .", "ont été affichés"),
        ("On a reçu onze candidatures. Onze candidatures ___ .", "ont été reçues"),
        ("Le comité a retenu sa candidature. Sa candidature ___ par le comité.", "a été retenue"),
        ("On a publié le portrait l'an dernier. Le portrait ___ l'an dernier.", "a été publié"),
        ("L'entreprise a créé trente postes. Trente postes ___ par l'entreprise.", "ont été créés"),
        ("On a fermé la scierie en 2019. La scierie ___ en 2019.", "a été fermée"),
        ("Le ministère a évalué ses études. Ses études ___ par le ministère.", "ont été évaluées"),
    ], corrige=True,
       notes="Exercice `t2passif` du module interactif. Faire entourer la terminaison "
             "du participe à chaque correction : c'est là que la faute se loge.")

    d.billet(
        "Récrivez à la voix active deux phrases passives trouvées dans votre portrait de région.",
        exemples=[
            "Si l'agent n'est pas nommé, inventez « on » ou « l'entreprise ».",
            "Notez ce que vous avez dû deviner.",
        ],
        notes="Le « ce que vous avez dû deviner » est le vrai apprentissage : il "
              "rend visible tout ce qu'une passive cache.")

    return d.save(dossier)
