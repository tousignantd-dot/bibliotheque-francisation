# -*- coding: utf-8 -*-
"""E2 · La lettre au courrier des lecteurs, et le bilan
Bloc E « Je me lance » · couleur framboise · production écrite · 75 min.
Source : section `appli` (production écrite) et « Je retiens des mots ».
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='E2', section='framboise',
        titre="La lettre au courrier des lecteurs, et le bilan",
        chapeau="Deux cents mots à quelqu'un qui écrit pour vivre, sur une "
                "pièce que vous n'avez pas vue. Le seul terrain où vous êtes "
                "son égal est le texte qu'il a publié.",
        duree='75 minutes')

    d.titre(notes="Dernière séance du module — et du programme, pour un groupe qui "
                  "aurait suivi les huit niveaux. Redistribuer les billets de D2 : la "
                  "question au critique y est déjà écrite.")

    d.objectifs([
        "résumer fidèlement un texte d'opinion, en deux phrases ;",
        "concéder ce qui tient, puis nommer un jugement sans appui ;",
        "citer exactement, avec deux-points et guillemets ;",
        "faire le bilan de ce qu'on sait maintenant faire.",
    ], notes="Le premier objectif est une attente de fin de cours du niveau 8 : "
             "« il résume un texte d'opinion ». La lettre au courrier des lecteurs en "
             "est une autre, nommée mot pour mot par le programme.")

    d.declencheur(
        'Préparation', "À qui écrit-on au courrier des lecteurs ?",
        pistes=[
            "Au critique, ou aux gens qui liront le journal ?",
            "Qu'est-ce qu'un journal publie, et qu'est-ce qu'il ne publie pas ?",
            "Que se passe-t-il si votre lettre attaque la personne ?",
            "Combien de vos lecteurs auront vu la pièce ?",
        ],
        notes="La deuxième piste est la règle du genre : on publie ce qui est signé et "
              "argumenté. La troisième donne la réponse pratique — une attaque ne se "
              "publie pas, et ce n'est pas une question de politesse.")

    d.tableau('Analyse', "Trois paragraphes, trois travaux",
              ['Le paragraphe', 'Ce qu\'il contient'],
              [["Le résumé", "ce que le critique soutient, en deux phrases"],
               ["La réserve", "ce qui tient, puis un jugement sans appui"],
               ["La demande", "ce que vous auriez voulu lire, et la signature"]],
              cle=0,
              note="De douze à seize phrases en tout. Une lettre longue ne se publie pas.",
              notes="Diapositive à photographier. La structure vaut pour toute réponse "
                    "publique à un texte d'opinion, quel qu'en soit le sujet.")

    d.cartes('Analyse', "Huit exigences, tirées du module", [
        ("Un résumé fidèle", "deux phrases, qu'il pourrait approuver"),
        ("Un verbe neutre", "il écrit, il soutient, il explique"),
        ("Une concession", "certes..., mais... · bien que... soit..."),
        ("Une citation exacte", "deux-points, guillemets, mots exacts"),
        ("Un relatif à préposition", "dont, sur lequel, à laquelle"),
        ("Une mise en relief", "ce que je lui reproche, c'est..."),
        ("Un conditionnel passé", "on aurait aimé lire..."),
        ("L'aveu", "je n'ai pas assisté à la représentation"),
    ], notes="La huitième est celle qu'on oublie, et c'est la plus importante : une "
             "lettre qui laisse croire que vous y étiez perd toute sa force le jour "
             "où quelqu'un le remarque.")

    d.regle("On discute le texte, jamais la personne",
            "« Vous n'y connaissez rien » ne se publie pas. « Ce jugement-là "
            "repose sur quel moment ? » se publie.",
            precision="La première phrase ferme la discussion et donne raison au "
                      "critique sans qu'il ait à répondre. La seconde l'oblige à "
                      "répondre, et c'est exactement ce que vous voulez. La "
                      "différence n'est pas morale : elle est efficace.",
            notes="Diapositive à photographier. Le redire au moment de la relecture "
                  "croisée : une lettre sur trois contient une pique, et son auteur "
                  "ne la voit pas.")

    d.piege('Piège', "généraliser un reproche précis",
            "le laisser précis",
            "« Il n'aime pas la pièce » alors qu'il reproche aux deux cadets de "
            "jouer trop fort : c'est la déformation la plus fréquente, et la "
            "plus difficile à voir en se relisant. Elle suffit à faire écarter "
            "une lettre, parce que le critique n'a qu'à citer son propre texte "
            "pour vous contredire. Restez sur la phrase exacte.",
            notes="Faire l'exercice à voix haute sur trois lettres du groupe, avant la "
                  "mise au propre : le groupe repère la généralisation chez les "
                  "autres bien avant chez lui.")

    d.pratique('Rédaction', "Écrivez la lettre",
               "De 12 à 16 phrases, trois paragraphes.", [
        ("Paragraphe 1", "ce qu'il soutient, en deux phrases fidèles"),
        ("Paragraphe 2", "ce qui tient, puis un jugement sans appui"),
        ("Paragraphe 3", "ce que vous auriez voulu lire, et vous signez"),
        ("Registre", "vouvoiement et registre soutenu du début à la fin"),
        ("Interdit", "toute phrase sur la personne du critique"),
        ("Obligatoire", "dire que vous n'avez pas vu la pièce"),
    ], corrige=False,
       notes="Trente minutes de rédaction au propre, dans la section « Je me lance » "
             "du module. L'assistant vérifie le texte avant l'envoi ; la correction "
             "reste privée.")

    d.tableau('Bilan', "Ce que le module a demandé",
              ['La compétence', 'Ce qu\'on sait faire'],
              [["Écouter", "suivre un exposé long, avec une consigne par écoute"],
               ["Lire", "une nouvelle, un poème, une critique"],
               ["Parler", "proposer une lecture et la défendre sans nier l'autre"],
               ["Écrire", "répondre à un texte d'opinion, par ses appuis"]],
              cle=0,
              note="Et une seule règle, depuis la première séance : une lecture se juge à ce qu'elle explique.",
              notes="Diapositive à photographier. Terminer là-dessus, et laisser le "
                    "groupe reprendre la règle à voix haute : c'est la dernière "
                    "séance du dernier module du programme.")

    d.billet(
        "Envoyez votre lettre, puis remplissez l'autoévaluation de « Je retiens "
        "des mots ».",
        exemples=[
            "Vingt énoncés, trois réponses possibles : pas encore, un peu, oui.",
            "Répondez honnêtement : personne ne note cette page-là.",
        ],
        notes="Fin du module. Les autoévaluations remontent dans le portail et "
              "servent à préparer la rencontre de bilan.")

    return d.save(dossier)
