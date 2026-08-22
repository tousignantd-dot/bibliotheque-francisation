# -*- coding: utf-8 -*-
"""A1 · Ça ne commence pas par les travaux
Bloc A « Je découvre » · couleur acier · 75 min. Séance d'ouverture.
Source : dialogue `prep`, exercices `prVF` et `prEtapes`, quatre premières
cartes de FC_CARDS.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A1', section='acier',
        titre="Ça ne commence pas par les travaux",
        chapeau="Doïna veut aménager son sous-sol pour sa mère. Son voisin "
                "lui apprend que tout ce qui décide du prix final se joue "
                "avant qu'un seul outil sorte du camion.",
        duree='75 minutes')

    d.titre(notes="Première séance du module. Ouvrir par une question au groupe : "
                  "qui a déjà fait faire des travaux chez lui, ici ou dans son pays "
                  "d'origine ? Les réponses sont toujours partagées, et c'est "
                  "exactement le sujet du module.")

    d.objectifs([
        "nommer les six étapes qui précèdent un chantier ;",
        "dire ce que chaque étape met dans les mains du propriétaire ;",
        "distinguer un entrepreneur général d'un corps de métier ;",
        "employer les quatre premiers mots du dossier avec leur article.",
    ], notes="Le deuxième objectif est celui du module entier : savoir d'avance ce "
             "qu'un papier ou une démarche va donner, c'est déjà la moitié du "
             "travail.")

    d.declencheur(
        'Observation', "Faire faire des travaux chez soi : par quoi commence-t-on ?",
        pistes=[
            "As-tu déjà fait faire des travaux, ici ou ailleurs ?",
            "Comment as-tu trouvé la personne qui les a faits ?",
            "Le prix a-t-il été écrit quelque part, ou dit de vive voix ?",
            "Y a-t-il eu une surprise à la fin ?",
        ],
        notes="Question sans mauvaise réponse. Beaucoup d'élèves viennent de pays où "
              "tout passe par la relation personnelle et la parole donnée. Ne rien "
              "dévaloriser : s'en servir pour comparer, et pour faire sentir ce "
              "qu'un document écrit change dans le rapport de force.")

    d.dialogue('Dialogue · 1 de 3', "Ce qui vient avant les travaux", [
        ("DOÏNA", "Léandre ! Tu as deux minutes ? Ma mère arrive de Roumanie au mois de mai et on voudrait lui aménager le sous-sol.", True),
        ("LÉANDRE", "C'est exactement ce qu'on a fait l'an passé. Je peux te dire une chose : ce n'est pas les travaux qui sont difficiles, c'est ce qui vient avant.", True),
        ("DOÏNA", "Comment ça, ce qui vient avant ? On appelle quelqu'un, il vient, il donne un prix, non ?", True),
        ("LÉANDRE", "Si tu fais ça, tu vas payer deux fois. Nous autres, on a commencé par une inspection.", True),
    ], consigne="Écouter d'abord, diapositive masquée.",
       notes="La dernière réplique porte tout le bloc. La faire répéter par deux "
             "élèves, puis demander ce que « payer deux fois » veut dire ici : "
             "réparer un résultat sans traiter la cause.")

    d.dialogue('Dialogue · 2 de 3', "Une inspectrice, un entrepreneur", [
        ("DOÏNA", "Un rapport pour quoi faire ? On voit bien qu'il n'y a rien de cassé.", True),
        ("LÉANDRE", "On voit ce qui est visible. Elle, elle regarde la fondation, l'humidité, la pente du terrain, le drain.", True),
        ("DOÏNA", "Et ensuite ?", True),
        ("LÉANDRE", "Ensuite, tu appelles un entrepreneur général. Lui, il coordonne les corps de métier. Tu n'as pas à les appeler un par un.", True),
    ], notes="Écrire « entrepreneur général » et « corps de métier » au tableau et "
             "les y laisser toute la séance. La confusion entre les deux revient "
             "chaque année.")

    d.dialogue('Dialogue · 3 de 3', "La licence et le permis", [
        ("LÉANDRE", "Vérifie la licence de ton entrepreneur : au Québec, celui qui exécute des travaux de construction pour quelqu'un d'autre doit en avoir une, de la Régie du bâtiment.", True),
        ("DOÏNA", "Ça se vérifie où, une licence ?", True),
        ("LÉANDRE", "Dans le registre de la Régie. C'est public, ça prend deux minutes. Deux minutes, avant de signer pour trente mille piastres.", True),
        ("DOÏNA", "Donc : une inspection, une soumission écrite, une licence à vérifier, un permis à demander.", True),
    ], notes="Ces deux faits sont vérifiés, et ce sont les seuls que le module avance "
             "comme des règles : la licence obligatoire, vérifiable au registre "
             "public ; et le permis, qui se demande à sa propre municipalité parce "
             "que les exigences varient de l'une à l'autre. Tout le reste du module "
             "est inventé.")

    d.tableau('Analyse', "Chaque étape, et ce qu'elle te donne",
              ["L'étape", 'Ce qui te reste en main'],
              [["L'inspection", "un rapport écrit qui décrit l'état réel"],
               ["La licence", "la certitude qu'on a le droit de faire les travaux"],
               ["La soumission", "un prix par ligne, et des exclusions"],
               ["Le permis", "l'accord de la ville, et un délai"],
               ["L'échéancier", "la date de chaque étape, séchage compris"]],
              cle=0,
              note="Une étape dont il ne reste rien d'écrit n'a pas eu lieu.",
              notes="Diapositive à photographier. C'est le tableau de référence du "
                    "module ; il revient en A4 sous forme d'exercice, puis à chaque "
                    "ouverture de défi. La sixième étape, la réunion de chantier, "
                    "s'ajoute au tableau en D1.")

    d.regle("Savoir d'avance ce qu'on va obtenir",
            "Chaque étape produit un objet précis : un papier, une confirmation, une date.",
            precision="Devant une inspectrice, vous attendez une description, pas un "
                      "prix. Devant un entrepreneur, vous attendez un prix, pas une "
                      "vérité sur l'état du bâtiment. Devant la ville, vous attendez "
                      "un délai. Demander la mauvaise chose à la bonne personne fait "
                      "perdre une semaine chaque fois.",
            notes="Diapositive à photographier. Insister : il ne s'agit pas de tout "
                  "comprendre, il s'agit de savoir quoi demander à qui.")

    d.vocabulaire('Vocabulaire', "Les quatre premiers mots, avec leur article", [
        ("un entrepreneur général", "La personne qui prend le chantier en charge au complet et qui fait venir chaque métier."),
        ("une soumission", "Le prix écrit qu'une entreprise propose, avec le détail de ce qu'elle fera."),
        ("un corps de métier", "Chacun des métiers appelés sur un chantier : le maçon, le plombier, l'électricien."),
        ("un permis de rénovation", "L'autorisation que la municipalité donne avant certains travaux."),
    ], notes="Faire répéter chaque mot avec son article. « Un corps de métier » "
             "désigne une spécialité, pas une personne : c'est la confusion la plus "
             "fréquente, et elle se corrige ici, pas plus tard.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après la conversation de Doïna et de Léandre.", [
        ("Le plus difficile dans un chantier, ce sont les travaux eux-mêmes.", "faux - c'est ce qui vient avant"),
        ("L'inspectrice de Léandre a trouvé une fissure derrière une étagère.", "vrai"),
        ("L'entrepreneur général coordonne les corps de métier.", "vrai"),
        ("Une soumission écrite au dos d'une facture vaut autant qu'une soumission détaillée.", "faux"),
        ("Un entrepreneur doit détenir une licence de la Régie du bâtiment.", "vrai"),
        ("Le permis est le même partout au Québec.", "faux - il se demande à sa municipalité"),
    ], corrige=True,
       notes="Faire justifier chaque « faux » par la réplique exacte. Le dernier "
             "surprend souvent : plusieurs élèves ont un voisin ou un cousin qui "
             "leur a dit le contraire pour une autre ville.")

    d.billet(
        "Quelle est la première question que tu poserais à un entrepreneur ?",
        exemples=[
            "Une phrase suffit.",
            "Pense à ce que tu voudrais savoir avant de le laisser commencer.",
        ],
        notes="Deux minutes. Garder les billets : ils reviennent en D2, quand le "
              "module travaille la question précise. La plupart écriront « combien "
              "ça coûte », et c'est justement la question qui ne suffit pas.")

    return d.save(dossier)
