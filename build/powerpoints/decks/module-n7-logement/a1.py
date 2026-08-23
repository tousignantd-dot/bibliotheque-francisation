# -*- coding: utf-8 -*-
"""A1 · L'enveloppe dans la porte
Bloc A « Je découvre » · couleur acier · 75 min. Séance d'ouverture.
Source : dialogue `prep`, exercice `prVF` et son bandeau de six mots.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A1', section='acier',
        titre="L'enveloppe dans la porte",
        chapeau="Un papier coincé dans une porte, quatre-vingt-quatre "
                "dollars de plus par mois, et un mois pour répondre. Tout "
                "le module part de là.",
        duree='75 minutes')

    d.titre(notes="Première séance du module. Ouvrir par une question au groupe : "
                  "qui a déjà reçu un papier de son propriétaire sans savoir quoi en "
                  "faire ? Presque tout le monde en a reçu un, et presque personne n'y "
                  "a répondu par écrit. C'est exactement le sujet du bloc.")

    d.objectifs([
        "comprendre ce qu'un avis de modification du bail annonce ;",
        "dire à partir de quand court le délai, et combien de temps il dure ;",
        "savoir ce qui arrive quand on ne répond pas ;",
        "employer six mots du dossier avec leur article.",
    ], notes="Le troisième objectif est le seul qui surprend tout le monde : ici, ne "
             "rien répondre veut dire accepter. Le poser dès la première séance.")

    d.declencheur(
        'Observation', "Ton loyer a-t-il déjà augmenté, et comment l'as-tu appris ?",
        pistes=[
            "Par un papier, par un appel, ou en voyant le montant changer ?",
            "As-tu répondu quelque chose ? Par écrit ou de vive voix ?",
            "Savais-tu que tu pouvais discuter le montant ?",
            "Combien de temps pensais-tu avoir pour répondre ?",
        ],
        notes="Question sans mauvaise réponse. Beaucoup d'élèves croient qu'une hausse "
              "de loyer ne se discute pas. Ne pas corriger tout de suite : le dialogue "
              "va le faire.")

    d.dialogue('Dialogue · 1 de 3', "Quatre-vingt-quatre dollars de plus", [
        ("SOKHNA", "Monsieur Lheureux ! Attendez, s'il vous plaît. J'ai trouvé une enveloppe coincée dans ma porte ce matin.", True),
        ("GÉRALD", "C'est moi qui l'ai mise. Je fais le tour des six logements cette semaine.", True),
        ("SOKHNA", "C'est un avis de renouvellement, si j'ai bien lu. Avec une augmentation de quatre-vingt-quatre dollars.", True),
        ("GÉRALD", "Le loyer passerait de neuf cent quarante à mille vingt-quatre à partir du premier juillet.", True),
    ], consigne="Écouter d'abord, diapositive masquée.",
       notes="Neuf cent quarante, mille vingt-quatre, quatre-vingt-quatre : écrire les "
             "trois nombres au tableau dès maintenant et les y laisser toute la séance. "
             "Ils reviennent dans les quatre blocs.")

    d.dialogue('Dialogue · 2 de 3', "Un mois pour répondre", [
        ("SOKHNA", "Il y a une case « refuser » et une case « accepter », et une histoire de délai.", True),
        ("GÉRALD", "Un mois. Vous avez un mois pour me répondre à partir du jour où vous avez reçu l'avis.", True),
        ("SOKHNA", "Et si je ne réponds rien du tout ?", True),
        ("GÉRALD", "Si vous ne répondez rien, c'est accepté. Le bail se renouvelle au nouveau montant.", True),
    ], notes="Faire répéter la dernière réplique par deux élèves. C'est la règle la "
             "plus importante du module, et celle qui coûte le plus cher à ignorer.")

    d.dialogue('Dialogue · 3 de 3', "Refuser ne veut pas dire partir", [
        ("SOKHNA", "Et si je refuse, vous me mettez dehors ?", True),
        ("GÉRALD", "Non plus. Si vous refusez, c'est à moi d'aller devant le Tribunal administratif du logement pour faire fixer le loyer.", True),
        ("SOKHNA", "Vous m'expliquez ça très calmement, pour quelqu'un qui demande quatre-vingt-quatre dollars de plus.", True),
        ("GÉRALD", "Parce que je préfère m'entendre avec vous que d'aller m'asseoir dans une salle d'audience. Faites-moi une proposition.", True),
    ], notes="La dernière réplique ouvre tout le bloc B. La souligner : le propriétaire "
             "demande lui-même une contre-proposition. Négocier n'est pas se battre.")

    d.tableau('Analyse', "Ce que dit l'avis, et ce que ça veut dire",
              ["La phrase de l'avis", 'Ce que ça veut dire'],
              [["porter le loyer à 1 024 $", "84 $ de plus par mois"],
               ["un mois à compter de la réception", "la date qui compte est celle où tu l'as reçu"],
               ["réputé avoir accepté", "ne rien dire, c'est dire oui"],
               ["s'adresser au Tribunal", "après ton refus, c'est à lui de bouger"],
               ["reconduit aux mêmes conditions", "tu restes à 940 $ un an de plus"]],
              cle=0,
              notes="Diapositive à photographier. C'est le tableau de référence du bloc "
                    "A et il revient en B2, sous forme d'exercice sur le document lui-même.")

    d.regle("Le silence n'est pas neutre",
            "Ne pas répondre à un avis de modification équivaut à l'accepter.",
            precision="Dans la plupart des démarches administratives, ne rien faire "
                      "veut dire refuser. Ici, c'est l'inverse : un mois passe, et la "
                      "hausse est acceptée. Un refus, lui, ne met pas fin au bail et ne "
                      "met personne dehors : il oblige seulement le propriétaire à "
                      "demander lui-même la fixation du loyer.",
            notes="Diapositive à photographier. Faire écrire la date limite de l'exemple "
                  "au tableau : avis reçu le 12 février, réponse au plus tard le 12 mars.")

    d.vocabulaire('Vocabulaire', "Six mots de l'avis reçu", [
        ("un avis de modification", "Le papier par lequel un propriétaire annonce qu'il veut changer le loyer ou une autre condition du bail."),
        ("une hausse de loyer", "L'augmentation du montant payé chaque mois pour habiter un logement."),
        ("un délai de réponse", "Le temps dont une personne dispose pour dire oui ou non avant qu'il soit trop tard."),
        ("la fixation du loyer", "La décision par laquelle un tribunal établit lui-même le montant du loyer."),
        ("une contrepartie", "Ce qu'une personne donne en échange de ce qu'elle obtient dans une entente."),
        ("un compromis", "Une solution où chacune des deux personnes accepte de reculer un peu."),
    ], notes="Faire répéter chaque mot avec son article. « La fixation du loyer » prend "
             "le défini : il n'y en a qu'une par dossier. Le faire remarquer.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après la conversation de Sokhna et de monsieur Lheureux.", [
        ("Sokhna habite le logement depuis sept ans sans un seul retard.", "vrai"),
        ("Le loyer passerait de 940 $ à 1 024 $ le premier juillet.", "vrai"),
        ("Sokhna a deux mois pour répondre à l'avis.", "faux - un mois, à partir de la réception"),
        ("Si elle ne répond rien, le bail est reconduit au nouveau montant.", "vrai"),
        ("Si elle refuse, le propriétaire peut la mettre dehors le premier juillet.", "faux - un refus ne met fin à rien"),
        ("Après un refus, c'est au propriétaire de s'adresser au Tribunal.", "vrai"),
    ], corrige=True,
       notes="Faire justifier chaque « faux » par la réplique exacte. Le cinquième "
             "inquiète toujours quelqu'un dans le groupe : y revenir lentement.")

    d.billet(
        "Quelle date noterais-tu, et où l'écrirais-tu ?",
        exemples=[
            "Une phrase suffit.",
            "Pense à un endroit que tu retrouveras dans trois semaines.",
        ],
        notes="Deux minutes. Les réponses servent en B2 : elles montrent qui a compris "
              "que la date de réception est la seule qu'on puisse prouver.")

    return d.save(dossier)
