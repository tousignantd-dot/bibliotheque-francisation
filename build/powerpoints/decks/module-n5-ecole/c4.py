# -*- coding: utf-8 -*-
"""C4 · À quoi renvoie « celui-ci » ?
Bloc C « Défi 2 · Lire l'avis du centre » · couleur ambre · 75 min.
Source du module : exercices `t2rep` et `t2note`, mini-leçon `t2rep`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C4', section='ambre',
        titre="À quoi renvoie « celui-ci » ?",
        chapeau="Un avis parle d'un formulaire, d'une demande, d'un avis et "
                "d'un local en quatre paragraphes. S'il répétait chaque fois "
                "le mot, il ferait trois pages. Il reprend donc — et lire un "
                "document officiel, c'est en bonne partie savoir à quoi "
                "chaque reprise renvoie.",
        duree='75 minutes')

    d.titre(notes="Dernière séance du défi 2. Elle est double : on apprend à lire les "
                  "reprises, puis à transformer l'avis en trois lignes de notes. La "
                  "deuxième moitié est celle qui reste, l'an prochain, quand la "
                  "grammaire sera oubliée.")

    d.objectifs([
        "reconnaître les reprises d'un texte officiel et retrouver leur renvoi ;",
        "employer « ce » suivi d'un nom plus général quand on écrit ;",
        "accorder « celui-ci » et « celle-ci » avec le nom qu'ils reprennent ;",
        "transformer un avis en trois lignes de notes utilisables.",
    ], notes="Le programme du niveau 5 consacre six points de savoir à la reprise de "
             "l'information. C'est l'un des rares endroits où lire et écrire demandent "
             "exactement la même compétence, dans les deux sens.")

    d.regle("Du précis vers le général, jamais l'inverse",
            "Le formulaire devient « ce document ». La demande devient "
            "« cette demande » ou « ce dossier ».",
            precision="En remontant vers le précis, vous ajoutez une information "
                      "que le lecteur n'a pas — et il croit qu'il s'agit d'un "
                      "autre papier.",
            notes="Diapositive à photographier. C'est la règle à employer quand on "
                  "écrit : elle ne peut pas être mal lue, contrairement à « celui-ci ».")

    d.cartes("Quatre reprises", "Ce qu'elles remplacent", [
        ("ce document · cette demande",
         "La plus sûre. On reprend le mot par un mot qui le contient."),
        ("celui-ci · celle-ci",
         "Le dernier nom du bon genre, en remontant d'un mot à la fois."),
        ("le · la · les",
         "Un nom déjà déterminé. « Signez l'avis et rapportez-le. »"),
        ("y",
         "Un lieu, ou un nom introduit par « à ». « J'y serai avant midi. »"),
    ], notes="Faire relire l'avis de C2 et surligner toutes les reprises. Il y en a plus "
             "que le groupe ne croit, et les repérer sur un vrai texte vaut mieux que "
             "n'importe quel exercice.")

    d.pratique('Emploi', "La bonne reprise",
               "Complétez à l'oral, puis à l'écrit.", [
        ("Remplissez le formulaire. ___ doit nous parvenir avant le 6 mars.",
         "Ce document"),
        ("J'ai envoyé ma demande de transfert. ___ a été reçue le 4 avril.",
         "Celle-ci"),
        ("Le retour est prévu le 30 mars. ___ n'est pas une échéance.", "Celui-ci"),
        ("J'ai bien reçu votre avis et je vous ___ rapporte signé demain.", "le"),
        ("Je passerai au secrétariat : j'___ serai avant midi.", "y"),
        ("Vous trouverez mon courriel du 3 mars. ___ portait sur mon horaire.",
         "Cette demande"),
    ], corrige=True,
       notes="Faire dire la phrase entière. La deuxième et la troisième s'opposent par "
             "le genre : demande est féminin, retour est masculin. C'est l'accord qui "
             "révèle le renvoi, pas l'inverse.")

    d.piege("Employer « celui-ci » trois phrases plus bas",
            "... Celui-ci doit être signé. (mais quatre noms ont passé depuis)",
            "... Ce document doit être signé.",
            "« Celui-ci » désigne le nom masculin singulier le plus proche. Au-delà "
            "d'une phrase, le lecteur remonte et se trompe. « Ce document » redonne "
            "la certitude en deux mots.",
            notes="Faire chercher dans l'avis de C2 un « celui-ci » éloigné : il n'y en a "
                  "pas. Un avis bien écrit ne les emploie qu'à courte portée, et c'est "
                  "un bon modèle.")

    d.regle("Un avis se lit une fois, une note se relit dix fois",
            "Ce qui reste utile tient en trois lignes : ce que je dois faire, "
            "pour quand, et ce qui arrive si je ne le fais pas.",
            precision="Écrivez-les à la main, sur l'avis lui-même, et datez-les.",
            notes="Diapositive à photographier. C'est la partie de la séance qui survit "
                  "au module. Faire écrire les trois lignes tout de suite, avis en main.")

    d.pratique('Prise de notes', "L'avis en trois lignes",
               "À partir de l'avis de la séance C2.", [
        ("Ligne 1 : l'échéance, en premier.", "6 mars : remettre le formulaire signé"),
        ("Ligne 2 : la conséquence.", "sinon : absence inscrite comme non motivée"),
        ("Ligne 3 : ce qui suit, avec les numéros exacts.",
         "retour 30 mars, local 214 ; rattrapage mardi et jeudi midi, local 118"),
        ("Et la date du jour où vous écrivez la note.",
         "trois avis dans une session, sans dates, on ne sait plus lequel est le dernier"),
    ], corrige=True,
       notes="Exiger les numéros de local exacts. C'est là que la moitié du groupe "
             "recopie approximativement, et un numéro faux est pire qu'un numéro absent.")

    d.pratique('Écriture', "Écrivez ce que l'avis vous demande",
               "Une phrase complète pour chaque consigne.", [
        ("Ce qu'Amelia doit faire et pour quand.", "une phrase, une date"),
        ("Ce qui arrivera si le formulaire n'est pas remis à temps.",
         "commencez par « Si »"),
        ("La période exacte de son absence.",
         "avec « à partir du » et « jusqu'au... inclusivement »"),
        ("Ce qu'elle devra faire si elle doit rester plus longtemps.",
         "commencez par « En cas de »"),
    ], corrige=False,
       notes="Ces quatre phrases reprennent tout le bloc C. Passer dans les rangées : "
             "l'erreur la plus fréquente est d'écrire la période à la place de "
             "l'échéance dans la première.")

    d.billet(
        "Recopiez les trois lignes de notes que vous avez écrites, sans regarder l'avis.",
        exemples=[
            "L'échéance en premier.",
            "Avec les numéros de local exacts.",
        ],
        notes="Ramasser les billets. Comparer avec l'avis : ce qui manque de mémoire est "
              "exactement ce qui doit être écrit sur la feuille, et c'est la meilleure "
              "démonstration possible de l'utilité d'une note.")

    return d.save(dossier)
