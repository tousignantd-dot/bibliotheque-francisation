# -*- coding: utf-8 -*-
"""A1 · Monte-t-on sur le toit demain ? — mise en situation.
Bloc A « Je découvre » · couleur teal · 75 min.
Source du module : dialogue `prep`, exercices `pr1` et `prVF`, cartes mémoire.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A1', section='teal',
        titre='Monte-t-on sur le toit demain ?',
        chapeau="Josée, contremaîtresse d'une équipe de couvreurs, annule la journée à "
                "cause du verglas annoncé. Diego voudrait quand même monter : le "
                "chantier a trois jours de retard.",
        duree='75 minutes')

    d.titre(notes="Ouverture du module 6. Écrire au tableau : QUARANTE KILOMÈTRES À "
                  "L'HEURE. C'est le chiffre qui décide, et c'est le sujet du module : "
                  "une règle chiffrée vaut mieux qu'une impression.")

    d.objectifs([
        "comprendre une décision prise à cause de la météo ;",
        "nommer les conditions qui rendent un travail dangereux ;",
        "reconnaître une règle de sécurité chiffrée ;",
        "savoir quoi proposer quand une journée est annulée.",
    ])

    d.declencheur(
        'Mise en situation', "Il est annoncé du verglas. Faut-il aller travailler dehors ?",
        pistes=[
            "Qui décide : l'employeur, l'employé, ou les deux ?",
            "Qu'est-ce qui rend un toit dangereux, exactement ?",
            "Est-ce qu'on peut refuser de monter ?",
            "Qu'est-ce qu'on fait de la journée si on n'y va pas ?",
        ],
        notes="Cinq minutes en grand groupe. La troisième question est importante : au "
              "Québec, un travailleur a le droit de refuser un travail dangereux. Le "
              "dire, sans développer — on y revient en B5.")

    d.cartes('La situation', "Ce qu'on sait de l'équipe", [
        ("Qui décide",
         "Josée, la contremaîtresse. C'est elle qui annule, et elle explique pourquoi."),
        ("Ce qui est annoncé",
         "Du verglas avant six heures. La membrane du toit sera glacée."),
        ("La règle de l'équipe",
         "Personne ne monte si les rafales dépassent quarante kilomètres à l'heure ou "
         "si la membrane est glacée. Une règle chiffrée, écrite d'avance."),
        ("Pourquoi cette règle existe",
         "Voilà deux ans, un couvreur s'est fracturé le poignet sur une pente gelée. "
         "La règle vient d'un accident réel."),
    ], notes="La quatrième carte est la plus importante : une règle de sécurité n'est "
             "presque jamais arbitraire. Elle a une histoire.")

    d.dialogue('Dialogue · 1 de 3', "J'annule la journée de demain", [
        ("JOSÉE", "Diego, j'annule la journée de demain sur le toit de l'école. On "
                  "annonce du verglas avant six heures.", True),
        ("DIEGO", "Du verglas ? Mais on a déjà trois jours de retard sur le chantier…",
         True),
        ("JOSÉE", "Notre règle est claire : personne ne monte si les rafales dépassent "
                  "quarante kilomètres à l'heure ou si la membrane est glacée.", True),
    ], consigne="Écoutez d'abord l'enregistrement, diapo masquée. Lisez ensuite.",
       notes="Passer l'audio de « Je découvre ». Faire remarquer que Josée ne discute "
             "pas : elle cite la règle. C'est ce qui met fin à la négociation.")

    d.dialogue('Dialogue · 2 de 3', "J'ai des crampons dans mon coffre", [
        ("DIEGO", "J'ai des crampons dans mon coffre. Je pourrais essayer, au moins sur "
                  "la pente sud.", True),
        ("JOSÉE", "Non. Voilà deux ans, un couvreur de l'équipe s'est fracturé le "
                  "poignet sur une pente gelée. Je ne recommencerai pas ça.", True),
    ], notes="Diego propose une solution partielle : c'est une réaction très humaine. "
             "Josée répond par un fait, pas par une opinion.")

    d.dialogue('Dialogue · 3 de 3', "Qu'est-ce qu'on fait, alors ?", [
        ("DIEGO", "D'accord. Qu'est-ce qu'on fait, alors ?", True),
        ("JOSÉE", "On rentre à l'atelier : il y a du bardeau à préparer pendant toute la "
                  "matinée. Si la pluie verglaçante cesse en après-midi, on remonte.",
         True),
        ("DIEGO", "Je préviens Prisca ? Elle part de Longueuil vers cinq heures, "
                  "d'habitude.", True),
    ], notes="Deux choses à relever : l'atelier remplace le toit, et Diego pense à "
             "prévenir la collègue qui part de loin. C'est le réflexe du module 3.")

    d.regle('La règle du module',
            "Une règle de sécurité se dit en chiffres, pas en impressions.",
            precision="« Il vente trop » se discute. « Les rafales dépassent quarante "
                      "kilomètres à l'heure » ne se discute pas. Le chiffre protège "
                      "celui qui décide comme celui qui exécute.",
            notes="Écrire la règle au tableau et l'y laisser tout le module. C'est elle "
                  "qui explique pourquoi on apprend à lire un bulletin météo.")

    d.tableau('Analyse', "Ce que Josée fait, en quatre gestes",
              ['Le geste', 'Sa phrase'],
              [["elle annonce la décision", "J'annule la journée de demain."],
               ["elle donne la raison", "On annonce du verglas avant six heures."],
               ["elle cite la règle", "Personne ne monte si les rafales dépassent 40 km/h."],
               ["elle propose autre chose", "On rentre à l'atelier préparer du bardeau."]],
              cle=0, props=[0.32, 0.68],
              notes="Quatre gestes, dans cet ordre. C'est ce qu'on attend d'une personne "
                    "qui annule un travail — au chantier comme ailleurs.")

    d.vocabulaire('Vocabulaire · 1 de 2', "Le mauvais temps", [
        ("la pluie verglaçante", "Une pluie qui gèle dès qu'elle touche une surface."),
        ("la poudrerie", "De la neige déjà tombée que le vent soulève."),
        ("le grésil", "De petits grains de glace qui tombent du ciel."),
        ("une rafale", "Une hausse brusque du vent, qui dure quelques secondes."),
        ("le facteur éolien", "L'effet du vent, qui fait ressentir un froid plus intense."),
        ("un redoux", "Un réchauffement court au milieu de l'hiver."),
    ], notes="Ces six mots n'existent dans aucune méthode de français général : ils sont "
             "propres à l'hiver québécois. Prendre le temps de les faire prononcer.")

    d.vocabulaire('Vocabulaire · 2 de 2', "La route et le bulletin", [
        ("la chaussée", "La partie de la route où roulent les véhicules."),
        ("la visibilité", "La distance à laquelle on distingue ce qui nous entoure."),
        ("un avertissement", "Un message officiel qui signale un danger à venir."),
        ("le mercure", "Une autre façon de nommer la température."),
        ("une éclaircie", "Un moment où les nuages s'ouvrent et laissent passer le soleil."),
        ("un chasse-neige", "Un camion qui pousse la neige hors de la route."),
    ], notes="« Le mercure » revient dans tous les bulletins. Le signaler : ce n'est pas "
             "le métal, c'est la température.")

    d.pratique('Pratique · 1 de 2', "Vrai ou faux",
               "Répondez sans relire le dialogue.", [
        ("L'équipe travaillera sur le toit de l'école demain matin.", "FAUX — c'est annulé"),
        ("Le chantier a du retard.", "VRAI — trois jours"),
        ("Diego a des crampons dans son coffre.", "VRAI"),
        ("Josée accepte que Diego monte avec ses crampons.", "FAUX"),
        ("Un couvreur de l'équipe s'est déjà blessé sur une pente gelée.", "VRAI"),
        ("L'équipe ne travaillera pas du tout demain.", "FAUX — à l'atelier"),
    ], corrige=True,
       notes="Le dernier énoncé est le piège : annuler le toit ne veut pas dire annuler "
             "la journée. C'est une distinction utile au travail.")

    d.pratique('Pratique · 2 de 2', "Quatre questions",
               "Répondez par une phrase complète.", [
        ("Pourquoi Josée annule-t-elle la journée ?",
         "Parce qu'on annonce du verglas avant six heures."),
        ("Quelle est la règle de l'équipe ?",
         "Personne ne monte si les rafales dépassent 40 km/h ou si la membrane est glacée."),
        ("Que fera l'équipe pendant la matinée ?", "Elle préparera du bardeau à l'atelier."),
        ("À quelle condition pourrait-elle remonter ?",
         "Si la pluie verglaçante cesse en après-midi."),
    ], corrige=True,
       notes="La dernière réponse contient un « si » : c'est la condition, sujet de la "
             "séance C4. La signaler sans l'expliquer.")

    d.piege("Le piège du « je peux quand même »",
            "J'ai des crampons, je peux essayer.",
            "La règle ne dépend pas de l'équipement de chacun.",
            "Une règle de sécurité vaut pour tout le monde, quel que soit l'équipement "
            "ou l'expérience. Faire une exception pour une personne, c'est la faire pour "
            "toutes — et c'est ainsi que les accidents arrivent.",
            notes="Discussion utile avec un groupe d'adultes qui travaillent. Beaucoup "
                  "ont déjà été dans la position de Diego.")

    d.billet(
        "Nommez une règle de sécurité de votre travail, avec son chiffre s'il y en a un.",
        exemples=[
            "Une règle, en une phrase.",
            "Si vous ne travaillez pas, nommez une règle de la vie quotidienne : la "
            "vitesse, la température d'un réfrigérateur, un délai.",
        ],
        notes="Ramasser. Les règles apportées par le groupe serviront en B5, où l'on "
              "expliquera une décision prise à cause de la météo.")

    return d.save(dossier)
