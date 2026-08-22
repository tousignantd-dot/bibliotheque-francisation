# -*- coding: utf-8 -*-
"""B1 · Au comptoir du secrétariat
Bloc B « Défi 1 · Prévenir de son absence » · couleur acier · 75 min.
Source du module : dialogue `t1`, exercice `t1a`.
"""
import os
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n5-ecole/images/')


def img(nom):
    chemin = IMG + nom
    return chemin if os.path.exists(chemin) else None


def build(dossier):
    d = Deck(
        code='B1', section='acier',
        titre="Au comptoir du secrétariat",
        chapeau="Amelia se présente enfin. Elle a environ deux minutes, il y "
                "a du monde derrière elle, et la personne au comptoir ne la "
                "connaît pas. L'ordre de ce qu'elle dit compte autant que "
                "ce qu'elle dit.",
        duree='75 minutes')

    d.titre(notes="Première séance du défi 1. Commencer par redonner aux élèves le billet "
                  "de sortie de A4 : c'est leur propre phrase d'ouverture, et elle va "
                  "servir tout de suite.")

    d.objectifs([
        "exposer une absence prévue dans l'ordre attendu au comptoir ;",
        "donner les dates avant le motif, et le motif en une seule phrase ;",
        "comprendre ce que la personne au comptoir peut décider et ne peut pas ;",
        "repartir en redisant ce qu'on doit faire et pour quand.",
    ], notes="Le deuxième objectif est celui qui surprend. Beaucoup de cultures — et "
             "beaucoup de gens — commencent par la raison, par politesse. Ici, la raison "
             "vient après les dates, et ce n'est pas de la froideur : c'est ce qui entre "
             "dans le système.")

    d.declencheur(
        'Observation', "Vous avez deux minutes au comptoir. "
                       "Par quoi commencez-vous ?",
        image=img('formulaire-comptoir.jpg'),
        pistes=[
            "Est-ce que la personne devant vous sait qui vous êtes ?",
            "Qu'est-ce qu'elle doit ouvrir dans son système avant de vous écouter ?",
            "Si vous commencez par la raison, que se passe-t-il ?",
            "Qu'est-ce que vous voulez avoir en main en repartant ?",
        ],
        notes="Laisser le groupe proposer un ordre, l'écrire au tableau, puis le "
              "comparer à celui du dialogue. L'écart est toujours le même : la raison "
              "arrive trop tôt et le nom trop tard.")

    d.dialogue('Dialogue · 1 de 3', "Je viens vous annoncer une absence", [
        ("AMELIA", "Bonjour. Je m'appelle Amelia Dumitrescu, groupe 4, "
                   "francisation.", True),
        ("JOCELYNE", "Bonjour. Qu'est-ce que je peux faire pour vous, madame "
                     "Dumitrescu ?", True),
        ("AMELIA", "Je viens vous annoncer une absence. Une longue absence, "
                   "prévue.", True),
        ("JOCELYNE", "Prévue, c'est déjà une bonne nouvelle. À partir de "
                     "quand ?", True),
    ], consigne="Écoutez d'abord, diapositive masquée.",
       notes="Neuf mots dans la première réplique, et le dossier est ouvert. Faire "
             "compter les mots au groupe : c'est ce qui convainc le mieux qu'une bonne "
             "ouverture est courte.")

    d.dialogue('Dialogue · 2 de 3', "Les dates, puis le motif", [
        ("AMELIA", "À partir du 9 mars, et je reviendrai le 30. Trois "
                   "semaines.", True),
        ("JOCELYNE", "Trois semaines. Et le motif, madame ?", True),
        ("AMELIA", "Ma mère est opérée à Bucarest. Je suis seule à pouvoir y "
                   "aller.", True),
        ("JOCELYNE", "Je comprends. Vous devrez me le mettre par écrit, par "
                     "exemple.", True),
    ], notes="Le motif tient en une phrase et demie, sans détail médical. Le faire "
             "remarquer : ni le formulaire ni la personne au comptoir n'en demandent "
             "davantage, et en donner plus n'aide pas la demande.")

    d.dialogue('Dialogue · 3 de 3', "Ce qu'elle ne décide pas", [
        ("AMELIA", "Je voudrais savoir si je garde ma place dans le groupe.", True),
        ("JOCELYNE", "Oui, si l'absence est motivée et annoncée d'avance. "
                     "C'est votre cas.", True),
        ("AMELIA", "Et mon allocation de participation, elle continue ?", True),
        ("JOCELYNE", "Ça, je ne le décide pas. Monsieur Gauthier vous "
                     "répondra là-dessus.", False),
    ], notes="La dernière réplique remet en scène la règle de A1 : trois portes, trois "
             "questions. Ce n'est pas un refus, c'est un aiguillage — et l'élève doit "
             "apprendre à l'entendre ainsi plutôt que comme une fin de non-recevoir.")

    d.regle("L'ordre du comptoir",
            "Qui je suis. Ce que je viens faire. À partir de quand, jusqu'à "
            "quand. Pourquoi. Ce que je demande.",
            precision="Cinq morceaux, dans cet ordre. Le cinquième est le seul "
                      "qui peut attendre : les quatre autres, non.",
            notes="Diapositive à photographier. Elle est le cœur du bloc B et elle "
                  "revient en B4 et en E1. La faire recopier à la main dans le cahier.")

    d.tableau('Deux ouvertures', "La même personne, deux minutes plus tard",
              ['Ce qui fait perdre du temps', 'Ce qui en fait gagner'],
              [["Bonjour, j'ai un problème.",
                "Bonjour, Amelia Dumitrescu, groupe 4."],
               ["C'est compliqué à expliquer.",
                "Je viens annoncer une absence prévue."],
               ["Je pars bientôt, un bon bout de temps.",
                "Du 9 au 27 mars inclusivement."],
               ["C'est pour des raisons familiales, ma mère...",
                "Ma mère est opérée à l'étranger."]],
              cle=1,
              notes="Faire compléter la colonne de droite avant de l'afficher. Ne pas "
                    "ridiculiser la colonne de gauche : c'est ce que tout le monde dit "
                    "la première fois, y compris les gens nés ici.")

    d.piege("Croire qu'il faut se justifier longuement",
            "Je vais tout expliquer pour qu'ils comprennent bien.",
            "Je donne le motif en une phrase, et je réponds si on m'en demande plus.",
            "Une longue justification allonge la file, brouille les dates et donne "
            "l'impression qu'on demande une faveur. Une absence motivée et annoncée "
            "d'avance est un droit, pas une faveur.",
            notes="Ce piège est culturel autant que linguistique. Le nommer explicitement "
                  "évite que les élèves lisent la brièveté comme de la sécheresse.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après le dialogue.", [
        ("Amelia donne son nom et son groupe dès la première phrase.", "vrai"),
        ("Son absence commence le 9 mars.", "vrai"),
        ("Elle a déjà le papier de l'hôpital en main.",
         "faux — elle l'aura au retour"),
        ("Elle doit mettre sa demande par écrit.", "vrai"),
        ("Madame Paradis décide de l'allocation de participation.",
         "faux — c'est monsieur Gauthier"),
        ("Une absence motivée et annoncée d'avance conserve la place.", "vrai"),
    ], corrige=True,
       notes="Faire justifier par la réplique exacte. La cinquième est celle que le "
             "groupe manque : on suppose que la personne au comptoir peut tout.")

    d.billet(
        "Écrivez les deux dates de votre absence, avec « à partir du » et « jusqu'au ».",
        exemples=[
            "Une absence inventée fait très bien l'affaire.",
            "Ajoutez « inclusivement » à la seconde date.",
        ],
        notes="Ramasser les billets. Le mot « inclusivement » manquera presque partout : "
              "c'est ce qui ouvre la séance C3.")

    return d.save(dossier)
