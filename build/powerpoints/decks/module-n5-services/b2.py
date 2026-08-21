# -*- coding: utf-8 -*-
"""B2 · Demander sans questionner.
Bloc B « Défi 1 · L'appel » · couleur acier · 75 min. Point de langue central du module.
Source : exercice `t1inter` et sa mini-leçon.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B2', section='acier',
        titre="Demander sans questionner",
        chapeau="« Quand est-ce que le camion passe ? » est correct. Mais "
                "quatre questions de suite font un interrogatoire. La "
                "subordonnée interrogative demande la même chose et laisse "
                "l'échange se suivre.",
        duree='75 minutes')

    d.titre(notes="Séance de grammaire, et le point de langue le plus important du "
                  "module. Commencer par lire trois premières phrases du devoir B1 à voix "
                  "haute, sans nommer les auteurs, et les faire améliorer par le groupe.")

    d.objectifs([
        "construire « Pouvez-vous me dire… », « Je voudrais savoir… » ;",
        "transformer une question directe en subordonnée ;",
        "employer « si » quand la réponse est oui ou non ;",
        "employer « ce que » et « ce qui » devant une chose.",
    ])

    d.declencheur(
        'Écoute', "Deux façons de demander. Laquelle préférez-vous entendre ?",
        pistes=[
            "« Quand est-ce que le camion passe ? »",
            "« Pouvez-vous me dire quand le camion passe ? »",
            "Laquelle est plus longue ? Laquelle est plus polie ?",
            "Et si on en pose quatre de suite ?",
        ],
        notes="Dire les deux phrases sur le même ton, sans jouer la politesse : c'est la "
              "structure qui doit faire la différence, pas la voix. Le groupe entend "
              "presque toujours la seconde comme plus douce.")

    d.regle("La question est déjà posée par l'ouverture",
            "Après « je voudrais savoir », on remet l'ordre normal : sujet, puis verbe.",
            precision="Plus de « est-ce que », plus d'inversion. « Je voudrais savoir "
                      "quand le camion passe » — et non « quand est-ce que le camion "
                      "passe ». Poser la question deux fois est l'erreur numéro un de "
                      "cette structure.",
            notes="Diapositive à photographier. C'est la règle unique de la séance ; tout "
                  "le reste en découle.")

    d.tableau('Les trois ouvertures', "À apprendre par cœur",
              ['Ouverture', 'Ton', 'Exemple'],
              [["Pouvez-vous me dire…", "la plus courante", "…quand le camion passe."],
               ["Je voudrais savoir…", "la plus neutre", "…si le bac sera vidé."],
               ["J'aimerais savoir…", "la plus douce", "…où se trouve le bureau."]],
              cle=0,
              note="Les trois marchent avec n'importe quel mot de question. En choisir une et l'automatiser.",
              notes="Diapositive à photographier. Conseiller à chaque élève d'en adopter "
                    "une seule pour commencer : l'automatisme vient plus vite.")

    d.cartes("Le mot de question ne change pas", "Sauf deux cas", [
        ("quand, où, comment, combien",
         "Ils passent tels quels : « …me dire quand le camion passe. »"),
        ("est-ce que devient si",
         "Réponse oui ou non : « …savoir si le bac sera vidé. »"),
        ("qu'est-ce que devient ce que",
         "« …me dire ce qu'il faut apporter. »"),
        ("qu'est-ce qui devient ce qui",
         "« …me dire ce qui manque à mon dossier. »"),
    ], notes="Les deux dernières cartes sont celles qu'on oublie. Les faire écrire dans "
             "le cahier, en couple : la question directe à gauche, la transformation à droite.")

    d.pratique('Transformation', "Mettez la question dans une phrase",
               "Commencez par « Pouvez-vous me dire… » ou « Je voudrais savoir… ».", [
        ("Quand est-ce que le camion passe ?",
         "Pouvez-vous me dire quand le camion passe ?"),
        ("Est-ce que le bac sera vidé cette semaine ?",
         "Je voudrais savoir si le bac sera vidé cette semaine."),
        ("Qu'est-ce qu'il faut apporter ?",
         "Pouvez-vous me dire ce qu'il faut apporter ?"),
        ("Où est le bureau le plus proche ?",
         "J'aimerais savoir où se trouve le bureau le plus proche."),
        ("Combien de temps ça prend ?",
         "Je voudrais savoir combien de temps prend le traitement."),
        ("Comment je peux suivre ma requête ?",
         "Pouvez-vous me dire comment je peux suivre ma requête ?"),
        ("Est-ce que vous avez reçu mon formulaire ?",
         "Je voudrais savoir si vous avez reçu mon formulaire."),
        ("Qu'est-ce qui manque à mon dossier ?",
         "Pouvez-vous me dire ce qui manque à mon dossier ?"),
    ], corrige=True,
       notes="Faire dire chaque réponse à voix haute avant de l'écrire. La structure "
             "s'installe par l'oreille bien plus que par la règle.")

    d.piege("Garder « est-ce que » dans la phrase",
            "Je voudrais savoir quand est-ce que le camion passe.",
            "Je voudrais savoir quand le camion passe.",
            "« Je voudrais savoir » pose déjà la question. La poser une seconde fois avec "
            "« est-ce que » double la structure. C'est l'erreur la plus fréquente, et "
            "elle s'entend tout de suite.",
            notes="Écrire la forme fautive au tableau et faire venir un élève barrer ce "
                  "qui est en trop. Le geste marque plus que la correction orale.")

    d.piege("Inverser le sujet dans la subordonnée",
            "J'aimerais savoir où se trouve-t-il le bureau.",
            "J'aimerais savoir où se trouve le bureau.",
            "L'inversion appartient à la question directe. Dans une subordonnée, on "
            "revient à l'ordre normal — et le sujet ne se répète pas.",
            notes="Erreur typique des élèves qui ont bien appris l'inversion au niveau "
                  "précédent. Les féliciter d'abord, puis corriger.")


    d.billet(
        "Écrivez cinq demandes en subordonnée pour un appel que vous devez vraiment faire.",
        exemples=[
            "École, clinique, propriétaire, service de la ville — au choix.",
            "Au moins une avec « si », et une avec « ce que ».",
        ],
        notes="Devoir directement réutilisable : ces cinq phrases serviront à l'appel réel "
              "du devoir B4. Le dire pour que les élèves les prennent au sérieux.")

    return d.save(dossier)
