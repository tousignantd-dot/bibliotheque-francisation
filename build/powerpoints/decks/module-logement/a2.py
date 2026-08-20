# -*- coding: utf-8 -*-
"""A2 · Le vocabulaire du logement.
Bloc A · couleur framboise (vocabulaire) · 60 min.
Source : cartes mémoire et savoir sur le « ½ » des annonces.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A2', section='framboise',
        titre='Le vocabulaire du logement',
        chapeau="« 4 ½ chauffé et éclairé, non-fumeur, libre le 1er juillet. » Une "
                "annonce de logement au Québec est écrite en abrégé — et chaque mot y "
                "coûte de l'argent.",
        duree='60 minutes')

    d.titre(notes="Apporter deux ou trois vraies annonces, prises sur un site ou dans un "
                  "journal local. Les élèves les décoderont à la fin de la séance.")

    d.objectifs([
        "comprendre la notation des pièces : 2 ½, 3 ½, 4 ½, 5 ½ ;",
        "décoder les abréviations courantes des annonces ;",
        "nommer les pièces et les services d'un logement ;",
        "calculer le vrai coût d'un loyer ;",
        "distinguer le son « an » du son « on » dans le vocabulaire du logement.",
    ])

    d.tableau('Analyse', "Combien de pièces ?",
              ['La notation', 'Ce que ça veut dire'],
              [["1 ½", "une seule pièce, plus la salle de bain — un studio"],
               ["2 ½", "une chambre et une cuisine, plus la salle de bain"],
               ["3 ½", "une chambre, un salon, une cuisine"],
               ["4 ½", "deux chambres, un salon, une cuisine"],
               ["5 ½", "trois chambres, un salon, une cuisine"]],
              cle=0, props=[0.2, 0.8],
              notes="Faire calculer à l'envers : combien de chambres dans un 6 ½ ? "
                    "Quatre. La règle est mécanique.")

    d.regle('La règle du demi',
            "Le demi, c'est toujours la salle de bain.",
            precision="Elle ne compte que pour une demi-pièce parce qu'on n'y vit pas. "
                      "Un logement avec deux salles de bain reste un « 5 ½ », pas un "
                      "« 6 » : l'annonce précise alors « deux salles de bain ».",
            notes="Faire remarquer l'annonce du 5 ½ en triplex, en A4 : elle précise "
                  "« deux salles de bain » séparément.")

    d.vocabulaire('Vocabulaire · 1 de 2', "Les pièces et les espaces", [
        ("une pièce fermée", "Une pièce avec une porte ou des murs entiers."),
        ("une cuisinette", "Une petite cuisine ouverte sur une autre pièce."),
        ("la buanderie", "Le local où se trouvent la laveuse et la sécheuse."),
        ("un balcon", "Une plateforme extérieure devant une fenêtre ou une porte."),
        ("le rez-de-chaussée", "L'étage au niveau de la rue, sans escalier à monter."),
        ("un triplex", "Un immeuble de trois logements superposés."),
    ], notes="« Triplex » et « rez-de-chaussée » sont propres au parc de logements "
             "québécois. Les faire prononcer.")

    d.tableau('Analyse', "Les abréviations des annonces",
              ["Ce qui est écrit", 'Ce que ça veut dire'],
              [["chauffé et éclairé", "chauffage et électricité compris"],
               ["libre immédiatement", "on peut emménager tout de suite"],
               ["non-fumeur", "il est interdit de fumer dans le logement"],
               ["électros non fournis", "il faut apporter son réfrigérateur et sa cuisinière"],
               ["stat. inclus", "une place de stationnement est comprise"]],
              cle=0, props=[0.35, 0.65],
              notes="Ces cinq formules reviennent dans presque toutes les annonces. Les "
                    "faire chercher dans les vraies annonces apportées en classe.")

    d.regle('Le vrai coût du loyer',
            "Le prix affiché n'est pas ce que vous paierez chaque mois.",
            precision="Un 3 ½ à 780 $ chauffé et éclairé coûte moins qu'un 3 ½ à 720 $ "
                      "sans chauffage : l'électricité d'un logement mal isolé peut "
                      "dépasser cent dollars par mois en hiver. Additionnez toujours "
                      "avant de comparer.",
            notes="Faire le calcul au tableau avec des chiffres réels. C'est un savoir "
                  "financier autant que linguistique.")

    d.cartes('En apprendre plus', "Quatre coûts qu'on oublie", [
        ("L'électricité",
         "Si le logement n'est pas « éclairé », comptez de quarante à cent cinquante "
         "dollars par mois selon la saison et l'isolation."),
        ("L'assurance habitation",
         "Souvent exigée par le bail. Une vingtaine de dollars par mois, et elle "
         "protège vos biens en cas de dégât d'eau ou d'incendie."),
        ("La laveuse à pièces",
         "Une buanderie commune coûte quelques dollars par brassée. Sur un an, c'est "
         "une somme."),
        ("Le déménagement lui-même",
         "Camion, boîtes, aide. Le 1er juillet, tout coûte plus cher : les camions se "
         "réservent des mois d'avance."),
    ], notes="Ces quatre coûts sont invisibles dans une annonce et bien réels dans un "
             "budget. Les donner comme un savoir pratique.")

    d.pratique('Pratique · 1 de 6', "Combien de chambres ?",
               "Le chiffre compte les pièces fermées.", [
        ("un 3 ½", "une chambre"),
        ("un 4 ½", "deux chambres"),
        ("un 5 ½", "trois chambres"),
        ("un 1 ½", "aucune — c'est un studio"),
        ("un 6 ½", "quatre chambres"),
    ], corrige=True,
       notes="Exercice mécanique et rapide. Faire dire la règle à voix haute : le "
             "chiffre moins deux, pour le salon et la cuisine.")

    d.pratique('Pratique · 2 de 6', "Que veut dire l'annonce ?",
               "Traduisez l'abréviation.", [
        ("chauffé et éclairé", "chauffage et électricité compris dans le loyer"),
        ("électros non fournis", "il faut apporter ses gros appareils"),
        ("libre immédiatement", "on peut emménager tout de suite"),
        ("non-fumeur", "interdiction de fumer dans le logement"),
        ("stat. inclus", "une place de stationnement est comprise"),
    ], corrige=True,
       notes="Faire chercher ces formules dans les vraies annonces. Elles y sont presque "
             "toutes.")

    d.piege("Le piège du loyer le moins cher",
            "Ce 3 ½ à 720 $ est le moins cher des trois.",
            "Il n'est pas chauffé : additionnez l'électricité avant de comparer.",
            "Un loyer sans chauffage peut coûter cent dollars de plus par mois en hiver. "
            "Le loyer affiché n'est comparable qu'entre logements qui incluent les mêmes "
            "choses. Faites toujours le total.",
            notes="Faire calculer deux exemples au tableau. L'écart surprend toujours.")

    d.piege("Le piège des électroménagers",
            "Je prends ce 5 ½, il est plus grand pour le même prix.",
            "Les électroménagers ne sont pas fournis : il faut les acheter.",
            "Un réfrigérateur et une cuisinière d'occasion coûtent plusieurs centaines de "
            "dollars, à payer d'un coup au moment du déménagement. C'est une dépense qui "
            "arrive au pire moment.",
            notes="Point pratique important pour des personnes nouvellement arrivées, qui "
                  "n'ont souvent aucun appareil.")

    d.pratique('Pratique · 3 de 6', "Calculez le vrai coût",
               "Additionnez ce qui n'est pas inclus.", [
        ("3 ½ à 780 $, chauffé et éclairé.", "780 $ — tout est inclus"),
        ("3 ½ à 720 $, non chauffé. Électricité : environ 90 $ par mois.", "environ 810 $"),
        ("4 ½ à 890 $, chauffage et eau chaude inclus, électricité à part : 45 $.",
         "environ 935 $"),
        ("5 ½ à 1 250 $, électros non fournis (achat de 800 $ une fois).",
         "1 250 $ par mois, plus 800 $ au départ"),
    ], corrige=True,
       notes="Le deuxième item renverse le classement : le moins cher devient le plus "
             "cher. C'est la leçon de la séance.")

    d.pratique('Pratique · 4 de 6', "Décodez une vraie annonce",
               "Une annonce apportée en classe.", [
        ("Combien de chambres ?", "d'après le chiffre"),
        ("Qu'est-ce qui est inclus ?", "chauffage, électricité, stationnement"),
        ("Qu'est-ce qu'il faut apporter ?", "électroménagers, meubles"),
        ("Quel est le vrai coût mensuel ?", "le loyer plus ce qui n'est pas inclus"),
    ], corrige=False,
       notes="Quinze minutes, en équipes de deux. Chaque équipe présente son annonce "
             "décodée au groupe.")


    d.regle('Deux sons nasaux de la visite',
            "Le son « an » garde les lèvres plates ; le son « on » les arrondit.",
            precision="« Chambre » et « salon » sont deux pièces, deux sons. Pendant "
                      "une visite, se tromper de voyelle nasale change la pièce dont "
                      "on parle — et parfois le montant du loyer.",
            notes="Faire dire les deux mots devant la caméra du téléphone. Les lèvres "
                  "se voient : rondes pour « on », plates pour « an ».")

    d.tableau('Analyse', "Les deux sons dans le vocabulaire du logement",
              ['Le son', "Il s'écrit", 'Mots du module'],
              [["le son « an »", "an, am, en, em", "logement, chambre, buanderie, septembre"],
               ["le son « on »", "on, om", "salon, camion, maison, répondu"]],
              cle=0,
              note="Devant un b ou un p, « on » s'écrit « om » : nombre, compte, pompe. "
                   "Le son ne change pas, seulement la lettre.",
              notes="Faire chercher au groupe un autre mot du module pour chaque case "
                    "avant de montrer la colonne de droite.")

    d.piege('Le piège de « chambre » et « nombre »',
            "nombre, quand on veut dire chambre",
            "chambre — les lèvres restent plates",
            "Les deux mots ne diffèrent que par la voyelle nasale ; tout le reste est "
            "identique. C'est la paire à faire entendre en premier, parce qu'elle isole "
            "exactement la difficulté : si on l'entend ici, on l'entend partout.",
            notes="Dire les deux mots en alternance, cinq allers-retours. Puis demander "
                  "au groupe de les dire à son tour pendant que l'enseignant devine.")

    d.pratique('Pratique · 5 de 6', 'Quel son entendez-vous ?',
               "Écoutez le mot, écrivez « an » ou « on ».", [
        ("logement", "le son « an »"),
        ("salon", "le son « on »"),
        ("chambre", "le son « an »"),
        ("camion", "le son « on »"),
        ("buanderie", "le son « an »"),
        ("maison", "le son « on »"),
        ("septembre", "le son « an »"),
        ("répondu", "le son « on »"),
    ], corrige=True, cols=2,
       notes="Les huit mots de l'exercice de sons du module en ligne, dans le même "
             "ordre. Dire chaque mot deux fois, sans montrer l'orthographe.")

    d.pratique('Pratique · 6 de 6', 'Trois phrases de visite à lire à voix haute',
               "Chacun lit une phrase. Le groupe ne corrige que les sons nasaux.", [
        ("Le logement a une chambre et un grand salon.", "an · an · on"),
        ("La buanderie est au sous-sol de la maison.", "an · on"),
        ("Le bail commence au mois de septembre.", "on · an"),
    ], corrige=True,
       notes="Ces phrases reprennent le vocabulaire de la visite de la rue Galt : "
             "on révise le sens en même temps que le son.")

    d.billet(
        "Décodez une annonce de logement en quatre lignes.",
        exemples=[
            "Le nombre de chambres, ce qui est inclus, ce qu'il faut apporter, le vrai "
            "coût.",
            "Une vraie annonce, trouvée où vous voulez.",
        ],
        notes="Ce billet est un exercice utile hors de la classe. Suggérer de le refaire "
              "chaque fois qu'on cherche un logement.")

    return d.save(dossier)
