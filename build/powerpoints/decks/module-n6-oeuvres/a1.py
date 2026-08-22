# -*- coding: utf-8 -*-
"""A1 · Un film n'arrive jamais tout seul
Bloc A « Je découvre » · couleur acier · 75 min. Séance d'ouverture.
Source : dialogue `prep`, exercices `prVF` et `prGenres`, quatre premières
cartes de FC_CARDS.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A1', section='acier',
        titre="Un film n'arrive jamais tout seul",
        chapeau="Autour d'un film, il y a toujours trois textes : une "
                "bande-annonce, une biographie, une critique. Ils ne "
                "servent pas au même travail, et aucun ne remplace le film.",
        duree='75 minutes')

    d.titre(notes="Première séance du module. Ouvrir par une question au groupe : "
                  "quel est le dernier film que vous avez vu, et qui vous l'a "
                  "conseillé ? Presque personne ne cite un texte : on cite quelqu'un. "
                  "C'est justement ce que le module vient compléter.")

    d.objectifs([
        "nommer les trois textes qui entourent un film et le générique ;",
        "dire d'avance ce que chacun donne, et ce qu'il ne donne pas ;",
        "distinguer un long métrage d'un court métrage ;",
        "employer les quatre premiers mots du dossier avec leur article.",
    ], notes="Le deuxième objectif est celui du module entier : savoir d'avance ce "
             "qu'on va trouver, c'est déjà la moitié de la compréhension.")

    d.declencheur(
        'Observation', "Comment choisis-tu un film, et qu'est-ce que tu lis avant ?",
        pistes=[
            "La bande-annonce, le résumé, l'avis de quelqu'un ?",
            "As-tu déjà lu une critique de film dans un journal ?",
            "Est-ce que tu regardes le générique jusqu'au bout ?",
            "Qu'est-ce qui t'a le plus surpris dans les films d'ici ?",
        ],
        notes="Question sans mauvaise réponse. Beaucoup d'élèves regardent surtout "
              "des films de leur pays d'origine ou en version doublée. Ne rien "
              "dévaloriser : s'en servir pour comparer les habitudes.")

    d.dialogue('Dialogue · 1 de 3', "Le premier soir au ciné-club", [
        ("BRUNO", "Bonsoir. Vous êtes Thérèse ? Moi, c'est Bruno Salvail, j'anime le ciné-club depuis neuf ans.", True),
        ("THÉRÈSE", "Bonsoir. Oui. Je travaille à la résidence à côté. Je passe devant la salle deux fois par jour depuis cinq ans et je ne suis jamais entrée.", True),
        ("BRUNO", "Ça arrive plus souvent que tu penses. On peut se tutoyer, ici. Le mercredi, on projette un long métrage, et après, on reste une demi-heure à en parler.", True),
        ("THÉRÈSE", "Je vais être honnête : je comprends les films, mais je ne sais jamais quoi dire après.", True),
    ], consigne="Écouter d'abord, diapositive masquée.",
       notes="Le tutoiement est posé dès la troisième réplique, et il tient tout le "
             "module. Le faire remarquer : c'est un choix du lieu, pas une "
             "familiarité.")

    d.dialogue('Dialogue · 2 de 3', "Les trois textes autour d'un film", [
        ("BRUNO", "Il y a une chose qui aide, avant même de parler : un film n'arrive jamais tout seul. Il y a toujours trois textes autour de lui.", True),
        ("THÉRÈSE", "Trois textes ? Je ne vois que le film.", True),
        ("BRUNO", "La bande-annonce, qu'on projette avant : deux minutes, une voix hors champ, et surtout aucune fin. Ensuite la biographie de la réalisatrice, sur la feuille verte.", True),
        ("THÉRÈSE", "Et le troisième ?", True),
    ], notes="Faire compter les trois sur les doigts. Le tableau d'analyse qui suit "
             "reprend exactement cette énumération : la préparer ici.")

    d.dialogue('Dialogue · 3 de 3', "Ce qu'aucun des trois ne donne", [
        ("BRUNO", "La critique. Celle-là paraît après, dans le journal. C'est le seul des trois où quelqu'un dit « moi, je pense que ».", True),
        ("THÉRÈSE", "Alors si je veux savoir ce qui se passe dans le film, je lis laquelle ?", True),
        ("BRUNO", "Aucune, honnêtement. Tu regardes le film. Le déroulement, lui, il n'est nulle part ailleurs.", True),
        ("THÉRÈSE", "Le déroulement, c'est l'ordre des choses qui arrivent ?", True),
    ], notes="La troisième réplique est la phrase du module. La faire répéter par deux "
             "élèves. Annoncer ici la production de E2 : dans quatre semaines, chacun "
             "écrira son résumé au journal.")

    d.tableau('Analyse', "Les trois textes, et ce que chacun donne",
              ['Le texte', 'Ce que tu y trouves'],
              [["La bande-annonce", "trois images fortes et aucune fin, pour donner envie"],
               ["La biographie", "des dates et un parcours, pour situer la personne"],
               ["La critique", "un avis signé, qui juge autant qu'il raconte"],
               ["Le résumé", "l'histoire en deux paragraphes, arrêtée avant la fin"],
               ["Le film", "le déroulement complet, qu'on ne trouve nulle part ailleurs"]],
              cle=0,
              note="Les quatre textes peuvent parler du même film sans jamais dire la même chose.",
              notes="Diapositive à photographier. C'est le tableau de référence du "
                    "module ; il revient en A4 sous forme d'exercice, puis à chaque "
                    "ouverture de défi.")

    d.regle("Savoir d'avance ce qu'on va trouver",
            "Reconnaître le genre d'un texte, c'est déjà avoir compris la moitié du travail.",
            precision="Devant une bande-annonce, tu cherches une envie. Devant une "
                      "biographie, tu cherches un parcours. Devant une critique, tu "
                      "cherches un avis et la raison qui l'appuie. Ce n'est pas la "
                      "même lecture, et ce n'est pas la même attente.",
            notes="Diapositive à photographier. Insister : on ne demande pas de tout "
                  "comprendre, on demande de savoir quoi chercher.")

    d.vocabulaire('Vocabulaire', "Les quatre premiers mots, avec leur article", [
        ("un ciné-club", "Un groupe qui regarde un film ensemble et qui en discute tout de suite après."),
        ("un long métrage", "Un film qui dure plus d'une heure, celui qu'on va voir en salle."),
        ("une bande-annonce", "Le court montage projeté avant le film, qui donne envie sans dire la fin."),
        ("le générique", "La liste des noms qui défile au début ou à la fin, et qui dit qui a fait quoi."),
    ], notes="Faire répéter chaque mot avec son article. « Le générique » prend le "
             "défini : il n'y en a qu'un par film. Le faire remarquer.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après la conversation de Thérèse et de Bruno.", [
        ("Thérèse passe devant la salle depuis cinq ans sans y être entrée.", "vrai"),
        ("Bruno anime le ciné-club depuis neuf ans.", "vrai"),
        ("Au ciné-club, chacun repart tout de suite après le film.", "faux - on reste une demi-heure"),
        ("La bande-annonce est faite pour donner envie, pas pour informer.", "vrai"),
        ("La critique est le seul des trois textes où quelqu'un dit « je ».", "vrai"),
        ("Pour savoir ce qui se passe dans le film, Bruno conseille la critique.", "faux - il conseille de regarder le film"),
    ], corrige=True,
       notes="Faire justifier chaque « faux » par la réplique exacte. Le dernier "
             "surprend : beaucoup d'élèves lisent le résumé pour éviter de regarder.")

    d.billet(
        "Quel texte voudrais-tu apprendre à lire en premier, et pourquoi ?",
        exemples=[
            "Une phrase suffit.",
            "Pense à ce que tu lis déjà, même dans ta langue.",
        ],
        notes="Deux minutes. Les réponses servent en A4 : elles disent quel texte "
              "intimide le plus le groupe, et c'est celui-là qu'il faudra travailler "
              "le plus lentement.")

    return d.save(dossier)
