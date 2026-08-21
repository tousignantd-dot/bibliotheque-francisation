# -*- coding: utf-8 -*-
"""B1 · Quarante-quatre heures, payées quarante-quatre.
Bloc B « Défi 1 · Une erreur sur la paie » · couleur acier · 75 min.
Source : dialogue `t1`, exercice `t1vf`.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n8-emploi/images/')


def build(dossier):
    d = Deck(
        code='B1', section='acier',
        titre="Quarante-quatre heures, payées quarante-quatre",
        chapeau="Avoir raison ne suffit pas. Encore faut-il le dire de "
                "manière à obtenir une correction plutôt qu'une discussion : "
                "des faits datés, une règle citée, et une date de retour.",
        duree='75 minutes')

    d.titre(notes="Ouverture du Défi 1, le plus utile du module. Demander qui a déjà "
                  "trouvé une erreur sur sa paie, et ce qu'il en a fait. Beaucoup n'ont "
                  "rien fait — c'est le point de départ.")

    d.objectifs([
        "comprendre un échange téléphonique administratif long et nuancé ;",
        "exposer un problème avec ses dates et ses chiffres ;",
        "répondre à une objection de procédure sans hausser le ton ;",
        "obtenir un engagement daté et une confirmation écrite.",
    ], notes="Les objectifs 3 et 4 sont ceux qui distinguent le niveau 8. Exposer, "
             "beaucoup savent le faire ; tenir après l'objection, non.")

    d.declencheur(
        'Observation', "Savez-vous lire votre relevé de paie ?",
        image=IMG + 'releve-paie-ecran.jpg',
        pistes=[
            "Combien d'heures y sont inscrites ?",
            "À quel taux chacune est-elle payée ?",
            "Y a-t-il une ligne que vous n'avez jamais comprise ?",
            "Le vérifiez-vous chaque période ?",
        ],
        notes="Question très concrète. Prévoir que plusieurs répondront qu'ils ne le "
              "lisent jamais. C'est justement le sujet.")

    d.dialogue('Dialogue · 1 de 3', "L'appel commence par des chiffres", [
        ("NADIA", "J'appelle au sujet de mon relevé de paie de la période du deux au quinze août. Je pense qu'il y a une erreur.", True),
        ("SYLVAIN", "Sylvain Ouellet, service de la paie. Vous avez le relevé devant vous ?", True),
        ("NADIA", "La semaine de l'inventaire, j'ai fait quarante-quatre heures. Elles sont toutes payées au taux simple.", True),
        ("SYLVAIN", "Effectivement, je vois quarante-quatre heures saisies. Mais il faudrait vérifier si elles ont été autorisées.", True),
    ], consigne="Écoutez d'abord, diapositive masquée.",
       notes="Nadia donne la période, les heures et le taux en trois phrases. Faire "
             "compter les informations : cinq données en quinze secondes.")

    d.dialogue('Dialogue · 2 de 3', "L'objection, et la réponse", [
        ("SYLVAIN", "L'autorisation et la majoration, ce sont deux choses différentes dans notre système.", True),
        ("NADIA", "Je comprends que c'est deux champs différents pour vous. De mon côté, j'ai travaillé quatre heures au-delà de quarante.", True),
        ("NADIA", "Au Québec, au-delà de quarante heures, la majoration est de cinquante pour cent. C'est la norme, pas une politique de l'entreprise.", True),
        ("SYLVAIN", "Vous avez raison sur la règle, je ne la conteste pas. Ce que je ne peux pas faire, c'est corriger sans approbation.", True),
    ], notes="Le cœur de la séance. Nadia reconnaît la contrainte de l'autre avant "
             "d'opposer la sienne. Sans cette reconnaissance, l'appel devient une "
             "chicane et le dossier n'avance pas.")

    d.dialogue('Dialogue · 3 de 3', "Repartir avec une date", [
        ("NADIA", "D'accord. Alors soyons pratiques : qu'est-ce qu'il vous faut, exactement, et de qui ?", True),
        ("SYLVAIN", "Un courriel de madame Trépanier qui confirme les quatre heures, avec la mention « heures supplémentaires autorisées ».", True),
        ("NADIA", "Est-ce que vous pouvez me confirmer par écrit ce qu'on vient de se dire ? Le dossier a déjà traîné trois semaines.", True),
        ("SYLVAIN", "Aucun problème, c'est légitime. Je vous envoie un courriel dans l'heure avec le numéro de dossier.", True),
    ], notes="« Qu'est-ce qu'il vous faut, de qui, et pour quand » est la phrase à "
             "retenir de tout le bloc B. La faire répéter par chacun.")

    d.tableau('Analyse', "Quatre gestes qui font avancer un dossier",
              ['Le geste', 'Ce qu\'il produit'],
              [["Donner la période et les chiffres", "l'autre trouve le dossier tout de suite"],
               ["Reconnaître la contrainte de l'autre", "il cesse de se défendre"],
               ["Citer la règle sans accuser", "le désaccord porte sur un fait, pas sur une personne"],
               ["Demander quoi, de qui, pour quand", "on repart avec une action, pas une promesse"]],
              cle=0,
              note="Aucun de ces quatre gestes ne demande de hausser le ton.",
              notes="Diapositive à photographier. C'est le plan du jeu de rôle de E1.")

    d.regle("La phrase qui débloque",
            "Qu'est-ce qu'il vous faut, exactement, et de qui ?",
            precision="Elle transforme une objection en marche à suivre. La personne au "
                      "bout du fil n'a pas commis l'erreur et n'a souvent pas le pouvoir "
                      "de la corriger seule ; lui demander ce dont elle a besoin la met "
                      "de votre côté. Ajoutez « et pour quand ? » : sans date, rien "
                      "n'est décidé.",
            notes="Diapositive à photographier. Elle sert aussi bien pour une paie que "
                  "pour un logement, une garderie ou une clinique.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après l'appel.", [
        ("Nadia a travaillé 44 heures la semaine de l'inventaire.", "vrai"),
        ("Les 44 heures n'apparaissent pas sur le relevé.", "faux — elles y sont, au taux simple"),
        ("Sylvain conteste la règle des 50 %.", "faux — il ne la conteste pas"),
        ("Il faut un courriel de la superviseure.", "vrai"),
        ("La correction paraîtra sur la paie du 29 si le document arrive avant mercredi midi.", "vrai"),
        ("Nadia demande une confirmation écrite par méfiance.", "faux — parce que le dossier a traîné"),
        ("La période du 2 au 9 août était correcte.", "faux — le même écart s'y trouve"),
    ], corrige=True,
       notes="Faire justifier chaque réponse par la réplique. L'appel est long : deux "
             "écoutes, en s'arrêtant après l'objection de Sylvain.")

    d.billet(
        "Sortez votre dernier relevé de paie et vérifiez trois choses.",
        exemples=[
            "Le nombre d'heures, le taux, et le total.",
            "Y a-t-il une semaine au-dessus de quarante heures ?",
        ],
        notes="Devoir concret. Prévenir que certains trouveront une vraie erreur : "
              "c'est arrivé dans presque tous les groupes.")

    return d.save(dossier)
