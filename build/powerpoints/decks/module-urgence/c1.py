# -*- coding: utf-8 -*-
"""C1 · Les soins et le suivi.
Bloc C · couleur acier (compréhension orale) · 60 min.
Source : dialogue `t2` et exercice `t2vf`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C1', section='acier',
        titre='Les soins et le suivi',
        chapeau="Le diagnostic tient en une phrase, mais ce qui suit tient en cinq : la "
                "cicatrice, le congé, la crème, le pansement, et le signal qui dit de "
                "revenir.",
        duree='60 minutes')

    d.titre(notes="Ouverture du défi 2. Rappeler où on en est : Fatou est à l'urgence, la "
                  "plaie est nettoyée, le pansement est posé. Le médecin va maintenant "
                  "expliquer la suite.")

    d.objectifs([
        "comprendre un diagnostic et le degré d'une brûlure ;",
        "retenir des consignes de soins données à l'oral ;",
        "savoir quand il faut retourner voir un médecin ;",
        "poser les questions qui manquent.",
    ])

    d.dialogue('Dialogue · 1 de 3', "Ce n'est pas dangereux", [
        ("L'URGENTOLOGUE", "C'est une brûlure du deuxième degré, superficielle. Ce n'est "
                           "pas dangereux.", True),
        ("FATOU", "Est-ce que je vais garder une cicatrice ?", True),
        ("L'URGENTOLOGUE", "Probablement pas, si vous protégez la peau du soleil pendant "
                           "six mois.", True),
    ], consigne="Écoutez d'abord l'enregistrement, diapo masquée. Lisez ensuite.",
       notes="Passer l'audio du défi 2. Faire remarquer le « si » dans la réponse du "
             "médecin : la promesse est conditionnelle, et la condition dure six mois.")

    d.dialogue('Dialogue · 2 de 3', "Est-ce que je peux retourner en cuisine ?", [
        ("FATOU", "Est-ce que je peux retourner en cuisine demain ?", True),
        ("L'URGENTOLOGUE", "Non. Je vous donne un congé de maladie de trois jours et une "
                           "crème à appliquer deux fois par jour.", True),
    ], notes="Deux informations dans une seule réplique : la durée du congé et la "
             "fréquence de la crème. Faire relever les deux chiffres.")

    d.dialogue('Dialogue · 3 de 3', "Si la douleur augmente, revenez", [
        ("FATOU", "Et le pansement, je le change moi-même ?", True),
        ("L'URGENTOLOGUE", "Vous le changez chaque matin. Si la douleur augmente ou si la "
                           "plaie devient jaune, revenez nous voir.", True),
    ], notes="La dernière phrase est la plus importante de tout le défi : ce sont les "
             "deux signes d'infection. Les écrire au tableau.")

    d.tableau('Analyse', "Les cinq informations du médecin",
              ['Le sujet', 'Ce qu\'il dit'],
              [["le diagnostic", "deuxième degré, superficielle, pas dangereux"],
               ["la cicatrice", "probablement pas, si on protège du soleil six mois"],
               ["le travail", "trois jours de congé de maladie"],
               ["la crème", "deux fois par jour"],
               ["le pansement", "changé chaque matin"]],
              cle=0,
              note="Cinq informations, sept répliques. Un patient qui n'en retient que "
                   "trois sort avec la moitié de son traitement.",
              notes="Faire noter les cinq dans le cahier avant de faire l'exercice. "
                    "L'écriture pendant l'écoute est une compétence à installer.")

    d.regle('Les deux signaux qui font revenir',
            "La douleur augmente, ou la plaie devient jaune.",
            precision="Ce sont les signes d'une infection. Une brûlure qui va bien fait "
                      "de moins en moins mal, jour après jour. Si la douleur monte "
                      "après deux jours, quelque chose ne va pas.",
            notes="Diapo à laisser affichée longtemps. C'est le savoir de sécurité de "
                  "la séance, et il vaut pour toute plaie, pas seulement les brûlures.")

    d.cartes('Ouvrir la mini-leçon', "Quatre choses sur le congé de maladie", [
        ("C'est un papier officiel",
         "Il porte le nom du médecin, la date et le nombre de jours. Gardez-en une "
         "copie ou une photo avant de le remettre à l'employeur."),
        ("Il ne dit pas pourquoi",
         "L'employeur a le droit de savoir combien de jours, pas de savoir de quoi vous "
         "souffrez. Votre diagnostic reste privé."),
        ("Un accident de travail est différent",
         "Une blessure survenue au travail relève de la CNESST. Le formulaire n'est pas "
         "le même, et il faut déclarer l'accident à l'employeur le jour même."),
        ("Prévenir tout de suite",
         "Téléphonez à votre employeur dès que vous savez combien de jours. Ne "
         "attendez pas d'avoir le papier en main."),
    ], notes="La troisième carte est importante et peu connue : une brûlure en cuisine "
             "est un accident de travail. Le dire, et renvoyer au module 3 pour la "
             "démarche auprès de l'employeur.")

    d.pratique('Pratique · 1 de 3', "Vrai ou faux — les soins",
               "Répondez sans relire le dialogue.", [
        ("La brûlure est du deuxième degré, superficielle.", "VRAI"),
        ("Le médecin dit que c'est dangereux.", "FAUX — ce n'est pas dangereux"),
        ("Fatou gardera sûrement une cicatrice.", "FAUX — probablement pas"),
        ("Il faut protéger la peau du soleil pendant six mois.", "VRAI"),
        ("Elle peut retourner en cuisine dès le lendemain.", "FAUX — trois jours de congé"),
        ("Elle reçoit un congé de maladie de trois jours.", "VRAI"),
        ("La crème s'applique deux fois par jour.", "VRAI"),
        ("Il faut revenir si la plaie devient jaune.", "VRAI"),
    ], corrige=True,
       notes="La troisième trompe : le médecin dit « probablement pas », ce qui n'est "
             "ni oui ni non. Faire entendre la nuance.")

    d.pratique('Pratique · 2 de 3', "Retrouvez le chiffre exact",
               "Les chiffres d'une consigne sont ce qu'on oublie en premier.", [
        ("Combien de jours de congé de maladie ?", "trois jours"),
        ("Combien de fois par jour la crème ?", "deux fois"),
        ("À quelle fréquence changer le pansement ?", "chaque matin"),
        ("Combien de temps protéger la peau du soleil ?", "six mois"),
    ], corrige=True,
       notes="Faire répondre cahier fermé. Puis demander qui avait noté les quatre "
             "chiffres pendant l'écoute : c'est la vraie leçon.")

    d.piege("Le piège du « ça va mieux »",
            "La crème, j'arrête quand ça ne fait plus mal.",
            "La crème, je continue jusqu'à ce que le médecin le dise.",
            "Une brûlure qui ne fait plus mal n'est pas guérie : la peau neuve est "
            "fragile pendant des semaines. Arrêter la crème trop tôt laisse la peau "
            "sèche et augmente le risque de cicatrice foncée.",
            notes="Relier au module 1, séance C4 : c'est le même raisonnement que pour "
                  "un antibiotique. Faire le lien explicitement.")

    d.pratique('Pratique · 3 de 3', "Quelle question posez-vous ?",
               "Le médecin vient de parler. Que demandez-vous ?", [
        ("« C'est une brûlure du deuxième degré. »",
         "Est-ce que c'est grave ?"),
        ("« Je vous donne un congé de maladie. »",
         "Pour combien de jours ?"),
        ("« Voici une crème à appliquer. »",
         "Combien de fois par jour, et pendant combien de temps ?"),
        ("« Revenez si ça ne va pas. »",
         "Qu'est-ce que je dois surveiller exactement ?"),
    ], corrige=True,
       notes="La quatrième question est celle que personne ne pose et qui manque le "
             "plus. Le souligner.")

    d.billet(
        "Résumez en cinq lignes ce que Fatou doit faire en rentrant chez elle.",
        exemples=[
            "Une ligne par consigne, avec le chiffre.",
            "Ajoutez une sixième ligne : dans quels cas elle doit retourner à l'urgence.",
        ],
        notes="Ramasser et corriger : ce billet montre exactement qui sait écouter une "
              "consigne médicale et qui ne le sait pas encore.")

    return d.save(dossier)
