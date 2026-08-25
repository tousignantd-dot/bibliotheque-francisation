# -*- coding: utf-8 -*-
"""B4 · Le futur simple du bulletin.
Bloc B · couleur ambre (écriture) · 75 min.
Source : le bulletin `t1` — se maintiendra, balaieront, tombera, descendra.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B4', section='ambre',
        titre='Le futur du bulletin',
        chapeau="« Le mercure se maintiendra », « les rafales balaieront », « le vent "
                "tombera ». Un bulletin météo est écrit presque entièrement au futur "
                "simple — c'est le temps de la prévision.",
        duree='75 minutes')

    d.titre(notes="Relire le bulletin de B1 et faire souligner tous les verbes. Presque "
                  "tous sont au futur simple : c'est le point de départ.")

    d.objectifs([
        "former le futur simple d'un verbe régulier ;",
        "connaître les futurs irréguliers les plus fréquents ;",
        "reconnaître le futur simple à l'écoute ;",
        "écrire une prévision au futur simple.",
    ])

    d.regle('La formation',
            "L'infinitif, puis les terminaisons -ai, -as, -a, -ons, -ez, -ont.",
            precision="Tomber donne il tombera. Descendre perd son e : il descendra. Les "
                      "terminaisons sont celles du verbe avoir au présent, et elles ne "
                      "changent jamais, quel que soit le verbe.",
            notes="Écrire la méthode au tableau : infinitif + terminaison. C'est le temps "
                  "le plus régulier du français.")

    d.tableau('Analyse', "Le futur simple de tomber",
              ['La personne', 'La forme'],
              [["je", "je tomberai"],
               ["tu", "tu tomberas"],
               ["il, elle", "le vent tombera"],
               ["nous", "nous tomberons"],
               ["vous", "vous tomberez"],
               ["ils, elles", "les rafales tomberont"]],
              cle=1,
              notes="La troisième et la sixième forme sont celles du bulletin : on y "
                    "parle du vent, du mercure, des rafales. "
                    "Faire remarquer qu'un bulletin n'emploie presque que la troisième "
                    "personne. C'est ce qui le rend prévisible.")

    d.tableau('Analyse', "Six futurs irréguliers du bulletin",
              ['Le verbe', 'Au futur'],
              [["être", "il sera"],
               ["avoir", "il y aura"],
               ["faire", "il fera"],
               ["venir", "le vent viendra"],
               ["se maintenir", "le mercure se maintiendra"],
               ["pouvoir", "on pourra"]],
              cle=1,
              notes="Six verbes irréguliers, tous fréquents dans un bulletin. Les faire "
                    "copier : ils s'apprennent par cœur, il n'y a pas de règle.")

    d.cartes('Ouvrir la mini-leçon', "Quatre choses à savoir en plus", [
        ("Le r est toujours là",
         "Tomber-a, descendr-a, ser-a, fer-a. Le son r avant la terminaison est la "
         "marque du futur : c'est ce qu'on entend."),
        ("Les verbes en -re perdent leur e",
         "Descendre donne descendra, prendre donne prendra, mettre donne mettra. Un "
         "seul changement, toujours le même."),
        ("Le futur proche existe aussi",
         "« Il va neiger » et « il neigera » disent la même chose. Le bulletin écrit "
         "emploie le futur simple ; à l'oral, on entend souvent « va »."),
        ("Le futur pour une consigne",
         "« Vous descendrez avant midi » est un ordre poli. C'est fréquent sur un "
         "chantier, et ce n'est pas une prévision."),
    ], notes="La première carte donne le repère d'écoute : le son r. C'est ce qui "
             "distingue « il tombe » de « il tombera ».")

    d.pratique('Pratique · 1 de 4', "Mettez au futur simple",
               "Troisième personne, comme dans un bulletin.", [
        ("le vent (tomber)", "le vent tombera"),
        ("le mercure (descendre)", "le mercure descendra"),
        ("les rafales (balayer)", "les rafales balaieront"),
        ("le ciel (se dégager)", "le ciel se dégagera"),
        ("la neige (s'accumuler)", "la neige s'accumulera"),
        ("la visibilité (diminuer)", "la visibilité diminuera"),
    ], corrige=True,
       notes="Les six verbes sont ceux du bulletin. Faire remarquer que tous sont "
             "réguliers : le futur est un temps facile.")

    d.pratique('Pratique · 2 de 4', "Les irréguliers",
               "Six verbes à connaître par cœur.", [
        ("il (être) beau demain", "il sera beau demain"),
        ("il y (avoir) des éclaircies", "il y aura des éclaircies"),
        ("il (faire) moins six", "il fera moins six"),
        ("le vent (venir) du nord-est", "le vent viendra du nord-est"),
        ("on (pouvoir) monter samedi", "on pourra monter samedi"),
    ], corrige=True,
       notes="Ces cinq formes suffisent pour comprendre n'importe quel bulletin. Les "
             "faire répéter à voix haute.")

    d.piege("Le piège du présent entendu pour du futur",
            "« Le vent tombe » et « le vent tombera » se ressemblent.",
            "Cherchez le son r : c'est la marque du futur.",
            "« Il tombe » et « il tombera » ne diffèrent que par une syllabe. Dans un "
            "bulletin, la différence est décisive : l'un dit ce qui se passe maintenant, "
            "l'autre ce qui est prévu. Le son r avant la terminaison est le repère.",
            notes="Faire dire les deux formes en alternance, dix fois. C'est un exercice "
                  "d'oreille, pas de grammaire.")

    d.piege("Le piège des verbes en -re",
            "le mercure descendera",
            "le mercure descendra",
            "Les verbes en -re perdent leur e final avant les terminaisons du futur : "
            "descendre donne descendra, prendre donne prendra, mettre donne mettra. "
            "C'est le seul changement, et il vaut pour tous les verbes de ce groupe.",
            notes="Faire écrire trois verbes en -re au futur, au tableau. Le motif "
                  "apparaît immédiatement.")

    d.pratique('Pratique · 3 de 4', "Présent ou futur ?",
               "Cherchez le son r.", [
        ("La pluie verglaçante recouvre les routes.", "présent — c'est en cours"),
        ("La pluie verglaçante se changera en neige.", "futur — c'est prévu"),
        ("Le mercure se maintient autour de zéro.", "présent"),
        ("Le mercure descendra à moins six.", "futur"),
        ("Les chasse-neige circulent depuis minuit.", "présent"),
    ], corrige=True,
       notes="C'est l'exercice d'écoute le plus utile du module. Le faire à l'oral "
             "d'abord, sans montrer le texte.")

    d.pratique('Pratique · 4 de 4', "Écrivez la prévision",
               "Quatre phrases au futur simple, comme un bulletin.", [
        ("Le ciel", "Le ciel se dégagera en fin de journée."),
        ("Le vent", "Le vent viendra du nord-est, avec des pointes à 45 km/h."),
        ("La température", "Le mercure descendra à moins quinze degrés."),
        ("Les précipitations", "Cinq à dix centimètres de neige tomberont d'ici demain."),
    ], corrige=True,
       notes="Ces quatre phrases sont le squelette d'un bulletin. Elles serviront "
             "directement en E1.")

    d.billet(
        "Écrivez la prévision de demain en quatre phrases, au futur simple.",
        exemples=[
            "Le ciel, le vent, la température, les précipitations.",
            "Soulignez le r de chaque verbe au futur.",
        ],
        notes="Corriger uniquement les verbes. Rendre avant E1, où ces phrases "
              "deviendront un bulletin complet.")

    return d.save(dossier)
