# -*- coding: utf-8 -*-
"""B5 · Raconter une nouvelle à voix haute.
Bloc B · couleur teal (écoute et réponds) · 60 min.
Source : production orale du défi 1, appuyée sur A4, B1 et B3.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B5', section='teal',
        titre='Raconter une nouvelle',
        chapeau="Trente secondes pour raconter ce qu'on a entendu, à quelqu'un qui ne "
                "l'a pas entendu. C'est ce qu'on fait tous les jours, dans toutes les "
                "langues — et c'est un exercice complet.",
        duree='60 minutes')

    d.titre(notes="Séance de production orale. Rendre les billets de A4 et B1 : ils "
                  "contiennent déjà les résumés. Disposer la classe en dyades.")

    d.objectifs([
        "raconter une nouvelle en cinq phrases, dans l'ordre chronologique ;",
        "commencer par l'essentiel, puis donner les détails ;",
        "employer un marqueur de temps à chaque étape ;",
        "répondre aux questions de celui qui écoute.",
    ])

    d.regle('La règle des trente secondes',
            "Une phrase pour l'essentiel, puis quatre phrases dans l'ordre du temps.",
            precision="« Une fillette de Gatineau a retrouvé son chat. Il s'était sauvé "
                      "il y a trois jours. Sa classe a fabriqué des affiches. Elle les a "
                      "distribuées dans le quartier. Une voisine l'a reconnu hier "
                      "matin. »",
            notes="Chronométrer ce modèle devant le groupe : environ vingt secondes. "
                  "C'est plus court qu'ils ne le croient.")

    d.cartes('Le modèle', "Comment on raconte, en quatre gestes", [
        ("La phrase d'ouverture",
         "Elle résume tout : qui, quoi, où. « Une fillette de Gatineau a retrouvé son "
         "chat disparu. » Celui qui écoute sait déjà de quoi il s'agit."),
        ("Le retour en arrière",
         "« Il s'était sauvé il y a trois jours. » On remonte au début, avec un "
         "marqueur de temps."),
        ("Les étapes, dans l'ordre",
         "« Sa classe a fabriqué des affiches, elle les a distribuées… » Un verbe par "
         "étape, dans l'ordre du temps."),
        ("La fin, avec le moment",
         "« Une voisine l'a reconnu hier matin. » On boucle en revenant au présent."),
    ], notes="Faire dire le modèle complet par un élève, puis analyser avec le groupe "
             "quel geste correspond à quelle phrase.")

    d.pratique('Pratique · 1 de 4', "La phrase d'ouverture",
               "Une seule phrase : qui, quoi, où.", [
        ("Le chat retrouvé", "Une fillette de Gatineau a retrouvé son chat disparu."),
        ("La collecte de mitaines",
         "Des élèves de Longueuil ont amassé deux cents paires de mitaines."),
        ("Le cycliste secouru",
         "À Trois-Pistoles, un cycliste a été secouru par deux passants."),
        ("Le documentaire de classe",
         "Des élèves de Victoriaville ont tourné un documentaire sur le recyclage."),
    ], corrige=True,
       notes="Faire dire les quatre à voix haute. Une phrase d'ouverture doit tenir en "
             "une respiration : c'est le critère.")

    d.pratique('Pratique · 2 de 4', "Ajoutez les quatre étapes",
               "Un marqueur de temps au début de chaque phrase.", [
        ("Étape 1", "Il y a trois jours, le chat s'est sauvé par une fenêtre."),
        ("Étape 2", "Ensuite, sa classe a fabriqué des affiches."),
        ("Étape 3", "Puis la fillette les a distribuées dans le quartier."),
        ("Étape 4", "Hier matin, une voisine l'a reconnu dans sa cour."),
    ], corrige=True,
       notes="Faire enchaîner l'ouverture et les quatre étapes d'un seul trait. C'est le "
             "récit complet, et il tient en trente secondes.")

    d.piege("Le piège du récit sans ouverture",
            "« Il y a trois jours, un chat s'est sauvé par une fenêtre… »",
            "« Une fillette a retrouvé son chat. Il s'était sauvé il y a trois jours… »",
            "Commencer par le début oblige l'auditeur à attendre pour savoir de quoi on "
            "parle. Commencer par le résultat lui donne un cadre : tout ce qui suit "
            "trouve sa place. C'est ce que font les journalistes.",
            notes="Faire l'expérience : raconter les deux versions au groupe et demander "
                  "laquelle était plus facile à suivre.")

    d.piege("Le piège du détail au mauvais moment",
            "« Une fillette — elle a six ans, elle habite à Gatineau, dans un quartier près de la rivière — a retrouvé son chat. »",
            "« Une fillette de Gatineau a retrouvé son chat. Elle a six ans. »",
            "Les détails insérés au milieu de la phrase d'ouverture la cassent. "
            "Donnez-la entière, puis ajoutez les détails dans les phrases suivantes.",
            notes="Erreur très fréquente à l'oral. La corriger en demandant simplement : "
                  "« redis-moi ta première phrase, sans rien ajouter ».")

    d.pratique('Pratique · 3 de 4', "Jeu de rôle · raconter et questionner",
               "À deux. L'un raconte, l'autre pose trois questions. Puis on échange.", [
        ("Celui qui raconte", "cinq phrases, trente secondes, sans notes"),
        ("Première question", "Quand est-ce que c'est arrivé ?"),
        ("Deuxième question", "Qui a fait ça, exactement ?"),
        ("Troisième question", "Est-ce qu'on sait pourquoi ?"),
    ], corrige=False,
       notes="Vingt minutes. Circuler et vérifier une seule chose : est-ce que la "
             "première phrase contient qui, quoi et où ? C'est le critère de la séance.")

    d.pratique('Pratique · 4 de 4', "Racontez votre propre nouvelle",
               "Celle de votre billet de la séance A4.", [
        ("La phrase d'ouverture", "qui, quoi, où — en une phrase"),
        ("Les étapes", "dans l'ordre du temps, avec un marqueur chacune"),
        ("La fin", "où en est la situation aujourd'hui"),
        ("Les questions", "votre partenaire en pose trois"),
    ], corrige=False,
       notes="Quinze minutes. Les nouvelles apportées par les élèves sont plus "
             "motivantes que celles du module : leur laisser la place.")

    d.billet(
        "Après le jeu de rôle : quelle question de votre partenaire vous a le plus surpris ?",
        exemples=[
            "Une seule question, celle à laquelle vous n'aviez pas pensé.",
            "Écrivez la réponse que vous auriez dû donner dans votre récit.",
        ],
        notes="Les questions manquées disent exactement ce qui manquait dans le récit. "
              "C'est le meilleur bilan de la séance.")

    return d.save(dossier)
