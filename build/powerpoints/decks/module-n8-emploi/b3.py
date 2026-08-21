# -*- coding: utf-8 -*-
"""B3 · Il faut que ça passe par : le subjonctif.
Bloc B « Défi 1 » · couleur ambre · 75 min.
Source : exercices `t1subj` et `t1pass`, et leurs mini-leçons.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B3', section='ambre',
        titre="Il faut que ça passe par : le subjonctif",
        chapeau="L'indicatif raconte le monde tel qu'il est ; le subjonctif "
                "parle du monde tel qu'il devrait être. Dans une réclamation, "
                "on passe son temps dans le second.",
        duree='75 minutes')

    d.titre(notes="Séance de grammaire, mais entièrement tirée du dialogue de B1. "
                  "Commencer par relire les répliques de Sylvain : elles sont pleines "
                  "de subjonctifs, et personne ne l'avait remarqué.")

    d.objectifs([
        "former le subjonctif présent à partir du « ils » du présent ;",
        "employer les quatre irréguliers du bureau : être, avoir, faire, aller ;",
        "reconnaître les déclencheurs de nécessité et de volonté ;",
        "ne pas employer le subjonctif après « après que » ni « espérer que ».",
    ], notes="Le quatrième objectif est celui qui distingue un niveau 8 d'un niveau 6 : "
             "connaître les exceptions, pas seulement la règle.")

    d.regle("La formation, en trois gestes",
            "Le « ils » du présent, moins -ent, plus les terminaisons.",
            precision="ils vérifi-ent donne : que je vérifie, que tu vérifies, qu'il "
                      "vérifie, que nous vérifiions, que vous vérifiiez, qu'ils "
                      "vérifient. Le double « i » de « vérifiions » est correct et "
                      "surprend tout le monde. Aux formes nous et vous, le subjonctif "
                      "ressemble à l'imparfait.",
            notes="Diapositive à photographier. Faire la manipulation à voix haute avec "
                  "trois verbes du module : entrer, comparer, avancer.")

    d.cartes("Les quatre à savoir par cœur", "Ce sont ceux qu'on emploie tous les jours", [
        ("être", "que je sois, que tu sois, qu'il soit, que nous soyons, que vous soyez"),
        ("avoir", "que j'aie, que tu aies, qu'il ait, que nous ayons, que vous ayez"),
        ("faire", "que je fasse, que nous fassions — un seul radical, aucune surprise"),
        ("aller", "que j'aille, que nous allions — le plus fréquent après « il faut que »"),
    ], notes="Trois autres méritent d'être ajoutés si le groupe suit : que je puisse, "
             "que je sache, qu'il faille.")

    d.tableau('Analyse', "Les déclencheurs du bureau",
              ['Ce qu\'ils expriment', 'Les expressions'],
              [["La nécessité", "il faut que · il est nécessaire que · il est important que"],
               ["La volonté", "je souhaite que · j'aimerais que · je demande que"],
               ["Le but et le temps", "pour que · avant que · jusqu'à ce que"],
               ["La condition et l'opposition", "à condition que · pourvu que · bien que"]],
              cle=0,
              note="Apprendre la liste, pas la règle : ces vingt expressions couvrent un courriel professionnel.",
              notes="Diapositive à photographier. Faire construire une phrase par ligne, "
                    "sur le dossier de paie de Nadia.")

    d.piege("Mettre le subjonctif après « après que »",
            "Après que j'aie envoyé le courriel…",
            "Après que j'ai envoyé le courriel…",
            "« Après que » introduit un fait accompli : l'action a eu lieu, donc "
            "l'indicatif. La faute est si répandue qu'on l'entend chez des locuteurs "
            "natifs — ce qui ne la rend pas correcte à l'écrit. Même chose pour "
            "« espérer que » : j'espère que vous comprenez, jamais que vous compreniez.",
            notes="Retenir la paire : avant que + subjonctif, après que + indicatif. "
                  "Le temps qui n'est pas encore là demande le subjonctif.")

    d.pratique('Grammaire', "Le verbe au subjonctif",
               "Complétez avec le verbe entre parenthèses.", [
        ("Il faut que la demande ___ (passer) par ma superviseure.", "passe"),
        ("Il est important que vous ___ (avoir) le document avant mercredi.", "ayez"),
        ("Je souhaite que la correction ___ (être) faite sur la paie du 29.", "soit"),
        ("Bien que la règle ___ (être) claire, le système ne l'applique pas.", "soit"),
        ("Pour que le dossier ___ (avancer), joignez l'autorisation.", "avance"),
        ("À condition que nous ___ (faire) la demande aujourd'hui…", "fassions"),
        ("Il ne faut pas que ce dossier ___ (traîner) encore.", "traîne"),
        ("J'espère que vous ___ (comprendre) ma démarche.", "comprenez — pas de subjonctif"),
    ], corrige=True,
       notes="Le dernier item est le piège de la séance. Le laisser tomber sans "
             "prévenir : la discussion qui suit vaut mieux qu'une explication.")

    d.pratique('Production', "Une phrase par déclencheur",
               "Écrivez une phrase sur votre propre travail.", [
        ("Il faut que…", ""),
        ("Il est important que…", ""),
        ("Pour que…", ""),
        ("Bien que…", ""),
    ], notes="Ramasser deux ou trois phrases et les projeter. Corriger devant le groupe "
             "sans nommer l'auteur.")

    d.billet(
        "Écrivez trois phrases avec « il faut que » sur votre travail.",
        exemples=[
            "Une avec le verbe être, une avec avoir, une avec aller.",
            "Relisez : la terminaison est-elle celle du subjonctif ?",
        ],
        notes="Ces trois phrases servent de matière première à la lettre de B4.")

    return d.save(dossier)
