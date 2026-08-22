# -*- coding: utf-8 -*-
"""C3 · De, à, rien du tout — et le mot « où »
Bloc C « Défi 2 » · couleur ambre · 75 min. Grammaire de la phrase.
Source : exercices `t2inf` et `t2ou`, leurs mini-leçons.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C3', section='ambre',
        titre="De, à, rien du tout — et le mot « où »",
        chapeau="Deux hésitations qui reviennent dix fois par jour : quel "
                "petit mot avant un infinitif, et comment coller une phrase "
                "à un nom sans le répéter.",
        duree='75 minutes')

    d.titre(notes="Séance de grammaire double. Prévoir la bascule à mi-parcours et "
                  "annoncer les deux parties dès le début : les élèves supportent "
                  "mal de croire qu'un seul point durera soixante-quinze minutes.")

    d.objectifs([
        "employer « de » ou « à » selon le verbe qui précède l'infinitif ;",
        "ne rien mettre après vouloir, pouvoir, devoir, savoir ;",
        "poser une question avec « quoi » devant un infinitif ;",
        "relier une phrase à un nom de lieu ou de temps avec « où ».",
    ], notes="Le deuxième objectif corrige la faute la plus fréquente à ce niveau, et "
             "elle porte sur les verbes les plus employés de la langue.")

    d.declencheur(
        'Observation', "Trois phrases : qu'est-ce qui change ?",
        pistes=[
            "« Elle m'a demandé de noter. »",
            "« J'ai commencé à comprendre. »",
            "« Je dois passer des examens. »",
        ],
        notes="Trois minutes. Le groupe voit la différence sans pouvoir l'expliquer. "
              "Annoncer tout de suite qu'il n'y a pas de règle : c'est une habitude "
              "par verbe, comme le genre des noms. Ça soulage.")

    d.tableau('Analyse', "Trois familles de verbes",
              ['La famille', 'Les verbes'],
              [["Avec de", "demander, arrêter, éviter, essayer, oublier, accepter"],
               ["Avec à", "commencer, continuer, apprendre, aider, réussir, hésiter"],
               ["Avec rien", "vouloir, pouvoir, devoir, falloir, savoir, aller"]],
              cle=0,
              note="Retenez le verbe avec son petit mot : « demander de » est un seul bloc à mémoriser.",
              notes="Diapositive à photographier. Le repère approximatif qui aide : "
                    "faire faire à quelqu'un appelle souvent « de » ; un mouvement "
                    "vers quelque chose appelle souvent « à ».")

    d.piege('Grammaire',
            "je dois de passer d'autres examens",
            "je dois passer d'autres examens",
            "Vouloir, pouvoir, devoir, falloir, savoir et aller collent "
            "directement à l'infinitif. Ce sont justement les verbes qu'on "
            "emploie le plus souvent, et un « de » de trop après eux s'entend "
            "tout de suite.",
            notes="Faire produire cinq phrases avec « je dois » à voix haute, en "
                  "chaîne autour de la classe. La correction se fait par la "
                  "répétition, pas par l'explication.")

    d.regle("Devant un infinitif, la question se pose avec « quoi »",
            "« Je ne sais pas quoi répondre », jamais « je ne sais pas que répondre ».",
            precision="Après savoir, demander et se demander, on peut poser une "
                      "question sans point d'interrogation : « je ne sais pas comment "
                      "le dire », « je me demande où aller ». C'est une phrase "
                      "d'adulte, et elle est parfaitement polie.",
            notes="Diapositive à photographier. Leyla emploie cette forme dans "
                  "l'entretien : « je ne sais pas quoi vous répondre pour la "
                  "moyenne ». La relire dans le dialogue de C1.")

    d.pratique('Grammaire', "De, à, quoi, ou rien ?",
               "Complétez avec un seul mot.", [
        ("La docteure m'a demandé ___ noter mes journées.", "de"),
        ("Je commence ___ monter les escaliers plus lentement.", "à"),
        ("J'ai arrêté ___ parler en montant.", "de"),
        ("Je ne savais pas ___ répondre.", "quoi"),
        ("Je dois ___ passer d'autres prélèvements.", "rien du tout"),
        ("Elle a réussi ___ dire ce qui avait changé.", "à"),
    ], corrige=True,
       notes="Faire relire chaque phrase entière une fois corrigée. C'est la lecture "
             "à voix haute qui installe l'habitude, pas la liste.")

    d.tableau('Analyse', "Le mot « où » ne parle pas que des endroits",
              ['Il relie', 'Un exemple'],
              [["Un lieu", "le laboratoire où vous êtes entrée ce matin"],
               ["Un moment", "le mois où mon fils a déménagé"],
               ["Un moment à venir", "le jour où j'aurai les résultats"],
               ["Un instant précis", "au moment où on l'a appelée"]],
              cle=0,
              note="C'est l'emploi de temps que le français parlé oublie, et c'est celui qui manque au niveau 6.",
              notes="Diapositive à photographier. Faire nommer l'antécédent de chaque "
                    "exemple : c'est le mot juste avant « où », et le repérer suffit "
                    "à comprendre la phrase.")

    d.piege('Grammaire',
            "le jour quand j'aurai les résultats",
            "le jour où j'aurai les résultats",
            "« Quand » ouvre une phrase entière et ne s'accroche jamais à un "
            "nom. « Quand j'aurai les résultats, je vous appellerai » est "
            "juste ; « le jour quand j'aurai » ne l'est pas. Même chose pour "
            "« le jour que », qui se dit beaucoup et ne s'écrit pas.",
            notes="C'est la faute la plus fréquente de tout le point. La corriger "
                  "sans dévaloriser « le jour que », qui est du français parlé "
                  "courant et non une erreur d'apprenant.")

    d.pratique('Grammaire', "Où, ou bien ou ?",
               "Complétez, avec ou sans accent.", [
        ("Février est le mois ___ ma fatigue a commencé.", "où"),
        ("Elle vient le lundi ___ le jeudi.", "ou"),
        ("Le jour ___ j'aurai les résultats, je vous appelle.", "où"),
        ("C'est la seule salle ___ on peut parler à quelqu'un.", "où"),
        ("Apportez la feuille ___ envoyez-la par la poste.", "ou"),
        ("L'année ___ elle est arrivée, il neigeait en mai.", "où"),
    ], corrige=True,
       notes="Rappeler le test avant de corriger : si l'on peut dire « ou bien », "
             "c'est celui sans accent. Le test ne se trompe jamais, et il tient dans "
             "une seule ligne de cahier.")

    d.billet(
        "Écrivez une phrase avec « le jour où » ou « le mois où ».",
        exemples=[
            "Un souvenir personnel fait très bien l'affaire.",
            "Le nom de temps vient avant, la phrase entière après.",
        ],
        notes="Deux minutes. Ramasser et relire trois billets à la séance suivante : "
              "cette structure sera exigée dans la production écrite de E2.")

    return d.save(dossier)
