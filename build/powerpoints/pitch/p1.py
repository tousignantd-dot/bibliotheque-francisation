# -*- coding: utf-8 -*-
"""P1 · Ce qu'il y a dans la boîte — le matériel, en chiffres et en structure.
Section teal · le troisième quart d'heure d'une rencontre.
Source : les comptes de `pitch/chiffres.py`, relevés sur le dépôt.
"""
from theme import Deck
from vues import ecran, poser
from chiffres import CH, n
from parcours import TEMPS


def build(dossier):
    d = Deck(
        code='P1', section='teal',
        titre="Ce qu'il y a dans la boîte",
        chapeau="La question qui vient toujours après la démonstration : « et qui va "
                "préparer tout ça ? ». La réponse est que c'est déjà préparé — %s séances "
                "de cours, chacune avec sa fiche et son diaporama."
                % n(CH['decks']),
        duree='8 minutes')

    d.titre(surtitre="PRÉSENTATION  ·  1 SUR 3",
            notes="Ne pas commencer par les chiffres. Demander d'abord combien d'heures "
                  "de préparation une séance leur coûte aujourd'hui, et laisser répondre.")

    d.parcours(TEMPS, 0,
               notes="Annoncer les trois temps et leur durée. Une salle qui sait "
                     "combien il reste écoute mieux.")

    d.chapitre("PREMIER TEMPS", "Ce qu'il y a dans la boîte",
               "Une séance de cours, c'est une fiche pour l'élève et un diaporama "
               "pour vous. %s fois." % n(CH['decks']),
               notes="Jalon. Laisser deux secondes de silence avant de passer : "
                     "c'est la phrase que la salle doit emporter.")

    d.objectifs([
        "voir ce qu'un enseignant reçoit, sans rien préparer ;",
        "comprendre pourquoi la fiche et le diaporama ne peuvent pas diverger ;",
        "savoir ce que le matériel couvre, niveau par niveau ;",
        "repartir avec un ordre de grandeur, pas une impression.",
    ], notes="Quatre points, quatre minutes. Le reste de la séance est du détail sur "
             "demande.")

    d.regle('La règle qui tient tout',
            "Une séance, c'est une fiche pour l'élève et un diaporama pour vous.",
            precision="Les deux sortent du même fichier de contenu. Corriger une règle "
                      "la corrige des deux côtés : il n'existe pas de version à jour et "
                      "de version oubliée. C'est %s fois la même promesse."
                      % n(CH['decks']),
            notes="C'est la diapositive à laisser à l'écran pendant les questions. "
                  "Si une seule idée doit rester, c'est celle-là.")

    # Huit niveaux ne tiennent pas sur une diapositive projetée — le thème le
    # refuse, et il a raison : on ne lit pas neuf rangées au fond d'une salle.
    # Deux niveaux par rangée, et le total en dernier.
    def paire(a, b):
        mods = (CH['modules_par_niveau'].get(a, 0)
                + CH['modules_par_niveau'].get(b, 0))
        sea = CH['par_niveau'].get(a, 0) + CH['par_niveau'].get(b, 0)
        return ['%s et %s' % (a.replace('Niveau ', ''), b.replace('Niveau ', '')),
                str(mods), str(sea)]

    lignes = [paire('Niveau 1', 'Niveau 2'), paire('Niveau 3', 'Niveau 4'),
              paire('Niveau 5', 'Niveau 6'), paire('Niveau 7', 'Niveau 8'),
              ['Tous', str(CH['cours']), n(CH['decks'])]]
    d.tableau('Le compte', "Ce qui existe aujourd'hui",
              ['Niveaux', 'Modules', 'Séances'],
              lignes, cle=0,
              note="Chaque séance a sa fiche : %s fiches pour %s séances."
                   % (n(CH['fiches']), n(CH['decks'])),
              notes="Ne pas lire le tableau. Le laisser à l'écran et donner la dernière "
                    "ligne : c'est la seule que quelqu'un retient.")

    ecran(d, "Ce que l'enseignant ouvre", "Le dépôt de matériel",
          poser('mat', '05-materiel-catalogue'),
          "Diaporamas et fiches au même endroit, filtrés par bloc. « 16 séances "
          "équipées sur 16 » : rien à préparer.",
          notes="La capture qui répond à « qui va préparer tout ça ? » mieux que "
                "n'importe quel chiffre. Laisser deux secondes de silence.")

    d.cartes('Dans un module', "Ce que l'élève trouve, et ce qu'il ne trouve pas ailleurs",
             [("Des voix, pas une lecture", "Chaque dialogue est enregistré par des voix "
               "différentes, au débit qu'on choisit. %s pistes audio produites."
               % n(CH['mp3'])),
              ("Sept familles d'exercices", "Vrai ou faux, association, cases à écrire, "
               "texte à trous, images, question ouverte, tableau. Pas une de plus : "
               "l'élève apprend une fois comment on répond."),
              ("Des mini-leçons", "La règle avec ses exemples, ouverte au moment où "
               "l'élève se trompe, pas au début du chapitre."),
              ("Des images produites pour la scène", "%s images, cadrées pour la "
               "situation du module — jamais une banque d'images décorative."
               % n(CH['images']))],
             notes="Insister sur les voix : c'est ce qui permet à l'élève d'écouter "
                   "quinze fois sans user la patience de personne.")

    d.cartes('Pour vous', "Le diaporama d'une séance, bloc par bloc",
             [("La règle", "un énoncé, gros, seul : la diapositive que les élèves "
               "photographient"),
              ("L'exercice projeté", "le même que dans le module, suivi de son corrigé, "
               "à la même place"),
              ("Le piège", "ce qu'on entend souvent, à côté de ce qu'il faut dire"),
              ("Le billet de sortie", "la dernière diapositive, celle qui ferme la "
               "séance — %s notes de présentateur en tout" % n(CH['notes']))],
             notes="Le chiffre des notes est celui qui compte pour un remplaçant : la "
                   "séance se donne sans avoir été écrite par soi.")

    ecran(d, "Pour vous", "Une séance, telle qu'elle est projetée",
          poser('mat', '10-diapo-titre'),
          "La première diapositive d'une séance de quatre heures. Il y en a "
          "seize par module, et elles se donnent sans avoir été écrites par soi.",
          notes="Dire que ce que la salle regarde en ce moment sort du même "
                "système : c'est le produit qui se présente lui-même.")

    d.piege('Ce qu\'on entend',
            "« Du matériel tout fait, mes enseignants n'en voudront pas. »",
            "« Le matériel est ouvert : on prend une séance, on la change, on la dépose. »",
            "Le dépôt accepte la version d'un enseignant à côté de l'officielle, sans "
            "jamais l'écraser. Ce n'est pas un manuel fermé : c'est un point de départ "
            "qui existe le lundi matin.",
            notes="Objection réelle, entendue en salle. Ne pas la balayer : montrer le "
                  "bouton « Remplacer l'officiel » dans le dépôt de matériel.")

    d.billet("Une question, avant de passer à la suite : combien d'heures par semaine "
             "vos enseignants passent-ils à fabriquer du matériel ?",
             exemples=["%s heures de classe sont déjà préparées." % n(CH['heures']),
                       "Elles ne remplacent personne : elles se donnent."],
             notes="Laisser le silence. C'est la question qui fait passer la rencontre "
                   "de « joli produit » à « combien on économise ».")

    return d.save(dossier)
