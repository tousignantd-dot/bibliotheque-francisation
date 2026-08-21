# -*- coding: utf-8 -*-
"""C2 · « Après avoir vérifié… »
Bloc C « Défi 2 · La demande » · couleur ambre · 75 min. L'infinitif passé.
Source : exercice `t2infpasse`, mini-leçon du même nom.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C2', section='ambre',
        titre="« Après avoir vérifié… »",
        chapeau="Deux actions qui se suivent, un seul sujet : l'infinitif "
                "passé les met dans une phrase et donne à la description ce "
                "ton professionnel qu'un employeur reconnaît tout de suite.",
        duree='75 minutes')

    d.titre(notes="Point de grammaire central du bloc C. Il paraît savant ; il est en "
                  "réalité très mécanique — deux morceaux, jamais plus.")

    d.objectifs([
        "former l'infinitif passé avec avoir ou avec être ;",
        "accorder le participe quand l'auxiliaire est être ;",
        "l'employer pour décrire des tâches qui se suivent ;",
        "ne pas le confondre avec « avant de » + infinitif présent.",
    ])

    d.declencheur(
        'Observation', "Deux phrases, ou une seule ?",
        pistes=[
            "« Je vérifiais les commandes. Ensuite, je préparais les bons. »",
            "« Après avoir vérifié les commandes, je préparais les bons. »",
            "Laquelle sonne le plus professionnelle ?",
            "Combien de fois le sujet est-il dit, dans chacune ?",
        ],
        notes="Le groupe entend la différence avant de savoir la nommer. Partir de là "
              "plutôt que de la grammaire.")

    d.tableau('Anatomie', "Deux morceaux, jamais plus",
              ['Le morceau', 'Ce qu\'il vaut'],
              [["après", "le mot d'entrée : il annonce ce qui s'est passé avant"],
               ["avoir ou être", "à l'infinitif — on ne conjugue rien"],
               ["le participe passé", "vérifié, reçu, rempli, arrivée"]],
              cle=0,
              note="Après avoir vérifié les commandes, je préparais les bons de livraison.",
              notes="Diapositive à photographier. Le fait qu'on ne conjugue rien est ce "
                    "qui rend la forme facile : le dire explicitement.")

    d.regle("Avec « être », le participe s'accorde",
            "Après être arrivée au Québec, elle a suivi une formation.",
            precision="Les verbes de déplacement — arriver, partir, venir, rester, "
                      "entrer, sortir — et les verbes pronominaux prennent être. Le "
                      "participe s'accorde alors avec la personne qui parle : Marisol "
                      "écrit « arrivée » avec deux e. Le test : si vous dites « je suis "
                      "arrivé » au passé composé, alors c'est « après être arrivé ».",
            notes="Diapositive à photographier. Le test du passé composé règle tous les "
                  "cas sans nouvelle liste à apprendre.")

    d.pratique('Application', "Mettez le verbe à l'infinitif passé",
               "Attention à l'auxiliaire et à l'accord.", [
        ("Après ___ les livraisons, je vérifiais les quantités. (recevoir)", "avoir reçu"),
        ("Après ___ six ans dans les stocks, elle connaît le métier. (travailler)", "avoir travaillé"),
        ("Après ___ au Québec, Marisol a cherché un emploi. (arriver)", "être arrivée"),
        ("Après ___ le formulaire, relisez-le à voix haute. (remplir)", "avoir rempli"),
        ("Après ___ à l'entrevue, il a envoyé un remerciement. (se présenter)", "s'être présenté"),
        ("Avant ___ , vérifiez votre courriel. (envoyer)", "d'envoyer — infinitif présent !"),
    ], corrige=True,
       notes="Le dernier item est le piège de la séance. Ne pas l'annoncer : le laisser "
             "se produire, puis expliquer.")

    d.piege("« Avant d'être parti »",
            "Avant d'être parti, vérifiez votre dossier.",
            "Avant de partir, vérifiez votre dossier.",
            "« avant de » demande toujours l'infinitif présent. Seul « après » prend "
            "l'infinitif passé, et c'est logique : « après » regarde en arrière, « avant "
            "de » regarde en avant. La forme « avant d'être parti » n'existe pas.",
            notes="Faire redire la paire : après avoir fait / avant de faire. Deux "
                  "formes, deux directions.")

    d.pratique('Rédaction', "Vos propres tâches",
               "Écrivez trois phrases sur votre dernier emploi, avec « après avoir ».", [
        ("Une tâche du matin", "Après avoir ouvert le magasin, je…"),
        ("Une tâche qui en suit une autre", "Après avoir vérifié…, je…"),
        ("Une étape de votre parcours", "Après être arrivé(e) au Québec, j'ai…"),
    ], corrige=True,
       notes="Circuler pendant l'écriture. L'accord du participe avec être est l'erreur "
             "à corriger individuellement ; elle ne se règle pas au tableau.")

    d.regle("Un seul sujet",
            "Les deux actions doivent avoir la même personne comme sujet.",
            precision="« Après avoir vérifié les commandes, mon chef partait » laisse "
                      "croire que c'est le chef qui a vérifié. Quand les sujets "
                      "diffèrent, il faut deux phrases — ou un « quand » : « Quand "
                      "j'avais vérifié les commandes, mon chef partait. »",
            notes="Diapositive à photographier. Cette contrainte est la seule vraie "
                  "limite de la forme.")

    d.billet(
        "Reprenez votre description de tâches et ajoutez-y « après avoir ».",
        exemples=[
            "Une seule phrase suffit.",
            "Relisez à voix haute : si vous butez, la phrase est trop longue.",
        ],
        notes="Le billet prépare directement la production écrite. Demander de garder la "
              "feuille jusqu'à E1.")

    return d.save(dossier)
