# -*- coding: utf-8 -*-
"""C2 · Accorder les adjectifs de la description
Bloc C « Défi 2 » · couleur ambre · grammaire · 75 min.
Source : exercice `t2adj` (cols:1) et sa mini-leçon — l'accord en genre et en
nombre, et les trois cas particuliers qui reviennent dans toute description.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C2', section='ambre',
        titre="Accorder les adjectifs de la description",
        chapeau="Grande s'entend. Ondulés ne s'entend pas du tout. Dans une "
                "description écrite, la moitié des accords sont muets.",
        duree='75 minutes')

    d.titre(notes="Séance de grammaire. Écrire au tableau « des cheveux ondulé » et "
                  "demander au groupe ce qui manque. Presque tout le monde voit "
                  "l'erreur à l'écrit ; personne ne l'entend à l'oral. C'est tout le "
                  "sujet de la séance.")

    d.objectifs([
        "accorder l'adjectif avec le nom, même quand rien ne s'entend ;",
        "reconnaître les adjectifs déjà terminés par e ;",
        "laisser invariable une couleur formée de deux mots ;",
        "accorder l'attribut après être et avoir l'air.",
    ], notes="Le troisième objectif surprend toujours : bleu marine ne s'accorde "
             "jamais, alors que bleue s'accorde. C'est le second mot qui bloque.")

    d.declencheur(
        'Observation', "Quels accords entends-tu, et lesquels ne s'entendent pas ?",
        pistes=[
            "grande, grand : entends-tu la différence ?",
            "ondulés, ondulé : et là ?",
            "rondes, rond : et là ?",
            "Comment fais-tu quand l'oreille ne dit rien ?",
        ],
        notes="Faire l'expérience à voix haute, en fermant les yeux. La réponse à la "
              "dernière question est la méthode de la séance : on cherche le nom des "
              "yeux.")

    d.tableau('Analyse', "Le nom décide, toujours",
              ['Le groupe', 'Pourquoi cet accord'],
              [["un visage allongé", "masculin singulier, comme visage"],
               ["une longue veste grise", "féminin singulier, deux fois"],
               ["des cheveux ondulés", "masculin pluriel, comme cheveux"],
               ["des lunettes rondes", "féminin pluriel, comme lunettes"],
               ["les pommettes hautes", "féminin pluriel, comme pommettes"],
               ["elle est grande", "attribut, accordé avec le sujet"]],
              cle=0,
              notes="Diapositive à photographier. Cheveux est masculin pluriel et "
                    "lunettes est féminin pluriel : ces deux noms décident de presque "
                    "tous les accords d'une description physique.")

    d.cartes('Trois cas', "Ce qui ne suit pas la règle simple", [
        ("Adjectif déjà en e",
         "mince, jeune, large, drôle. Rien ne change au féminin : un homme mince, une femme mince. Mais le s du pluriel reste."),
        ("Couleur en deux mots",
         "bleu marine, vert clair, gris foncé : invariables. Une casquette bleu marine, des yeux vert clair. Mais une casquette bleue s'accorde."),
        ("Attribut après être",
         "Elle est grande. Ils ont l'air fatigués. L'adjectif s'accorde avec le sujet, même loin du nom."),
        ("Deux adjectifs, deux accords",
         "Sa valise est rouge et beaucoup plus grosse que la mienne : chacun s'accorde de son côté."),
    ], notes="Une carte à la fois, avec un exemple demandé au groupe entre chaque. Le "
             "deuxième cas mérite deux minutes de plus que les autres.")

    d.regle("Chercher le nom des yeux, pas de l'oreille",
            "Un accord muet s'écrit quand même.",
            precision="Devant un adjectif, on remonte au nom : quel nom, quel genre, "
                      "quel nombre ? La question prend deux secondes et règle presque "
                      "tous les cas. L'oreille, elle, ne signale qu'un accord sur "
                      "deux.",
            notes="Diapositive à photographier. Le geste est le même qu'en B3 pour les "
                  "reprises : remonter au nom. Le faire remarquer.")

    d.pratique('Grammaire', "Écrivez l'adjectif à la bonne forme",
               "L'adjectif est entre parenthèses. Cherchez d'abord le nom.", [
        ("Kadiatou a un visage (allongé) ... et les pommettes hautes.", "allongé"),
        ("Elle a des cheveux (ondulé) ... attachés en chignon.", "ondulés"),
        ("Elle porte une longue veste (gris) ... et un foulard vert.", "grise"),
        ("Ses lunettes sont (rond) ..., à monture fine.", "rondes"),
        ("Ghislain portera une casquette (bleu marine) ....", "bleu marine"),
        ("Les deux voyageurs avaient l'air (fatigué) ....", "fatigués"),
    ], corrige=True,
       notes="Faire nommer le nom avant la forme, à chaque item. Sans cela, les élèves "
             "accordent au son et se trompent une fois sur trois.")

    d.piege('Couleur', "Une casquette bleue marine",
            "Une casquette bleu marine",
            "Dès qu'une couleur s'écrit en deux mots, elle ne s'accorde plus du tout : "
            "bleu marine, vert clair, gris foncé, jaune paille. La règle est nette et "
            "elle ne souffre pas d'exception — ce qui la rend facile.",
            notes="Faire chercher trois autres couleurs en deux mots par le groupe. "
                  "Les écrire au tableau avec un nom féminin devant, pour vérifier.")

    d.billet(
        "Décris en une phrase ce que tu portes aujourd'hui.",
        exemples=[
            "Au moins deux adjectifs.",
            "Souligne les accords qui ne s'entendent pas.",
        ],
        notes="Deux minutes. Les billets se corrigent d'un coup d'œil et montrent qui "
              "accorde au son.")

    return d.save(dossier)
