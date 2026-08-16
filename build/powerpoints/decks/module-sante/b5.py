# -*- coding: utf-8 -*-
"""B5 · Au comptoir, en vrai — jeu de rôle.
Bloc B « Défi 1 · À la pharmacie » · couleur teal (production orale) · 60 min.
Source du module : dialogue `t1`, exercices `co1` et `co3` — production orale du défi 1.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B5', section='teal',
        titre='Au comptoir, en vrai',
        chapeau="Tout le défi 1 dans un seul échange de deux minutes : présenter son "
                "ordonnance, écouter la posologie, poser une question, confirmer.",
        duree='60 minutes')

    d.titre(notes="Séance de production orale. Redistribuer les billets de B1 et B4 : "
                  "chacun a déjà écrit sa question et sa formule de vérification.")

    d.objectifs([
        "mener un échange complet au comptoir de la pharmacie ;",
        "poser au moins une question sur son traitement ;",
        "confirmer ce qu'on a compris avant de partir ;",
        "reconnaître ce qui manque dans une consigne.",
    ])

    d.regle('La règle des quatre temps',
            "Je présente · j'écoute · je demande · je confirme.",
            precision="Quatre temps, deux minutes. C'est le déroulement de tout passage "
                      "en pharmacie, et c'est la grille d'évaluation d'aujourd'hui.",
            notes="Écrire les quatre au tableau et les y laisser toute la séance. Ce "
                  "sont les critères, et les élèves doivent les avoir sous les yeux.")

    d.cartes('Analyse', "Ce qu'on dit à chaque temps", [
        ("Je présente",
         "« Bonjour, j'ai une ordonnance du médecin pour des antibiotiques. »"),
        ("J'écoute",
         "Sans interrompre. Le pharmacien donne combien, quand, combien de temps, et "
         "l'interdiction."),
        ("Je demande",
         "« Est-ce que je peux le prendre avec de la nourriture ? » Une question, au "
         "moins — c'est le cœur de l'échange."),
        ("Je confirme",
         "« Donc un comprimé matin et soir, pendant sept jours ? » Puis on remercie et "
         "on part."),
    ], notes="Les quatre temps viennent du dialogue de B1. Les faire retrouver dans le "
             "texte avant de commencer le jeu de rôle.")

    d.pratique('Pratique · 1 de 3', "Qu'est-ce qui manque ?",
               "Trois échanges incomplets. Que faut-il ajouter ?", [
        ("Le client présente, écoute, remercie et part.",
         "il n'a rien demandé et n'a rien confirmé"),
        ("Le client présente, demande, confirme — mais n'a pas écouté la durée.",
         "il ignore combien de temps dure le traitement"),
        ("Le client demande trois fois la même chose.",
         "il n'a pas reformulé : « donc c'est bien… » aurait réglé la question"),
    ], corrige=True,
       notes="Les faire jouer par l'enseignant, très vite, avant de les analyser. "
             "Entendre l'échange raté vaut mieux que le lire.")

    d.pratique('Pratique · 2 de 3', "Trois ordonnances",
               "À deux, jouez les quatre temps. Le pharmacien lit sa fiche.", [
        ("Antibiotique",
         "un comprimé, deux fois par jour, sept jours, pas d'alcool"),
        ("Sirop pour la toux",
         "une cuillère, trois fois par jour, au besoin, ne pas conduire après"),
        ("Crème pour la peau",
         "une application le soir, dix jours, éviter le soleil"),
    ], corrige=False,
       notes="Vingt minutes, trois tours, on échange les rôles à chaque fois. Le "
             "deuxième et le troisième cas ne sont pas dans le module : le client doit "
             "écouter pour de vrai, il ne peut pas réciter.")

    d.piege("Le piège de la question polie inutile",
            "Est-ce que je peux vous demander quelque chose, s'il vous plaît ?",
            "Est-ce que je peux le prendre avec de la nourriture ?",
            "Demander la permission de poser une question fait perdre le tour de parole "
            "et le fil. Au comptoir, on pose directement la question : c'est déjà poli, "
            "et c'est ce que le pharmacien attend.",
            notes="Beaucoup d'élèves surchargent leurs demandes de politesse. Le dire "
                  "explicitement : la politesse est dans le ton, pas dans la longueur.")

    d.pratique('Pratique · 3 de 3', "Votre vrai passage en pharmacie",
               "Avec votre propre médicament, ou celui d'un proche.", [
        ("Ce que vous présentez", "une ordonnance, un renouvellement, une question"),
        ("Ce que vous voulez savoir", "la question de votre billet de B1"),
        ("Ce que vous confirmerez", "la formule de votre billet de B4"),
        ("Le temps que ça prend", "deux minutes, pas plus"),
    ], corrige=False,
       notes="Quinze minutes. Écouter deux ou trois passages devant le groupe si "
             "l'ambiance le permet, jamais en obligeant.")

    d.billet(
        "Notez la question que vous n'avez pas osé poser la dernière fois.",
        exemples=[
            "À la pharmacie, chez le médecin, ou ailleurs.",
            "Écrivez-la telle que vous la poserez la prochaine fois.",
        ],
        notes="Ramasser. C'est le billet le plus révélateur du module : il dit ce qui "
              "bloque vraiment, et il oriente la révision de E2.")

    return d.save(dossier)
