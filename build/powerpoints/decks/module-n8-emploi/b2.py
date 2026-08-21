# -*- coding: utf-8 -*-
"""B2 · Ce que dit la norme, et ce qu'elle ne dit pas.
Bloc B « Défi 1 » · couleur teal · 75 min.
Source : exercice `t1normes` et sa mini-leçon. Faits vérifiés à la CNESST.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B2', section='teal',
        titre="Ce que dit la norme, et ce qu'elle ne dit pas",
        chapeau="Quatre règles de la Loi sur les normes du travail. Elles "
                "s'appliquent à presque tous les salariés du Québec, avec ou "
                "sans contrat écrit — et un employeur ne peut pas offrir moins.",
        duree='75 minutes')

    d.titre(notes="Séance d'information autant que de langue. Toutes les données de "
                  "cette séance ont été vérifiées sur le site de la CNESST. Ne rien "
                  "ajouter de mémoire : renvoyer à la CNESST pour tout cas particulier.")

    d.objectifs([
        "connaître le seuil des heures supplémentaires et sa majoration ;",
        "savoir à quelles conditions un congé remplace le paiement ;",
        "distinguer la période de repas de la pause-café ;",
        "nommer l'organisme responsable et les délais de recours.",
    ], notes="Rappeler que l'enseignante n'est pas juriste. L'objectif est de savoir "
             "quoi chercher et où appeler, pas de donner un avis.")

    d.regle("Le seuil, et la majoration",
            "Au-delà de quarante heures par semaine, chaque heure est majorée de cinquante pour cent.",
            precision="Le seuil est hebdomadaire, jamais quotidien : douze heures un "
                      "mardi ne sont pas supplémentaires si la semaine reste sous "
                      "quarante. Un salarié payé 22 $ l'heure reçoit 33 $ pour la "
                      "quarante et unième. Une convention collective peut prévoir "
                      "mieux ; jamais moins.",
            notes="Diapositive à photographier. C'est la donnée que Nadia cite au "
                  "téléphone en B1.")

    d.cartes("Quatre règles vérifiées", "Source : CNESST, Loi sur les normes du travail", [
        ("Les heures supplémentaires",
         "Au-delà de 40 h dans une semaine : majoration de 50 % du taux horaire habituel."),
        ("Le congé au lieu du paiement",
         "À la demande du salarié seulement. 4 heures faites donnent 6 heures de congé, à prendre dans les 12 mois."),
        ("La période de repas",
         "30 minutes après 5 heures consécutives. Non payée, sauf si le salarié ne peut pas quitter son poste."),
        ("La pause-café",
         "Aucune obligation d'en accorder. Mais si elle est accordée, elle est payée et comptée dans les heures travaillées."),
    ], notes="Diapositive à photographier. Les quatre cartes sont la matière de "
             "l'exercice interactif « Ce que dit la norme ».")

    d.tableau('Analyse', "Quand ça ne se règle pas dans l'entreprise",
              ['Le recours', 'Les conditions et le délai'],
              [["Congédiement sans cause juste et suffisante",
                "2 ans de service continu ; plainte dans les 45 jours"],
               ["Harcèlement psychologique ou sexuel",
                "plainte dans les 2 ans de la dernière manifestation"],
               ["Où s'adresser",
                "la CNESST, qui offre d'abord un service de médiation"]],
              cle=0,
              note="Ces délais sont courts et ils ne se rattrapent pas.",
              notes="Insister : devant un doute, on appelle la CNESST avant que le délai "
                    "coure, pas après. Le service de renseignement est gratuit.")

    d.piege("Confondre l'autorisation et la majoration",
            "Sans autorisation écrite, les heures ne comptent pas.",
            "L'autorisation est une exigence de l'employeur ; la majoration vient de la loi.",
            "C'est exactement la distinction que fait Sylvain en B1, et c'est ce qui "
            "rend l'appel difficile : les deux questions sont vraies en même temps. On "
            "règle la procédure interne — le courriel de la superviseure — sans jamais "
            "concéder que le travail fait ne se paie pas.",
            notes="Le point le plus subtil du bloc B. Le reprendre en E1 : c'est "
                  "l'objection que l'assistant opposera à l'élève.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "D'après les quatre règles.", [
        ("Au-delà de 40 heures par semaine, la majoration est de 50 %.", "vrai"),
        ("L'employeur peut décider seul de remplacer le paiement par un congé.", "faux — à la demande du salarié"),
        ("Le congé qui remplace le paiement se prend dans les 12 mois.", "vrai"),
        ("On a droit à 30 minutes de repas après 5 heures consécutives.", "vrai"),
        ("La période de repas est toujours payée.", "faux — sauf si on ne peut quitter son poste"),
        ("L'employeur doit accorder une pause-café.", "faux — aucune obligation"),
        ("Une pause accordée est payée.", "vrai — et comptée dans les heures"),
    ], corrige=True,
       notes="Les deux « faux » sont ceux que tout le monde se trompe. Y consacrer le "
             "temps nécessaire.")

    d.pratique('Application', "Quelle règle s'applique ?",
               "Nommez la règle, puis dites ce qui est dû.", [
        ("Quarante-quatre heures travaillées, quarante-quatre payées au taux simple.", "majoration de 50 % sur les 4 heures au-delà de 40"),
        ("Six heures d'affilée sans avoir pu manger.", "droit à 30 minutes après 5 heures consécutives"),
        ("Repas pris au poste, téléphone à répondre.", "période de repas payée"),
        ("Deux pauses de dix minutes accordées chaque jour.", "payées et comptées dans les heures travaillées"),
        ("Quatre heures supplémentaires converties en congé.", "6 heures de congé, à prendre dans les 12 mois"),
    ], corrige=True,
       notes="Exercice de transfert. Accepter toute formulation qui nomme la bonne "
             "règle et le bon chiffre.")

    d.billet(
        "Notez le numéro de la CNESST et ce qu'on peut lui demander.",
        exemples=[
            "Un renseignement se demande sans porter plainte.",
            "Quel délai s'applique à la situation d'un proche ?",
        ],
        notes="Faire chercher le numéro en classe, sur le site officiel. Ne pas le "
              "dicter de mémoire.")

    return d.save(dossier)
