# -*- coding: utf-8 -*-
"""D2 · Raconter la journée, répondre à l'invitation.
Bloc D « Défi 3 · Les voisins » · couleur ambre · 75 min.
Source : exercice `t3passe`, dialogue `t3b`, exercices `t3bvf` et `t3invit`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='D2', section='ambre',
        titre="Raconter la journée, répondre à l'invitation",
        chapeau="Un récit sans imparfait est une liste ; un récit sans passé "
                "composé ne bouge pas.",
        duree='75 minutes')

    d.titre(notes="Séance double : la grammaire du récit d'abord, puis l'acte de parole "
                  "qui ferme le module. Les deux se tiennent : on raconte, puis on est "
                  "invité.")

    d.objectifs([
        "employer le passé composé pour ce qui avance ;",
        "employer l'imparfait pour ce qui dure autour ;",
        "accorder le participe avec « être » ;",
        "accepter ou refuser une invitation avec une raison.",
    ])

    d.tableau('Deux temps, deux rôles', "Ce n'est pas deux façons de dire la même chose",
              ['Le temps', 'Son rôle', 'Exemple'],
              [["passé composé", "ce qui arrive, une fois — ça avance",
                "Le camion est arrivé à neuf heures."],
               ["imparfait", "ce qui durait autour — le décor",
                "Il pleuvait depuis le matin."],
               ["imparfait", "l'habitude d'autrefois",
                "Avant, on déménageait avec les amis."],
               ["les deux ensemble", "ce qui durait, coupé par ce qui arrive",
                "Je portais la boîte quand elle est sortie."]],
              cle=0,
              note="Si vous pouvez demander « et ensuite ? », c'est du passé composé.",
              notes="Diapositive à photographier. Le test « et ensuite ? » est le plus "
                    "rapide, et il fonctionne presque toujours.")

    d.regle("Une quinzaine de verbes prennent « être »",
            "aller · venir · arriver · partir · monter · descendre · entrer · sortir · rester · tomber",
            precision="Avec « être », le participe s'accorde avec le sujet : elle est "
                      "descendue, ils sont montés. Avec « avoir », pas d'accord dans ces "
                      "phrases.",
            notes="Ne pas donner la liste complète : ces dix-là couvrent tout ce dont les "
                  "élèves ont besoin dans ce module.")

    d.piege("Monter et descendre avec le mauvais auxiliaire",
            "Ils sont montés le divan.",
            "Ils ont monté le divan.",
            "Avec un complément direct, ces deux verbes prennent « avoir » : ils ont monté "
            "le divan, elle a descendu les boîtes. Sans complément, ils prennent "
            "« être » : ils sont montés au deuxième, elle est descendue au sous-sol.",
            notes="C'est le piège propre à ce module : on passe la journée à monter des "
                  "choses. Faire produire les deux formes en alternance.")

    d.pratique('Conjugaison', "Passé composé ou imparfait ?",
               "L'enseignante lit la phrase ; le groupe donne le verbe au bon temps.", [
        ("Le camion ___ (arriver) avec deux heures de retard.", "est arrivé"),
        ("Quand ils ont commencé, il ___ (pleuvoir) depuis le matin.", "pleuvait"),
        ("Mon garçon ___ (dormir) dans l'auto.", "dormait"),
        ("Les hommes ___ (monter) le divan en dix minutes.", "ont monté — complément direct"),
        ("Nous ___ (finir) à neuf heures et demie.", "avons fini"),
        ("Je ___ (porter) la dernière boîte quand la voisine est sortie.", "portais"),
        ("En 1998, son mari ___ (échapper) la laveuse.", "a échappé"),
        ("La laveuse ___ (descendre) toute seule jusqu'en bas.", "est descendue — accord"),
    ], corrige=True,
       notes="Ce sont les items de l'exercice t3passe. Les deux dernières lignes opposent "
             "les deux auxiliaires sur des verbes voisins.")

    d.dialogue('Dialogue', "Un café dimanche", [
        ("THÉRÈSE", "Je fais du café dimanche après-midi, avec la voisine du 1. "
                    "Vous viendriez ?", True),
        ("AMADOU", "C'est gentil de me le proposer. Dimanche après-midi, par "
                   "exemple, je travaille : je suis à l'hôpital jusqu'à sept "
                   "heures.", True),
        ("AMADOU", "Une fin de semaine sur deux. Mais dimanche prochain, je suis "
                   "libre, et là, j'accepterais avec plaisir.", True),
        ("THÉRÈSE", "Parfait, on dit dimanche prochain. Deux heures ? Vous amènerez "
                    "votre garçon si vous voulez.", True),
    ], consigne="Écoutez, puis repérez les trois morceaux de la réponse d'Amadou.",
       notes="Les trois morceaux : remercier, refuser avec une raison, proposer une autre "
             "date. Les faire nommer par le groupe avant de les donner.")

    d.regle("Un refus sans raison n'est pas un refus de l'invitation",
            "C'est perçu comme un refus de la personne.",
            precision="Trois morceaux suffisent : « C'est gentil » · « malheureusement, je "
                      "travaille » · « par contre, dimanche prochain, je serais libre ». "
                      "Trente secondes, et la porte reste ouverte.",
            notes="Diapositive à photographier. C'est la règle culturelle la plus utile du "
                  "module, et elle sert bien au-delà du voisinage.")

    d.cartes("Les mots qui relient", "Trois connecteurs suffisent", [
        ("parce que", "donne la cause : parce que je travaille ce dimanche-là"),
        ("par contre", "oppose, et ouvre l'autre date : dimanche prochain, par contre…"),
        ("malheureusement", "annonce le non avant de l'expliquer"),
        ("La phrase complète", "C'est gentil, mais malheureusement je travaille. Par "
                              "contre, dimanche prochain, je serais libre."),
    ], notes="Faire apprendre la dernière carte telle quelle. On ne change ensuite que la "
             "raison.")

    d.pratique('Production', "Répondez à l'invitation",
               "Par deux : l'un invite, l'autre répond en trois morceaux.", [
        ("Vous êtes libre et content d'y aller",
         "C'est gentil. Avec plaisir — deux heures, chez vous ?"),
        ("Vous travaillez ce jour-là",
         "C'est gentil, mais malheureusement je travaille. Par contre, dimanche prochain…"),
        ("Vous avez déjà un rendez-vous",
         "Merci d'y avoir pensé. J'ai déjà un rendez-vous ce jour-là. Une autre fois, avec plaisir."),
        ("Vous voulez venir avec votre enfant",
         "Avec plaisir. Est-ce que je peux venir avec mon garçon ?"),
        ("Vous ne savez pas encore",
         "C'est gentil. Je dois vérifier mon horaire : je vous le confirme demain."),
        ("Vous demandez quoi apporter",
         "Est-ce que j'apporte quelque chose ?"),
    ], corrige=True,
       notes="C'est le laboratoire de la mini-leçon t3invit. Faire passer tout le monde : "
             "c'est la dernière répétition avant la production orale du bloc E.")

    d.billet(
        "Racontez votre dernier déménagement en cinq phrases.",
        exemples=[
            "Trois au passé composé — ce qui est arrivé.",
            "Deux à l'imparfait — le temps qu'il faisait, ce que faisaient les autres.",
        ],
        notes="Le billet est la répétition écrite de la production orale de E1. Le "
              "ramasser et rendre les corrections avant le bloc E.")

    return d.save(dossier)
