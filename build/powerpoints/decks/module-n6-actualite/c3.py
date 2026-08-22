# -*- coding: utf-8 -*-
"""C3 · Le passé simple : le reconnaître, jamais l'écrire
Bloc C « Défi 2 · L'entrevue et le documentaire » · couleur teal · 75 min.
Source : extrait de documentaire dans le dialogue `t2`, exercice `t2ps` et sa
mini-leçon « Le passé simple : le reconnaître, jamais l'écrire ».
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C3', section='teal',
        titre="Le passé simple : le reconnaître, jamais l'écrire",
        chapeau="« Ils se réunirent. L'entente dura seize ans. » C'est le "
                "temps des documentaires et des livres d'histoire. Personne, "
                "au Québec, ne le parle - et tout le monde le lit.",
        duree='75 minutes')

    d.titre(notes="Troisième séance du Défi 2. Dire d'entrée de jeu ce que le programme "
                  "demande : reconnaître, et rien de plus. Aucun élève n'aura jamais à "
                  "écrire un passé simple. Le dire enlève la moitié de l'angoisse.")

    d.objectifs([
        "reconnaître un verbe au passé simple à la troisième personne ;",
        "lui donner son équivalent au passé composé ;",
        "identifier les trois terminaisons les plus fréquentes ;",
        "connaître par cœur il fut, il eut et ils firent.",
    ], notes="Objectifs volontairement modestes et entièrement passifs. Ne rien "
             "demander de plus, même aux élèves rapides : leur donner plutôt d'autres "
             "verbes à reconnaître.")

    d.declencheur(
        'Observation', "Ces verbes, tu les as déjà entendus ?",
        pistes=[
            "« Les fabricants se réunirent à Genève. »",
            "« L'entente dura seize ans. »",
            "« Elle ne fut connue que bien plus tard. »",
            "Est-ce que quelqu'un parle comme ça, autour de toi ?",
        ],
        notes="La quatrième question a une seule réponse : personne. Le faire dire par "
              "le groupe plutôt que par soi. Ce temps existe uniquement à l'écrit et "
              "dans les récits lus à voix haute.")

    d.dialogue('Documentaire', "Le temps des choses, extrait", [
        ("NARRATRICE", "En mille neuf cent vingt-quatre, les fabricants d'ampoules se réunirent à Genève et fixèrent ensemble une durée de vie maximale de mille heures.", True),
        ("NARRATRICE", "L'entente dura seize ans.", True),
        ("NARRATRICE", "Elle ne fut connue du public que bien plus tard, quand des chercheurs retrouvèrent les documents dans des archives d'entreprise.", True),
    ], consigne="Trois phrases, six verbes au passé simple. Écoutez d'abord.",
       notes="Faire écouter deux fois. À la deuxième écoute, demander de lever la main "
             "chaque fois qu'un verbe sonne étrange : le groupe repère les six sans "
             "connaître la règle.")

    d.tableau('Analyse', "Trois familles à repérer",
              ['La terminaison', 'Les verbes concernés'],
              [["il -a, ils -èrent", "les verbes en -er : il fixa, ils fixèrent"],
               ["il -it, ils -irent", "les verbes en -ir : il finit, ils finirent"],
               ["il -ut, ils -urent", "quelques verbes courants : il fut, ils furent"]],
              cle=0,
              note="Trois seulement à connaître par cœur : il fut (a été), il eut (a eu), ils firent (ont fait).",
              notes="Diapositive à photographier. Ne pas donner d'autre tableau de "
                    "conjugaison : les six formes de l'extrait suffisent, et le "
                    "programme n'en demande pas plus.")

    d.regle("Reconnaître, pas employer",
            "Tu n'auras jamais à écrire un passé simple. Tu auras souvent à en lire un.",
            precision="Il vit dans les documentaires, les romans et les livres "
                      "d'histoire. Jamais dans une conversation, jamais dans une "
                      "lettre, jamais dans un courriel. Quand tu en rencontres un, "
                      "traduis-le mentalement en passé composé et continue : ils se "
                      "réunirent, donc ils se sont réunis.",
            notes="Diapositive à photographier. Le geste de traduction mentale est la "
                  "seule stratégie à installer. Le faire pratiquer à voix haute sur les "
                  "six verbes de l'extrait.")

    d.pratique('Association', "Comme on le dirait en parlant",
               "Donnez l'équivalent au passé composé.", [
        ("les fabricants se réunirent", "les fabricants se sont réunis"),
        ("ils fixèrent une durée maximale", "ils ont fixé une durée maximale"),
        ("l'entente dura seize ans", "l'entente a duré seize ans"),
        ("elle ne fut connue que plus tard", "elle n'a été connue que plus tard"),
        ("des chercheurs retrouvèrent les documents", "des chercheurs ont retrouvé les documents"),
        ("le public eut la preuve sous les yeux", "le public a eu la preuve sous les yeux"),
    ], corrige=True,
       notes="Faire traduire à l'oral avant d'afficher. Le quatrième est le plus "
             "difficile : « fut connue » est un passif, et il faut garder le participe "
             "accordé au féminin.")

    d.piege("Confondre il fixa et il fixera",
            "En mille neuf cent vingt-quatre, ils fixeront une durée maximale.",
            "En mille neuf cent vingt-quatre, ils fixèrent une durée maximale.",
            "À l'oreille, un passé simple en -a ressemble à un futur, et « ils durent » "
            "du verbe durer ressemble à « ils durent » du verbe devoir. Le contexte "
            "tranche toujours : dans un documentaire qui raconte une date passée, c'est "
            "du passé simple. Une date au début de la phrase est le meilleur indice.",
            notes="Faire chercher l'indice dans la phrase fautive : la date de 1924 "
                  "rend le futur impossible. C'est un raisonnement, pas une "
                  "reconnaissance de forme, et c'est ce qu'on veut installer.")

    d.cartes("Où tu le rencontreras", "Et où tu ne le rencontreras jamais", [
        ("Dans un documentaire",
         "la voix hors champ raconte au passé simple, presque toujours."),
        ("Dans un roman, un livre d'histoire",
         "c'est le temps du récit écrit, depuis des siècles."),
        ("Jamais dans une conversation",
         "personne ne dit « je mangeai ». Ni ici, ni ailleurs."),
        ("Jamais dans une lettre ou un courriel",
         "même au courrier des lecteurs : on y écrit au passé composé."),
    ], notes="La quatrième carte importe pour E2 : un élève qui voudrait « faire "
             "sérieux » dans sa lettre pourrait être tenté. Le prévenir maintenant.")

    d.billet(
        "Traduis en français parlé : « L'entente dura seize ans. »",
        exemples=[
            "Une phrase, avec le passé composé.",
            "Et dis dans quel genre de texte tu as vu ce temps.",
        ],
        notes="Deux minutes. Un billet très court : la séance est dense et le groupe "
              "est fatigué. La réponse attendue tient en six mots.")

    return d.save(dossier)
