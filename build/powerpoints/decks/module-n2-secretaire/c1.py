# -*- coding: utf-8 -*-
"""C1 · Demain, je ne viens pas.
Bloc C « Défi 2 » · couleur acier · 75 min. Première séance du défi.
Source : dialogue `t2`, exercices `t2vf`, `t2neg` et `t2poli`, mini-leçon
« Dire non : ne … pas ».

Prévenir d'une absence est, au niveau 2, une affaire de **deux petits mots**
et de rien d'autre. On ne justifie pas, on ne raconte pas au passé, on ne
rédige pas de billet : on dit « demain, je ne viens pas », on donne son nom
et son groupe, et c'est fini. C'est ce qui sépare ce module de
`module-n3-secretariat`, qui fait exactement l'inverse un niveau plus haut.

La séance ajoute une seconde chose, plus discrète : les six phrases du
comptoir et ce qu'elles veulent dire. Un débutant les entend sans savoir
laquelle ouvre, laquelle vérifie et laquelle termine.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C1', section='acier',
        titre="Demain, je ne viens pas",
        chapeau="Prévenir le secrétariat d'une absence, en deux phrases.",
        duree='75 minutes')

    d.titre(notes="Première séance du Défi 2. Demander qui a déjà manqué un cours sans "
                  "prévenir, et pourquoi. La réponse est presque toujours la même : on "
                  "ne savait pas quoi dire.")

    d.objectifs([
        "dire qu'on ne vient pas, avec « ne … pas » ;",
        "écrire n' devant une voyelle ;",
        "donner son nom et son groupe quand on les demande ;",
        "reconnaître les phrases du comptoir et ce qu'elles font.",
    ])

    d.dialogue('Dialogue · 1 de 2', "Vous êtes malade ?", [
        ("AMEL", "Bonjour, madame. Demain, je ne viens pas au cours.", True),
        ("LINE", "Vous êtes malade ?", True),
        ("AMEL", "Non. J'ai un rendez-vous à la clinique.", True),
        ("LINE", "D'accord. Votre nom et votre groupe ?", True),
    ], consigne="Écoutez deux fois avant de lire.",
       notes="Faire remarquer qu'Amel répond en cinq mots et qu'on ne lui en demande "
             "pas plus. Au niveau 2, on signale une absence, on ne l'explique pas.")

    d.dialogue('Dialogue · 2 de 2', "Ce n'est pas nécessaire", [
        ("AMEL", "Amel Tazi, groupe de madame Dufresne.", True),
        ("LINE", "Merci. J'écris votre absence.", True),
        ("AMEL", "Est-ce que je dois écrire un papier ?", True),
        ("LINE", "Non, ce n'est pas nécessaire. Je préviens l'enseignante.", True),
    ], notes="La question d'Amel est celle que tout le groupe se pose. La réponse "
             "dépend du centre : vérifier avant la séance et corriger si la règle "
             "locale est autre.")

    d.regle("Ne … pas, autour du verbe.",
            "Je ne viens pas. Je ne comprends pas.",
            precision="Deux petits mots, et le verbe au milieu. Devant une voyelle, "
                      "<b>ne</b> devient <b>n'</b> : je <b>n'</b>ai pas, ce <b>n'</b>est "
                      "pas. À l'oral, beaucoup de gens disent « je viens pas » ; à "
                      "l'écrit, on garde le <b>ne</b>.",
            notes="Diapositive à photographier. Écrire une phrase positive au tableau, "
                  "puis venir poser « ne » et « pas » de chaque côté du verbe avec deux "
                  "papiers. Le geste vaut mieux que l'explication.")

    d.tableau('Analyse · 1 de 2', "La négation, trois cas",
              ["Ce qu'on veut dire", "Comment on l'écrit"],
              [["le cas ordinaire", "Je ne viens pas demain."],
               ["devant une voyelle", "Je n'ai pas le papier."],
               ["avec « il y a »", "Il n'y a pas de cours lundi."],
               ["un, du deviennent de", "Je n'ai pas d'attestation."]],
              cle=1,
              note="Le dernier cas est automatique : après la négation, « un » devient « de ».",
              notes="Diapositive à photographier. Le quatrième cas ne se comprend pas, "
                    "il s'imite. Faire produire quatre phrases sur le même modèle.")

    d.tableau('Analyse · 2 de 2', "Six phrases du comptoir",
              ["Ce qu'on dit", "Ce que ça fait"],
              [["Excusez-moi, madame.", "j'ouvre l'échange"],
               ["Je voudrais une attestation.", "je demande, poliment"],
               ["Pouvez-vous répéter ?", "je n'ai pas bien entendu"],
               ["Demain, je ne viens pas.", "je préviens d'une absence"],
               ["Merci beaucoup, bonne journée.", "je termine et je pars"]],
              cle=1,
              note="Cinq phrases, et tout l'échange tient debout.",
              notes="Diapositive à photographier. Faire jouer les cinq à la suite, dans "
                    "l'ordre, comme un seul passage au comptoir. C'est la répétition "
                    "générale du jeu de rôle.")

    d.piege('Écriture', "je viens pas demain", "je ne viens pas demain",
            "Tout le monde dit « je viens pas ». Mais dans un message au secrétariat, "
            "on écrit <b>je ne viens pas</b> : c'est ce qu'on attend d'un papier. "
            "L'oral et l'écrit ne suivent pas la même règle, et les deux sont justes "
            "à leur place.",
            notes="Ne pas corriger l'oral des élèves sur ce point : ils imitent ce "
                  "qu'ils entendent, et ils ont raison. La règle vaut pour l'écrit.")

    d.pratique('Pratique · 1 de 2', "Complétez la négation",
               "Écrivez « ne », « n' » ou « pas ».", [
        ("Demain, je ___ viens pas au cours.", "ne"),
        ("Je ne comprends ___.", "pas"),
        ("Le bureau ___ est pas ouvert le midi.", "n'"),
        ("Il n'y a ___ de cours lundi.", "pas"),
        ("Je ___ ai pas mon attestation.", "n'"),
        ("Ce n'est ___ nécessaire.", "pas"),
    ], corrige=True, cols=2,
       notes="Faire à l'oral d'abord. Les deux « n' » sont le vrai travail : demander à "
             "chaque fois par quelle lettre commence le verbe.")

    d.pratique('Pratique · 2 de 2', "Je préviens de mon absence",
               "Vingt minutes, à deux, debout. On échange les rôles.", [
        ("Étape 1", "A salue : « Bonjour, madame. »"),
        ("Étape 2", "A dit : « Demain, je ne viens pas au cours. »"),
        ("Étape 3", "B demande le nom et le groupe. A répond."),
        ("Étape 4", "A demande s'il doit écrire un papier, puis remercie."),
    ], cols=1,
       notes="Interdire les explications : celui qui dit pourquoi il est absent "
             "recommence. C'est contre-intuitif, et c'est exactement le niveau de "
             "langue attendu ici.")

    d.billet(
        "Écrivez trois phrases négatives sur votre semaine.",
        exemples=[
            "Vendredi, je ne viens pas au cours.",
            "Je n'ai pas mon attestation.",
            "Il n'y a pas de cours lundi.",
        ],
        notes="Devoir court. Exiger le « ne » : c'est tout l'objet de la séance, et "
              "c'est ce qui disparaît en premier.")

    return d.save(dossier)
