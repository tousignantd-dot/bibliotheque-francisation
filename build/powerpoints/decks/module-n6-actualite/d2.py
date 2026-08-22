# -*- coding: utf-8 -*-
"""D2 · Si, à mon avis, cette machine
Bloc D « Défi 3 · Le courrier des lecteurs » · couleur teal · 75 min.
Source : exercices `t3si`, `t3pdv` et `t3subst`, avec leurs mini-leçons
« L'hypothèse avec si », « Annoncer un avis comme un avis » et « Reprendre un
mot sans le redire ».
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='D2', section='teal',
        titre="Si, à mon avis, cette machine",
        chapeau="Trois outils, et une seule fin : écrire une opinion qui se "
                "discute. Poser une hypothèse plutôt qu'accuser, annoncer "
                "son avis comme un avis, et ne pas répéter trois fois le "
                "même mot.",
        duree='75 minutes')

    d.titre(notes="Dernière séance du Défi 3, et dernière séance de grammaire du "
                  "module. Tout ce qui s'y fait sert directement au courriel de E2 : le "
                  "dire au début, ça change l'attention du groupe.")

    d.objectifs([
        "poser une hypothèse réaliste avec « si » et le présent ;",
        "ne jamais mettre de futur après « si » ;",
        "annoncer un avis avec à mon avis, pour ma part, selon moi ;",
        "reprendre un mot sans le répéter, par un synonyme ou un nom.",
    ], notes="Le deuxième objectif est une correction, pas une acquisition : la faute "
             "est déjà installée chez presque tout le monde. La nommer explicitement.")

    d.declencheur(
        'Observation', "Pourquoi « si » plutôt qu'une accusation ?",
        pistes=[
            "« Si les gens savaient que ça marche, ils écriraient. »",
            "Est-ce que cette phrase accuse quelqu'un ?",
            "Comment la dirait-on en accusant ?",
            "Laquelle des deux versions ferait publier la lettre ?",
        ],
        notes="La dernière question a une réponse claire : la version avec « si ». "
              "Toutes les lettres d'opinion en sont pleines, et c'est exactement pour "
              "cette raison.")

    d.tableau('Analyse', "L'hypothèse en « si » : trois suites possibles",
              ['Après « si »', 'Dans l\'autre partie'],
              [["si + présent", "présent : si tu gardes ta facture, tu as une preuve"],
               ["si + présent", "futur : si le marchand refuse, vous écrirez"],
               ["si + présent", "impératif : si ça ne bouge pas, écrivez-lui"],
               ["si + passé composé", "présent : si vous avez gardé la facture, vous pouvez"]],
              cle=0,
              note="Jamais de futur après « si ». C'est la faute la plus fréquente, et elle s'entend tout de suite.",
              notes="Diapositive à photographier. Écrire la note en gros au tableau et "
                    "l'y laisser toute la séance. La règle est simple ; c'est "
                    "l'automatisme qui est long.")

    d.regle("« si » n'est pas toujours une condition",
            "Il demande à Nadège si le marchand a rappelé.",
            precision="Ici, « si » ne pose aucune hypothèse : il rapporte une question. "
                      "C'est une interrogation indirecte, et le verbe suit le temps du "
                      "récit, sans aucune restriction. Le repère : s'il y a un verbe de "
                      "parole ou de pensée avant - demander, savoir, se demander - il "
                      "ne s'agit pas d'une condition.",
            notes="Diapositive à photographier. Le groupe qui vient d'apprendre "
                  "l'interdiction du futur après « si » va la surappliquer ici. "
                  "L'annoncer avant que ça arrive.")

    d.pratique('Grammaire', "Poser une condition avec « si »",
               "Attention : le verbe à trouver n'est pas toujours celui qui suit « si ».", [
        ("Si le marchand ... (refuser), vous écrirez une mise en demeure.", "refuse"),
        ("Si les gens savaient que ça marche, ils ... (écrire) plus souvent.", "écriraient"),
        ("Si vous ... (garder) votre facture, vous pouvez réclamer aujourd'hui.", "avez gardé"),
        ("Si ça ne bouge pas, ... (écrire) une mise en demeure.", "écrivez"),
        ("Si l'appareil ... (avoir) trois ans, la garantie légale court encore.", "a"),
        ("Il m'a demandé si le commerçant ... (rappeler) depuis.", "avait rappelé"),
    ], corrige=True, cols=2,
       notes="Le dernier est le piège de l'interrogation indirecte. Le laisser tomber "
             "sans prévenir : l'erreur du groupe rend la règle mémorable.")

    d.tableau('Analyse', "Annoncer que ce qui suit est un avis",
              ['Le connecteur', 'Ce qu\'il fait'],
              [["à mon avis, selon moi", "les plus courants, en tête de phrase"],
               ["pour ma part", "annonce souvent un désaccord poli"],
               ["personnellement, à mon sens", "insiste sur la personne qui parle"],
               ["selon, d'après + un nom", "rapporte l'avis d'un autre, sans s'engager"],
               ["paraît-il", "prend ses distances : on me l'a dit, je n'en réponds pas"]],
              cle=0,
              note="Un seul suffit. Ne pas les empiler : « à mon avis, je pense personnellement que » se lit mal.",
              notes="Diapositive à photographier. Faire chercher dans les deux lettres "
                    "de D1 lequel chacune emploie : Provencher « à mon avis », "
                    "Berthiaume « pour ma part ». Ce n'est pas un hasard.")

    d.pratique('Grammaire', "Le connecteur de point de vue qui convient",
               "Chacun ne sert qu'une fois.", [
        ("... , on demande beaucoup trop aux consommateurs.", "à mon avis"),
        ("... , je ne partage pas l'avis exprimé la semaine dernière.", "pour ma part"),
        ("... le Service de sécurité incendie, le feu serait parti du sous-sol.", "selon"),
        ("L'appareil était irréparable, ... .", "paraît-il"),
        ("... , je trouve que trois ans, c'est court pour une laveuse.", "personnellement"),
        ("... moi, la vraie question est celle des pièces de rechange.", "selon"),
    ], corrige=True, cols=2,
       notes="Le troisième et le sixième emploient tous deux « selon », mais l'un "
             "rapporte un organisme et l'autre soi-même. Faire remarquer la nuance : "
             "elle décide de qui s'engage.")

    d.tableau('Analyse', "Reprendre un mot sans le redire",
              ['Le procédé', 'L\'exemple'],
              [["Un synonyme", "la laveuse, l'appareil, la machine"],
               ["Un terme plus général", "une laveuse, une sécheuse, ces électroménagers"],
               ["Un nom tiré du verbe", "le marchand a refusé, devant ce refus"],
               ["Un démonstratif", "j'ai écrit une lettre. Cette lettre est restée sans réponse"]],
              cle=0,
              note="Le piège : réparer et remplacer ne sont pas synonymes, et c'est toute la question du module.",
              notes="Diapositive à photographier. Le troisième procédé - la "
                    "nominalisation - est le plus difficile et le plus utile à l'écrit. "
                    "Y consacrer le temps qui reste.")

    d.pratique('Vocabulaire', "Ne pas répéter le même mot trois fois",
               "Un seul mot par trou.", [
        ("Ma laveuse a brisé. Cette ... avait trois ans.", "machine, ou appareil"),
        ("Le marchand a refusé. Devant ce ... , j'ai écrit à l'Office.", "refus"),
        ("J'ai demandé une réparation. Ma ... est restée sans réponse.", "demande"),
        ("Le technicien est venu deux fois. Cette ... n'a rien réglé.", "visite"),
        ("Le feu a détruit deux logements. Cet ... a fait six sinistrés.", "incendie"),
        ("Elle a choisi d'écrire. Elle a ... pour la lettre plutôt que le téléphone.", "opté"),
    ], corrige=True, cols=2,
       notes="Les items 2, 3 et 4 sont des nominalisations. Les faire construire à voix "
             "haute à partir du verbe : refuser donne refus, demander donne demande, "
             "venir donne visite. Le dernier surprend : ce n'est pas « venue ».")

    d.billet(
        "Écris la première phrase de ta lettre au Courrier de la Batture.",
        exemples=[
            "Une formule d'appel, puis une phrase.",
            "Commence par ce que la chronique disait, pas par ton avis.",
        ],
        notes="Trois minutes. Ce billet est la vraie première ligne du courriel de E2 : "
              "le ramasser, le corriger et le rendre en E1. Le module se referme sur "
              "ces phrases-là.")

    return d.save(dossier)
