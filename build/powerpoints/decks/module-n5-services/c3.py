# -*- coding: utf-8 -*-
"""C3 · À quoi renvoie ce mot ?
Bloc C « Défi 2 · L'écran » · couleur acier · 75 min. Compréhension écrite.
Source : exercice `t2rep` et sa mini-leçon.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C3', section='acier',
        titre="À quoi renvoie ce mot ?",
        chapeau="Un règlement ne répète pas vingt fois « la demande de carte "
                "de citoyenne ». Il écrit « celle-ci ». Le texte devient "
                "court — et difficile, parce qu'il faut se rappeler à tout "
                "moment de quoi on parle.",
        duree='75 minutes')

    d.titre(notes="Séance de compréhension écrite. Ramasser le devoir C2 et lire trois "
                  "descriptions à voix haute : elles montrent où en sont les relatifs, "
                  "qui reviennent aujourd'hui comme forme de reprise.")

    d.objectifs([
        "repérer les quatre formes de reprise dans un texte officiel ;",
        "remonter à ce qu'un pronom remplace ;",
        "savoir que « ce dernier » désigne le plus proche ;",
        "remplacer « y » et « en » par le groupe complet pour vérifier.",
    ])

    d.declencheur(
        'Lecture', "Deux phrases. De quoi parle la seconde ?",
        pistes=[
            "« Apportez une preuve de résidence. »",
            "« Celle-ci doit dater de moins de trois mois. »",
            "Qu'est-ce que « celle-ci » remplace ?",
            "Comment l'avez-vous su ?",
        ],
        notes="Le groupe trouve vite. Faire expliciter la méthode : on remonte à la "
              "phrase précédente. C'est toute la séance, et il vaut mieux qu'ils la "
              "formulent eux-mêmes.")

    d.regle("Quand un mot vous arrête, remontez",
            "Ce qu'il reprend est presque toujours dans la phrase précédente.",
            precision="Ou dans le titre juste au-dessus. Si vous devez remonter plus loin "
                      "qu'un paragraphe, c'est probablement le texte qui est mal écrit — "
                      "pas vous qui lisez mal. Le dire libère beaucoup d'élèves.",
            notes="Diapositive à photographier. La deuxième phrase de la précision est "
                  "importante pour la confiance du groupe : ne pas la sauter.")

    d.tableau('Les quatre formes de reprise', "Elles font toutes la même chose",
              ['Forme', 'Exemple'],
              [["un pronom", "elle, la, y, en"],
               ["un synonyme", "la demande, puis la requête"],
               ["un mot général", "le bac, le bidon, la boîte, repris par « ces contenants »"],
               ["un démonstratif", "ce document, cette pièce, ces matières"]],
              cle=0,
              note="Toutes renvoient plus haut. Aucune n'apporte d'information nouvelle.",
              notes="Diapositive à photographier. La note du bas est utile : un élève qui "
                    "cherche du nouveau dans une reprise perd son temps.")

    d.cartes("Les deux plus glissants", "Ils désignent le plus proche", [
        ("ce dernier",
         "Le dernier nommé. « Le formulaire et le reçu ; ce dernier peut être une photo. » Il s'agit du reçu."),
        ("celui-ci, celle-ci",
         "Le plus proche, pas le plus important. Dans un texte officiel, presque toujours celui d'avant."),
        ("celui-là, celle-là",
         "Le plus éloigné. Rare dans une page de service."),
        ("Le contresens qui coûte cher",
         "Croire que « ce dernier » désigne le sujet principal du paragraphe."),
    ], notes="La dernière carte mérite un exemple au tableau : une consigne mal comprise "
             "sur ce point fait apporter le mauvais document au guichet.")

    d.tableau('Y et en', "Deux petits mots qui portent beaucoup",
              ['Mot', 'Il reprend', 'Exemple'],
              [["y", "un lieu, ou « à quelque chose »", "l'écocentre : on y apporte les vieux appareils"],
               ["en", "« de quelque chose »", "des visites gratuites : vous en avez quatre"]],
              cle=0,
              note="Le test : remplacez par le groupe complet et relisez. La phrase redevient claire.",
              notes="Diapositive à photographier. Faire pratiquer le test à voix haute sur "
                    "les deux exemples : c'est un geste, pas une connaissance.")

    d.pratique('Reprise', "À quoi renvoie le mot souligné ?",
               "Remontez et répondez.", [
        ("« Apportez une preuve de résidence. Celle-ci doit dater de moins de trois mois. »",
         "la preuve de résidence"),
        ("« L'écocentre ouvre à neuf heures. On y apporte les vieux appareils. »",
         "à l'écocentre"),
        ("« Vous avez droit à quatre visites. Vous en avez utilisé deux. »",
         "des visites gratuites"),
        ("« Joignez le formulaire et le reçu ; ce dernier peut être une photo. »",
         "le reçu — le dernier nommé"),
        ("« Votre demande a été enregistrée. Cette requête porte le numéro 24-118-7690. »",
         "la demande enregistrée"),
        ("« Peinture, huile, piles : ces matières ne vont jamais dans un bac. »",
         "la peinture, l'huile et les piles"),
    ], corrige=True,
       notes="Faire lire chaque paire à voix haute par un élève, puis demander à un autre "
             "de répondre. La lecture à voix haute fait déjà la moitié du travail.")

    d.piege("Lire par-dessus les pronoms",
            "Je continue, je comprends l'idée générale.",
            "Je m'arrête une seconde sur « celle-ci » et je remonte.",
            "On croit avoir compris, et on rate la condition. « Celle-ci doit dater de "
            "moins de trois mois » : si on n'a pas vu que c'était la preuve de résidence, "
            "on apporte un bail de trois ans et on repart bredouille.",
            notes="C'est l'erreur de lecture la plus coûteuse du module. Lui donner du "
                  "temps : elle explique la moitié des deuxièmes visites au guichet.")

    # `capture` n'existe que dans theme.Deck : les présentations la portent, les
    # fiches imprimées non (build/powerpoints/fiche.py n'a pas la méthode). Une
    # fiche noir et blanc n'a de toute façon rien à faire d'une capture d'écran.
    if hasattr(d, 'capture'):
        d.capture('t2rep', "L'exercice à l'écran",
                  consigne="Reliez chaque mot souligné à ce qu'il reprend.",
                  notes="Dix minutes de travail individuel. La mini-leçon développe les quatre "
                        "formes de reprise et le piège de « ce dernier ».")

    d.billet(
        "Sur la page que vous avez trouvée au devoir C1, relevez trois reprises.",
        exemples=[
            "Un pronom, un démonstratif, un « y » ou un « en ».",
            "Pour chacun, écrivez ce qu'il remplace.",
        ],
        notes="Devoir en continuité directe avec C1 : la même page sert deux fois, ce qui "
              "montre qu'une page officielle se travaille en plusieurs passages.")

    return d.save(dossier)
