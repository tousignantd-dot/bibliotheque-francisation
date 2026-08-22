# -*- coding: utf-8 -*-
"""D1 · Je dois arrêter le cours.
Bloc D « Défi 3 · Quand on doit arrêter » · couleur acier · 75 min.
Source : dialogue `t3`, exercices `t3vf` et `t3mots`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='D1', section='acier',
        titre='Je dois arrêter le cours',
        chapeau="Un emploi commence, et le cours du matin devient "
                "impossible. C'est la démarche la plus difficile du module, "
                "et celle qui laisse une trace le plus longtemps.",
        duree='75 minutes')

    d.titre(notes="Ouverture du défi 3. Séance délicate : plusieurs élèves du groupe "
                  "envisagent peut-être d'arrêter. Le ton est informatif, jamais "
                  "moralisateur — le module apprend à le dire, pas à ne pas le faire.")

    d.objectifs([
        "annoncer qu'on arrête le cours ;",
        "donner son dernier jour de cours ;",
        "distinguer un arrêt temporaire d'un abandon ;",
        "demander une attestation de fréquentation.",
    ])

    d.declencheur(
        'Observation', "Quelqu'un arrête le cours. Qu'est-ce qu'il faut faire ?",
        pistes=[
            "Est-ce qu'il suffit de ne plus venir ?",
            "À qui faut-il le dire ?",
            "Est-ce qu'on peut revenir plus tard ?",
            "Qu'est-ce qui prouve qu'on a suivi le cours ?",
        ],
        notes="La réponse spontanée est souvent « on arrête, c'est tout ». C'est "
              "exactement ce que le module corrige : un départ non déclaré ferme mal "
              "le dossier et complique un retour.")

    d.dialogue('Dialogue · 1 de 3', "Je dois arrêter le cours", [
        ("NAWEL", "Bonjour, monsieur. C'est vous qui remplacez madame Cloutier ?", True),
        ("MARC", "Oui, ce matin. Marc Ferland, à l'accueil. Je vous écoute.", True),
        ("NAWEL", "Nawel Belkacem, groupe 12. Je dois arrêter le cours.", True),
        ("MARC", "Je vous écoute jusqu'au bout. Prenez votre temps.", True),
    ], consigne="Écoutez d'abord, diapo masquée.",
       notes="Nawel dit son affaire en une phrase, comme au défi 1. Faire remarquer que "
             "la personne au comptoir ne discute pas la décision : elle écoute.")

    d.dialogue('Dialogue · 2 de 3', "Quel est votre dernier jour ?", [
        ("NAWEL", "Je commence un travail à temps plein le premier avril.", True),
        ("MARC", "Je comprends. Quel est votre dernier jour de cours ?", True),
        ("NAWEL", "Le vendredi 28 mars.", True),
        ("MARC", "Vendredi 28 mars. Vous arrêtez pour un temps, ou vous abandonnez le cours ?", True),
    ], notes="La date du dernier jour est le renseignement central du défi. Marc la "
             "répète : c'est ce que fait toujours un comptoir, et ce n'est pas de la "
             "méfiance.")

    d.dialogue('Dialogue · 3 de 3', "Un papier qui prouve", [
        ("NAWEL", "Quelle est la différence ?", True),
        ("MARC", "Si vous arrêtez pour un temps, le dossier reste ouvert. Si vous abandonnez, je le ferme.", True),
        ("NAWEL", "Est-ce que je peux avoir un papier qui prouve que j'ai suivi le cours ?", True),
        ("MARC", "Une attestation de fréquentation. Elle se demande avant de partir, jamais après.", True),
    ], notes="Nawel pose la question de la différence : c'est le bon réflexe et il faut "
             "l'enseigner. On ne choisit pas entre deux mots qu'on ne comprend pas.")

    d.tableau('Analyse', "Arrêter pour un temps ou abandonner",
              ["Ce qu'on dit", "Ce qui arrive au dossier"],
              [["j'arrête pour un temps", "la date est notée, le dossier reste ouvert"],
               ["j'abandonne le cours", "le dossier se ferme"],
               ["je ne dis rien", "des absences s'accumulent sans raison"]],
              cle=1,
              note="La troisième ligne n'est pas un choix : c'est ce qui arrive "
                   "quand personne ne vient le dire.",
              notes="Diapo à photographier. Insister sur la troisième ligne sans "
                    "culpabiliser : c'est le cas le plus fréquent, et il est réparable "
                    "tant qu'on vient au comptoir.")

    d.pratique('Vocabulaire', "Les mots de l'arrêt",
               "Associez chaque mot à ce qu'il veut dire.", [
        ("un abandon", "arrêter le cours pour de bon : le dossier se ferme"),
        ("une interruption", "arrêter pour un temps : le dossier reste ouvert"),
        ("une attestation de fréquentation", "le papier qui prouve qu'on a suivi le cours"),
        ("le dernier jour de cours", "la date qu'on inscrit au dossier quand on part"),
        ("signer le formulaire", "écrire son nom pour que la demande soit valide"),
        ("en main propre", "remis à la personne elle-même, pas par la poste"),
    ], corrige=True,
       notes="Reprend l'exercice 4 du module interactif. Ces six mots sont ceux du "
             "défi entier.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après le dialogue.", [
        ("Nawel commence un travail le premier avril.", "vrai"),
        ("Son dernier jour de cours est le vendredi 28 mars.", "vrai"),
        ("Arrêter pour un temps et abandonner, c'est la même chose.", "faux"),
        ("L'attestation est prête tout de suite.", "faux — trois jours"),
        ("L'attestation se demande avant de partir.", "vrai"),
    ], corrige=True,
       notes="Faire justifier par la réplique. La dernière réponse est le sujet entier "
             "de la séance D2.")

    d.billet(
        "Écrivez la phrase que vous diriez si vous deviez arrêter.",
        exemples=[
            "« Mon nom, c'est… , groupe… . Je dois arrêter le cours. »",
            "« Mon dernier jour est le… »",
        ],
        notes="Devoir court. Personne n'est obligé d'arrêter pour écrire la phrase : "
              "c'est un exercice, et le dire clairement évite un malaise.")

    return d.save(dossier)
