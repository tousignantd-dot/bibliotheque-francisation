# -*- coding: utf-8 -*-
"""A4 · Inconvénient normal ou trouble de voisinage ?
Bloc A « Je découvre » · couleur teal · écoute et réponds · 75 min.
Source : exercices `prNorm` et `prImg`, et la mini-leçon `prNorm`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A4', section='teal',
        titre="Inconvénient normal ou trouble de voisinage ?",
        chapeau="Habiter près des autres coûte quelque chose à tout le monde. "
                "Quatre questions décident de ce qui dépasse : l'heure, la "
                "durée, la répétition, l'endroit.",
        duree='75 minutes')

    d.titre(notes="Dernière séance du bloc A. Elle ferme la question posée en A1 par "
                  "Ruslana : « est-ce que j'ai le droit de me plaindre ? »")

    d.objectifs([
        "nommer les quatre critères qui font la limite ;",
        "classer huit situations d'un côté ou de l'autre ;",
        "expliquer pourquoi la faute du voisin n'entre pas dans la balance ;",
        "dire pourquoi la répétition compte plus que la force du bruit.",
    ], notes="Le troisième objectif est celui qui déloge la colère : on peut causer un "
             "trouble sans rien faire de mal, et c'est le cas le plus fréquent.")

    d.declencheur(
        'Observation', "Un enfant qui court dix minutes : normal ou pas normal ?",
        pistes=[
            "Et à quelle heure ?",
            "Et si c'est tous les jours pendant deux mois ?",
            "Et si c'est dans un triplex du centre plutôt qu'en campagne ?",
            "Qu'est-ce qui a changé dans ta réponse ?",
        ],
        notes="Faire varier une seule chose à la fois : l'heure, puis la durée, puis "
              "la répétition, puis l'endroit. Le groupe découvre les quatre critères "
              "sans qu'on les nomme.")

    d.cartes('Analyse', "Les quatre questions, dans cet ordre", [
        ("1. L'heure", "Le même bruit ne pèse pas pareil à 19 h et à 5 h 45. La nuit va de 23 h à 7 h."),
        ("2. La durée", "Trois minutes se supportent. Quarante minutes, non — et ce n'est pas la même chose en plus long."),
        ("3. La répétition", "Le critère le plus fort. Un événement isolé n'est presque jamais un trouble."),
        ("4. L'endroit", "On n'attend pas le même calme dans un triplex du centre que dans une maison isolée."),
    ], notes="Diapositive à photographier. Retenir l'ordre : c'est celui dans lequel on "
             "les écrit dans une lettre, au bloc D.")

    d.regle("La faute n'entre pas dans la balance",
            "On peut causer un trouble de voisinage sans rien faire de mal.",
            precision="Ce qui compte est l'effet du bruit sur le voisin, mesuré à "
                      "l'heure, à la durée et à la répétition — jamais l'intention de "
                      "celui qui le fait. Chercher un coupable fait perdre du temps et "
                      "ferme la conversation avant qu'elle commence.",
            notes="Diapositive à photographier. C'est la phrase qui rend le bloc B "
                  "possible : on monte parler à quelqu'un qui n'a rien fait de mal.")

    d.tableau('Analyse', "Huit situations, deux colonnes",
              ['Inconvénient normal', 'Trouble de voisinage'],
              [["Des pas de 18 h à 21 h", "Un tapis roulant à 5 h 45, quinze matins"],
               ["Une fête une fois par an", "De la musique toutes les nuits, un mois"],
               ["Une porte qui claque le soir", "Un chien qui jappe seul huit heures"],
               ["Un enfant qui court dix minutes", "Des travaux dès 6 h, trois semaines"]],
              notes="Faire justifier chaque classement par un des quatre critères, à "
                    "voix haute. Une réponse sans critère ne compte pas.")

    d.piege('Méthode',
            "Attendre d'être à bout pour commencer à noter",
            "Noter dès le troisième jour",
            "Un registre qui commence le jour où l'on craque commence trop tard : il "
            "ne couvre pas les six semaines qui comptent. Trente secondes par matin — "
            "la date, l'heure du début, l'heure de la fin, ce qu'on entend — et rien "
            "de plus : ni commentaire, ni adjectif.",
            notes="Faire fabriquer le tableau du registre au tableau, en quatre "
                  "colonnes. Ceux qui vivent la situation peuvent commencer ce soir.")

    d.pratique('Pratique', "Normal ou pas normal ?",
               "Classez chaque situation, puis nommez le critère qui décide.", [
        ("Des pas au-dessus de la tête, de 18 h à 21 h, tous les jours.", "inconvénient normal - l'heure"),
        ("Un tapis roulant de 5 h 45 à 6 h 25, quinze matins de suite.", "trouble - l'heure et la répétition"),
        ("Une fête bruyante un samedi soir, une fois dans l'année.", "inconvénient normal - la répétition"),
        ("Un chien qui jappe seul six à huit heures par jour, depuis deux mois.", "trouble - la durée et la répétition"),
        ("Une porte d'entrée qui claque quand quelqu'un rentre le soir.", "inconvénient normal"),
        ("Des travaux de rénovation dès six heures, pendant trois semaines.", "trouble - l'heure et la durée"),
    ], corrige=True,
       notes="Le cinquième déclenche toujours un débat. Y laisser deux minutes : c'est "
             "la meilleure façon de faire sentir où passe la limite.")

    d.billet(
        "Dans ton immeuble, nomme un inconvénient normal et un qui ne l'est pas.",
        exemples=[
            "Dis à chaque fois quel critère décide.",
            "Si tu n'en as pas, invente une situation plausible.",
        ],
        notes="Deux minutes. Fin du bloc A : le groupe sait maintenant nommer le "
              "problème. Le bloc B lui apprend à en parler.")

    return d.save(dossier)
