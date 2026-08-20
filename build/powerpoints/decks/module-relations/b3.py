# -*- coding: utf-8 -*-
"""B3 · Poser des questions à l'autre.
Bloc B · couleur ambre (écriture) · 75 min.
Source : exercice `t1q`, dialogues `t1` et `appli`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B3', section='ambre',
        titre="Poser des questions à l'autre",
        chapeau="Dans une conversation informelle, celui qui pose les questions "
                "fait avancer l'échange. Cinq mots interrogatifs suffisent — et "
                "trois façons de les employer, de la plus familière à la plus soignée.",
        duree='75 minutes')

    d.titre(notes="Rappeler le constat de B1 : Chantal pose cinq questions en douze "
                  "répliques. C'est ce qu'on outille aujourd'hui.")

    d.objectifs([
        "poser une question avec où, quand, combien de fois, depuis quand et pourquoi ;",
        "choisir entre les trois formes de question selon la situation ;",
        "relancer une conversation qui s'arrête ;",
        "répondre à une question par plus qu'un seul mot.",
    ])

    d.tableau('Analyse', "Trois façons de poser la même question",
              ['Forme', 'Exemple'],
              [["Intonation (familier)", "Tu travailles où ?"],
               ["Est-ce que (courant)", "Où est-ce que tu travailles ?"],
               ["Inversion (soigné)", "Où travailles-tu ?"]],
              cle=1,
              note="Les trois sont correctes. La deuxième passe partout : c'est celle à "
                   "employer si on hésite.",
              notes="Faire dire les trois à voix haute. La première est celle qu'ils "
                    "entendront le plus au Québec ; la troisième, celle qu'on leur "
                    "demandera à l'écrit.")

    d.cartes('Les cinq mots utiles', "Ce que chacun demande", [
        ("où",
         "Le lieu. « Tu travailles où ? » — la question la plus fréquente quand on "
         "rencontre quelqu'un."),
        ("depuis quand",
         "Le point de départ. « Tu joues depuis quand ? » Réponse : « depuis l'automne », "
         "« depuis six ans »."),
        ("combien de fois",
         "La fréquence. « Tu joues combien de fois par semaine ? » Réponse : « une seule, "
         "le jeudi »."),
        ("pourquoi",
         "La raison. « Pourquoi tu as arrêté ? » Attention : la réponse commence par "
         "« parce que », jamais par « à cause de » suivi d'un verbe."),
    ], notes="La quatrième carte annonce la séance D2, où grâce à et à cause de seront "
             "travaillés. Ne pas développer.")

    d.regle('Répondre par plus quun mot',
            "Une réponse d'un seul mot ferme la conversation. Ajoutez toujours une phrase.",
            precision="« — Tu travailles où ? — À l'hôpital. » s'arrête là. « — À la "
                      "buanderie de l'hôpital. Je commence à sept heures. » donne à l'autre "
                      "quelque chose à quoi répondre. C'est la différence entre un "
                      "interrogatoire et une conversation.",
            notes="Faire l'expérience : deux élèves jouent la version courte, puis la "
                  "version longue. Le groupe entend la différence tout de suite.")

    d.piege('La question qui ne relance pas',
            "— Tu aimes ça ? — Oui.",
            "— Qu'est-ce que tu aimes le plus là-dedans ?",
            "Une question à laquelle on répond par oui ou non arrête la conversation aussi "
            "sûrement qu'un silence. Les questions ouvertes — avec où, quand, comment, "
            "pourquoi, qu'est-ce que — obligent l'autre à raconter.",
            notes="Faire transformer cinq questions fermées en questions ouvertes, au "
                  "tableau, avec le groupe.")

    d.pratique('Pratique · 1 de 2', "Écrivez la question",
               "Trouvez la question qui va avec la réponse. Employez « tu ».", [
        ("— ___ ?  — À la buanderie de l'hôpital.", "Où est-ce que tu travailles ?"),
        ("— ___ ?  — À cinq heures et quart.", "À quelle heure est-ce que tu te lèves ?"),
        ("— ___ ?  — Une fois par semaine, le jeudi.", "Tu joues combien de fois ?"),
        ("— ___ ?  — Depuis l'automne.", "Tu joues depuis quand ?"),
        ("— ___ ?  — Parce que je ne connaissais personne.", "Pourquoi est-ce que tu as arrêté ?"),
    ], corrige=True, cols=1,
       notes="Accepter les trois formes de question. Ce qui compte est le mot interrogatif "
             "choisi, pas la construction.")

    d.pratique('Pratique · 2 de 2', "Allonger la réponse",
               "Ajoutez une phrase à chaque réponse trop courte.", [
        ("— Tu travailles où ? — À l'hôpital.", "… à la buanderie. Je commence à sept heures."),
        ("— Tu joues depuis longtemps ? — Non.", "… seulement depuis l'automne. J'avais arrêté un an."),
        ("— Tu viens en autobus ? — Oui.", "… oui, mais l'arrêt est à trois coins de rue."),
        ("— Tu aimes l'hiver ? — Maintenant, oui.", "… maintenant, oui. Mon premier hiver a été dur."),
    ], corrige=True, cols=1,
       notes="Les réponses proposées ne sont que des exemples. Toute phrase qui relance "
             "est bonne. Faire lire trois productions d'élèves à voix haute.")

    d.cartes('En pratique', "Trois questions à préparer pour soi", [
        ("« Tu fais ça depuis longtemps ? »",
         "Préparez votre réponse pour une activité de votre vie : un sport, un cours, un "
         "emploi. Deux phrases suffisent."),
        ("« Qu'est-ce que tu fais dans la vie ? »",
         "Question très fréquente. Nommez le lieu et l'horaire, pas seulement le métier."),
        ("« Comment tu as connu ça ? »",
         "Presque personne n'arrive seul quelque part. Racontez qui vous en a parlé."),
    ], notes="Faire écrire les trois réponses maintenant, dans le cahier. Elles serviront "
             "au jeu de rôle de E1.")

    d.billet(
        "Écrivez cinq questions que vous poseriez à quelqu'un rencontré à une activité.",
        exemples=[
            "Cinq mots interrogatifs différents, cinq questions ouvertes.",
            "Aucune question à laquelle on peut répondre par oui ou non.",
        ],
        notes="Ramasser. Les meilleures questions serviront de banque commune au jeu de "
              "rôle de E1 — les recopier au tableau ce jour-là.")

    return d.save(dossier)
