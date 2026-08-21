# -*- coding: utf-8 -*-
"""B2 · Demander poliment, sans avoir l'air de commander
Bloc B « Défi 1 » · couleur ambre · 75 min. Écriture et grammaire.
Source : exercice `t1dem` et sa mini-leçon (la question indirecte).
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B2', section='ambre',
        titre="Demander poliment, sans avoir l'air de commander",
        chapeau="« Le trajet dure combien de temps ? » n'est pas impoli, "
                "mais c'est sec. « Pourriez-vous me dire combien de temps "
                "dure le trajet ? » ouvre la même porte plus largement — et "
                "la question change de forme en passant.",
        duree='75 minutes')

    d.titre(notes="Séance de grammaire. Le point est double : le conditionnel de "
                  "politesse, et le fait que la question indirecte remet le sujet et le "
                  "verbe dans l'ordre de la phrase déclarative. Le second point est "
                  "celui qu'on manque.")

    d.objectifs([
        "employer « je voudrais » et « pourriez-vous » à la place de l'impératif ;",
        "transformer une question directe en question indirecte ;",
        "remettre le sujet avant le verbe dans la question indirecte ;",
        "poser trois questions polies de suite sans répéter la même formule.",
    ], notes="Le quatrième objectif est pratique : un élève qui n'a qu'une formule la "
             "répète cinq fois et s'entend. Trois formules suffisent à faire un échange "
             "naturel.")

    d.regle("La question indirecte remet la phrase à l'endroit",
            "« Est-ce que je pourrais… », « Je voudrais savoir si… », "
            "« Pourriez-vous me dire… » — puis sujet, puis verbe.",
            precision="On ne dit pas « Pourriez-vous me dire combien coûte-t-il ». "
                      "Après la formule, la question redevient une phrase ordinaire.",
            notes="Diapositive à photographier. C'est l'erreur la plus fréquente et elle "
                  "survit longtemps : l'élève garde l'inversion de la question directe "
                  "et l'ajoute à la formule polie.")

    d.tableau('Deux formes', "La même question, deux façons",
              ['Question directe', 'Question indirecte'],
              [["Combien ça coûte ?", "Pourriez-vous me dire combien ça coûte ?"],
               ["Où est le quai ?", "Je voudrais savoir où est le quai."],
               ["Est-ce que c'est direct ?", "Je voudrais savoir si c'est direct."],
               ["Quand partez-vous ?", "Pourriez-vous me dire quand vous partez ?"]],
              cle=1,
              notes="La quatrième ligne montre le point crucial : « partez-vous » "
                    "devient « vous partez ». Faire relever le changement par le groupe "
                    "avant de l'expliquer.")

    d.cartes("Trois formules, trois usages", "Elles ne sont pas interchangeables", [
        ("Je voudrais…",
         "Pour dire ce qu'on veut : « Je voudrais un aller-retour. »"),
        ("Je voudrais savoir si…",
         "Pour une question à laquelle on répond oui ou non."),
        ("Pourriez-vous me dire…",
         "Pour une question ouverte : combien, quand, où, comment."),
        ("Est-ce que je pourrais…",
         "Pour demander une permission : changer la date, payer plus tard."),
    ], notes="Faire trouver au groupe un exemple de chacune, tiré de leur propre voyage. "
             "La quatrième est celle qu'on oublie et qui sert le plus souvent : "
             "demander la permission de faire quelque chose.")

    d.piege("Garder l'inversion après la formule polie",
            "Pourriez-vous me dire à quelle heure part-il ?",
            "Pourriez-vous me dire à quelle heure il part ?",
            "La formule polie contient déjà sa question. Ce qui suit est une "
            "phrase ordinaire : sujet, puis verbe. Deux questions dans la même "
            "phrase, c'est une de trop.",
            notes="Faire corriger cinq phrases au tableau. C'est le seul exercice de la "
                  "séance qui demande de l'entraînement mécanique, et il le vaut.")

    d.pratique('Transformation', "Rendez la question polie",
               "À l'oral d'abord, puis à l'écrit.", [
        ("Le trajet dure combien de temps ?", "Pourriez-vous me dire combien de temps dure le trajet ?"),
        ("Il faut changer d'autocar ?", "Je voudrais savoir s'il faut changer d'autocar."),
        ("Je peux apporter une grosse valise ?", "Est-ce que je pourrais apporter une grosse valise ?"),
        ("Le quai est où ?", "Pourriez-vous me dire où est le quai ?"),
        ("Vous partez à quelle heure ?", "Pourriez-vous me dire à quelle heure vous partez ?"),
        ("Je peux changer la date ?", "Est-ce que je pourrais changer la date ?"),
    ], corrige=True,
       notes="Faire dire chaque réponse à voix haute et sur un ton posé : la politesse "
             "passe autant par le débit que par les mots. Un « pourriez-vous » lancé "
             "vite sonne plus sec qu'un « combien ça coûte » dit doucement.")

    d.tableau('Le ton compte aussi', "Ce qui se remarque au comptoir",
              ['Ce qui aide', 'Ce qui nuit'],
              [["Saluer avant de demander", "Commencer par sa question"],
               ["Une information par phrase", "Tout dire d'un souffle"],
               ["Laisser finir la réponse", "Poser la suivante trop vite"],
               ["Remercier à la fin", "Partir sans rien dire"]],
              cle=1,
              notes="Rien de tout cela n'est du vocabulaire, et tout se remarque. Le "
                    "dire une fois clairement évite bien des malentendus attribués à "
                    "tort au niveau de langue.")

    d.billet(
        "Écrivez trois questions polies que vous poseriez pour votre propre voyage.",
        exemples=[
            "Trois formules différentes : ne répétez pas « pourriez-vous » trois fois.",
            "Relisez-les : le sujet est-il bien avant le verbe ?",
        ],
        notes="Ramasser les billets. Les trois questions servent directement au jeu de "
              "rôle de E1 : l'élève arrive avec ses questions déjà écrites, ce qui "
              "change tout.")

    return d.save(dossier)
