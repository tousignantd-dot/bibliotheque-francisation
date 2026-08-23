# -*- coding: utf-8 -*-
"""C3 · Ils, le, en : reprendre sans répéter
Bloc C « Défi 2 » · couleur ambre · écriture et grammaire · 75 min.
Source : exercice `t2repr` et sa mini-leçon.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C3', section='ambre',
        titre="Ils, le, en : reprendre sans répéter",
        chapeau="Un texte tient par ses reprises. C'est ce qui sépare une "
                "suite de phrases d'un texte, et c'est aussi ce qui rend un "
                "texte impossible à suivre quand la reprise est floue.",
        duree='75 minutes')

    d.titre(notes="Séance de grammaire du texte, la plus utile du module hors de la "
                  "classe : elle sert dans une lettre, une critique, un compte rendu. "
                  "Les items font deux phrases, prévoir plus de temps qu'à l'habitude.")

    d.objectifs([
        "retrouver ce qu'un pronom reprend dans la phrase précédente ;",
        "comprendre le « ils » qui ne reprend personne ;",
        "employer « le » pour une phrase entière, « en » pour un groupe en de ;",
        "reprendre par un autre mot plutôt que par un pronom.",
    ], notes="Le quatrième objectif est celui qui distingue un texte de niveau 7 : la "
             "substitution lexicale ajoute un jugement, et c'est là que passe "
             "l'opinion dans une critique.")

    d.declencheur(
        'Préparation', "Que se passe-t-il si l'on répète le nom à chaque phrase ?",
        pistes=[
            "Lisez tout haut : « Le film... Le film... Le film... »",
            "C'est correct, alors pourquoi est-ce insupportable ?",
            "Et si l'on met un pronom partout ?",
            "Quand un pronom devient-il dangereux ?",
        ],
        notes="Le dernier point est la séance : deux noms devant, un pronom derrière, "
              "et le lecteur ne sait plus. C'est ce qu'on appelle la reprise floue.")

    d.tableau('Analyse', "Quatre façons de reprendre",
              ['Le procédé', 'Un exemple de la chanson'],
              [["Un pronom", "la rampe est neuve, ils l'ont refaite"],
               ["« le » pour une phrase", "j'avais dit l'an prochain, je l'ai dit neuf fois"],
               ["« en » pour un « de »", "elle parle de son escalier, elle en parle tout le temps"],
               ["Un autre mot", "la chanson, la pièce, ce refrain-là, l'œuvre"]],
              cle=0,
              note="Cherchez la préposition du verbe : « de » appelle en, un lieu appelle y.",
              notes="Diapositive à photographier. Le deuxième cas surprend : un "
                    "pronom qui remplace toute une phrase, et non un nom.")

    d.regle("Le « ils » du français ne reprend pas toujours quelqu'un",
            "« Ils ont encore augmenté le loyer » : personne n'a été nommé, et "
            "tout le monde comprend.",
            precision="Il désigne ceux qui décident et qu'on ne rencontre pas. Ce "
                      "n'est pas une faute, c'est un emploi courant — et dans la "
                      "chanson, c'est un choix : nommer le propriétaire en aurait "
                      "fait une plainte.",
            notes="Diapositive à photographier. Beaucoup d'élèves cherchent le "
                  "référent et croient avoir manqué une phrase. Les rassurer : il n'y "
                  "en a pas.")

    d.cartes('Analyse', "Reprendre par un autre mot", [
        ("Neutre", "le film, le long métrage, l'œuvre"),
        ("Avec un jugement", "cette petite merveille, ce long métrage bavard"),
        ("Plus général", "la pièce, le spectacle, l'ouvrage"),
        ("Une phrase devenue un nom", "j'avais dit l'an prochain, cette promesse-là"),
    ], cols=1,
       notes="La deuxième carte est la plus importante pour D2 : c'est ainsi qu'une "
             "critique fait passer son opinion sans jamais l'annoncer.")

    d.piege('Écrit',
            "« Marilou parle à Ghyslaine de sa chanson. Elle l'aime. »",
            "« Marilou parle à Ghyslaine de sa chanson. Marilou l'aime beaucoup. »",
            "Deux noms de femmes devant, un « elle » derrière : le lecteur ne "
            "sait pas laquelle. Quand deux référents possibles précèdent, on "
            "reprend le nom, ou l'on récrit la phrase. Le pronom est le plus "
            "léger des procédés et le moins tolérant à l'ambiguïté.",
            notes="Erreur très fréquente à l'écrit et jamais à l'oral, où le contexte "
                  "et le regard suffisent. La montrer sur un texte d'élève de A4, "
                  "anonymement.")

    d.pratique('Grammaire', "Complétez la reprise",
               "Relisez les deux phrases ensemble avant de répondre.", [
        ("La rampe est neuve. Ils ___ ont refaite en septembre.", "l'"),
        ("___ ont refait la rampe, et on ne sait pas qui.", "Ils"),
        ("J'avais dit l'an prochain. Je ___ ai dit neuf fois.", "l'"),
        ("Elle parle de son escalier. Elle ___ parle depuis neuf ans.", "en"),
        ("Une boîte est dans le corridor. Elle ___ est depuis neuf ans.", "y"),
        ("Le comité a reçu trois propositions. ___ trois entrent dans le budget.", "Les"),
    ], corrige=True,
       notes="Exercice `t2repr` du module, qui en compte dix. Faire relire les deux "
             "phrases ensemble à voix haute : la première décide, et l'oreille "
             "tranche mieux que la règle.")

    d.pratique('Production écrite', "Le même paragraphe, sans répétition",
               "Récrivez en variant les reprises.", [
        ("Texte de départ", "Le film est lent. Le film dure une heure cinquante. J'ai aimé le film."),
        ("Une reprise par pronom", "il, l', en"),
        ("Une reprise par un autre mot", "ce long métrage, l'œuvre"),
        ("Une reprise avec un jugement", "cette heure et demie tranquille"),
    ], corrige=False,
       notes="Dix minutes, puis lecture croisée en dyades. Le contrôle est simple : "
             "le mot « film » ne doit plus apparaître qu'une fois.")

    d.billet(
        "Écrivez deux phrases sur une œuvre, la seconde reprenant la première.",
        exemples=[
            "Sans répéter le nom de l'œuvre.",
            "Soulignez la reprise.",
        ],
        notes="Ramasser. Les billets où la reprise est floue se repèrent en trois "
              "secondes et font une excellente ouverture pour C4.")

    return d.save(dossier)
