# -*- coding: utf-8 -*-
"""E2 · Réponds à Ousmane, et parle-lui de l'article
Bloc E « Je me lance » · couleur framboise · bilan · 75 min.
Source : bloc `appli` de `custom.js` — la production écrite et ses dix
exigences —, banc FC_CARDS, autoévaluation en seize énoncés.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='E2', section='framboise',
        titre="Réponds à Ousmane, et parle-lui de l'article",
        chapeau="Un seul courriel, deux travaux : donner des nouvelles, et "
                "informer quelqu'un du contenu d'un article. Ce sont les "
                "deux intentions du programme.",
        duree='75 minutes')

    d.titre(notes="Dernière séance du module. Ressortir les billets de A3 — l'objet "
                  "écrit en début de module — et de D2 — la première phrase. Chacun "
                  "commence son courriel avec ce qu'il a déjà.")

    d.objectifs([
        "écrire un courriel de dix à quatorze phrases en trois ou quatre paragraphes ;",
        "réagir à une bonne nouvelle et à une triste, chacune avec le mot juste ;",
        "résumer un article en citant sa source ;",
        "annoncer son avis comme un avis, dans un paragraphe à part.",
    ], notes="Les quatre objectifs sont les quatre exigences majeures de la grille. "
             "Les lire à voix haute avant que le groupe commence à écrire.")

    d.declencheur(
        'Préparation', "Qu'est-ce que tu as à raconter, toi ?",
        pistes=[
            "Un évènement de ton côté, avec une date ou une durée.",
            "Quelque chose qui était déjà arrivé avant le reste.",
            "Ce que tu penses du programme de jumelage.",
            "Note trois idées avant d'écrire une seule phrase.",
        ],
        notes="Cinq minutes de notes en vrac, sans phrases. Passer voir : ceux qui "
              "écrivent des phrases dès la préparation finissent par un texte plat.")

    d.tableau('Plan', "Quatre paragraphes, quatre travaux",
              ['Le paragraphe', 'Ce qu\'il contient'],
              [["1", "tu réagis à ses nouvelles : félicitations, condoléances"],
               ["2", "tu donnes les tiennes, avec une date ou une durée"],
               ["3", "l'article : ce que c'est, pour qui, combien de temps, la source"],
               ["4", "ton avis, annoncé comme un avis, et ce qu'il peut faire"]],
              cle=0,
              note="Objet de trois à six mots, formule d'appel, salutation, signature.",
              notes="Diapositive à photographier. C'est le plan de D2, appliqué au "
                    "courriel complet. Les élèves l'ont déjà dans leur cahier.")

    d.tableau('Grille', "Ce que le texte doit contenir",
              ['L\'exigence', 'Un exemple'],
              [["Le mot juste", "toutes mes condoléances, bon rétablissement"],
               ["Un plus-que-parfait", "quand tu m'as écrit, j'avais déjà changé d'horaire"],
               ["Une reprise", "ce programme, je le trouve utile ; j'en ai parlé"],
               ["Deux connecteurs", "pourtant, d'ailleurs, c'est pourquoi"],
               ["Une relative avec où", "l'année où je suis arrivée à Saint-Hyacinthe"],
               ["Un avis annoncé", "à mon avis, ça conviendrait bien à Kadiatou"]],
              cle=0,
              notes="Diapositive à photographier. Six rangées, pas de note : c'est la "
                    "densité maximale. La grille complète, à dix exigences, est dans "
                    "le module à l'écran.")

    d.piege('Information', "Il y a un super programme, tu devrais t'inscrire",
            "L'organisme jumelle des familles pour six mois. À mon avis, c'est utile",
            "La première phrase n'est qu'un avis : celui qui la lit ne sait toujours "
            "pas ce qu'est le programme. La seconde donne le fait, puis l'avis, et "
            "les sépare. C'est la différence entre informer quelqu'un et le "
            "convaincre.",
            notes="Le piège le plus fréquent de cette production. Le montrer avant "
                  "l'écriture, pas à la correction.")

    d.pratique('Vocabulaire', "Les seize mots du module",
               "Reformez les quatre familles, puis employez un mot de chacune.", [
        ("Les évènements", "une naissance, un déménagement, des funérailles, un faire-part"),
        ("Ce que le courriel raconte", "un accident de travail, une réadaptation, des retrouvailles, un imprévu"),
        ("Décrire une personne", "une silhouette, un visage allongé, des cheveux ondulés, un signe particulier"),
        ("Le quartier et son journal", "un jumelage, un organisme communautaire, un bénévole, une coordonnatrice"),
    ], corrige=True,
       notes="Révision avant l'écriture. Les élèves ont aussi les cartes mémoire dans "
             "la section « Je retiens des mots » du module.")

    d.regle("Garde ton avis pour un paragraphe à part",
            "Un courriel qui mêle le fait et l'opinion n'informe personne.",
            precision="Ousmane n'a pas lu l'article. Tout ce qu'il en saura vient de "
                      "toi. Sépare : voici ce que le journal écrit, voici ce que j'en "
                      "pense. Il pourra alors se faire sa propre idée — et c'est ça, "
                      "informer quelqu'un.",
            notes="Diapositive à photographier. Dernière règle du module, et la plus "
                  "transférable : elle vaut pour tout ce qu'on rapporte à quelqu'un.")

    d.billet(
        "Qu'est-ce que tu sais faire maintenant que tu ne savais pas faire ?",
        exemples=[
            "Une ou deux phrases.",
            "Regarde la liste d'autoévaluation du module avant de répondre.",
        ],
        notes="Cinq minutes cette fois, pas deux. Ce billet ferme le module : le "
              "ramasser et le remettre à chacun à la première séance du module "
              "suivant.")

    return d.save(dossier)
