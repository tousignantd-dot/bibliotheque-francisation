# -*- coding: utf-8 -*-
"""A4 · Chaque nouvelle demande une réponse différente
Bloc A « Je découvre » · couleur teal · écoute et réponds · 75 min.
Source : exercice `prEvts` et sa mini-leçon, exercice `prImg` — les lieux de
l'histoire —, fin du banc de vocabulaire de « Je découvre ».
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A4', section='teal',
        titre="Chaque nouvelle demande une réponse différente",
        chapeau="On ne répond pas à une naissance comme à un décès. Le mot "
                "juste existe pour chaque nouvelle, et il est court.",
        duree='75 minutes')

    d.titre(notes="Dernière séance du bloc A. Elle est sociale plutôt que "
                  "grammaticale : c'est ici que se joue le rapport aux gens, et les "
                  "élèves y ont beaucoup à dire. Prévoir du temps de parole.")

    d.objectifs([
        "féliciter, offrir ses condoléances, souhaiter un rétablissement ;",
        "poser une question qui ouvre la conversation au lieu de la fermer ;",
        "reconnaître les lieux et les objets de l'histoire ;",
        "employer les quatre mots de « Je découvre » sans hésiter.",
    ], notes="Le deuxième objectif est le plus difficile et le plus utile : il ne "
             "s'agit pas de politesse, mais de laisser l'autre continuer à parler.")

    d.declencheur(
        'Observation', "Que dis-tu à quelqu'un qui vient de perdre un proche ?",
        pistes=[
            "Que dit-on dans ta langue, exactement ?",
            "Est-ce qu'on parle du décès, ou de la personne qui reste ?",
            "Est-ce qu'on offre quelque chose : un plat, du temps, un silence ?",
            "Qu'est-ce qui t'a semblé différent ici ?",
        ],
        notes="Question délicate et très riche. Laisser venir, ne rien hiérarchiser. "
              "Retenir une ou deux formules d'autres langues et les écrire au tableau "
              "à côté de « toutes mes condoléances ».")

    d.tableau('Analyse', "La nouvelle, et le mot juste",
              ['La nouvelle', 'Ce qu\'on répond'],
              [["Une naissance", "Félicitations à vous deux ! Comment va la maman ?"],
               ["Un mariage", "Quelle belle nouvelle ! Vous descendez pour l'occasion ?"],
               ["Un décès", "Toutes mes condoléances. Je pense à toi et à ta famille."],
               ["Un accident", "Bon rétablissement à lui. Est-ce qu'il remarche ?"],
               ["Un déménagement", "Et le nouveau quartier, vous vous y plaisez ?"]],
              cle=0,
              note="Condoléances est toujours au pluriel, et toujours accompagné.",
              notes="Diapositive à photographier. Faire répéter chaque réponse à voix "
                    "haute : ces phrases doivent venir sans réflexion le jour où elles "
                    "serviront.")

    d.regle("Parler de la personne, jamais de l'évènement",
            "La cause d'un décès ne se demande pas. Si la personne veut la dire, elle la dira.",
            precision="Devant un accident, on demande comment va le blessé, pas "
                      "comment c'est arrivé ni qui est responsable. Devant un décès, "
                      "on nomme celui qui reste. C'est la règle la plus sûre dans une "
                      "langue qu'on apprend : elle évite toutes les maladresses d'un "
                      "coup.",
            notes="Diapositive à photographier. Rassurer : une formule courte et juste "
                  "vaut mieux qu'une longue phrase qu'on ne maîtrise pas.")

    d.cartes('Comparer', "Ce qui ouvre, ce qui referme", [
        ("Nous aussi, on a déménagé l'an passé.",
         "Referme. La conversation revient vers celui qui parle, et l'autre cesse de raconter."),
        ("Et le nouveau quartier, vous vous y plaisez ?",
         "Ouvre. Une question sur le présent, à laquelle il y a beaucoup à répondre."),
        ("Ça va aller, ce n'est pas grave.",
         "Referme. Décider à la place de l'autre que ce n'est pas grave lui enlève le droit de trouver ça grave."),
        ("J'espère que ça va aller. Dis-moi si je peux aider.",
         "Ouvre. On reconnaît la difficulté, et on laisse à l'autre le choix de la suite."),
    ], notes="Faire jouer les quatre répliques à deux. La différence s'entend "
             "immédiatement, bien mieux qu'elle ne s'explique.")

    d.pratique('Association', "Qu'est-ce que tu réponds ?",
               "Lisez la nouvelle, puis choisissez la réponse qui convient.", [
        ("Notre fille Assia est née le 14 mars.", "Félicitations à vous deux ! Comment va la maman ?"),
        ("Mon oncle Mamadou est décédé en février.", "Toutes mes condoléances. Je pense à toi."),
        ("Mon beau-frère s'est cassé la cheville au travail.", "Bon rétablissement à lui. Est-ce qu'il remarche ?"),
        ("Nous avons déménagé en juin.", "Et le nouveau quartier, vous vous y plaisez ?"),
        ("Ma cousine se marie le 12 septembre.", "Quelle belle nouvelle ! Vous descendez pour l'occasion ?"),
        ("Ma sœur est arrivée de Conakry en octobre.", "Ça doit vous faire du bien de l'avoir avec vous."),
    ], corrige=True,
       notes="Les élèves referont l'exercice à l'écran ensuite. Ici, l'important est "
             "de le dire à voix haute : ces phrases se disent plus qu'elles ne "
             "s'écrivent.")

    d.pratique('Vocabulaire', "Les lieux de cette histoire",
               "Décrivez chaque lieu en une phrase, puis dites ce qui s'y passe.", [
        ("le comptoir de la boulangerie", "Marisol y travaille tôt le matin"),
        ("l'écran du courriel", "les quatre paragraphes d'Ousmane"),
        ("la table de cuisine", "Marisol relit la feuille imprimée"),
        ("le terminus d'autobus", "Kadiatou et Ousmane arrivent vendredi"),
        ("la salle communautaire", "l'organisme du quartier s'y réunit"),
        ("le journal de quartier", "l'article du Défi 3"),
    ], corrige=True, cols=2,
       notes="Cet exercice existe à l'écran avec les photos ; ici il se fait de "
             "mémoire, ce qui oblige à formuler. Demander une phrase complète.")

    d.billet(
        "Écris la phrase que tu dirais à Ousmane pour son oncle.",
        exemples=[
            "Une ou deux phrases.",
            "Souviens-toi : on parle de la personne qui reste.",
        ],
        notes="Deux minutes. Relire les billets avant B1 : ils montrent qui a compris "
              "la règle du bloc, et qui pose encore des questions sur l'évènement.")

    return d.save(dossier)
