# -*- coding: utf-8 -*-
"""B3 · Pouvoir, devoir, falloir.
Bloc B « Défi 1 · L'appel » · couleur ambre · 75 min.
Source : exercice `t1modal` et sa mini-leçon.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B3', section='ambre',
        titre="Pouvoir, devoir, falloir",
        chapeau="Trois verbes qui ne disent pas une action, mais comment il "
                "faut la prendre. Dans une démarche, ils portent "
                "l'essentiel : ce qu'on a le droit de faire, ce qu'on est "
                "obligé de faire, ce que la règle exige de tout le monde.",
        duree='75 minutes')

    d.titre(notes="Séance de grammaire. Ramasser le devoir B2 et corriger deux ou trois "
                  "subordonnées au tableau avant de commencer : la structure de B2 revient "
                  "dans tous les exercices d'aujourd'hui.")

    d.objectifs([
        "distinguer possibilité, obligation nommée et règle générale ;",
        "employer l'infinitif après pouvoir, devoir et falloir ;",
        "conjuguer les trois au présent et au passé composé ;",
        "employer « il faut » pour énoncer une règle sans désigner personne.",
    ])

    d.declencheur(
        'Discussion', "Trois phrases. Est-ce que je suis obligé, dans les trois ?",
        pistes=[
            "« Vous pouvez faire la demande en ligne. »",
            "« Vous devez présenter deux pièces. »",
            "« Il faut une preuve de résidence. »",
            "Qui est obligé, dans la troisième ?",
        ],
        notes="La dernière question est le cœur de la séance : personne n'est nommé, et "
              "c'est précisément pour ça que l'administration emploie cette forme.")

    d.regle("Après les trois, le verbe reste à l'infinitif",
            "Je dois apporter · Vous pouvez rappeler · Il faut sortir le bac.",
            precision="Ces trois verbes commandent le verbe qui suit. Celui-ci ne se "
                      "conjugue jamais : ni « je dois j'apporte », ni « il faut vous "
                      "sortez ». C'est la première chose à installer, avant toute nuance "
                      "de sens.",
            notes="Diapositive à photographier. Faire répéter les trois exemples à voix "
                  "haute par le groupe entier.")

    d.tableau('Les trois verbes', "Ce que chacun dit",
              ['Verbe', 'Ce qu\'il exprime', 'Exemple'],
              [["pouvoir", "c'est possible, c'est permis", "Vous pouvez faire la demande en ligne."],
               ["devoir", "c'est obligé, et je sais qui", "Vous devez présenter deux pièces."],
               ["falloir", "c'est obligé, peu importe qui", "Il faut une preuve de résidence."]],
              cle=0,
              note="« Il faut » ne se conjugue qu'avec « il » : c'est la forme des règlements.",
              notes="Diapositive à photographier. Insister sur la troisième ligne : c'est "
                    "celle que les élèves lisent partout sans jamais l'employer eux-mêmes.")

    d.cartes("Pouvoir sert aussi à demander", "Quatre usages à distinguer", [
        ("La possibilité",
         "« Vous pouvez faire la demande en ligne. » — c'est offert."),
        ("La demande de service",
         "« Pouvez-vous répéter, s'il vous plaît ? » — la formule polie du téléphone."),
        ("La permission",
         "« Est-ce que je peux passer demain ? » — je demande le droit."),
        ("L'impossibilité passée",
         "« Je n'ai pas pu terminer ma demande. » — participe « pu », sans accent."),
    ], notes="La troisième carte prête à confusion avec « je dois passer demain », qui "
             "annonce au lieu de demander. Faire jouer les deux phrases à deux élèves.")

    d.tableau('Les trois au passé composé', "Trois participes irréguliers",
              ['Verbe', 'Participe', 'Exemple'],
              [["pouvoir", "pu", "Je n'ai pas pu terminer le formulaire."],
               ["devoir", "dû", "J'ai dû me déplacer au guichet."],
               ["falloir", "fallu", "Il a fallu que je rappelle."]],
              cle=1,
              note="« dû » porte son accent au masculin singulier seulement : dû, due, dus, dues.",
              notes="Diapositive à photographier. Ces trois participes reviennent dans "
                    "tout récit de démarche qui a mal tourné — donc en D2 et en E2.")

    d.pratique('Conjugaison', "Complétez",
               "Pouvoir, devoir ou falloir, à la bonne forme.", [
        ("Vous ___ présenter deux pièces d'identité.", "devez"),
        ("___ -vous répéter le numéro, s'il vous plaît ?", "Pouvez"),
        ("Pour entrer à l'écocentre, il ___ une preuve de résidence.", "faut"),
        ("Je n'ai pas ___ terminer le formulaire.", "pu"),
        ("J'ai ___ me déplacer au comptoir.", "dû"),
        ("Il ___ que vous sortiez le bac la veille au soir.", "faut"),
        ("Il a ___ que je rappelle avec mon numéro.", "fallu"),
        ("Est-ce que je ___ faire ma demande par téléphone ?", "peux"),
    ], corrige=True,
       notes="La sixième phrase annonce « il faut que » + subjonctif, travaillé en D2. "
             "Le signaler sans le développer : ce n'est pas la séance.")

    d.piege("Conjuguer falloir à d'autres personnes",
            "Nous fallons revenir demain.",
            "Il faut que nous revenions demain.",
            "Falloir n'existe qu'avec « il ». Dès qu'on veut nommer quelqu'un, il faut "
            "passer par « il faut que » et le subjonctif — la structure du défi 3.",
            notes="Erreur rare mais tenace. Un élève qui la fait a compris le sens et "
                  "cherche la forme : le lui dire, c'est encourageant.")

    d.pratique('Emploi', "Dites-le des trois façons",
               "Même information, trois formulations.", [
        ("Règle générale, personne n'est nommé", "Il faut deux pièces d'identité."),
        ("Obligation, la personne est nommée", "Vous devez apporter deux pièces d'identité."),
        ("Possibilité offerte", "Vous pouvez apporter votre bail ou une facture."),
        ("Demande polie au téléphone", "Pouvez-vous me dire quelles pièces il faut ?"),
        ("Ce qui n'a pas été possible", "Je n'ai pas pu faire la demande en ligne."),
        ("Ce qui a été imposé", "J'ai dû me déplacer au guichet."),
    ], corrige=True,
       notes="Exercice de synthèse. Faire remarquer que les six phrases pourraient se "
             "suivre dans un même appel : c'est ce que le niveau 5 demande.")

    d.billet(
        "Écrivez cinq phrases sur une démarche que vous avez déjà faite.",
        exemples=[
            "Deux avec « il faut », deux avec « je dois » ou « j'ai dû », une avec « je n'ai pas pu ».",
            "Une démarche vraie : école, clinique, banque, ville.",
        ],
        notes="Devoir qui prépare deux choses à la fois : la prise de notes de B4 et le "
              "récit de démarche du défi 3.")

    return d.save(dossier)
