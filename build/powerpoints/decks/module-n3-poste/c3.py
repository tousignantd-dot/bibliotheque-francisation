# -*- coding: utf-8 -*-
"""C3 · Je vais le prendre, je vais en prendre trois.
Bloc C « Défi 2 · Dire ce qu'il y a dedans, et payer » · couleur teal · 75 min.
Source : mini-leçons `t2pron` et `t2donnez`, exercices `t2pron` et `t2donnez`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C3', section='teal',
        titre='Je vais le prendre, je vais en prendre trois',
        chapeau="Quand la chose vient d'être nommée, on ne la répète pas : on "
                "la remplace par un petit mot. Et dès qu'on dit un nombre, ce "
                "petit mot est « en ».",
        duree='75 minutes')

    d.titre(notes="Séance de grammaire orale. C'est le point le plus abstrait du module : "
                  "tout se joue sur des exemples entendus, jamais sur la règle seule.")

    d.objectifs([
        "employer « le », « la », « les » pour une chose déjà nommée ;",
        "employer « en » dès qu'on dit un nombre ;",
        "placer le petit mot devant le verbe ;",
        "annoncer son choix au comptoir en trois mots.",
    ])

    d.regle("La phrase du défi 2",
            "Je vais le prendre.",
            precision="Trois mots, et le choix est fait. « Le » remplace « le "
                      "colis standard », que la préposée vient de nommer. On ne "
                      "répète pas le nom du service : ce serait long, et personne "
                      "ne le fait.",
            notes="Diapo à photographier. Faire jouer le contraste : « Je vais prendre "
                  "le colis standard » n'est pas faux, mais personne ne parle comme ça "
                  "au comptoir.")

    d.tableau('Analyse', "Quel petit mot ?",
              ['Ce qu\'on remplace', 'Le petit mot', 'La phrase'],
              [["le colis standard", "le", "Je vais le prendre."],
               ["cette enveloppe-là", "la", "Je vais la prendre."],
               ["les deux carnets", "les", "Je vais les prendre."],
               ["trois enveloppes", "en", "Je vais en prendre trois."]],
              cle=1,
              note="Dès qu'il y a un nombre dans la réponse, c'est « en ». Toujours.",
              notes="Diapo à photographier. La dernière ligne est la seule qui compte "
                    "vraiment : c'est celle que les élèves ne devinent jamais.")

    d.regle("La place du petit mot",
            "Je vais LE prendre.  ·  Je vais EN prendre trois.",
            precision="Il se met devant le verbe, jamais après. On ne dit pas "
                      "« je vais prendre le » ni « je vais prendre en trois ». "
                      "Cette place-là ne bouge pas, quel que soit le petit mot.",
            notes="Diapo à photographier. Faire répéter les deux phrases en frappant "
                  "dans les mains sur le petit mot : la place s'entend mieux qu'elle "
                  "ne s'explique.")

    d.pratique('Écriture', "Complétez avec « le », « la », « les » ou « en »",
               "Regardez ce que la préposée vient de nommer.", [
        ("« Le colis standard ? » — Oui, je vais ___ prendre.", "le"),
        ("« Cette enveloppe-là ? » — Oui, je vais ___ prendre.", "la"),
        ("« Des timbres ? » — Je vais ___ prendre douze.", "en — il y a un nombre"),
        ("« Les deux carnets ? » — Je vais ___ prendre tous les deux.", "les"),
        ("« Un mandat-poste ? » — Je vais ___ prendre un, s'il vous plaît.", "en — il y a un nombre"),
        ("« Le reçu ? » — Oui, je vais ___ garder.", "le"),
    ], corrige=True,
       notes="C'est l'exercice `t2pron` du module interactif. Les deux lignes avec « en » "
             "sont celles à reprendre : c'est le seul point neuf de la séance.")

    d.regle("Demander quelque chose au comptoir",
            "Donnez-moi un carnet, s'il vous plaît.",
            precision="Le verbe d'abord, puis « moi » avec un trait d'union. Sans "
                      "« s'il vous plaît » à la fin, la phrase devient un ordre. "
                      "Avec lui, c'est la façon normale de demander, et personne "
                      "ne la trouve brusque.",
            notes="Diapo à photographier. Faire répéter avec et sans « s'il vous plaît » : "
                  "la différence de ton est immédiate, même pour une oreille débutante.")

    d.cartes("D'autres verbes du comptoir", "Le verbe, puis -moi", [
        ("Donnez-moi…",
         "Un carnet de timbres, trois enveloppes, le reçu. C'est le verbe le plus "
         "employé au comptoir, et il ne choque personne."),
        ("Montrez-moi…",
         "Les enveloppes, les boîtes, les formats. Quand on veut voir avant de "
         "choisir, ce qui est presque toujours une bonne idée."),
        ("Expliquez-moi…",
         "La différence entre deux services, ce qui est écrit sur un papier. "
         "Demander une explication est parfaitement normal."),
        ("Répétez…",
         "Sans « moi » : on dit « Répétez le prix, s'il vous plaît ». C'est la "
         "seule des quatre qui se passe du petit mot."),
    ], notes="Faire remarquer la dernière carte : le trait d'union et le « moi » ne "
             "vont pas avec tous les verbes. Ne pas en faire une règle, seulement un "
             "constat sur ces quatre-là.")

    d.pratique('Écriture', "Écrivez la demande",
               "Commencez par le verbe, et n'oubliez pas le trait d'union.", [
        ("Demander un carnet de timbres.", "Donnez-moi un carnet de timbres, s'il vous plaît."),
        ("Demander trois enveloppes.", "Donnez-moi trois enveloppes, s'il vous plaît."),
        ("Demander qu'on vous montre les boîtes.", "Montrez-moi les boîtes, s'il vous plaît."),
        ("Demander qu'on répète le prix.", "Répétez le prix, s'il vous plaît."),
        ("Demander qu'on vous explique la différence.", "Expliquez-moi la différence, s'il vous plaît."),
        ("Demander un reçu.", "Donnez-moi le reçu, s'il vous plaît."),
    ], corrige=True,
       notes="C'est l'exercice `t2donnez` du module. Le trait d'union se perd chez la "
             "moitié du groupe : le corriger systématiquement, il compte à l'écrit.")

    d.piege(
        "Le trait d'union",
        "Donnez moi un carnet.",
        "Donnez-moi un carnet.",
        "Le trait d'union n'est pas une décoration : il relie le verbe et le « moi » "
        "en un seul bloc, et c'est ainsi que le mot se prononce. À l'oral, personne "
        "n'entend la différence ; à l'écrit, elle se voit tout de suite.",
        notes="Faire écrire les six demandes de l'exercice au tableau par six élèves "
              "différents : les traits d'union manquants sautent aux yeux du groupe.")

    d.billet(
        "Écrivez deux demandes que vous ferez au comptoir, avec « donnez-moi ».",
        exemples=[
            "Une avec un nombre : combien en voulez-vous ?",
            "N'oubliez pas « s'il vous plaît » à la fin.",
        ],
        notes="Deux minutes. Vérifier le trait d'union et la présence de la formule de "
              "politesse : ce sont les deux seules choses à corriger ce soir.")

    return d.save(dossier)
