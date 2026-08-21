# -*- coding: utf-8 -*-
"""C2 · L'avis, le retard, l'absence.
Bloc C « Défi 2 · Permission, retard, absence » · couleur ambre · 75 min.
Source : exercices `t2avis`, `t2permis` et `t2mot`, dialogue `t2b`.

La séance de compréhension écrite du module — la deuxième intention du
programme, « comprendre une directive » à l'écrit. Le support est celui que
tout élève a réellement sous les yeux : la feuille affichée près de la porte
de sa classe.

On y lit une heure, un jour de congé, un numéro de téléphone et deux règles.
C'est exactement le lexique du programme : pause, congé, calendrier,
permission, absence, retard.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n2-classe/images/')


def build(dossier):
    d = Deck(
        code='C2', section='ambre',
        titre="L'avis, le retard, l'absence",
        chapeau="Lire la feuille affichée près de la porte, et prévenir quand "
                "on ne sera pas là.",
        duree='75 minutes')

    d.titre(notes="Séance de lecture et d'écriture. Apporter le vrai avis affiché dans "
                  "le corridor du centre : la séance vaut trois fois plus avec le "
                  "document réel du groupe.")

    d.objectifs([
        "lire un avis affiché et y trouver une heure ;",
        "distinguer ce qui est permis de ce qui est interdit ;",
        "dire qu'on est en retard ou absent ;",
        "écrire un mot de trois lignes à son enseignante.",
    ])

    d.declencheur(
        'Observation', "Qu'est-ce qui est écrit sur cette porte ?",
        image=IMG + 'avis-porte.jpg',
        pistes=[
            "Où est cette feuille ?",
            "Qu'est-ce qu'on y cherche, en général ?",
            "Est-ce qu'il y a un avis sur notre porte ?",
            "Qu'est-ce qui est écrit dessus ?",
        ],
        notes="Sortir dans le corridor pendant l'observation, si c'est possible : cinq "
              "minutes debout devant le vrai avis valent la demi-heure qui suit.")

    d.tableau('Lecture', "AVIS AUX ÉLÈVES — local 114",
              ["Ce qui est écrit", "Ce que ça veut dire"],
              [["Cours : du lundi au vendredi, 8 h 30 à 12 h 30",
                "quatre heures, tous les matins"],
               ["Pause : de 10 h à 10 h 15",
                "quinze minutes, dans le corridor ou dehors"],
               ["Congé : lundi 5 octobre",
                "pas de cours ce jour-là, pour tout le groupe"],
               ["Absence : téléphonez au 514 555-0142 avant 8 h 30",
                "un appel de trente secondes suffit"]],
              cle=2,
              note="Un avis se lit en cherchant un chiffre : une heure, un jour, un "
                   "numéro.",
              notes="Diapositive à photographier. Poser les questions dans le désordre : "
                    "« à quelle heure la pause ? », « quel jour le congé ? ». On "
                    "cherche, on ne lit pas tout.")

    d.regle("Permis, interdit",
            "Deux mots qui règlent toutes les règles d'un centre.",
            precision="<b>Permis</b> : on a le droit. <b>Autorisé</b> et <b>possible</b> "
                      "veulent dire la même chose. <b>Interdit</b> : on n'a pas le "
                      "droit. Et avec <b>devoir</b>, ce n'est plus un choix : « vous "
                      "devez téléphoner avant 8 h 30 ».",
            notes="Diapositive à photographier. Ces quatre mots sont affichés partout "
                  "dans un établissement : les faire chercher dans le corridor comme "
                  "devoir facultatif.")

    d.regle("En retard, ou absent ?",
            "On vient plus tard, ou on ne vient pas du tout.",
            precision="« Je suis <b>en retard</b> » : j'arrive, mais après l'heure. "
                      "« Je suis <b>absent</b> » : je ne viens pas. Une femme écrit "
                      "« <b>absente</b> », avec un e — et le t s'entend. Un "
                      "<b>congé</b>, lui, est pour tout le groupe : on ne téléphone pas "
                      "pour un congé.",
            notes="Diapositive à photographier. Le lien avec B2 est direct : absent / "
                  "absente s'accorde comme vert / verte. Le dire.")

    d.dialogue('Dialogue', "Demain, je suis absent", [
        ("TARIQ", "Madame, demain, je suis absent.", True),
        ("MADAME LEDUC", "Ah oui ? Pourquoi, Tariq ?", True),
        ("TARIQ", "J'ai un rendez-vous à la clinique.", True),
        ("MADAME LEDUC", "D'accord. Téléphone au centre avant huit heures et demie.", True),
        ("TARIQ", "Est-ce que je fais un travail à la maison ?", True),
        ("MADAME LEDUC", "Oui. Les pages quinze et seize.", True),
    ], consigne="Écoutez, puis retenez les quatre choses que Tariq a dites.",
       notes="Quatre choses : le jour, l'annonce, la raison, la question sur le travail. "
             "Faire compter par le groupe — c'est le plan du mot écrit de E1.")

    d.pratique('Lecture', "Vrai ou faux, d'après l'avis",
               "Relisez l'avis, puis répondez.", [
        ("Le cours finit à midi et demi.", "vrai"),
        ("La pause dure quinze minutes.", "vrai"),
        ("Le lundi 5 octobre, il y a un cours.", "faux — c'est un congé"),
        ("Quand on est en retard, il faut frapper à la porte.", "faux — on entre en silence"),
        ("Pour une absence, on téléphone avant 8 h 30.", "vrai"),
        ("On peut apporter une bouteille d'eau en classe.", "vrai"),
    ], corrige=True, cols=1,
       notes="Ce sont les six énoncés de l'exercice 3 du module en ligne. Les faire en "
             "cherchant dans l'avis affiché, pas de mémoire.")

    d.pratique('Écriture', "Le mot à l'enseignante",
               "Quatre lignes, pas plus. Écrivez-les dans cet ordre.", [
        ("Ligne 1", "Bonjour madame Leduc,"),
        ("Ligne 2", "Demain, je suis absent. (ou : je suis en retard)"),
        ("Ligne 3", "J'ai un rendez-vous. (la raison, en trois mots)"),
        ("Ligne 4", "Merci. Votre prénom."),
    ], cols=1,
       notes="Vingt minutes. C'est exactement le cadre de la production écrite de E1 : "
             "les élèves qui l'écrivent ici arrivent prêts à la dernière séance.")

    d.billet(
        "Écrivez un mot à votre enseignante pour une absence de la semaine prochaine.",
        exemples=[
            "Bonjour madame,",
            "Jeudi, je suis absente. J'ai un rendez-vous.",
            "Merci. Myriam",
        ],
        notes="Devoir court. Vérifier l'accord de « absent / absente » : c'est le même "
              "que celui des couleurs, vu en B2.")

    return d.save(dossier)
