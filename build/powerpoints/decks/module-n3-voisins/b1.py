# -*- coding: utf-8 -*-
"""B1 · Mon vélo gêne dans le corridor.
Bloc B « Défi 1 · Est-ce que je peux ? » · couleur acier · 75 min.
Source : dialogue `t1`, exercice `t1vf`.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n3-voisins/images/')


def build(dossier):
    d = Deck(
        code='B1', section='acier',
        titre="Mon vélo gêne dans le corridor",
        chapeau="La cour, la remise, le corridor et la corde à linge "
                "appartiennent à tout le monde en même temps. Une phrase "
                "demandée avant vaut mieux qu'une chicane après.",
        duree='75 minutes')

    d.titre(notes="Ouverture du défi 1. Commencer par la question de A3 restée sans "
                  "réponse : à qui appartient la cour ? Le dialogue y répond en pratique "
                  "plutôt qu'en droit.")

    d.objectifs([
        "comprendre une demande de permission et sa réponse ;",
        "reconnaître un « oui », un « oui, mais » et un « non » poli ;",
        "relever la condition posée avec la permission ;",
        "savoir à qui s'adresser quand ce n'est pas à son voisin.",
    ])

    d.declencheur(
        'Observation', "Où est-ce qu'on range un vélo, l'hiver ?",
        image=IMG + 'ruelle-arriere.jpg',
        pistes=[
            "Où mettez-vous ce qui ne rentre pas chez vous ?",
            "Est-ce qu'on peut laisser une chose dans le corridor ?",
            "Qu'est-ce qui arrive si personne ne demande rien ?",
            "À qui demanderiez-vous, dans votre immeuble ?",
        ],
        notes="La quatrième question est la vraie question de la séance. Beaucoup "
              "répondront « à personne » : c'est exactement ce que le défi vient "
              "corriger.")

    d.dialogue('Dialogue · 1 de 3', "Excusez-moi de vous déranger", [
        ("RACHID", "Madame Lachapelle ? Excusez-moi de vous déranger.", True),
        ("MANON", "Pas du tout. Entrez une minute, il fait froid dans l'escalier.", True),
        ("RACHID", "Merci. Mon vélo dort dans le corridor et il gêne tout le monde.", True),
        ("MANON", "Ah, je l'ai vu. Il prend pas mal de place devant la porte.", True),
    ], consigne="Écoutez d'abord, diapo masquée.",
       notes="Rachid dit pourquoi il vient AVANT de demander quoi que ce soit. C'est "
             "l'ordre à retenir : la raison, puis la demande. Une demande sans raison "
             "inquiète.")

    d.dialogue('Dialogue · 2 de 3', "Bien sûr, allez-y", [
        ("RACHID", "Est-ce que je peux le mettre dans la remise, en arrière ?", True),
        ("MANON", "Bien sûr, allez-y. Il y a de la place au fond.", True),
        ("RACHID", "Est-ce qu'il faut demander à quelqu'un d'autre ?", True),
        ("MANON", "Le concierge a la clé. Monsieur Nadeau, au rez-de-chaussée.", True),
    ], notes="La permission arrive tout de suite, mais elle n'est pas complète : il "
             "manque la clé. Faire remarquer que Rachid pose la question — Manon ne l'a "
             "pas offerte. Rien ne se donne avant qu'on le demande.")

    d.dialogue('Dialogue · 3 de 3', "Je préfère que non", [
        ("RACHID", "Est-ce que je pourrais l'accrocher au mur ?", True),
        ("MANON", "Oui, accrochez-le au mur du fond. La tondeuse doit passer.", True),
        ("RACHID", "Une dernière chose : la rampe de l'escalier, en bas ?", True),
        ("MANON", "Je préfère que non. C'est la sortie de secours, il faut la garder libre.", True),
    ], notes="Les deux réponses les plus utiles du module sont ici : « oui, mais » avec "
             "sa condition, et « je préfère que non » avec sa raison. Les faire répéter "
             "toutes les deux à voix haute.")

    d.tableau('Analyse', "Trois réponses, trois façons d'écouter",
              ["Ce qu'on entend", "Ce que ça veut dire"],
              [["Bien sûr, allez-y.", "oui, sans condition"],
               ["Oui, mais accrochez-le au mur.", "oui, avec une condition à respecter"],
               ["Il faudrait demander au concierge.", "je ne peux pas décider seule"],
               ["Je préfère que non.", "non — poliment, mais non"]],
              cle=1,
              note="Un refus poli s'accompagne presque toujours de sa raison. "
                   "Sans raison, il sonne sec.",
              notes="Diapo à photographier. C'est le tableau que les élèves relisent "
                    "avant le jeu de rôle. Faire chercher un exemple pour chaque ligne.")

    d.regle("Une demande commence par sa raison",
            "« Mon vélo gêne dans le corridor. Est-ce que je peux… ? »",
            precision="Deux phrases, dans cet ordre. La raison d'abord — elle "
                      "rassure —, la demande ensuite. Et devant, une phrase de "
                      "politesse : « Excusez-moi de vous déranger. »",
            notes="Diapo à photographier. Faire construire trois demandes complètes au "
                  "tableau, avec des situations données par le groupe.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après le dialogue.", [
        ("Le vélo de Rachid gêne le passage dans le corridor.", "vrai"),
        ("Manon refuse que Rachid utilise la remise.", "faux — elle accepte tout de suite"),
        ("C'est le concierge qui a la clé de la remise.", "vrai — monsieur Nadeau"),
        ("Il faut accrocher le vélo au mur du fond.", "vrai — pour laisser passer la tondeuse"),
        ("Rachid doit sortir son vélo de la remise pendant l'hiver.", "faux — il peut le laisser toute l'année"),
        ("Manon accepte qu'on attache un vélo à la rampe de l'escalier.", "faux — c'est la sortie de secours"),
    ], corrige=True,
       notes="Faire justifier chaque « faux » par la réplique exacte. C'est l'exercice "
             "`t1vf` du module interactif, mot pour mot.")

    d.billet(
        "Écrivez une permission que vous auriez à demander chez vous.",
        exemples=[
            "La raison d'abord, la demande ensuite.",
            "« Ma poussette bloque l'entrée. Est-ce que je peux… ? »",
        ],
        notes="Devoir court. Les situations réelles ramassées ici serviront d'exemples "
              "à B2 : chacun travaillera sa propre demande plutôt que celle du manuel.")

    return d.save(dossier)
