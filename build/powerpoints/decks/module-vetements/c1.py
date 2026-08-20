# -*- coding: utf-8 -*-
"""C1 · Demander un avis.
Bloc C « Défi 2 · Demander un avis et lire l'étiquette » · acier · 75 min.
Source : dialogue `t2`, exercice `t2vf`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C1', section='acier',
        titre='Demander un avis',
        chapeau="« Qu'est-ce que tu en penses ? » Demander un avis est facile ; "
                "en donner un sans blesser demande deux ou trois formules — et "
                "recevoir un avis qui ne fait pas plaisir en demande une autre.",
        duree='75 minutes')

    d.titre(notes="Ouverture du bloc C. Demander qui, dans le groupe, magasine seul et qui "
                  "magasine accompagné. La réponse ouvre la séance.")

    d.objectifs([
        "demander un avis de trois façons ;",
        "donner un avis franc mais poli ;",
        "nuancer un désaccord ;",
        "remercier pour un avis qu'on ne suit pas.",
    ])

    d.declencheur(
        'Mise en situation', "Votre ami essaie un manteau qui ne lui va pas. Que dites-vous ?",
        pistes=[
            "Dites-vous la vérité ?",
            "Comment le dire sans blesser ?",
            "Qu'est-ce qui aide : dire ce qui ne va pas, ou proposer autre chose ?",
            "Et si c'est vous qui recevez l'avis ?",
        ],
        notes="La troisième piste porte toute la séance : un avis utile propose une "
              "solution, il ne se contente pas de juger.")

    d.dialogue('Dialogue · 1 de 3', "La question", [
        ("KOFI", "Diane, tu as une minute ? Qu'est-ce que tu penses de celui-là ?", True),
        ("DIANE", "Franchement ? La couleur te va très bien. Mais il me semble un peu court.", True),
        ("KOFI", "Un peu court ?", False),
        ("DIANE", "Pour attendre l'autobus, oui. Tu vas avoir froid aux jambes.", True),
    ], consigne="Écoutez d'abord, diapo masquée.",
       notes="Diane commence par ce qui est bien. Ce n'est pas de la flatterie : c'est ce "
             "qui rend la suite audible.")

    d.dialogue('Dialogue · 2 de 3', "Le désaccord", [
        ("KOFI", "Je le trouve beau, par exemple.", True),
        ("DIANE", "Il est beau, c'est vrai. Mais est-ce que tu veux un beau manteau ou un manteau chaud ?", True),
        ("KOFI", "Les deux, si possible.", False),
        ("DIANE", "Alors regarde le long, dans la même couleur. Il est là-bas.", True),
    ], notes="« Il est beau, c'est vrai. Mais… » : reconnaître avant de nuancer. C'est la "
             "formule la plus utile de la séance.")

    d.dialogue('Dialogue · 3 de 3', "Merci quand même", [
        ("KOFI", "Tu as raison. Je vais essayer le long.", True),
        ("DIANE", "Et si tu préfères le court, prends-le. C'est toi qui vas le porter.", True),
        ("KOFI", "Merci du conseil. Ça m'aide.", True),
        ("DIANE", "De rien.", False),
    ], notes="La dernière réplique de Diane est importante : un avis se donne, il ne "
             "s'impose pas.")

    d.tableau('Analyse', "Demander, donner, nuancer",
              ["Ce qu'on fait", "Ce qu'on dit"],
              [["Demander", "Qu'est-ce que tu en penses ?"],
               ["Donner", "Je trouve qu'il te va bien."],
               ["Nuancer", "Il est beau, c'est vrai. Mais…"],
               ["Remercier", "Merci du conseil."]],
              cle=2,
              note="Reconnaître d'abord, nuancer ensuite : la phrase passe.",
              notes="Diapo à photographier. Les apostrophes du tableau sont volontairement "
                    "simples : c'est de l'oral.")

    d.regle("Reconnaître avant de nuancer",
            "« Il est beau, c'est vrai. Mais il est court. »",
            precision="Commencer par ce qui est vrai et positif désamorce la critique. La "
                      "personne entend le « mais » sans se fermer. La formule inverse — "
                      "« Il est court, mais il est beau » — laisse l'impression contraire : "
                      "c'est la <b>deuxième</b> moitié qu'on retient.",
            notes="Diapo à photographier. Faire tester l'ordre inverse : le groupe entend "
                  "immédiatement la différence.")

    d.piege("Le compliment automatique",
            "C'est beau ! Ça te va bien ! Prends-le !",
            "La couleur te va bien. La longueur, je suis moins sûre.",
            "Un avis qui approuve tout ne sert à rien, et la personne le sait. Elle vous a "
            "demandé votre avis parce qu'elle hésite : lui dire « c'est parfait » la laisse "
            "exactement où elle était.",
            notes="Dire aussi l'inverse : un avis brutal ne sert pas davantage. Le juste "
                  "milieu est la formule de la diapo précédente.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après le dialogue.", [
        ("Diane trouve la couleur bien choisie.", "vrai"),
        ("Elle trouve le manteau trop long.", "faux — trop court"),
        ("Kofi trouve le manteau beau.", "vrai"),
        ("Diane propose un autre modèle.", "vrai — le long, même couleur"),
        ("Elle insiste pour qu'il prenne le long.", "faux — c'est lui qui décide"),
        ("Kofi remercie Diane.", "vrai"),
    ], corrige=True,
       notes="Faire justifier les deux « faux » par la réplique exacte.")

    d.billet(
        "Écrivez un avis en deux temps sur un vêtement.",
        exemples=[
            "Ce qui est bien, puis ce qui l'est moins.",
            "Terminez par une proposition : « Essaie plutôt… »",
        ],
        notes="Ramasser. Ces avis servent au jeu de rôle de E1.")

    return d.save(dossier)
