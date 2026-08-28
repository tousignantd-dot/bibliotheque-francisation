# -*- coding: utf-8 -*-
"""D2 · La forme qui commande, et où on en est.
Bloc D « Défi 3 · Trois choses avant midi » · couleur ambre · 60 min.
Source : exercices `t3imp`, `t3aspect` et `t3ecoute`, mini-leçons `t3imp` et `t3aspect`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='D2', section='ambre',
        titre="La forme qui commande, et où on en est",
        chapeau="« Sortez », « rangez », « éteignez » : le verbe passe en "
                "premier et le sujet disparaît. Et quand le chef revient, "
                "trois réponses possibles — c'est fait, je suis en train, "
                "je vais le faire.",
        duree='60 minutes')

    d.titre(notes="Séance d'écriture, dernière avant les productions. Commencer par la "
                  "lecture des consignes notées au billet de D1 : elles contiennent "
                  "presque toutes un impératif, sans que les élèves l'aient su.")

    d.objectifs([
        "reconnaître et former l'impératif en -ez ;",
        "employer la négation « n'oubliez pas » ;",
        "dire où on en est : c'est fait, en train de, je vais ;",
        "répondre à un chef qui demande si c'est terminé.",
    ])

    d.regle("Le sujet disparaît",
            "Vous sortez les plateaux. — Sortez les plateaux.",
            precision="Pour donner une consigne, on enlève le mot « vous » "
                      "et le verbe se retrouve en premier. Rien d'autre ne "
                      "change. Ce n'est pas impoli : c'est la forme normale "
                      "du travail, souvent adoucie par « s'il vous plaît ».",
            notes="Diapo à photographier. Le dernier point compte beaucoup : plusieurs "
                  "élèves entendent un impératif comme un reproche et se croient mal "
                  "vus. Le dire explicitement enlève une inquiétude réelle.")

    d.tableau('Analyse', "Trois formes, et une seule sert vraiment",
              ["La forme", "À qui on parle"],
              [["range", "à un collègue qu'on tutoie"],
               ["rangez", "à vous, ou à plusieurs, ou poliment"],
               ["rangeons", "à tout le groupe, en s'incluant"]],
              cle=1,
              note="Au travail, c'est presque toujours la forme en -ez. Les "
                   "deux autres s'entendent, mais rarement d'un chef "
                   "d'équipe.",
              notes="Diapo à photographier. Ne pas faire conjuguer les trois formes pour "
                    "vingt verbes : donner celle qui sert, et laisser les autres se "
                    "reconnaître à la lecture.")

    d.pratique('Écriture', "Mettez le verbe à la forme du chef d'équipe",
               "La forme en -ez, sans le mot « vous ».", [
        ("___ les plateaux du chariot. (sortir)", "Sortez"),
        ("___ les boîtes dans la chambre froide. (ranger)", "Rangez"),
        ("___ le four à onze heures. (éteindre)", "Éteignez"),
        ("N'___ pas de poinçonner en arrivant. (oublier)", "oubliez"),
        ("___ me voir avant votre pause. (venir)", "Venez"),
        ("___ là à six heures, s'il vous plaît. (être)", "Soyez"),
    ], corrige=True,
       notes="C'est l'exercice `t3imp` du module interactif, mot pour mot. Les deux "
             "dernières lignes sont irrégulières : « venez », « faites », « soyez » "
             "s'apprennent par cœur, il n'y a pas de règle utile derrière.")

    d.regle("La négation entoure le verbe",
            "N'oubliez pas le four. Ne partez pas avant midi.",
            precision="Comme d'habitude : « ne » devant, « pas » derrière. "
                      "C'est la forme qu'un chef emploie pour ce qui a déjà "
                      "été oublié une fois.",
            notes="Diapo à photographier. À l'oral, le « ne » tombe souvent : « oubliez "
                  "pas le four ». Le signaler pour la compréhension, mais faire écrire "
                  "la forme complète.")

    d.tableau('Analyse', "Dire où on en est",
              ["La réponse", "Ce qu'elle dit"],
              [["C'est fait. Je viens de finir.", "terminé, à l'instant"],
               ["Je suis en train de le faire.", "commencé, pas fini"],
               ["Je vais le faire à onze heures.", "pas commencé, mais prévu"]],
              cle=1,
              note="Les trois sont de bonnes réponses. La seule mauvaise "
                   "est celle qui laisse croire que c'est fait quand ça ne "
                   "l'est pas.",
              notes="Diapo à photographier. C'est le tableau le plus utile du défi : un "
                    "chef d'équipe ne demande pas si c'est parfait, il demande où on en "
                    "est pour organiser la suite.")

    d.pratique('Écriture', "Viens de, suis en train de, ou vais",
               "Dites où en est la tâche.", [
        ("Les plateaux sont sortis depuis deux minutes : je ___ finir.", "viens de"),
        ("Il me reste trois boîtes : je ___ les ranger.", "suis en train de"),
        ("Il est dix heures et demie : je ___ éteindre le four dans trente minutes.", "vais"),
        ("Le lave-vaisselle tourne encore : il ___ laver la dernière brassée.", "est en train de"),
        ("Tout est terminé : les trois tâches, ___ .", "c'est fait"),
    ], corrige=True,
       notes="C'est l'exercice `t3aspect` du module interactif, mot pour mot. Après ces "
             "trois tournures, le verbe reste à l'infinitif — c'est la même règle qu'au "
             "défi 2 avec pouvoir et devoir.")

    d.pratique('Écoute', "C'est fait, ou pas encore ?",
               "Écoutez la phrase : est-ce que la tâche est terminée ?", [
        ("Je viens de finir les plateaux.", "c'est fait"),
        ("Je suis en train de ranger les boîtes.", "pas encore"),
        ("Le four est éteint depuis onze heures.", "c'est fait"),
        ("Je vais poinçonner dans deux minutes.", "pas encore"),
        ("Les plateaux, c'est fait.", "c'est fait"),
        ("Il me reste trois boîtes.", "pas encore"),
        ("J'ai terminé la chambre froide.", "c'est fait"),
        ("Je commence tout de suite après ma pause.", "pas encore"),
    ], corrige=True,
       notes="C'est l'exercice `t3ecoute` du module interactif, mot pour mot. Le faire "
             "livre fermé : c'est le petit mot du début — viens, suis, vais — qui donne "
             "la réponse, et il passe vite.")

    d.billet(
        "Écrivez où vous en êtes dans trois tâches d'aujourd'hui.",
        exemples=[
            "Une terminée, une commencée, une à venir.",
            "« Les plateaux, c'est fait. Je suis en train de… »",
        ],
        notes="Devoir court. Ces trois phrases entrent telles quelles dans le mot écrit "
              "de E1 : le dire, ça change le soin que les élèves y mettent.")

    return d.save(dossier)
