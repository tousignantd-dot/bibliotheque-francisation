# -*- coding: utf-8 -*-
"""A3 · Les mots du dossier, et ce qu'ils désignent
Bloc A « Je découvre » · couleur framboise · 75 min.
Source : exercices `prVocab` et `prImg`, banc `FC_CARDS`.
"""
from theme import Deck

import pathlib

IMG = str(pathlib.Path(__file__).resolve().parents[4]
          / 'assets' / 'interactive' / 'module-n8-habitation' / 'images') + '/'


def build(dossier):
    d = Deck(
        code='A3', section='framboise',
        titre="Dix mots qu'on ne peut pas remplacer",
        chapeau="Un dossier d'assurance a son vocabulaire, et il n'a pas de "
                "synonyme. Employer « le tuyau » à la place de « le drain de "
                "fondation » suffit à rendre une contestation illisible.",
        duree='75 minutes')

    d.titre(notes="Séance de vocabulaire. Prévenir le groupe : dans ce module, "
                  "employer le mot exact n'est pas une élégance, c'est ce qui décide "
                  "si l'on vous répond. Le module entier repose sur deux mots qu'on "
                  "confond — plancher et fondation.")

    d.objectifs([
        "nommer les dix mots restants du dossier avec leur article ;",
        "distinguer le drain de plancher du drain de fondation ;",
        "associer un mot à la scène qu'il désigne ;",
        "reconnaître les mots qui ne se laissent pas remplacer par un synonyme.",
    ], notes="Le deuxième objectif est le pivot du module : toute la contestation de "
             "Teodora tient à cette différence-là.")

    d.declencheur(
        'Observation', "Où est le drain, sur cette photo, et à quoi sert-il ?",
        image=IMG + 'drain-de-plancher.jpg',
        pistes=[
            "Où se trouve ce drain : dedans ou dehors ?",
            "Qu'est-ce qui a été soulevé, et pourquoi ?",
            "Que voit-on autour de l'ouverture ?",
            "Y a-t-il un drain comme celui-là chez vous ?",
        ],
        notes="Laisser observer avant de nommer. Le cerne brunâtre autour de "
              "l'ouverture est ce que l'expert appellera « un dépôt » : c'est le seul "
              "constat visuel de tout son rapport.")

    d.vocabulaire('Vocabulaire 1 de 2', "Le sinistre et l'installation", [
        ("un clapet antiretour", "Un petit dispositif installé sur un drain, qui laisse l'eau sortir mais l'empêche de revenir."),
        ("un drain de fondation", "Le tuyau perforé posé au pied des murs d'un bâtiment pour évacuer l'eau du sol."),
        ("un expert en sinistre", "La personne qui examine les dommages, en cherche la cause et évalue ce qu'ils coûtent."),
        ("une contre-expertise", "Un second examen, demandé par l'assuré, qui vient discuter les conclusions du premier."),
        ("un constat", "Ce qu'une personne a vu de ses propres yeux et qu'elle écrit sans l'interpréter."),
    ], notes="Faire répéter avec l'article. « Contre-expertise » est le mot que "
             "personne ne connaît et qui change tout : on peut payer son propre "
             "expert, et beaucoup de gens l'ignorent toute leur vie.")

    d.vocabulaire('Vocabulaire 2 de 2', "Le refus et le recours", [
        ("le défaut d'entretien", "Le reproche fait à quelqu'un de ne pas avoir entretenu ce dont il avait la charge."),
        ("une facture acquittée", "Une facture accompagnée de la preuve qu'elle a bien été payée."),
        ("une réponse finale", "La dernière position écrite d'une entreprise sur une plainte, avec ses raisons."),
        ("un transfert de dossier", "L'envoi de tout le dossier d'une plainte à l'organisme public qui surveille l'entreprise."),
        ("une décision motivée", "Une décision qui dit non seulement ce qui est décidé, mais sur quoi elle s'appuie."),
    ], notes="« Acquittée » mérite un arrêt : une facture n'est pas une preuve de "
             "paiement. Beaucoup d'élèves envoient la facture et pas le reçu, et le "
             "dossier reste incomplet sans que personne le leur dise.")

    d.regle("Deux drains, et tout le module tient à la différence",
            "Le drain de plancher est à l'intérieur, dans la dalle du "
            "sous-sol. Le drain de fondation est à l'extérieur, au pied des "
            "murs, sous la terre. Ce ne sont ni le même tuyau, ni le même "
            "entretien, ni la même responsabilité.",
            precision="La lettre de refus de Teodora parle du drain de plancher. Le "
                      "rapport d'expertise du même assureur décrit le drain de "
                      "fondation. Personne chez l'assureur ne l'avait remarqué, et "
                      "c'est là que se gagne la révision.",
            notes="Diapositive à photographier, et la plus importante de la séance. "
                  "Faire dessiner les deux au tableau, en coupe. Trente secondes de "
                  "craie valent un paragraphe.")

    d.pratique('Vocabulaire', "Le mot juste",
               "Complétez avec le mot exact du dossier.", [
        ("La protection ajoutée au contrat en 2023 s'appelle un ___.", "avenant"),
        ("Les mille dollars qui restent à ma charge, c'est la ___.", "franchise"),
        ("Le cas nommé au contrat pour lequel on ne paie pas, c'est une ___.", "exclusion"),
        ("Le second examen que j'ai payé, c'est une ___.", "contre-expertise"),
        ("La preuve que la facture a été payée : une facture ___.", "acquittée"),
        ("La dernière position écrite de l'entreprise : une ___.", "réponse finale"),
    ], corrige=True,
       notes="Exercice à faire à l'oral d'abord, sans écrire. Les articles comptent : "
             "refuser « avenant » sans « un ».")

    d.pratique('Association', "Quelle photo pour quelle phrase ?",
               "Six scènes du sous-sol, deux jours après le sinistre.", [
        ("Un sous-sol fini où l'eau brune arrive à mi-mollet, entre un divan et une bibliothèque basse.",
         "sous-sol-inonde"),
        ("Le drain rond au centre d'une dalle de béton, sa grille de fonte soulevée et posée à côté.",
         "drain-de-plancher"),
        ("Des lés de plancher flottant gondolés et des bacs de plastique empilés au bord d'un trottoir.",
         "bord-de-trottoir"),
        ("Deux ventilateurs de séchage posés au pied d'un mur dont le gypse a été coupé à mi-hauteur.",
         "ventilateurs-sechage"),
        ("Un regard d'égout dans une ruelle de brique, l'eau qui affleure au ras de la fonte.",
         "regard-ruelle"),
        ("Un touret de câble de caméra déroulé sur le béton, devant l'ouverture d'un drain de fondation.",
         "camera-de-drain"),
    ], corrige=True,
       notes="Faire décrire chaque photo à voix haute avant de l'associer. La "
             "sixième anticipe le bloc B : c'est la caméra de la contre-expertise, "
             "et l'assureur ne l'a jamais passée.")

    # `capture` n'existe que dans theme.Deck : les présentations la portent,
    # les fiches imprimées non (build/powerpoints/fiche.py n'a pas la
    # méthode). Une fiche noir et blanc n'a de toute façon rien à faire
    # d'une capture d'écran.
    if hasattr(d, 'capture'):
        d.capture('prImg', "L'exercice tel que les élèves le verront",
                  consigne="Glissez chaque photo sur la phrase qui la décrit.",
                  notes="Ouvrir le module. Faire travailler à deux : celui qui glisse "
                        "doit dire pourquoi avant de lâcher la photo.")

    d.billet(
        "Écrivez les cinq mots du dossier que vous ne connaissiez pas ce matin.",
        exemples=[
            "Un mot par ligne, avec son article.",
            "À côté de chacun, la définition dans vos propres mots.",
        ],
        notes="La liste sert de repère personnel pour tout le module. Ceux qui en "
              "trouvent moins de cinq peuvent écrire ceux dont ils ne sont pas sûrs.")

    return d.save(dossier)
