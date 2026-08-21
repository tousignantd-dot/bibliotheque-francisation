# -*- coding: utf-8 -*-
"""C3 · « Ne pas tout répéter »
Bloc C « Défi 2 · Le message et le mot » · couleur ambre · 75 min. Grammaire.
Source : exercice `t2pron`, mini-leçon `t2pron`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C3', section='ambre',
        titre="Ne pas tout répéter : le, lui, y, en",
        chapeau="« J'ai appelé madame Faye. J'ai laissé un message à madame "
                "Faye. Je vais rappeler madame Faye. » C'est clair, et ce "
                "n'est plus du français au bout de trois phrases. Le "
                "programme appelle ça la reprise de l'information.",
        duree='75 minutes')

    d.titre(notes="Commencer par écrire les trois phrases du chapeau au tableau et les "
                  "lire à voix haute, très sérieusement. Le groupe rit : c'est le meilleur "
                  "point de départ possible pour cette séance.")

    d.objectifs([
        "remplacer un complément direct par le, la ou les ;",
        "remplacer une personne annoncée par « à » par lui ou leur ;",
        "employer y pour un lieu et en pour une quantité ;",
        "placer le pronom devant le verbe, sauf à l'impératif affirmatif.",
    ], notes="Les quatre objectifs sont un seul apprentissage vu sous quatre angles. Le "
             "test de la préposition, donné plus bas, les réunit.")

    d.regle("Le test de la préposition",
            "Regardez ce qu'il y a devant le complément : c'est lui qui "
            "choisit le pronom.",
            precision="Rien devant : le, la, les. · « à » plus une personne : lui, "
                      "leur. · « à » plus une chose ou un lieu : y. · « de » ou une "
                      "quantité : en.",
            notes="Diapositive à photographier, et le seul contenu vraiment nécessaire de "
                  "la séance. Tout le reste en découle. La faire recopier telle quelle "
                  "dans les cahiers.")

    d.tableau('Quatre exemples', "La phrase longue, et la phrase courte",
              ['On répète', 'On reprend'],
              [["J'écoute le message.", "Je l'écoute."],
               ["Je laisse un message à Ndeye.", "Je lui laisse un message."],
               ["J'écris aux voisins du deuxième.", "Je leur écris."],
               ["Je vais à la fête de la ruelle.", "J'y vais."],
               ["Je fais des empanadas.", "J'en fais."]],
              cle=1,
              notes="Faire couvrir la colonne de droite et la reconstituer oralement, "
                    "ligne par ligne. Puis faire l'inverse : donner la phrase courte et "
                    "faire retrouver ce que le pronom remplace.")

    d.cartes("Deux confusions à régler tout de suite", "Elles reviennent chaque année", [
        ("y ne remplace jamais une personne",
         "Je pense à ma sœur donne « je pense à elle », jamais « j'y pense »."),
        ("leur pronom ne prend jamais de s",
         "Je leur écris. Mais : leurs enfants, avec un s, est un déterminant."),
        ("en garde le nombre",
         "J'ai besoin de deux plaques donne « j'en ai besoin de deux »."),
        ("le devient l' devant une voyelle",
         "J'écoute le message donne « je l'écoute »."),
    ], notes="La deuxième carte est celle qui se voit à l'écrit et qui coûte des points "
             "partout. L'écrire au tableau en deux couleurs si possible : leur / leurs.")

    d.regle("Devant le verbe, toujours",
            "Sauf à l'impératif affirmatif, où le pronom passe derrière avec "
            "un trait d'union.",
            precision="Je lui téléphone. · Je vais lui téléphoner. · "
                      "Téléphone-lui ! · Ne lui téléphone pas.",
            notes="Faire apprendre les deux derniers exemples ensemble : « rappelez-moi » "
                  "et « ne me rappelez pas ». Le pronom saute d'un côté à l'autre du "
                  "verbe, et c'est ce saut qu'il faut sentir.")

    d.pratique('Grammaire', "Remplacez ce qui se répète",
               "Écrivez seulement le pronom.", [
        ("J'écoute le message. Je ___ écoute.", "l'"),
        ("Je laisse un message à madame Faye. Je ___ laisse un message.", "lui"),
        ("J'écris aux voisins du deuxième. Je ___ écris.", "leur"),
        ("Je vais à la fête de la ruelle. J' ___ vais.", "y"),
        ("Elle fait des empanadas. Elle ___ fait.", "en"),
        ("J'arrose les plantes du troisième. Je ___ arrose.", "les"),
        ("Elle pense à son voyage au Sénégal. Elle ___ pense.", "y"),
    ], corrige=True,
       notes="Exercice t2pron de l'activité. Pour chaque item, faire nommer la préposition "
             "avant de donner le pronom : c'est la démarche qu'on veut installer, pas la "
             "réponse.")

    d.piege("Employer « y » pour une personne",
            "Je pense à ma sœur, donc j'y pense.",
            "Je pense à elle.",
            "Pour une personne, on garde la préposition et le pronom fort. « Y » ne "
            "remplace jamais quelqu'un.",
            notes="Donner le contre-exemple qui trompe : « je pense à mon voyage, j'y "
                  "pense ». La même préposition, deux pronoms différents, selon que c'est "
                  "une chose ou une personne.")

    d.billet(
        "Écrivez trois phrases de votre semaine, puis récrivez-les avec un pronom.",
        exemples=[
            "Une avec le, la ou les. Une avec lui ou leur. Une avec y ou en.",
            "Six lignes en tout : la phrase longue, puis la phrase courte.",
        ],
        notes="Ramasser. Les erreurs de « leur / leurs » se comptent facilement et disent "
              "s'il faut y revenir en C4.")

    return d.save(dossier)
