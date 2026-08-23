# -*- coding: utf-8 -*-
"""A4 · La phrase passive, et ce qu'elle cache
Bloc A « Je découvre » · couleur ambre · 75 min. Écriture.
Source du module : l'exercice `prPass` et la mini-leçon du même nom.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A4', section='ambre',
        titre="La phrase passive, et ce qu'elle cache",
        chapeau="« Sont exclus les dommages causés aux biens meubles » — "
                "exclus par qui ? La phrase ne le dit pas, et c'est "
                "exactement pour ça qu'elle est écrite ainsi.",
        duree='75 minutes')

    d.titre(notes="Premier point de grammaire du module. Le passif est ici un "
                  "outil de lecture avant d'être un outil d'écriture : les "
                  "documents du défi 1 et du défi 2 en sont pleins.")

    d.objectifs([
        "former le passif à quatre temps, avec l'accord du participe ;",
        "repérer un passif sans complément d'agent dans un contrat ;",
        "poser la question « par qui ? » devant chacun ;",
        "employer le passif pour poser un fait sans accuser personne.",
    ], notes="Le quatrième objectif est celui qui sert dans une négociation. "
             "Y consacrer au moins un tiers de la séance.")

    d.declencheur(
        'Pour commencer', "« Le chauffeur a signé l'inventaire. » Dites la "
                          "même chose en commençant par « l'inventaire ».",
        pistes=[
            "Qu'est-ce qui a changé dans la phrase ?",
            "Est-ce que la réalité a changé ?",
            "Maintenant, enlevez « par le chauffeur ». Que reste-t-il ?",
        ],
        notes="La troisième piste est le cœur de la séance : en enlevant le "
              "complément d'agent, on obtient la phrase de contrat. Laisser "
              "la classe constater que personne n'agit plus.")

    d.regle("être au temps du verbe, plus le participe accordé",
            "on exclut devient : est exclu · on a refusé devient : a été refusé · on refusera devient : sera refusé · on avait offert devient : avait été offert",
            precision="Le participe ne bouge jamais ; c'est « être » qui "
                      "voyage dans les temps. Et il s'accorde avec le sujet, "
                      "comme un adjectif.",
            notes="Diapositive à photographier. Faire remarquer que le nombre "
                  "de mots augmente d'un à chaque étage : est exclu, a été "
                  "exclu, avait été exclu.")

    d.tableau('Analyse', "Défaire un passif pour voir qui manque",
              ['La phrase du contrat', 'La question qu\'elle laisse ouverte'],
              [["Sont exclus les dommages causés…", "Exclus par qui ?"],
               ["Il a été établi que…", "Établi par qui, sur quelle pièce ?"],
               ["La décision vous sera communiquée.", "Par qui, dans quel délai ?"],
               ["Le dommage retenu s'établit à 940 $.", "Retenu par qui, écarté sur quoi ?"]],
              cle=0,
              note="Un passif sans « par » cache quelqu'un. C'est presque toujours une bonne question.",
              notes="Diapositive à photographier. Ces quatre phrases sont "
                    "reprises telles quelles dans les documents du défi 1 et "
                    "du défi 2 : la classe les reverra.")

    d.cartes('Attention', "Un état ou une action ?", [
        ("« Le meuble est fendu »", "décrit un état, qui peut dater de trente ans."),
        ("« Le meuble a été fendu pendant le portage »", "décrit une action, située dans le temps."),
        ("Devant un assureur", "seule la seconde pèse quelque chose."),
        ("Le test", "Est-ce qu'on peut ajouter « par… » ? Si oui, c'est un passif."),
    ], cols=2,
       notes="La confusion est très fréquente et elle coûte une réclamation. "
             "Le test de la dernière carte est le plus rapide à appliquer.")

    d.piege('Attention',
            "« Aucune déclaration ne m'a été proposée par votre chauffeur »",
            "« Aucune déclaration de valeur ne m'a été proposée »",
            "Le passif sert précisément à ne pas nommer. En nommant le "
            "chauffeur, vous transformez un fait en accusation — et une "
            "accusation se nie, alors qu'un fait se discute. Employez le "
            "passif au moment où accuser fermerait la conversation.",
            notes="Ce piège-là n'est pas une faute de grammaire : c'est un "
                  "choix de stratégie, et il sera réemployé en C4 et en E2.")

    d.pratique('Pratique', "Mettez le verbe à la voix passive",
               "Écrivez seulement le verbe et son auxiliaire.", [
        ("L'inventaire (signer, passé composé) ___ par le chauffeur.", "a été signé"),
        ("La rampe (tordre, passé composé) ___ par le coin de la remorque.", "a été tordue"),
        ("Les deux boîtes (laisser, passé composé) ___ sur le balcon.", "ont été laissées"),
        ("Ces dommages-là (exclure, présent) ___ par la clause 7.3.", "sont exclus"),
        ("La décision vous (communiquer, futur) ___ par écrit.", "sera communiquée"),
        ("Le connaissement (rédiger, plus-que-parfait) ___ bien avant.", "avait été rédigé"),
    ], corrige=True, cols=1,
       notes="C'est l'exercice `prPass` du module, dans sa version projetée. "
             "Faire écrire, puis corriger en demandant chaque fois avec quoi "
             "le participe s'accorde.")

    d.billet(
        "Écris une phrase passive qui pose un fait de ton déménagement sans accuser personne.",
        exemples=[
            "Commence par la chose, pas par la personne.",
            "N'écris pas « par… » à la fin : c'est le but de l'exercice.",
        ],
        notes="Cinq minutes. Ramasser : les phrases qui nomment encore "
              "quelqu'un se repèrent d'un coup d'œil, et c'est exactement "
              "l'erreur à reprendre avant le défi 2.")

    return d.save(dossier)
