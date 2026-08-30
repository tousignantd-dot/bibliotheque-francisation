# -*- coding: utf-8 -*-
"""F1 · La logique pédagogique — ce qui fonde le cours, et pourquoi.

Section framboise · le seul diaporama de la trousse qui ne vend rien. Il
répond à la question que posent les conseillers pédagogiques et les
enseignants d'expérience, jamais les directions : **sur quoi cette chose-là
est-elle bâtie ?**

Il se projette devant un public qui connaît le métier. D'où trois partis pris
d'écriture : on montre du matériel réel plutôt que des principes (le dialogue
d'Oksana est celui du module 9, mot pour mot), on nomme ce qu'on a refusé de
faire autant que ce qu'on a fait, et on ne dit jamais « innovant ».

Les quinze décisions qu'il expose sont documentées dans `CLAUDE.md` ; celle-ci
en est la synthèse projetable, pas une source de plus.
"""
from theme import Deck
from chiffres import CH, n


def build(dossier):
    d = Deck(
        code='F1', section='framboise',
        titre="La logique pédagogique",
        chapeau="Ce qui décide du contenu, de l'ordre des choses, du moment où la règle "
                "arrive et de ce que la machine n'a pas le droit de faire. Rien ici "
                "n'est une intention : tout est déjà dans les %s modules."
                % n(CH['cours']),
        duree='20 minutes')

    d.titre(surtitre="LES FONDEMENTS",
            notes="Devant des conseillers pédagogiques ou des enseignants "
                  "d'expérience, commencer par leur demander ce qu'ils reprochent "
                  "d'habitude au matériel tout fait. Les réponses tombent presque "
                  "toujours dans les quatre premières diapositives.")

    d.objectifs([
        "d'où vient le contenu, et ce qu'il ne copie jamais ;",
        "pourquoi on part d'une situation et non d'un point de grammaire ;",
        "quand la règle arrive, et pourquoi jamais avant ;",
        "ce que l'assistant refuse de faire, et qui l'a décidé.",
    ], notes="Quatre questions. Si la salle n'en a qu'une, c'est presque toujours "
             "la quatrième — garder du temps pour elle.")

    # ── 1. D'où vient le contenu ──────────────────────────────────────
    d.regle("La source",
            "Le programme dit ce qu'il faut savoir faire. Il ne dit jamais avec "
            "quels mots.",
            precision="Le Programme d'études Francisation du ministère donne, pour "
                      "chaque niveau, des situations de communication, des intentions, "
                      "des savoirs et des critères. C'est une spécification. Le "
                      "scénario, les personnages et les dialogues s'inventent.",
            notes="Point à ne pas survoler devant des enseignants : ils ont tous vu du "
                  "matériel qui recopie un manuel existant en changeant les prénoms. "
                  "Ici, rien n'est repris d'un manuel — la contrainte est écrite dans "
                  "les règles du projet.")

    d.dialogue("Ce que ça donne", "Le module 9 s'ouvre là-dessus",
               [("OKSANA", "Bertrand, il fait quatorze degrés chez moi. Le calorifère "
                           "du salon est resté froid toute la nuit.", False),
                ("BERTRAND", "Quatorze ? En novembre, c'est beaucoup trop bas. Est-ce "
                             "que les autres pièces chauffent ?", False),
                ("OKSANA", "C'est seulement celui du salon qui ne réagit plus, même "
                           "quand je monte le thermostat à vingt-deux.", True),
                ("BERTRAND", "Avant d'appeler ta propriétaire, descends au panneau "
                             "électrique.", False)],
               # 88 caractères : `dialogue()` n'accorde qu'une ligne (0,36 po), et
               # la seconde passait sur la première réplique. Mesuré, pas deviné.
               consigne="Situation « Problème dans le logement ». Aucune phrase n'y "
                        "place une règle de grammaire.",
               notes="Lire les quatre répliques à voix haute. Faire remarquer ce qui "
                     "s'y trouve sans avoir été planté : un imparfait, un présent, une "
                     "négation, une subordonnée — et surtout du vocabulaire qu'on "
                     "n'apprend nulle part ailleurs (calorifère, disjoncteur).")

    d.cartes("Comment un module s'écrit", "Quatre décisions, toujours dans cet ordre",
             [("La situation d'abord", "On prend une situation du programme — appeler "
               "un propriétaire, consulter un médecin, répondre à une offre d'emploi. "
               "Elle est déjà écrite, on ne la choisit pas."),
              ("Une personne, pas un exemple", "Oksana loue le 4B. Elle a un nom, un "
               "logement, un problème qui dure depuis trois jours. Un dialogue entre "
               "« A » et « B » ne s'écoute pas deux fois."),
              ("Les savoirs viennent après", "On regarde ce que le dialogue a "
               "naturellement produit, et on va y chercher ce que le programme demande "
               "à ce niveau. L'inverse fabrique des phrases que personne ne dit."),
              ("Ce qui manque se rajoute", "S'il manque un savoir obligatoire, on "
               "retouche la situation pour qu'il y tombe — jamais on ne colle un "
               "exercice hors sol à la fin.")],
             notes="C'est l'ordre qui compte, pas la liste. Beaucoup de matériel part "
                   "du savoir et fabrique une situation autour : ça se voit tout de "
                   "suite, et les élèves ne s'en servent jamais dehors.")

    # ── 2. L'ordre des choses ─────────────────────────────────────────
    d.tableau("Le chemin", "Ce que l'élève traverse, dans l'ordre",
              ['Étape', 'Ce qu\'il y fait', 'Ce qu\'on observe'],
              [["Je découvre", "Il écoute le dialogue, autant de fois qu'il veut",
                "s'il comprend la situation"],
               ["Défi 1 à 3", "Il travaille un savoir à la fois, en exercices",
                "où il se trompe"],
               ["Je me lance", "Il produit — sa voix, puis un texte",
                "ce qu'il sait faire seul"],
               ["Je retiens des mots", "Il reprend le vocabulaire de la situation",
                "ce qui reste une semaine après"]],
              cle=0,
              # Le thème refuse quatre rangées **plus** une note : elle descend donc
              # chez le présentateur, où elle se lit de près — sous un tableau
              # projeté, en petits caractères, personne ne l'aurait lue.
              notes="Les mêmes quatre étapes dans les %s modules, du niveau 1 au "
                    "niveau 8 : l'élève n'apprend qu'une fois comment un cours "
                    "fonctionne. La constance est un choix pédagogique, pas une "
                    "facilité de production — un élève de francisation dépense "
                    "beaucoup d'énergie à comprendre une interface, et celle-là il "
                    "la comprend une seule fois." % n(CH['cours']))

    d.regle("La forme des exercices",
            "Sept familles, pas une de plus.",
            precision="Vrai ou faux, associer, des cases à écrire, un texte à trous, "
                      "des images, une question ouverte, un tableau. Un élève de "
                      "francisation dépense beaucoup d'énergie à comprendre ce qu'on "
                      "lui demande : il l'apprend une fois, puis il ne pense plus "
                      "qu'au français.",
            notes="La contrainte a été tenue sur les 87 modules et les huit niveaux. "
                  "Elle coûte cher à l'écriture — il faut faire entrer une intention "
                  "dans une forme existante — et c'est l'élève qui encaisse la "
                  "différence quand on ne la tient pas. Les sept sont montrées en "
                  "images dans l'annexe A2.")

    d.regle("Le moment de la règle",
            "La règle arrive quand l'élève s'est trompé, jamais avant.",
            precision="Les mini-leçons ne sont pas en tête de module : elles s'ouvrent "
                      "depuis l'exercice, au moment de l'erreur. Une règle lue avant "
                      "d'en avoir eu besoin ne se retient pas — elle se recopie.",
            notes="C'est la décision la plus discutée du projet, et la plus facile à "
                  "défendre en salle : demander qui, dans la salle, se souvient d'une "
                  "règle apprise avant d'en avoir eu besoin.")

    d.piege("Ce qu'on nous dit",
            "« Si la machine corrige tout de suite, l'élève ne cherche plus. »",
            "« Elle ne donne pas la réponse au premier essai. »",
            "Une réponse ouverte demande deux tentatives avant que la réponse attendue "
            "s'affiche. C'était une correction, pas un réglage d'origine : la première "
            "version donnait tout du premier coup, et on voyait des élèves valider "
            "n'importe quoi pour lire la solution.",
            notes="Dire que c'est une correction, pas une intention initiale. Un projet "
                  "qui raconte n'avoir jamais eu tort n'est pas crédible devant des "
                  "praticiens.")

    # ── 3. Ce que l'élève ose ─────────────────────────────────────────
    d.regle("La correction et l'envoi",
            "La correction est privée. L'envoi est un geste.",
            precision="Quand un élève fait relire son texte ou son enregistrement, "
                      "rien n'est gardé et rien ne part. L'enseignant reçoit ce que "
                      "l'élève décide de lui envoyer, quand il le décide. C'est ce qui "
                      "permet de recommencer douze fois.",
            notes="Le point que les enseignants comprennent le plus vite : un élève "
                  "adulte qui sait qu'on l'observe ne s'enregistre pas. Celui qui sait "
                  "que personne n'écoute recommence jusqu'à être content.")

    d.cartes("Écouter", "Ce qu'il a fallu pour que l'oral serve à quelque chose",
             [("Une voix par personnage", "Oksana et Bertrand ne sonnent pas pareil. "
               "Sans ça, l'élève ne sait pas qui parle et n'entend qu'un texte lu."),
              ("Un débit ralenti à la source", "La voix enseignante est synthétisée "
               "plus lentement, pas étirée après coup — l'étirement dégrade le son et "
               "s'entend."),
              ("Réécouter ne coûte rien", "%s pistes audio, dans le module. L'élève "
               "réécoute une réplique quinze fois sans user la patience de personne."
               % n(CH['mp3'])),
              ("Le mot dans une phrase", "Un mot isolé se prononce mal et s'oublie. "
               "Chaque mot du vocabulaire est enregistré dans une phrase porteuse.")],
             notes="La phrase porteuse est le détail que les enseignants relèvent : "
                   "c'est exactement ce qu'ils font en classe quand ils refusent de "
                   "faire répéter un mot seul.")

    d.regle("Le vocabulaire",
            "Une seule porte d'entrée dans la progression.",
            precision="La section « Je retiens des mots » d'un module n'enregistre "
                      "rien : elle fait travailler. C'est l'atelier de cartes mémoire, "
                      "en répétition espacée, qui fait monter un mot d'une boîte à "
                      "l'autre — et l'élève y **écrit** le mot, il ne le reconnaît pas "
                      "dans une liste.",
            notes="Deux moteurs de mémorisation feraient deux progressions qui "
                  "divergent. Et reconnaître n'est pas savoir : on écrit.")

    # ── 4. Ce que la machine n'a pas le droit de faire ────────────────
    d.piege("La question qui vient toujours",
            "« Votre assistant va faire les exercices à leur place. »",
            "« Il a interdiction de donner une réponse. »",
            "Il cite la phrase du dialogue où se trouve l'information, puis repose une "
            "question plus facile. La traduction s'ajoute sous le français et ne le "
            "remplace jamais ; « simplifier » reformule en français, il ne traduit pas.",
            notes="Ces trois refus sont écrits dans les consignes envoyées au modèle, "
                  "pas dans une politique d'usage. Si on demande à voir, on peut "
                  "montrer le fichier.")

    d.regle("Qui décide",
            "Aucun parcours n'est suggéré automatiquement à un élève.",
            precision="Le portail dit ce qu'un élève a fait et où il s'est trompé. Il "
                      "ne conclut rien et ne propose rien. C'est l'enseignant qui "
                      "envoie une mini-leçon de dix minutes à qui en a besoin — un "
                      "choix, pas une étape transitoire vers l'automatisation.",
            notes="À dire fermement : ce n'est pas une fonctionnalité manquante. "
                  "Diagnostiquer est le métier, et une machine qui range des élèves "
                  "dans des cases se trompe sur ceux qui en ont le plus besoin.")

    d.cartes("Ce qu'on n'a pas retiré", "Quatre choses qui restent, et c'est délibéré",
             [("L'enseignant", "Rien ne s'ouvre tout seul à un élève. C'est "
               "l'enseignant qui date un module, choisit la séance, lit les "
               "productions."),
              ("Le papier", "%s fiches imprimables, noir et blanc. Un élève sans "
               "appareil fait la séance quand même." % n(CH['fiches'])),
              ("La classe", "Le jeu de rôle a une moitié qui se joue à deux, en salle. "
               "Elle ne disparaît pas quand l'assistant est fermé."),
              ("Le droit de refuser", "Un centre peut fermer l'assistant. Les %s "
               "modules se replient : ce qui reste est un cours, pas une démo cassée."
               % n(CH['cours']))],
             notes="Cette diapositive répond d'avance à « vous remplacez le "
                   "professeur ». Ne pas la sauter même si personne n'a posé la "
                   "question — surtout si personne ne l'a posée.")

    d.billet("La question à laquelle tout ceci essaie de répondre : qu'est-ce qu'un "
             "adulte fait, seul, un mardi soir, quand il veut apprendre le français ?",
             exemples=["Il écoute. Il se trompe. Il recommence sans témoin.",
                       "Le lendemain, quelqu'un regarde ce qu'il a fait."],
             notes="Terminer là-dessus et se taire. C'est la seule diapositive du "
                   "diaporama qui ne contient aucun chiffre, et c'est voulu.")

    return d.save(dossier)
