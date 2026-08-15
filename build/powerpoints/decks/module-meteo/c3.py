# -*- coding: utf-8 -*-
"""C3 · Lui, leur, eux, elles.
Bloc C · couleur ambre (écriture) · 75 min.
Source : exercices `t2ci` et `t2cilui` et leur mini-leçon.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C3', section='ambre',
        titre='Lui, leur, eux, elles',
        chapeau="« Je leur envoie un message. » « Je compte sur elle. » Deux pronoms, "
                "deux places différentes — et c'est la préposition qui décide de tout.",
        duree='75 minutes')

    d.titre(notes="Écrire les deux phrases du chapeau au tableau et demander pourquoi le "
                  "pronom n'est pas au même endroit. Personne ne trouvera : c'est le "
                  "sujet de la séance.")

    d.objectifs([
        "remplacer un complément avec « à » par lui ou leur ;",
        "remplacer un complément avec une autre préposition par lui, elle, eux, elles ;",
        "placer le pronom au bon endroit ;",
        "éviter la répétition d'un nom dans un message.",
    ])

    d.regle('La règle',
            "Après « à », c'est lui ou leur, devant le verbe. Après une autre préposition, c'est lui, elle, eux ou elles, après le verbe.",
            precision="« Je parle à Josée » devient « je lui parle ». « Je compte sur "
                      "Josée » devient « je compte sur elle ». La préposition décide du "
                      "pronom ET de sa place.",
            notes="Écrire la règle en deux lignes au tableau. C'est la seule chose à "
                  "retenir de toute la séance.")

    d.tableau('Analyse', "Deux familles de pronoms",
              ['La préposition', 'Le pronom', 'La place'],
              [["à + une personne", "lui, leur", "avant le verbe"],
               ["sur, avec, de, chez…", "lui, elle, eux, elles", "après la préposition"]],
              cle=1,
              note="Une seule préposition change de comportement : « à ». Toutes les "
                   "autres gardent le pronom après elles.",
              notes="C'est ce qui rend « à » particulier. Le dire ainsi : « à » fait "
                    "monter le pronom devant le verbe.")

    d.tableau('Analyse', "Lui et leur : singulier et pluriel",
              ['Le complément', 'Le pronom', 'Un exemple'],
              [["à Josée (une personne)", "lui", "Je lui parle."],
               ["à Diego (une personne)", "lui", "Je lui téléphone."],
               ["aux apprentis (plusieurs)", "leur", "Je leur souris."],
               ["aux fournisseurs (plusieurs)", "leur", "Je leur écris."]],
              cle=1,
              note="« Lui » ne dit rien du genre : il vaut pour un homme comme pour une "
                   "femme. Seul le nombre change.",
              notes="Erreur fréquente : croire que « lui » est masculin et « elle » "
                    "féminin. Devant le verbe, c'est « lui » dans les deux cas.")

    d.cartes('En apprendre plus', "Quatre choses à savoir en plus", [
        ("« Leur » sans s devant un verbe",
         "« Je leur écris » — jamais de s. Le « leurs » avec s est un déterminant : "
         "« leurs outils ». Devant un verbe, jamais."),
        ("Au passé composé, devant l'auxiliaire",
         "« Je lui ai parlé. » Le pronom se place devant « ai », comme tous les pronoms "
         "compléments."),
        ("À la négative, entre ne et le verbe",
         "« Je ne lui parle pas. » « Je ne compte pas sur elle. » Les deux familles "
         "gardent leur place."),
        ("Après « à » pour une chose, c'est « y »",
         "« Je pense à mon travail » devient « j'y pense ». « Lui » et « leur » ne "
         "valent que pour des personnes."),
    ], notes="La quatrième carte relie au module 2, séance C2. Le signaler à ceux qui "
             "l'ont fait : « y » pour une chose, « lui » pour une personne.")

    d.pratique('Pratique · 1 de 4', "Lui ou leur ?",
               "Une personne, ou plusieurs ?", [
        ("Je téléphone à Josée avant six heures.", "Je lui téléphone avant six heures."),
        ("Diego demande à Mado de vérifier la route.",
         "Diego lui demande de vérifier la route."),
        ("Josée offrira une prime aux apprentis.", "Josée leur offrira une prime."),
        ("J'écris un courriel aux fournisseurs.", "Je leur écris un courriel."),
        ("Nous allons demander au client de patienter.",
         "Nous allons lui demander de patienter."),
        ("Elle répond aux automobilistes avec patience.", "Elle leur répond avec patience."),
    ], corrige=True,
       notes="Faire compter les personnes avant de choisir. C'est le seul critère : "
             "singulier ou pluriel.")

    d.pratique('Pratique · 2 de 4', "Lui, elle, eux ou elles ?",
               "Après une préposition autre que « à ».", [
        ("Diego compte sur Josée pour la sécurité.", "Diego compte sur elle."),
        ("Prisca part avec ses deux collègues.", "Prisca part avec eux."),
        ("Je me fie à mes coéquipiers pour les échafaudages.",
         "Je me fie à eux — « se fier à » garde la préposition"),
        ("Te souviens-tu des couvreurs de l'an dernier ?", "Te souviens-tu d'eux ?"),
        ("Mado discute avec la répartitrice de nuit.", "Mado discute avec elle."),
    ], corrige=True,
       notes="Le troisième item est le piège : « se fier à » emploie « à » mais garde le "
             "pronom après. Quelques verbes font ainsi ; les signaler sans en faire une "
             "liste.")

    d.piege("Le piège du « leurs » avec un s",
            "Je leurs ai envoyé un message.",
            "Je leur ai envoyé un message.",
            "Devant un verbe, « leur » est un pronom et ne prend jamais de s. Le "
            "« leurs » avec s est un déterminant, et il est suivi d'un nom : « leurs "
            "outils », « leurs feuilles de temps ». Regardez ce qui suit.",
            notes="Erreur d'écriture très fréquente. Le repère « nom après ou verbe "
                  "après » est mécanique et fiable.")

    d.piege("Le piège de la place",
            "Je parle lui.",
            "Je lui parle.",
            "Avec « à », le pronom passe devant le verbe. C'est l'inverse de l'ordre "
            "habituel, et l'inverse de beaucoup de langues. Il n'y a pas d'exception : "
            "lui et leur sont toujours devant le verbe conjugué.",
            notes="Faire répéter cinq phrases à voix haute, pronom devant. L'oreille "
                  "finit par accepter ce que la règle explique.")

    d.pratique('Pratique · 3 de 4', "Devant ou après ?",
               "Cherchez la préposition.", [
        ("Je parle ___ (à Josée).", "je lui parle — devant"),
        ("Je compte ___ (sur Josée).", "je compte sur elle — après"),
        ("J'écris ___ (aux fournisseurs).", "je leur écris — devant"),
        ("Je pars ___ (avec les apprentis).", "je pars avec eux — après"),
        ("Je téléphone ___ (au client).", "je lui téléphone — devant"),
    ], corrige=True,
       notes="Faire nommer la préposition à voix haute avant chaque réponse. C'est elle "
             "qui décide, jamais le sens.")

    d.pratique('Pratique · 4 de 4', "Écrivez le message",
               "Trois phrases avec un pronom, sans répéter les noms.", [
        ("Vous prévenez l'équipe que l'avertissement est levé.",
         "Je leur envoie un message dès que l'avertissement est levé."),
        ("Vous demandez à Mado de vérifier la route.",
         "Je lui demande de vérifier l'état de la route."),
        ("Vous partez avec vos deux collègues.", "Je pars avec eux vers huit heures."),
    ], corrige=True,
       notes="Faire relire les trois phrases en vérifiant la place du pronom. C'est le "
             "seul point à corriger.")

    d.billet(
        "Écrivez quatre phrases, deux avec lui ou leur, deux avec eux ou elles.",
        exemples=[
            "Toutes doivent parler d'une équipe de travail.",
            "Soulignez la préposition dans chacune.",
        ],
        notes="Corriger la place du pronom avant le choix. La préposition soulignée "
              "montre si la méthode est acquise, même quand la réponse est fausse.")

    return d.save(dossier)
