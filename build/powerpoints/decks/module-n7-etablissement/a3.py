# -*- coding: utf-8 -*-
"""A3 · Familier, standard, soutenu
Bloc A « Je découvre » · couleur ambre · 75 min. Variétés de langue.
Source : exercice `prReg` et sa mini-leçon.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A3', section='ambre',
        titre='Familier, standard, soutenu',
        chapeau="Les trois niveaux sont polis. Ce qui change, c'est la "
                "distance qu'ils supposent — et un comité de sélection n'a "
                "offert aucune intimité.",
        duree='75 minutes')

    d.titre(notes="Séance délicate : le familier n'est pas fautif, et il ne faut pas "
                  "que le groupe reparte en croyant que sa façon de parler est "
                  "mauvaise. Le dire dès l'ouverture.")

    d.objectifs([
        "reconnaître le niveau de langue d'une phrase entendue ;",
        "repérer ce qui trahit le familier et ce qui trahit le soutenu ;",
        "choisir le standard pour l'entrevue et le téléphone ;",
        "garder le soutenu pour la lettre.",
    ], notes="Le programme du niveau 7 demande de « reconnaître les variétés de "
             "langue et d'en tenir compte ». Reconnaître d'abord : le choix vient "
             "tout seul ensuite.")

    d.declencheur(
        'Observation', "À qui parlez-vous comme ça ?",
        pistes=[
            "« Ça commence quand, la job ? »",
            "« À quel moment la formation commence-t-elle ? »",
            "« Je vous saurais gré de m'indiquer la date. »",
            "Laquelle diriez-vous à votre voisine ? à un comité ?",
        ],
        notes="Faire lire les trois phrases par trois élèves. Personne ne se trompe "
              "sur la première ni sur la troisième ; c'est la deuxième qui se "
              "travaille.")

    d.tableau('Analyse', "Ce qui trahit chaque niveau",
              ['Le niveau', 'Ce qui le trahit'],
              [['familier', "la question sans marque, les mots coupés, le « ne » absent"],
               ['standard', "la phrase entière, le « ne » prononcé, le vouvoiement"],
               ['soutenu', "les formules figées et les phrases à subordonnées"]],
              cle=0,
              note="Le standard est le niveau de l'établissement : c'est celui qu'il "
                   "emploie avec vous, et celui qu'il attend en retour.",
              notes="Trois rangées seulement, donc la note tient. Insister sur le "
                    "« ne » : à l'oral courant tout le monde le laisse tomber, en "
                    "entrevue il coûte un dixième de seconde et il s'entend.")

    d.regle("Un cran au-dessus, jamais un cran en dessous",
            "Écoutez le niveau de l'autre et tenez-vous juste au-dessus.",
            precision="Un comité qui vous dit « on va commencer » ne vous invite pas à "
                      "répondre « ouais, correct ». Il parle standard parce qu'il vous "
                      "reçoit ; le standard est donc la réponse.",
            notes="Diapositive à photographier. C'est la règle pratique de toute la "
                  "séance, et elle évite d'avoir à juger chaque phrase une par une.")

    d.pratique('Compréhension', "Familier, standard ou soutenu ?",
               "Dites à quel niveau appartient chaque phrase.", [
        ("Veuillez agréer, Madame, l'expression de mes sentiments distingués.", "soutenu"),
        ("Je vous remercie de m'avoir reçue ce matin.", "standard"),
        ("Merci ben, là, c'était le fun.", "familier"),
        ("À quel moment la formation commence-t-elle ?", "standard"),
        ("J'ai pas eu de nouvelles pantoute depuis l'entrevue.", "familier"),
        ("Je vous saurais gré de bien vouloir accuser réception.", "soutenu"),
    ], corrige=True,
       notes="Faire dire, pour chaque item familier, la version standard équivalente. "
             "C'est l'exercice de production caché de la séance.")

    d.cartes('Reformulation', "La même chose, trois fois", [
        ("Remercier",
         "familier : merci ben · standard : je vous remercie · "
         "soutenu : je vous remercie de l'attention portée à ma candidature"),
        ("Demander une date",
         "familier : ça commence quand ? · standard : à quel moment "
         "commence-t-elle ? · soutenu : pourriez-vous me préciser la date ?"),
        ("Dire qu'on est sans nouvelles",
         "familier : j'ai pas eu de nouvelles · standard : je n'ai reçu aucune "
         "nouvelle depuis le 12 mars"),
        ("Se présenter au téléphone",
         "familier : c'est Rania · standard : bonjour, Rania Nassar, "
         "dossier 41-2887"),
    ], notes="Faire jouer les paires : l'un dit la version familière, l'autre répond "
             "par la version standard. Deux minutes par paire suffisent.")

    d.piege('Piège', "J'ai appliqué sur le programme.",
            "J'ai posé ma candidature au programme.",
            "« Appliquer » vient de l'anglais et se remarque immédiatement dans un "
            "centre de formation. On pose sa candidature, on soumet un dossier.",
            notes="Faute très répandue et jamais corrigée en milieu de travail. La "
                  "reprendre ici épargne une gêne en entrevue.")

    d.billet("Écris une phrase familière que tu dis souvent, puis la même phrase en "
             "français standard.",
             exemples=["Familier : ça finit à quelle heure ?",
                       "Standard : à quelle heure la rencontre se termine-t-elle ?"],
             notes="Ramasser les billets et en lire trois à voix haute à la séance "
                   "suivante, sans nommer personne.")

    return d.save(dossier)
