# -*- coding: utf-8 -*-
"""E1 · Raconte le film à quelqu'un qui ne l'a pas vu
Bloc E « Je me lance » · couleur teal · 75 min.
Source : bloc « Je me lance » du module — jeu de rôle `cineclub` et
production orale.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='E1', section='teal',
        titre="Raconte le film à quelqu'un qui ne l'a pas vu",
        chapeau="Quatre-vingt-dix secondes : de quel film il s'agit, le "
                "déroulement dans l'ordre et sans la fin, puis ce qui t'a "
                "convaincu et ce qui t'a moins convaincu.",
        duree='75 minutes')

    d.titre(notes="Avant-dernière séance. Tout ce qui a été appris depuis quatre "
                  "semaines se joue ici, à l'oral. Prévoir des écouteurs : "
                  "l'enregistrement se fait dans la salle, tout le monde en même "
                  "temps.")

    d.objectifs([
        "raconter le déroulement d'un film dans l'ordre de l'histoire ;",
        "placer les retours en arrière avec le plus-que-parfait ;",
        "ne pas dévoiler le dénouement, même si on le demande ;",
        "donner un avis nuancé, appuyé sur un moment précis.",
    ], notes="Le troisième objectif est une consigne de politesse autant que de "
             "langue. La tenir jusqu'au bout, y compris entre élèves.")

    d.declencheur(
        'Observation', "Comment raconte-t-on un film sans le gâcher ?",
        pistes=[
            "Jusqu'où peut-on aller sans dévoiler la fin ?",
            "Faut-il raconter dans l'ordre du film, ou dans l'ordre de l'histoire ?",
            "Que fais-tu si l'autre te demande comment ça finit ?",
            "As-tu déjà eu un film gâché par quelqu'un ?",
        ],
        notes="La dernière piste fait parler tout le monde. Elle sert : après cette "
              "discussion, personne ne raconte le dénouement.")

    d.cartes("Le plan en trois temps", "Quatre-vingt-dix secondes, pas plus", [
        ("TEMPS 1 - De quoi il s'agit",
         "le titre, le genre, et où tu l'as vu. Deux phrases suffisent."),
        ("TEMPS 2 - Le déroulement",
         "dans l'ordre de l'histoire, avec les retours en arrière placés."),
        ("TEMPS 3 - Ton avis",
         "une chose qui t'a convaincu, une chose qui t'a moins convaincu."),
        ("Ce qu'on ne dit pas",
         "le dénouement. Jamais, même si on te le demande deux fois."),
    ], notes="Ce plan est celui de l'activité interactive, à l'identique. Le faire "
             "copier au tableau et l'y laisser pendant tout l'enregistrement.")

    d.tableau('Analyse', "Ce qu'on réutilise, et d'où ça vient",
              ['Ce que tu emploies', 'Vu en'],
              [["le plus-que-parfait", "B3 - elle avait pris l'autobus du matin"],
               ["l'imparfait", "B4 - elle vidait la cuisine quand..."],
               ["les marqueurs de temps", "B4 - la veille, le lendemain, dès"],
               ["« où »", "C4 - le village où elle avait grandi"],
               ["accorder un point", "D2 - c'est vrai que..., mais"],
               ["annoncer son avis", "D2 - pour ma part, je trouve que"]],
              cle=0,
              notes="Diapositive à photographier. Elle montre au groupe que rien de "
                    "nouveau n'est demandé : tout a été travaillé, et daté.")

    d.regle("L'ordre de l'histoire, pas l'ordre du film",
            "Le film peut se permettre de mélanger. Toi, non.",
            precision="Un film a l'image pour prévenir : la couleur change, la musique "
                      "s'arrête. Toi, tu n'as que ta voix et tes verbes. Raconte dans "
                      "l'ordre où les choses sont arrivées, et sers-toi du "
                      "plus-que-parfait chaque fois que tu recules d'un cran.",
            notes="Diapositive à photographier. C'est la consigne qui sauve les "
                  "enregistrements : sans elle, la moitié du groupe raconte dans "
                  "l'ordre du film et perd son auditeur en trois phrases.")

    d.pratique('Production orale', "Les sept sujets à couvrir",
               "Cochez au fur et à mesure de votre enregistrement.", [
        ("De quel film il s'agit et où tu l'as vu.", "TEMPS 1"),
        ("Le déroulement dans l'ordre, sans le dénouement.", "TEMPS 2"),
        ("Les retours en arrière placés au bon endroit.", "TEMPS 2"),
        ("Un point accordé avant de répondre.", "TEMPS 3"),
        ("Un jugement appuyé sur un moment précis.", "TEMPS 3"),
        ("Une hypothèse avec « si », sans futur après « si ».", "TEMPS 3"),
    ], corrige=False,
       notes="Ces sept points sont la grille de correction, et ils sont donnés "
             "d'avance : l'élève doit savoir sur quoi il est évalué avant de parler.")

    d.cartes("Le jeu de rôle, d'abord", "Une répétition avant l'enregistrement", [
        ("L'assistant a vu le film",
         "et il l'a trouvé raté. Il a lu la critique et il est d'accord avec elle."),
        ("Il n'est pas hostile",
         "il est déçu, et ses reproches sont précis. Il attend les tiens."),
        ("Il grossit parfois",
         "« il dit que la voisine ne sert à rien » : à toi de relire la phrase exacte."),
        ("Il ne dévoile rien",
         "et il te demandera peut-être la fin. Tiens bon."),
    ], notes="Faire faire le jeu de rôle avant l'enregistrement, sans exception. Les "
             "élèves qui sautent l'étape produisent des comptes rendus deux fois plus "
             "courts.")

    d.piege("Raconter dans l'ordre du film",
            "Elle est au quai avec son frère, puis dans la cuisine, puis au quai.",
            "Son frère est parti en 1978. Aujourd'hui, elle revient vider la maison.",
            "Raconté dans l'ordre du film, le récit devient incompréhensible pour "
            "quelqu'un qui n'a pas les images. Raconté dans l'ordre de l'histoire, il "
            "tient en quatre phrases. C'est le même contenu, et ce n'est pas le même "
            "auditeur qui suit.",
            notes="Faire la démonstration à voix haute, les deux versions de suite. "
                  "Trente secondes chacune, et personne ne raconte plus dans l'ordre "
                  "du film.")

    d.billet(
        "Écris ta première phrase, celle qui ouvre ton enregistrement.",
        exemples=[
            "Une seule phrase, et elle doit contenir le titre.",
            "Par exemple : « J'ai vu... mercredi soir, au ciné-club. »",
        ],
        notes="Deux minutes, avant d'enregistrer. Une première phrase préparée fait "
              "gagner vingt secondes d'hésitation à chaque élève.")

    return d.save(dossier)
