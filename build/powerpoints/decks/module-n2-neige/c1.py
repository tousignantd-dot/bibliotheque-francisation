# -*- coding: utf-8 -*-
"""C1 · Qu'est-ce que je mets ?
Bloc C « Défi 2 · Je m'habille pour dehors » · couleur acier · 75 min.
Source : dialogue `t2`, exercices `t2vf`, `t2vet` et `t2faut`, mini-leçon
« Il faut, je mets, mets ».

Le bulletin est compris ; reste à en tirer une décision. C'est le passage du
module de la compréhension à l'action : moins huit et du vent, donc manteau
d'hiver, tuque et mitaines.

La grammaire de la séance tient en trois formes, et le niveau 2 n'en demande
pas davantage : « il faut » suivi du verbe entier, « je mets » pour soi,
« mets » à quelqu'un. Le piège est connu et se paie tous les jours dans les
classes : « il faut je mets ».
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n2-neige/vocab/')


def build(dossier):
    d = Deck(
        code='C1', section='acier',
        titre="Qu'est-ce que je mets ?",
        chapeau="Choisir ses vêtements selon la température, et le dire de "
                "trois façons.",
        duree='75 minutes')

    d.titre(notes="Ouverture du Défi 2. Commencer par les trois températures notées en "
                  "devoir : « Mardi, moins deux. Qu'est-ce que vous avez mis ? » La "
                  "séance part de là.")

    d.objectifs([
        "nommer les vêtements de l'hiver québécois ;",
        "dire où se met chaque vêtement ;",
        "employer « il faut » + le verbe entier ;",
        "distinguer « je mets », « mets » et « mettez ».",
    ])

    d.declencheur(
        'Observation', "Il fait moins huit et il vente. Qu'est-ce qu'on met ?",
        image=IMG + 'manteau.jpg',
        pistes=[
            "Qu'est-ce qu'il y a sur la photo ?",
            "Est-ce que ce manteau suffit à moins huit ?",
            "Qu'est-ce qui manque ?",
            "Quel vêtement d'hiver vous a manqué votre premier hiver ?",
        ],
        notes="La quatrième piste est la vraie. Presque tout le monde a passé un "
              "premier hiver sans tuque ou sans bottes ; c'est la matière de la "
              "séance et elle vient du groupe.")

    d.dialogue('Dialogue', "Devant la porte, sept heures et quart", [
        ("YOUSSEF", "Maman, je mets mon manteau d'automne ?", True),
        ("ZINA", "Non. Il fait moins huit. Il faut le manteau d'hiver.", True),
        ("YOUSSEF", "D'accord. Et mes espadrilles ?", True),
        ("ZINA", "Non, tes bottes. Il y a de la neige.", True),
        ("YOUSSEF", "Et mes mains ? J'ai froid aux mains.", True),
        ("ZINA", "Mets tes mitaines. Elles sont dans le sac.", True),
    ], consigne="Écoutez deux fois. Notez les trois vêtements.",
       notes="Faire écouter diapositive masquée. Trois vêtements à attraper : "
             "manteau, bottes, mitaines. Puis dévoiler et faire lire à deux voix.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après le dialogue.", [
        ("Youssef veut mettre son manteau d'automne.", "vrai"),
        ("Sa mère dit oui.", "faux - elle dit non"),
        ("Youssef met ses bottes.", "vrai"),
        ("Les mitaines sont dans le sac.", "vrai"),
        ("Zina part sans rien sur la tête.", "faux - elle prend une tuque"),
    ], corrige=True, cols=1,
       notes="Le dernier demande d'écouter la fin du dialogue, où Zina change d'avis. "
             "Le refaire écouter plutôt que de donner la réponse.")

    d.vocabulaire('Vocabulaire', "Ce qu'on met, et où", [
        ("une tuque", "Sur la tête et les oreilles. Le mot est québécois."),
        ("des mitaines", "Sur les mains. Les doigts sont ensemble, sauf le pouce."),
        ("des bottes", "Sur les pieds, par-dessus des bas de laine."),
        ("un foulard", "Autour du cou, contre le vent."),
    ], notes="Diapositive à photographier. « Tuque » n'existe qu'ici : le dire. Les "
             "élèves l'entendront dès leur première sortie.")

    d.tableau('Analyse', "Le vêtement et sa place",
              ["Vêtement", "Où on le met"],
              [["une tuque", "sur la tête et les oreilles"],
               ["des mitaines", "sur les mains"],
               ["des bottes", "sur les pieds"],
               ["un foulard", "autour du cou"],
               ["un manteau", "par-dessus tous les autres vêtements"],
               ["des bas de laine", "dans les bottes, sur les pieds"]],
              cle=1,
              notes="Diapositive à photographier. Faire montrer l'endroit sur soi en "
                    "disant le mot : le geste fixe le vocabulaire mieux que la liste.")

    d.regle("Après « il faut », le verbe reste entier",
            "Il faut mettre une tuque.",
            precision="« Il faut » ne change jamais, et le verbe qui suit non plus : "
                      "mettre, sortir, rester. C'est une règle pour tout le monde. "
                      "Pour dire ce que je fais, moi : « Je mets ma tuque. »",
            notes="Diapositive à photographier. Faire construire trois phrases avec "
                  "« il faut » sur le thème de l'hiver, au tableau.")

    d.piege(
        'Piège', "Il faut je mets une tuque.", "Il faut mettre une tuque.",
        "L'erreur est logique : l'élève sait conjuguer et il conjugue. Mais après "
        "« il faut », le verbe ne se conjugue pas — il garde sa forme de "
        "dictionnaire. Une seule fois par phrase : ou bien « il faut mettre », ou "
        "bien « je mets ».",
        notes="Presque tout le groupe fait cette erreur. La dédramatiser tout de "
              "suite, puis la faire corriger à l'oral trois fois de suite.")

    d.pratique('Pratique', "Il faut, je mets, mets",
               "Complétez avec « il faut », « je mets » ou « mets ».", [
        ("Il fait moins vingt. ___ mettre un manteau d'hiver.", "Il faut"),
        ("Moi, ___ mes bottes tous les matins.", "je mets"),
        ("Youssef, ___ ta tuque !", "mets"),
        ("Il y a de la glace. ___ marcher lentement.", "Il faut"),
        ("J'ai froid aux mains. ___ mes mitaines.", "Je mets"),
    ], corrige=True, cols=1,
       notes="Faire lire la phrase complète à voix haute après chaque réponse. "
             "L'oreille corrige ce que la règle n'a pas encore fixé.")

    d.pratique('Pratique · deux par deux', "Habillez votre voisin",
               "Quinze minutes, debout. A donne la température, B dit quoi mettre.", [
        ("Étape 1", "A dit : « Il fait moins vingt et il vente. »"),
        ("Étape 2", "B répond : « Il faut mettre une tuque et des mitaines. »"),
        ("Étape 3", "A ajoute une chose oubliée : « Et les pieds ? »"),
        ("Étape 4", "On échange les rôles avec une autre température."),
    ], cols=1,
       notes="Donner cinq températures au tableau, de moins trente à plus vingt. "
             "L'étape 3 est celle qui fait parler : personne ne pense aux pieds.")

    d.billet(
        "Demain matin, écrivez ce que vous mettez pour sortir, et pourquoi.",
        exemples=[
            "Il fait moins 10.",
            "Je mets mon manteau d'hiver et ma tuque.",
            "Il vente, alors je mets mon foulard.",
        ],
        notes="Trois phrases. Elles serviront telles quelles dans la production "
              "écrite de E1 : le dire au groupe, ça change l'effort qu'on y met.")

    return d.save(dossier)
