# -*- coding: utf-8 -*-
"""E1 · À toi : raconter et écrire un fait divers.
Bloc E · couleur teal (je me lance) · 90 min.
Source : section `appli` — production orale puis écrite d'un fait divers.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='E1', section='teal',
        titre='À toi : écrire un fait divers',
        chapeau="Tout le module en une séance. Raconter une nouvelle à voix haute, puis "
                "l'écrire comme un journaliste : le résultat d'abord, le décor à "
                "l'imparfait, les événements au passé composé.",
        duree='90 minutes')

    d.titre(notes="Séance d'application. Aucun contenu nouveau. Un tiers d'oral, un "
                  "tiers d'écrit, un tiers de relecture croisée.")

    d.objectifs([
        "raconter une nouvelle à voix haute en trente secondes ;",
        "écrire un fait divers de huit à dix lignes ;",
        "employer l'imparfait pour le décor et le passé composé pour les événements ;",
        "relire un texte en vérifiant les auxiliaires et les accords.",
    ])

    d.regle("La structure d'un fait divers",
            "Le résultat · le décor · les événements dans l'ordre · la suite.",
            precision="Une phrase pour le résultat, deux ou trois pour le décor à "
                      "l'imparfait, trois ou quatre pour les événements au passé "
                      "composé, une pour ce qui va se passer maintenant.",
            notes="Écrire la structure au tableau. C'est le plan de la production "
                  "écrite, et il tient en quatre lignes.")

    d.tableau('Analyse', "Un fait divers, phrase par phrase",
              ['La partie', 'Le temps', 'Un exemple'],
              [["le résultat", "passé composé", "Un feu a détruit un garage rue des Ormes."],
               ["le décor", "imparfait", "Il était 22 h et il faisait très froid."],
               ["les événements", "passé composé", "Les pompiers sont arrivés dix minutes plus tard."],
               ["la suite", "présent ou futur", "L'enquête se poursuit présentement."]],
              cle=1, props=[0.22, 0.22, 0.56],
              notes="Trois temps dans un même texte, chacun à sa place. C'est la synthèse "
                    "de C2, C3 et C4.")

    d.pratique('Pratique · 1 de 4', "À l'oral · racontez votre nouvelle",
               "À deux, trente secondes, sans notes. Puis on échange.", [
        ("La phrase d'ouverture", "qui, quoi, où — en une phrase"),
        ("Les étapes", "dans l'ordre du temps, avec un marqueur chacune"),
        ("La situation actuelle", "où en sont les choses aujourd'hui"),
        ("Les questions", "votre partenaire en pose trois"),
    ], corrige=False,
       notes="Vingt minutes. Les nouvelles apportées par les élèves valent mieux que "
             "celles du module. Rendre les billets de B5.")

    d.cartes('Écrire', "Quatre choses à vérifier dans un fait divers", [
        ("Le titre",
         "Court, avec un verbe. « Un feu détruit un garage » plutôt que « Incendie ». "
         "Cinq à huit mots."),
        ("La première phrase",
         "Elle répond à qui, quoi, où, quand. Si elle n'y arrive pas, elle est trop "
         "longue ou incomplète."),
        ("Les temps",
         "Imparfait pour le décor, passé composé pour les événements. Un décor au passé "
         "composé sonne faux."),
        ("La source",
         "« Selon les autorités », « d'après les organisateurs ». Une information non "
         "confirmée doit être marquée comme telle."),
    ], notes="La quatrième carte reprend la notion de A4. C'est ce qui distingue un fait "
             "divers d'un récit personnel.")

    d.pratique('Pratique · 2 de 4', "Écrivez le titre et la première phrase",
               "Un titre de cinq à huit mots, une phrase qui répond aux quatre questions.", [
        ("Un feu dans un garage", "Un feu détruit un garage rue des Ormes"),
        ("Une collecte réussie dans une école",
         "Des élèves de Longueuil amassent 200 paires de mitaines"),
        ("Un animal retrouvé", "Une fillette de Gatineau retrouve son chat"),
        ("Un projet scolaire présenté", "Une classe de Victoriaville filme un documentaire"),
    ], corrige=True,
       notes="Faire remarquer que les titres sont au présent : c'est l'usage des "
             "journaux, même pour des événements passés.")

    d.pratique('Pratique · 3 de 4', "Écrivez le fait divers complet",
               "Huit à dix lignes, selon la structure en quatre parties.", [
        ("Le sujet", "une nouvelle de votre semaine, ou un événement inventé"),
        ("La structure", "résultat, décor, événements, suite"),
        ("Les temps", "imparfait pour le décor, passé composé pour les événements"),
        ("À ne pas oublier", "le titre, et la source si l'information n'est pas certaine"),
    ], corrige=False,
       notes="Trente minutes d'écriture individuelle. Circuler et aider sur le choix des "
             "temps, pas sur le contenu.")

    d.piege("Le piège du décor au passé composé",
            "Il a fait très froid et il a été 22 h.",
            "Il faisait très froid et il était 22 h.",
            "Le décor d'un fait divers est toujours à l'imparfait : l'heure, la météo, "
            "l'état des gens. Au passé composé, ces phrases deviennent des événements — "
            "comme si le froid était arrivé d'un coup.",
            notes="Erreur la plus fréquente de la production écrite. La corriger en "
                  "priorité pendant la relecture croisée.")

    d.pratique('Pratique · 4 de 4', "Relecture croisée",
               "Échangez les textes. Six vérifications, dans l'ordre.", [
        ("Le titre a-t-il un verbe ?", "et fait-il moins de huit mots ?"),
        ("La première phrase répond-elle aux quatre questions ?", "qui, quoi, où, quand"),
        ("Le décor est-il à l'imparfait ?", "l'heure, la météo, l'état des gens"),
        ("Les événements sont-ils au passé composé ?", "et les auxiliaires sont-ils bons ?"),
        ("Les participes sont-ils accordés ?", "avec être seulement"),
        ("Y a-t-il une source pour ce qui n'est pas certain ?", "selon, d'après"),
    ], corrige=True,
       notes="Une relecture croisée trouve deux fois plus d'erreurs qu'une relecture par "
             "l'auteur. Ramasser les versions corrigées, pas les premières.")

    d.billet(
        "En une phrase : qu'est-ce que vous comprenez mieux dans les nouvelles qu'au début du module ?",
        exemples=[
            "Une seule chose, précise.",
            "Exemple : « je sais quoi chercher dans la première phrase ».",
        ],
        notes="Lire quelques billets à voix haute, sans nommer les auteurs. C'est la "
              "meilleure préparation à la séance de bilan.")

    return d.save(dossier)
