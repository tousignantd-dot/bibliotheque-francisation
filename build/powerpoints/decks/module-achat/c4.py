# -*- coding: utf-8 -*-
"""C4 · La veille de la livraison.
Bloc C · couleur acier · 55 min.
Source : dialogue `t2b`, exercice `t2b`.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-achat/images/')


def build(dossier):
    d = Deck(
        code='C4', section='acier',
        titre='La veille de la livraison',
        chapeau="Le téléphone sonne : « je vous confirme entre huit heures et "
                "midi ». Cinq minutes de conversation qui décident si "
                "l'appareil entrera ou repartira.",
        duree='55 minutes')

    d.titre(notes="Séance courte et très pratique. Elle clôt le bloc C.")

    d.objectifs([
        "comprendre un appel de confirmation de livraison ;",
        "savoir qui doit être présent et pourquoi ;",
        "préparer le passage avant l'arrivée du camion ;",
        "vérifier ce qui est prévu et ce qui ne l'est pas.",
    ])

    d.declencheur(
        'Mise en situation', "Le camion arrive demain matin. Qu'avez-vous à préparer ?",
        image=IMG + 'camion-livraison.jpg',
        pistes=[
            "Qui doit être à la maison ?",
            "Qu'est-ce qu'il faut dégager ?",
            "Que se passe-t-il si l'appareil n'entre pas ?",
            "L'ancien appareil, qui s'en occupe ?",
        ],
        notes="Cinq minutes. La troisième piste est celle qui coûte : le camion repart, la "
              "livraison reste facturée, et il faut tout recommencer.")

    d.dialogue('Dialogue · 1 de 2', "La confirmation", [
        ("PATRICK", "Bonjour, c'est pour la livraison de demain. Je vous confirme entre huit heures et midi.", True),
        ("YIN", "Parfait. Est-ce que quelqu'un doit être là ?", True),
        ("PATRICK", "Oui, une personne majeure. On ne laisse pas l'appareil sans signature.", True),
        ("YIN", "Il faut préparer quelque chose ?", True),
    ], consigne="Écoutez d'abord, diapo masquée.",
       notes="« Entre huit heures et midi » est un créneau de quatre heures, pas un "
             "rendez-vous. Le dire : il faut prévoir la demi-journée.")

    d.dialogue('Dialogue · 2 de 2', "Ce qu'il faut vérifier", [
        ("PATRICK", "Dégagez le passage et mesurez la porte du sous-sol. Si elle fait moins de soixante-dix centimètres, appelez-nous avant.", True),
        ("YIN", "Elle fait soixante-quinze. Ça va.", False),
        ("PATRICK", "Bien. On monte l'appareil et on repart avec l'emballage. L'installation, c'est un autre technicien.", True),
        ("YIN", "Et l'ancienne laveuse, vous la reprenez ?", True),
    ], notes="Le livreur redit la distinction livraison / installation. La cohérence entre "
             "les séances est voulue : la même information trois fois.")

    d.tableau('Analyse', "Cinq choses à préparer",
              ['À faire', 'Pourquoi'],
              [["Être là, majeur", "il faut une signature"],
               ["Dégager le passage", "corridor, escalier, entrée"],
               ["Mesurer la porte", "sous les 70 cm, il faut prévenir"],
               ["Sortir le livret de la boîte", "les livreurs repartent avec l'emballage"],
               ["Vérifier le bon de livraison", "la reprise doit y être notée"]],
              cle=2,
              note="La quatrième est celle que personne ne fait — et le livret part à la poubelle.",
              notes="Diapo à photographier. Les cinq points tiennent en dix minutes de "
                    "préparation.")

    d.regle("Le créneau n'est pas un rendez-vous",
            "« Entre huit heures et midi » veut dire quatre heures d'attente possible.",
            precision="Les équipes de livraison enchaînent plusieurs adresses et ne peuvent "
                      "pas donner d'heure précise. Prévoyez la demi-journée, ou demandez si "
                      "un appel est fait trente minutes avant — beaucoup d'entreprises le "
                      "font sur demande.",
            notes="Conseil pratique utile : la question « pouvez-vous m'appeler avant "
                  "d'arriver ? » obtient souvent oui.")

    d.piege("Laisser partir l'emballage avec le livret",
            "Ils ont tout emporté, y compris le mode d'emploi.",
            "Je sors le livret de la boîte avant qu'ils repartent.",
            "Le mode d'emploi est dans la boîte, ou collé sur l'appareil. Les livreurs "
            "repartent avec le carton — et le livret avec. Or c'est lui qui contient le "
            "tableau des problèmes, qui vaut quatre-vingt-dix dollars par appel évité.",
            notes="Annoncer le bloc D : c'est exactement ce dont il sera question.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après le dialogue.", [
        ("Personne n'a besoin d'être présent.", "faux — une personne majeure"),
        ("Il faut mesurer la porte du sous-sol.", "vrai"),
        ("Sous soixante-dix centimètres, il faut appeler avant.", "vrai"),
        ("Les livreurs installent l'appareil.", "faux — c'est un autre technicien"),
        ("Le technicien de l'installation vient le matin.", "faux — l'après-midi"),
        ("La reprise de l'ancienne laveuse est automatique.", "faux — elle doit être notée"),
    ], corrige=True,
       notes="Faire justifier chaque « faux » par la réplique exacte.")

    d.cartes("Si l'appareil n'entre pas", "Ce qui se passe", [
        ("Le camion repart avec",
         "Les livreurs n'ont ni le temps ni le mandat de démonter une porte."),
        ("La livraison reste facturée",
         "Le déplacement a eu lieu. Une deuxième livraison se paie une deuxième fois."),
        ("Comment l'éviter",
         "Mesurer le passage avant l'achat, et prévenir le magasin si un accès est "
         "étroit. Certaines entreprises envoient alors une équipe de deux."),
    ], notes="La troisième carte donne la solution. La mesure du passage revient de A3 : "
             "c'est le même conseil, à un autre moment.")

    d.billet(
        "Préparez la livraison d'un appareil chez vous, en cinq lignes.",
        exemples=[
            "Qui sera là, ce qu'il faut dégager, les mesures du passage.",
            "Notez la question que vous poserez à l'appel de confirmation.",
        ],
        notes="Bilan du bloc C. Ce billet est très concret et se retient.")

    return d.save(dossier)
