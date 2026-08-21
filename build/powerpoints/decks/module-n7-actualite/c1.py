# -*- coding: utf-8 -*-
"""C1 · Huit minutes avec la conseillère
Bloc C « Défi 2 · L'article » · couleur acier · 75 min.
Source : extrait `t2` (l'entrevue), exercice `t2vf`.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n7-actualite/images/')


def build(dossier):
    d = Deck(
        code='C1', section='acier',
        titre="Huit minutes avec la conseillère",
        chapeau="Une entrevue n'est pas un reportage : c'est une personne "
                "qu'on fait parler longuement, et qu'on relance quand elle "
                "esquive. L'extrait d'aujourd'hui est le plus long du module.",
        duree='75 minutes')

    d.titre(notes="Ouverture du Défi 2. Prévenir : vingt-deux répliques, dont plusieurs "
                  "de quatre phrases. On ne l'écoutera pas d'un seul tenant — on le "
                  "coupe en trois, comme le reportage.")

    d.objectifs([
        "suivre une entrevue longue et en retenir la structure ;",
        "repérer comment un journaliste relance quelqu'un ;",
        "distinguer « recommandé » de « décidé » ;",
        "comprendre qui décide quoi dans une municipalité.",
    ], notes="Le quatrième objectif dépasse la langue et c'est assumé : savoir qu'une "
             "recommandation n'est pas une décision est utile à tout adulte qui habite "
             "une ville.")

    d.declencheur(
        'Observation', "Qu'est-ce qui se passe dans un studio, à deux ?",
        image=IMG + 'studio-radio.jpg',
        pistes=[
            "Qui pose les questions, qui répond ?",
            "L'invitée a-t-elle vu les questions d'avance ?",
            "Que fait le journaliste si la réponse est vague ?",
            "Peut-il dire ce qu'il pense de la réponse ?",
        ],
        notes="La troisième piste est le coeur de la séance : la relance. Les élèves "
              "sous-estiment souvent qu'on a le droit de redemander.")

    d.dialogue('Entrevue · 1 de 3', "Ce qui a changé depuis hier", [
        ("LUDOVIC", "Madame Ferron, bonjour. Hier, notre reportage disait que le local de la rue Boisjoli était à l'étude. Ce matin, un communiqué est sorti. Qu'est-ce qui a changé ?", True),
        ("HÉLÈNE", "Ce qui a changé, c'est que le dossier a été déposé officiellement. Le communiqué a été publié hier soir par le service des communications.", True),
        ("LUDOVIC", "Donc l'emplacement a été choisi ?", True),
        ("HÉLÈNE", "L'emplacement recommandé, oui. Mais je veux être précise : recommandé n'est pas décidé. La décision finale sera prise par le conseil municipal, en séance publique, le 14 octobre.", True),
    ], consigne="Écoutez d'abord, diapositive masquée.",
       notes="« Recommandé n'est pas décidé » est la phrase à retenir de la séance. "
             "L'écrire au tableau. Elle contient aussi trois phrases passives, qui "
             "seront le sujet de C2.")

    d.dialogue('Entrevue · 2 de 3', "La relance : vous m'aviez dit autre chose", [
        ("LUDOVIC", "Vous m'aviez dit la semaine dernière que rien n'était fait.", True),
        ("HÉLÈNE", "Et c'était exact la semaine dernière. Je vous avais dit que le comité n'avait pas encore reçu l'analyse technique, et c'était vrai : il l'a reçue lundi.", True),
        ("HÉLÈNE", "Je vous avais dit aussi que je vous rappellerais dès qu'il y aurait du nouveau, et c'est ce que j'ai fait.", True),
        ("LUDOVIC", "Parlons du stationnement. Le dépanneur d'en face craint de perdre ses huit places.", True),
    ], notes="Ces quatre répliques sont bourrées de discours indirect au passé : "
             "« vous m'aviez dit que », « je vous avais dit que je vous rappellerais ». "
             "Ne pas l'expliquer aujourd'hui - c'est C3. Seulement le faire remarquer.")

    d.dialogue('Entrevue · 3 de 3', "Qui exploite, et qui peut poser une question", [
        ("LUDOVIC", "Ce n'est donc pas la Ville qui va l'opérer ?", True),
        ("HÉLÈNE", "Non, et c'est important de le dire parce que beaucoup de gens se trompent là-dessus. La Ville met le local à disposition. L'exploitation relève du système de consigne, pas de la municipalité.", True),
        ("LUDOVIC", "Un citoyen qui n'est pas d'accord, il fait quoi ?", True),
        ("HÉLÈNE", "Il vient au conseil le 14 octobre. Toute séance du conseil comprend une période de questions où les personnes présentes peuvent interroger les élus. C'est prévu par la loi.", True),
    ], notes="La dernière réplique est vraie et vérifiable : au Québec, toute séance du "
             "conseil d'une municipalité comprend une période de questions du public, et "
             "le conseil en fixe la durée et la procédure par règlement. Le dire au "
             "groupe : c'est un droit qu'ils ont.")

    d.regle("Recommandé n'est pas décidé",
            "Un comité recommande ; un conseil décide, en séance publique.",
            precision="La distinction n'est pas un détail administratif : elle dit à "
                      "quel moment un citoyen peut encore intervenir. Tant que ce n'est "
                      "que recommandé, la période de questions du conseil sert à quelque "
                      "chose. C'est aussi ce que la chronique du Défi 3 va confondre, "
                      "volontairement.",
            notes="Diapositive à photographier. Elle prépare directement D1.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après l'entrevue.", [
        ("Le communiqué a été publié avant l'accord du comité exécutif.", "faux - après"),
        ("Le local de la rue Boisjoli fait cent quarante mètres carrés.", "vrai"),
        ("Le local de la rue Marquette est plus grand.", "faux - quatre-vingts mètres carrés"),
        ("Deux des huit places seraient réservées, quinze minutes.", "vrai"),
        ("C'est la Ville qui exploitera le point de dépôt.", "faux - le système de consigne"),
        ("Le dépôt serait ouvert du mardi au dimanche.", "vrai"),
        ("Les heures précises sont déjà fixées.", "faux - négociées plus tard"),
    ], corrige=True,
       notes="Faire justifier par la réplique. La cinquième affirmation est celle que "
             "le voisin sceptique du jeu de rôle défendra en E1.")

    d.billet(
        "En une phrase : quelle est la différence entre recommandé et décidé ?",
        exemples=[
            "Dites-le avec vos mots, pas avec ceux de la conseillère.",
            "Ajoutez : à votre avis, pourquoi est-ce que ça compte ?",
        ],
        notes="Deux minutes. Les réponses au « pourquoi ça compte » montrent quels "
              "élèves ont saisi l'enjeu civique, pas seulement le vocabulaire.")

    return d.save(dossier)
