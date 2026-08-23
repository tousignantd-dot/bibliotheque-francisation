# -*- coding: utf-8 -*-
"""C1 · Deux appels le même soir
Bloc C « Défi 2 · Redire ce qui a été dit » · couleur acier · compréhension
orale · 75 min.
Source : dialogue `t2`, exercice `t2vf` et son bandeau de quatre mots.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C1', section='acier',
        titre="Deux appels le même soir",
        chapeau="Ruslana raconte deux fois la même conversation : à sa "
                "propriétaire, puis à un service de médiation. Ce qui se dit "
                "sur un palier ne vaut que si l'on sait le redire.",
        duree='75 minutes')

    d.titre(notes="Ouverture du défi 2. Rappeler que le défi 1 s'est bien terminé : "
                  "trois engagements et une date. Le travail change de nature, pas de "
                  "dossier.")

    d.objectifs([
        "suivre un compte rendu de conversation au téléphone ;",
        "repérer ce que la propriétaire retient et note ;",
        "comprendre ce qu'un service de médiation fait et ne fait pas ;",
        "employer quatre mots de la preuve et de l'arbitrage.",
    ], notes="Le troisième objectif corrige une idée reçue : la médiation ne dit "
             "jamais qui a raison.")

    d.declencheur(
        'Observation', "Tu racontes une conversation à quelqu'un. Qu'est-ce qui change ?",
        pistes=[
            "Est-ce que tu répètes les mots exacts ?",
            "Qu'est-ce que tu enlèves ? Qu'est-ce que tu ajoutes ?",
            "Est-ce que tu dis ce que tu en as pensé ?",
            "Comment ferais-tu la différence entre les deux ?",
        ],
        notes="Tout le défi est là. Ne rien expliquer : les quatre pistes ouvrent C2 "
              "et C4 sans les nommer.")

    d.dialogue('Dialogue · 1 de 4', "Je vous appelle d'abord pour vous informer", [
        ("GINETTE", "Ginette Ostiguy, bonjour.", True),
        ("RUSLANA", "Bonjour madame Ostiguy, Ruslana Kovalenko, votre locataire du quatre, sur la 8e Avenue.", True),
        ("RUSLANA", "Je vous appelle d'abord pour vous informer, pas pour me plaindre — je voudrais que vous sachiez ce que j'ai fait avant que vous l'appreniez autrement.", True),
        ("GINETTE", "Je vous écoute.", True),
    ], consigne="Écouter d'abord, diapositive masquée.",
       notes="La deuxième réplique de Ruslana explique l'appel entier : il ne sert pas "
             "à obtenir, il sert à dater. Y revenir en C3.")

    d.dialogue('Dialogue · 2 de 4', "Je vous rapporte ce qu'il m'a dit", [
        ("RUSLANA", "Il m'a dit qu'il s'en doutait, parce que sa conjointe le lui avait dit avant moi.", True),
        ("RUSLANA", "Il m'a expliqué qu'il partait à l'atelier à sept heures moins le quart et que c'était le seul moment où il pouvait courir.", True),
        ("GINETTE", "Il a refusé de changer d'heure, autrement dit.", True),
        ("RUSLANA", "Mais il m'a dit aussi qu'il mettrait un tapis de caoutchouc cette semaine, et qu'il allait descendre son vélo à l'épaule.", True),
    ], notes="Quatre formes du discours rapporté en quatre répliques : avait dit, "
             "partait, mettrait, allait descendre. Les faire repérer sans les "
             "expliquer : C2 s'en charge.")

    d.dialogue('Dialogue · 3 de 4', "J'ai des obligations, moi aussi", [
        ("GINETTE", "J'ai eu deux locataires qui se sont fait la guerre pendant un an. Les deux sont partis. J'ai perdu les deux.", True),
        ("RUSLANA", "C'est exactement ce que je veux éviter. C'est pour ça que je vous appelle maintenant et pas dans trois mois.", True),
        ("GINETTE", "Qu'est-ce que vous attendez de moi ?", True),
        ("RUSLANA", "Rien pour l'instant, à part que vous soyez au courant et que la date de cet appel soit notée quelque part.", True),
    ], notes="Faire remarquer la dernière réplique : demander qu'une date soit notée "
             "n'est pas une menace, et c'est pourtant le geste qui compte le plus.")

    d.dialogue('Dialogue · 4 de 4', "Ce que nous ne faisons pas", [
        ("HUBERT", "Service de médiation citoyenne, Hubert Vachon à l'appareil.", True),
        ("HUBERT", "Je vais commencer par vous dire ce que nous ne faisons pas. Nous ne décidons rien, nous ne donnons aucun conseil juridique, et nous ne disons jamais qui a raison.", True),
        ("HUBERT", "C'est gratuit, c'est confidentiel, et c'est volontaire des deux côtés : votre voisin peut refuser, et vous pouvez partir en tout temps.", True),
        ("HUBERT", "Racontez-moi ce qu'il vous a dit, et je vous dirai ce que j'entends.", True),
    ], notes="Trois adjectifs à retenir : gratuit, confidentiel, volontaire. Les faire "
             "écrire : ce sont les trois que les élèves rapporteront chez eux.")

    d.tableau('Analyse', "Ce que la médiation fait, ce qu'elle ne fait pas",
              ['Elle ne fait pas', 'Elle fait'],
              [["Décider qui a raison", "Faire parler les deux personnes"],
               ["Donner un conseil juridique", "Rester neutre au milieu"],
               ["Obliger quelqu'un à venir", "Recevoir ceux qui acceptent"],
               ["Remplacer un tribunal", "Éviter d'y aller"],
               ["Coûter quelque chose", "Écrire l'entente à la fin"]],
              cle=1,
              notes="Diapositive à photographier. Beaucoup d'élèves croient que la "
                    "médiation tranche. Elle ne tranche jamais, et c'est sa force.")

    d.vocabulaire('Vocabulaire', "Quatre mots de la preuve", [
        ("un registre des bruits", "Le carnet où l'on note chaque jour l'heure, la durée et la nature de ce qu'on entend."),
        ("un témoin", "La personne qui a vu ou entendu la même chose que vous et qui peut le confirmer."),
        ("la médiation citoyenne", "Un service gratuit où une personne neutre aide deux voisins à trouver eux-mêmes une entente."),
        ("le règlement municipal", "Les règles écrites par une ville pour son territoire, notamment sur le bruit et les heures."),
    ], notes="« Un témoin » est masculin même pour une femme : la voisine du deux est "
             "un témoin. Le faire remarquer, c'est une question fréquente.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après les deux appels.", [
        ("Ruslana appelle sa propriétaire pour lui demander d'intervenir.", "faux - pour l'informer, et pour dater"),
        ("Elle rapporte que son voisin a refusé de changer d'heure.", "vrai"),
        ("Madame Ostiguy a déjà perdu deux locataires dans une chicane.", "vrai"),
        ("Madame Ostiguy dit que l'affaire ne concerne que les deux locataires.", "faux - elle dit avoir des obligations"),
        ("Le médiateur commence par dire ce que son service ne fait pas.", "vrai"),
        ("La médiation peut être imposée au voisin qui refuse.", "faux - elle est volontaire des deux côtés"),
    ], corrige=True,
       notes="Faire justifier chaque « faux » par la réplique exacte. Le premier est "
             "le plus instructif : un appel peut ne rien demander et tout changer.")

    d.billet(
        "Pourquoi Ruslana appelle-t-elle sa propriétaire si elle ne lui demande rien ?",
        exemples=[
            "Une phrase suffit.",
            "Pense à ce qui commence le jour de l'appel.",
        ],
        notes="Deux minutes. La bonne réponse — pour dater — sera reprise en C3, où le "
              "mot « avisé » commande tout.")

    return d.save(dossier)
