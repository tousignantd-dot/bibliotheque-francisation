# -*- coding: utf-8 -*-
"""C2 · L'avis d'admission conditionnelle
Bloc C « Défi 2 » · couleur teal · 75 min. Lecture d'un document officiel.
Source : exercices `t2avis` (type `texte`) et `t2mise`, et leurs mini-leçons.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C2', section='teal',
        titre="L'avis d'admission conditionnelle",
        chapeau="Une page, trois minutes, cinq endroits. La bonne nouvelle "
                "est en haut, l'obligation est au milieu — et beaucoup de "
                "gens referment la feuille avant d'y arriver.",
        duree='75 minutes')

    d.titre(notes="Séance de lecture pure. Distribuer si possible la copie papier de "
                  "l'avis, tirée des fiches élèves : un document qu'on tient dans la "
                  "main se lit autrement qu'un document projeté.")

    d.objectifs([
        "regarder cinq endroits d'un avis avant d'en lire la première phrase ;",
        "dire exactement ce que veut dire « admission conditionnelle » ;",
        "retrouver la condition, la date limite et la personne à contacter ;",
        "lire la mise en page comme une information, au même titre que le texte.",
    ], notes="Le quatrième objectif vient de la grammaire du texte : « tenir compte "
             "de la présentation matérielle et de la mise en page ». Ce n'est pas de "
             "la décoration, c'est du sens.")

    d.declencheur(
        'Observation', "Que faites-vous en recevant une lettre officielle ?",
        pistes=[
            "Vous l'ouvrez tout de suite, ou vous attendez ?",
            "Vous lisez le début, ou vous cherchez un mot précis ?",
            "Avez-vous déjà lu une lettre deux fois et compris deux choses différentes ?",
        ],
        notes="La dernière question est la plus riche : beaucoup diront oui. C'est "
              "exactement ce que la méthode des cinq endroits vient corriger.")

    d.tableau('Analyse', "Cinq endroits, dans cet ordre",
              ['Où regarder', 'Ce que ça donne'],
              [["L'en-tête", "quel établissement parle, et il ne parle que pour lui"],
               ["La ligne en gras", "le genre du document, donc tout ce qui va suivre"],
               ["L'encadré", "la condition ou la date : ce qui est entouré est ce qui oblige"],
               ["Les deux dates", "celle de l'envoi, et celle qui vous oblige"],
               ["La dernière ligne", "à qui vous adresser, et à quel poste"]],
              cle=0,
              note="Regardez avant de lire. Un lecteur pressé qui sait regarder comprend plus vite qu'un lecteur appliqué.",
              notes="Diapositive à photographier. Faire appliquer les cinq points sur "
                    "l'avis distribué, en trois minutes, chronomètre en main.")

    d.regle("Conditionnelle veut dire : à vous, jusqu'à la date",
            "Une admission conditionnelle réserve la place, elle ne la donne pas.",
            precision="Ce n'est ni un oui, ni un non. Le centre garde une place dans "
                      "un groupe précis, et personne d'autre ne peut la prendre tant "
                      "que la date n'est pas passée. « Je suis acceptée mais pas "
                      "vraiment » est une lecture inquiète, et elle est fausse.",
            notes="Diapositive à photographier. Faire redire la phrase par trois "
                  "élèves différents. Elle défait une angoisse réelle et très "
                  "répandue.")

    d.tableau('Analyse', "Ce que l'avis de Bintou dit exactement",
              ['La ligne', 'Ce qu\'elle veut dire'],
              [["Avis d'admission conditionnelle", "le genre du document, dès la première ligne"],
               ["Une place vous est réservée", "elle est à vous, dans le groupe du 2 mars"],
               ["La candidate fournira la preuve", "fournissez-la : ce futur est un ordre"],
               ["Les documents se déposent", "c'est vous qui les déposez, personne d'autre"],
               ["La place est libérée le 6 février", "la date qui oblige, à mettre au calendrier"],
               ["Vous vous adresserez à madame Dostie", "la seule personne qui peut changer quelque chose"]],
              cle=0,
              notes="Diapositive à photographier. Six lignes : c'est tout l'avis. "
                    "Faire constater qu'une page officielle tient en six phrases "
                    "utiles.")

    d.pratique('Pratique', "Où est la réponse ?",
               "Nommez le passage de l'avis qui répond à la question.", [
        ("Quel est l'objet de la lettre ?", "Avis d'admission conditionnelle"),
        ("Qu'est-ce que le centre réserve, et pour quel groupe ?", "une place dans le groupe du 2 mars"),
        ("Quelle est exactement la condition ?", "fournir la preuve de réussite du test"),
        ("Qu'arrive-t-il le 6 février si rien n'a été déposé ?", "la place réservée est libérée"),
        ("À qui faut-il s'adresser pour une question ?", "à madame Dostie, au poste 4412"),
    ], corrige=True,
       notes="C'est l'exercice du type « texte » du module interactif, fait ici à "
             "l'oral. Demander de pointer le passage sur la copie papier avant de "
             "répondre : le geste compte autant que la réponse.")

    d.piege('Lecture',
            "lire le début et refermer la feuille",
            "lire jusqu'à la date qui oblige",
            "La bonne nouvelle est en haut, l'obligation est au milieu. C'est "
            "l'ordre habituel d'un avis, et il n'est pas fait pour vous "
            "piéger : la politesse veut qu'on annonce d'abord ce qui est "
            "accordé. Mais le résultat est le même si vous vous arrêtez là.",
            notes="Demander qui, dans le groupe, a déjà lu seulement le début d'une "
                  "lettre officielle. Beaucoup de mains. Dédramatiser, puis donner la "
                  "méthode comme un outil, pas comme un reproche.")

    d.pratique('Pratique', "Que dit la mise en page ?",
               "Associez chaque endroit à ce qu'il vous apprend.", [
        ("Le nom en haut à gauche", "quel établissement parle"),
        ("La ligne en gras sous l'en-tête", "le genre du document"),
        ("La suite de chiffres en petit", "le numéro de dossier, à donner au téléphone"),
        ("Le passage entouré d'un trait", "la condition ou la date à ne pas manquer"),
        ("Le blanc entre deux paragraphes", "un changement d'idée"),
        ("La dernière ligne avant la signature", "à qui s'adresser"),
    ], corrige=True, cols=2,
       notes="Terminer sur le blanc entre les paragraphes : c'est le point qui sert "
             "directement à la production écrite de E2, où l'on demandera trois "
             "paragraphes séparés.")

    d.billet(
        "Note dans ton agenda la date qui t'oblige, cette session.",
        exemples=[
            "Une date d'inscription, de remise, de rendez-vous.",
            "Écris à côté ce qui arrive si tu la manques.",
        ],
        notes="Trois minutes. Certains élèves n'auront aucune date : leur faire "
              "écrire celle de la remise de la production écrite du module. Le geste "
              "est ce qui compte.")

    return d.save(dossier)
