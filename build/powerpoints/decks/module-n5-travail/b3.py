# -*- coding: utf-8 -*-
"""B3 · « Elle dit que », « elle demande si »
Bloc B « Défi 1 » · couleur acier · 75 min. Discours rapporté au présent.
Source : dialogue `t1` (message de madame Thériault), exercice `t1rap`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B3', section='acier',
        titre="« Elle dit que », « elle demande si »",
        chapeau="Quand vous prenez un message, vous n'êtes plus celle qui "
                "parle : vous êtes celle qui raconte ce que quelqu'un "
                "d'autre a dit. Le français a une façon précise de faire "
                "ça, et elle change trois choses à la fois.",
        duree='75 minutes')

    d.titre(notes="Séance de grammaire centrale du module, et celle que les attentes de "
                  "fin de cours du niveau 5 nomment explicitement : « rapporter le sens "
                  "général des propos de quelqu'un au présent en employant les pronoms "
                  "et les déterminants appropriés ».")

    d.objectifs([
        "rapporter une affirmation avec « que » ;",
        "rapporter une question fermée avec « si » ;",
        "rapporter une question ouverte en gardant le mot interrogatif ;",
        "changer les pronoms en passant du direct au rapporté.",
    ])

    d.dialogue('Écoute', "Le message de madame Thériault", [
        ("THERIAULT", "Oui bonjour, c'est madame Thériault, du 5680 rue Beaubien, "
                      "appartement 3. Je vous appelle parce que la dame qui vient le "
                      "mercredi matin m'a dit qu'elle ne pourrait pas venir cette "
                      "semaine.", True),
        ("THERIAULT", "Alors moi je voulais savoir si quelqu'un d'autre peut passer, "
                      "parce que j'ai mon rendez-vous à la clinique jeudi et il faut "
                      "que quelqu'un m'aide avant.", True),
        ("THERIAULT", "Rappelez-moi avant midi si possible, après je ne réponds pas. "
                      "Merci beaucoup.", True),
    ], consigne="Écoutez deux fois. Ne prenez pas de notes à la première écoute.",
       notes="Faire écouter une première fois sans écrire, une seconde en écrivant. La "
             "différence entre les deux écoutes est le sujet de la séance B4. Ici, on ne "
             "travaille que la transformation des phrases.")

    d.regle("Rapporter change trois choses",
            "Le mot qui relie les deux phrases, les pronoms, et l'ordre des "
            "mots dans la question.",
            precision="Le verbe qui rapporte reste au présent : elle dit, elle "
                      "demande, il explique. Une note d'appel est lue le jour même : "
                      "rien n'oblige à passer au passé.",
            notes="Diapositive à photographier. Insister sur le présent : beaucoup "
                  "d'élèves ont appris le discours rapporté au passé et compliquent tout.")

    d.tableau('Trois cas', "Ce qu'on entend, et ce qu'on écrit",
              ['Ce qu\'elle dit', 'Ce qu\'on écrit'],
              [["Je ne peux pas venir mercredi.", "Elle dit qu'elle ne peut pas venir mercredi."],
               ["Est-ce que quelqu'un peut passer ?", "Elle demande si quelqu'un peut passer."],
               ["Quand est-ce que vous rappelez ?", "Elle demande quand nous rappelons."],
               ["Qu'est-ce qu'il faut apporter ?", "Elle demande ce qu'il faut apporter."],
               ["Rappelez-moi avant midi.", "Elle demande de la rappeler avant midi."]],
              cle=1,
              notes="Cinq lignes, cinq mécanismes différents. Les faire lire une à une et "
                    "demander chaque fois ce qui a disparu : « est-ce que », l'inversion, "
                    "le point d'interrogation, l'impératif.")

    d.cartes("Les mots qui relient", "Un par sorte de phrase", [
        ("Une affirmation : « que »",
         "Elle dit qu'elle ne peut pas venir. Il explique que le formulaire est signé."),
        ("Une question fermée : « si »",
         "Elle demande si la journée est payée. Jamais « si est-ce que »."),
        ("Une question ouverte : le mot reste",
         "Elle demande quand nous rappelons, où est le formulaire, qui remplace."),
        ("Un ordre : « de » plus l'infinitif",
         "Elle demande de la rappeler. Il demande d'envoyer le formulaire."),
    ], notes="La quatrième carte est celle qu'on oublie d'enseigner. Or c'est la plus "
             "utile dans une note d'appel : les gens demandent presque toujours qu'on "
             "fasse quelque chose.")

    d.piege("Garder « est-ce que »",
            "Elle demande si est-ce que quelqu'un peut venir.",
            "Elle demande si quelqu'un peut venir.",
            "« Si » remplace « est-ce que » : il ne s'ajoute pas à lui. Une seule des "
            "deux formes survit, et c'est « si ».",
            notes="Faire dire la faute à voix haute par le groupe, puis la version juste. "
                  "L'oreille attrape la lourdeur avant que la règle ne l'explique.")

    d.piege("Oublier de changer les pronoms",
            "Elle dit que je ne peux pas venir mercredi.",
            "Elle dit qu'elle ne peut pas venir mercredi.",
            "En rapportant, « je » devient « elle » et « mon » devient « son ». Sans "
            "ce changement, la note fait croire que c'est vous qui ne venez pas.",
            notes="Cette faute-là a des conséquences réelles : une note mal rapportée "
                  "envoie quelqu'un chercher la mauvaise personne. Le dire.")

    d.pratique('Transformation', "Rapportez au présent",
               "Commencez par les mots donnés.", [
        ("« Je ne peux pas venir cette semaine. » Elle dit…", "qu'elle ne peut pas venir cette semaine"),
        ("« Est-ce que quelqu'un peut passer ? » Elle demande…", "si quelqu'un peut passer"),
        ("« Quand est-ce que vous me rappelez ? » Elle demande…", "quand nous la rappelons"),
        ("« Où est le formulaire ? » Il demande…", "où est le formulaire"),
        ("« Qu'est-ce qu'il faut remplir ? » Elle demande…", "ce qu'il faut remplir"),
        ("« Rappelez-moi avant midi. » Elle demande…", "de la rappeler avant midi"),
        ("« Mon rendez-vous est jeudi matin. » Elle dit…", "que son rendez-vous est jeudi matin"),
        ("« Envoyez le formulaire à la paie. » Il demande…", "d'envoyer le formulaire à la paie"),
    ], cols=2, corrige=True,
       notes="Les huit énoncés sont ceux de l'exercice interactif. Faire l'oral en groupe, "
             "puis laisser les élèves les refaire seuls sur les postes.")

    d.pratique('Écoute et transformation', "Le message de madame Thériault",
               "Rapportez quatre phrases du message que vous venez d'entendre.", [
        ("Ce qu'elle annonce sur son aide du mercredi.", "Elle dit que son aide du mercredi ne viendra pas."),
        ("Ce qu'elle demande à la coopérative.", "Elle demande si quelqu'un d'autre peut passer."),
        ("Ce qu'elle dit de son rendez-vous.", "Elle dit que son rendez-vous est jeudi."),
        ("Ce qu'elle demande à la fin.", "Elle demande de la rappeler avant midi."),
    ], corrige=True,
       notes="Ces quatre phrases sont exactement les quatre lignes centrales de la note "
             "de B4. Le dire au groupe : la grammaire d'aujourd'hui est l'outil de demain.")

    d.billet(
        "Écoutez quelqu'un parler deux minutes, puis rapportez trois de ses phrases.",
        exemples=[
            "Une affirmation, une question fermée, une question ouverte.",
            "Commencez chaque fois par « il dit que », « elle demande si », "
            "« il demande quand ».",
        ],
        notes="Faire faire l'exercice en équipes de deux, en classe, si le temps le "
              "permet : l'un raconte sa fin de semaine, l'autre rapporte. C'est plus "
              "vivant qu'un devoir.")

    return d.save(dossier)
