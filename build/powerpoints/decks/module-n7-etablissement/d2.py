# -*- coding: utf-8 -*-
"""D2 · Rapporter ce qui a été dit
Bloc D « Défi 3 · Le suivi, après » · couleur ambre · 75 min.
Source : exercices `t3rap` et `t3que`, et leurs mini-leçons.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='D2', section='ambre',
        titre='Rapporter ce qui a été dit',
        chapeau="« Je rappelle encore » ferme une porte. « Vous m'aviez dit "
                "de vous rappeler » l'ouvre — même personne, même dossier, "
                "même jour.",
        duree='75 minutes')

    d.titre(notes="Séance de grammaire du texte appliquée au téléphone. Les items font "
                  "deux phrases : les faire lire en entier avant de compléter.")

    d.objectifs([
        "faire reculer les temps quand le verbe introducteur est au passé ;",
        "employer le conditionnel pour un futur rapporté ;",
        "employer le plus-que-parfait pour ce qui était déjà fait ;",
        "limiter avec « ne… que » et conclure avec « donc ».",
    ], notes="Le premier objectif est mécanique et se retient en une séance ; le "
             "quatrième est celui qui fait finir un appel proprement.")

    d.declencheur(
        'Observation', "Comment rapporter sans reprocher ?",
        pistes=[
            "« Vous m'aviez dit de rappeler. » ou « vous aviez promis » ?",
            "Qu'est-ce que « promis » ajoute ?",
            "Qui a l'air d'avoir tort, dans chaque cas ?",
            "Lequel des deux obtient une réponse ?",
        ],
        notes="Le mot « promis » met l'autre en défaut dès la deuxième phrase, et il "
              "n'y a plus rien à obtenir ensuite. Le faire dire par le groupe plutôt "
              "que l'annoncer.")

    d.tableau('Analyse', "Chaque temps recule d'un cran",
              ['Ce qui a été dit', 'Ce qu\'on rapporte'],
              [['le stage arrive tôt', "vous m'aviez dit qu'il arrivait tôt"],
               ['il arrivera avant Noël', "vous m'aviez dit qu'il arriverait"],
               ['je vais vous rappeler', "vous m'aviez dit que vous alliez me rappeler"],
               ["j'ai déposé mon dossier", "j'ai expliqué que j'avais déposé"],
               ['rappelez-moi', "vous m'aviez demandé de vous rappeler"]],
              cle=0,
              notes="Cinq rangées sans note : la densité tient. Diapositive à "
                    "photographier — c'est tout le contenu grammatical de la séance, "
                    "et il s'apprend par cette table.")

    d.regle("Le futur rapporté devient conditionnel",
            "« Le stage arrivera avant Noël » devient « il m'avait dit qu'il "
            "arriverait avant Noël ».",
            precision="C'est la postériorité quand le point de référence est décalé. "
                      "À l'oral, « aller » à l'imparfait fait la même chose et sonne "
                      "plus naturel : « vous alliez me rappeler ».",
            notes="Diapositive à photographier. Les deux formes sont correctes ; "
                  "laisser le groupe choisir celle qu'il dira le plus facilement.")

    d.pratique('Grammaire', "Rapportez au passé",
               "Mettez le verbe au temps qui convient.", [
        ("« Le stage arrive tôt. » On rapporte : Il m'avait dit que le stage (arriver) ___ tôt.", "arrivait"),
        ("« Il arrivera avant Noël. » On rapporte : Il m'avait répondu qu'il (arriver) ___ avant Noël.", "arriverait"),
        ("« Je vais vous rappeler. » On rapporte : Vous m'aviez dit que vous (aller) ___ me rappeler.", "alliez"),
        ("« J'ai déposé mon dossier. » On rapporte : J'ai expliqué que j'(déposer) ___ mon dossier.", "avais déposé"),
        ("« Les places sont limitées. » On rapporte : La lettre disait qu'elles (être) ___ limitées.", "étaient"),
        ("« Rappelez-moi. » On rapporte : Vous m'aviez demandé de vous (rappeler) ___.", "rappeler"),
    ], corrige=True,
       notes="Faire lire la phrase rapportée à voix haute, au téléphone imaginaire. "
             "C'est ainsi qu'elle se retiendra, pas en la copiant.")

    d.regle("Ne… que limite, il ne nie pas",
            "« Il ne me manque qu'un préalable » dit que tout le reste est en règle.",
            precision="Le mot restreint ce qui suit « que ». « Je ne travaille que les "
                      "fins de semaine » et « je ne travaille pas que les fins de "
                      "semaine » disent deux choses opposées : placez « que » juste "
                      "devant ce que vous limitez.",
            notes="Diapositive à photographier. Faire produire les deux phrases par "
                  "deux élèves, puis demander au groupe laquelle veut dire quoi.")

    d.cartes('Clôture', "Trente secondes pour finir un appel", [
        ("Une restriction",
         "Il ne me manque qu'un préalable ; le reste du dossier est complet."),
        ("Une conséquence",
         "Les dossiers se regardent à la mi-décembre ; je vous rappellerai donc le 10."),
        ("Une reformulation",
         "Autrement dit, je m'inscris à la mise à niveau et je vous rappelle en "
         "décembre ?"),
        ("Une date, jamais un souhait",
         "Je vous reparle le 10 décembre. Merci de m'avoir rappelée."),
    ], notes="Faire jouer la clôture en paires, deux minutes chacun. Un appel qui se "
             "termine sans date recommence au complet la fois suivante.")

    d.billet("Rapporte une phrase qu'on t'a dite au téléphone, avec « on m'avait dit "
             "que… ».",
             exemples=["On m'avait dit que la réponse arriverait avant Noël.",
                       "On m'avait dit que j'allais recevoir une lettre."],
             notes="Ramasser les billets. Vérifier une seule chose : le temps du verbe "
                   "rapporté. Le reste appartient à l'élève.")

    return d.save(dossier)
