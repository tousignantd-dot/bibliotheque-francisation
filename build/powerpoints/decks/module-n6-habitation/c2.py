# -*- coding: utf-8 -*-
"""C2 · Onze pages qu'on ne lit jamais en entier
Bloc C « Défi 2 · Les papiers du chantier » · couleur ambre · 75 min.
Source : exercice `t2rapport` (type texte) et sa mini-leçon, exercice `t2ps` et
la sienne. Savoirs du programme : tenir compte de la présentation matérielle
et de la mise en page ; reconnaître les verbes courants au passé simple à la
3e personne et les associer au passé composé.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C2', section='ambre',
        titre="Onze pages qu'on ne lit jamais en entier",
        chapeau="Un rapport d'inspection est fait pour qu'on y retrouve une "
                "chose précise, deux ans plus tard, au téléphone, pendant "
                "qu'un entrepreneur attend au bout du fil.",
        duree='75 minutes')

    d.titre(notes="Séance de lecture. Le module porte l'exercice en type « texte » : "
                  "l'élève clique dans le rapport le passage qui répond. Ici, sur "
                  "papier, faire souligner au crayon — le geste est le même et il "
                  "s'installe mieux à la main.")

    d.objectifs([
        "repérer une section par son numéro plutôt que par sa page ;",
        "trouver la section des limites et dire ce qu'elle change ;",
        "reconnaître un passé simple et le traduire en passé composé ;",
        "distinguer « non vérifié » de « en bon état ».",
    ], notes="Le quatrième objectif est le plus important de la séance, et il n'a "
             "rien de grammatical. Y consacrer du temps.")

    d.declencheur(
        'Observation', "« La présence d'une membrane n'est ni confirmée ni infirmée. » Qu'est-ce que ça veut dire ?",
        pistes=[
            "Y a-t-il une membrane, oui ou non ?",
            "Pourquoi l'inspectrice écrit-elle une phrase pareille ?",
            "Qu'est-ce que ça change pour celui qui achète ?",
        ],
        notes="La phrase est authentiquement difficile, et c'est voulu. La réponse — "
              "on ne sait pas — surprend toujours : plusieurs élèves la lisent comme "
              "« il n'y en a pas ».")

    d.tableau('Analyse', "Ce que la présentation dit avant les phrases",
              ['Le signal', 'Ce qu\'il annonce'],
              [["un titre en majuscules", "une section commence"],
               ["un numéro devant", "on pourra y revenir en le citant"],
               ["un chiffre et une unité", "ça se remesure et ça se compare"],
               ["le mot « limites »", "ce qui n'a pas pu être vu"]],
              cle=0,
              note="Au téléphone, on ne dit pas « la page du mur » : on dit « la section 2 ».",
              notes="Diapositive à photographier. La note est une phrase à faire "
                    "pratiquer : citer un numéro fait immédiatement prendre au "
                    "sérieux.")

    d.tableau('Analyse', "Ce qu'un rapport ne fait pas",
              ['Il ne fait pas', 'Conséquence pour vous'],
              [["chiffrer les travaux", "le prix se cherche dans la soumission"],
               ["recommander quelqu'un", "le choix reste le vôtre, et c'est mieux"],
               ["voir derrière les murs", "ce qui est fermé n'est pas garanti"],
               ["valoir plus tard", "il décrit l'état à une date précise"]],
              cle=0,
              note="Ce qu'il ne fait pas est exactement ce qui lui donne sa valeur.",
              notes="Diapositive à photographier. Reprise volontaire du tableau de A4 : "
                    "le groupe l'a vu il y a deux semaines, et il le comprend "
                    "autrement maintenant qu'il a le rapport sous les yeux.")

    d.regle("« Non vérifié » n'est pas « en bon état »",
            "Un rapport honnête écrit ce qu'il n'a pas pu voir.",
            precision="La dalle de la maison de Doïna n'avait aucune membrane en "
                      "dessous, et le rapport ne l'avait pas dit : il avait écrit "
                      "qu'il n'avait pas pu le vérifier. Ce n'est pas une faute de "
                      "l'inspectrice, c'est la limite d'une inspection visuelle. "
                      "Celui qui lit doit faire la différence, parce que c'est lui "
                      "qui paiera l'imprévu.",
            notes="Diapositive à photographier. C'est la règle de la séance, et elle "
                  "prépare directement le bloc D.")

    d.pratique('Lecture', "Où est la réponse ?",
               "Dites dans quelle section du rapport chaque réponse se trouve.", [
        ("En quelle année la maison a-t-elle été construite ?", "section 1, historique"),
        ("Quel défaut a été relevé dans la fondation ?", "section 2, fondation et drainage"),
        ("Quel est le taux d'humidité du mur nord ?", "section 2, phrase chiffrée"),
        ("Qu'est-ce qui envoie l'eau vers la fondation ?", "section 2, fin du paragraphe"),
        ("Qu'est-ce qui n'a pas pu être vérifié sous le sous-sol ?", "section 3, sous-sol"),
        ("Pourquoi certaines choses n'ont-elles pas été vues ?", "section 4, limites"),
    ], corrige=True,
       notes="Le même exercice existe dans le module, où l'élève clique dans le texte. "
             "Ici, faire souligner au crayon sur la fiche : huit passages, huit "
             "questions.")

    d.tableau('Analyse', "Le passé qu'on lit et qu'on n'entend jamais",
              ['Le rapport écrit', 'Vous diriez'],
              [["fut construite", "a été construite"],
               ["refirent la toiture", "ont refait la toiture"],
               ["remplacèrent", "ont remplacé"],
               ["ne fut consignée", "n'a pas été consignée"]],
              cle=0,
              note="Le programme demande de le reconnaître, jamais de l'écrire.",
              notes="Diapositive à photographier. Rassurer explicitement : personne ne "
                    "sera évalué sur la production du passé simple. La note le dit, "
                    "et il faut le redire à voix haute.")

    d.pratique('Pratique', "Traduire le passé des documents",
               "Donnez la forme que vous emploieriez en parlant.", [
        ("l'inspectrice releva une fissure", "a relevé"),
        ("le sol se tassa peu à peu", "s'est tassé"),
        ("quelqu'un condamna le puisard", "a condamné"),
        ("elle eut le rapport en main", "a eu"),
        ("ils firent poser une membrane", "ont fait poser"),
        ("la résidence fut vendue en 2022", "a été vendue"),
    ], corrige=True,
       notes="La cinquième contient un faire causatif au passé simple : deux points du "
             "module dans la même ligne, et le groupe le remarque tout seul.")

    d.billet(
        "Écris la phrase du rapport qui t'a le plus surpris, et pourquoi.",
        exemples=[
            "Une phrase, une raison.",
            "Ça peut être une phrase que tu as trouvée belle, ou inquiétante.",
        ],
        notes="Trois minutes. Fin de la séance de lecture du rapport. Annoncer C3 : "
              "l'autre papier, celui qui a un prix au bout.")

    return d.save(dossier)
