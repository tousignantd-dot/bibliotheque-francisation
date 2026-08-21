# -*- coding: utf-8 -*-
"""C4 · Est-ce que ça me concerne ?
Bloc C « Défi 2 · Le bulletin de 6 h 50 » · couleur acier · 75 min.
Source : exercices `t2conc` et `t2note`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C4', section='acier',
        titre="Est-ce que ça me concerne ?",
        chapeau="Un bulletin donne cinq informations et quatre ne vous "
                "regardent pas. Savoir lesquelles écarter est aussi utile que "
                "savoir écouter — et c'est ce qui permet de tenir jusqu'au "
                "bout sans se fatiguer.",
        duree='75 minutes')

    d.titre(notes="Dernière séance du défi 2. Elle réunit l'écoute et la décision. "
                  "Reprendre les billets de A1, où chacun a écrit sa route et son sens : "
                  "toute la séance se fait avec les trajets réels du groupe, pas avec "
                  "ceux de Tereza.")

    d.objectifs([
        "trier ce qui vous concerne avec deux questions : ma route, mon sens ;",
        "tenir compte de l'heure d'une fermeture ;",
        "prendre une note pendant qu'on écoute, une ligne par route ;",
        "dire sa décision en une phrase, avec sa raison.",
    ], notes="La prise de notes est une compétence transférable : la même technique sert "
             "au téléphone, en réunion, chez le médecin. Le dire au groupe, ça change le "
             "sérieux avec lequel on s'y met.")

    d.regle("Deux questions, pas une",
            "Est-ce ma route ? Et est-ce mon sens ?",
            precision="La moitié des détours inutiles viennent de la seconde : une "
                      "entrave en direction est ne touche pas quelqu'un qui roule "
                      "vers l'ouest, même sur la même autoroute.",
            notes="Diapositive à photographier. Faire appliquer les deux questions au "
                  "trajet réel de trois élèves, à voix haute, avant de continuer.")

    d.tableau('Prendre une note', "Ce qu'on écrit, ce qu'on n'écrit pas",
              ['On écrit', 'On n\'écrit pas'],
              [["le nom de la route", "les articles"],
               ["un mot pour l'état", "les verbes"],
               ["les chiffres en chiffres", "les heures en lettres"],
               ["une ligne par route", "des phrases"]],
              cle=1,
              notes="Faire l'expérience des deux : une écoute où l'on écrit des phrases, "
                    "une écoute où l'on écrit quatre mots. La seconde tient, la première "
                    "décroche à la deuxième route.")

    d.cartes("Une note qui tient", "Cinq lignes, dix secondes à relire", [
        ("Jacques-Cartier", "fermé 9 h"),
        ("Champlain", "ouvert, 10 min"),
        ("Pont-tunnel", "rien à signaler"),
        ("40 ouest", "camion accotement Pie-IX"),
        ("Henri-Bourassa", "nid-de-poule, voie droite"),
    ], notes="Projeter cette note et demander au groupe combien de temps il faut pour la "
             "relire. Deux secondes. C'est le seul critère : une note se relit dans une "
             "auto, en mouvement.")

    d.piege("Vouloir noter tout le bulletin",
            "J'écris tout, je trierai après.",
            "J'écris ma route en entier, les autres en un mot.",
            "Écrire tout fait perdre la suite. Le tri se fait pendant l'écoute, pas "
            "après : votre route mérite trois mots, les autres un seul.",
            notes="Rappeler que le bulletin repasse dans dix minutes. Ce qui a été "
                  "manqué revient, à condition d'avoir laissé une ligne vide pour "
                  "l'accueillir.")

    d.pratique('Tri', "Est-ce que ça concerne Tereza ?",
               "Elle part de Longueuil vers Saint-Laurent, le matin.", [
        ("Le pont Jacques-Cartier est fermé vers Montréal.", "oui — c'est son pont, son sens, son heure"),
        ("L'autoroute 20 est ralentie vers Québec.", "non — ce n'est pas sa route"),
        ("Un carambolage bloque la 40 ouest, avant sa sortie.", "oui — sa route, son sens"),
        ("Un nid-de-poule sur Henri-Bourassa, direction est.", "non — pas son sens"),
        ("La voie de gauche de la 40 est fermée jusqu'à 5 h.", "non — elle part à 6 h 50"),
        ("La bretelle de la 15 nord vers la 40 ouest est fermée.", "oui — c'est exactement son chemin"),
    ], corrige=True,
       notes="Les six items viennent de l'exercice `t2conc`. Refaire ensuite le même "
             "tri avec le trajet d'un élève volontaire : c'est là que la séance prend.")

    d.pratique('Prise de notes', "Écrivez votre note",
               "Une ligne par route, le nom d'abord.", [
        ("Ligne 1 — Jacques-Cartier", "fermé 9 h"),
        ("Ligne 2 — Champlain", "ouvert, 10 min d'attente"),
        ("Ligne 3 — pont-tunnel", "rien à signaler"),
        ("Ligne 4 — autoroute 40", "camion sur accotement, Pie-IX"),
        ("Ligne 5 — Henri-Bourassa", "nid-de-poule, voie de droite"),
        ("Votre décision, en une phrase", "On prend Champlain : dix minutes d'attente valent mieux que d'attendre neuf heures."),
    ], corrige=True,
       notes="Faire écrire pendant une écoute réelle, chronométrée. Puis comparer les "
             "notes deux par deux : les meilleures ne sont pas les plus complètes, ce "
             "sont les plus courtes.")

    d.billet(
        "Écrivez la note que vous prendriez demain matin, pour votre trajet à vous.",
        exemples=[
            "Deux ou trois lignes suffisent : vous n'avez pas quatre routes.",
            "Ajoutez une ligne pour votre décision, avec sa raison.",
        ],
        notes="Ramasser les billets : ils servent de brouillon au message écrit de la "
              "séance E2, où la même information devient un courriel.")

    return d.save(dossier)
