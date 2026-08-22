# -*- coding: utf-8 -*-
"""C3 · Celui, celle, ceux, celles
Bloc C « Défi 2 · Lire une bande dessinée » · couleur ambre · 75 min.
Source : exercice `t2demo`, mini-leçon `t2demo`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C3', section='ambre',
        titre="Celui, celle, ceux, celles",
        chapeau="« Prenez celui qui a la couverture bleue. » « Celle que "
                "vous avez rapportée hier a une suite. » Écoutez deux "
                "minutes de conversation au comptoir d'une bibliothèque : "
                "ces quatre mots y reviennent vingt fois, et sans eux on ne "
                "comprend rien.",
        duree='75 minutes')

    d.titre(notes="Séance de langue. Commencer par une petite mise en scène : poser trois "
                  "livres sur le bureau et demander à un élève d'en désigner un sans dire "
                  "son titre ni le montrer du doigt. Il trouvera « celui qui… » ou il "
                  "butera — dans les deux cas, la séance est lancée.")

    d.objectifs([
        "remplacer un nom déjà dit par celui, celle, ceux ou celles ;",
        "accorder avec le nom remplacé, jamais avec ce qui suit ;",
        "ne jamais laisser le pronom seul : qui, que, de, -ci ou -là derrière ;",
        "désigner par une caractéristique plutôt qu'en montrant du doigt.",
    ], notes="Le quatrième objectif est le savoir du programme : les pronoms démonstratifs "
             "complexes non déictiques — non déictique voulant dire qu'on ne pointe rien. "
             "Le mot n'a pas à être dit aux élèves ; la chose, oui.")

    d.declencheur(
        'Mise en route', "« J'ai lu deux albums. Le deuxième album était "
                         "meilleur. » Comment éviter de répéter « album » ?",
        pistes=[
            "Quel mot mettriez-vous à la place du second « album » ?",
            "Et si l'on parlait de deux planches, au féminin ?",
            "Et de plusieurs personnages ?",
            "Est-ce qu'on peut dire « celui » tout seul, à la fin d'une phrase ?",
        ],
        notes="La quatrième piste est celle qui surprend : en anglais, « this one » se "
              "suffit ; en français, il faut dire lequel. C'est la difficulté principale "
              "pour les élèves qui passent par l'anglais.")

    d.regle("Il ne vit jamais seul",
            "Après celui, celle, ceux, celles, il faut toujours quelque chose : "
            "qui, que, de, ou -ci et -là.",
            precision="« Celui qui parle. » « Celle que je préfère. » « Ceux de la "
                      "première planche. » « Celui-là. » Un « celui » posé tout seul au "
                      "bout d'une phrase laisse l'autre en attente d'une suite qui ne "
                      "vient pas. C'est ce qui distingue le français de l'anglais ici.",
            notes="Diapositive à photographier. Faire produire les quatre formes à voix "
                  "haute avec un complément différent chacune. Trois minutes, et le "
                  "réflexe est posé.")

    d.tableau('Quatre formes', "L\'accord se fait avec le nom remplacé",
              ['Le nom remplacé', 'La forme', 'Un exemple du module'],
              [["l'album (masc. sing.)", "celui", "celui que j'ai lu la semaine passée"],
               ["la planche (fém. sing.)", "celle", "celle qui m'a le plus marquée"],
               ["les personnages (masc. plur.)", "ceux", "ceux qu'on voit au début"],
               ["les bulles (fém. plur.)", "celles", "celles qui ont une pointe en ronds"],
               ["Ce qui décide", "le nom", "jamais le verbe ni le sujet qui suit"]],
              cle=1,
              notes="La dernière rangée est la règle d'accord. Faire le geste : chercher le "
                    "nom d'abord, à voix basse, puis choisir la forme. Les quatre formes "
                    "se prononcent différemment — celui, celle, ceux, celles — donc "
                    "l'accord s'entend, ce qui est une chance.")

    d.cartes("Montrer, ou désigner", "Deux emplois qu'on ne mélange pas", [
        ("On montre du doigt",
         "celui-ci, sur la tablette · prenez celui-là · celles-là, en bas."),
        ("On désigne par ce qu'on en dit",
         "celui que je préfère · celle qui a gagné un prix · ceux de la fin."),
        ("Ce qu'il ne faut pas faire",
         "Dire « celui-ci » d'un livre resté à la maison : rien n'est montré."),
    ], notes="La troisième carte est la faute la plus répandue et la plus discrète. Si la "
             "chose n'est pas devant vous, « celui-ci » sonne faux sans qu'on sache "
             "pourquoi. Employer « celui que », « celui qui », « celui de ».")

    d.pratique('Complétez', "celui, celle, ceux ou celles ?",
               "Cherchez d'abord le nom remplacé, puis accordez.", [
        ("J'ai lu deux albums ; ___ que je préfère est le deuxième.", "celui"),
        ("Cette planche-ci est belle, mais ___ de la fin est encore mieux.", "celle"),
        ("Les personnages ___ qu'on voit au début reviennent au dernier tome.", "ceux"),
        ("Prenez ___ qui a la couverture bleue : c'est le premier tome.", "celui"),
        ("Les bulles ___ qui ont une pointe en petits ronds sont des pensées.", "celles"),
        ("La série ___ que Nadia recommande compte quatre albums.", "celle"),
    ], corrige=True,
       notes="C'est l'exercice `t2demo` du module interactif. Faire dire à chaque fois le "
             "nom remplacé avant de donner la réponse : « albums, masculin pluriel… non, "
             "un seul, masculin singulier : celui ». C'est le raisonnement qu'on veut "
             "installer.")

    d.piege("Accorder avec ce qui suit",
            "J'ai lu deux albums ; celle que je préfère est le deuxième.",
            "J'ai lu deux albums ; celui que je préfère est le deuxième.",
            "L'accord se fait avec le nom remplacé — album, masculin —, jamais avec le "
            "verbe ni avec le sujet de la relative. Cherchez toujours le nom d'abord : "
            "il est souvent deux ou trois mots plus tôt.",
            notes="Faire souligner le nom remplacé au crayon dans les six phrases de "
                  "l'exercice. Le geste vaut mieux que la règle : là où le nom est "
                  "souligné, la faute ne se produit plus.")

    d.pratique('À l\'oral', "Désignez sans nommer",
               "Deux par deux, trois livres sur la table.", [
        ("Désignez un livre sans dire son titre et sans le montrer du doigt.",),
        ("Votre voisin doit le prendre. S'il se trompe, précisez autrement.",),
        ("Recommencez avec une planche, puis avec un personnage.",),
        ("Faites une phrase avec « ceux de… » ou « celles de… ».",),
    ], notes="Exercice court et vivant. La deuxième consigne est la vraie : quand le voisin "
             "se trompe, l'élève doit ajouter une caractéristique, donc produire une "
             "seconde relative. C'est là que la structure s'installe.")

    d.billet(
        "Écrivez deux phrases qui comparent deux œuvres, avec « celui » ou « celle ».",
        exemples=[
            "« J'ai lu deux romans ; celui que je préfère est… »",
            "« Cette planche-ci est belle, mais celle de la fin… »",
        ],
        notes="Les deux phrases servent directement à la production écrite du bloc E, où "
              "l'élève compare souvent son œuvre à une autre. Relire les billets : "
              "l'accord est le point à vérifier, et il se voit d'un coup d'œil.")

    return d.save(dossier)
