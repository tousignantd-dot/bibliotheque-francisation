# -*- coding: utf-8 -*-
"""A3 · Les marqueurs de temps.
Bloc A · couleur ambre (écriture) · 60 min.
Source : exercice `prMarq` et sa mini-leçon.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A3', section='ambre',
        titre='Les marqueurs de temps',
        chapeau="« Hier », « quelques minutes après », « présentement », « bientôt ». "
                "Sans ces mots, un fait divers devient une liste d'événements sans "
                "ordre — et le lecteur ne sait plus ce qui a mené à quoi.",
        duree='60 minutes')

    d.titre(notes="Lire un court fait divers sans aucun marqueur de temps, puis le même "
                  "avec. Le groupe entendra tout de suite ce qui manque.")

    d.objectifs([
        "reconnaître un marqueur de passé, de présent et de futur ;",
        "placer un marqueur au bon endroit dans une phrase ;",
        "raconter un événement dans l'ordre chronologique ;",
        "employer les marqueurs les plus fréquents des faits divers.",
    ])

    d.tableau('Analyse', "Les marqueurs du passé",
              ['Le marqueur', 'Ce qu\'il situe'],
              [["hier, avant-hier", "un ou deux jours avant"],
               ["la semaine dernière, l'an passé", "une période terminée"],
               ["il y a peu de temps", "récemment, sans préciser"],
               ["deux jours avant", "avant un autre moment déjà nommé"],
               ["pendant que, avant que", "en même temps ou avant une autre action"]],
              cle=0, props=[0.42, 0.58],
              notes="La quatrième ligne est la plus difficile : « deux jours avant » se "
                    "compte à partir d'un autre moment, pas à partir d'aujourd'hui.")

    d.tableau('Analyse', "Le présent et le futur",
              ['Le marqueur', 'Ce qu\'il situe'],
              [["aujourd'hui, maintenant", "le moment où l'on parle"],
               ["présentement, actuellement", "en ce moment, registre écrit"],
               ["demain, après-demain", "un ou deux jours après"],
               ["bientôt, dans quelques jours", "prochainement, sans préciser"],
               ["l'an prochain, la prochaine fois", "une période à venir"]],
              cle=0, props=[0.42, 0.58],
              notes="« Présentement » et « actuellement » sont les marqueurs des textes "
                    "de nouvelles. Les faire remarquer : on les lit plus qu'on ne les "
                    "dit.")

    d.regle('La règle',
            "Un marqueur de temps se place au début ou à la fin de la phrase.",
            precision="« Hier, un feu s'est déclaré rue des Ormes. » ou « Un feu s'est "
                      "déclaré rue des Ormes hier. » Les deux sont corrects. Au début, "
                      "le marqueur est plus visible — c'est le choix des journalistes.",
            notes="Faire remarquer que les reportages commencent presque toujours par le "
                  "moment : « Hier, dans une école de Longueuil… »")

    d.cartes('En apprendre plus', "Quatre choses à savoir en plus", [
        ("La virgule après le marqueur",
         "Quand le marqueur ouvre la phrase, une virgule le suit : « Hier, un feu s'est "
         "déclaré. » Pas de virgule quand il est à la fin."),
        ("« Depuis » n'est pas un marqueur de moment",
         "« Depuis trois jours » dit une durée qui continue, pas un point dans le "
         "temps. C'est autre chose, et c'est très utile dans un fait divers."),
        ("« Il y a » et « dans »",
         "« Il y a trois jours » : dans le passé. « Dans trois jours » : dans le futur. "
         "Deux mots très courts, deux directions opposées."),
        ("L'ordre du récit",
         "Un fait divers commence souvent par le plus récent, puis remonte : « Le chat "
         "a été retrouvé. Il s'était sauvé il y a trois jours. »"),
    ], notes="La quatrième carte explique une difficulté réelle de lecture : les faits "
             "divers ne sont pas toujours chronologiques.")

    d.pratique('Pratique · 1 de 4', "Passé, présent ou futur ?",
               "Classez le marqueur.", [
        ("avant-hier", "passé"),
        ("présentement", "présent"),
        ("dans une semaine", "futur"),
        ("l'an passé", "passé"),
        ("actuellement", "présent"),
        ("la prochaine fois", "futur"),
    ], corrige=True, cols=2,
       notes="Exercice rapide. Enchaîner sur le texte à compléter, qui est le vrai "
             "exercice de la séance.")

    d.pratique('Pratique · 2 de 4', "Complétez le fait divers",
               "Un marqueur de temps par trou.", [
        ("Rue des Ormes, à Sherbrooke, un feu s'est déclaré dans un garage ___.", "hier"),
        ("Les pompiers sont arrivés sur les lieux ___ après l'appel.", "quelques minutes"),
        ("Le propriétaire, qui dormait, a été réveillé ___ par l'odeur de fumée.",
         "juste à temps"),
        ("___, l'enquête se poursuit pour connaître la cause de l'incendie.",
         "Présentement / Aujourd'hui"),
        ("Les résidants pourront réintégrer leur maison ___.", "dans quelques jours / bientôt"),
    ], corrige=True,
       notes="Faire remarquer la progression : passé, passé, passé, présent, futur. "
             "C'est la structure de presque tous les faits divers.")

    d.piege("Le piège de « il y a » et « dans »",
            "Le chat s'est sauvé dans trois jours.",
            "Le chat s'est sauvé il y a trois jours.",
            "« Il y a » regarde vers le passé, « dans » vers le futur. Deux mots très "
            "courts, faciles à confondre à l'oral, et qui inversent complètement le sens "
            "d'une phrase.",
            notes="Faire dessiner une ligne du temps au tableau, avec « aujourd'hui » au "
                  "milieu. Placer les deux expressions de part et d'autre.")

    d.piege("Le piège de « avant-hier »",
            "Le journaliste dit hier, donc c'était hier.",
            "Dany dit avant-hier : les deux ne parlent pas du même moment.",
            "Dans le dialogue de A1, le reportage dit « hier » et Dany dit « avant-hier ». "
            "Le reportage a été enregistré un autre jour. Un marqueur de temps se compte "
            "toujours à partir du moment où l'on parle — et ce moment change.",
            notes="Point d'écoute fine qui explique beaucoup de confusions dans les "
                  "bulletins réécoutés en différé.")

    d.pratique('Pratique · 3 de 4', "Remettez le récit dans l'ordre",
               "Numérotez de 1 à 5, du plus ancien au plus récent.", [
        ("Une voisine a reconnu le chat dans sa cour hier matin.", "4"),
        ("Le chat s'est sauvé par une fenêtre entrouverte il y a trois jours.", "1"),
        ("La fillette a distribué des affiches dans le quartier.", "3"),
        ("La classe a fabriqué des affiches.", "2"),
        ("La voisine a averti la famille.", "5"),
    ], corrige=True,
       notes="Faire remarquer que le texte du module ne suit pas cet ordre : il commence "
             "par la fin. C'est le point de la quatrième carte.")

    d.pratique('Pratique · 4 de 4', "Racontez avec des marqueurs",
               "Trois phrases : un passé, un présent, un futur.", [
        ("Un événement passé", "La semaine dernière, une tempête a fermé les écoles."),
        ("La situation actuelle", "Présentement, les équipes déneigent les rues."),
        ("Ce qui va arriver", "Les cours reprendront dans deux jours."),
    ], corrige=True,
       notes="Les corrigés sont des modèles. Faire écrire trois phrases sur une vraie "
             "nouvelle de la semaine.")

    d.billet(
        "Racontez un événement de votre semaine en trois phrases.",
        exemples=[
            "Un marqueur de temps au début de chaque phrase.",
            "Passé, présent, futur — dans cet ordre.",
        ],
        notes="Corriger la virgule après le marqueur en tête de phrase. C'est le point "
              "d'écriture de la séance.")

    return d.save(dossier)
