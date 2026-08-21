# -*- coding: utf-8 -*-
"""C2 · Intervenir sans couper la parole.
Bloc C « Défi 2 » · couleur teal · 75 min.
Source : exercices `t2inter` et `t2conn`, et la mini-leçon des connecteurs.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C2', section='teal',
        titre="Intervenir sans couper la parole",
        chapeau="Un connecteur ne décore pas la phrase : il annonce ce qui "
                "vient. « Cependant » prévient votre interlocuteur qu'une "
                "objection arrive — et vous donne le temps de la formuler.",
        duree='75 minutes')

    d.titre(notes="Séance de prise de parole. Beaucoup d'oral. Prévoir de faire jouer "
                  "la réunion en petits groupes dans la seconde moitié.")

    d.objectifs([
        "employer sept formules d'intervention selon l'intention ;",
        "distinguer l'opposition qui admet de celle qui met en balance ;",
        "choisir le mode après un connecteur de condition ;",
        "reformuler pour garder la parole quand la phrase part de travers.",
    ], notes="L'objectif 4 est le plus utile en situation réelle et le moins enseigné.")

    d.cartes("Sept façons d'intervenir", "L'intention d'abord, la formule ensuite", [
        ("Reformuler pour vérifier",
         "Si je résume ce que vous venez de dire…"),
        ("Appuyer sur une source",
         "C'est écrit à la page quatre ; j'ai vérifié deux fois."),
        ("Objecter sans contredire de front",
         "Cependant, il y a une donnée qui n'est pas dans la soumission."),
        ("Reconnaître avant de nuancer",
         "Tout à fait, et je ne dis pas qu'il faut refuser."),
        ("Avancer une solution sans l'imposer",
         "Je proposerais un partage."),
        ("Nommer son propre intérêt",
         "C'est moi qui écoperais de ce travail, alors je le dis en connaissance de cause."),
        ("Reconnaître ce qui a manqué",
         "On aurait dû demander leurs délais avant de comparer les prix."),
    ], cols=1,
       notes="Diapositive à photographier. Faire choisir à chacun les deux formules "
             "qu'il emploiera vraiment : sept d'un coup, personne ne les retient.")

    d.tableau('Analyse · 1 de 2', "L'opposition et la conséquence",
              ['Ce que ça fait', 'Les connecteurs'],
              [["J'admets, puis j'objecte", "cependant · toutefois · néanmoins"],
               ["Je mets deux choses en balance", "en revanche · par contre"],
               ["Ce qui suit découle de ce qui précède", "par conséquent · donc · c'est pourquoi"]],
              cle=0,
              note="« Par contre » est correct au Québec ; « en revanche » passe mieux dans une lettre.",
              notes="Diapositive à photographier. Faire produire une phrase par ligne, "
                    "sur le dossier des deux fournisseurs.")

    d.tableau('Analyse · 2 de 2', "L'explication et la condition",
              ['Ce que ça fait', 'Les connecteurs'],
              [["Je confirme et j'explique", "en effet · car · en raison de"],
               ["Je pose une condition (indicatif)", "du moment que · dès lors que · puisque"],
               ["Je pose une condition (subjonctif)", "à condition que · pourvu que · à moins que"]],
              cle=0,
              note="« En effet » confirme ; « en fait » corrige. Ce ne sont pas des variantes.",
              notes="La confusion « en effet / en fait » inverse le sens de la phrase. "
                    "C'est l'erreur la plus fréquente à ce niveau.")

    d.regle("Reformuler pour garder la parole",
            "Autrement dit…",
            precision="Quand vous sentez que votre phrase est partie de travers, "
                      "n'arrêtez pas et ne vous excusez pas : enchaînez « autrement "
                      "dit » et redites la même chose plus simplement. Personne n'y "
                      "verra une hésitation ; tout le monde y verra un souci de clarté. "
                      "Même service avec « ce que je veux dire, c'est que ».",
            notes="Diapositive à photographier. C'est la stratégie de survie la plus "
                  "utile d'une réunion en langue seconde.")

    d.piege("Confondre en effet et en fait",
            "Le portrait change. En fait, le délai passe à dix jours.",
            "Le portrait change. En effet, le délai passe à dix jours.",
            "« En effet » confirme ce qu'on vient de dire et l'explique. « En fait » "
            "corrige ce que l'autre croyait. Employer le second à la place du premier "
            "revient à contredire son propre propos, et l'interlocuteur cherche "
            "l'erreur qu'on vient de lui signaler — sans la trouver.",
            notes="Faire produire deux phrases par élève, une avec chaque connecteur.")

    d.pratique('Grammaire', "Le connecteur juste",
               "Complétez la phrase.", [
        ("L'écart de prix est réel. ___, le délai est de dix jours.", "Cependant / Toutefois"),
        ("Ferrico livre en quatre jours ; ___, Lachance en demande dix.", "en revanche / par contre"),
        ("Il faudrait doubler le stock ; ___, l'économie tombe à vingt mille.", "par conséquent / donc"),
        ("Ça change le portrait. ___, tout le calcul reposait sur le prix.", "En effet"),
        ("J'accepte, ___ Ferrico n'impose rien avant octobre.", "du moment que"),
        ("Nous tranchons le seize, ___ vous ayez les deux chiffres.", "à condition que"),
        ("___, je ne viens pas demander une faveur.", "Autrement dit"),
    ], corrige=True,
       notes="Attention aux deux dernières : l'une demande l'indicatif, l'autre le "
             "subjonctif. Le faire remarquer plutôt que de le corriger.")

    d.pratique('Production', "Prenez la parole",
               "En équipes de trois, rejouez le point trois de l'ordre du jour.", [
        ("L'un défend le changement de fournisseur (le prix).", ""),
        ("L'un apporte la donnée du délai et propose un compromis.", ""),
        ("L'un dirige la réunion et tranche ou reporte.", ""),
        ("Chacun doit employer au moins trois des sept formules.", ""),
    ], notes="Vingt minutes. Circuler et noter les formules réellement employées, pour "
             "les projeter à la fin sans nommer d'auteur.")

    d.billet(
        "Choisissez deux formules d'intervention et écrivez-les sur une fiche.",
        exemples=[
            "Une pour objecter, une pour proposer.",
            "Gardez la fiche : elle sert à la production orale de E1.",
        ],
        notes="Deux formules bien tenues valent mieux que sept mal retenues.")

    return d.save(dossier)
