# -*- coding: utf-8 -*-
"""B1 · Tu ou vous ?
Bloc B « Défi 1 · Ça va ? Et toi ? » · couleur acier · 75 min.
Source : dialogue `t1`, exercice `t1tuvous`, mini-leçon `t1tuvous`.

La séance qui porte le point de langue du défi. Le programme du niveau 2
demande les pronoms personnels conjoints et l'indicatif présent de quelques
verbes usuels ; le tutoiement et le vouvoiement sont ce qui les rend
nécessaires, parce que le même échange change de forme selon la personne.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n2-bonjour/images/')


def build(dossier):
    d = Deck(
        code='B1', section='acier',
        titre="Tu ou vous ?",
        chapeau="Deux façons de parler à une seule personne. C'est la "
                "distance qui décide, pas la grammaire.",
        duree='75 minutes')

    d.titre(notes="Séance clé du module. Beaucoup d'élèves viennent de langues sans cette "
                  "distinction, ou avec une distinction différente. Prendre le temps de "
                  "l'expliquer avec des personnes réelles, pas avec des règles.")

    d.objectifs([
        "choisir « tu » ou « vous » selon la personne ;",
        "accorder le verbe avec le pronom choisi ;",
        "renvoyer la question : et toi ? et vous ? ;",
        "tenir le même choix pendant tout l'échange.",
    ])

    d.declencheur(
        'Observation', "À qui dit-on « tu » ?",
        image=IMG + 'apres-midi-centre.jpg',
        pistes=[
            "À qui parlez-vous en classe ?",
            "Dites-vous « tu » à votre enseignante ?",
            "Et à la personne assise à côté de vous ?",
            "Dans votre langue, y a-t-il deux façons de dire « tu » ?",
        ],
        notes="La dernière question ouvre presque toujours une discussion riche : "
              "plusieurs langues du groupe ont la même distinction, et la comparaison "
              "installe la notion plus vite qu'une explication.")

    d.dialogue('Dialogue · 1 de 2', "Salut, Samir !", [
        ("NADIA", "Salut, Samir ! Ça va ?", True),
        ("SAMIR", "Ça va, et toi ?", True),
        ("NADIA", "Ça va bien. Tu arrives comment, le matin ?", True),
        ("SAMIR", "Je prends le métro. Et toi ?", True),
    ], consigne="Écoutez deux fois avant de lire.",
       notes="Nadia et Samir sont dans la même classe : ils se tutoient dès le premier "
             "jour. Le faire remarquer avant d'afficher le deuxième dialogue.")

    d.dialogue('Dialogue · 2 de 2', "La même chose, avec madame Roy", [
        ("NADIA", "Bonjour, madame Roy. Vous allez bien ?", True),
        ("GILBERTE", "Ça va, Nadia. Tu vas au centre ?", True),
        ("NADIA", "Oui. Et vous, vous sortez ce matin ?", True),
        ("GILBERTE", "Non, je reste à la maison aujourd'hui.", True),
    ], notes="Faire entendre que madame Roy tutoie Nadia et que Nadia la vouvoie. Ce "
             "n'est pas une faute : c'est l'usage entre une personne âgée et une jeune "
             "voisine.")

    d.tableau('Analyse', "Le mot change, le verbe aussi",
              ['Avec « tu »', 'Avec « vous »'],
              [["tu vas", "vous allez"],
               ["tu travailles", "vous travaillez"],
               ["tu prends", "vous prenez"],
               ["et toi ?", "et vous ?"]],
              cle=2,
              note="La forme du « vous » finit presque toujours par le son [e].",
              notes="Diapositive à photographier. Faire lire les deux colonnes à voix "
                    "haute, ligne par ligne, pour entendre le [e] final.")

    d.regle("Dans le doute, « vous »",
            "« Vous » ne fâche jamais personne.",
            precision="On passe à « tu » quand l'autre le propose : « on peut se "
                      "tutoyer ». Avant, on garde « vous » — avec une personne plus âgée, "
                      "un commis, un professeur, une personne qu'on ne connaît pas.",
            notes="Diapositive à photographier. Donner la phrase « on peut se tutoyer » : "
                  "c'est celle qu'ils entendront, et ils doivent la reconnaître.")

    d.piege('Le piège', "tu allez", "tu vas · vous allez",
            "On ne mélange pas les deux dans la même phrase. Quand on choisit « vous », "
            "<b>tout</b> le reste suit : le verbe, et le « et vous ? » de la fin. Un "
            "échange qui commence au « vous » finit au « vous ».",
            notes="Écrire au tableau une phrase mélangée et faire corriger par le groupe. "
                  "L'erreur est fréquente en milieu d'échange, quand l'attention baisse.")

    d.pratique('Compréhension', "Tu ou vous ?",
               "Complétez avec « tu » ou « vous ».", [
        ("Nadia à madame Roy : « Et ___ , ça va ? »", "vous"),
        ("Nadia à Samir : « Et ___ , ça va ? »", "toi"),
        ("Madame Roy à Nadia : « ___ vas au centre ? »", "tu"),
        ("Nadia à madame Roy : « ___ allez bien ? »", "vous"),
        ("À une personne inconnue : « ___ travaillez ici ? »", "vous"),
    ], corrige=True, cols=1,
       notes="Faire justifier chaque réponse par la personne, pas par la forme du verbe : "
             "c'est la personne qui décide.")

    d.pratique('Pratique · à deux', "Deux fois le même échange",
               "Deux par deux, la même conversation jouée deux fois.", [
        ("Étape 1", "Jouez l'échange entre deux camarades : « tu »."),
        ("Étape 2", "Rejouez-le avec une voisine de soixante-dix ans : « vous »."),
        ("Étape 3", "Changez de rôle et recommencez."),
        ("Étape 4", "Notez les deux verbes qui vous ont fait hésiter."),
    ], cols=1,
       notes="Vingt minutes. L'étape 4 est celle qui reste : ramasser les verbes cités "
             "et les écrire au tableau à la fin.")

    d.billet(
        "Écrivez la même question deux fois, au « tu » puis au « vous ».",
        exemples=[
            "Tu travailles le soir ?",
            "Vous travaillez le soir ?",
            "Et toi ? / Et vous ?",
        ],
        notes="Devoir court. Trois paires suffisent ; en demander plus dilue le point.")

    return d.save(dossier)
