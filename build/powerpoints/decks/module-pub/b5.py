# -*- coding: utf-8 -*-
"""B5 · Les suffixes.
Bloc B · couleur ambre (écriture) · 60 min.
Source : exercice `t1suffixe` et sa mini-leçon.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B5', section='ambre',
        titre='Les suffixes',
        chapeau="« Réparer » donne « réparable », « réparateur », « réparation ». Un "
                "verbe, et trois mots nouveaux — sans jamais ouvrir de dictionnaire.",
        duree='60 minutes')

    d.titre(notes="Écrire « réparer » au tableau et demander au groupe tous les mots de "
                  "la même famille. Il en viendra quatre ou cinq : c'est la séance.")

    d.objectifs([
        "reconnaître un suffixe et ce qu'il fabrique ;",
        "connaître cinq suffixes courants ;",
        "former un adjectif ou un nom à partir d'un verbe ;",
        "deviner la nature d'un mot grâce à son suffixe.",
    ])

    d.regle('La règle',
            "Un suffixe se place à la fin et fabrique un mot d'une autre nature.",
            precision="« Réparer » est un verbe. « Réparable » est un adjectif. "
                      "« Réparation » est un nom. Le suffixe ne change pas seulement le "
                      "sens : il change ce que le mot est.",
            notes="C'est la différence avec le préfixe : celui-ci change le sens, "
                  "celui-là change la nature. Le dire explicitement.")

    d.tableau('Analyse', "Cinq suffixes",
              ['Le suffixe', 'Il fabrique', 'Un exemple'],
              [["-able", "un adjectif", "réparer donne réparable"],
               ["-eur, -euse", "un nom de personne", "bricoler donne bricoleur"],
               ["-té", "un nom", "solide donne solidité"],
               ["-ance", "un nom", "confiant donne confiance"],
               ["-age", "un nom", "coller donne collage"]],
              cle=0, props=[0.22, 0.28, 0.5],
              notes="Quatre des cinq fabriquent des noms. Le faire remarquer : le suffixe "
                    "sert surtout à transformer une action en chose.")

    d.cartes('En apprendre plus', "Quatre choses à savoir en plus", [
        ("« -able » veut dire « qu'on peut »",
         "Réparable : qu'on peut réparer. Jetable : qu'on peut jeter. Lavable, "
         "buvable, faisable. Le sens est toujours le même."),
        ("« -eur » a un féminin",
         "Bricoleur donne bricoleuse. Réparateur donne réparatrice. Animateur donne "
         "animatrice. Les deux formes existent."),
        ("Le radical change parfois",
         "« Solide » donne « solidité », pas « solideté ». Le mot de base s'ajuste un "
         "peu. C'est fréquent avec -té."),
        ("Deviner la nature d'un mot",
         "Un mot en -able est un adjectif. Un mot en -tion, -té, -ance, -age est un "
         "nom. Cela aide à lire une phrase difficile."),
    ], notes="La quatrième carte est un outil de lecture : reconnaître la nature d'un "
             "mot inconnu permet de comprendre la structure de la phrase.")

    d.pratique('Pratique · 1 de 4', "Formez le mot",
               "Ajoutez le suffixe demandé.", [
        ("réparer (un adjectif)", "réparable"),
        ("bricoler (un nom de personne)", "bricoleur, bricoleuse"),
        ("solide (un nom)", "solidité"),
        ("confiant (un nom)", "confiance"),
        ("jeter (un adjectif)", "jetable"),
        ("animer (un nom de personne)", "animateur, animatrice"),
    ], corrige=True,
       notes="Faire nommer la nature du mot demandé avant d'écrire. C'est ce qui guide "
             "le choix du suffixe.")

    d.pratique('Pratique · 2 de 4', "Trois mots par verbe",
               "Un adjectif, un nom de personne, un nom d'action.", [
        ("réparer", "réparable · réparateur · réparation"),
        ("animer", "animable (rare) · animateur · animation"),
        ("coller", "collable (rare) · colleur · collage"),
        ("laver", "lavable · laveur · lavage"),
    ], corrige=True,
       notes="Certaines cases restent vides ou rares : c'est normal. Tous les verbes ne "
             "donnent pas les trois. Le dire.")

    d.piege("Le piège du suffixe qui n'existe pas",
            "solideté, confiantance",
            "solidité, confiance",
            "Le mot de base s'ajuste souvent avant le suffixe : « solide » perd son e et "
            "devient « solidi- », « confiant » perd son t et devient « confi- ». Il n'y "
            "a pas de règle simple : ces mots s'apprennent un par un.",
            notes="Le dire honnêtement. Chercher une règle ici ferait perdre du temps : "
                  "ce sont des mots à mémoriser.")

    d.piege("Le piège du « -able » systématique",
            "Tous les verbes donnent un adjectif en -able.",
            "Beaucoup, mais pas tous.",
            "« Réparable », « lavable », « jetable » existent. « Marchable » ou "
            "« dormable » n'existent pas. Le suffixe -able s'emploie surtout avec les "
            "verbes qui ont un complément : on répare quelque chose, on lave quelque "
            "chose.",
            notes="Nuance utile et rarement enseignée : le critère est le complément. "
                  "L'expliquer avec trois exemples et passer.")

    d.pratique('Pratique · 3 de 4', "Quelle est la nature du mot ?",
               "D'après son suffixe.", [
        ("réparable", "un adjectif — suffixe -able"),
        ("réparation", "un nom — suffixe -tion"),
        ("réparatrice", "un nom de personne — suffixe -trice"),
        ("solidité", "un nom — suffixe -té"),
        ("bricolage", "un nom — suffixe -age"),
    ], corrige=True,
       notes="Cet exercice est un outil de lecture. Faire remarquer qu'on peut identifier "
             "la nature d'un mot sans en connaître le sens.")

    d.pratique('Pratique · 4 de 4', "Écrivez la phrase",
               "Employez le mot formé.", [
        ("réparable", "Ce grille-pain est encore réparable."),
        ("bricoleuse", "Ma voisine est une excellente bricoleuse."),
        ("solidité", "La solidité de cette chaise m'étonne."),
        ("collage", "Le collage a tenu toute la semaine."),
    ], corrige=True,
       notes="Faire lire les phrases à voix haute. Un mot bien formé mais mal employé se "
             "repère tout de suite à l'oral.")

    d.billet(
        "Choisissez un verbe et fabriquez-en trois mots.",
        exemples=[
            "Un adjectif, un nom de personne, un nom d'action.",
            "Puis une phrase avec chacun des trois.",
        ],
        notes="Corriger la forme et l'emploi. Rendre avant C1 : les affiches du défi 2 "
              "contiennent plusieurs mots dérivés.")

    return d.save(dossier)
