# -*- coding: utf-8 -*-
"""B1 · Les questions qui manquent.
Bloc B « Défi 1 · S'informer sur une activité » · couleur acier · 75 min.
Source : dialogue `t1`, exercices `t1vf` et `t1cond`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B1', section='acier',
        titre='Les questions qui manquent',
        chapeau="Rosa rappelle : il y a des choses qu'elle n'a pas notées. "
                "Faut-il savoir nager ? Peut-on rester pour regarder ? Les "
                "réponses arrivent dans une langue particulière : celle des conditions.",
        duree='75 minutes')

    d.titre(notes="Ouverture du bloc B. Normaliser le fait de rappeler : personne ne pense "
                  "à tout du premier coup, et rappeler n'a rien d'embarrassant.")

    d.objectifs([
        "rappeler pour compléter une information ;",
        "poser des questions sur les conditions d'admission ;",
        "reconnaître une obligation, un conseil et une interdiction ;",
        "comprendre ce qui arrive si on manque un cours.",
    ])

    d.declencheur(
        'Mise en situation', "Vous avez oublié de demander quelque chose. Que faites-vous ?",
        pistes=[
            "Rappelez-vous, ou attendez-vous d'y retourner ?",
            "Comment commencez-vous l'appel ?",
            "Est-ce gênant de rappeler ? Pourquoi ?",
            "Que se passe-t-il si vous ne rappelez pas ?",
        ],
        notes="Cinq minutes. Beaucoup diront qu'ils n'osent pas rappeler. C'est le sujet de "
              "la séance : la première phrase de Rosa est justement celle qui rend l'appel "
              "facile.")

    d.dialogue('Dialogue · 1 de 3', "Rappeler sans gêne", [
        ("ROSA", "Je rappelle pour le cours de natation. Il y a des choses que je n'ai pas notées.", True),
        ("LOUISE", "Allez-y, je vous écoute.", False),
        ("ROSA", "Est-ce qu'il faut que mon garçon sache déjà nager ?", True),
        ("LOUISE", "Non. Le groupe du samedi, c'est le niveau débutant. Il est important qu'il n'ait pas peur de l'eau, c'est tout.", True),
    ], consigne="Écoutez d'abord, diapo masquée.",
       notes="La première réplique est la formule à retenir : « je rappelle pour… » + « il "
             "y a des choses que je n'ai pas notées ». Elle règle toute la gêne en une "
             "phrase. La faire répéter par le groupe.")

    d.dialogue('Dialogue · 2 de 3', "Ce qui arrive si…", [
        ("ROSA", "Et s'il manque un cours ?", True),
        ("LOUISE", "Il n'y a pas de reprise, mais ce n'est pas grave : chaque cours reprend ce qui a été vu.", False),
        ("ROSA", "Est-ce que je peux rester pour regarder ?", True),
        ("LOUISE", "Il est préférable que les parents restent dans la salle d'attente. Les enfants écoutent mieux.", False),
    ], notes="« Il est préférable » n'est pas « il est interdit ». La nuance sera "
             "travaillée en B2 : ici, la faire seulement remarquer.")

    d.dialogue('Dialogue · 3 de 3', "Le détail qui compte", [
        ("ROSA", "Et pour l'inscription, il faut que je vienne en personne ?", True),
        ("LOUISE", "Pas nécessairement. Mais si vous payez en ligne, il faut quand même apporter la preuve d'adresse au premier cours.", True),
    ], notes="Le « quand même » de la dernière réplique est un signal : une condition "
             "revient malgré ce qui vient d'être dit. Le faire remarquer.")

    d.tableau('Analyse', "Trois forces de condition",
              ['Ce qu\'on entend', 'Ce que ça exige'],
              [["Il faut…", "obligation — sans cela, non"],
               ["Il est important que…", "condition réelle, souvent la seule"],
               ["Il est préférable que…", "conseil — on peut faire autrement"],
               ["Pas nécessairement", "ce n'est pas obligatoire"]],
              cle=0,
              note="Écoutez lequel des quatre vous entendez : ils ne demandent pas la même chose.",
              notes="Diapo centrale du bloc. Faire recopier avant B2, qui reprendra ces "
                    "formes une par une.")

    d.regle("La phrase qui rend le rappel facile",
            "« Je rappelle pour… Il y a des choses que je n'ai pas notées. »",
            precision="Cette phrase dit tout : pourquoi vous appelez, et que vous ne "
                      "recommencez pas à zéro. La personne au bout du fil sait "
                      "immédiatement quoi faire — et personne ne trouve cela pénible.",
            notes="Diapo à photographier. La faire répéter par deux élèves différents.")

    d.piege('Ne pas rappeler',
            "Je vais me débrouiller, je verrai bien sur place.",
            "Je rappelle pour le cours de natation. Il y a des choses que je n'ai pas notées.",
            "Se présenter sans le document ou sans le matériel obligatoire fait perdre un "
            "déplacement complet, et parfois une place. Un appel de deux minutes remplace "
            "un aller-retour d'une heure.",
            notes="Le calcul est concret : le faire au tableau, en minutes.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après le dialogue.", [
        ("Il faut savoir nager pour s'inscrire au groupe du samedi.", "faux — c'est le niveau débutant"),
        ("Il est important que l'enfant n'ait pas peur de l'eau.", "vrai — c'est la seule condition"),
        ("Un cours manqué peut être repris plus tard.", "faux — il n'y a pas de reprise"),
        ("Les parents sont invités à rester au bord de la piscine.", "faux — dans la salle d'attente"),
        ("L'inscription doit obligatoirement se faire en personne.", "faux — en ligne aussi"),
        ("La preuve d'adresse peut être apportée au premier cours.", "vrai"),
    ], corrige=True,
       notes="Faire justifier chaque réponse par la réplique exacte. La dernière est celle "
             "qui contient le « quand même ».")

    d.billet(
        "Écrivez les trois questions que vous poseriez en rappelant.",
        exemples=[
            "Commencez par la formule : « Je rappelle pour… »",
            "Trois questions sur les conditions, pas sur l'horaire ni le prix.",
        ],
        notes="Ramasser. Ces questions servent au jeu de rôle de E1, où l'assistant ne "
              "donne rien sans qu'on le demande.")

    return d.save(dossier)
