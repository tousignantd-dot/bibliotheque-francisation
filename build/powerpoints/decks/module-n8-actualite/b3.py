# -*- coding: utf-8 -*-
"""B3 · La phrase qui efface celui qui a décidé
Bloc B « Défi 1 » · couleur ambre · 75 min.
Source : exercice `t1passif` et sa mini-leçon du même nom. Savoir du
niveau 8 : la voix passive, son accord, et le passif sans agent.
"""
from theme import Deck

import pathlib

IMG = str(pathlib.Path(__file__).resolve().parents[4]
          / 'assets' / 'interactive' / 'module-n8-actualite' / 'images') + '/'


def build(dossier):
    d = Deck(
        code='B3', section='ambre',
        titre="Un passif sans « par » est un endroit où quelqu'un manque",
        chapeau="« Le règlement a été adopté. » La phrase est complète, "
                "correcte, et sans responsable. C'est pour cela qu'on la "
                "trouve dans tous les communiqués.",
        duree='75 minutes')

    d.titre(notes="Séance de grammaire, mais l'enjeu est de lecture. Commencer par "
                  "écrire la phrase du chapeau au tableau et demander qui a adopté le "
                  "règlement : la réponse n'est pas dans la phrase, et c'est le sujet "
                  "de la séance.")

    d.objectifs([
        "fabriquer une phrase passive et la retourner à la voix active ;",
        "accorder le participe passé avec le sujet ;",
        "reconnaître un passif sans agent et poser la question « par qui ? » ;",
        "ne pas confondre le passif avec le passé composé d'un verbe de mouvement.",
    ], notes="Le troisième objectif est le geste du bloc ; les trois autres sont ce "
             "qu'il faut savoir pour l'exécuter. Ne pas passer plus de vingt minutes "
             "sur la forme.")

    d.declencheur(
        'Observation', "Trois phrases sur le même comptage",
        image=IMG + 'erables-lisiere.jpg',
        pistes=[
            "« Le comité a compté trois cent quarante-deux arbres. »",
            "« Trois cent quarante-deux arbres ont été comptés par le comité. »",
            "« Trois cent quarante-deux arbres ont été comptés. »",
            "Laquelle donne le plus l'impression d'un chiffre officiel ? Et pourquoi ?",
        ],
        notes="La troisième est celle que le groupe désigne, et c'est justement celle "
              "où personne n'assume le chiffre. Le faire dire par un élève avant de "
              "l'expliquer.")

    d.regle("Le complément passe devant, l'auteur recule derrière « par »",
            "Le conseil a adopté le règlement. Le règlement a été adopté par "
            "le conseil. Le verbe devient être plus participe passé, au même "
            "temps que le verbe actif.",
            precision="C'est l'auxiliaire être qui porte le temps : passé composé "
                      "actif, passé composé passif. Et l'auteur de l'action peut tout "
                      "simplement ne pas être écrit : « Le règlement a été adopté » "
                      "est une phrase complète.",
            notes="Diapositive à photographier. Faire transformer trois phrases à voix "
                  "haute avant de continuer, avec des verbes du dossier : adopter, "
                  "publier, compter.")

    d.cartes('Analyse', "Trois choses à surveiller", [
        ("L'accord du participe",
         "Il s'accorde toujours avec le sujet. La cession a été autorisée. "
         "Les logements seront livrés. L'évaluation n'a pas été publiée. "
         "C'est la faute la plus visible à l'écrit."),
        ("Le passif honnête",
         "Il met en tête ce dont on parle. Dans un article sur un "
         "règlement, « Le règlement a été adopté par le conseil » est un "
         "ordre normal : le sujet du texte vient d'abord, et l'auteur y est."),
        ("Le passif qui efface",
         "Il a été décidé de ne pas publier l'évaluation. Des erreurs ont "
         "été commises. Le terrain a été évalué. Personne n'a rien fait, "
         "tout est arrivé tout seul."),
    ], notes="Insister sur la deuxième carte : le passif n'est pas une faute et ce "
             "n'est pas un mensonge. Un élève qui en sort en se méfiant de toutes les "
             "phrases passives a mal compris la séance.")

    d.pratique('Pratique 1 de 2', "Retournez la phrase à la voix active",
               "Commencez par le mot donné entre parenthèses.", [
        ("Le règlement a été adopté par le conseil municipal. (Le conseil municipal)",
         "Le conseil municipal a adopté le règlement."),
        ("La cession a été autorisée par le maire et trois conseillers. (Le maire et trois conseillers)",
         "Le maire et trois conseillers ont autorisé la cession."),
        ("L'évaluation n'a pas été rendue publique par la Ville. (La Ville)",
         "La Ville n'a pas rendu l'évaluation publique."),
        ("Trois cent quarante-deux arbres ont été comptés par le comité. (Le comité)",
         "Le comité a compté trois cent quarante-deux arbres."),
        ("Les logements seront livrés par le promoteur avant 2031. (Le promoteur)",
         "Le promoteur livrera les logements avant 2031."),
        ("Le communiqué a été envoyé aux journaux par le service des communications. (Le service des communications)",
         "Le service des communications a envoyé le communiqué aux journaux."),
    ], corrige=True,
       notes="Écrire chaque réponse au tableau : c'est l'orthographe du participe et "
             "le temps du verbe actif qui posent problème, pas l'ordre des mots.")

    d.piege('Piège', "« elle est arrivée » pris pour un passif",
            "le test du « par quelqu'un »",
            "« Elle est attendue par le comité » se dit : c'est un passif. "
            "« Elle est arrivée par le comité » ne veut rien dire : c'est un "
            "passé composé de verbe de mouvement, et son participe s'accorde "
            "pour une autre raison. Le test tient en trois secondes et il ne "
            "se trompe pas.",
            notes="Faire appliquer le test à cinq phrases dictées, en alternant les "
                  "deux cas. C'est une confusion de niveau 8 qui se règle en dix "
                  "minutes et qui traîne autrement pendant des mois.")

    d.tableau('Application', "Six passifs, et la question à poser",
              ['Ce qui est écrit', 'La question à noter'],
              [["Le terrain a été évalué.",
                "par qui, et le document est-il public ?"],
               ["Une consultation a été tenue.",
                "quand, et combien de personnes y étaient ?"],
               ["Les préoccupations ont été entendues.",
                "entendues par qui, et qu'est-ce qui a changé ?"],
               ["Il a été convenu de reporter la décision.",
                "convenu entre qui et qui ?"],
               ["Le dossier a été transmis au service concerné.",
                "à quelle date, et à quel service ?"]],
              cle=0,
              notes="Diapositive à photographier, et à recopier dans le cahier. Ces "
                    "questions se posent telles quelles à une assemblée publique : "
                    "elles sont polies, précises, et personne ne peut y répondre par "
                    "oui ou par non.")

    d.pratique('Pratique 2 de 2', "Qui manque dans la phrase ?",
               "Nommez celui qui a agi, quand la phrase ne le dit pas.", [
        ("Aucune étude n'a été demandée sur le terrain de l'aréna.", "la Ville, ou le conseil municipal"),
        ("Il a été décidé de ne pas publier l'évaluation.", "celui qui a pris la décision n'est pas nommé"),
        ("Le projet a été bonifié.", "bonifié par qui, et sur quel point ?"),
        ("Des erreurs ont été commises.", "personne : c'est tout l'intérêt de la tournure"),
    ], corrige=True,
       notes="Le dernier item est le plus important et il n'a pas de bonne réponse "
             "grammaticale : la phrase est correcte et vide. Laisser le groupe "
             "s'agacer un peu avant de conclure.")

    d.billet(
        "Relevez trois phrases passives dans les deux articles de B2 et écrivez la question que chacune appelle.",
        exemples=[
            "Une seule ligne par phrase : la phrase, puis « par qui ? ».",
            "Ne récrivez pas les phrases : notez les questions.",
        ],
        notes="Devoir. La consigne de ne pas récrire est volontaire : devant un passif "
              "sans agent, la bonne réaction n'est pas de corriger le texte, c'est de "
              "savoir ce qu'on ignore encore.")

    return d.save(dossier)
