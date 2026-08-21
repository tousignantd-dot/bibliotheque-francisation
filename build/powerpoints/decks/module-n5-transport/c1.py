# -*- coding: utf-8 -*-
"""C1 · « Quatre routes en cinquante secondes »
Bloc C « Défi 2 · Le bulletin de 6 h 50 » · couleur acier · 75 min.
Source : dialogue `t2`, exercice `t2a`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C1', section='acier',
        titre="« Quatre routes en cinquante secondes »",
        chapeau="Un vrai bulletin ne parle pas d'une route : il en fait "
                "quatre en cinquante secondes, et la vôtre est peut-être la "
                "troisième. Tenir jusqu'au bout sans perdre le début, c'est "
                "tout le défi 2.",
        duree='75 minutes')

    d.titre(notes="Première séance du défi 2, et la plus exigeante du module en écoute. "
                  "Faire écouter le bulletin de six heures cinquante en entier, sans "
                  "arrêt, puis demander combien de routes ont été nommées. Peu de gens "
                  "en trouvent quatre du premier coup, et c'est normal.")

    d.objectifs([
        "suivre un bulletin de quatre ou cinq routes sans perdre le début ;",
        "reconnaître l'ordre habituel : les ponts, les autoroutes, les rues ;",
        "attraper le nom de la route en tête de phrase ;",
        "comprendre ce que « pour le moment » annonce.",
    ], notes="Le troisième objectif est une technique, pas une connaissance : si l'on "
             "attrape le nom, on sait tout de suite si la suite nous concerne — et sinon, "
             "on peut cesser d'écouter jusqu'à la route suivante. C'est permis, et c'est "
             "reposant.")

    d.dialogue('Dialogue · 1 de 3', "Les ponts, d'abord", [
        ("GAÉTAN", "Six heures cinquante, le point sur la circulation. On "
                   "commence par les ponts. Le pont Jacques-Cartier est fermé "
                   "en direction de Montréal jusqu'à neuf heures.", True),
        ("TEREZA", "Fermé jusqu'à neuf heures… Amine, il a dit neuf heures ?", True),
        ("GAÉTAN", "Sur le pont Samuel-De Champlain, la circulation est dense "
                   "mais fluide. On calcule dix minutes d'attente.", True),
    ], consigne="Écoutez d'abord, diapositive masquée.",
       notes="Faire remarquer que Tereza vérifie l'heure à voix haute : c'est ce qu'on "
             "fait quand on ne peut pas faire répéter. La formule « dense mais fluide » "
             "a été vue en A4 — la faire retrouver par le groupe.")

    d.dialogue('Dialogue · 2 de 3', "Puis les autoroutes", [
        ("GAÉTAN", "Sur l'autoroute 25, dans le pont-tunnel, tout est ouvert "
                   "dans les deux sens. Aucune entrave à signaler.", True),
        ("GAÉTAN", "Sur l'autoroute 40, un véhicule lourd est immobilisé sur "
                   "l'accotement, à la hauteur de Pie-IX. La circulation n'est "
                   "pas touchée pour le moment.", True),
        ("AMINE", "« Pas touchée pour le moment. » Ça veut dire : attends dix "
                  "minutes et ce sera touché.", True),
    ], notes="La traduction d'Amine est la leçon de la séance. « Pour le moment » annonce "
             "que la personne au micro s'attend au pire — c'est une formule figée, elle "
             "s'apprend d'un bloc.")

    d.dialogue('Dialogue · 3 de 3', "Écrire pendant qu'on écoute", [
        ("TEREZA", "Attends, je récapitule. Jacques-Cartier : fermé jusqu'à "
                   "neuf heures. Champlain : ouvert, dix minutes d'attente.", True),
        ("AMINE", "Tu vois ? Tu l'as eu au complet.", True),
        ("TEREZA", "Je l'ai eu parce que je l'ai écrit. Si je ne l'écris pas, "
                   "à la troisième route, j'ai déjà perdu la première.", False),
    ], notes="La dernière réplique est la technique de tout le défi 2. Elle sera "
             "travaillée pour elle-même en C4. Personne ne retient quatre routes de tête "
             "à sept heures du matin, et ce n'est pas une question de langue.")

    d.regle("L'ordre du bulletin est presque toujours le même",
            "Les ponts d'abord, les autoroutes ensuite, les grandes rues à la "
            "fin.",
            precision="Quand on connaît cet ordre, on sait quand arrive sa route — "
                      "et on peut se reposer entre les deux.",
            notes="Diapositive à photographier. Faire situer par chacun sa propre route "
                  "dans cet ordre, à partir des billets ramassés en A1.")

    d.tableau('Le bulletin de 6 h 50', "Quatre routes, quatre états",
              ['La route', 'Son état'],
              [["Jacques-Cartier", "fermé jusqu'à 9 h"],
               ["Samuel-De Champlain", "ouvert, 10 min d'attente"],
               ["Le pont-tunnel", "aucune entrave"],
               ["L'autoroute 40", "camion sur l'accotement"],
               ["Henri-Bourassa", "nid-de-poule, voie de droite"]],
              cle=1,
              notes="Faire remplir ce tableau pendant une deuxième écoute, à la volée. "
                    "C'est exactement la note demandée en C4 — l'exercice commence ici.")

    d.piege("Vouloir tout comprendre avant de noter",
            "J'écoute d'abord, j'écrirai ensuite.",
            "J'écris le nom de la route pendant qu'il dit la suite.",
            "Le nom arrive en tête de phrase et la suite dure trois secondes. Si "
            "l'on attend d'avoir compris, la route suivante est déjà commencée.",
            notes="Faire l'expérience : une écoute sans écrire, une écoute en écrivant. "
                  "La différence se voit sur les feuilles, elle ne se discute pas.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après le bulletin de six heures cinquante.", [
        ("Le pont Jacques-Cartier est fermé vers Montréal.", "vrai"),
        ("Il rouvrira vers midi.", "faux — à neuf heures"),
        ("On attend dix minutes à l'approche de Champlain.", "vrai"),
        ("Le pont-tunnel est fermé dans un sens.", "faux — tout est ouvert"),
        ("Le nid-de-poule est sur l'autoroute 40.", "faux — sur Henri-Bourassa"),
        ("Le prochain bulletin passe dans dix minutes.", "vrai"),
    ], corrige=True,
       notes="Les six items viennent de l'exercice `t2a`. Faire justifier chaque « faux » "
             "en retrouvant la phrase exacte : c'est de l'écoute fine, pas de la mémoire.")

    d.billet(
        "Écrivez les quatre routes du bulletin, une par ligne, avec un mot pour l'état.",
        exemples=[
            "Le nom d'abord, l'état en trois mots : Jacques-Cartier — fermé 9 h.",
            "Si vous en avez manqué une, laissez la ligne vide.",
        ],
        notes="Ramasser les billets : ils préparent directement la prise de notes de C4. "
              "Une note trouée est utilisable ; une note où tout est mêlé ne l'est pas.")

    return d.save(dossier)
