# -*- coding: utf-8 -*-
"""C2 · Lire un avertissement routier.
Bloc C · couleur teal (lire et répondre) · 60 min.
Source : exercices `t2alerte` et `t2pictos`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C2', section='teal',
        titre='Lire un avertissement routier',
        chapeau="Un texte officiel de six lignes, lu sur un téléphone à six heures du "
                "matin. Il dit où, quoi, jusqu'à quand, et ce qu'on doit faire.",
        duree='60 minutes')

    d.titre(notes="Distribuer le texte de l'avertissement et laisser cinq minutes de "
                  "lecture silencieuse avant toute explication.")

    d.objectifs([
        "lire un avertissement routier et en tirer les quatre informations ;",
        "repérer le tronçon de route concerné ;",
        "distinguer une interdiction d'une recommandation ;",
        "lire des prévisions présentées par moments de la journée.",
    ])

    d.cartes('Le texte', "Avertissement de poudrerie", [
        ("Où",
         "Le ministère des Transports diffuse un avertissement de poudrerie pour "
         "l'autoroute 10, entre Sainte-Julie et Marieville."),
        ("Quoi et jusqu'à quand",
         "Des rafales du nord-est réduiront la visibilité par moments jusqu'à demain "
         "matin."),
        ("Ce qu'on doit faire",
         "La route demeure ouverte, mais les camions et les véhicules légers sont "
         "invités à ralentir."),
        ("Les services",
         "Les chasse-neige circulent en continu et un poste de secours est ouvert à la "
         "halte routière du kilomètre 37."),
    ], notes="Quatre blocs, toujours les mêmes dans un avertissement : où, quoi, "
             "consigne, services. Les faire noter.")

    d.regle('La règle de lecture',
            "Cherchez d'abord le tronçon : entre quoi et quoi ?",
            precision="Un avertissement ne vise jamais tout le réseau. « Entre "
                      "Sainte-Julie et Marieville » : si votre trajet ne passe pas là, "
                      "l'avertissement ne vous concerne pas. C'est la première "
                      "information à chercher.",
            notes="Faire tracer le trajet au tableau, avec les deux villes. La notion de "
                  "tronçon devient concrète.")

    d.tableau('Analyse', "Interdiction ou recommandation ?",
              ['La formulation', 'Le degré'],
              [["la route est fermée", "interdiction — on ne passe pas"],
               ["sont invités à ralentir", "recommandation forte"],
               ["il est conseillé de reporter", "recommandation"],
               ["la circulation est interdite aux camions", "interdiction, pour certains"]],
              cle=0, props=[0.45, 0.55],
              note="« Invités à » est une formule polie qui cache une recommandation "
                   "forte : c'est le langage officiel.",
              notes="Lier au module 4, séance B3 : la politesse administrative atténue "
                    "les consignes. Il faut lire la conséquence.")

    d.pratique('Pratique · 1 de 4', "Vrai ou faux",
               "D'après l'avertissement.", [
        ("L'avertissement vise tout le réseau routier du Québec.",
         "FAUX — l'autoroute 10, entre deux villes"),
        ("Les rafales viennent du nord-est.", "VRAI"),
        ("La circulation est interdite sur l'autoroute 10.", "FAUX — la route reste ouverte"),
        ("Les chasse-neige sont déjà à l'œuvre.", "VRAI — en continu"),
        ("Un poste de secours est ouvert au kilomètre 37.", "VRAI"),
    ], corrige=True,
       notes="Le premier et le troisième énoncés généralisent : c'est le piège habituel "
             "des textes officiels. Faire chercher les mots qui limitent.")

    d.pratique('Pratique · 2 de 4', "Les quatre informations",
               "Où, quoi, jusqu'à quand, quelle consigne ?", [
        ("Où ?", "l'autoroute 10, entre Sainte-Julie et Marieville"),
        ("Quoi ?", "de la poudrerie, avec des rafales du nord-est"),
        ("Jusqu'à quand ?", "jusqu'à demain matin"),
        ("Quelle consigne ?", "ralentir — la route reste ouverte"),
        ("Quels services ?", "chasse-neige en continu, poste de secours au km 37"),
    ], corrige=True,
       notes="Faire remplir cette grille sur un vrai avertissement, s'il y en a un le "
             "jour du cours. L'actualité vaut mieux que l'exemple.")

    d.regle('Lire des prévisions par moments',
            "Matinée · midi · fin de journée. Chaque moment a ses conditions.",
            precision="« Ciel couvert en matinée, vent qui se lève vers midi, ciel qui "
                      "s'éclaircit en fin de journée. » Une prévision n'est jamais "
                      "valable pour toute la journée : il faut chercher le moment qui "
                      "nous concerne.",
            notes="Relier à B1 : c'est la même structure que le bulletin radio, en plus "
                  "court.")

    d.pratique('Pratique · 3 de 4', "Est-ce annoncé ?",
               "D'après les prévisions de demain, lues à voix haute.", [
        ("De la neige en matinée", "OUI"),
        ("De la pluie verglaçante", "NON"),
        ("Des vents forts à partir de midi", "OUI"),
        ("Un ciel dégagé toute la matinée", "NON — couvert en matinée"),
        ("Des éclaircies en fin de journée", "OUI"),
        ("Une soirée douce", "NON — moins quinze"),
    ], corrige=True,
       notes="Lire les prévisions à voix haute deux fois avant d'afficher les énoncés : "
             "« Demain, ciel couvert en matinée avec de faibles chutes de neige. Le vent "
             "du nord-est se lèvera vers midi, avec des pointes à 45 km/h. En fin de "
             "journée, le ciel s'éclaircira et le mercure descendra à moins quinze "
             "degrés. » Les six énoncés se corrigent vite ensuite.")

    d.piege("Le piège du tronçon ignoré",
            "Il y a un avertissement sur la 10, je ne pars pas.",
            "L'avertissement vise le tronçon Sainte-Julie–Marieville.",
            "Un avertissement sur une autoroute ne vise presque jamais toute sa "
            "longueur. Si votre trajet ne passe pas par le tronçon nommé, il ne vous "
            "concerne pas — et vous perdriez une journée pour rien.",
            notes="L'erreur inverse est plus grave, mais celle-ci coûte des journées de "
                  "travail. Les deux méritent d'être nommées.")

    d.piege("Le piège du « par moments »",
            "La visibilité sera mauvaise tout le trajet.",
            "« Par moments » veut dire : à certains endroits, à certaines heures.",
            "« Par moments » est une expression clé des avertissements. Elle veut dire "
            "que la visibilité tombera brusquement puis reviendra. C'est plus dangereux "
            "qu'une mauvaise visibilité constante : on ne s'y attend pas.",
            notes="Point de sécurité routière important. Le dire clairement : les "
                  "carambolages arrivent dans les baisses soudaines de visibilité.")

    d.pratique('Pratique · 4 de 4', "Écrivez l'avertissement",
               "Quatre lignes : où, quoi, jusqu'à quand, quelle consigne.", [
        ("La situation",
         "De la poudrerie sur la route 132, entre Sorel et Bécancour, jusqu'à ce soir."),
        ("La consigne", "la route reste ouverte, les conducteurs doivent ralentir"),
        ("Les services", "les chasse-neige circulent, un poste de secours au km 12"),
    ], corrige=False,
       notes="Quinze minutes. Ramasser : ces avertissements montrent si les quatre blocs "
             "sont acquis.")

    d.billet(
        "Consultez un avertissement routier réel et notez ses quatre informations.",
        exemples=[
            "Où, quoi, jusqu'à quand, quelle consigne.",
            "S'il n'y en a aucun aujourd'hui, notez l'état d'une route de votre trajet.",
        ],
        notes="Devoir court et concret. Il installe l'habitude de consulter avant de "
              "partir, qui est le vrai objectif du défi 2.")

    return d.save(dossier)
