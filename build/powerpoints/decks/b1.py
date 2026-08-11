# -*- coding: utf-8 -*-
"""B1 · Oksana appelle madame Rioux.
Bloc B · couleur acier (compréhension orale) · 75 min.
Source : dialogue `t1`, exercices `t1vf` et `t1sens`.
"""
from theme import Deck

IMG = '/Users/danieltousignant/Claude/bibliotheque-francisation/assets/interactive/module-probleme/images/'


def build(dossier):
    d = Deck(
        code='B1', section='acier',
        titre='Oksana appelle madame Rioux',
        chapeau="Deux problèmes en un seul appel : le calorifère du salon qui ne chauffe "
                "plus, et une tache brune qui grossit au plafond de la chambre. "
                "L'appel dure trois minutes et règle les deux.",
        duree='75 minutes')

    d.titre(notes="Ouverture du bloc B. C'est le dialogue le plus important du module : "
                  "tout le bloc s'appuie dessus. Prévoir deux écoutes complètes.")

    d.objectifs([
        "comprendre un appel téléphonique entre une locataire et sa propriétaire ;",
        "reconnaître les cinq moments d'un appel réussi ;",
        "comprendre les expressions du dialogue : constater l'ampleur, tenir au courant, à ma charge ;",
        "savoir demander une solution temporaire en attendant la réparation.",
    ])

    d.declencheur('Avant d\'écouter', "Que va-t-elle dire en premier ?",
                  image=IMG + 'plafond.jpg',
                  pistes=[
                      "Oksana a deux problèmes. Par lequel commence-t-elle ?",
                      "Comment se présente-t-on au téléphone à sa propriétaire ?",
                      "Que faut-il dire tout de suite : le problème, ou depuis quand ?",
                      "Écoutez, et vérifiez vos réponses.",
                  ],
                  notes="Faire écouter l'audio du module (Tâche 1) sans afficher le texte. "
                        "Poser les quatre questions AVANT l'écoute et y revenir après.")

    d.dialogue('Dialogue · 1 de 4', "Se présenter et nommer le problème", [
        ("OKSANA", "Bonjour madame Rioux, c'est Oksana Kravets, au 4B. Je vous appelle parce que le calorifère du salon ne chauffe plus depuis avant-hier.", True),
        ("MME RIOUX", "Depuis avant-hier ? Il fallait me prévenir tout de suite, voyons. Il fait combien chez vous ce matin ?", False),
        ("OKSANA", "Quatorze degrés. J'ai vérifié le panneau électrique : le disjoncteur retombe chaque fois que je le remonte.", True),
    ], consigne="Écoutez d'abord, diapo masquée. Repérez ensuite ce qu'Oksana dit dans sa première phrase.",
       notes="Faire compter les informations de la première réplique : le nom, le logement, "
             "le problème, depuis quand. Quatre informations en une phrase. C'est le modèle "
             "à reproduire.")

    d.dialogue('Dialogue · 2 de 4', "La propriétaire organise la réparation", [
        ("MME RIOUX", "Ne le remontez plus, c'est dangereux. Je vais faire venir mon électricien. Il passe déjà chez les locataires du deuxième jeudi matin ; je vais lui demander de monter chez vous après avoir terminé leur installation.", True),
        ("OKSANA", "Jeudi, c'est dans trois jours. Est-ce que je peux avoir un chauffage d'appoint en attendant ?", True),
        ("MME RIOUX", "Bien sûr. J'en garde deux au sous-sol, dans le local d'entretien. Passez en chercher un ce soir, le concierge vous ouvrira.", False),
    ], notes="Deux structures à signaler ici, sans les enseigner encore : « faire venir » "
             "(séance C3) et « après avoir terminé » (séance C2). Dire au groupe qu'on y "
             "reviendra. La demande d'Oksana est le point à retenir : on a le droit de "
             "demander une solution temporaire.")

    d.dialogue('Dialogue · 3 de 4', "Le deuxième problème", [
        ("OKSANA", "Merci beaucoup. Il y a autre chose, aussi. Il y a une tache brune au plafond de la chambre, et elle grossit.", True),
        ("MME RIOUX", "Une tache brune ? Ça fait combien de temps qu'elle est là ?", False),
        ("OKSANA", "Ça fait deux semaines. Au début, elle était grande comme une pièce de deux dollars ; maintenant, elle fait la taille d'une assiette.", True),
    ], notes="« Il y a autre chose, aussi » — la formule qui permet d'enchaîner un deuxième "
             "problème sans rappeler une autre fois. La faire répéter. La comparaison "
             "d'Oksana (pièce de deux dollars → assiette) vaut mieux que n'importe quel "
             "adjectif : c'est du concret.")

    d.dialogue('Dialogue · 4 de 4', "Qui paie ?", [
        ("MME RIOUX", "Vous êtes au dernier étage… ça vient probablement de la toiture. Envoyez-moi une photo par courriel : ça me permettra de constater l'ampleur du dégât avant de faire venir le couvreur.", False),
        ("OKSANA", "Je vous l'envoie ce midi. Est-ce que ces réparations-là sont à ma charge ?", True),
        ("MME RIOUX", "Pas du tout. Vous payez le loyer ; l'entretien de l'immeuble, c'est ma part du contrat. Vous, tenez-moi seulement au courant si la tache change encore.", True),
    ], notes="La question d'Oksana est légitime et courante. La réponse est la règle "
             "générale : l'entretien est à la charge de la personne propriétaire. Y revenir "
             "à la séance B4.")

    d.cartes('Analyse', "Les cinq moments de l'appel", [
        ("1 · Je me présente",
         "Mon nom et mon numéro de logement, tout de suite. « C'est Oksana Kravets, au 4B. » "
         "La propriétaire a plusieurs locataires : elle doit savoir qui appelle."),
        ("2 · Je nomme le problème et sa durée",
         "L'appareil, la pièce, depuis quand. « Le calorifère du salon ne chauffe plus "
         "depuis avant-hier. »"),
        ("3 · Je donne un chiffre",
         "« Quatorze degrés. » « Deux semaines. » Un chiffre dit l'urgence sans avoir à "
         "insister."),
        ("4 · Je dis ce que j'ai déjà vérifié",
         "« J'ai vérifié le panneau électrique. » Ça évite qu'on vous fasse refaire ce que "
         "vous avez déjà fait, et ça montre le sérieux de l'appel."),
    ], notes="Faire noter ces cinq moments. Le cinquième est sur la diapo suivante.")

    d.regle('Le cinquième moment',
            "Je demande une solution temporaire en attendant la réparation.",
            precision="« Est-ce que je peux avoir un chauffage d'appoint en attendant ? » "
                      "C'est la question qu'on oublie presque toujours de poser. La "
                      "réparation prendra le temps qu'elle prendra ; entre-temps, vous avez "
                      "le droit de demander de quoi vivre normalement dans votre logement.",
            notes="Le point le plus utile de la séance dans la vie réelle. Faire trouver "
                  "d'autres exemples : une plaque chauffante si la cuisinière est morte, "
                  "une clé de dépannage, l'accès à une autre buanderie.")

    d.pratique('Pratique', 'Vrai ou faux',
               "Écoutez de nouveau le dialogue, puis répondez.", [
        ("Madame Rioux trouve qu'Oksana a attendu trop longtemps avant de l'appeler.", "VRAI"),
        ("La propriétaire conseille de remonter le disjoncteur encore une fois.", "FAUX — c'est dangereux"),
        ("L'électricien doit passer chez d'autres locataires le même jour.", "VRAI — au deuxième"),
        ("Oksana devra attendre une semaine avant la visite de l'électricien.", "FAUX — trois jours"),
    ], corrige=True)

    d.pratique('Pratique', 'Suite',
               "Même consigne.", [
        ("La propriétaire prête un chauffage d'appoint.", "VRAI"),
        ("La tache du plafond est apparue hier.", "FAUX — ça fait deux semaines"),
        ("La propriétaire demande une photo avant de faire venir le couvreur.", "VRAI"),
        ("Oksana devra payer les réparations.", "FAUX — l'entretien est à la charge de la propriétaire"),
    ], corrige=True,
       notes="Si le groupe hésite sur la dernière, revenir au dialogue 4 et faire relire "
             "la réponse de madame Rioux mot à mot.")

    d.vocabulaire('Vocabulaire', "Les expressions du dialogue", [
        ("constater l'ampleur du dégât", "Voir de ses yeux jusqu'où va le problème."),
        ("me prévenir", "M'avertir à l'avance."),
        ("tenir au courant", "Donner des nouvelles au fur et à mesure."),
        ("à ma charge", "Payé par moi."),
        ("un chauffage d'appoint", "Un appareil ajouté pour dépanner."),
    ], notes="Faire réemployer chaque expression dans une phrase nouvelle avant de passer "
             "à la suivante. « Tenir au courant » et « à ma charge » sont les deux plus "
             "utiles au téléphone.")

    d.piege('Au téléphone',
            "Bonjour, c'est moi, j'ai un problème de chauffage.",
            "Bonjour madame Rioux, c'est Oksana Kravets, au 4B.",
            "Se présenter par son nom et son numéro de logement prend deux secondes et évite "
            "trente secondes de confusion. Une propriétaire qui gère six logements ne "
            "reconnaît pas une voix au téléphone — et « j'ai un problème de chauffage » ne "
            "lui dit pas dans quel appartement.",
            notes="Faire pratiquer la première phrase à deux, en binômes, trois fois de "
                  "suite. C'est mécanique, et c'est exactement ce qui bloque au moment de "
                  "téléphoner pour vrai.")

    d.billet(
        "Écrivez la première phrase de votre appel à votre propriétaire.",
        exemples=[
            "Quatre informations : votre nom · votre logement · le problème · depuis quand.",
            "Exemple : « Bonjour, c'est Ana Lopes, au 2C. Le robinet de la cuisine coule depuis trois jours. »",
        ],
        notes="Ces billets serviront de point de départ au jeu de rôle de la séance E1. "
              "Les conserver.")

    return d.save(dossier)
