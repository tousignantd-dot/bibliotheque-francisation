# -*- coding: utf-8 -*-
"""C1 · Ce qui est accepté, ce qui est refusé
Bloc C « Défi 2 · Faire valoir sa réclamation » · couleur acier · 75 min.
Compréhension orale. Source du module : le dialogue `t2` et l'exercice `t21`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C1', section='acier',
        titre="Ce qui est accepté, ce qui est refusé",
        chapeau="Trente-trois répliques, un point accepté et deux refusés. "
                "Ce qui se joue n'est plus du vocabulaire : c'est de "
                "l'argumentation.",
        duree='75 minutes')

    d.titre(notes="Séance charnière du module. L'experte n'est pas de "
                  "mauvaise foi : elle a raison sur deux points sur trois, et "
                  "c'est ce qui rend l'exercice réel. Le dire à la classe "
                  "avant l'écoute.")

    d.objectifs([
        "suivre une conversation de désaccord conduite en cinq étapes ;",
        "repérer les deux moments où Amira accepte, et pourquoi ;",
        "entendre comment elle obtient la clause, puis sa lecture exacte ;",
        "reconnaître le compromis chiffré et sa contrepartie.",
    ], notes="Les cinq étapes — découper, concéder, exiger la clause, "
             "retourner, proposer — structurent tout le bloc C. Les annoncer "
             "ici et y revenir à chaque séance.")

    d.declencheur(
        'Avant d\'écouter', "On vous refuse quelque chose au téléphone. Quelle "
                            "est votre première phrase ?",
        pistes=[
            "« Pourquoi ? » ou « sur quelle clause vous appuyez-vous ? »",
            "Quelle différence entre les deux ?",
            "Laquelle appelle une opinion, laquelle appelle un texte ?",
        ],
        notes="La distinction est le cœur de la séance. « Pourquoi » appelle "
              "une opinion, qui se discute sans fin ; « quelle clause » "
              "appelle un texte, qu'on peut relire et retourner.")

    d.dialogue('Écoute', "Ce qui est accepté, ce qui est refusé", [
        ("AMIRA", "J'aimerais qu'on prenne les trois points l'un après l'autre.", True),
        ("VÉRONIQUE", "Deuxième point : la rampe de l'escalier extérieur. Refusé.", False),
        ("AMIRA", "Sur quelle clause vous appuyez-vous, exactement ?", True),
        ("AMIRA", "Celle-là, je l'accepte. Elle est logique et la clause est claire.", True),
        ("AMIRA", "Certes la clause existe. Mais elle parle du transport, et le vaisselier n'a pas été fendu pendant le transport.", True),
        ("VÉRONIQUE", "C'est un argument. Je ne dis pas qu'il est gagnant, je dis que c'en est un.", False),
    ], consigne="Six répliques sur trente-trois. Les quatre en couleur sont "
                "les quatre gestes de la méthode.",
       notes="Faire écouter l'extrait entier avant d'afficher. Demander "
             "ensuite quel geste manque dans cette liste : le cinquième, la "
             "proposition chiffrée, qui vient à la fin de l'extrait.")

    d.tableau('Analyse', "Cinq étapes, et la phrase qui les ouvre",
              ['L\'étape', 'Ce qu\'on dit'],
              [["1. Découper", "Reprenons les trois points l'un après l'autre."],
               ["2. Concéder", "Celle-là, je l'accepte. La clause est claire."],
               ["3. Exiger la clause", "Sur quelle clause vous appuyez-vous ?"],
               ["4. Retourner", "Certes la clause existe. Or elle parle du transport."],
               ["5. Proposer", "Je propose huit cent cinquante dollars, contre ma renonciation."]],
              cle=0,
              note="Les étapes ne s'inversent pas : concéder après avoir contesté ne compte pas.",
              notes="Diapositive à photographier. C'est le plan de tout le "
                    "bloc C, du jeu de rôle de E1 et de la lettre de E2. La "
                    "faire recopier.")

    d.regle("Un refus sans clause n'est pas un refus",
            "C'est une opinion — et une opinion se retire. Demandez la clause, puis demandez qu'on vous la lise mot pour mot.",
            precision="C'est dans les mots exacts que se trouve presque "
                      "toujours la faille : ici, « pendant leur transport » "
                      "et non « pendant le service ».",
            notes="Diapositive à photographier. Faire remarquer qu'Amira "
                  "demande deux fois : d'abord la clause, ensuite sa lecture "
                  "exacte. Une seule demande n'aurait rien donné.")

    d.pratique('Pratique', "Vrai ou faux",
               "Écoutez de nouveau, puis répondez.", [
        ("Amira conteste le montant retenu pour les livres.", "FAUX"),
        ("La rampe est refusée parce qu'elle appartient au bâtiment.", "VRAI"),
        ("Amira conteste aussi le refus concernant la rampe.", "FAUX"),
        ("Elle soutient que le meuble a été fendu pendant le portage.", "VRAI"),
        ("Elle demande la révision des trois points de la décision.", "FAUX"),
        ("Encaisser un chèque du déménageur n'a aucun effet sur la révision.", "FAUX"),
    ], corrige=True, cols=1,
       notes="C'est l'exercice `t21` du module, dans sa version projetée. "
             "Quatre « faux » : trois d'entre eux portent sur ce qu'Amira ne "
             "conteste PAS, ce qui est tout le point de la séance.")

    d.billet(
        "Écris la phrase par laquelle tu concéderais un point, puis celle par laquelle tu retournerais.",
        exemples=[
            "Deux phrases, dans cet ordre.",
            "La première commence par « certes » ou « je vous l'accorde ».",
        ],
        notes="Cinq minutes. Ramasser : les concessions à moitié faites — "
              "« c'est peut-être vrai, mais » — sont l'erreur à reprendre, et "
              "elle sera travaillée en C4.")

    return d.save(dossier)
