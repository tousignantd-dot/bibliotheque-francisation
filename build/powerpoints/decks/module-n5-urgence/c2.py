# -*- coding: utf-8 -*-
"""C2 · Le décor et l'évènement.
Bloc C « Défi 2 » · couleur ambre · 75 min. Écriture.
Source : exercice `t2recit` et sa mini-leçon.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n5-urgence/images/')


def build(dossier):
    d = Deck(
        code='C2', section='ambre',
        titre="Le décor et l'évènement",
        chapeau="Deux temps, deux rôles. L'imparfait pour ce qui durait "
                "autour, le passé composé pour ce qui est arrivé. Ce n'est "
                "pas de la grammaire savante : c'est ce qui permet à "
                "l'infirmière de comprendre.",
        duree='75 minutes')

    d.titre(notes="Séance de grammaire, la plus importante du module. Commencer par "
                  "relire deux billets de C1 et souligner au tableau les verbes : les "
                  "élèves verront d'eux-mêmes le mélange.")

    d.objectifs([
        "employer l'imparfait pour le décor et le passé composé pour les faits ;",
        "former l'imparfait à partir du radical de « nous » ;",
        "accorder le participe passé avec l'auxiliaire être ;",
        "raconter une nuit en cinq phrases organisées.",
    ])

    d.declencheur(
        'Comparaison', "« Elle dormait quand je suis rentrée. » Qu'est-ce qui a "
                       "commencé en premier ?",
        image=IMG + 'chambre.jpg',
        pistes=[
            "Lequel des deux faits dure ?",
            "Lequel arrive à un moment précis ?",
            "Que devient la phrase si on met les deux au passé composé ?",
            "Peut-on dire « elle a dormi quand je suis rentrée » ?",
        ],
        notes="Dessiner une ligne au tableau : un trait long pour l'imparfait, une croix "
              "pour le passé composé. Le schéma vaut mieux qu'une définition.")

    d.regle("L'imparfait plante le décor, le passé composé raconte",
            "Elle avait de la fièvre. Elle est tombée.",
            precision="L'imparfait dit ce qui durait, se répétait ou était vrai autour. "
                      "Le passé composé dit ce qui est arrivé une fois, à un moment qu'on "
                      "peut nommer.",
            notes="Diapositive à photographier. Ajouter le test : si l'on peut ajouter "
                  "« ce jour-là, à telle heure », c'est le passé composé.")

    d.tableau('Les signaux', "Les mots qui appellent un temps",
              ['Ils appellent l\'imparfait', 'Ils appellent le passé composé'],
              [["depuis, ça faisait… que", "hier, cette nuit, ce matin-là"],
               ["tous les jours, souvent, toujours", "à deux heures, vers minuit"],
               ["pendant que, quand (le décor)", "tout d'un coup, soudain"],
               ["avant, dans ce temps-là", "trois fois, une fois"],
               ["c'était, il faisait, elle avait", "elle est tombée, j'ai appelé"]],
              cle=0,
              notes="Ces signaux sont des indices, pas des règles. Le dire : c'est le sens "
                    "qui décide, et le même verbe peut aller aux deux temps.")

    d.cartes("Former les deux temps", "Deux mécaniques, peu d'exceptions", [
        ("Imparfait",
         "Le radical de « nous » au présent + -ais, -ais, -ait, -ions, -iez, -aient. "
         "Nous fais-ons donne je faisais."),
        ("Une seule exception",
         "être donne j'étais, tu étais, il était."),
        ("Passé composé avec avoir",
         "j'ai appelé, elle a dormi, nous avons attendu."),
        ("Passé composé avec être",
         "les verbes de mouvement et tous les pronominaux : elle est tombée, elle "
         "s'est levée."),
    ], notes="La quatrième carte porte l'erreur la plus fréquente du module : « elle s'a "
             "levée ». Tous les pronominaux prennent être, sans exception.")

    d.pratique('Formation', "Imparfait ou passé composé ?",
               "Mettez le verbe au temps qui convient.", [
        ("Elle ___ (avoir) de la fièvre depuis mercredi.", "avait"),
        ("Elle ___ (manger) très peu depuis deux jours.", "mangeait"),
        ("Cette nuit, elle ___ (se lever) pour aller à la toilette.", "s'est levée"),
        ("Elle ___ (tomber) dans l'escalier vers deux heures.", "est tombée"),
        ("Il ___ (faire) noir et l'escalier ___ (être) étroit.", "faisait · était"),
        ("J'___ (appeler) le 9-1-1 tout de suite après.", "ai appelé"),
        ("Quand je suis arrivée en bas, elle me ___ (parler) déjà.", "parlait"),
        ("Les ambulanciers ___ (arriver) sept minutes plus tard.", "sont arrivés"),
        ("Avant sa chute, elle ___ (marcher) sans marchette.", "marchait"),
        ("Elle ___ (ne pas perdre) connaissance.", "n'a pas perdu"),
    ], corrige=True,
       notes="La septième est la plus formatrice : un fait ponctuel dans un décor qui "
             "dure, dans la même phrase. La faire relire deux fois.")

    d.piege("Employer avoir avec un verbe pronominal",
            "Elle s'a levée à deux heures.",
            "Elle s'est levée à deux heures.",
            "Tous les verbes pronominaux prennent être : elle s'est levée, je me suis "
            "blessé, ils se sont assis.",
            notes="Erreur systématique chez beaucoup d'élèves. La corriger par la "
                  "répétition orale plutôt que par la règle.")

    d.piege("Oublier l'accord avec être",
            "Elle est tombé.",
            "Elle est tombée.",
            "Avec l'auxiliaire être, le participe s'accorde avec le sujet : elle est "
            "tombée, ils sont arrivés, nous sommes restées.",
            notes="Ne s'entend pas à l'oral, mais compte à l'écrit — et le message à la "
                  "famille de la séance E2 est un écrit.")

    d.billet(
        "Racontez en cinq phrases une nuit où quelqu'un n'allait pas bien.",
        exemples=[
            "Deux phrases à l'imparfait pour le décor, trois au passé composé.",
            "Une nuit inventée fait le même travail qu'une nuit vécue.",
        ],
        notes="Préciser que personne n'est obligé de raconter quelque chose de personnel. "
              "Ramasser : ces récits serviront de base à la production orale de E1.")

    return d.save(dossier)
