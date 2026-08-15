# -*- coding: utf-8 -*-
"""B5 · Expliquer une décision de chantier.
Bloc B · couleur teal (écoute et réponds) · 60 min.
Source : dialogue `prep` et exercice `t1expr` — production orale du défi 1.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B5', section='teal',
        titre='Expliquer une décision',
        chapeau="Annoncer qu'on annule, à quelqu'un qui n'est pas d'accord. C'est ce que "
                "Josée fait avec Diego — et c'est la situation la plus délicate du "
                "module.",
        duree='60 minutes')

    d.titre(notes="Séance de production orale. Rendre les billets de A1 et A4 : ils "
                  "contiennent des règles de sécurité et des décisions réelles.")

    d.objectifs([
        "annoncer une décision et la justifier par une règle ;",
        "répondre à quelqu'un qui n'est pas d'accord ;",
        "proposer une solution de rechange ;",
        "comprendre les expressions québécoises de la météo.",
    ])

    d.regle('La règle des quatre phrases',
            "La décision · la raison · la règle · la solution de rechange.",
            precision="« J'annule la journée. On annonce du verglas. Notre règle est "
                      "claire : personne ne monte au-dessus de quarante. On rentre "
                      "préparer le bardeau. » Quatre phrases, et il n'y a plus rien à "
                      "discuter.",
            notes="Écrire les quatre au tableau. C'est exactement ce que fait Josée, et "
                  "c'est le modèle des jeux de rôle.")

    d.cartes('Analyse', "Comment répondre à quelqu'un qui insiste", [
        ("Reconnaître son point",
         "« Je sais qu'on a du retard. » Nier le problème de l'autre ferme la "
         "conversation ; le reconnaître l'ouvre."),
        ("Revenir à la règle",
         "« Mais la règle est à quarante. » Pas à une opinion, pas à une préférence : à "
         "un chiffre écrit d'avance."),
        ("Donner la raison de la règle",
         "« Il y a deux ans, un couvreur s'est fracturé le poignet. » Un fait vaut "
         "mieux qu'un argument."),
        ("Refermer sur la solution",
         "« On rentre à l'atelier, il y a du bardeau à préparer. » La conversation se "
         "termine sur une action, pas sur un refus."),
    ], notes="Ces quatre gestes sont ceux de Josée. Les faire retrouver dans le dialogue "
             "de A1 avant de les pratiquer.")

    d.tableau('Analyse', "Trois expressions québécoises de la météo",
              ["L'expression", 'Ce qu\'elle veut dire'],
              [["il mouille à boire debout", "il pleut très fort"],
               ["il fait frette", "il fait très froid"],
               ["ça va poudrer", "il va y avoir de la poudrerie"]],
              cle=0,
              note="Ces expressions ne sont pas dans les bulletins officiels, mais elles "
                   "sont partout sur un chantier.",
              notes="En ajouter deux ou trois apportées par le groupe. Les élèves qui "
                    "travaillent en connaissent souvent d'autres.")

    d.pratique('Pratique · 1 de 4', "Que veut dire l'expression ?",
               "Français courant du Québec.", [
        ("« Il mouille à boire debout. »", "il pleut très fort"),
        ("« Il fait frette à matin. »", "il fait très froid ce matin"),
        ("« Ça va poudrer sur la 10. »", "il va y avoir de la poudrerie sur l'autoroute 10"),
        ("« Le vent est tombé. »", "le vent a diminué"),
    ], corrige=True,
       notes="La quatrième est celle du bulletin, vue en B1. Le faire remarquer : c'est "
             "la même expression, dans deux registres.")

    d.pratique('Pratique · 2 de 4', "Annoncez la décision",
               "Quatre phrases : décision, raison, règle, solution.", [
        ("Rafales à 60 km/h annoncées demain.",
         "J'annule la journée sur le toit. Des rafales à 60 sont annoncées. Notre règle "
         "est à 40. On rentre préparer le matériel."),
        ("Pluie verglaçante en cours ce matin.",
         "On ne monte pas ce matin. Il tombe de la pluie verglaçante. La membrane sera "
         "glacée. On commence par l'atelier."),
        ("Poudrerie sur la route du chantier.",
         "On part plus tard. Il y a un avertissement de poudrerie. La visibilité tombe "
         "sous 200 mètres. On attend que le vent faiblisse."),
    ], corrige=True,
       notes="Faire dire les quatre phrases d'un seul trait, debout. Chronométrer : "
             "vingt secondes suffisent.")

    d.piege("Le piège de la décision sans raison",
            "On ne monte pas aujourd'hui. C'est comme ça.",
            "On ne monte pas : les rafales dépassent quarante.",
            "Une décision sans raison paraît arbitraire et se discute. Une décision "
            "justifiée par un chiffre ne se discute pas — et celui qui la reçoit peut "
            "l'expliquer à son tour aux autres.",
            notes="Faire l'expérience : donner les deux versions au groupe et demander "
                  "laquelle on accepterait le mieux.")

    d.piege("Le piège de l'annulation sans solution",
            "On ne travaille pas aujourd'hui.",
            "On ne monte pas, mais on rentre préparer le bardeau.",
            "Annuler sans proposer autre chose, c'est annoncer une journée perdue — pour "
            "l'entreprise et pour la paie de chacun. La solution de rechange transforme "
            "une annulation en changement de programme.",
            notes="Point concret : une journée à l'atelier est une journée payée. C'est "
                  "ce qui rend la quatrième phrase importante.")

    d.pratique('Pratique · 3 de 4', "Jeu de rôle · le collègue qui insiste",
               "À deux. L'un annonce l'annulation, l'autre insiste. Puis on échange.", [
        ("Vous annoncez", "la décision, la raison, la règle, la solution"),
        ("Le collègue insiste", "« Mais on a du retard », « j'ai des crampons »"),
        ("Vous reconnaissez son point", "« Je sais qu'on a du retard, mais… »"),
        ("Vous revenez à la règle", "avec le chiffre, pas avec une opinion"),
        ("Vous refermez", "sur la solution de rechange"),
    ], corrige=False,
       notes="Vingt minutes. Circuler et vérifier une seule chose : est-ce que la règle "
             "chiffrée est citée ? C'est le critère de la séance.")

    d.pratique('Pratique · 4 de 4', "Votre propre décision",
               "Reprenez la règle de sécurité de votre billet de A1.", [
        ("La condition", "quel chiffre, quelle situation ?"),
        ("La décision", "qu'est-ce qu'on ne fait pas ?"),
        ("La règle", "d'où vient-elle, et pourquoi ?"),
        ("La solution", "qu'est-ce qu'on fait à la place ?"),
    ], corrige=False,
       notes="Dix minutes. Les règles apportées par le groupe sont plus variées que "
             "celles du chantier : entretien ménager, cuisine, transport, garderie.")

    d.billet(
        "Écrivez les quatre phrases d'une annulation, pour votre propre travail.",
        exemples=[
            "La décision, la raison, la règle, la solution.",
            "Si vous ne travaillez pas, choisissez une sortie annulée à cause de la météo.",
        ],
        notes="Ramasser. Ces quatre phrases seront reprises à l'écrit en E1, dans un "
              "message à l'équipe.")

    return d.save(dossier)
