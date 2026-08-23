# -*- coding: utf-8 -*-
"""B2 · Demander au conditionnel
Bloc B « Défi 1 · Frapper à la porte d'en haut » · couleur ambre · grammaire ·
75 min.
Source : exercice `t1cond` et sa mini-leçon.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B2', section='ambre',
        titre="Demander au conditionnel",
        chapeau="« Mettez du caoutchouc » et « accepteriez-vous de mettre du "
                "caoutchouc ? » demandent la même chose. La première obtient "
                "un refus une fois sur deux.",
        duree='75 minutes')

    d.titre(notes="Séance de grammaire, mais l'enjeu est pratique : le conditionnel "
                  "laisse à l'autre le droit de refuser, et c'est pour ça qu'il "
                  "accepte plus souvent.")

    d.objectifs([
        "former le conditionnel présent de tous les verbes du dossier ;",
        "demander poliment : accepteriez-vous, pourriez-vous, je voudrais ;",
        "construire une hypothèse : si + imparfait, puis conditionnel ;",
        "reconnaître le conditionnel d'incertitude.",
    ], notes="Le troisième objectif est le seul qui produit une faute visible : jamais "
             "de conditionnel après « si ».")

    d.declencheur(
        'Observation', "À qui obéis-tu plus volontiers : à un ordre ou à une demande ?",
        pistes=[
            "« Ouvre la fenêtre » et « pourrais-tu ouvrir la fenêtre ? »",
            "Qu'est-ce qui change, exactement ?",
            "Dans laquelle des deux peux-tu répondre non ?",
            "Laquelle te donne envie de dire oui ?",
        ],
        notes="Le groupe trouve seul la réponse : on accepte plus facilement ce qu'on "
              "pourrait refuser. C'est tout le mécanisme.")

    d.regle("Le conditionnel présent",
            "Le radical du futur, plus les terminaisons de l'imparfait.",
            precision="-ais, -ais, -ait, -ions, -iez, -aient. « J'accepterais, tu "
                      "accepterais, il accepterait, nous accepterions, vous "
                      "accepteriez, ils accepteraient. » Si vous savez le futur, vous "
                      "savez le conditionnel : les radicaux irréguliers sont les mêmes.",
            notes="Diapositive à photographier. Faire conjuguer « accepter » à voix "
                  "haute par le groupe entier, puis « pouvoir » et « vouloir ».")

    d.tableau('Analyse', "Les radicaux irréguliers, les mêmes qu'au futur",
              ['Infinitif', 'Radical'],
              [["être", "je serais"],
               ["avoir", "j'aurais"],
               ["aller", "j'irais"],
               ["faire", "je ferais"],
               ["pouvoir", "je pourrais"],
               ["vouloir", "je voudrais"],
               ["devoir", "je devrais"]],
              cle=1,
              notes="Diapositive à photographier. Sept verbes, et ils couvrent presque "
                    "tout ce qu'on dit dans une négociation.")

    d.cartes('Analyse', "Trois emplois, et ce qu'ils font", [
        ("La politesse", "« Accepteriez-vous de mettre du caoutchouc ? » L'autre garde le droit de refuser."),
        ("L'hypothèse", "« Si le tapis était contre l'autre mur, je ne l'entendrais plus. » On montre sans imposer."),
        ("L'incertitude", "« Le bruit viendrait du moteur plutôt que de vos pas. » On avance sans accuser."),
    ], cols=3,
       notes="Le troisième emploi est celui des journalistes : « l'incendie aurait pris "
             "naissance au sous-sol ». Il dit « on me l'a rapporté, je ne l'ai pas "
             "vérifié ».")

    d.piege('Grammaire',
            "Si vous partiriez plus tard",
            "Si vous partiez plus tard, cela changerait tout",
            "Après « si », jamais de conditionnel. La condition est à l'imparfait, la "
            "conséquence au conditionnel — jamais l'inverse, jamais les deux. Un moyen "
            "de ne plus se tromper : après « si », il n'y a jamais de -rais.",
            notes="C'est la faute la plus fréquente du niveau et elle s'entend tout de "
                  "suite. Faire produire trois hypothèses correctes avant de continuer.")

    d.pratique('Pratique', "Mettez le verbe au conditionnel présent",
               "Attention au s de la première personne.", [
        ("Est-ce que vous ___ (accepter) de mettre un tapis de caoutchouc ?", "accepteriez"),
        ("___ (pouvoir)-vous regarder si le tapis rentre dans le couloir ?", "Pourriez"),
        ("Je ___ (vouloir) vous parler cinq minutes, si vous avez le temps.", "voudrais"),
        ("Si le tapis était contre l'autre mur, je ne l'___ (entendre) presque plus.", "entendrais"),
        ("Si vous partiez à sept heures, cela me ___ (donner) une heure de plus.", "donnerait"),
        ("Le bruit ___ (venir) du moteur plutôt que de vos pas.", "viendrait"),
        ("Je ___ (être) prête à ne rien dire pour les fins de semaine.", "serais"),
        ("Nous ___ (faire) le point dans deux semaines, si cela vous va.", "ferions"),
    ], corrige=True,
       notes="Faire relire les huit phrases à la suite : elles forment la conversation "
             "du bloc E presque en entier.")

    d.billet(
        "Écris une demande au conditionnel à quelqu'un qui n'est pas obligé de dire oui.",
        exemples=[
            "Commence par « Accepteriez-vous » ou « Pourriez-vous ».",
            "Demande une seule chose, et une chose précise.",
        ],
        notes="Deux minutes. Ceux qui écrivent « pourriez-vous faire quelque chose » "
              "n'ont pas compris la moitié précise : y revenir en B4.")

    return d.save(dossier)
