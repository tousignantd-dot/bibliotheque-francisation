# -*- coding: utf-8 -*-
"""A4 · La langue de l'administration.
Bloc A « Je découvre » · couleur ambre · 75 min. Registres.
Source : exercice `prReg` et sa mini-leçon.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A4', section='ambre',
        titre="La langue de l'administration",
        chapeau="« Les vidanges » et « les matières résiduelles » désignent "
                "la même chose. Un seul des deux se trouve dans un "
                "règlement — et c'est celui-là qui décide de ce que le "
                "camion ramasse.",
        duree='75 minutes')

    d.titre(notes="Dernière séance du bloc A. Ramasser le devoir A3 et en lire trois "
                  "phrases à voix haute, sans nommer les auteurs. Elles servent "
                  "d'échauffement et montrent où en est le vocabulaire.")

    d.objectifs([
        "reconnaître les mots officiels des services publics ;",
        "passer du mot courant au mot officiel et retour ;",
        "savoir que reconnaître ne veut pas dire imiter ;",
        "employer le bon registre selon qu'on écrit ou qu'on parle.",
    ])

    d.declencheur(
        'Discussion', "Pourquoi un règlement n'écrit-il pas « les vidanges » ?",
        pistes=[
            "Est-ce pour faire savant ?",
            "Est-ce pour être poli ?",
            "Que se passe-t-il si deux mots ne veulent pas dire exactement la même chose ?",
            "Est-ce que vous devez parler comme ça, vous ?",
        ],
        notes="La dernière question est celle qui compte. Beaucoup d'élèves croient qu'on "
              "leur demande d'adopter ce registre. Dire tout de suite que non : il s'agit "
              "de le comprendre, et de l'employer seulement quand on s'adresse au service.")

    d.regle("Le mot officiel est un mot précis, pas un mot chic",
            "Il a une valeur légale : c'est lui qui est écrit dans le règlement.",
            precision="« Une demande » peut rester sans trace ; « une requête » porte un "
                      "numéro. Ce n'est pas la même chose, et c'est pour cela que les "
                      "deux mots existent. Employer le mot du service, c'est parler de la "
                      "même chose que lui.",
            notes="Diapositive à photographier. C'est la clé de toute la séance : la "
                  "précision, jamais l'élégance.")

    d.tableau('Les mots · 1 de 2', "La démarche elle-même",
              ['Au quotidien', 'Au service'],
              [["une demande", "une requête"],
               ["le temps que ça prend", "le délai"],
               ["les jours de semaine", "les jours ouvrables"]],
              cle=1,
              note="On dit la gauche à son voisin, la droite au service.",
              notes="Diapositive à photographier. Les trois mots du téléphone : ce sont "
                    "ceux du défi 1, et « requête » est le plus important des trois.")

    d.tableau('Les mots · 2 de 2', "Les choses et les gens",
              ['Au quotidien', 'Au service'],
              [["les vidanges", "les matières résiduelles"],
               ["la personne au comptoir", "le préposé"],
               ["les prix d'astheure", "les tarifs en vigueur"]],
              cle=1,
              note="La colonne de gauche n'est pas fautive : elle est d'un autre usage.",
              notes="Diapositive à photographier. Insister sur la note : plusieurs élèves "
                    "croient qu'on leur reproche leur façon de parler.")

    d.cartes("Quatre formules d'ouverture", "Répondre dans le même registre", [
        ("On vous dit",
         "« Comment puis-je vous aider ? » — poli, neutre, professionnel."),
        ("Vous répondez",
         "« Bonjour, je vous appelle parce que… » — et non « ouais, c'est parce que… »"),
        ("À l'écrit, on commence par",
         "« Bonjour, » et on emploie « vous » du début à la fin."),
        ("On ne dit jamais",
         "« Je sollicite votre bienveillante attention. » Trop, c'est aussi une erreur."),
    ], notes="La dernière carte surprend et fait rire, ce qui la rend mémorable. Beaucoup "
             "d'élèves pensent que plus c'est compliqué, mieux c'est.")

    d.piege("Croire qu'il faut parler comme un règlement",
            "Je sollicite l'ouverture d'une requête auprès de vos services.",
            "Bonjour, je voudrais ouvrir une requête, s'il vous plaît.",
            "Un service public parle un français clair et courant. Le registre soutenu "
            "n'ajoute rien et rend la demande moins facile à traiter. Ce qu'il faut, "
            "c'est le mot juste dans une phrase simple.",
            notes="Nommer l'inquiétude : plusieurs élèves n'osent pas téléphoner de peur "
                  "de « mal parler ». Or l'obstacle réel est le vocabulaire, pas le style.")

    d.pratique('Registre', "Dites-le au service",
               "Reformulez chaque phrase comme vous la diriez à un préposé.", [
        ("Ça fait deux semaines que mes vidanges sont pas ramassées.",
         "Mon bac n'a pas été ramassé depuis deux semaines."),
        ("Ça prend combien de temps, votre affaire ?",
         "Quel est le délai de traitement, s'il vous plaît ?"),
        ("Je veux que vous notiez ma demande quelque part.",
         "Est-ce que vous pouvez ouvrir une requête ?"),
        ("C'est-tu les prix d'astheure ou les vieux ?",
         "Est-ce que ce sont les tarifs en vigueur ?"),
        ("Je vais passer un de ces jours.",
         "Je me présenterai au comptoir cette semaine."),
        ("Faut-tu que j'apporte des papiers ?",
         "Est-ce qu'il faut apporter des pièces justificatives ?"),
    ], corrige=True,
       notes="Accepter toute reformulation claire et polie. L'important est le mot juste "
             "et le « vous », pas la tournure exacte.")


    d.tableau('Ce qui change entre parler et écrire', "Deux registres, une même démarche",
              ['Au téléphone', 'Dans un courriel'],
              [["« Bonjour, je vous appelle parce que… »", "« Bonjour, Je vous écris au sujet de… »"],
               ["on peut hésiter, reprendre", "on relit avant d'envoyer"],
               ["on fait répéter", "on cite le numéro de requête"],
               ["on remercie et on raccroche", "on termine par une formule de salutation"]],
              cle=0,
              note="La même personne, la même demande — deux façons de la porter.",
              notes="Ce tableau annonce le bloc E : l'appel en E1, le courriel en E2. "
                    "Le dire au groupe pour qu'il voie où va le module.")

    d.billet(
        "Relevez trois mots officiels dans un papier reçu chez vous.",
        exemples=[
            "Un avis, une facture, une lettre d'un ministère, un courriel d'école.",
            "Pour chacun, écrivez comment vous diriez la même chose à un ami.",
        ],
        notes="Devoir de repérage. Il transforme le courrier que les élèves reçoivent "
              "déjà en matériel de cours, et prépare le défi 2.")

    return d.save(dossier)
