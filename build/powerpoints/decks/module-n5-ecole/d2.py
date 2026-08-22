# -*- coding: utf-8 -*-
"""D2 · Il faut que, pour que, et les six connecteurs
Bloc D « Défi 3 · Demander un changement » · couleur ambre · 75 min.
Grammaire et écriture. Source du module : exercices `t3sub`, `t3con` et
`t3ecrit`, et leurs mini-leçons.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='D2', section='ambre',
        titre="Il faut que, pour que, et les six connecteurs",
        chapeau="Une demande administrative n'a besoin de dire que trois "
                "choses : ce qui est nécessaire, dans quel but, et malgré "
                "quoi. Trois entrées de subjonctif, six connecteurs, et une "
                "lettre de quatre phrases tient debout.",
        duree='75 minutes')

    d.titre(notes="Dernière séance avant « Je me lance ». Rendre les billets de D1 au "
                  "début : chacun a déjà sa phrase emphatique, et la séance "
                  "d'aujourd'hui lui donne les trois autres.")

    d.objectifs([
        "former le subjonctif présent de presque tous les verbes ;",
        "connaître les cinq irréguliers d'une demande ;",
        "choisir entre un connecteur de cause et un de conséquence ;",
        "écrire les quatre phrases d'une demande administrative.",
    ])

    d.regle("Trois entrées, et c'est tout",
            "Il faut que je travaille. Pour que le transfert se fasse. Bien que ce soit tard.",
            precision="L'obligation, le but, la concession : c'est tout ce qu'une "
                      "demande administrative a besoin de dire. Les trois demandent le "
                      "subjonctif, et il n'y en a pas d'autres à retenir pour ce "
                      "module.",
            notes="Diapositive à photographier. Ne pas présenter le subjonctif comme "
                  "un temps difficile : le présenter comme trois formules qui servent "
                  "à demander. Le reste vient plus tard, à un autre niveau.")

    d.tableau('Analyse', "Comment on le forme",
              ["La forme", "Ce qu'elle devient"],
              [["le radical du « ils » du présent", "ils travaillent : que je travaille"],
               ["les terminaisons", "-e, -es, -e, -ions, -iez, -ent"],
               ["neuf verbes sur dix", "ils écrivent : que j'écrive"],
               ["les cinq irréguliers", "sois · aie · aille · fasse · puisse"]],
              cle=1,
              note="Apprenez les cinq irréguliers comme cinq mots : ce sont exactement "
                   "ceux d'une demande.",
              notes="Diapositive à photographier. Faire fabriquer dix subjonctifs à "
                    "partir de dix formes en « ils », à la chaîne, à l'oral. "
                    "L'opération est mécanique et elle se retient en une séance.")

    d.piege("Confondre « je dois » et « il faut que »",
            "Je dois travailler le matin.",
            "Il faut que je travaille le matin.",
            "« Je dois » parle de vous ; « il faut que » parle d'une nécessité qui "
            "vient d'ailleurs — le loyer, l'employeur, la vie. Dans une demande, la "
            "seconde tournure explique sans se plaindre, et c'est pour cela qu'elle "
            "vaut la peine d'être apprise.",
            notes="Ce n'est pas une faute de grammaire : c'est un choix de ton. Le "
                  "nommer ainsi. Les deux phrases sont correctes, et elles ne font pas "
                  "le même effet sur la personne qui lit.")

    d.pratique('Grammaire', "Il faut que… : le subjonctif présent",
               "Mettez le verbe entre parenthèses au subjonctif.", [
        ("Il faut que je ___ (travailler) le matin pour payer mon loyer.", "travaille"),
        ("Pour que le transfert ___ (se faire), il vous faut une demande écrite.", "se fasse"),
        ("Il faut que vous ___ (être) au secrétariat avant seize heures.", "soyez"),
        ("Bien que le délai ___ (être) court, je remplirai le formulaire ce soir.", "soit"),
        ("Il faut que j'___ (aller) chercher mon attestation avant vendredi.", "aille"),
        ("Pour que je ___ (pouvoir) suivre le cours du soir, il faut changer mon groupe.", "puisse"),
    ], corrige=True, cols=2,
       notes="Ce sont les six items de l'exercice `t3sub`. Rappeler la règle qui sauve "
             "l'écrit : après « pour que », jamais d'infinitif — mais quand c'est la "
             "même personne des deux côtés, on écrit « pour » + infinitif.")

    d.cartes("Les six connecteurs d'une demande", "Ce que chacun annonce", [
        ("parce que — la raison, après",
         "Je demande un transfert parce que je travaille le matin. Le plus courant, "
         "et il ne commence jamais une lettre."),
        ("comme — la raison, avant",
         "Comme je travaille le matin, je ne peux plus suivre le cours de jour. La "
         "plus élégante à l'écrit : elle pose le décor."),
        ("donc, c'est pourquoi — ce qui en découle",
         "Je travaille le matin, donc je ne peux plus venir. « C'est pourquoi » est "
         "plus soutenu et convient mieux à l'écrit."),
        ("puisque, par contre",
         "« Puisque » pour une raison que l'autre connaît déjà. « Par contre » pour "
         "la nuance : c'est lui qui montre qu'on a réfléchi."),
    ], notes="Diapositive à photographier. « Puisque » employé pour une raison "
             "inconnue sonne comme un reproche : le signaler, c'est la seule chose "
             "qui puisse mal tourner dans une demande polie.")

    d.pratique('Écoute et réponds', "Une cause, ou une conséquence ?",
               "Dites si le connecteur introduit la raison ou ce qui en découle.", [
        ("Je demande un transfert parce que je travaille le matin.", "une cause"),
        ("Je travaille le matin, donc je ne peux plus venir le jour.", "une conséquence"),
        ("Comme mon horaire a changé, je vous écris aujourd'hui.", "une cause"),
        ("Mon absence était motivée, c'est pourquoi ma place a été gardée.", "une conséquence"),
        ("Puisque le formulaire est en ligne, je l'ai rempli hier soir.", "une cause"),
        ("Le délai est de dix jours, donc j'aurai une réponse le 14.", "une conséquence"),
    ], corrige=True, cols=2,
       notes="Six des huit items de `t3con`. Le test se fait sans grammaire : la "
             "raison répond à « pourquoi ? », la conséquence répond à « et alors ? ».")

    d.regle("Une demande tient en quatre phrases",
            "Qui je suis · ce qui bloque · pourquoi · ce que je demande, et à partir de quand.",
            precision="Le motif de la lettre est dans la première phrase, pas dans la "
                      "dernière : la personne qui la lit en a quarante autres devant "
                      "elle. Et toujours une date — une demande sans date oblige "
                      "quelqu'un à vous rappeler pour l'obtenir.",
            notes="Diapositive à photographier et à laisser affichée pendant "
                  "l'écriture. C'est la structure de la production écrite de E2 : elle "
                  "s'installe ici ou nulle part.")

    d.pratique('Écriture', "Les quatre phrases d'une demande",
               "Une phrase complète par consigne, sur votre propre situation.", [
        ("1 — Qui vous êtes et ce que vous demandez.",
         "Je m'appelle…, groupe…, et je vous écris pour demander un changement de groupe."),
        ("2 — Ce qui vous bloque, en une phrase emphatique.",
         "Ce qui me bloque, c'est l'horaire du matin."),
        ("3 — Votre raison, en commençant par « Comme ».",
         "Comme j'ai commencé un emploi qui débute à sept heures, je ne peux plus suivre le cours de jour."),
        ("4 — Votre demande, avec « il faut que » ou « pour que », et une date.",
         "Pour que je puisse continuer, je vous demande un transfert au groupe du soir à partir du 20 avril."),
    ], corrige=True,
       notes="Ce sont les quatre premières consignes de l'exercice `t3ecrit`. Les "
             "corrigés sont des modèles, pas des réponses : lire trois productions "
             "d'élèves avant de les afficher. La cinquième consigne — la question "
             "glissée sur le délai — se travaille en E1 avec le message vocal.")

    d.billet(
        "Écrivez la formule de fin de votre demande, puis ce que vous mettez sous votre nom.",
        exemples=[
            "Je vous remercie de votre attention. Veuillez agréer mes salutations distinguées.",
            "Votre nom, votre groupe, et un numéro où l'on peut vous joindre.",
        ],
        notes="Deux lignes qui ne se réinventent pas : les faire recopier telles "
              "quelles. Le numéro de téléphone est ce qu'on oublie, et c'est ce qui "
              "empêche la réponse d'arriver.")

    return d.save(dossier)
