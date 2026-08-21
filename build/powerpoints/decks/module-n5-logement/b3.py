# -*- coding: utf-8 -*-
"""B3 · Rapporter ce qu'on vous a dit.
Bloc B « Défi 1 · L'appel » · couleur ambre · 75 min.
Source : dialogue `t1b`, exercice `t1indirect` et sa mini-leçon.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B3', section='ambre',
        titre="Rapporter ce qu'on vous a dit",
        chapeau="Après un appel, personne ne répète les phrases exactes de "
                "l'autre. On les rapporte : « Elle me dit que… », « Je lui ai "
                "demandé si… »",
        duree='75 minutes')

    d.titre(notes="Séance de grammaire, la plus dense du bloc B. Le discours indirect est "
                  "un savoir du niveau 5 et il revient dans la production écrite finale.")

    d.objectifs([
        "rapporter une déclaration avec « que » ;",
        "rapporter une question par oui ou non avec « si » ;",
        "distinguer « ce que » et « ce qui » ;",
        "changer les pronoms quand on change de bouche.",
    ])

    d.declencheur(
        'Observation', "Comment racontez-vous un appel à quelqu'un ?",
        pistes=[
            "La propriétaire a dit : « Le chauffage n'est pas inclus. »",
            "Comment le racontez-vous à votre conjoint le soir ?",
            "Qu'est-ce qui change dans la phrase ?",
            "Et si c'était une question ?",
        ],
        notes="Écrire au tableau la phrase directe, puis noter les versions proposées par "
              "le groupe. Certaines seront correctes, d'autres garderont « est-ce que ». "
              "Ne rien corriger : le tableau suivant le fera.")

    d.dialogue('Dialogue · 1 de 2', "Qu'est-ce qu'elle vous a dit ?", [
        ("SAMUEL", "Puis, cet appel ? Vous avez pris des notes ?", True),
        ("NADÈGE", "J'ai tout écrit. Elle me dit que le logement est libre le "
                   "premier juillet et que le loyer est de mille cinquante dollars.", True),
        ("SAMUEL", "Est-ce que vous lui avez demandé si le chauffage était compris ?", True),
        ("NADÈGE", "C'est la première chose que j'ai demandée. Elle m'explique que "
                   "le chauffage est électrique et qu'il n'est pas inclus.", True),
    ], consigne="Comptez les « que » et les « si ».",
       notes="Faire relever les verbes introducteurs : dit, demandé, explique. Ce sont eux "
             "qui portent la phrase rapportée.")

    d.dialogue('Dialogue · 2 de 2', "Ce qui n'est pas fourni", [
        ("SAMUEL", "Et vous savez ce qui n'est pas fourni ?", True),
        ("NADÈGE", "La laveuse et la sécheuse. Le poêle et le réfrigérateur, eux, "
                   "sont là.", True),
        ("SAMUEL", "Vous avez posé les bonnes questions. Il vous manque juste ce que "
                   "personne ne pense à demander : le bruit, l'isolation, et depuis "
                   "quand le loyer n'a pas augmenté.", True),
        ("NADÈGE", "Ça, je le demanderai jeudi, pendant la visite.", True),
    ], notes="Les deux formes voisines sont ici, à deux répliques d'écart : « ce qui n'est "
             "pas fourni » et « ce que personne ne pense à demander ». Les encadrer au "
             "tableau : c'est le point le plus difficile de la séance.")

    d.tableau('Les cinq transformations', "Ce qui devient quoi",
              ['La phrase entendue', 'La phrase rapportée'],
              [["« Le logement est libre. »", "Elle me dit QUE le logement est libre."],
               ["« Est-ce que c'est chauffé ? »", "Je demande SI c'est chauffé."],
               ["« Quand est-il libre ? »", "Je demande QUAND il est libre."],
               ["« Qu'est-ce que vous fournissez ? »", "Je demande CE QUE vous fournissez."],
               ["« Qu'est-ce qui est inclus ? »", "Je demande CE QUI est inclus."]],
              cle=0,
              note="Dans les cinq cas, le point d'interrogation disparaît.",
              notes="Diapositive à photographier. C'est le tableau de référence du module "
                    "pour le discours indirect.")

    d.regle("« Est-ce que » ne survit jamais",
            "Dans une phrase rapportée, « est-ce que » devient « si » — ou disparaît.",
            precision="« Est-ce que » est un outil de question directe. Une phrase "
                      "rapportée n'est plus une question : c'est une déclaration au sujet "
                      "d'une question. « Je demande est-ce que c'est libre » est toujours "
                      "faux.",
            notes="Diapositive à photographier. C'est l'erreur numéro un, et elle est très "
                  "tenace parce qu'elle sonne bien à l'oreille de l'élève.")

    d.cartes("Ce que ou ce qui ?", "Regardez ce qui suit", [
        ("ce qui + verbe",
         "Le verbe suit directement : ce qui EST inclus, ce qui ARRIVE."),
        ("ce que + sujet",
         "Un sujet vient d'abord : ce que VOUS fournissez, ce que PERSONNE ne demande."),
        ("L'astuce",
         "Cherchez un sujet entre le relatif et le verbe. S'il y en a un, c'est « ce que »."),
        ("La même règle que qui / que",
         "C'est exactement la logique des relatifs du défi 2 : sujet ou complément."),
    ], notes="La quatrième carte annonce la séance C3. Le faire remarquer : les élèves "
             "voient rarement que c'est la même règle.")

    d.piege("Laisser les pronoms de l'autre personne",
            "Elle dit qu'elle vous rappelle vendredi.",
            "Elle dit qu'elle me rappelle vendredi.",
            "Celui qui rapporte n'est plus celui qui parlait. Elle vous a dit « je vous "
            "rappelle » : en le rapportant, « je » devient « elle » et « vous » devient "
            "« me ». On pense au verbe, on change le « que », et on oublie les pronoms.",
            notes="Erreur discrète : la phrase reste grammaticale, mais elle dit autre "
                  "chose. Faire relire les pronoms en dernier, toujours.")

    d.pratique('Transformation', "Rapportez ces phrases",
               "Commencez par « Elle me dit… » ou « Je lui demande… ».", [
        ("« Le loyer est de 1 050 $. »", "Elle me dit que le loyer est de 1 050 $."),
        ("« Est-ce que le logement est libre ? »", "Je lui demande si le logement est libre."),
        ("« Quand pouvez-vous visiter ? »", "Elle me demande quand je peux visiter."),
        ("« Qu'est-ce que vous cherchez ? »", "Elle me demande ce que je cherche."),
        ("« Qu'est-ce qui est inclus ? »", "Je lui demande ce qui est inclus."),
        ("« Je vous rappelle vendredi. »", "Elle me dit qu'elle me rappelle vendredi."),
    ], corrige=True,
       notes="Les deux dernières sont les plus difficiles. Prendre le temps sur la "
             "sixième : deux pronoms changent en même temps.")

    d.billet(
        "Rapportez trois choses qu'on vous a dites au téléphone cette semaine.",
        exemples=[
            "« Elle me dit que… » — une déclaration.",
            "« Je lui ai demandé si… » — une question.",
        ],
        notes="Devoir d'écriture. Il réemploie l'appel réel du devoir B2 et prépare "
              "directement la production écrite finale, qui exige deux phrases rapportées.")

    return d.save(dossier)
