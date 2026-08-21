# -*- coding: utf-8 -*-
"""A4 · Les mots du poste.
Bloc A « Je découvre » · couleur framboise · 60 min. Fin du bloc A.
Source : `FC_CARDS` (section prep), exercices `prVocab`, `prImg`, `prTaches`.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n8-emploi/images/')


def build(dossier):
    d = Deck(
        code='A4', section='framboise',
        titre="Les mots du poste",
        chapeau="Seize mots pour tout le module, quatre pour aujourd'hui. "
                "Ils ont un point commun : ils décrivent ce qu'on fait, pas ce "
                "qu'on est.",
        duree='60 minutes')

    d.titre(notes="Séance de vocabulaire et de consolidation du bloc A. Aucun point de "
                  "grammaire neuf. Les quatre mots du jour reviendront dans les trois "
                  "défis.")

    d.objectifs([
        "employer les quatre mots du poste dans une phrase à soi ;",
        "relier une image de milieu de travail à ce qu'elle montre ;",
        "relier chaque bloc de tâches à sa règle chiffrée ;",
        "réviser le découpage en groupes de souffle sur ces mots.",
    ])

    d.vocabulaire('Famille 1', "Le poste et les tâches",
                  [("une description de tâches", "Le document qui énumère tout ce qu'on doit faire dans son poste."),
                   ("un supérieur immédiat", "La personne à qui on rend des comptes directement, celle qui tranche."),
                   ("faire le suivi", "Reprendre un dossier commencé pour le faire avancer."),
                   ("un imprévu", "Ce qui arrive sans avoir été planifié et oblige à changer sa journée.")],
                  notes="Faire répéter avec l'article. « Faire le suivi » est le seul "
                        "verbe de la liste : le faire conjuguer au présent et à "
                        "l'imparfait.")

    d.cartes("Quatre mots, quatre usages", "Comment on s'en sert vraiment", [
        ("une description de tâches",
         "On la demande quand on entre en poste, et on la ressort quand on vous confie autre chose."),
        ("un supérieur immédiat",
         "On lui parle avant d'aller plus haut. Sauter un échelon coûte cher, même quand on a raison."),
        ("faire le suivi",
         "Le geste qui distingue un employé qu'on rappelle : personne n'a eu à le lui demander."),
        ("un imprévu",
         "Ce n'est pas une urgence. On l'absorbe, on prévient la personne concernée, et on continue."),
    ], notes="Demander un exemple vécu pour chaque carte. Le vocabulaire s'ancre par "
             "l'anecdote, jamais par la définition seule.")

    d.declencheur(
        'Observation', "Que se passe-t-il dans cette salle ?",
        image=IMG + 'salle-reunion.jpg',
        pistes=[
            "Qu'est-ce qui est posé au centre de la table ?",
            "Combien de personnes sont attendues ?",
            "À quoi sert le tableau du fond ?",
            "Cette salle existe-t-elle là où vous travaillez ?",
        ],
        notes="Cette image annonce le Défi 2. On ne nomme pas encore « ordre du jour » "
              "ni « compte rendu » : on laisse le groupe le décrire avec ses mots.")

    d.tableau('Révision', "Le bloc de tâches et sa règle",
              ['Le bloc', 'La règle'],
              [["La réception des commandes", "avant midi ; après, on avertit"],
               ["Le suivi des livraisons", "mardi et jeudi ; prévenir le client"],
               ["Les factures des fournisseurs", "moins de 25 $ : on approuve seul"],
               ["La réunion de production", "compte rendu dans les deux jours"]],
              cle=0,
              note="Quatre lignes qui résument huit mois de travail.",
              notes="Reprise de A1, de mémoire cette fois : masquer la colonne de droite "
                    "et faire reconstituer.")

    d.pratique('Vocabulaire', "Le mot juste",
               "Complétez avec le mot de la liste.", [
        ("Elle a demandé sa ___ dès son premier jour.", "description de tâches"),
        ("Avant d'écrire à la direction, parlez-en à votre ___ .", "supérieur immédiat"),
        ("Le mardi et le jeudi, elle ___ des livraisons.", "fait le suivi"),
        ("Un bon reçu à deux heures est un ___ , pas une urgence.", "imprévu"),
        ("Ce dossier traîne : personne n'en a ___ .", "fait le suivi"),
        ("Mon ___ approuve les écarts de plus de vingt-cinq dollars.", "supérieur immédiat"),
    ], corrige=True,
       notes="Le troisième et le cinquième item emploient le même verbe à deux temps "
             "différents. Le faire remarquer plutôt que de le corriger.")

    d.billet(
        "Écrivez trois phrases sur votre propre travail, une par mot.",
        exemples=[
            "Employez « faire le suivi » à l'imparfait.",
            "Nommez un imprévu qui vous est arrivé cette semaine.",
        ],
        notes="Ramasser les billets : ils donnent une photographie du groupe avant "
              "d'entrer dans le Défi 1, qui est le plus exigeant du module.")

    return d.save(dossier)
