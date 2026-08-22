# -*- coding: utf-8 -*-
"""B2 · Le courriel d'Ousmane, lu au complet
Bloc B « Défi 1 » · couleur teal · écoute et réponds · 75 min.
Source : exercice `t1texte` — le type `texte` du moteur, un texte suivi dont
les passages se cliquent — et sa mini-leçon « Suivre le fil d'un texte long ».
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B2', section='teal',
        titre="Le courriel d'Ousmane, lu au complet",
        chapeau="Quatre paragraphes, sept questions, et une seule façon de "
                "répondre : retrouver dans le texte le passage exact qui "
                "répond.",
        duree='75 minutes')

    d.titre(notes="Séance centrale du Défi 1. C'est ici que les élèves ouvrent pour "
                  "la première fois un exercice du type « texte » : on choisit une "
                  "question, puis on clique dans le texte le passage qui y répond. "
                  "Montrer le geste une fois au projecteur avant de les laisser "
                  "faire.")

    d.objectifs([
        "trouver dans un texte long le passage qui répond à une question ;",
        "distinguer l'idée principale d'un paragraphe de ses détails ;",
        "justifier une réponse en citant le texte plutôt qu'en résumant ;",
        "repérer ce qui n'est écrit nulle part et qui se déduit.",
    ], notes="Le troisième objectif est le plus exigeant : au niveau 6, une réponse "
             "juste se prouve, elle ne s'affirme pas.")

    d.declencheur(
        'Observation', "Comment fais-tu pour retrouver une information dans un texte ?",
        pistes=[
            "Tu relis tout, ou tu cherches un mot précis ?",
            "Par où commences-tu : le début, la fin, le paragraphe le plus court ?",
            "Qu'est-ce que tu fais quand l'information n'y est pas écrite ?",
            "As-tu déjà répondu de mémoire au lieu de vérifier ?",
        ],
        notes="La dernière question est la vraie. Répondre de mémoire est l'erreur la "
              "plus fréquente, et elle produit des réponses plausibles mais fausses.")

    d.tableau('Analyse', "Quatre paragraphes, quatre idées",
              ['Le paragraphe', 'Ce qu\'il porte'],
              [["Premier", "les excuses du silence, et la naissance d'Assia"],
               ["Deuxième", "la maison vendue et le déménagement de juin"],
               ["Troisième", "l'arrivée de Kadiatou et l'accident du beau-frère"],
               ["Quatrième", "le décès de l'oncle, puis le mariage de septembre"]],
              cle=0,
              note="Un blanc, une idée. Lire les quatre premières phrases donne le plan.",
              notes="Diapositive à photographier. Faire l'expérience en direct : lire "
                    "seulement les premières phrases, puis demander de quoi parle le "
                    "courriel. Le groupe répond juste presque à tous les coups.")

    d.regle("Une réponse se montre dans le texte",
            "Choisis la question, puis clique le passage qui y répond.",
            precision="L'exercice ne demande pas de résumer ni de deviner : il demande "
                      "de désigner. Si aucun passage ne répond, c'est que la question "
                      "porte sur autre chose, ou que la réponse se déduit — et alors "
                      "il faut dire de quoi. Recliquer un passage déjà pris le libère.",
            notes="Diapositive à photographier. Montrer le geste au projecteur, y "
                  "compris l'erreur : cliquer un mauvais passage, puis le libérer.")

    d.pratique('Compréhension', "Sept questions sur le courriel",
               "Pour chaque question, dites à voix haute le passage qui y répond.", [
        ("Quel évènement le premier paragraphe annonce-t-il ?", "notre fille Assia est née le 14 mars"),
        ("Que veut dire on l'avait déjà vendue ?", "la maison de la rue Perreault"),
        ("Quand la famille a-t-elle changé de logement ?", "le déménagement s'est fait en juin"),
        ("Qui est arrivé au Québec en octobre ?", "ma sœur Kadiatou, venue de Conakry"),
        ("Quel accident est raconté ?", "mon beau-frère est tombé d'une plateforme"),
        ("Quelle est la nouvelle triste ?", "mon oncle Mamadou est décédé au pays en février"),
        ("Pourquoi descendent-ils en septembre ?", "ma cousine se marie le samedi 12"),
    ], corrige=True,
       notes="À l'oral d'abord, texte sous les yeux. Exiger le passage exact, pas un "
             "résumé. Les élèves referont ensuite le même exercice à l'écran, en "
             "cliquant dans le texte.")

    d.cartes('Méthode', "Quatre fils tiennent un texte long", [
        ("Les reprises",
         "le, la, en, y, celui-là. Chacun renvoie en arrière. Devant l'un d'eux, recule d'une phrase."),
        ("Les temps",
         "Le plus-que-parfait recule d'un cran ; l'imparfait plante le décor. Ils placent les évènements sans dates."),
        ("Les connecteurs",
         "pourtant, donc, d'ailleurs. Ils annoncent la suite avant qu'elle arrive."),
        ("La mise en page",
         "Un blanc, un paragraphe, un tiret. Ils découpent le texte et comptent les idées."),
    ], notes="Ces quatre fils sont le programme du module entier : les reprises en B3, "
             "les temps en B4, les connecteurs en D2, la mise en page vue en A3.")

    d.piege('Lecture', "Répondre de mémoire, après une seule lecture",
            "Retourner au texte et désigner le passage",
            "Dans un courriel de quatre paragraphes, la mémoire garde les faits mais "
            "perd leur ordre et leurs liens. Une réponse donnée sans retourner au "
            "texte est plausible une fois sur deux, et fausse l'autre fois.",
            notes="Faire l'expérience : poser une question, laisser répondre de "
                  "mémoire, puis vérifier ensemble. L'effet est plus convaincant que "
                  "n'importe quelle consigne.")

    d.billet(
        "Écris une question dont la réponse est dans le troisième paragraphe.",
        exemples=[
            "Une seule question.",
            "Vérifie que la réponse s'y trouve vraiment.",
        ],
        notes="Deux minutes. Les meilleures questions se posent au groupe en B3, en "
              "ouverture.")

    return d.save(dossier)
