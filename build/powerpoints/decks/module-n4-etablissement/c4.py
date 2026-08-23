# -*- coding: utf-8 -*-
"""C4 · Une situation, une phrase
Bloc C « Défi 2 · Les messages qu'on me laisse » · couleur ambre · 75 min.
Source du module : exercice `t2motifs`, et reprise de `t2a`.
"""
import os
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n4-etablissement/images/')


def img(nom):
    chemin = IMG + nom
    return chemin if os.path.exists(chemin) else None


def build(dossier):
    d = Deck(
        code='C4', section='ambre',
        titre="Une situation, une phrase",
        chapeau="Six situations qui arrivent vraiment, et six phrases toutes "
                "faites pour les dire. Ce sont les phrases que vous "
                "emporterez : elles servent au centre, au travail, chez le "
                "médecin et à la garderie.",
        duree='75 minutes')

    d.titre(notes="Dernière séance du bloc C. Elle assemble tout ce qui précède : le "
                  "mot du motif de A4, la cause de C2, le pronom de C3. Séance de "
                  "production orale guidée, à faire debout autant que possible.")

    d.objectifs([
        "associer une situation réelle à la phrase qui la dit ;",
        "produire cette phrase sans hésiter et sans la lire ;",
        "répondre à un message plutôt que de rappeler pour rien ;",
        "reformuler ce qu'on a compris avant de raccrocher.",
    ], notes="Le deuxième objectif est le vrai travail de la séance. Une phrase lue "
             "n'est pas une phrase acquise : viser la production sans support à la fin "
             "des soixante-quinze minutes.")

    d.tableau('Six situations, six phrases', "À dire sans réfléchir",
              ['La situation', 'La phrase'],
              [["Enfant malade", "Je serai absente aujourd'hui parce que mon fils est malade."],
               ["Autobus manqué", "J'aurai une heure de retard à cause de l'autobus."],
               ["Cours du soir arrêté", "Je vous écris pour abandonner le cours du soir."],
               ["Raison privée", "J'ai un empêchement familial ce matin."],
               ["Départ avant la fin", "Je devrai quitter à onze heures pour un rendez-vous."],
               ["Papier rapporté", "Je vous remets le papier qui justifie mon absence."]],
              cle=1,
              notes="Masquer la colonne de droite. Faire produire chaque phrase par un "
                    "élève différent, debout, avant de révéler. Puis comparer : ce que "
                    "le groupe produit est souvent très proche.")

    d.declencheur(
        'Observation', "Un enfant couché, un thermomètre à côté. "
                       "Vous appelez, et vous dites quoi ?",
        image=img('enfant-malade-lit.jpg'),
        pistes=[
            "Quelle est la première phrase, après « bonjour » ?",
            "Combien de phrases pour le motif : une, deux, trois ?",
            "Dites-vous le nom de la maladie ? Pourquoi ?",
            "Qu'est-ce que vous promettez avant de raccrocher ?",
        ],
        notes="La troisième piste ouvre une petite discussion utile : personne au "
              "secrétariat n'a le droit de demander un détail médical, et personne ne "
              "le demande. Le dire clairement rassure.")

    d.regle("Une phrase pour le motif, jamais deux",
            "Personne ne vérifie, personne ne juge. Un motif court est un "
            "motif de personne qui sait comment ça marche.",
            precision="Le détail médical, familial ou financier ne regarde "
                      "pas un dossier scolaire.",
            notes="Diapositive à photographier. Elle règle la question de la longueur "
                  "une fois pour toutes, et elle revient en E1 comme critère de la "
                  "production orale.")

    d.pratique('Production', "Dites la phrase, debout",
               "Une situation vous est donnée, vous dites la phrase.", [
        ("Votre enfant a de la fièvre et vous allez à la clinique.",
         "Je serai absente aujourd'hui, jeudi le 17, parce que mon fils est malade."),
        ("Il y a une panne de métro et vous arriverez vers dix heures.",
         "J'aurai deux heures de retard à cause d'une panne de métro."),
        ("Vous avez un rendez-vous à l'immigration à onze heures.",
         "Je devrai quitter le cours à dix heures et demie pour un rendez-vous."),
        ("Vous arrêtez le cours du soir à partir du 1er octobre.",
         "Je vous écris pour abandonner le cours du soir à partir du 1er octobre."),
        ("Votre voiture ne démarre pas et vous ne viendrez pas.",
         "Je serai absent aujourd'hui à cause d'un problème de voiture."),
        ("Vous rapportez le papier de la clinique.",
         "Je vous remets le papier qui justifie mon absence de lundi."),
    ], corrige=True,
       notes="Passer dans les rangées. Corriger deux choses seulement : la date, qui "
             "manque souvent, et la longueur du motif. Le reste, laisser passer.")

    d.cartes("Répondre à un message", "Rappeler, ou ne pas rappeler", [
        ("On vous demande de rappeler",
         "Vous rappelez, en donnant votre nom et votre groupe d'abord."),
        ("Il manque un des trois renseignements",
         "Vous rappelez, et vous demandez précisément ce qui manque."),
        ("Le message est complet",
         "Vous ne rappelez pas : vous faites ce qu'on vous demande."),
        ("Vous voulez confirmer que vous avez écouté",
         "Ce n'est pas nécessaire. Le secrétariat en reçoit quarante par jour."),
    ], notes="La quatrième carte surprend et soulage. Beaucoup d'élèves rappellent par "
             "politesse et occupent une ligne pour rien. Dire que faire ce qu'on "
             "demande est la meilleure des réponses.")

    d.regle("Redites ce que vous avez compris",
            "Donc je remets la note avant vendredi, avec le papier de la "
            "clinique. C'est bien ça ?",
            precision="Deux secondes, et vous savez tous les deux que vous "
                      "avez compris la même chose.",
            notes="C'est la phrase de sortie du module, et la plus rentable de toutes. "
                  "La faire dire par chacun, à voix haute, avec sa propre situation.")

    d.piege("Rappeler pour dire qu'on a bien reçu le message",
            "Bonjour, c'est juste pour vous dire que j'ai eu votre message.",
            "Bonjour. Nourhane Ouazzani, groupe 6. Je vous apporte ma note.",
            "Le secrétariat reçoit quarante appels par jour. Un appel qui "
            "n'apporte rien occupe une ligne. Faites ce qu'on vous demande : "
            "c'est la meilleure des confirmations.",
            notes="Nuancer une fois : si le message était difficile à comprendre, "
                  "rappeler pour vérifier est parfaitement légitime. Ce qui ne sert à "
                  "rien, c'est la confirmation pure.")

    d.billet(
        "Choisissez une des six situations et écrivez la phrase complète, "
        "avec la date.",
        exemples=[
            "Une seule phrase, avec la date exacte et le motif.",
            "Relisez-la à voix haute avant de la remettre.",
        ],
        notes="Ramasser : ces billets servent de brouillon en D1, où la même phrase "
              "devient la quatrième ligne d'une note écrite. Rien ne se perd d'un bloc "
              "à l'autre.")

    return d.save(dossier)
