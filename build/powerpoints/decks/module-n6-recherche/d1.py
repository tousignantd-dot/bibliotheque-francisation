# -*- coding: utf-8 -*-
"""D1 · Parlez-moi de votre expérience.
Bloc D « Défi 3 · L'entrevue » · couleur acier · 75 min.
Source : dialogue `t3`, exercices `t3vf` et `t3quest`.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n6-recherche/images/')


def build(dossier):
    d = Deck(
        code='D1', section='acier',
        titre="Parlez-moi de votre expérience",
        chapeau="Vingt minutes, une table, et des questions ouvertes. Une "
                "réponse d'une phrase ferme la porte ; une réponse avec un "
                "exemple précis l'ouvre.",
        duree='75 minutes')

    d.titre(notes="Première séance du Défi 3. C'est la séance que le groupe attend "
                  "depuis le début du module : dire clairement que tout ce qui précède "
                  "servait à celle-ci.")

    d.objectifs([
        "comprendre ce que cache une question d'entrevue ;",
        "répondre en trois ou quatre phrases plutôt qu'en une ;",
        "raconter un exemple précis avec un chiffre ;",
        "dire honnêtement ce qu'on ne connaît pas encore.",
    ], notes="Le quatrième objectif surprend. Il est pourtant celui qui a fait bonne "
             "impression dans le dialogue : l'employeur y a répondu « c'est la bonne "
             "attitude ».")

    d.declencheur(
        'Observation', "« Parlez-moi de votre expérience. »",
        image=IMG + 'entrevue-table.jpg',
        pistes=[
            "Que répondriez-vous ?",
            "En combien de phrases ?",
            "Qu'est-ce que l'employeur veut vraiment savoir ?",
            "Et si vous n'aviez que dix secondes ?",
        ],
        notes="Faire répondre deux ou trois personnes à voix haute, sans corriger. Les "
              "réponses courtes serviront de matière à la séance D2.")

    d.dialogue('Dialogue · 1 de 3', "Une réponse développée", [
        ("ROBERT", "Asseyez-vous. J'ai lu votre demande. Parlez-moi de votre expérience en inventaire.", True),
        ("MARISOL", "J'ai été responsable des stocks pendant six ans, dans une entreprise de meubles en Colombie. Une entreprise comparable à la vôtre, entre autres par la taille : une quarantaine d'employés.", True),
        ("ROBERT", "Et concrètement, vous faisiez quoi dans une journée ?", True),
        ("MARISOL", "Je recevais les livraisons le matin, je vérifiais les quantités, et j'entrais tout dans le système. L'après-midi, je préparais les commandes, notamment celles qui partaient le lendemain.", True),
    ], consigne="Écoutez d'abord, diapositive masquée.",
       notes="Marisol emploie « entre autres » et « notamment ». Ce n'est pas un ornement : "
             "ce sont les mots qui lui permettent de développer sans se répéter. La "
             "séance D2 y revient.")

    d.dialogue('Dialogue · 2 de 3', "L'exemple qui convainc", [
        ("ROBERT", "Vous avez déjà trouvé des écarts importants ?", True),
        ("MARISOL", "Oui, une fois : trois cents pieds de planches qui manquaient. Après avoir vérifié les bons de réception, j'ai vu que la livraison était incomplète depuis le début. Le fournisseur nous a remboursés.", True),
        ("ROBERT", "Bonne réponse. C'est exactement le genre de chose que je veux qu'on me signale tout de suite.", True),
    ], notes="Trois temps dans la réponse : la situation, ce qu'elle a fait, ce que ça a "
             "donné. C'est la recette de la séance D2. La faire repérer ici.")

    d.dialogue('Dialogue · 3 de 3', "Dire ce qu'on ne sait pas", [
        ("MARISOL", "J'aimerais que vous sachiez aussi que j'ai travaillé avec un logiciel d'inventaire. Ce n'est pas celui que vous utilisez, mais la logique est la même.", True),
        ("ROBERT", "Le nôtre s'apprend en deux semaines. Ce qui ne s'apprend pas en deux semaines, c'est la rigueur.", True),
        ("MARISOL", "Par contre, il faut que je vous dise : si je n'ai pas compris, je fais répéter. Je préfère demander deux fois que me tromper une fois.", True),
        ("ROBERT", "Ça, c'est la bonne attitude.", True),
    ], notes="Marisol place elle-même une information qu'on ne lui a pas demandée, puis "
             "annonce sa limite comme une qualité. Les deux gestes se travaillent en D2.")

    d.tableau('Décodage', "Ce que la question cache",
              ['La question posée', 'Ce qu\'il veut savoir'],
              [["Parlez-moi de votre expérience.", "Savez-vous faire le travail ?"],
               ["Ici, ça parle fort et ça va vite.", "Tiendrez-vous le rythme ?"],
               ["Que savez-vous de notre entreprise ?", "Ce poste vous intéresse-t-il vraiment ?"],
               ["Avez-vous des questions pour moi ?", "Y avez-vous réfléchi avant de venir ?"]],
              cle=0,
              note="Répondre à la question posée ne suffit pas : c'est à l'inquiétude qu'il faut répondre.",
              notes="Diapositive à photographier. C'est la clé de lecture d'une entrevue, "
                    "et elle vaut pour tous les métiers.")

    d.regle("Vos questions à vous",
            "En poser au moins une, toujours.",
            precision="Sur l'horaire, l'équipe, la formation ou la suite du processus. "
                      "Ne pas en poser donne l'air de ne pas être intéressé — ou de "
                      "n'avoir rien préparé. Le salaire et les vacances, eux, viennent "
                      "plus tard, quand l'offre est faite.",
            notes="Diapositive à photographier. Faire préparer deux questions dès "
                  "maintenant : elles serviront au jeu de rôle de E1.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après le dialogue.", [
        ("Robert Chartier est le chef d'entrepôt.", "vrai"),
        ("Marisol répond en une seule phrase.", "faux — trois ou quatre, avec un exemple"),
        ("Elle raconte l'histoire des planches manquantes.", "vrai"),
        ("Elle cache qu'elle ne connaît pas leur logiciel.", "faux — elle le dit"),
        ("Pour Robert, la rigueur s'apprend en deux semaines.", "faux — le logiciel, oui ; la rigueur, non"),
        ("Marisol pose une question sur les horaires.", "vrai"),
    ], corrige=True,
       notes="Faire justifier chaque réponse par la réplique.")

    d.billet(
        "Préparez votre réponse à « Parlez-moi de votre expérience ».",
        exemples=[
            "Trois ou quatre phrases, avec un chiffre.",
            "Chronométrez-vous : entre quarante et soixante secondes.",
        ],
        notes="Le chronomètre est utile : les réponses trop courtes durent huit secondes, "
              "les trop longues dépassent deux minutes. Le milieu s'apprend en le mesurant.")

    return d.save(dossier)
