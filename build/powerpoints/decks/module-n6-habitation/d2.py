# -*- coding: utf-8 -*-
"""D2 · Poser la condition, poser la question
Bloc D « Défi 3 · Quand le plan change » · couleur teal · 75 min.
Source : exercices `t3si`, `t3quest` et `t3conn`, et leurs mini-leçons. Savoirs
du programme : exprimer la condition dans une hypothèse avec le marqueur si ;
employer quel, quelle, quels, quelles ; employer des phrases subordonnées
infinitives interrogatives ; employer des connecteurs de points de vue et
d'exemplification.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='D2', section='teal',
        titre="Poser la condition, poser la question",
        chapeau="« C'est long ? » obtient « ça dépend ». « Combien de jours "
                "ouvrables entre l'injection et le gypse ? » obtient un "
                "nombre, et ce nombre s'écrit.",
        duree='75 minutes')

    d.titre(notes="Dernière séance avant « Je me lance », et la plus utile de tout le "
                  "module. Ressortir les billets de A1 : la plupart avaient écrit "
                  "« combien ça coûte », et on va voir pourquoi ça ne suffit pas.")

    d.objectifs([
        "poser une hypothèse avec « si » sans mettre de futur après ;",
        "poser une question avec quel, quelle, quels, quelles ;",
        "poser une question indirecte : je voudrais savoir quoi faire ;",
        "annoncer un exemple ou un avis avec le bon connecteur.",
    ], notes="Trois points en une séance, c'est beaucoup. Le premier et le deuxième "
             "sont les priorités ; le troisième se rattrape en E1 si le temps manque.")

    d.declencheur(
        'Observation', "« Est-ce que ce sera prêt le 12 mai ? » Que peut répondre un entrepreneur honnête ?",
        pistes=[
            "De quoi dépend la réponse ?",
            "Comment poser la question autrement ?",
            "Qu'est-ce qui change si on ajoute « si le permis sort dans dix jours » ?",
        ],
        notes="C'est exactement ce que fait Doïna dans le dialogue de D1. Relire sa "
              "réplique avant de continuer : elle pose la condition avant de "
              "demander la date.")

    d.tableau('Analyse', "L'hypothèse réaliste avec « si »",
              ['Après si', 'Après la virgule'],
              [["le présent", "le futur : le sous-sol sera prêt"],
               ["le présent", "le présent : vous refaites tout"],
               ["le présent", "l'impératif : appelez-moi"],
               ["le passé composé", "le présent : ce n'est pas dans le prix"]],
              cle=0,
              note="Jamais de futur juste après « si ». Le futur va de l'autre côté de la virgule.",
              notes="Diapositive à photographier. La note est la règle en une ligne, et "
                    "c'est la faute la plus fréquente de tous les niveaux.")

    d.regle("Une décision de chantier se prend en hypothèses",
            "On ne demande pas ce qui arrivera : on demande ce qui arrivera si.",
            precision="Deux solutions, deux prix, deux délais, un permis qui prendra "
                      "le temps qu'il prendra, et une pluie que personne ne contrôle. "
                      "« Si le permis sort dans dix jours, est-ce que ce sera prêt le "
                      "12 ? » est la seule question à laquelle un homme de métier "
                      "honnête peut répondre. Et sa réponse, elle, vous engage tous "
                      "les deux.",
            notes="Diapositive à photographier. C'est la règle du bloc D.")

    d.pratique('Pratique', "Poser la condition",
               "Complétez avec le temps qui convient.", [
        ("Si le permis ___ (sortir) dans dix jours, le sous-sol sera prêt.", "sort"),
        ("Si l'eau revient un jour, vous ___ (refaire) tout le plancher.", "referez"),
        ("Si je ne signe pas avant le 15, la soumission ___ (ne plus être) valide.", "ne sera plus"),
        ("Si quelqu'un ___ (condamner) le puisard avant nous, ce n'est pas dans le prix.", "a condamné"),
        ("Si le mur n'est pas sec, ___ (ne pas refermer) les cloisons.", "ne refermez pas"),
        ("S'il ___ (pleuvoir) trois semaines de suite, l'échéancier saute.", "pleut"),
    ], corrige=True,
       notes="Faire relire chaque phrase entière à voix haute après correction. C'est "
             "le rythme des deux moitiés qui installe la règle, pas la règle "
             "elle-même.")

    d.tableau('Analyse', "Deux façons de poser une vraie question",
              ['La forme', 'Un exemple'],
              [["quel + nom", "Quelle garantie donnez-vous ?"],
               ["quels au pluriel", "Quels travaux ne sont pas compris ?"],
               ["savoir + infinitif", "Je voudrais savoir quoi faire si l'eau revient."],
               ["savoir + mot interrogatif", "J'aimerais savoir quand payer."]],
              cle=0,
              note="La question indirecte ne prend pas de point d'interrogation.",
              notes="Diapositive à photographier. La forme indirecte passe mieux au "
                    "téléphone et par écrit ; la directe va plus vite en réunion. "
                    "Les deux valent.")

    d.pratique('Pratique', "De la question vague à la question précise",
               "Récrivez la question pour qu'elle obtienne une réponse.", [
        ("C'est long, vos travaux ?", "Combien de jours ouvrables entre l'injection et le gypse ?"),
        ("Il y a une garantie ?", "Quelle garantie donnez-vous, et pour combien de temps ?"),
        ("Ça va coûter plus cher ?", "Quel montant s'ajoute si vous trouvez un imprévu ?"),
        ("Vous faites quoi si vous trouvez autre chose ?", "Je voudrais savoir quoi faire dans ce cas-là."),
        ("Ce n'est pas compris, ça ?", "Quels travaux ne sont pas compris ?"),
    ], corrige=True,
       notes="Exercice central de la séance. Le point à répéter à chaque correction : "
             "une bonne question contient un chiffre, une date ou un document.")

    d.piege('Piège', "faire semblant de connaître un mot",
            "demander ce qu'il veut dire",
            "« Qu'est-ce que ça veut dire, reprofiler ? » Personne n'a jamais perdu "
            "d'argent en posant cette question. Beaucoup en ont perdu en hochant la "
            "tête. Un homme de métier explique volontiers son vocabulaire : il ne "
            "l'emploie pas pour impressionner, il l'emploie parce que c'est le sien.",
            notes="Faire pratiquer la phrase à voix haute, deux par deux. Elle est plus "
                  "difficile à dire qu'à comprendre, et c'est pour ça qu'on la "
                  "répète.")

    d.tableau('Analyse', "Annoncer un exemple, annoncer un avis",
              ['La famille', 'Les mots'],
              [["un exemple", "par exemple, notamment, entre autres, ainsi"],
               ["mon avis", "à mon avis, selon moi, personnellement"],
               ["l'avis d'un autre", "d'après l'inspectrice, selon Fernand"],
               ["celui d'un document", "d'après la soumission, selon le rapport"]],
              cle=0,
              note="Devant quelqu'un que vous payez, séparer le fait de l'opinion vaut de l'argent.",
              notes="Diapositive à photographier. « Notamment » ne veut pas dire "
                    "« surtout » : c'est l'erreur à corriger si le temps le permet.")

    d.billet(
        "Écris les deux questions que tu poserais avant de signer.",
        exemples=[
            "Chacune doit contenir un chiffre, une date ou un document.",
            "Emploie « quel » dans au moins une des deux.",
        ],
        notes="Cinq minutes cette fois, pas trois. Ces deux questions sont exactement "
              "ce qu'on demandera en E1 : les garder et les rendre à leurs auteurs "
              "la séance suivante.")

    return d.save(dossier)
