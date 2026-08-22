# -*- coding: utf-8 -*-
"""C4 · Le jour où, et ce qui était déjà fait
Bloc C « Défi 2 · Ce que disent les documents » · couleur teal · 75 min.
Source : exercices `t2ou` et `t2pqp`, leurs mini-leçons. Savoirs du programme :
la subordonnée relative avec « où », complément de lieu ou de temps ; le
plus-que-parfait qui désigne une action précédant une autre action passée.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C4', section='teal',
        titre="Le jour où, et ce qui était déjà fait",
        chapeau="Deux outils pour dire long sans faire deux phrases, et pour "
                "placer une action avant une autre à l'intérieur du passé. "
                "Les documents s'en servent sans arrêt.",
        duree='75 minutes')

    d.titre(notes="Dernière séance du bloc C. Elle ferme le Défi 2 par les deux "
                  "tournures qui font les phrases longues d'un document — la relative "
                  "et le plus-que-parfait.")

    d.objectifs([
        "réunir deux phrases avec « qui », « que » ou « où » ;",
        "employer « où » pour un moment, pas seulement pour un lieu ;",
        "former le plus-que-parfait avec l'auxiliaire à l'imparfait ;",
        "reconnaître, entre deux passés, celui qui vient d'abord.",
    ], notes="Le deuxième objectif corrige la faute la plus répandue du niveau : « le "
             "jour que » au lieu de « le jour où ».")

    d.declencheur(
        'Observation', "« C'est la cafétéria. La rencontre s'y tiendra. » Comment dire les deux en une phrase ?",
        pistes=[
            "Quel petit mot peut réunir les deux ?",
            "Est-ce qu'on garde « dans » quelque part ?",
            "Et si c'était un moment au lieu d'un lieu ?",
        ],
        notes="Laisser produire : plusieurs proposeront « dans laquelle », qui est "
              "correct. Accueillir, puis montrer que « où » fait la même chose en un "
              "mot — et qu'il sert aussi pour le temps.")

    d.tableau('Analyse', "qui, que, où : le test qui tranche",
              ['Ce qui manque', 'Le mot'],
              [["le sujet du verbe", "qui — le technicien qui est venu"],
               ["le complément direct", "que — le formulaire qu'elle a rempli"],
               ["un endroit", "où — le bureau où on dépose les demandes"],
               ["un moment", "où — le jour où l'affichage est descendu"]],
              cle=0,
              note="Enlève le mot, remets la phrase droite, et regarde ce qui manque.",
              notes="Diapositive à photographier. Le quatrième cas est celui qu'on "
                    "n'attend pas : « le jour où », « l'année où », « la semaine où ». "
                    "Jamais « le jour que », même si on l'entend.")

    d.pratique('Pratique', "Réunis les deux phrases",
               "Employez qui, que ou où.", [
        ("C'est la cafétéria. La rencontre s'y tiendra.", "la cafétéria où se tiendra la rencontre"),
        ("Je me souviens du jour. L'affichage est descendu ce jour-là.", "le jour où l'affichage est descendu"),
        ("C'est un formulaire. Il tient sur une page.", "un formulaire qui tient sur une page"),
        ("Voici la note. Marie-Soleil a écrit cette note.", "la note que Marie-Soleil a écrite"),
        ("C'est le bureau. On y dépose les demandes.", "le bureau où on dépose les demandes"),
        ("1988 est l'année. L'usine a déménagé cette année-là.", "l'année où l'usine a déménagé"),
    ], corrige=True,
       notes="Faire appliquer le test à voix haute avant d'écrire : « il manque quoi "
             "ici ? ». La méthode compte plus que la bonne réponse.")

    d.piege('Piège', "le jour que l'affichage est descendu",
            "le jour où l'affichage est descendu",
            "Pour un moment, c'est « où », exactement comme pour un lieu. On entend "
            "parfois « le jour que » à l'oral, mais ce n'est pas la forme écrite, et "
            "c'est la faute la plus fréquente du niveau. Une seule lettre à changer, "
            "et elle se corrige d'un coup.",
            notes="Le montrer aussi à l'envers : « la cafétéria où dans laquelle » est "
                  "faux — « où » contient déjà « dans ». Un seul mot suffit.")

    d.regle("Le plus-que-parfait recule d'un cran",
            "Auxiliaire à l'imparfait + participe passé : l'action se place avant une autre action passée.",
            precision="« Elle a obtenu le poste parce qu'elle avait suivi la formation » "
                      "— la formation d'abord, l'obtention ensuite, et les deux sont "
                      "au passé. Ses compagnons : déjà, la veille, auparavant, parce "
                      "que. Dans un document, il sert presque toujours à justifier une "
                      "décision par ce qui existait avant.",
            notes="Diapositive à photographier. Rappeler l'article 4.5 : « l'employé "
                  "qui avait déjà occupé le poste ». C'est de là que la question est "
                  "partie, dans le dialogue du Défi 2.")

    d.pratique('Pratique', "Mets au plus-que-parfait",
               "Le verbe est entre parenthèses.", [
        ("Yaneth a déposé sa demande vendredi. Elle ___ (lire) la note la veille.", "avait lu"),
        ("Le comité l'a rencontrée le 30. Elle ___ (préparer) trois exemples.", "avait préparé"),
        ("Quand la rencontre a commencé, vingt-deux personnes ___ (arriver) déjà.", "étaient déjà arrivées"),
        ("Ghislain n'a pas été surpris : il ___ (voir) l'affichage dès le premier jour.", "avait vu"),
        ("Elle a obtenu le poste parce qu'elle ___ (suivre) la formation en mars.", "avait suivi"),
    ], corrige=True,
       notes="Le troisième item porte l'accord avec « être » : « arrivées ». Le "
             "signaler sans en faire une leçon — c'est la même règle qu'au passé "
             "composé, déjà connue.")

    d.pratique('Bilan du bloc', "Qu'est-ce qui vient en premier ?",
               "Deux passés dans la même phrase : lequel est le plus ancien ?", [
        ("Elle a obtenu le poste parce qu'elle avait suivi la formation.", "la formation"),
        ("Josée est revenue à l'expédition ; elle avait travaillé deux ans à la qualité.", "les deux ans à la qualité"),
        ("Le candidat a été refusé : il n'avait pas remis son formulaire à temps.", "le formulaire non remis"),
        ("L'usine a changé de nom en 1988 ; elle avait déménagé la même année.", "le déménagement"),
    ], corrige=True,
       notes="Exercice de lecture, pas de production. C'est la compétence visée par le "
             "programme : comprendre l'antériorité, pas la produire à volonté.")

    d.billet(
        "Écris une phrase avec « le jour où » sur ta propre vie.",
        exemples=[
            "Une seule phrase.",
            "Ajoute, si tu peux, ce que tu avais déjà fait avant ce jour-là.",
        ],
        notes="Cinq minutes. La seconde consigne fait produire un plus-que-parfait "
              "sans le nommer. Ramasser : c'est la mesure du bloc C.")

    return d.save(dossier)
