# -*- coding: utf-8 -*-
"""E2 · « Ce que j'ai lu dans le journal cette semaine »
Bloc E « Je me lance » · couleur framboise · 75 min. Dernière séance.
Source : production écrite (courriel), banc de vocabulaire, autoévaluation.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='E2', section='framboise',
        titre="« Ce que j'ai lu dans le journal cette semaine »",
        chapeau="Dernière séance. Un courriel de sept à dix phrases à "
                "quelqu'un qui habite ailleurs et qui ne lit pas L'Écho des "
                "Cantons : la nouvelle des vélos volés, ce que la police "
                "demande, et ce que vous en pensez.",
        duree='75 minutes')

    d.titre(notes="Séance de clôture. Prévoir trois temps : l'écriture du courriel, la "
                  "révision du vocabulaire par les cartes mémoire, puis "
                  "l'autoévaluation. Ne pas sacrifier le troisième : c'est lui qui "
                  "dit à l'élève ce qu'il a gagné en quatre semaines.")

    d.objectifs([
        "écrire un courriel qui raconte une nouvelle à quelqu'un qui est loin ;",
        "croiser le passé composé et l'imparfait dans le même texte ;",
        "rapporter une parole au présent en nommant sa source ;",
        "faire le bilan de ce qu'on est maintenant capable de faire.",
    ], notes="Le troisième objectif est celui qui distingue ce module de tous les "
             "autres récits écrits du niveau. Le rappeler avant l'écriture, pas "
             "après.")

    d.regle("Six exigences, et elles se cochent",
            "Une salutation et la nouvelle · deux passés composés · un "
            "imparfait · une parole rapportée · une phrase impersonnelle · "
            "votre avis et sa signature.",
            precision="Une personne qui est loin ne connaît ni la rue, ni le "
                      "quartier, ni le journal. Dites où c'est, dites d'où vient "
                      "l'information, et séparez nettement ce que le journal "
                      "rapporte de ce que vous en pensez.",
            notes="Diapositive à photographier, et à laisser affichée pendant "
                  "l'écriture. Les six exigences sont exactement celles de la carte "
                  "de production écrite de l'activité.")

    d.tableau('Le plan', "Ce que chaque phrase doit faire",
              ['La phrase', 'Son rôle'],
              [["Allô Teresa,", "Une ligne, pas trois"],
               ["Une trentaine de vélos ont été volés ici.", "La nouvelle, dès le début"],
               ["Les cabanons n'étaient pas barrés.", "Le décor, à l'imparfait"],
               ["La police demande de noter le numéro.", "Une parole rapportée, avec sa source"],
               ["Il vaut mieux barrer son cabanon.", "Une phrase impersonnelle"],
               ["Moi, ce qui me surprend, c'est le nombre.", "L'avis, annoncé comme un avis"]],
              cle=1,
              notes="Faire écrire le courriel en suivant le tableau ligne par ligne la "
                    "première fois. Les élèves rapides peuvent ensuite en écrire un "
                    "second sur une autre nouvelle, sans le tableau.")

    d.cartes("Trois détails qui changent tout", "Ce qui distingue un courriel qu'on comprend de loin", [
        ("Un lieu nommé",
         "« dans mon quartier, à Sherbrooke » — Teresa ne connaît pas la rue."),
        ("Une source nommée",
         "« la police demande » vaut mieux que « il paraît qu'il faut »."),
        ("Une frontière nette",
         "Les faits d'abord, l'avis ensuite : jamais les deux dans la même phrase."),
        ("Une signature",
         "Votre prénom, et le lien : ta belle-sœur, ton cousin, ton amie du cours."),
    ], notes="La troisième carte est la plus transférable du module : elle vaut pour "
             "tout ce que l'élève écrira ensuite, du courriel au commentaire en "
             "ligne.")

    d.pratique('Vérification', "Avant d'envoyer votre courriel",
               "Six choses à vérifier, dans l'ordre.", [
        ("La nouvelle est-elle dite dès le début ?", "sinon, on ne sait pas de quoi il s'agit"),
        ("Y a-t-il deux phrases au passé composé ?", "les évènements, dans l'ordre"),
        ("Y a-t-il une phrase à l'imparfait ?", "le décor : les cabanons n'étaient pas barrés"),
        ("Une parole est-elle rapportée avec son nom ?", "la police, un témoin, la Ville"),
        ("Y a-t-il une phrase impersonnelle ?", "il faut, il vaut mieux, il est important de"),
        ("Votre avis est-il annoncé et justifié ?", "et le courriel est-il signé ?"),
    ], corrige=True,
       notes="Les six points sont exactement ceux de la carte de production écrite. "
             "Faire cocher avant de demander la correction assistée : l'élève corrige "
             "d'abord lui-même.")

    d.vocabulaire('Bilan · 1 de 2', "Les mots à emporter", [
        ("un fait divers", "Un court article qui raconte un évènement arrivé près de chez soi."),
        ("le chapeau", "Les lignes en gras sous le titre, qui disent toute la nouvelle."),
        ("un témoin", "La personne qui était sur place et qui a vu ce qui s'est passé."),
        ("une déclaration", "Ce que quelqu'un dit officiellement, et que le journal peut répéter."),
    ], notes="Quatre des seize mots, choisis parce qu'ils servent à lire n'importe "
             "quel journal, pas seulement celui du module. Renvoyer aux cartes "
             "mémoire pour les douze autres.")

    d.vocabulaire('Bilan · 2 de 2', "Les phrases à emporter", [
        ("Un immeuble a passé au feu cette nuit.", "La nouvelle d'abord : quoi, où, quand."),
        ("Il dormait quand il a entendu l'alarme.", "Le décor et l'évènement dans la même phrase."),
        ("La police dit que l'enquête se poursuit.", "Une parole rapportée porte toujours un nom."),
        ("Moi, ce qui me surprend, c'est le nombre.", "Un avis s'annonce comme un avis."),
    ], notes="Ces quatre phrases sont le module entier en quatre lignes — une par "
             "bloc. Les faire recopier dans le cahier : ce sont celles qui serviront "
             "dès la semaine prochaine.")

    d.piege("Écrire à quelqu'un de loin comme à un voisin",
            "Il y a eu un gros vol sur la rue, tu sais bien.",
            "Une trentaine de vélos ont été volés dans mon quartier, à Sherbrooke.",
            "La personne qui reçoit votre courriel ne connaît ni la rue, ni le "
            "quartier, ni le journal. Chaque nom propre que vous employez doit être "
            "situé, sinon il ne veut rien dire.",
            notes="Dernier piège du module. Il fait le lien avec tout le reste : "
                  "raconter, c'est se mettre à la place de quelqu'un qui n'était pas "
                  "là et qui n'a rien lu.")

    d.billet(
        "Nommez une chose que vous ferez cette semaine grâce à ce module.",
        exemples=[
            "Une chose concrète : lire un fait divers, le raconter, poser une question.",
            "Écrivez à qui vous le raconterez, et quel jour.",
        ],
        notes="Fin du module. Ramasser les billets et y revenir la semaine suivante : "
              "demander qui l'a fait. Faire ensuite l'autoévaluation en seize points "
              "de l'onglet « Je retiens des mots », en classe, sans la ramasser.")

    return d.save(dossier)
