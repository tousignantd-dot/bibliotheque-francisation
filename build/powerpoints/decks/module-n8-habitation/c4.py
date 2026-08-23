# -*- coding: utf-8 -*-
"""C4 · Ce qui serait arrivé si le motif était le bon
Bloc C « Défi 2 · L'appel qui conteste » · couleur teal · 75 min.
Source : exercice `t2irr` et sa mini-leçon.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C4', section='teal',
        titre="L'hypothèse irréelle, l'arme tranquille",
        chapeau="Contredire quelqu'un l'oblige à se défendre. L'hypothèse "
                "irréelle accepte ce qu'il affirme, en déroule la "
                "conséquence, et laisse voir qu'elle ne s'est pas produite.",
        duree='75 minutes')

    d.titre(notes="Dernière séance du bloc C, et la forme grammaticale la plus utile "
                  "du module. Annoncer d'emblée ce qu'elle permet : faire tomber un "
                  "argument sans rien nier et sans mettre personne en cause.")

    d.objectifs([
        "distinguer les deux montages : sur le présent, sur le passé ;",
        "n'employer jamais le conditionnel après « si » ;",
        "ajouter le fait qui montre que la conséquence est absente ;",
        "reconnaître une condition exprimée sans « si ».",
    ], notes="Le troisième objectif est celui qu'on oublie et sans lequel toute la "
             "démonstration s'effondre : une hypothèse seule n'est qu'une "
             "supposition.")

    d.declencheur(
        'Raisonnement', "Si le drain avait été bouché depuis des années, que se serait-il passé ?",
        pistes=[
            "L'eau serait-elle montée seulement le 14 septembre ?",
            "Que se serait-il passé aux grosses pluies des années précédentes ?",
            "Est-ce arrivé ? Comment le sait-on ?",
            "Est-ce qu'on vient de contredire l'expert, ou de faire autre chose ?",
        ],
        notes="La dernière question est le cœur de la séance : on n'a rien contredit. "
              "On a accepté l'affirmation de l'expert et on a montré où elle mène. "
              "Le faire dire par le groupe avant de l'expliquer.")

    d.regle("Deux montages, et on ne les mélange pas",
            "Sur le présent : si + imparfait, puis conditionnel présent. Sur "
            "le passé : si + plus-que-parfait, puis conditionnel passé.",
            precision="Jamais de conditionnel après « si ». C'est la faute la plus "
                      "connue du français et la plus vite remarquée : « si "
                      "j'aurais su » se corrige en une seconde et se remarque en "
                      "moins que ça.",
            notes="Diapositive à photographier. Faire répéter les deux montages en "
                  "chœur, une fois. Ils tiennent en dix mots et ils servent partout.")

    d.tableau('Formes', "La condition et sa conséquence",
              ['Si… (la condition)', '… (la conséquence)'],
              [["Si j'étais couverte", "je recevrais l'indemnité"],
               ["Si la lettre nommait le bon drain", "la décision se comprendrait mieux"],
               ["Si le drain avait été bouché", "l'eau serait remontée bien avant"],
               ["Si on m'avait demandé la facture", "je l'aurais envoyée le premier jour"],
               ["Si l'expert avait passé une caméra", "il aurait vu que le drain était libre"]],
              cle=0,
              notes="Diapositive à photographier. Les deux premières lignes sont sur le "
                    "présent, les trois autres sur le passé. Faire trouver la coupure "
                    "au groupe avant de la dire.")

    d.regle("Une hypothèse seule ne prouve rien",
            "« Si le drain avait été bouché depuis des années, l'eau serait "
            "remontée bien avant. » Il manque une phrase, et c'est elle qui "
            "fait l'argument : « et aucune remontée n'est survenue depuis "
            "2019. »",
            precision="Sans le fait qui constate l'absence de la conséquence, vous "
                      "n'avez énoncé qu'une supposition — et une supposition ne se "
                      "verse à aucun dossier.",
            notes="Diapositive à photographier. C'est la deuxième moitié de la "
                  "technique, et celle que tout le monde oublie. La faire écrire.")

    d.pratique('Grammaire', "Mettez le verbe au temps de l'irréel",
               "Rien de tout cela ne s'est produit.", [
        ("Si le drain avait été bouché depuis des années, l'eau ___ (remonter) bien avant.", "serait remontée"),
        ("Si on m'avait demandé la facture, je l'___ (envoyer) le premier jour.", "aurais envoyée"),
        ("Si l'expert avait passé une caméra, il ___ (voir) que le drain était libre.", "aurait vu"),
        ("Si l'obstruction ___ (être) progressive, elle aurait laissé des traces.", "avait été"),
        ("Si j'étais couverte pour ce sinistre, je ___ (recevoir) dix-huit mille quatre cents dollars.", "recevrais"),
        ("Si le service avait examiné la contre-expertise, il ___ (rouvrir) le dossier.", "aurait rouvert"),
    ], corrige=True,
       notes="Le quatrième est le test : c'est celui où l'on est tenté d'écrire "
             "« aurait été » après « si ». Le laisser se produire, puis corriger.")

    d.cartes('Analyse', "La condition sans « si »", [
        ("Par un gérondif",
         "« En passant une caméra, on aurait su tout de suite. » La "
         "condition est dans le gérondif, et la conséquence au conditionnel "
         "passé."),
        ("Par un infinitif",
         "« À lire le rapport, on comprend l'inverse de la lettre. » Forme "
         "soutenue, fréquente à l'écrit administratif."),
        ("Par un conditionnel seul",
         "« Un drain bouché depuis dix ans aurait débordé plus tôt. » La "
         "condition n'est même pas énoncée : elle est contenue dans le "
         "sujet. C'est la plus élégante des trois."),
    ], cols=1,
       notes="Le niveau 8 demande de les reconnaître, pas nécessairement de les "
             "produire. Faire relever la troisième dans le module : elle y est.")

    d.piege(
        'Irréel du passé',
        "Se contenter de dire « ce n'est pas vrai »",
        "Dérouler ce qui serait arrivé, puis constater que ce n'est pas arrivé",
        "Nier oblige l'autre à se défendre, et une contestation qui nie "
        "quatre pages d'expertise se lit comme un refus de comprendre. "
        "L'hypothèse irréelle fait exactement l'inverse : elle accepte "
        "l'affirmation de l'expert, en tire la conséquence logique, et "
        "montre que le monde ne s'est pas comporté ainsi. Personne n'a été "
        "mis en cause, et l'argument est tombé tout seul.",
        notes="Faire reformuler la différence par un élève avant de conclure la "
              "séance. C'est l'idée la plus transférable du module.")

    d.billet(
        "Écrivez deux phrases d'hypothèse irréelle sur le dossier de Teodora.",
        exemples=[
            "La première sur le passé : si… avait été…, … se serait produit.",
            "La seconde est le fait qui montre que ça ne s'est pas produit.",
        ],
        notes="Ces deux phrases entrent telles quelles dans la lettre du bloc E. À la "
              "fin du bloc C, chaque élève a donc écrit sa concession et son "
              "hypothèse : la moitié de sa lettre est faite.")

    return d.save(dossier)
