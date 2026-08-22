# -*- coding: utf-8 -*-
"""D1 · L'Écho de la Yamaska, et le temps qu'on ne parle pas
Bloc D « Défi 3 · L'article qu'on transmet » · couleur acier · 75 min.
Source : dialogue `t3`, exercices `t3art` (type texte), `t3vf` et `t3ps` et
leurs mini-leçons — l'article de quartier et le passé simple, que le
programme demande de reconnaître et non de produire.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='D1', section='acier',
        titre="L'Écho de la Yamaska, et le temps qu'on ne parle pas",
        chapeau="Tout commença dans un sous-sol d'église, en 1998. Personne "
                "ne parle comme ça — et pourtant les journaux l'écrivent "
                "tous les jours.",
        duree='75 minutes')

    d.titre(notes="Ouverture du Défi 3. Apporter un vrai journal de quartier si "
                  "possible, et le faire circuler pendant les cinq premières minutes. "
                  "La plupart des élèves n'en ont jamais ouvert un.")

    d.objectifs([
        "trouver dans un article de quartier où se cache chaque information ;",
        "reconnaître un passé simple et le remplacer par un passé composé ;",
        "distinguer un fait d'une parole rapportée ;",
        "employer les quatre mots du Défi 3 avec leur article.",
    ], notes="Le deuxième objectif est de reconnaissance seulement. Ne jamais faire "
             "produire un passé simple : ce n'est pas ce que le programme demande, et "
             "ce n'est utile à personne.")

    d.declencheur(
        'Observation', "Qu'est-ce qu'un journal de quartier publie ?",
        pistes=[
            "En as-tu déjà reçu un dans ta boîte aux lettres ?",
            "Qu'est-ce qu'on y trouve qu'on ne trouve pas ailleurs ?",
            "Qui l'écrit, à ton avis ?",
            "Y a-t-il quelque chose de semblable dans ton pays d'origine ?",
        ],
        notes="Le journal de quartier est un objet québécois très courant et très mal "
              "connu des nouveaux arrivants. Prendre le temps : il porte des services "
              "réels.")

    d.dialogue('Dialogue · 1 de 3', "Comme les journaux écrivent", [
        ("GHISLAIN", "Marisol, tu as vu L'Écho de la Yamaska de cette semaine ? Il y a un article sur la fête où on était samedi.", True),
        ("MARISOL", "Non, montrez-moi. Ah, ils ont mis une photo du parc.", True),
        ("GHISLAIN", "Lis le début. C'est écrit comme les journaux écrivent quand ils racontent une histoire ancienne.", True),
        ("NARRATRICE", "Tout commença dans un sous-sol d'église, en 1998. Une dizaine de familles se réunirent un jeudi soir. Elles ne se quittèrent plus.", True),
    ], consigne="Écouter d'abord, diapositive masquée.",
       notes="La voix de la narratrice lit les passages écrits : c'est un choix du "
             "module. Le dire au groupe — on n'entend jamais ce temps dans une "
             "conversation.")

    d.dialogue('Dialogue · 2 de 3', "Un temps qui met de la distance", [
        ("MARISOL", "Se réunirent, ne se quittèrent plus… Je comprends le sens, mais personne ne parle comme ça.", True),
        ("GHISLAIN", "Personne, non. Dans ta tête, tu le remplaces par le passé composé : elles se sont réunies. C'est la même chose.", True),
        ("MARISOL", "Et pourquoi l'écrire comme ça, alors ?", True),
        ("GHISLAIN", "Parce que ça met de la distance. Ça dit : c'est fini, c'est loin, c'est de l'histoire.", True),
    ], notes="La dernière réplique est la seule explication à donner. Ne pas entrer "
             "dans la conjugaison complète : quatre formes suffisent.")

    d.dialogue('Dialogue · 3 de 3', "Deux sortes de guillemets", [
        ("NARRATRICE", "Ce n'est pas du bénévolat au sens habituel, précise la coordonnatrice. Les deux familles apprennent, et personne n'est là pour aider l'autre.", True),
        ("MARISOL", "Pourquoi il y a des guillemets autour de duos et de parrainage ?", True),
        ("GHISLAIN", "Ce ne sont pas les mêmes. Les premiers rendent à la coordonnatrice ses mots exacts.", True),
        ("GHISLAIN", "Les autres, autour d'un seul mot, veulent dire : c'est le mot de l'organisme, pas le mien.", True),
    ], notes="Ces deux emplois se retravaillent en D2. Ici, il suffit que le groupe "
             "voie qu'il y en a deux.")

    d.vocabulaire('Vocabulaire', "Les quatre mots du Défi 3", [
        ("un jumelage", "Le fait de mettre ensemble deux familles pour qu'elles se rencontrent régulièrement."),
        ("un organisme communautaire", "Un groupe du quartier, sans but de profit, qui organise des services."),
        ("un bénévole", "Une personne qui donne son temps sans être payée."),
        ("une coordonnatrice", "La personne qui organise le travail des autres et parle au nom de l'organisme."),
    ], notes="Ces quatre mots ouvrent des portes réelles à Saint-Hyacinthe comme "
             "ailleurs. Donner l'adresse d'un organisme du quartier si le groupe en a "
             "un.")

    d.tableau('Analyse', "Où se cache chaque information",
              ['La question', 'Où chercher'],
              [["De quand date l'organisme", "premier paragraphe"],
               ["Ce qui se lance cet automne", "deuxième paragraphe"],
               ["Combien de temps ça dure", "deuxième paragraphe"],
               ["Qui parle, et pour dire quoi", "troisième paragraphe, entre guillemets"],
               ["Jusqu'à quand s'inscrire", "dernier paragraphe"]],
              cle=0,
              note="Pour une date limite, on commence toujours par la fin.",
              notes="Diapositive à photographier. Les élèves referont l'exercice à "
                    "l'écran, en cliquant dans le texte de l'article.")

    d.pratique('Grammaire', "Que dirais-tu, toi ?",
               "Le journal écrit à gauche. Dites la forme que vous emploieriez.", [
        ("tout commença", "tout a commencé"),
        ("elles se réunirent", "elles se sont réunies"),
        ("elles ne se quittèrent plus", "elles ne se sont plus quittées"),
        ("il fut le premier président", "il a été le premier président"),
        ("le quartier fit sa fête", "le quartier a fait sa fête"),
        ("vingt familles vinrent", "vingt familles sont venues"),
    ], corrige=True, cols=2,
       notes="Les quatre formes à retenir par cœur sont il fut, il eut, il fit, il "
             "vint. Les écrire au tableau et les y laisser jusqu'à la fin du bloc.")

    d.billet(
        "Note une phrase de l'article que tu ne dirais jamais à l'oral.",
        exemples=[
            "Recopie-la telle quelle.",
            "Écris à côté comment tu la dirais.",
        ],
        notes="Deux minutes. Les billets servent en D2 : ils montrent ce que le groupe "
              "a repéré tout seul de la langue écrite.")

    return d.save(dossier)
