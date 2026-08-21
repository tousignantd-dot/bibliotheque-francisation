# -*- coding: utf-8 -*-
"""B4 · Prendre des notes pendant un appel.
Bloc B « Défi 1 · L'appel » · couleur ambre · 75 min.
Source : exercices `t1notes` et `t1fiche`, mini-leçon `t1notes`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B4', section='ambre',
        titre="Prendre des notes pendant un appel",
        chapeau="Écouter et écrire en même temps, dans une langue qu'on "
                "apprend, est difficile. La solution n'est pas d'écrire plus "
                "vite : c'est d'avoir moins à écrire.",
        duree='75 minutes')

    d.titre(notes="Fin du défi 1. Commencer par lire à voix haute deux ou trois séries de "
                  "notes rapportées du devoir B2 : elles montrent tout de suite ce qui "
                  "manque et ce qui prend trop de place.")

    d.objectifs([
        "préparer une feuille d'appel à trois colonnes ;",
        "noter des mots et des chiffres plutôt que des phrases ;",
        "employer huit abréviations courantes ;",
        "vérifier en répétant à voix haute.",
    ])

    d.declencheur(
        'Expérience', "Écoutez et notez. Vous avez une seule écoute.",
        pistes=[
            "« C'est un 4 ½ à 1 050 $, non chauffé, libre le 1er juillet. »",
            "« Le poêle et le frigo sont fournis, pas la laveuse. »",
            "« Une case de stationnement incluse, et une buanderie au sous-sol. »",
            "Comparez vos notes avec votre voisin.",
        ],
        notes="Lire les trois phrases d'affilée, à vitesse normale, une seule fois. "
              "Personne n'aura tout. C'est le but : l'écart entre ce qu'on entend et ce "
              "qu'on retient justifie toute la séance.")

    d.tableau('La feuille d\'appel', "Trois colonnes, préparées avant d'appeler",
              ['Ce que je demande', 'Ce qu\'on me répond'],
              [["Chauffage et électricité inclus ?", "non — élec., ±100 $/mois hiver"],
               ["Électroménagers fournis ?", "poêle + frigo oui / laveuse non"],
               ["Buanderie ?", "s/s, 2 $ la brassée"],
               ["Stationnement ?", "1 case incl."],
               ["Date d'occupation ?", "1er juill."],
               ["Insonorisé ?", "à vérifier à la visite"],
               ["Loyer de l'ancien locataire ?", "à demander jeudi"]],
              cle=0,
              note="Une troisième colonne, à droite : ce qui reste à vérifier pendant la visite.",
              notes="Diapositive à photographier. Distribuer la feuille vierge à trois "
                    "colonnes après l'avoir montrée. Les élèves ont déjà écrit les "
                    "questions au devoir B1 : ils n'ont qu'à les recopier.")

    d.regle("Des mots, pas des phrases",
            "« chauff. non incl. — ±100 $/mois hiver » vaut mieux qu'une phrase complète.",
            precision="Le nom, le chiffre, l'unité. Votre mémoire remettra les mots de "
                      "liaison une heure plus tard ; elle ne remettra pas les chiffres. "
                      "Notez tout montant, toute date et toute heure au moment exact où "
                      "vous les entendez.",
            notes="Diapositive à photographier. Montrer les deux versions au tableau, "
                  "l'une sous l'autre, et faire mesurer le temps d'écriture de chacune.")

    d.cartes("Huit abréviations", "Elles suffisent pour un appel de logement", [
        ("incl. · non incl.", "inclus · non inclus"),
        ("ch. · stat. · élec.", "chambre · stationnement · électricité"),
        ("rdv · ±", "rendez-vous · à peu près"),
        ("/mois · s/s", "par mois · sous-sol"),
    ], notes="Inviter chacun à inventer les siennes, à une condition : toujours les mêmes. "
             "Une abréviation qu'on ne relit pas ne sert à rien.")

    d.pratique('Décodage', "Que veut dire cette note ?",
               "Écrivez la phrase complète.", [
        ("chauff. non incl.", "le chauffage n'est pas inclus"),
        ("2 ch.", "deux chambres"),
        ("stat. incl.", "le stationnement est inclus"),
        ("±100 $/mois", "à peu près cent dollars par mois"),
        ("rdv jeu. 18 h", "rendez-vous jeudi à dix-huit heures"),
        ("élec. à ma charge", "l'électricité est payée par le locataire"),
    ], corrige=True,
       notes="Exercice court. Il sert surtout à vérifier que tout le monde lit les mêmes "
             "abréviations de la même façon.")

    d.regle("Répétez à voix haute avant de raccrocher",
            "« Jeudi dix-huit heures, quatre cent douze Bowen, appartement trois. C'est noté. »",
            precision="Cette phrase vérifie et donne du temps en même temps : vous écrivez "
                      "pendant que vous parlez. Si vous avez mal entendu, on vous corrige "
                      "tout de suite. Personne ne trouve ça impoli — au contraire.",
            notes="Diapositive à photographier. Faire répéter la formule en chœur, puis "
                  "deux par deux avec des adresses inventées.")

    d.pratique('Écoute', "Remplissez la fiche d'appel",
               "Écoutez le dialogue du module, puis complétez.", [
        ("Adresse", "412, rue Bowen, appartement 3"),
        ("Loyer", "1 050 $ par mois"),
        ("Date d'occupation", "le 1er juillet"),
        ("Chauffage", "électrique, non inclus, ±100 $/mois l'hiver"),
        ("Électroménagers fournis", "le poêle et le réfrigérateur"),
        ("Buanderie", "au sous-sol, 2 $ la brassée"),
        ("Stationnement", "une case incluse"),
        ("Visite", "jeudi à 18 h"),
    ], corrige=True,
       notes="Repasser l'audio du dialogue t1 deux fois. La première pour remplir, la "
             "seconde pour vérifier. C'est l'évaluation formative du défi 1.")

    d.piege("Improviser les questions pendant l'appel",
            "Je verrai bien ce que je demande.",
            "Mes huit questions sont écrites devant moi.",
            "En écoutant une langue qu'on apprend, on n'a pas de tête libre pour inventer "
            "une question. Écrire les questions avant, c'est libérer toute son attention "
            "pour écouter la réponse.",
            notes="C'est le message central du défi 1. Le répéter en fin de séance.")

    d.billet(
        "Recopiez au propre vos notes d'appel, en trois colonnes.",
        exemples=[
            "Colonne 3 : ce que vous irez vérifier pendant la visite.",
            "Nous partirons de cette colonne à la séance C1.",
        ],
        notes="Devoir de mise au propre. La troisième colonne fait le pont avec le défi 2 : "
              "les questions de visite sortent des trous laissés par l'appel.")

    return d.save(dossier)
