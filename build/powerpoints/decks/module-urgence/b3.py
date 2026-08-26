# -*- coding: utf-8 -*-
"""B3 · Je me suis brûlé : les verbes pronominaux au passé.
Bloc B · couleur ambre (écriture) · 75 min.
Source : exercice `t1pron` et sa mini-leçon.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B3', section='ambre',
        titre='Je me suis brûlé',
        chapeau="Quand on se blesse soi-même, le français ajoute un petit mot devant le "
                "verbe. Et cet ajout change l'auxiliaire, puis l'accord. Trois "
                "conséquences pour deux lettres.",
        duree='75 minutes')

    d.titre(notes="Écrire au tableau les deux phrases : « L'huile a brûlé son bras » et "
                  "« Elle s'est brûlé le bras ». Demander la différence. Le groupe "
                  "trouvera « c'est elle-même » : c'est exactement la leçon.")

    d.objectifs([
        "reconnaître un verbe pronominal ;",
        "le conjuguer au passé composé avec être ;",
        "accorder le participe avec le sujet ;",
        "savoir quand l'accord ne se fait pas.",
    ])

    d.regle('La règle',
            "Un verbe pronominal se conjugue toujours avec être au passé composé.",
            precision="Je me suis brûlé. Il s'est coupé. Nous nous sommes lavés. Jamais "
                      "avoir, dans aucun cas. C'est la seule règle du français où il n'y "
                      "a pas d'exception à retenir.",
            notes="Bonne nouvelle à annoncer comme telle : après la difficulté du choix "
                  "d'auxiliaire en B2, ici il n'y a rien à choisir.")

    d.tableau('Analyse', "Se brûler au passé composé",
              ['La personne', 'Le pronom', 'La forme'],
              [["je", "me", "je me suis brûlé"],
               ["tu", "te", "tu t'es brûlé"],
               ["il, elle", "se", "elle s'est brûlée"],
               ["nous", "nous", "nous nous sommes brûlés"],
               ["vous", "vous", "vous vous êtes brûlés"]],
              cle=1,
              notes="Le pronom change avec la personne : me, te, se, nous, vous, se. "
                    "C'est la seule partie qui demande de la mémoire.")

    d.regle("La règle d'accord",
            "Le participe s'accorde avec le sujet — sauf si une partie du corps suit.",
            precision="« Elle s'est blessée » : accord. « Elle s'est blessé le bras » : "
                      "pas d'accord, parce que « le bras » vient après. Dès qu'un "
                      "complément suit le participe, l'accord disparaît.",
            notes="Diapo la plus difficile du module. Y consacrer le temps qu'il faut, "
                  "et accepter que tout le monde ne la maîtrise pas à la fin.")

    d.tableau('Analyse', "Avec ou sans accord",
              ['La phrase', 'Accord ?', 'Pourquoi'],
              [["Elle s'est blessée.", "oui", "rien après le participe"],
               ["Elle s'est blessé le bras.", "non", "« le bras » suit"],
               ["Ils se sont coupés.", "oui", "rien après"],
               ["Ils se sont coupé le doigt.", "non", "« le doigt » suit"]],
              cle=1,
              note="Le test tient en une question : y a-t-il quelque chose juste après le "
                   "participe ? Si oui, pas d'accord.",
              notes="Faire appliquer le test à voix haute sur les quatre lignes. C'est "
                    "un test mécanique : il ne demande pas de comprendre pourquoi.")

    d.cartes('Ouvrir la mini-leçon', "Quatre verbes pronominaux du travail", [
        ("se blesser",
         "Le mot général : « je me suis blessé au travail ». C'est celui à employer "
         "quand on remplit une déclaration d'accident."),
        ("se couper",
         "Avec un objet tranchant. « Je me suis coupé le doigt en préparant les "
         "légumes. »"),
        ("se brûler",
         "Avec la chaleur. « Elle s'est brûlé l'avant-bras avec de l'huile chaude. »"),
        ("se tordre",
         "Une articulation qui part de travers. « Il s'est tordu la cheville dans "
         "l'escalier. »"),
    ], notes="Ces quatre verbes couvrent la grande majorité des accidents de travail. "
             "Les faire employer chacun dans une phrase complète.")

    d.pratique('Pratique · 1 de 3', "Écrivez le verbe pronominal au passé composé",
               "L'auxiliaire est toujours être.", [
        ("Je (se brûler) ___ l'avant-bras.", "me suis brûlé — pas d'accord, « l'avant-bras » suit"),
        ("Elle (se couper) ___ en préparant les légumes.", "s'est coupée — accord"),
        ("Ils (se blesser) ___ au travail.", "se sont blessés — accord"),
        ("Nous (se laver) ___ les mains avant les soins.", "nous sommes lavé les mains"),
        ("Il (se tordre) ___ la cheville.", "s'est tordu la cheville — pas d'accord"),
    ], corrige=True,
       notes="Faire chercher, pour chaque item, s'il y a un complément après le "
             "participe. C'est la seule question à se poser.")

    d.piege("Le piège de la partie du corps",
            "Elle s'est brûlée le bras.",
            "Elle s'est brûlé le bras.",
            "Quand la partie du corps est écrite après le participe, l'accord ne se fait "
            "pas. C'est contre-intuitif : on voit « elle », on veut accorder. Mais le "
            "français accorde avec ce qui précède, et ici la partie du corps suit.",
            notes="Cette diapo mérite dix minutes. Écrire les deux versions au tableau et "
                  "faire appliquer le test par cinq élèves différents.")

    d.piege("Le piège de l'auxiliaire",
            "Je m'ai brûlé le bras.",
            "Je me suis brûlé le bras.",
            "Un verbe pronominal ne prend jamais avoir. Cette erreur vient souvent de la "
            "langue maternelle, où l'auxiliaire est le même dans les deux cas. En "
            "français, le petit pronom impose être, sans exception.",
            notes="Erreur très fréquente et très audible. La corriger systématiquement à "
                  "l'oral, dès la première occurrence, pendant tout le reste du module.")

    d.pratique('Pratique · 2 de 3', "Accord ou pas d'accord ?",
               "Appliquez le test : y a-t-il un complément après le participe ?", [
        ("Elle s'est coupé___ .", "coupée — accord, rien ne suit"),
        ("Elle s'est coupé___ le doigt.", "coupé — pas d'accord, « le doigt » suit"),
        ("Ils se sont brûlé___ .", "brûlés — accord"),
        ("Ils se sont brûlé___ les mains.", "brûlé — pas d'accord"),
        ("Nous nous sommes blessé___ au travail.", "blessés — « au travail » n'est pas un complément direct"),
    ], corrige=True,
       notes="Le cinquième item est le plus fin : « au travail » indique le lieu, pas "
             "l'objet. L'accord se fait. Le signaler sans en faire une règle nouvelle.")

    d.pratique('Pratique · 3 de 3', "Racontez l'accident",
               "Une phrase par situation, avec un verbe pronominal au passé composé.", [
        ("Une coupure au doigt avec un couteau",
         "Je me suis coupé le doigt avec un couteau."),
        ("Une brûlure à la main avec de l'eau bouillante",
         "Elle s'est brûlé la main avec de l'eau bouillante."),
        ("Une cheville tordue dans un escalier",
         "Il s'est tordu la cheville dans l'escalier."),
        ("Deux collègues blessés en déchargeant un camion",
         "Ils se sont blessés en déchargeant un camion."),
    ], corrige=True,
       notes="Le quatrième item n'a pas de partie du corps : l'accord se fait. C'est le "
             "contraste qui installe la règle.")

    d.billet(
        "Écrivez deux phrases avec un verbe pronominal au passé composé.",
        exemples=[
            "Une avec une partie du corps après le participe, une sans.",
            "Soulignez le participe et écrivez à côté : accord, ou pas d'accord.",
        ],
        notes="Corriger surtout la présence de l'auxiliaire être. L'accord viendra plus "
              "tard ; l'auxiliaire, lui, doit être acquis avant la fin du module.")

    return d.save(dossier)
