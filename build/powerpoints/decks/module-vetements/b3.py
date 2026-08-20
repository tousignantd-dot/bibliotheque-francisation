# -*- coding: utf-8 -*-
"""B3 · Décrire un vêtement.
Bloc B « Défi 1 » · couleur ambre · 60 min.
Source : mini-leçon `t1decrire`, exercice `t1decrire`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B3', section='ambre',
        titre='Décrire un vêtement',
        chapeau="Le vêtement, sa couleur, sa matière, sa longueur — et dans "
                "cet ordre. En français, l'adjectif suit presque toujours le "
                "nom, et les couleurs s'accordent.",
        duree='60 minutes')

    d.titre(notes="Séance de langue. Elle complète B2 : B2 dit ce qui ne va pas, B3 décrit "
                  "ce qu'on cherche.")

    d.objectifs([
        "placer l'adjectif après le nom ;",
        "accorder la couleur avec le vêtement ;",
        "employer « en » pour la matière ;",
        "enchaîner deux ou trois adjectifs.",
    ])

    d.declencheur(
        'Observation', "Laquelle de ces phrases est juste ?",
        pistes=[
            "« un noir manteau »",
            "« un manteau noir »",
            "« une veste grise en laine »",
            "« une grise veste »",
        ],
        notes="Faire choisir avant d'expliquer. Beaucoup de langues placent l'adjectif "
              "avant : l'erreur est prévisible et sans gravité.")

    d.regle("L'adjectif suit le nom",
            "un manteau noir, une veste grise, des bottes chaudes",
            precision="C'est la règle générale du français, et elle vaut pour toutes les "
                      "couleurs et toutes les matières. Quelques adjectifs très courants "
                      "font exception — <b>beau</b>, <b>grand</b>, <b>petit</b>, "
                      "<b>gros</b>, <b>nouveau</b> — et se placent avant : « un beau "
                      "manteau », « une petite veste ».",
            notes="Diapo à photographier. Ne pas allonger la liste des exceptions : ces "
                  "cinq suffisent pour parler de vêtements.")

    d.tableau('Analyse', "L'ordre des mots",
              ['La phrase', "Ce qu'on ajoute"],
              [["un manteau", "le vêtement"],
               ["un manteau noir", "+ la couleur"],
               ["un manteau noir en duvet", "+ la matière"],
               ["un manteau noir en duvet, long", "+ la longueur"]],
              cle=0,
              note="On ajoute par la droite, un morceau à la fois.",
              notes="Diapo centrale. Faire construire la même série avec « une veste », en "
                    "surveillant les accords.")

    d.tableau('Analyse', "La couleur s'accorde",
              ['Masculin', 'Féminin'],
              [["un manteau noir", "une veste noire"],
               ["un chandail gris", "une tuque grise"],
               ["un foulard vert", "une écharpe verte"],
               ["un pantalon blanc", "une jupe blanche"]],
              cle=3,
              note="Blanc / blanche est irrégulier : à retenir tel quel.",
              notes="Lien direct avec A2 : la consonne finale se réveille au féminin.")

    d.cartes("Les couleurs qui ne changent jamais", "Trois choses à savoir", [
        ("Celles qui finissent par -e",
         "rouge, jaune, beige, rose. « Un manteau rouge », « une veste rouge » : identique."),
        ("Celles qui viennent d'un objet",
         "marine, kaki, crème, turquoise, olive. Elles ne prennent rien : « des bottes "
         "marine », « une veste crème »."),
        ("Les couleurs en deux mots",
         "bleu foncé, vert pâle, gris clair. Elles ne s'accordent pas non plus : « une "
         "veste bleu foncé »."),
    ], notes="Ces trois cartes évitent la surcorrection. Les deux dernières familles "
             "surprennent, mais elles sont fréquentes dans les magasins.")

    d.regle("La matière : « en »",
            "un manteau en duvet, une veste en laine",
            precision="« En » introduit la matière : en laine, en coton, en duvet, en "
                      "cuir, en polyester, en nylon. On dit aussi « de laine », mais « en » "
                      "est le plus courant à l'oral, et c'est celui qu'on lit sur les "
                      "étiquettes.",
            notes="Diapo à photographier. Faire lire l'étiquette d'un vêtement porté en "
                  "classe : la composition y est écrite.")

    d.piege("Accorder ce qui ne s'accorde pas",
            "des bottes marines, une veste beige foncée",
            "des bottes marine, une veste beige foncé",
            "Une fois la règle de l'accord apprise, on l'applique partout. Or les couleurs "
            "venues d'un nom d'objet et les couleurs en deux mots restent invariables. "
            "C'est l'erreur du bon élève.",
            notes="Ne pas dramatiser : c'est une faute d'écrit, invisible à l'oral.")

    d.pratique('Pratique · 1 de 2', "Remettez dans l'ordre",
               "Écrivez la phrase correcte.", [
        ("noir / manteau / un", "un manteau noir"),
        ("grise / veste / une / laine / en", "une veste grise en laine"),
        ("chaudes / bottes / des", "des bottes chaudes"),
        ("bleu / chandail / un / foncé", "un chandail bleu foncé"),
    ], corrige=True, cols=1,
       notes="Faire écrire, puis corriger au tableau.")

    d.pratique('Pratique · 2 de 2', "Accordez la couleur",
               "Écrivez la forme juste.", [
        ("une veste (vert)", "verte"),
        ("des bottes (noir)", "noires"),
        ("une tuque (gris)", "grise"),
        ("une écharpe (rouge)", "rouge — invariable"),
        ("des gants (marine)", "marine — invariable"),
        ("une jupe (blanc)", "blanche"),
    ], corrige=True,
       notes="Les deux invariables sont volontairement mêlées aux autres.")

    d.billet(
        "Décrivez trois vêtements que vous portez aujourd'hui.",
        exemples=[
            "Nom, couleur, matière — dans cet ordre.",
            "Au moins un féminin et un masculin.",
        ],
        notes="Court et immédiat. Les élèves ont la réponse sur eux.")

    return d.save(dossier)
