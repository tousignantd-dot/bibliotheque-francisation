# -*- coding: utf-8 -*-
"""A3 · Les quatre éléments d'une publicité.
Bloc A · couleur acier (compréhension) · 60 min.
Source : exercice `prPub` — l'affiche de l'Atelier Roues Libres.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A3', section='acier',
        titre="Les quatre éléments d'une publicité",
        chapeau="Qui parle, à qui, pour dire quoi, et par quel moyen. Quatre questions "
                "qui permettent de démonter n'importe quelle publicité — celles du "
                "quartier comme celles de la télévision.",
        duree='60 minutes')

    d.titre(notes="Séance d'analyse. Apporter deux ou trois vraies publicités : un "
                  "dépliant, une affiche, une page de journal. Les élèves les "
                  "démonteront à la fin.")

    d.objectifs([
        "nommer l'émetteur, le récepteur, le message et le canal ;",
        "trouver ces quatre éléments dans une affiche ;",
        "distinguer ce qui est dit de ce qui est sous-entendu ;",
        "reconnaître le canal choisi et son effet.",
    ])

    d.tableau('Analyse', "Les quatre éléments",
              ["L'élément", 'La question'],
              [["l'émetteur", "qui envoie le message ?"],
               ["le récepteur", "à qui s'adresse-t-il ?"],
               ["le message", "qu'est-ce qu'on annonce ?"],
               ["le canal", "par quel moyen le message circule-t-il ?"]],
              cle=0,
              note="Le récepteur est le seul des quatre qui n'est presque jamais écrit. "
                   "Il faut le déduire.",
              notes="Écrire les quatre au tableau et les y laisser tout le module. C'est "
                    "la grille d'analyse de toutes les séances.")

    d.cartes("L'affiche", "L'Atelier Roues Libres", [
        ("Le texte",
         "« L'Atelier Roues Libres ouvre sa clinique de printemps. Apportez votre vélo : "
         "nos mécaniciens bénévoles vous montreront à régler vos freins et à graisser "
         "votre chaîne. »"),
        ("La suite",
         "« Le samedi 26 avril, de 10 h à 15 h, dans le stationnement de l'école "
         "Saint-Fidèle. Entrée libre. »"),
        ("Ce qu'on remarque d'abord",
         "L'organisme se nomme dès le premier mot. C'est presque toujours le cas : "
         "l'émetteur signe son message."),
        ("Ce qu'il faut déduire",
         "Le récepteur n'est pas nommé. C'est en lisant « apportez votre vélo » qu'on "
         "comprend à qui l'affiche parle."),
    ], notes="Faire lire l'affiche en silence avant d'afficher les deux dernières cartes. "
             "Ce sont elles qui enseignent.")

    d.regle('La règle',
            "Le récepteur se déduit du message, il est rarement écrit.",
            precision="Une affiche ne dit pas « ce message s'adresse aux gens qui ont un "
                      "vélo ». Elle dit « apportez votre vélo » — et c'est ainsi qu'on "
                      "sait à qui elle parle. Cherchez les verbes à l'impératif et les "
                      "possessifs.",
            notes="Diapo centrale. Faire chercher « votre vélo », « vos freins », « votre "
                  "chaîne » : trois indices du récepteur.")

    d.pratique('Pratique · 1 de 4', "Les quatre éléments de l'affiche",
               "D'après l'affiche de l'Atelier Roues Libres.", [
        ("Quel organisme envoie ce message ?", "l'Atelier Roues Libres"),
        ("À qui l'affiche s'adresse-t-elle ?", "aux gens du quartier qui ont un vélo"),
        ("Qu'est-ce qu'on annonce exactement ?",
         "une clinique où des bénévoles montrent à régler ses freins et graisser sa chaîne"),
        ("Par quel moyen le message est-il diffusé ?", "par une affiche"),
    ], corrige=True,
       notes="Faire pointer, pour chaque réponse, ce qui l'a permis dans le texte. Le "
             "récepteur demandera une déduction.")

    d.pratique('Pratique · 2 de 4', "Les informations pratiques",
               "Quand, où, à quelles conditions ?", [
        ("Quel jour et à quelle heure ?", "le samedi 26 avril, de 10 h à 15 h"),
        ("À quel endroit ?", "dans le stationnement de l'école Saint-Fidèle"),
        ("Combien ça coûte ?", "rien — entrée libre"),
        ("Qu'est-ce qu'il faut apporter ?", "son vélo"),
    ], corrige=True,
       notes="Ces quatre informations sont le minimum vital d'une affiche. Les faire "
             "vérifier dans les vraies publicités apportées en classe.")

    d.tableau('Analyse', "Quatre canaux et leur longueur",
              ['Le canal', 'La longueur possible'],
              [["la capsule radio", "trente secondes, une seule idée"],
               ["l'affiche", "un coup d'œil, toutes les informations pratiques"],
               ["l'infolettre", "un paragraphe, avec un lien pour en savoir plus"],
               ["le bouche-à-oreille", "aussi long qu'on veut, mais peu de gens"]],
              cle=0, props=[0.35, 0.65],
              note="Chaque canal a sa longueur. C'est pour ça qu'Omar dit à Solange : "
                   "« le reste, tu l'écriras sur l'affiche ».",
              notes="Le lien avec A1 est direct. Le faire remarquer : ce n'est pas moins "
                    "d'information, c'est une autre répartition.")

    d.pratique('Pratique · 3 de 4', "Quel canal pour quel message ?",
               "Et pourquoi celui-là ?", [
        ("Annoncer un atelier à tout le quartier, vite.", "la radio communautaire"),
        ("Donner l'heure, l'adresse et le prix.", "l'affiche, qu'on peut relire"),
        ("Rejoindre les gens qui sont déjà venus.", "l'infolettre"),
        ("Convaincre un voisin qui hésite.", "le bouche-à-oreille"),
    ], corrige=True,
       notes="Faire remarquer qu'une vraie campagne emploie plusieurs canaux, chacun pour "
             "ce qu'il fait le mieux.")

    d.piege("Le piège du récepteur « tout le monde »",
            "Cette affiche s'adresse à tout le monde.",
            "Elle s'adresse aux gens du quartier qui ont un vélo.",
            "Aucune publicité ne s'adresse à tout le monde, même celles qui en ont "
            "l'air. Cherchez les indices : un objet nommé, un lieu, une heure, un prix. "
            "Chacun réduit le public visé, et c'est voulu.",
            notes="Faire chercher le récepteur de trois vraies publicités. Il est "
                  "toujours plus précis qu'il n'en a l'air.")

    d.pratique('Pratique · 4 de 4', "Démontez une publicité",
               "Une vraie publicité, apportée en classe.", [
        ("L'émetteur", "qui signe le message ?"),
        ("Le récepteur", "quels indices vous l'ont fait deviner ?"),
        ("Le message", "en une phrase"),
        ("Le canal", "et pourquoi celui-là ?"),
    ], corrige=False,
       notes="Quinze minutes, en équipes de deux. Chaque équipe présente sa publicité au "
             "groupe en une minute.")

    d.billet(
        "Choisissez une publicité vue cette semaine et nommez ses quatre éléments.",
        exemples=[
            "L'émetteur, le récepteur, le message, le canal.",
            "Une ligne chacun.",
        ],
        notes="Ramasser. Les publicités choisies par le groupe sont souvent plus "
              "intéressantes que celles du module : en garder quelques-unes.")

    return d.save(dossier)
