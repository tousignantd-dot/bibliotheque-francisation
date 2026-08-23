# -*- coding: utf-8 -*-
"""A2 · Ce que la voix ajoute aux mots
Bloc A « Je découvre » · couleur indigo · 75 min.
Source : exercice `prInto` et sa mini-leçon.

Le seul savoir de phonétique du niveau 8 est l'intonation expressive. Il ne se
traite pas comme les autres : il n'y a plus de son à opposer, donc pas de
paires minimales et pas d'alphabet phonétique. Ce sont des **répliques
entières** qu'on écoute, et c'est la mélodie qu'on juge.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A2', section='indigo',
        titre="La même phrase, trois intentions",
        chapeau="Au niveau 8, le programme ne demande plus qu'une chose à la "
                "voix : produire l'intonation expressive. Pas un son de plus "
                "— une mélodie.",
        duree='75 minutes')

    d.titre(notes="Séance de graphie-phonie, mais sans aucun son nouveau. Prévenir le "
                  "groupe dès le début : aujourd'hui, on ne travaille pas la "
                  "prononciation des mots, on travaille ce que la voix ajoute "
                  "par-dessus.")

    d.objectifs([
        "reconnaître à l'oreille la surprise, l'incompréhension et la volonté ;",
        "décrire la mélodie de chacune : monte, freine, descend ;",
        "produire une phrase de volonté sans qu'elle devienne une demande de permission ;",
        "entendre chez l'autre la déception qu'il ne dira pas.",
    ], notes="Le troisième objectif est celui qui sert directement au bloc C : c'est "
             "la voix d'une contestation au téléphone.")

    d.declencheur(
        'Écoute', "Dites « ce n'est pas au dossier » de trois façons différentes",
        pistes=[
            "Une fois comme si vous l'appreniez à l'instant.",
            "Une fois comme si vous n'aviez pas compris.",
            "Une fois comme si vous refusiez de l'accepter.",
            "Les mots changent-ils ? Qu'est-ce qui change, alors ?",
        ],
        notes="Faire faire l'exercice à deux, à voix haute, avant toute explication. "
              "Presque tout le monde y arrive dans sa langue maternelle : le "
              "problème n'est pas l'oreille, c'est l'oser en français.")

    d.regle("Il n'y a plus de son à apprendre, il y a une mélodie",
            "À ce stade, vous prononcez assez bien pour être compris. Ce qui "
            "vous reste à gagner, c'est ce que la voix ajoute par-dessus les "
            "mots — et c'est souvent la seule chose que votre interlocuteur "
            "retiendra.",
            precision="Une intonation plate se lit comme de l'indifférence, alors "
                      "qu'elle n'est le plus souvent que de la prudence. C'est le "
                      "malentendu le plus coûteux de tout le niveau.",
            notes="Diapositive à photographier. Insister : ce n'est pas jouer la "
                  "comédie. Trois phrases sur dix minutes d'appel suffisent.")

    d.cartes('Analyse', "Quatre courbes, quatre repères", [
        ("La surprise",
         "Les premiers mots sont plats, puis les deux ou trois dernières "
         "syllabes montent d'un coup, comme une marche. "
         "« Vous me dites que le drain n'a pas été entretenu ? »"),
        ("L'incompréhension",
         "Rien ne monte : le débit traîne exactement là où vous avez "
         "décroché, avec un blanc juste avant le mot en cause. "
         "« Excusez-moi, le mot exclusion… vous l'employez comment ? »"),
        ("La volonté",
         "La courbe va vers le bas, les syllabes se séparent, et on marque "
         "une pause avant le dernier groupe. C'est la voix d'une décision "
         "déjà prise. « Je veux une réponse écrite, et je l'aurai. »"),
        ("La déception",
         "La quatrième, celle qu'on entend chez l'autre : ça descend dès la "
         "première syllabe et ça ne se relève jamais. "
         "« Ah. Je pensais que la facture était au dossier. »"),
    ], notes="Faire écouter chaque exemple dans le module, puis faire répéter en "
             "exagérant. L'exagération est ce qui fait entrer une mélodie dans "
             "l'oreille ; on la réduira ensuite.")

    d.piege(
        'Intonation',
        "Je veux une réponse écrite ? — la voix monte à la fin",
        "Je veux une réponse écrite. — la voix descend et appuie",
        "Une phrase de volonté dite avec une mélodie montante devient une "
        "demande de permission. C'est exactement l'inverse de ce qu'on "
        "voulait, et c'est la faute la plus fréquente au téléphone : on "
        "n'ose pas conclure, alors on monte, et l'autre entend qu'on "
        "négocie déjà à zéro.",
        notes="Faire dire les deux versions par la même personne, l'une après "
              "l'autre. La différence s'entend immédiatement, et elle ne "
              "s'explique pas mieux qu'elle ne s'entend.")

    d.pratique('Écoute', "Quelle intention la voix porte-t-elle ?",
               "Écoutez chaque réplique. Surprise, incompréhension ou volonté ?", [
        ("Vous me dites que le drain n'a pas été entretenu ?", "surprise"),
        ("Attendez, je ne vous suis plus du tout.", "incompréhension"),
        ("Je veux une réponse écrite, et je l'aurai.", "volonté"),
        ("Comment ça, la facture n'est pas au dossier ?", "surprise"),
        ("Excusez-moi, le mot « exclusion », vous l'employez comment ?", "incompréhension"),
        ("Ce dossier-là, je le fais rouvrir.", "volonté"),
        ("Quatre pages ? On ne m'en avait jamais parlé !", "surprise"),
        ("Je tiens à ce que ce soit écrit dans la lettre.", "volonté"),
    ], corrige=True,
       notes="Passer deux fois chaque extrait. Après la correction, faire répéter les "
             "trois de volonté : ce sont celles du bloc C.")

    # Cinq rangées à libellés longs plus une `note=` dépassaient le garde-fou
    # du gabarit — le même que l'activité 116 a payé trois fois. La colonne de
    # gauche porte donc l'intention en un mot, et la phrase passe à droite :
    # le retournement raccourcit la colonne courte et se lit mieux de loin.
    d.tableau('Analyse', "La même phrase, cinq intentions",
              ['La mélodie', 'Ce qu\'on entend'],
              [["Surprise", "« La facture n'est pas au dossier ? » — elle monte sur « dossier »"],
               ["Constat", "« La facture n'est pas au dossier. » — elle reste plate"],
               ["Incompréhension", "« La facture n'est pas au dossier… » — elle freine, et laisse ouvert"],
               ["Volonté", "« Je veux une réponse écrite. » — elle descend, les mots pèsent"],
               ["Résignation", "« Bon. Je veux une réponse écrite. » — le « bon » tombe avant le reste"]],
              cle=0,
              notes="Diapositive à photographier. Presque les mêmes mots cinq fois : "
                    "ce n'est pas le texte qui change. Faire lire chaque ligne par une "
                    "personne différente, c'est plus efficace que de commenter.")

    d.billet(
        "Enregistrez-vous en disant : « Je veux une réponse écrite, et je l'aurai. »",
        exemples=[
            "Réécoutez-vous. Est-ce que la voix monte ou descend à la fin ?",
            "Recommencez jusqu'à ce qu'elle descende.",
        ],
        notes="Le téléphone de l'élève suffit. Ceux qui n'osent pas s'enregistrer "
              "peuvent le faire à deux, l'autre disant ce qu'il entend.")

    return d.save(dossier)
