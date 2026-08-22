# -*- coding: utf-8 -*-
"""A2 · Trois portes, une seule question
Bloc A « Je découvre » · couleur framboise · 75 min.
Source : exercice `prDeux` et son bandeau, mini-leçon `prDeux`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A2', section='framboise',
        titre="Trois portes, une seule question",
        chapeau="Sous-louer, céder, résilier. Les trois mots parlent du même "
                "moment de la vie et ne mènent pas au même endroit.",
        duree='75 minutes')

    d.titre(notes="Reprendre les billets de sortie de A1 : lire deux ou trois "
                  "réponses à voix haute, sans nommer personne. Elles disent où en "
                  "est le groupe, et elles ouvrent la séance mieux qu'une consigne.")

    d.objectifs([
        "poser la seule question qui départage les trois démarches ;",
        "dire qui reste au bail dans chaque cas ;",
        "reconnaître le risque de la sous-location et l'accepter en "
        "connaissance de cause ;",
        "employer le mot juste dans une phrase complète.",
    ], notes="Le troisième objectif est un objectif de prudence, pas de grammaire. "
             "On ne cherche pas à décourager : on cherche à ce que personne ne "
             "signe sans savoir de quoi il répond.")

    d.declencheur(
        'Mise en situation', "Vous prêtez votre logement à quelqu'un. Il ne paie pas. Qui le propriétaire appelle-t-il ?",
        pistes=[
            "Et si vous aviez cédé votre bail plutôt que sous-loué ?",
            "Le propriétaire connaît-il seulement la personne qui habite là ?",
            "Qu'est-ce que vous auriez voulu savoir avant de dire oui ?",
        ],
        notes="Laisser le groupe se tromper. Presque tous répondent « la personne qui "
              "habite là ». La correction fait tout le poids de la séance : le "
              "locateur ne connaît que son locataire.")

    d.cartes('Analyse', "Ce que chaque démarche fait de vous", [
        ("Sous-louer", "Vous prêtez pour un temps. Le bail reste à votre nom, vous revenez à la date prévue, et vous répondez du loyer jusqu'au bout."),
        ("Céder son bail", "Vous transmettez le contrat. L'autre personne prend votre place aux mêmes conditions, et vous sortez du dossier pour de bon."),
        ("Résilier", "Vous mettez fin au bail avant son terme. La loi ne le permet que dans des situations précises, et il faut un avis en bonne et due forme."),
        ("La question qui tranche", "Après, qui est encore au bail ? Vous, l'autre, ou personne. Trois réponses possibles, trois portes différentes."),
    ], notes="Une carte à la fois. Demander un exemple de vie réelle entre chaque : "
             "quelqu'un qui part aux études, quelqu'un qui déménage, quelqu'un qui "
             "ne peut plus payer. Les trois cas existent dans presque tous les "
             "groupes.")

    d.tableau('Comparaison', "La même situation, trois issues",
              ['Ce que la personne veut', 'La porte'],
              [["Je pars six mois et je reviens", "sous-location"],
               ["Je déménage en février pour de bon", "cession de bail"],
               ["Ma sœur prendra le logement jusqu'à la fin", "cession de bail"],
               ["J'accepte de répondre si l'autre ne paie pas", "sous-location"]],
              cle=1,
              notes="Faire justifier chaque ligne par la question du tableau de A1. "
                    "Ne pas donner la réponse : la faire trouver, ligne par ligne.")

    d.regle("La sous-location ne vous libère de rien",
            "Le locateur ne connaît que son locataire.",
            precision="Si votre sous-locataire ne paie pas, c'est vous qui devez "
                      "le loyer. Si votre sous-locataire abîme le logement, c'est "
                      "vous qu'on ira voir. C'est ensuite à vous de vous retourner "
                      "vers lui. C'est le prix à payer pour garder son logement — "
                      "et c'est pour cela qu'on demande des références.",
            notes="Diapositive à photographier. C'est la phrase à retenir de tout le "
                  "bloc A. La faire redire par trois élèves différents avant de "
                  "passer à la suite.")

    d.piege('Attention',
            "« J'ai sous-loué, donc je ne suis plus responsable de rien. »",
            "« J'ai sous-loué, et je réponds encore de tout jusqu'au 30 juin. »",
            "C'est la croyance la plus répandue, et la plus coûteuse. La "
            "sous-location déplace l'occupant, jamais la responsabilité. Elle "
            "n'existe d'ailleurs que pour ça : garder le bail à son nom.",
            notes="Prendre le temps. Demander à quelqu'un de reformuler dans ses mots, "
                  "puis vérifier avec un deuxième élève que la reformulation était "
                  "juste.")

    d.vocabulaire('Vocabulaire', "Trois mots à ne pas confondre", [
        ("la sous-location", "Le fait de prêter son logement à quelqu'un pour un temps, en gardant son bail à son nom."),
        ("la cession de bail", "Le fait de transmettre son bail à quelqu'un d'autre et de sortir du contrat pour de bon."),
        ("la résiliation", "La fin d'un contrat avant la date prévue, dans les cas que la loi permet."),
    ], notes="Insister sur le préfixe « sous- » : il veut dire « qui dépend de ». Un "
             "sous-locataire dépend du locataire, jamais directement du locateur. Ce "
             "préfixe explique à lui seul toute la responsabilité.")

    d.pratique('Pratique', "Sous-location ou cession ?",
               "Dites de quoi il s'agit dans chaque cas.", [
        ("Farida garde son bail et reprend son logement le premier juillet.", "sous-location"),
        ("La personne qui arrive devient locataire à la place de celle qui part.", "cession"),
        ("Le locataire de départ reste responsable du loyer jusqu'à la fin.", "sous-location"),
        ("Le nom au bail change, et l'ancien locataire n'a plus rien à y voir.", "cession"),
        ("L'entente porte sur une période avec une date de fin.", "sous-location"),
        ("On prête son logement pendant qu'on travaille ailleurs six mois.", "sous-location"),
    ], corrige=True,
       notes="Corriger en faisant reposer la question à chaque fois : après, qui est "
             "encore au bail ? Le but n'est pas la bonne réponse, c'est le réflexe.")

    d.billet(
        "Écrivez une phrase complète qui commence par « Je veux sous-louer parce que… »",
        exemples=[
            "Inventez la raison si vous voulez.",
            "Attention au mot : sous-louer, pas céder.",
        ],
        notes="Deux minutes. Ramasser les billets : ceux qui écrivent « céder » sans "
              "s'en rendre compte sont ceux à suivre de près en A4 et en C2.")

    return d.save(dossier)
