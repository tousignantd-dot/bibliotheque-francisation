# -*- coding: utf-8 -*-
"""D2 · Ce carton-là, cet avis, cette boîte.
Bloc D « Défi 3 · Le carton dans la boîte aux lettres » · couleur ambre · 75 min.
Source : mini-leçons `t3dem` et `t3suivre`, exercices `t3dem`, `t3suivre`, `t3services`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='D2', section='ambre',
        titre='Ce carton-là, cet avis, cette boîte',
        chapeau="Quand on montre une chose qu'on a dans la main, on a besoin "
                "d'un petit mot devant. Quatre formes, et un « -là » qui "
                "s'ajoute partout au Québec.",
        duree='75 minutes')

    d.titre(notes="Séance de grammaire et d'écriture, doublée d'une séance de services. "
                  "La première heure : les démonstratifs. La seconde : le déménagement "
                  "et les phrases pour demander un service.")

    d.objectifs([
        "employer « ce », « cet », « cette » et « ces » ;",
        "ajouter « -là » pour montrer un objet ;",
        "savoir ce qui suit et ce qui ne suit pas lors d'un déménagement ;",
        "demander cinq services différents au comptoir.",
    ])

    d.tableau('Analyse', "Quatre formes, une seule idée : je montre",
              ['La forme', 'Devant quoi', 'Exemples'],
              [["ce", "un mot masculin", "ce carton, ce colis, ce reçu"],
               ["cet", "un mot masculin qui commence par une voyelle", "cet avis, cet envoi"],
               ["cette", "un mot féminin", "cette boîte, cette enveloppe, cette lettre"],
               ["ces", "un pluriel, masculin ou féminin", "ces timbres, ces enveloppes"]],
              cle=0,
              note="« Cet » existe parce que « ce avis » est trop dur à prononcer : deux voyelles collées.",
              notes="Diapo à photographier. Faire chercher au groupe cinq autres mots du "
                    "module pour chaque ligne. Les mots du bureau de poste sont presque "
                    "tous dans la liste.")

    d.regle("Le « -là » du Québec",
            "ce carton-là  ·  cette boîte-là",
            precision="Au comptoir, on ajoute très souvent « -là » pour bien "
                      "montrer l'objet qu'on tient. Avec un trait d'union. Ce "
                      "n'est pas obligatoire, mais c'est ce que vous entendrez, "
                      "et ça rend la phrase plus claire quand on montre du doigt.",
            notes="Diapo à photographier. Faire dire la phrase avec le geste : « ce "
                  "carton-là » en tendant un papier. Le mot et le geste vont ensemble.")

    d.pratique('Écriture', "Complétez avec « ce », « cet », « cette » ou « ces »",
               "Regardez le mot qui suit.", [
        ("J'ai trouvé ___ carton-là dans ma boîte aux lettres.", "ce"),
        ("___ avis dit que mon colis est arrivé.", "Cet — avis commence par une voyelle"),
        ("___ boîte-là est trop grosse pour la boîte rouge.", "Cette"),
        ("Est-ce que ___ timbres sont encore bons ?", "ces"),
        ("Je voudrais envoyer ___ colis-là par Xpresspost.", "ce"),
        ("Combien coûtent ___ enveloppes-là ?", "ces"),
    ], corrige=True,
       notes="C'est l'exercice `t3dem` du module. La deuxième ligne est la seule "
             "difficile : « cet avis », jamais « ce avis ». La faire répéter à voix "
             "haute, l'oreille tranche mieux que la règle.")

    d.piege(
        "Devant une voyelle",
        "ce avis, ce envoi",
        "cet avis, cet envoi",
        "Deux voyelles collées ne se prononcent pas : le français ajoute un t pour "
        "les séparer. C'est le même réflexe que « mon amie » plutôt que « ma amie ». "
        "Il n'y a rien à comprendre, seulement à entendre.",
        notes="Faire dire « ce avis » à voix haute au groupe : personne n'y arrive "
              "proprement. C'est la meilleure explication de la règle.")

    d.regle("Quand on déménage",
            "les lettres suivent, les colis ne suivent pas",
            precision="Le service de réacheminement fait suivre votre courrier à la "
                      "nouvelle adresse, jusqu'à douze mois. Il porte sur les "
                      "lettres, le courrier recommandé et les magazines. Les colis "
                      "et les grosses enveloppes prépayées, eux, restent à "
                      "l'ancienne adresse.",
            notes="Diapo à photographier. Cette information sauve des colis chaque "
                  "année. Ajouter la consigne pratique : prévenir soi-même les "
                  "boutiques en ligne de son nouveau domicile.")

    d.pratique('Compréhension', "Est-ce que ça suit ?",
               "Vous déménagez. Qu'est-ce qui arrive à la nouvelle adresse ?", [
        ("Une lettre de votre banque", "ça suit"),
        ("Un colis commandé sur Internet", "ça ne suit pas"),
        ("Un envoi en courrier recommandé", "ça suit"),
        ("Le magazine auquel vous êtes abonné", "ça suit"),
        ("Une grosse enveloppe prépayée", "ça ne suit pas"),
        ("Une carte d'anniversaire de votre famille", "ça suit"),
    ], corrige=True, cols=2,
       notes="C'est l'exercice `t3suivre` du module. La règle tient en une phrase : ce "
             "qui entre dans une boîte aux lettres suit, le reste non.")

    d.pratique('À l\'oral', "Un service, une phrase",
               "Quelle phrase dit-on au comptoir ?", [
        ("Vous avez trouvé un carton dans votre boîte aux lettres.", "Je viens chercher un colis. Voici mon avis."),
        ("Vous envoyez un papier important et vous voulez une preuve.", "Je voudrais l'envoyer par courrier recommandé."),
        ("Vous devez envoyer deux cents dollars à quelqu'un.", "J'aimerais acheter un mandat-poste, s'il vous plaît."),
        ("Vous déménagez le mois prochain.", "Est-ce que je pourrais faire suivre mon courrier ?"),
        ("Vous ne comprenez pas ce qu'on vient de vous dire.", "Est-ce que vous pouvez répéter, s'il vous plaît ?"),
        ("Vous voulez garder la preuve de ce que vous avez payé.", "Donnez-moi le reçu, s'il vous plaît."),
    ], corrige=True,
       notes="C'est l'exercice `t3services` du module. Il réunit les quatre formules de "
             "la séance A4 et les services de la séance B3 : c'est la dernière "
             "répétition générale avant le jeu de rôle de E1.")

    d.billet(
        "Écrivez la phrase que vous direz pour faire suivre votre courrier.",
        exemples=[
            "Employez « est-ce que je pourrais ».",
            "Ajoutez la date de votre déménagement.",
        ],
        notes="Deux minutes. Vérifier la formule polie et l'ordre des mots. C'est la "
              "dernière trace écrite avant l'évaluation formative de E1.")

    return d.save(dossier)
