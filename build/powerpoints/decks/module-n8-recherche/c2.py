# -*- coding: utf-8 -*-
"""C2 · Lire un profil d'entreprise
Bloc C « Défi 2 » · couleur ambre · 75 min.
Source : exercice `t2profil` (type `texte`) et sa mini-leçon.
Intention du programme : s'informer sur une entreprise ou sur un emploi en
lisant.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C2', section='ambre',
        titre="Un texte écrit pour rassurer",
        chapeau="Une page « À propos » n'est pas un document d'information : "
                "c'est un document de présentation, relu par quelqu'un dont "
                "le métier est d'éviter les ennuis.",
        duree='75 minutes')

    d.titre(notes="Première des deux séances de lecture. Distribuer le profil de "
                  "Boréalis sur papier : le texte se travaille au crayon, pas à "
                  "l'écran.")

    d.objectifs([
        "prélever un fait récent, un chiffre et une difficulté avouée ;",
        "reconnaître une phrase passive et dire ce qu'elle n'apprend pas ;",
        "distinguer une valeur affichée d'une pratique mesurée ;",
        "tirer trois questions d'un texte qui n'en pose aucune.",
    ], notes="Le quatrième objectif est la sortie de la séance : on ne lit pas pour "
             "se rassurer, on lit pour repartir avec des questions.")

    d.declencheur(
        'Observation', "Cette phrase dit-elle quelque chose ?",
        pistes=[
            "« Nous plaçons l'humain au centre de nos décisions. »",
            "Écrivez la phrase contraire. Est-ce qu'une entreprise l'écrirait ?",
            "« Un taux de roulement de onze pour cent, inférieur à la moyenne. »",
            "Même question. Laquelle des deux pourrait être fausse ?",
        ],
        notes="Le test est là et il est imparable : si la phrase inverse serait "
              "absurde à écrire, la phrase ne dit rien. Aucune entreprise n'écrit "
              "« nous méprisons l'humain ».")

    d.regle("Les faits datés sont les seuls solides",
            "Une année, un effectif, un pourcentage, un montant : ce sont les "
            "seuls éléments qu'on ne peut pas arranger sans mentir. "
            "Prélevez-les et laissez le reste.",
            precision="Réal Bourbonnais l'annonce lui-même dans le module : « à "
                      "l'entrevue individuelle, je pose toujours une question tirée "
                      "du profil de l'entreprise ». Ce n'est pas une menace, c'est un "
                      "mode d'emploi.",
            notes="Diapositive à photographier. Faire noter la différence entre citer "
                  "l'année de fondation, que tout le monde peut lire en dix secondes, "
                  "et citer le fait récent, qui suppose qu'on a lu.")

    d.cartes('Analyse', "Quatre choses à repérer dans un profil", [
        ("Le fait daté",
         "Fondée en 1985. Deux cent dix personnes, dont cent trente-quatre à "
         "la production. Le carnet a doublé en dix-huit mois. On les note, on "
         "les replace, et cela prouve qu'on a lu."),
        ("La phrase sans sujet",
         "L'entreprise a été acquise. Une réorganisation a été menée. Ces "
         "tournures ne disent pas qui a décidé, et c'est souvent exactement "
         "le renseignement qui manque. Chaque passif est une question."),
        ("La valeur affichée",
         "Le respect, l'excellence, l'esprit d'équipe : dans neuf profils sur "
         "dix. Ce qui vaut quelque chose est une pratique nommée, avec un "
         "chiffre à côté."),
        ("La difficulté avouée",
         "La supervision du soir s'exerce sans soutien sur place. Quand un "
         "profil reconnaît une contrainte, il vous dit ce qui inquiète "
         "l'employeur. C'est le meilleur renseignement du document."),
    ], notes="Faire chercher les quatre dans le profil de Boréalis, au crayon, par "
             "groupes de deux. Dix minutes suffisent.")

    d.pratique('Pratique 1 de 2', "Où est-ce écrit ?",
               "Retrouvez dans le profil le passage qui répond.", [
        ("En quelle année l'entreprise a-t-elle été fondée, et par qui ?", "en 1985, par les frères Deslauriers"),
        ("Combien de personnes y travaillent, et combien à la production ?", "deux cent dix, dont cent trente-quatre"),
        ("Qui a racheté l'entreprise, et d'où vient ce groupe ?", "le Groupe Landron, de Mississauga"),
        ("À quel taux les chaînes du soir tournent-elles, et que comprend ce taux ?", "quatre-vingt-deux pour cent, arrêts planifiés exclus"),
        ("Quelle difficulté du poste le profil reconnaît-il ?", "la supervision sans soutien après dix-huit heures"),
    ], corrige=True,
       notes="Exercice de repérage, pas de compréhension : le mot exact du texte est "
             "la seule réponse acceptée. C'est ce que fait l'exercice interactif, où "
             "l'élève clique dans le texte.")

    d.tableau('Analyse', "Le passif, et la question qu'il donne",
              ['Ce qui est écrit', 'Ce qui manque'],
              [["L'entreprise a été acquise en janvier.",
                "par qui, et à l'initiative de qui"],
               ["La production a été réorganisée en trois quarts.",
                "qui l'a décidé, et sur quel avis"],
               ["Le poste a été créé.",
                "à la demande de qui, et pour combien de temps"]],
              cle=0,
              note="Notez chaque passif que vous rencontrez : la liste que vous en tirez est votre liste de questions.",
              notes="Diapositive à photographier. Le passif n'est pas une ruse : c'est "
                    "la langue normale des documents d'entreprise. Mais il efface "
                    "celui qui agit, et c'est souvent ce qu'on voudrait savoir.")

    d.pratique('Pratique 2 de 2', "Dit ou ne dit rien ?",
               "Pour chaque phrase, décidez si elle renseigne.", [
        ("Une entreprise à échelle humaine.", "ne dit rien"),
        ("Un taux de roulement de onze pour cent.", "renseigne"),
        ("Nous plaçons l'humain au centre.", "ne dit rien"),
        ("Sept personnes en poste sur les seize prévues.", "renseigne"),
        ("Une équipe passionnée et dynamique.", "ne dit rien"),
        ("Aucun produit n'est vendu au grand public.", "renseigne"),
    ], corrige=True,
       notes="Appliquer le test du déclencheur à chaque phrase : la version inverse "
             "serait-elle absurde ? Si oui, la phrase ne distingue rien.")

    d.billet(
        "Reprenez la page « À propos » de votre devoir et écrivez trois questions qu'elle vous laisse.",
        exemples=[
            "Une tirée d'un passif.",
            "Une tirée d'un chiffre dont vous ne savez pas ce qu'il recouvre.",
        ],
        notes="Devoir. Ces questions se posent telles quelles en entrevue, et elles "
              "distinguent immédiatement celui qui a lu de celui qui a survolé.")

    return d.save(dossier)
