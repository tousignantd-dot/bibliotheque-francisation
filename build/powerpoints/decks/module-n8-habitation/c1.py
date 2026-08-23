# -*- coding: utf-8 -*-
"""C1 · Trois points, ce sera court
Bloc C « Défi 2 · L'appel qui conteste » · couleur acier · 75 min.
Source : dialogue `t2`, exercice `t21`.

C'est ici que se joue l'intention même du programme au niveau 8 : « échanger
avec son assureur à l'occasion d'une réclamation par téléphone ». Une seule
intention pour tout le niveau, et elle tient dans cet appel-là.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C1', section='acier',
        titre="L'appel qui conteste",
        chapeau="Vous ne cherchez pas à avoir raison. Vous cherchez à faire "
                "écrire quelque chose à quelqu'un — et cette personne-là ne "
                "décide rien.",
        duree='75 minutes')

    d.titre(notes="Ouverture du bloc C, et cœur du module : c'est la seule intention "
                  "que le programme donne à cette situation au niveau 8. Le dire au "
                  "groupe : ce qu'on fait ce matin est exactement ce que le cours "
                  "demande de savoir faire.")

    d.objectifs([
        "ouvrir un appel avec son nom, son numéro de dossier et une date ;",
        "annoncer le nombre de points, puis s'y tenir ;",
        "appuyer chaque argument sur une pièce qu'on peut envoyer ;",
        "demander trois choses précises et un délai.",
    ], notes="Le deuxième objectif est le plus utile de tout le module, et le moins "
             "évident : annoncer « trois points, ce sera court » oblige les deux "
             "personnes à tenir la conversation.")

    d.declencheur(
        'Discussion', "Comment commencez-vous un appel à une grande entreprise ?",
        pistes=[
            "Que dites-vous dans votre première phrase ?",
            "Avez-vous vos papiers devant vous ?",
            "Combien de fois avez-vous dû répéter votre histoire ?",
            "Qu'est-ce qui a fini par marcher, la dernière fois ?",
        ],
        notes="Beaucoup racontent avoir dû tout reprendre depuis le début à chaque "
              "transfert. C'est exactement ce que le numéro de dossier évite, et "
              "c'est pourquoi Teodora le donne dans sa première phrase.")

    d.dialogue('Dialogue 1 de 3', "Annoncer, puis tenir", [
        ("TEODORA", "Teodora Vlaicu, dossier 2026-41837. Je vous avais dit que je rappellerais après avoir lu le rapport.", True),
        ("MARJOLAINE", "Je vous écoute.", True),
        ("TEODORA", "Je conteste le refus, et je voudrais vous dire sur quoi. Trois points, ce sera court.", True),
        ("MARJOLAINE", "Allez-y.", True),
    ], consigne="Écoutez d'abord, diapositive masquée.",
       notes="Quatre répliques, et tout le cadre de l'appel est posé. Faire compter "
             "les mots de la troisième : elle annonce l'intention, le nombre et la "
             "durée. C'est la phrase à copier.")

    d.dialogue('Dialogue 2 de 3', "Un fait, une date, une pièce", [
        ("TEODORA", "Premièrement, votre lettre invoque le drain de plancher. Le rapport de votre expert décrit le drain de fondation. Ce ne sont pas les mêmes tuyaux.", True),
        ("MARJOLAINE", "Un instant… Effectivement, la lettre dit « drain de plancher ». Je le note.", True),
        ("TEODORA", "Deuxièmement, le drain de plancher a été nettoyé le 3 mai par Plomberie Chartier. J'ai la facture acquittée.", True),
        ("MARJOLAINE", "Cette pièce ne figure pas au dossier. Vous pouvez me l'envoyer aujourd'hui ?", True),
    ], notes="Faire remarquer « je le note » et « vous pouvez me l'envoyer » : ce sont "
             "les deux seules choses que l'agente peut faire, et Teodora les obtient "
             "toutes les deux. C'est ça, réussir l'appel.")

    d.dialogue('Dialogue 3 de 3', "Concéder, sans lâcher", [
        ("MARJOLAINE", "Madame Vlaicu, je dois vous dire une chose : ce n'est pas moi qui décide. Je transmets.", True),
        ("TEODORA", "Je le sais, et je ne vous en tiens pas rigueur. Certes, ce n'est pas vous qui avez fermé le dossier — il n'en reste pas moins que c'est à vous que je peux parler aujourd'hui.", True),
        ("MARJOLAINE", "C'est juste.", True),
        ("TEODORA", "Que le dossier soit rouvert, que la contre-expertise soit examinée par quelqu'un d'autre, et que la réponse me soit donnée par écrit, avec ses motifs.", True),
    ], notes="La réplique de Teodora est le modèle de la concession, et elle sera "
             "reprise telle quelle en C3. « C'est juste » est le signe qu'elle a "
             "fonctionné : l'agente cesse de se défendre.")

    d.regle("La personne au bout du fil ne décide pas",
            "Elle note, elle transmet, elle explique. Se fâcher contre elle "
            "n'ouvre aucune porte et ferme la seule qui l'était.",
            precision="Ce qu'on lui demande, c'est d'inscrire quelque chose au "
                      "dossier — et pour cela il faut que ce soit inscriptible : un "
                      "fait, une date, une pièce, une demande précise. « C'est "
                      "injuste » ne s'inscrit nulle part.",
            notes="Diapositive à photographier. C'est la règle qui change le plus de "
                  "choses dans la vie réelle des élèves, bien au-delà de l'assurance.")

    d.tableau('Analyse', "Ce que l'appel obtient, point par point",
              ['Ce que dit Teodora', 'Ce que ça produit'],
              [["Nom, numéro, date", "le dossier est ouvert à l'écran"],
               ["« Trois points, ce sera court »", "on l'écoute jusqu'au bout"],
               ["La contradiction des deux documents", "une note au dossier"],
               ["La facture du 3 mai", "une pièce demandée, donc versée"],
               ["« Dans combien de temps ? »", "une date qui existe"]],
              cle=0,
              notes="Diapositive à photographier. Chaque ligne de gauche est une "
                    "phrase à réutiliser telle quelle. Faire recopier la colonne de "
                    "gauche dans le cahier.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après l'appel.", [
        ("Teodora annonce d'avance combien de points elle va présenter.", "vrai"),
        ("La facture du nettoyage figurait déjà au dossier.", "faux - elle n'y est pas"),
        ("La contre-expertise a relevé des racines dans le drain de fondation.", "faux - aucune"),
        ("Teodora reproche à madame Pelchat d'avoir fermé le dossier.", "faux - elle la dédouane"),
        ("Elle demande que la révision soit faite par quelqu'un d'autre.", "vrai"),
        ("La réponse finale écrite est annoncée dans les soixante jours.", "vrai"),
    ], corrige=True,
       notes="Le quatrième est celui qui compte : faire relire la réplique de "
             "concession et demander au groupe ce qu'elle coûte à Teodora. Rien.")

    d.billet(
        "Écrivez votre première phrase d'appel, celle qui ouvre le dossier.",
        exemples=[
            "Votre nom, un numéro de dossier, une date.",
            "Puis la phrase qui annonce combien de points vous allez présenter.",
        ],
        notes="Deux phrases seulement. Elles seront dites à voix haute au début de "
              "E1, avant le jeu de rôle : chacun ouvre son propre appel.")

    return d.save(dossier)
