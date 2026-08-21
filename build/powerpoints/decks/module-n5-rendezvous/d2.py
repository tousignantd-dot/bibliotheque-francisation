# -*- coding: utf-8 -*-
"""D2 · « Il faut que… » et les petits mots qui évitent de tout répéter.
Bloc D « Défi 3 » · couleur ambre · 75 min. Écriture.
Source : exercices `t3faut` et `t3pron`, et leurs mini-leçons.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n5-rendezvous/images/')


def build(dossier):
    d = Deck(
        code='D2', section='ambre',
        titre="« Il faut que… » et les petits mots",
        chapeau="Deux points de langue pour un seul appel : dire une "
                "obligation qui vise quelqu'un de précis, et reprendre ce "
                "qui vient d'être dit sans le répéter en entier.",
        duree='75 minutes')

    d.titre(notes="Rendre les billets de D1 corrigés. Lire deux messages d'annulation à "
                  "voix haute : le groupe compte les six éléments sur ses doigts.")

    d.objectifs([
        "former le subjonctif présent des verbes usuels ;",
        "employer « il faut que » quand l'obligation vise quelqu'un de précis ;",
        "reconnaître « faut que » à l'oral du Québec ;",
        "reprendre un mot déjà dit par le, la, les, y ou en.",
    ])

    d.declencheur(
        'Observation', "« Je veux déplacer mon rendez-vous. Mon rendez-vous est le "
                       "mardi. Je ne peux pas venir à mon rendez-vous. »",
        image=IMG + 'calendrier-rendezvous.jpg',
        pistes=[
            "Est-ce que ces trois phrases sont fausses ?",
            "Est-ce que quelqu'un parle comme ça ?",
            "Qu'est-ce qui manque ?",
            "Comment dirait-on la deuxième et la troisième ?",
        ],
        notes="Aucune des trois phrases n'est fautive : c'est l'ensemble qui ne ressemble "
              "à aucune conversation réelle. C'est exactement ce que le niveau 5 demande "
              "de dépasser.")

    d.regle("Après « il faut que », le subjonctif",
            "« Il faut que vous soyez à jeun » — jamais « vous êtes ».",
            precision="On le forme sur le « ils » du présent : ils prenn-ent donne que je "
                      "prenne. Sept verbes suffisent pour tout ce qui se dit en clinique : "
                      "que je sois, que j'aie, que j'aille, que je fasse, que je puisse, "
                      "que je vienne, que je sache.",
            notes="Diapositive à photographier. Rassurer : le programme n'en demande pas "
                  "plus au niveau 5, et sept formes s'apprennent en une soirée.")

    d.cartes("Quatre façons de dire l'obligation", "Toutes justes", [
        ("il faut + infinitif",
         "La règle, pour tout le monde. « Il faut arriver quinze minutes avant. »"),
        ("il faut que + subjonctif",
         "Quelqu'un de précis. « Il faut que vous soyez à jeun. »"),
        ("il faudrait que",
         "Plus doux, encore négociable. « Il faudrait que je vienne plus tôt. »"),
        ("je dois + infinitif",
         "Même sens, sans subjonctif. Le raccourci quand la forme ne vient pas."),
    ], notes="Dire clairement que la quatrième est acceptable : un élève bloqué en pleine "
             "phrase vaut mieux qu'un élève qui se tait.")

    d.piege("Écrire « faut que » sans le « il »",
            "« Faut que je déplace mon rendez-vous. » dans un courriel.",
            "« Il faut que je déplace mon rendez-vous. »",
            "À l'oral du Québec, le « il » tombe presque toujours, et c'est parfaitement "
            "normal — il faut le reconnaître à l'écoute. À l'écrit, en revanche, on le "
            "remet.",
            notes="Le dire sans jugement : ce n'est pas du relâchement, c'est la langue "
                  "parlée d'ici. Les élèves l'entendent tous les jours et croient mal "
                  "comprendre.")

    d.cartes("Cinq petits mots de reprise", "Ce que chacun remplace", [
        ("le, la, les",
         "Une chose déjà nommée, sans préposition. « J'annule le rendez-vous » donne « je l'annule »."),
        ("y",
         "Un lieu, ou « à + quelque chose ». « Je vais à la clinique » donne « j'y vais »."),
        ("en",
         "« De + quelque chose », et les quantités. « J'ai trois questions » donne « j'en ai trois »."),
        ("Où les mettre",
         "Devant le verbe, et devant l'auxiliaire au passé : je l'ai noté, j'y suis allé."),
    ], notes="« y » ne remplace jamais une personne : « je pense à ma fille » donne « je pense "
             "à elle ». Le dire, c'est l'erreur suivante.")

    d.pratique('Écriture', "Mettez au subjonctif présent",
               "Le verbe est entre parenthèses.", [
        ("Il faut que vous ___ (être) à jeun douze heures avant.", "soyez"),
        ("Il faut que je ___ (être) au travail à sept heures.", "sois"),
        ("Il faudrait que nous ___ (prendre) un rendez-vous de suivi.", "prenions"),
        ("Il faut que vous ___ (avoir) votre carte avec vous.", "ayez"),
        ("Il faut que j'___ (aller) chercher mon fils.", "aille"),
        ("Il faudrait que la clinique ___ (pouvoir) me rappeler.", "puisse"),
        ("Il faut que vous ___ (venir) quinze minutes plus tôt.", "veniez"),
        ("Il faut qu'elle ___ (faire) l'ordonnance avant votre départ.", "fasse"),
    ], corrige=True, cols=2,
       notes="« Prenions » est le seul qui prend le radical de l'imparfait. Le faire "
             "remarquer avant la correction.")

    d.pratique('Écriture', "Remplacez par le, la, les, y ou en",
               "Le mot à remplacer est entre guillemets.", [
        ("Je veux déplacer « mon rendez-vous ».", "je veux le déplacer"),
        ("Je vais « à la clinique » jeudi.", "j'y vais jeudi"),
        ("J'ai parlé « de mes étourdissements ».", "j'en ai parlé"),
        ("J'ai apporté « mes médicaments ».", "je les ai apportés"),
        ("Je pense « à mon rendez-vous » tous les jours.", "j'y pense"),
        ("J'ai « deux questions » à vous poser.", "j'en ai deux"),
    ], corrige=True, cols=2,
       notes="Faire remarquer la place du pronom au passé composé : « je les ai apportés », "
             "et non « j'ai les apportés ».")

    d.billet(
        "Réécrivez votre message de D1 en employant au moins un pronom de reprise.",
        exemples=[
            "« Mon rendez-vous du jeudi ? Je voudrais le déplacer. »",
            "Et une obligation : « Il faut que je… »",
        ],
        notes="Deux exigences précises, faciles à vérifier d'un coup d'œil en ramassant. "
              "Le message final servira en E1.")

    return d.save(dossier)
