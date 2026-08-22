# -*- coding: utf-8 -*-
"""A2 · Les lettres qui ne disent pas ce qu'elles montrent
Bloc A « Je découvre » · couleur indigo · 75 min. Graphie-phonie.
Source : exercice `prGraphie` et sa mini-leçon.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A2', section='indigo',
        titre="Les lettres qui ne disent pas ce qu'elles montrent",
        chapeau="Vous entendez « é-co-gra-fie » dans un corridor. Vous "
                "l'écrivez comme vous l'avez entendu et vous ne le trouvez "
                "nulle part. Trois cas seulement, et les mots de la santé "
                "en sont pleins.",
        duree='75 minutes')

    d.titre(notes="Séance de prononciation. Courte en contenu et longue en "
                  "répétition : prévoir au moins vingt minutes de répétition à voix "
                  "haute, en groupe puis individuellement.")

    d.objectifs([
        "reconnaître les lettres ch qui se disent comme un k ;",
        "reconnaître la lettre x qui se dit comme un s ;",
        "reconnaître les lettres sh et sch qui se disent comme un ch ;",
        "retrouver un mot écrit quand on ne l'a qu'entendu.",
    ], notes="Le quatrième objectif est celui qui sert dans la vraie vie : il "
             "débloque un adulte devant un mot médical entendu une seule fois.")

    d.declencheur(
        'Observation', "Un mot entendu à l'hôpital et jamais retrouvé écrit",
        pistes=[
            "Ça vous est-il déjà arrivé de chercher un mot sans le trouver ?",
            "Y a-t-il des lettres muettes dans votre première langue ?",
            "Comment faites-vous, en général, quand un mot vous échappe ?",
        ],
        notes="Laisser trois minutes. Presque tout le monde a une histoire de mot "
              "introuvable. Ne pas donner la solution tout de suite : elle vaut "
              "davantage après l'aveu collectif.")

    d.tableau('Analyse', "Cas 1 · les lettres ch qui se disent comme un k",
              ['On écrit', 'On dit'],
              [["une échographie", "é-co-gra-fie"],
               ["chronique", "cro-nique"],
               ["un psychiatre", "psi-kiatre"],
               ["le cholestérol", "co-les-té-rol"],
               ["la technique", "tec-nique"],
               ["un écho", "é-co"]],
              cle=0,
              notes="Faire répéter chaque mot deux fois. Insister ensuite sur "
                    "l'exception qui rassure : « chercher », « chaque », « chambre » "
                    "gardent le son normal. Le k est l'exception, jamais la règle.")

    d.tableau('Analyse', "Cas 2 · la lettre x qui se dit comme un s",
              ['On écrit', 'On dit'],
              [["six", "sisse, tout seul"],
               ["six semaines", "si semaines"],
               ["six ans", "siz ans"],
               ["dix heures", "diz heures"],
               ["soixante-dix", "soi-sante-dis"]],
              cle=0,
              note="Le mot ne change pas : c'est sa fin qui bouge selon ce qui suit.",
              notes="Faire l'exercice avec un délai réel : « dans six semaines », "
                    "« dans dix jours », « à six heures ». C'est exactement ce qu'une "
                    "secrétaire leur dira au téléphone.")

    d.tableau('Analyse', "Cas 3 · les lettres sh et sch qui se disent comme un ch",
              ['On écrit', 'On dit'],
              [["un schéma", "ché-ma"],
               ["un shampoing", "cham-poin"],
               ["un short", "chort"]],
              cle=0,
              note="Trois mots venus d'ailleurs, et rien dans leur écriture ne prévient.",
              notes="Retenir surtout « un schéma » : un feuillet d'hôpital en contient "
                    "presque toujours un, et c'est le dessin qui explique un parcours "
                    "en un coup d'œil.")

    d.piege('Prononciation',
            "donner à tous les ch le souffle de chat",
            "essayer d'abord le k dans un mot de médecine",
            "Dire « te-chnique » ou « psy-chiatre » avec le souffle de « chat » "
            "rend le mot méconnaissable, et l'interlocuteur ne devinera pas. "
            "La liste des mots savants se compte sur les doigts : une carte "
            "suffit à l'apprendre une fois pour toutes.",
            notes="Faire relire les six mots du cas 1 à voix haute, lentement, en "
                  "exagérant le k. L'exagération se corrige d'elle-même en deux jours ; "
                  "l'hésitation, non.")

    d.cartes('Méthode', "Un mot entendu, comment le retrouver écrit", [
        ("J'entends un k", "J'essaie ch avant de conclure : écho, chronique, psychiatre."),
        ("J'entends un s", "J'essaie x quand c'est un nombre : six, dix, soixante."),
        ("J'entends un ch", "J'essaie sh et sch : schéma, shampoing, short."),
        ("Je ne trouve toujours pas", "Je demande à quelqu'un de l'écrire. Personne ne s'en offusque."),
    ], notes="La quatrième carte est la plus importante. Faire dire la phrase à voix "
             "haute par tout le groupe : « Pouvez-vous me l'écrire, s'il vous plaît ? »")

    d.pratique('Écoute', "Quelle famille de lettres ?",
               "Écoutez le mot, puis dites : comme k, comme s, ou comme ch.", [
        ("une échographie", "comme k"),
        ("un psychiatre", "comme k"),
        ("le cholestérol", "comme k"),
        ("six", "comme s"),
        ("soixante-dix", "comme s"),
        ("un schéma", "comme ch"),
        ("un short", "comme ch"),
    ], corrige=True,
       notes="Lire les mots soi-même plutôt que d'utiliser l'audio du module : le "
             "groupe doit entendre une voix vivante avant l'écran. L'audio servira "
             "pour la reprise individuelle.")

    d.billet(
        "Écrivez un mot que vous avez entendu à l'hôpital sans savoir l'écrire.",
        exemples=[
            "Écrivez-le comme vous l'avez entendu, ce n'est pas grave.",
            "On le cherchera ensemble à la prochaine séance.",
        ],
        notes="Deux minutes. Ramasser les billets et préparer les réponses pour A3 : "
              "ce sont des mots que les élèves porteront longtemps.")

    return d.save(dossier)
