# -*- coding: utf-8 -*-
"""C4 · Où, qui, que — et reprendre sans répéter
Bloc C « Défi 2 » · couleur ambre · 75 min. Grammaire du texte.
Source du module : exercices `t2ou` et `t2subst`, et leurs deux mini-leçons.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C4', section='ambre',
        titre="Où, qui, que — et reprendre sans répéter",
        chapeau="Deux façons de tenir un texte : accrocher une phrase à un "
                "nom, et redire une idée déjà dite sans la répéter. Les "
                "quatre points d'organisation se gagnent là.",
        duree='75 minutes')

    d.titre(notes="Les deux savoirs vont ensemble parce qu'ils font le même "
                  "travail : ils évitent de recommencer à zéro à chaque "
                  "phrase. C'est ce qui sépare un texte d'une liste.")

    d.objectifs([
        "employer « où » pour un lieu et aussi pour un moment ;",
        "choisir entre « qui », « que » et « où » ;",
        "fabriquer un nom à partir d'un verbe ;",
        "poser un démonstratif devant le nom de reprise.",
    ], notes="Le premier savoir est explicitement au programme du niveau 6 ; "
             "le second aussi, sous le nom de « procédés de substitution "
             "lexicale ».")

    d.declencheur(
        'Observation', "« L'année ___ le règlement a été adopté. » Que met-on dans le trou ?",
        pistes=[
            "« que » ? C'est ce qu'on entend le plus.",
            "« où » ? Mais ce n'est pas un lieu.",
            "Pourquoi est-ce difficile ?",
        ],
        notes="La difficulté est réelle et vaut la peine d'être nommée : "
              "dans presque toutes les autres langues, le lieu et le temps "
              "n'ont pas le même mot.")

    d.regle("« Où » sert au lieu et au temps",
            "la page où il l'a trouvé · l'année où le règlement a été adopté",
            precision="Les noms de temps qui l'appellent : l'année, le jour, "
                      "le moment, la semaine, l'époque, la fois. Si le mot "
                      "juste avant est un nom de temps, c'est « où ».",
            notes="Diapositive à photographier. « L'année que » est la faute "
                  "la plus fréquente du niveau, et elle s'entend chez des "
                  "gens qui parlent très bien.")

    d.tableau('Analyse', "Qui, que, où : ce qui manque après",
              ['Ce qui manque', 'Le mot'],
              [["le sujet du verbe", "qui — une lectrice qui écrit souvent"],
               ["le complément direct", "que — la page qu'elle a trouvée"],
               ["rien, et c'est un lieu", "où — la page où il l'a trouvé"],
               ["rien, et c'est un moment", "où — le jour où ils ont remis"]],
              cle=1,
              note="La même phrase peut prendre les trois, et parler de trois choses différentes.",
              notes="Diapositive à photographier. Prendre le temps sur la "
                    "note du bas : c'est le seul point de la séance qui "
                    "demande de la lenteur.")

    d.pratique('Pratique', "Où, qui ou que ?",
               "Complétez chaque phrase avec un seul mot.", [
        ("C'est l'année ... le conseil a adopté le règlement.", "où"),
        ("Voici la page ... il a trouvé la liste.", "où"),
        ("Voici la page ... elle a trouvée en premier.", "qu'"),
        ("C'est une lectrice ... écrit souvent au bulletin.", "qui"),
        ("Le jour ... ils ont remis leur plan, il pleuvait.", "où"),
        ("Le tableau ... ils ont recopié vient de la ville.", "qu'"),
    ], corrige=True, cols=1,
       notes="C'est l'exercice `t2ou` du module. Faire dire, pour chaque "
             "item, ce qui manque après le trou : c'est le test, et il "
             "suffit.")

    d.regle("Fabriquer un nom, et poser un démonstratif devant",
            "La ville a distribué les bacs. Cette distribution a duré trois semaines.",
            precision="Cinq suffixes couvrent presque tout : -tion, -age, "
                      "-ment, -sion, -ure. Sans « cette » devant, le lecteur "
                      "croit qu'on change de sujet.",
            notes="Diapositive à photographier. Le déterminant est le mot le "
                  "plus court de la phrase et il fait tout le travail de "
                  "liaison : le retirer suffit à casser le fil.")

    d.tableau('Analyse', "Le verbe, puis son nom",
              ['Le verbe', 'Le nom'],
              [["distribuer", "la distribution"],
               ["ramasser", "le ramassage"],
               ["traiter", "le traitement"],
               ["décider", "la décision"],
               ["enfouir", "l'enfouissement"]],
              cle=0,
              note="Aucun suffixe ne se devine : notez le nom en même temps que le verbe.",
              notes="Diapositive à photographier. Faire ajouter deux verbes "
                    "du sujet de chaque équipe, avec leur nom : c'est du "
                    "vocabulaire directement réemployable.")

    d.pratique('Pratique', "Redites-le avec un nom",
               "Reprenez chaque phrase par un groupe du nom.", [
        ("On enfouit les matières organiques.", "l'enfouissement des matières organiques"),
        ("La ville a distribué les bacs au printemps.", "cette distribution du printemps"),
        ("Le camion ramasse le bac chaque semaine.", "ce ramassage hebdomadaire"),
        ("Les habitants se sont plaints de l'odeur.", "ces plaintes au sujet de l'odeur"),
        ("On traite les résidus dans une usine.", "le traitement des résidus"),
        ("Le conseil a décidé de garder la collecte.", "cette décision du conseil"),
    ], corrige=True, cols=1,
       notes="C'est l'exercice `t2subst` du module. Rappeler qu'un mot précis "
             "sans synonyme, comme « biométhanisation », se répète sans "
             "gêne : un synonyme approximatif fait plus de dégâts.")

    d.billet(
        "Écris deux phrases sur ton sujet : la seconde reprend la première par un nom.",
        exemples=[
            "Commence la seconde par « Cette… » ou « Ce… ».",
            "Exemple : « La ville a distribué les bacs. Cette distribution… »",
        ],
        notes="Trois minutes. Ce billet se réemploie tel quel dans "
              "l'introduction écrite de la séance E2.")

    return d.save(dossier)
