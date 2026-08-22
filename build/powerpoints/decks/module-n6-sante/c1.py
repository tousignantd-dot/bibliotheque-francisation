# -*- coding: utf-8 -*-
"""C1 · Vingt minutes, et c'est vous qui parlez
Bloc C « Défi 2 · Vingt minutes avec la spécialiste » · couleur acier · 75 min.
Source : dialogue `t2`, exercice `t2vf`, quatre mots de FC_CARDS.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C1', section='acier',
        titre="Vingt minutes, et c'est vous qui parlez",
        chapeau="La docteure a le dossier devant elle et préfère l'entendre "
                "de vous. Elle ne demande pas comment vous allez : elle "
                "demande ce qui a changé.",
        duree='75 minutes')

    d.titre(notes="Ouverture du Défi 2. Reprendre la phrase de Gilles restée au "
                  "tableau depuis B1 : « ne répondez pas ça va ». Toute la séance "
                  "explique pourquoi.")

    d.objectifs([
        "suivre un entretien de vingt minutes du début à la fin ;",
        "reconnaître ce qu'une spécialiste cherche quand elle pose une question ;",
        "comprendre la différence entre un résultat et une cause ;",
        "employer les quatre mots de l'entretien avec leur article.",
    ], notes="Le troisième objectif est le cœur du défi. Il n'est pas médical : "
             "c'est une distinction de raisonnement, et elle sert bien au-delà de la "
             "santé.")

    d.declencheur(
        'Observation', "Qu'est-ce que vous répondez à « comment allez-vous ? »",
        pistes=[
            "Et si la question était vraie, que répondriez-vous ?",
            "Est-ce qu'on vous a déjà demandé de préciser ?",
            "Qu'est-ce qui vous empêche de dire ce qui ne va pas ?",
        ],
        notes="Cinq minutes. Les réponses tournent vite autour de « je ne veux pas "
              "déranger ». Noter la phrase au tableau sans la commenter : elle sera "
              "reprise en C2.")

    d.dialogue('Dialogue · 1 de 3', "Je préfère l'entendre de vous", [
        ("SYLVINE", "Madame Demirci, bonjour. Sylvine Charest, je suis interniste. J'ai votre dossier devant moi, mais je préfère l'entendre de vous.", True),
        ("LEYLA", "Je suis fatiguée. Ça fait huit mois.", True),
        ("SYLVINE", "Continuez. Huit mois, ça commence quand exactement ?", True),
        ("LEYLA", "Au mois de février. C'est le mois où mon fils a déménagé à Québec.", True),
    ], consigne="Écouter d'abord, diapositive masquée.",
       notes="Faire remarquer « continuez » : la docteure ne remplit pas le silence. "
             "C'est de la place laissée, et c'est ce que les élèves interprètent le "
             "plus souvent comme un reproche.")

    d.dialogue('Dialogue · 2 de 3', "Ce n'est pas une impression", [
        ("SYLVINE", "Ne cherchez pas de moyenne, décrivez-moi une journée ordinaire. Vous vous levez à quelle heure ?", True),
        ("LEYLA", "Cinq heures et demie. Vers dix heures, il faut que je m'assoie. Avant, je ne m'assoyais pas.", True),
        ("SYLVINE", "Bon. Ça, c'est un renseignement utile : ce n'est pas une impression, c'est un changement.", True),
        ("LEYLA", "Chez madame Turcotte, il y a douze marches. Avant, je les montais en parlant. Là, j'arrête de parler.", True),
    ], notes="Arrêter sur « douze marches ». Ce n'est pas un détail pittoresque : "
             "c'est une mesure, qu'on pourra refaire dans six semaines. Le dire "
             "explicitement au groupe.")

    d.dialogue('Dialogue · 3 de 3', "Vous ressortez avec un plan", [
        ("LEYLA", "Beaucoup, ça veut dire combien ? Et est-ce que c'est grave ?", True),
        ("SYLVINE", "Assez pour qu'on ne devine pas. Un diagnostic, ce n'est pas un mot qu'on choisit : c'est un mot qu'on mérite, à force de vérifier.", True),
        ("LEYLA", "Merci, docteure. Je pensais que j'allais ressortir avec une réponse.", True),
        ("SYLVINE", "Vous ressortez avec un plan. C'est moins satisfaisant et c'est plus utile.", True),
    ], notes="Écrire au tableau : « Vous ressortez avec un plan. » Plusieurs élèves "
             "vivront ça et le liront comme un échec. Nommer maintenant ce qui sera "
             "relu en D1 dans le compte rendu.")

    d.tableau('Analyse', "Ce que la docteure cherche, question par question",
              ['Elle demande', 'Ce qu\'elle cherche'],
              [["Ça commence quand ?", "une date, ou un évènement qui en tient lieu"],
               ["Une journée ordinaire ?", "des faits, plutôt qu'une moyenne"],
               ["Autre chose ?", "ce que vous n'auriez pas pensé à relier"],
               ["Vous prenez quoi ?", "tout ce qui circule, ordonnance ou non"]],
              cle=0,
              note="Aucune de ces questions ne demande comment vous allez. Toutes demandent ce qui a changé.",
              notes="Diapositive à photographier. C'est le tableau de référence du "
                    "défi : il annonce C2 et il sert de plan au jeu de rôle de E1.")

    d.regle("Un résultat n'est pas une cause",
            "Une anémie dit ce qu'on observe ; elle ne dit pas pourquoi.",
            precision="C'est pour cela que la docteure demande d'autres examens "
                      "plutôt que de donner une réponse le jour même. La distinction "
                      "n'est pas médicale : elle vaut pour une auto qui ne démarre "
                      "pas comme pour un dossier qui bloque.",
            notes="Diapositive à photographier. Prendre un exemple hors santé si le "
                  "groupe hésite : un voyant allumé au tableau de bord est un "
                  "résultat, pas une cause.")

    d.vocabulaire('Vocabulaire', "Les quatre mots de l'entretien", [
        ("un antécédent", "Un évènement de santé déjà arrivé, qu'on redit à chaque nouveau médecin."),
        ("un prélèvement", "Le peu de sang ou de liquide qu'on prend pour le faire analyser."),
        ("un diagnostic", "Le nom donné à un problème une fois qu'on a assez vérifié pour l'écrire."),
        ("une anémie", "Un résultat d'analyse : le sang transporte l'oxygène moins bien qu'il le devrait."),
    ], notes="Faire répéter avec l'article. « Un antécédent » est long et se dit mal "
             "au pluriel : le faire dire trois fois, seul puis dans la phrase « mes "
             "antécédents sont sur cette feuille ».")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après l'entretien.", [
        ("La docteure préfère entendre l'histoire de la bouche de Leyla.", "vrai"),
        ("La fatigue a commencé le mois où son fils a déménagé.", "vrai"),
        ("Une anémie légère indique déjà la cause du problème.", "faux - c'est un résultat"),
        ("La docteure refuse de dire si c'est grave, et explique pourquoi.", "vrai"),
        ("Le laboratoire est au troisième étage.", "faux - au rez-de-chaussée"),
        ("Le compte rendu ira au médecin de famille.", "vrai"),
    ], corrige=True,
       notes="Faire justifier chaque « faux » par la réplique exacte. Le troisième "
             "est le plus important du module : y revenir même s'il est réussi.")

    d.billet(
        "Qu'est-ce qui a changé chez vous depuis un an ?",
        exemples=[
            "Quelque chose de banal fait très bien l'affaire.",
            "Dites l'avant et le maintenant, dans la même phrase.",
        ],
        notes="Deux minutes. Le sujet n'a pas à être médical : le sommeil, le "
              "français, le travail, le trajet. Ce qui s'entraîne, c'est la forme "
              "« avant ceci, maintenant cela ».")

    return d.save(dossier)
