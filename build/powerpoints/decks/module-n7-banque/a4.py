# -*- coding: utf-8 -*-
"""A4 · Dire ce qu'on n'a pas compris
Bloc A « Je découvre » · couleur teal · 90 min. Écoute et réponse.
Source : exercice `prReprise` et sa mini-leçon, savoir lexical de la situation.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A4', section='teal',
        titre="Dire ce qu'on n'a pas compris",
        chapeau="Faire oui de la tête met fin à l'explication, et le document "
                "se signe sur un malentendu. Trois phrases, apprises par "
                "coeur, changent tout.",
        duree='90 minutes')

    d.titre(notes="Séance la plus importante du bloc A, et celle que les élèves "
                  "réemploieront le plus vite ailleurs : chez le médecin, à l'école, au "
                  "garage. Le dire en ouvrant.")

    d.objectifs([
        "reprendre le mot exact qu'on n'a pas compris ;",
        "reformuler avec ses propres mots pour vérifier ;",
        "demander un exemple chiffré appliqué à son cas ;",
        "interrompre poliment au moment où le mot échappe.",
    ], notes="Le programme du niveau 7 nomme ce savoir dans la situation elle-même : "
             "« expressions pour reprendre une partie d'un discours et exprimer une "
             "incompréhension partielle ». Le mot qui compte est « partielle ».")

    d.declencheur(
        'Observation', "Que fais-tu quand tu ne comprends pas un mot dans une "
                       "explication importante ?",
        pistes=[
            "Tu demandes tout de suite, ou tu attends la fin ?",
            "Est-ce que ça t'est déjà arrivé de faire oui sans comprendre ?",
            "Qu'est-ce qui t'a retenu de demander ?",
            "Qu'est-ce qui s'est passé ensuite ?",
        ],
        notes="Question personnelle mais sans risque : tout le monde a fait oui de la "
              "tête un jour. Commencer par le dire soi-même met le groupe à l'aise.")

    d.regle("« Quoi ? » ne dit rien à personne",
            "Votre interlocuteur ne sait pas ce qui vous a échappé : il recommence à "
            "l'identique.",
            precision="Le mot, le chiffre, ou toute la phrase ? Tant qu'il l'ignore, il "
                      "répète la même chose de la même façon, et vous ne comprenez pas "
                      "davantage la deuxième fois. Reprendre le mot exact lui dit "
                      "précisément où vous avez décroché.",
            notes="Diapositive à photographier. Faire l'expérience : dire une phrase "
                  "difficile, laisser un élève répondre « quoi ? », répéter à "
                  "l'identique. Le groupe comprend tout de suite.")

    d.tableau('Analyse', "Trois phrases, trois effets",
              ['Ce que je dis', "Ce que j'obtiens"],
              [['Quand vous dites x', 'une définition du mot exact'],
               ['Donc si je comprends bien', 'une confirmation ou une correction'],
               ['Sur mille dollars', 'un chiffre appliqué à mon cas'],
               ['Quoi ?', 'la même phrase, redite pareil']],
              cle=0,
              note="Les trois premières sont à apprendre par coeur.",
              notes="Diapositive à photographier. Faire copier les trois phrases dans "
                    "le cahier, en toutes lettres, avec leur ponctuation.")

    d.cartes('Modèles', "Les phrases à emporter", [
        ('Faire répéter', "Quand vous dites « capitalisé », ça veut dire quoi exactement ?"),
        ('Faire répéter', "Je vous suis jusqu'au taux, mais j'ai perdu la suite."),
        ('Vérifier', "Donc si je comprends bien, je ne paie que sur ce que je prends ?"),
        ('Vérifier', "Ce que vous appelez « le minimum », c'est le montant en bas ?"),
        ('Demander un exemple', "Sur mille dollars, ça donnerait combien exactement ?"),
        ('Demander un exemple', "Ça ressemblerait à quoi, dans mon cas à moi ?"),
    ], notes="Faire répéter chaque phrase avec la bonne intonation : la voix monte à la "
             "fin, et elle ralentit sur les trois derniers mots.")

    d.pratique('Application', "À quoi sert chaque phrase ?",
               "Dites : je fais répéter, je vérifie, ou je demande un exemple.", [
        ("Excusez-moi, vous pouvez répéter le dernier chiffre ?", "je fais répéter"),
        ("Donc si je comprends bien, le taux peut monter ?", "je vérifie"),
        ("Sur mille dollars, ça donnerait combien ?", "je demande un exemple"),
        ("Quand vous dites « variable », ça veut dire quoi ?", "je fais répéter"),
        ("Autrement dit, la date de fin est au contrat ?", "je vérifie"),
        ("Vous auriez un cas concret à me donner ?", "je demande un exemple"),
    ], corrige=True,
       notes="Faire justifier : ce n'est pas le sens de la phrase qui décide, c'est ce "
             "qu'elle demande à l'autre de produire.")

    d.piege('Le piège', "attendre la fin pour poser sa question",
            "interrompre au mot qui manque",
            "Après trois minutes d'explication, le mot est loin et vous ne savez plus "
            "lequel c'était. Couper tout de suite, poliment, avec « excusez-moi, un "
            "mot » : personne n'en prend ombrage, et l'explication reprend au bon "
            "endroit.",
            notes="Faire pratiquer l'interruption elle-même, qui est un geste de langue "
                  "à part entière. Beaucoup d'élèves ne l'ont jamais fait en français.")

    d.pratique('Jeu de rôle', "Deux par deux, trois minutes chacun",
               "A explique un produit avec des mots difficiles ; B ne fait jamais oui "
               "de la tête.", [
        ("A dit : « les intérêts sont capitalisés mensuellement »", "B reprend le mot"),
        ("A dit : « le taux est variable »", "B demande la conséquence"),
        ("A dit : « c'est déductible »", "B propose sa compréhension"),
        ("A donne un pourcentage", "B demande un exemple chiffré"),
        ("A parle trop vite", "B fait ralentir"),
    ], corrige=False,
       notes="Circuler. Le seul critère de réussite : B n'a jamais dit « d'accord » "
             "sans avoir posé une question. Le dire avant de commencer.")

    d.billet("Écris la phrase que tu emploieras la prochaine fois que tu ne "
             "comprendras pas un mot.",
             exemples=["Quand vous dites « capitalisé », ça veut dire quoi exactement ?"],
             notes="Deux minutes. Garder les billets et les redistribuer au début du "
                   "bloc B : c'est exactement la situation du dialogue de B1.")

    return d.save(dossier)
