# -*- coding: utf-8 -*-
"""A3 · Les mots du premier jour.
Bloc A « Je découvre » · couleur teal · 60 min.
Source : exercices `prImg` et `prNom`, cartes mémoire.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n1-presenter/images/')


def build(dossier):
    d = Deck(
        code='A3', section='teal',
        titre='Les mots du premier jour',
        chapeau="Douze mots suffisent pour la première journée : le nom, le "
                "pays, la langue, la famille — et trois mots de politesse.",
        duree='60 minutes')

    d.titre(notes="Séance de vocabulaire. Elle clôt le bloc A et prépare les deux défis.")

    d.objectifs([
        "nommer ce qu'on demande sur un formulaire ;",
        "dire son pays et sa langue ;",
        "comprendre les mots « prénom », « nom de famille », « adresse » ;",
        "reconnaître ces mots à l'écrit.",
    ])

    d.declencheur(
        'Observation', "Qu'est-ce qu'on écrit dans ces cases ?",
        image=IMG + 'formulaire.jpg',
        pistes=[
            "Combien de cases voyez-vous ?",
            "Qu'est-ce qu'on demande en premier ?",
            "Avez-vous déjà rempli un formulaire ici ?",
            "Qu'est-ce qui était difficile ?",
        ],
        notes="Presque tous auront rempli un formulaire en arrivant au Québec. Laisser "
              "raconter : c'est l'expérience commune du groupe.")

    d.tableau('Analyse', "Ce qu'on demande",
              ['Le mot', "Ce qu'on écrit"],
              [["prénom", "Amina"],
               ["nom de famille", "Benali"],
               ["adresse", "4520, rue Bélanger"],
               ["pays d'origine", "Algérie"]],
              cle=0,
              note="Ici, le prénom vient toujours en premier.",
              notes="Diapo à photographier. Faire remplir un formulaire vierge en classe, "
                    "au tableau, tous ensemble.")

    d.cartes("Le pays et la langue", "Deux mots qui vont ensemble", [
        ("Le pays",
         "D'où vous venez : l'Algérie, le Vietnam, la Colombie, Haïti. « Je viens "
         "d'Algérie. »"),
        ("La langue",
         "Ce que vous parlez : l'arabe, le vietnamien, l'espagnol, le créole. « Je parle "
         "arabe. »"),
        ("Ce n'est pas la même chose",
         "On peut venir d'un pays et parler plusieurs langues. Dites-les toutes : c'est "
         "une force, pas une complication."),
    ], notes="Faire dire à chaque élève son pays et ses langues. Écrire les pays du "
             "groupe au tableau : c'est une carte de la classe.")

    d.tableau('Analyse', "La famille",
              ['Le mot', 'Un exemple'],
              [["un enfant", "J'ai un enfant."],
               ["un fils", "J'ai un fils."],
               ["une fille", "J'ai une fille."],
               ["pas d'enfants", "Je n'ai pas d'enfants."]],
              cle=3,
              note="À la négation, « un » devient « d' » : je n'ai pas d'enfants.",
              notes="Ne pas expliquer la règle de la négation à ce stade : la faire "
                    "répéter comme un bloc.")

    d.regle("Trois mots de politesse",
            "Bonjour, merci, pardon.",
            precision="Ce sont les trois premiers mots à savoir. On les emploie partout, "
                      "tous les jours, et ils suffisent à être poli même quand on ne peut "
                      "rien dire d'autre.",
            notes="Diapo à photographier. Le défi 2 les reprendra en détail.")

    d.pratique('Pratique · 1 de 2', "Le mot juste",
               "Complétez.", [
        ("— Comment vous appelez-vous ? — Je m'___ Amina.", "appelle"),
        ("Pouvez-vous ___ votre nom ?", "épeler"),
        ("Son nom de ___ est Benali.", "famille"),
        ("— Merci. — De ___ .", "rien"),
    ], corrige=True, cols=1,
       notes="Utiliser l'exercice 4 du module.")

    d.pratique('Pratique · 2 de 2', "À deux · la fiche",
               "L'un pose les questions, l'autre répond et écrit.", [
        ("Question 1", "Comment vous appelez-vous ?"),
        ("Question 2", "Pouvez-vous épeler votre nom de famille ?"),
        ("Question 3", "D'où venez-vous ?"),
        ("Question 4", "Quelles langues parlez-vous ?"),
    ], cols=1,
       notes="Vingt minutes. Chacun repart avec la fiche de son voisin, écrite par son "
             "voisin : les erreurs d'épellation sautent aux yeux.")

    d.billet(
        "Écrivez les mots du premier jour dans votre langue et en français.",
        exemples=[
            "Prénom, nom de famille, adresse, pays, langue.",
            "Gardez cette liste : elle sert à chaque formulaire.",
        ],
        notes="Fin du bloc A. Ce billet devient un outil que l'élève garde dans son sac.")

    return d.save(dossier)
