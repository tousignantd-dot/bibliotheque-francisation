# -*- coding: utf-8 -*-
"""D1 · « L'appel de sept heures vingt-cinq »
Bloc D « Défi 3 · Le trajet refait » · couleur acier · 75 min.
Source : dialogue `t3`, exercices `t3a` et `t3poli`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='D1', section='acier',
        titre="« L'appel de sept heures vingt-cinq »",
        chapeau="Comprendre le bulletin ne sert à rien si l'on n'en fait "
                "rien. Sept heures vingt, l'autoroute est bloquée, l'atelier "
                "ouvre à huit heures et c'est Tereza qui a les clés. Elle "
                "prend le téléphone.",
        duree='75 minutes')

    d.titre(notes="Première séance du défi 3, et le moment où le module bascule de "
                  "l'écoute vers la parole. Ouvrir en demandant qui, dans le groupe, a "
                  "déjà eu à téléphoner pour annoncer un retard, et ce qui a été difficile. "
                  "Les réponses tournent presque toujours autour de la peur d'être jugé.")

    d.objectifs([
        "annoncer un retard en trois informations, dans l'ordre ;",
        "se nommer dès la première phrase ;",
        "proposer soi-même ce qu'on fait en attendant ;",
        "distinguer une explication d'une justification.",
    ], notes="Le quatrième objectif est culturel autant que linguistique. Beaucoup "
             "d'élèves se défendent avant qu'on les accuse, parce que dans leur milieu "
             "d'origine un retard se paie cher. Le dire sans juger.")

    d.dialogue('Dialogue · 1 de 3', "Se nommer, puis expliquer", [
        ("GHISLAINE", "Atelier d'assemblage, Ghislaine Lachance, bonjour.", True),
        ("TEREZA", "Bonjour madame Lachance, c'est Tereza Nogueira. Je vous "
                   "appelle de l'auto : je vais être en retard ce matin.", True),
        ("GHISLAINE", "Bonjour Tereza. Qu'est-ce qui se passe ?", True),
    ], consigne="Écoutez d'abord, diapositive masquée.",
       notes="Faire compter les secondes : en deux répliques, la responsable sait qui "
             "appelle et pourquoi. Faire remarquer le vouvoiement d'un côté et le "
             "prénom de l'autre : c'est la norme entre une employée et sa responsable.")

    d.dialogue('Dialogue · 2 de 3', "Ce qui bloque, et depuis quand", [
        ("TEREZA", "Il y a eu un carambolage sur la 40 en direction ouest, à "
                   "la hauteur de Côte-de-Liesse. Deux voies sur trois sont "
                   "bloquées.", True),
        ("GHISLAINE", "Depuis quand ?", True),
        ("TEREZA", "Depuis six heures et demie, à peu près. Ça fait presque "
                   "une heure. Les remorqueuses viennent tout juste de "
                   "commencer.", True),
    ], notes="Tout le bloc B est là : le mot juste, les deux repères, le sens, « depuis » "
             "et « ça fait… que ». Le faire remarquer au groupe — c'est la preuve que "
             "les séances précédentes servaient à quelque chose.")

    d.dialogue('Dialogue · 3 de 3', "L'heure, et la solution", [
        ("GHISLAINE", "Vous pensez arriver à quelle heure ?", True),
        ("TEREZA", "J'arrive vers huit heures quinze, huit heures vingt au "
                   "plus tard.", True),
        ("TEREZA", "C'est moi qui ouvre le mardi. Est-ce que Farida peut "
                   "prendre les clés ? Elle arrive à sept heures et demie.", True),
        ("GHISLAINE", "Je m'en occupe. Merci de m'avoir prévenue.", False),
    ], notes="La dernière réplique de Tereza est ce qui distingue un appel réussi d'un "
             "appel ordinaire : elle propose avant qu'on lui demande. Le faire "
             "remarquer, c'est le critère principal du jeu de rôle de E1.")

    d.regle("Trois informations, dans l'ordre",
            "Ce qui se passe. L'heure d'arrivée. Ce qu'on fait en attendant.",
            precision="Tout le reste allonge l'appel et affaiblit ce que vous "
                      "dites. Un appel réussi dure trente secondes.",
            notes="Diapositive à photographier. C'est la grille du message oral de E1 et "
                  "de l'exercice `t3msg` de l'activité interactive.")

    d.tableau('Deux façons de le dire', "L\'une informe, l\'autre inquiète",
              ['Ce qui se dit', 'Ce qui ne se dit pas'],
              [["C'est Tereza Nogueira.", "Salut, c'est moi."],
               ["Un carambolage sur la 40.", "Ce n'est pas de ma faute."],
               ["J'arrive vers 8 h 15.", "Dès que je peux."],
               ["Farida peut ouvrir.", "Je ne sais pas quoi faire."]],
              cle=1,
              notes="Faire lire la colonne de droite à voix haute : elle fait rire, et "
                    "c'est ce qui la fixe. Personne ne veut être celui qui dit « dès que "
                    "je peux ».")

    d.piege("Se défendre avant qu'on vous accuse",
            "Ce n'est vraiment pas de ma faute, je suis partie à l'heure, je vous jure.",
            "Il y a eu un carambolage sur la 40, en direction ouest.",
            "Une explication donne un fait. Une défense répond à une accusation que "
            "personne n'a portée — et se défendre donne l'impression qu'il y a de "
            "quoi.",
            notes="Faire remarquer que Ghislaine ne demande jamais de preuve. Elle "
                  "demande ce qui se passe, l'heure, et qui ouvre. Répondre à ces trois "
                  "questions suffit à clore l'affaire.")

    d.piege("Attendre d'être certain pour appeler",
            "J'appellerai quand je saurai à quelle heure j'arrive.",
            "J'appelle maintenant, et je rappelle si ça change.",
            "Le bon moment est celui où l'on comprend qu'on sera en retard. On peut "
            "très bien dire : « je ne sais pas encore, je vous rappelle dans vingt "
            "minutes ».",
            notes="Un appel de trente secondes à sept heures vingt vaut mieux qu'une "
                  "explication parfaite à huit heures et quart. C'est la phrase à "
                  "laisser au tableau.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après l'appel à l'atelier.", [
        ("Tereza se nomme dès sa première phrase.", "vrai"),
        ("Elle appelle après être arrivée.", "faux — elle appelle de l'auto"),
        ("Ça bloque depuis environ une heure.", "vrai"),
        ("Elle annonce une heure d'arrivée précise.", "vrai"),
        ("C'est Ghislaine qui propose que Farida ouvre.", "faux — c'est Tereza"),
        ("Ghislaine lui demande de se dépêcher.", "faux — au contraire"),
    ], corrige=True,
       notes="Les six items viennent de l'exercice `t3a`. La dernière réponse surprend "
             "toujours : aucune responsable ne demande d'accélérer, et le proposer met "
             "tout le monde mal à l'aise.")

    d.billet(
        "Écrivez les trois premières phrases de votre appel : qui vous êtes, ce qui se passe, l'heure.",
        exemples=[
            "Bonjour madame X, c'est …, de l'atelier.",
            "Une heure en chiffres, jamais un « bientôt ».",
        ],
        notes="Ramasser les billets : ce sont les brouillons de la production orale de "
              "E1. Relever ceux où le nom manque, c'est l'oubli le plus fréquent et le "
              "plus coûteux sur un répondeur.")

    return d.save(dossier)
