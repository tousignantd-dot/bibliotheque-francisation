# -*- coding: utf-8 -*-
"""D1 · Personne ne s'occupe de ça
Bloc D « Défi 3 · Le suivi, après » · couleur acier · 75 min.
Source : dialogue `t3`, exercices `t3vf` et `t3avis` (type texte).
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='D1', section='acier',
        titre="Personne ne s'occupe de ça",
        chapeau="La lettre dit que la candidature est retenue et qu'elle est "
                "sur la liste d'attente. Ni le rang, ni jusqu'à quand, ni ce "
                "qu'il faudrait faire. Il n'y a pas de comptoir pour ça.",
        duree='75 minutes')

    d.titre(notes="Ouverture du bloc D, et cœur du module. Prévenir le groupe : cette "
                  "séance ne porte pas sur un refus, mais sur ce qu'on fait quand "
                  "aucune procédure n'existe.")

    d.objectifs([
        "distinguer « retenue » et « admise » dans un avis ;",
        "trouver dans une lettre la date et le nom qui donnent prise ;",
        "comprendre ce qu'une liste d'attente fait et ne fait pas ;",
        "employer quatre mots du suivi avec leur article.",
    ], notes="Le premier objectif est celui qui décide de tout : deux personnes lisent "
             "la même lettre, l'une comprend qu'elle a réussi, l'autre qu'elle est "
             "refusée, et aucune n'a raison.")

    d.declencheur(
        'Observation', "Que faites-vous d'une réponse qui ne répond pas ?",
        pistes=[
            "« Votre candidature a été retenue. » — c'est un oui ou un non ?",
            "« Le rang n'est pas communiqué. » — pourquoi ?",
            "Qui, dans un établissement, s'occupe des gens sur une liste ?",
            "Que reste-t-il à faire quand la réponse est « personne » ?",
        ],
        notes="La troisième question est la vraie question du bloc. La réponse honnête "
              "est « personne », et c'est ce qui rend l'appel de suivi nécessaire.")

    d.dialogue('Dialogue · 1 de 3', "Le rang ne se communique pas", [
        ("RANIA", "Bonjour. Rania Nassar, dossier 41-2887. J'appelle au sujet de la lettre de lundi.", True),
        ("RANIA", "Elle dit que je suis sur la liste d'attente. Je voudrais savoir à quel rang je suis.", True),
        ("NADINE", "Le rang ne se communique pas, madame. Ce n'est pas moi qui décide de ça.", True),
        ("RANIA", "Je comprends. Est-ce que quelqu'un s'occupe des personnes qui sont sur la liste ?", True),
    ], consigne="Écouter d'abord, diapositive masquée.",
       notes="Faire remarquer les trois premiers éléments : nom, numéro de dossier, "
             "motif. Dix secondes, et la personne au bout du fil a ouvert le dossier.")

    d.dialogue('Dialogue · 2 de 3', "Un message précis", [
        ("NADINE", "Personne ne s'en occupe comme telle. La liste bouge quand une personne se désiste.", True),
        ("RANIA", "Monsieur Fiset m'avait dit de le rappeler après la décision. Est-ce qu'il est là ?", True),
        ("NADINE", "Il est en rencontre jusqu'à onze heures. Vous voulez que je lui dise quoi exactement ?", True),
        ("RANIA", "Que j'ai rappelé comme il l'avait demandé, au sujet du dossier 41-2887.", True),
    ], notes="Le message laissé est un contenu à part entière : nom, dossier, motif en "
             "une phrase, numéro. Le faire relever au tableau par le groupe.")

    d.dialogue('Dialogue · 3 de 3', "Une seule case", [
        ("ÉMILIEN", "Il y avait vingt-quatre places et quarante et une candidatures retenues.", True),
        ("ÉMILIEN", "Ceux qui sont passés devant vous avaient tous leur préalable de mathématiques.", True),
        ("RANIA", "Donc ce n'est ni l'entrevue ni la lettre. C'est une seule case.", True),
        ("ÉMILIEN", "Une seule case, oui. Et c'est une bonne nouvelle, parce qu'une case, ça se remplit.", True),
    ], notes="Réplique finale à faire répéter. C'est la phrase que le module veut "
             "laisser : ce qui manque est nommable, donc réparable.")

    d.tableau('Analyse', "Ce que l'avis dit, et ce qu'il cache",
              ['Dans la lettre', 'Ce que ça veut dire'],
              [['retenue', "le dossier a passé la sélection"],
               ['admise', "il y avait une place"],
               ["liste d'attente", "retenue, sans place, appelée si quelqu'un se désiste"],
               ['rang non communiqué', "inutile de le redemander, il change tous les jours"],
               ['dossier actif', "rien à refaire d'ici la date indiquée"]],
              cle=0,
              notes="Cinq rangées sans note : la densité tient. Diapositive à "
                    "photographier, c'est le vocabulaire de tous les avis "
                    "d'admission du Québec.")

    d.regle("Un avis dit trois choses et en cache une quatrième",
            "Il dit ce qui a été décidé, sur quoi, à quelle date. Il ne dit jamais ce "
            "qu'il faudrait changer.",
            precision="Cette quatrième chose ne s'obtient qu'au téléphone, et "
                      "seulement si l'on appelle. C'est aussi la seule qui serve à "
                      "l'année suivante.",
            notes="Diapositive à photographier. Faire chercher, dans l'avis distribué, "
                  "la phrase qui contient une date et celle qui nomme une personne : "
                  "ce sont les deux prises.")

    d.vocabulaire('Vocabulaire', "Quatre mots du suivi", [
        ("une liste d'attente", "Le classement des personnes retenues qui n'ont pas eu de place."),
        ("un rang", "La position d'une personne dans un classement."),
        ("une mise à niveau", "Le cours court qu'on suit pour atteindre le niveau exigé."),
        ("la reconnaissance des acquis", "La démarche qui évalue ce qu'une personne sait déjà faire."),
    ], notes="Préciser ce que la reconnaissance des acquis ne fait pas : elle ne fait "
             "pas entrer dans un programme contingenté. Elle est gratuite et se "
             "demande au centre de services scolaire.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après les deux appels.", [
        ("La lettre indique le rang de Rania sur la liste.", "faux - le rang ne se communique pas"),
        ("Une personne du centre est chargée de faire avancer les dossiers.", "faux - personne"),
        ("Rania rappelle parce que le conseiller le lui avait demandé.", "vrai"),
        ("Selon le conseiller, l'entrevue s'est mal passée.", "faux - elle s'est très bien passée"),
        ("Il lui manque le préalable de mathématiques.", "vrai"),
        ("Le conseiller lui promet une place en janvier.", "faux - il ne promet rien"),
    ], corrige=True,
       notes="Le dernier item compte le plus : un conseiller honnête ne promet jamais "
             "une place, et l'élève doit apprendre à ne pas entendre une promesse là "
             "où il n'y en a pas.")

    d.billet("Écris ce que tu dirais dans les vingt premières secondes d'un appel de "
             "suivi.",
             exemples=["Bonjour, Rania Nassar, dossier 41-2887.",
                       "Je vous appelle au sujet de la lettre du 10 avril."],
             notes="Ramasser les billets : ils préparent directement la séance E1, où "
                   "l'appel se joue en entier.")

    return d.save(dossier)
