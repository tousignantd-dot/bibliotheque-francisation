# -*- coding: utf-8 -*-
"""D1 · Trois choses avant midi.
Bloc D « Défi 3 · Trois choses avant midi » · couleur acier · 75 min.
Source : dialogue `t3`, exercices `t3vf` et `t3note`.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n3-horaire/images/')


def build(dossier):
    d = Deck(
        code='D1', section='acier',
        titre="Trois choses avant midi",
        chapeau="Une consigne de travail arrive vite et ne se répète pas "
                "toujours. Fabiola fait deux choses que personne ne lui a "
                "apprises : elle prend son crayon, et elle redit tout pour "
                "vérifier.",
        duree='75 minutes')

    d.titre(notes="Ouverture du défi 3. C'est le défi le plus transférable du module : "
                  "recevoir une consigne, la noter, la redire, se sert dans tous les "
                  "métiers et dans toutes les salles de cours.")

    d.objectifs([
        "comprendre trois consignes données à la suite ;",
        "reconnaître la forme du verbe qui commande ;",
        "noter une consigne en trois mots ;",
        "redire ce qu'on a compris pour le vérifier.",
    ])

    d.declencheur(
        'Observation', "Qu'est-ce qu'on fait quand on reçoit trois consignes d'un coup ?",
        image=IMG + 'chariot-plateaux.jpg',
        pistes=[
            "Est-ce qu'on retient trois choses de mémoire ?",
            "Est-ce qu'on peut demander de répéter ?",
            "Qu'est-ce qu'on écrit, et où ?",
            "Qu'est-ce qui arrive si on en oublie une ?",
        ],
        notes="Presque tout le monde répond « non » à la première question et « oui » à "
              "la deuxième — puis avoue ne jamais l'avoir fait. C'est là qu'est le "
              "travail.")

    d.dialogue('Dialogue · 1 de 3', "Je prends mon crayon", [
        ("GAÉTAN", "Fabiola, écoutez-moi bien. Trois choses avant midi.", True),
        ("FABIOLA", "Je vous écoute. Je prends mon crayon.", True),
        ("GAÉTAN", "Premièrement, sortez les plateaux du chariot du deuxième étage.", True),
        ("FABIOLA", "Les plateaux du deuxième. Ensuite ?", True),
    ], consigne="Écoutez d'abord, diapo masquée.",
       notes="Deux gestes en deux répliques : Fabiola annonce qu'elle note, puis elle "
             "redit la consigne en trois mots avant de demander la suite. Les faire "
             "relever tous les deux — ce sont les deux compétences du défi.")

    d.dialogue('Dialogue · 2 de 3', "Premièrement, deuxièmement, troisièmement", [
        ("GAÉTAN", "Deuxièmement, rangez les boîtes de la livraison dans la chambre froide.", True),
        ("FABIOLA", "La livraison de ce matin ? D'accord.", True),
        ("GAÉTAN", "Troisièmement, éteignez le four à onze heures. N'oubliez pas.", True),
        ("FABIOLA", "Onze heures pile. Est-ce que je peux répéter, pour vérifier ?", True),
    ], notes="Les trois mots qui organisent la liste — premièrement, deuxièmement, "
             "troisièmement — sont un cadeau pour celui qui écoute : ils disent d'avance "
             "combien il y en a. Faire remarquer aussi la demande de Fabiola : elle "
             "demande la permission de répéter.")

    d.dialogue('Dialogue · 3 de 3', "C'est fait, monsieur Roy", [
        ("FABIOLA", "Les plateaux, les boîtes dans la chambre froide, le four à onze heures.", True),
        ("GAÉTAN", "Parfait. Vous notez mieux que bien du monde ici.", False),
        ("FABIOLA", "Monsieur Roy ? Les plateaux, c'est fait. Je viens de finir.", True),
        ("FABIOLA", "Je suis en train de les ranger. Il reste trois boîtes.", True),
    ], notes="La reformulation de Fabiola est plus courte que la consigne du chef : elle "
             "garde l'essentiel et laisse tomber le reste. C'est exactement l'exercice de "
             "la fin de séance.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après le dialogue.", [
        ("Monsieur Roy donne trois consignes à faire avant midi.", "vrai"),
        ("La première consigne est de ranger les boîtes.", "faux — sortir les plateaux"),
        ("Les boîtes de la livraison vont dans la chambre froide.", "vrai"),
        ("Le four doit être éteint à onze heures.", "vrai"),
        ("Fabiola répète les trois consignes pour vérifier.", "vrai"),
        ("Quand le chef revient, les trois tâches sont terminées.", "faux — il reste trois boîtes"),
    ], corrige=True,
       notes="C'est l'exercice `t3vf` du module interactif, mot pour mot. La dernière "
             "ligne prépare la séance suivante : dire où on en est vaut mieux que "
             "prétendre avoir fini.")

    d.pratique('Écriture', "Noter une consigne en trois mots",
               "Qu'est-ce que vous écrivez dans votre carnet ?", [
        ("« Sortez les plateaux du chariot du deuxième étage. »", "plateaux — chariot 2e étage"),
        ("« Rangez les boîtes de la livraison dans la chambre froide. »", "boîtes livraison, chambre froide"),
        ("« Éteignez le four à onze heures. »", "four : 11 h"),
        ("« Miguel entre à six heures jeudi, à votre place. »", "jeudi : Miguel, 6 h"),
        ("« La pause est de onze heures et demie à midi. »", "pause 11 h 30 - 12 h"),
        ("« Avisez-moi trois jours avant. »", "aviser 3 jours d'avance"),
    ], corrige=True, cols=1,
       notes="C'est l'exercice `t3note` du module interactif. La règle est simple : on "
             "garde le nom de la chose, le lieu ou l'heure, et rien d'autre. Les verbes "
             "et les articles se perdent sans dommage.")

    d.billet(
        "Notez trois consignes que vous recevez souvent.",
        exemples=[
            "En trois mots chacune, comme dans un carnet.",
            "Au travail, à l'école, ou à la maison.",
        ],
        notes="Devoir court. Prévoir de vrais carnets ou des cartons de format poche : "
              "plusieurs élèves n'ont jamais eu l'idée d'en avoir un sur eux, et c'est "
              "l'objet qui change le plus de choses dans une première année d'emploi.")

    return d.save(dossier)
