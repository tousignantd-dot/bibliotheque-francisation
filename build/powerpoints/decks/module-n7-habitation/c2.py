# -*- coding: utf-8 -*-
"""C2 · Redire au passé ce qui a été dit
Bloc C « Défi 2 · Redire ce qui a été dit » · couleur ambre · grammaire ·
75 min.
Source : exercice `t2ind` et sa mini-leçon.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C2', section='ambre',
        titre="Redire au passé ce qui a été dit",
        chapeau="Après « il m'a dit que », tout recule d'un cran. Trois "
                "décalages, et rien de plus.",
        duree='75 minutes')

    d.titre(notes="La séance de grammaire la plus lourde du module, et la plus "
                  "rentable : le discours rapporté au passé sert dans tous les "
                  "comptes rendus, au travail comme ailleurs.")

    d.objectifs([
        "employer le plus-que-parfait pour ce qui était déjà arrivé ;",
        "employer le conditionnel présent pour ce qui devait arriver ;",
        "employer aller à l'imparfait pour une intention proche ;",
        "décaler aussi les personnes et les repères de temps.",
    ], notes="Le quatrième objectif est celui qu'on oublie, et c'est celui qui trahit "
             "un compte rendu bâclé : un « demain » resté sur place se trompe d'un jour.")

    d.declencheur(
        'Observation', "« Je mettrai du caoutchouc. » Comment le racontes-tu demain ?",
        pistes=[
            "Il m'a dit qu'il… quoi ?",
            "Est-ce que le futur reste un futur ?",
            "Et « j'ai acheté le tapis en janvier » ?",
            "Et « je vais descendre mon vélo » ?",
        ],
        notes="Écrire les trois réponses du groupe au tableau, justes ou fausses. La "
              "correction viendra des trois règles, pas de l'enseignante.")

    d.regle("Le point de référence n'est plus aujourd'hui",
            "Quand le verbe qui introduit est au passé, tout ce qui suit recule.",
            precision="« Il m'a dit que », « il m'a expliqué que », « il m'a promis "
                      "que » : à partir de là, on se règle sur le jour de la "
                      "conversation, pas sur aujourd'hui. Si l'introducteur est au "
                      "présent — « il dit que » —, rien ne bouge. Tout le mécanisme "
                      "tient à ce seul mot.",
            notes="Diapositive à photographier. Faire le test au présent d'abord : "
                  "« il dit qu'il mettra ». Puis au passé. La différence saute aux "
                  "oreilles.")

    d.tableau('Analyse', "Les trois décalages",
              ['Ses mots', 'Rapporté au passé'],
              [["J'ai acheté le tapis.", "Il m'a dit qu'il avait acheté le tapis."],
               ["Je mettrai du caoutchouc.", "Il m'a dit qu'il mettrait du caoutchouc."],
               ["Je vais descendre mon vélo.", "Il m'a dit qu'il allait descendre son vélo."],
               ["Je ne peux pas.", "Il m'a dit qu'il ne pouvait pas."],
               ["Ma conjointe me l'avait dit.", "Il m'a dit que sa conjointe le lui avait dit."]],
              cle=1,
              notes="Diapositive à photographier. Les deux dernières rangées montrent "
                    "ce qui NE bouge pas : l'imparfait et le plus-que-parfait sont déjà "
                    "au fond du passé.")

    d.cartes('Analyse', "Ce qui bouge aussi", [
        ("Les personnes", "je devient il, mon devient son, nous devient ils, ici devient là"),
        ("Le temps", "hier devient la veille, demain devient le lendemain, ce matin devient ce matin-là"),
        ("Ce qui ne bouge pas", "les heures et les dates précises : 5 h 45 reste 5 h 45, le 4 février reste le 4 février"),
    ], cols=3,
       notes="La troisième carte rassure : ce qui fait la valeur d'un compte rendu — "
             "les chiffres — ne se transforme jamais.")

    d.piege('Grammaire',
            "Il m'a dit qu'il mettra du caoutchouc",
            "Il m'a dit qu'il mettrait du caoutchouc",
            "Mélanger deux points de référence dans la même phrase. Si l'introducteur "
            "est au passé, tout suit : le futur devient un conditionnel présent. Ce "
            "conditionnel-là n'exprime aucune condition — c'est un futur vu de loin, "
            "ce qu'on appelle parfois le futur du passé.",
            notes="Faire remarquer que le mot « conditionnel » induit en erreur : il "
                  "n'y a aucune condition dans « il m'a dit qu'il mettrait ».")

    d.pratique('Pratique', "Rapportez au passé",
               "Mettez le verbe à la forme qui convient.", [
        ("Il m'a dit : « J'ai acheté le tapis en janvier. » — rapporté : qu'il ___ acheté le tapis.", "avait"),
        ("« Ma conjointe me l'avait signalé. » — rapporté : que sa conjointe le lui ___ signalé.", "avait"),
        ("« Je mettrai du caoutchouc cette semaine. » — rapporté : qu'il ___ du caoutchouc.", "mettrait"),
        ("« Je regarderai si l'appareil rentre. » — rapporté : qu'il ___ si l'appareil rentrait.", "regarderait"),
        ("« Je vais descendre mon vélo à l'épaule. » — rapporté : qu'il ___ descendre son vélo.", "allait"),
        ("« Je vais y penser d'ici vendredi. » — rapporté : qu'il ___ y penser d'ici vendredi.", "allait"),
        ("« Je ne peux pas changer mon heure. » — rapporté : qu'il ne ___ pas changer son heure.", "pouvait"),
        ("« Revenez me voir si ça ne suffit pas. » — rapporté : de ___ le voir si cela ne suffisait pas.", "revenir"),
    ], corrige=True,
       notes="Le huitième change de forme : un impératif rapporté devient « de » plus "
             "l'infinitif. Le signaler après la correction, pas avant.")

    d.billet(
        "Rapporte au passé une phrase que quelqu'un t'a dite cette semaine.",
        exemples=[
            "Commence par « Il m'a dit que » ou « Elle m'a dit que ».",
            "Vérifie les personnes : je devient il ou elle.",
        ],
        notes="Deux minutes. Ramasser : c'est l'exercice qui prédit le mieux la "
              "réussite de la production orale du bloc E.")

    return d.save(dossier)
