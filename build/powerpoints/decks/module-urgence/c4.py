# -*- coding: utf-8 -*-
"""C4 · Les examens, les soins et la fiche brûlure.
Bloc C · couleur framboise (vocabulaire) · 75 min.
Source : exercices `t2exam`, `t2consult` et `t2fiche`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C4', section='framboise',
        titre='Les examens et les soins',
        chapeau="Radiographie, prise de sang, points de suture, vaccin contre le tétanos. "
                "Quatre mots qu'on entend à l'urgence, et qu'il vaut mieux comprendre "
                "avant de dire oui.",
        duree='75 minutes')

    d.titre(notes="Séance de vocabulaire technique. Beaucoup d'élèves reconnaissent les "
                  "gestes sans connaître les mots français. Partir de ce qu'ils "
                  "connaissent.")

    d.objectifs([
        "nommer cinq examens ou soins courants à l'urgence ;",
        "comprendre ce que chacun sert à vérifier ou à réparer ;",
        "connaître les bons gestes en cas de brûlure ;",
        "savoir ce qu'il ne faut jamais faire.",
    ])

    d.tableau('Analyse', "Cinq examens et soins",
              ['Le mot', 'Ce que c\'est'],
              [["une radiographie", "une image des os"],
               ["une prise de sang", "un prélèvement pour analyser le sang"],
               ["des points de suture", "des fils pour refermer une plaie"],
               ["un vaccin contre le tétanos", "une injection après une blessure salissante"],
               ["un pansement stérile", "une protection propre posée sur la plaie"]],
              cle=0,
              note="Ces cinq mots reviennent dans toute visite à l'urgence, quelle que "
                   "soit la blessure.",
              notes="Faire dire pour chacun : est-ce que ça fait mal ? Les réponses "
                    "honnêtes rassurent plus que les réponses rassurantes.")

    d.cartes('Ouvrir la mini-leçon', "Quatre choses sur les points de suture", [
        ("Ils se posent vite",
         "Une plaie doit être refermée dans les six à huit heures. Passé ce délai, le "
         "risque d'infection est trop grand et on la laisse ouverte."),
        ("Ils se retirent",
         "Entre cinq et quatorze jours selon l'endroit du corps. Il faut retourner à "
         "la clinique : ils ne tombent pas tout seuls."),
        ("La colle existe aussi",
         "Pour les petites plaies, on emploie parfois une colle médicale ou des "
         "bandelettes. Moins impressionnant, aussi efficace."),
        ("Le tétanos va avec",
         "Une plaie sale ou profonde demande un rappel du vaccin si le dernier date de "
         "plus de dix ans. Personne ne s'en souvient : dites-le et on vérifiera."),
    ], notes="La deuxième carte est la plus utile : beaucoup de gens ne retournent pas "
             "faire retirer leurs points, et la peau se referme dessus.")

    d.tableau('Analyse', "La fiche-conseil sur les brûlures",
              ['Le moment', 'Ce qu\'il faut faire'],
              [["tout de suite", "retirer bagues et bracelets, eau fraîche 15 minutes"],
               ["à ne jamais faire", "percer les cloques, glace, beurre, dentifrice"],
               ["couvrir", "un pansement stérile, sans serrer"],
               ["consulter", "cloques, grande surface, visage ou mains"],
               ["après", "protéger du soleil six mois"]],
              cle=0,
              note="Les bagues d'abord : la peau enfle vite, et un anneau devient "
                   "impossible à retirer en quelques minutes.",
              notes="Le geste des bagues est celui que personne ne connaît et qui évite "
                    "le plus de complications. Insister.")

    d.regle('Le geste que personne ne connaît',
            "Retirer bagues, bracelets et montre avant que la peau enfle.",
            precision="Une brûlure enfle dans les minutes qui suivent. Un anneau qui "
                      "serre coupe la circulation, et il faudra le scier à l'hôpital. "
                      "C'est le premier geste, avant même l'eau.",
            notes="Demander qui porte une bague en ce moment. Faire visualiser la scène : "
                  "cela suffit pour que le geste soit retenu.")

    d.pratique('Pratique · 1 de 3', "L'examen et sa description",
               "Reliez chaque examen à ce qu'il est.", [
        ("une radiographie", "une image des os"),
        ("une prise de sang", "un prélèvement pour analyser le sang"),
        ("des points de suture", "des fils pour refermer une plaie"),
        ("un vaccin contre le tétanos", "une injection après une blessure salissante"),
        ("un pansement stérile", "une protection propre posée sur la plaie"),
    ], corrige=True, cols=2,
       notes="Exercice rapide de reconnaissance. Enchaîner sur la mise en situation.")

    d.pratique('Pratique · 2 de 3', "La consultation de monsieur Nguyen",
               "Il s'est coupé la main en réparant une clôture. Plaie profonde et sale.", [
        ("Comment monsieur Nguyen s'est-il blessé ?",
         "Il s'est coupé la main en réparant une clôture."),
        ("Quels soins a-t-il reçus à l'urgence ?",
         "Quatre points de suture et un rappel du vaccin contre le tétanos."),
        ("Pourquoi le vaccin contre le tétanos ?",
         "Parce que la plaie était sale et profonde."),
        ("Pourquoi doit-il revenir dans dix jours ?",
         "Pour faire retirer les fils des points de suture."),
    ], corrige=True,
       notes="Lire la situation complète à voix haute deux fois : « Monsieur Nguyen "
             "s'est coupé la main en réparant une clôture. La plaie est profonde et "
             "sale. À l'urgence, on lui fait quatre points de suture et un rappel du "
             "vaccin contre le tétanos. Il doit revenir dans dix jours pour faire "
             "retirer les fils. »")

    d.piege("Le piège de la glace",
            "De la glace sur la brûlure, ça soulage.",
            "De l'eau fraîche qui coule, jamais de glace.",
            "La glace soulage sur le moment, puis elle gèle des tissus déjà abîmés et "
            "aggrave la brûlure en profondeur. C'est l'eau fraîche qui refroidit sans "
            "geler — et elle doit couler, pas stagner dans un bol.",
            notes="Diapo à répéter du module : le geste est contre-intuitif, et une "
                  "seule présentation ne suffit pas à défaire l'habitude.")

    d.pratique('Pratique · 3 de 3', "Vrai ou faux — la fiche brûlure",
               "D'après la fiche-conseil.", [
        ("Il faut retirer les bagues avant que la peau enfle.", "VRAI"),
        ("Mettre de la glace directement sur la brûlure est recommandé.", "FAUX"),
        ("L'eau fraîche doit couler pendant quinze minutes.", "VRAI"),
        ("On peut percer les cloques si elles gênent.", "FAUX — jamais"),
        ("Une brûlure au visage demande de consulter.", "VRAI"),
        ("Il faut protéger la peau du soleil pendant six mois.", "VRAI"),
    ], corrige=True,
       notes="Ces six énoncés sont le cœur du savoir de sécurité du module. Les faire "
             "reprendre à voix haute, en chœur, dans leur version juste.")

    d.billet(
        "Écrivez la fiche-conseil sur les brûlures, de mémoire, en cinq lignes.",
        exemples=[
            "Tout de suite · à ne jamais faire · couvrir · consulter · après.",
            "Une ligne par rubrique, avec les chiffres.",
        ],
        notes="Ramasser. Une fiche complète et juste vaut mieux qu'un examen : c'est un "
              "savoir qui peut servir le soir même, à la maison.")

    return d.save(dossier)
