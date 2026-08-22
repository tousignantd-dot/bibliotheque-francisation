# -*- coding: utf-8 -*-
"""B3 · Je sais faire, j'ai de l'expérience en...
Bloc B « Défi 1 » · couleur teal · 75 min. Écoute et réponse.
Source du module : exercices `t1sais` et `t1rep`, mini-leçon `t1sais`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B3', section='teal',
        titre="Je sais faire, j'ai de l'expérience en",
        chapeau="Ce qu'on sait faire aujourd'hui, et ce qu'on a déjà fait "
                "avant : deux choses différentes, deux constructions "
                "différentes, et le patron écoute les deux.",
        duree='75 minutes')

    d.titre(notes="Reprendre le devoir de A1 : les trois choses que chacun sait faire. "
                  "Elles vont servir d'exemples pendant toute la séance.")

    d.objectifs([
        "dire ce qu'on sait faire avec « je sais » et un infinitif ;",
        "dire son expérience avec « j'ai de l'expérience en » ;",
        "dire combien de temps avec « pendant » et « depuis » ;",
        "répondre « non » sans fermer la porte.",
    ])

    d.tableau('Analyse', "Deux façons de parler de son travail",
              ['On veut dire', 'On construit', "L'exemple"],
              [["Je peux le faire", "je sais + infinitif", "Je sais faire le ménage."],
               ["Je l'ai déjà fait", "de l'expérience en + domaine", "J'ai de l'expérience en cuisine."],
               ["Ça a duré et c'est fini", "pendant + durée", "J'ai gardé des enfants pendant six ans."],
               ["Ça dure encore", "depuis + durée", "Je fais le ménage depuis longtemps."]],
              cle=1,
              note="Après « en », on nomme le travail, jamais le bâtiment : en cuisine, pas en restaurant.",
              notes="Diapo à photographier. La note du bas règle une erreur très "
                    "fréquente et très visible.")

    d.regle("Après « je sais », le verbe ne change jamais",
            "Je sais faire. Je sais servir. Je sais cuisiner.",
            precision="Le deuxième verbe reste à l'infinitif, la forme du dictionnaire. "
                      "C'est vrai aussi après « je peux » et « je veux ». Trois verbes "
                      "à connaître, et la construction est la même pour les trois.",
            notes="Diapo à photographier. Faire produire dix phrases en chaîne, un "
                  "élève après l'autre, sans reprendre : la vitesse installe le réflexe.")

    d.cartes("Pendant ou depuis", "Deux mots, deux histoires différentes", [
        ("Pendant : c'est terminé",
         "« J'ai gardé des enfants pendant six ans. » Le travail a duré six ans et il "
         "est fini. C'est ce qu'on dit d'un emploi laissé derrière soi, ou d'un pays "
         "quitté."),
        ("Depuis : ça continue",
         "« Je fais le ménage depuis longtemps. » Ça a commencé et ça dure encore "
         "aujourd'hui. Le patron entend que vous êtes en train de le faire."),
        ("La forme courte",
         "« Six ans d'expérience en garde d'enfants. » Sans verbe, sans phrase. C'est "
         "celle qu'on écrit dans une annonce ou sur un formulaire."),
        ("Le nombre d'abord",
         "Devant un patron pressé, commencer par le nombre d'années : c'est le "
         "renseignement qu'il retient, avant même le domaine."),
    ], notes="Faire produire à chacun une phrase avec « pendant » et une avec "
             "« depuis », tirées de sa propre vie, et les faire dire à voix haute.")

    d.piege("S'arrêter à « je ne sais pas »",
            "Vous savez servir au comptoir ? — Non.",
            "Non, mais je peux apprendre vite.",
            "Le « non » tout seul ferme la porte, et c'est vous qui la fermez. Il y a "
            "toujours un « mais » à dire après : ce que vous savez faire d'autre, ou ce "
            "que vous pouvez apprendre. C'est cette moitié de phrase qui décide de la suite.",
            notes="Le point le plus important du défi. Faire répéter la phrase entière "
                  "par tout le groupe, deux fois, avant de passer à l'exercice.")

    d.pratique('Écriture', "Complétez la phrase",
               "Complétez avec : sais, ai, en, pendant, jamais.", [
        ("Je ___ faire le ménage et la vaisselle.", "sais"),
        ("J'___ de l'expérience en garde d'enfants.", "ai"),
        ("J'ai de l'expérience ___ cuisine et ___ entretien.", "en"),
        ("J'ai gardé des enfants ___ six ans, à Conakry.", "pendant"),
        ("Je n'ai ___ travaillé en boulangerie, mais j'apprends vite.", "jamais"),
        ("Je ne ___ pas encore servir, mais je peux apprendre.", "sais"),
    ], corrige=True,
       notes="Même exercice que t1sais dans le module. Faire relire chaque phrase "
             "complète à voix haute.")

    d.pratique('Écoute et réponds', "À chaque question du patron, sa réponse",
               "L'enseignante pose la question ; vous donnez la réponse de Fanta.", [
        ("Vous avez déjà travaillé en boulangerie ?", "Non, jamais. Mais j'ai de l'expérience en ménage."),
        ("Vous êtes disponible quels jours ?", "Du lundi au vendredi, le matin."),
        ("Vous vous appelez comment ?", "Fanta Traoré. T-R-A-O-R-É."),
        ("Et je vous joins où ?", "Au 438 555-0192. Je peux vous l'écrire ?"),
        ("Six heures et demie, c'est trop tôt ?", "Non, ce n'est pas un problème pour moi."),
        ("Temps plein ou temps partiel ?", "Du temps partiel. Je suis à l'école l'après-midi."),
    ], corrige=True,
       notes="Même appariement que t1rep dans le module. Deuxième tour : chacun répond "
             "pour lui-même, avec sa vraie disponibilité et son vrai nom.")

    d.pratique('Oral', "Deux par deux : trois questions, trois réponses",
               "L'un joue le patron et pose les trois questions. On change de rôle.", [
        ("Vous avez déjà fait ce travail ?", "Non, mais… / Oui, pendant… ans."),
        ("Qu'est-ce que vous savez faire ?", "Je sais… J'ai de l'expérience en…"),
        ("Depuis quand ?", "Depuis… / Pendant… ans."),
    ], notes="Quinze minutes. Écouter surtout le « mais » après le « non » : c'est "
             "l'objectif de la séance, pas la grammaire.")

    d.billet(
        "Écrivez deux phrases : ce que vous savez faire, et votre expérience.",
        exemples=[
            "Une avec « je sais » et un infinitif.",
            "Une avec « j'ai de l'expérience en » et un nombre d'années.",
        ],
        notes="Deux minutes. Ces deux phrases entreront telles quelles dans la petite "
              "annonce de E2 : le dire au groupe.")

    return d.save(dossier)
