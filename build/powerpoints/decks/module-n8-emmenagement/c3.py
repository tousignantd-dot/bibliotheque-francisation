# -*- coding: utf-8 -*-
"""C3 · Ce qui aurait pu ne pas arriver
Bloc C « Défi 2 · Faire valoir sa réclamation » · couleur ambre · 75 min.
Écriture. Source du module : l'exercice `t2irr` et la mini-leçon du même nom.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C3', section='ambre',
        titre="Ce qui aurait pu ne pas arriver",
        chapeau="« Si on m'avait offert une déclaration de valeur, j'en "
                "aurais fait une. » La phrase désigne une faute et n'accuse "
                "personne. C'est pour ça qu'elle sert.",
        duree='75 minutes')

    d.titre(notes="Le programme du niveau 8 demande le conditionnel passé et "
                  "le plus-que-parfait. Les deux se rencontrent dans une "
                  "seule construction, celle-ci, et elle est l'outil de "
                  "négociation du module.")

    d.objectifs([
        "former si + plus-que-parfait, conditionnel passé ;",
        "ne jamais mettre de conditionnel après « si » ;",
        "accorder le participe dans les deux moitiés de la phrase ;",
        "retourner l'hypothèse contre soi, pour concéder.",
    ], notes="Le quatrième objectif est le plus utile et le moins évident : "
             "c'est ce qu'Amira fait à propos des boîtes du balcon.")

    d.declencheur(
        'Pour commencer', "« Si j'avais lu le contrat… » — terminez la phrase.",
        pistes=[
            "Est-ce que la personne a lu le contrat ?",
            "Comment le sait-on, alors que la phrase ne le dit pas ?",
            "À qui la phrase fait-elle un reproche ?",
        ],
        notes="La deuxième piste est le cœur : la construction affirme que la "
              "condition ne s'est pas réalisée. La troisième prépare le "
              "retournement — ici, le reproche est à soi-même.")

    d.regle("Si + plus-que-parfait, conditionnel passé",
            "Si j'avais lu le connaissement, je ne l'aurais pas signé.",
            precision="Jamais de conditionnel après « si ». « Si j'aurais lu » "
                      "ne se dit ni ne s'écrit, et cela s'entend "
                      "immédiatement.",
            notes="Diapositive à photographier. Moyen mnémotechnique : les "
                  "deux « r » du conditionnel ne franchissent jamais le "
                  "« si ». Le faire répéter.")

    d.tableau('Analyse', "Deux temps, une seule recette",
              ['Le temps', 'Comment il se forme'],
              [["plus-que-parfait", "avoir ou être à l'imparfait + participe : j'avais lu"],
               ["conditionnel passé", "avoir ou être au conditionnel + participe : j'aurais refusé"],
               ["avec être", "le participe s'accorde avec le sujet : elles seraient restées"],
               ["avec avoir", "il s'accorde avec le complément direct placé avant : la photo que j'aurais prise"]],
              cle=0,
              note="Si vous savez dire « j'avais lu » et « j'aurais lu », vous savez tout faire.",
              notes="Diapositive à photographier. Les deux dernières lignes "
                    "sont les seules vraies difficultés : l'accord du "
                    "participe, dans les deux moitiés de la phrase.")

    d.cartes('Analyse', "Retourner l'hypothèse contre soi", [
        ("L'hypothèse qui accuse", "« Si vos hommes avaient rentré les boîtes… »"),
        ("L'hypothèse qui concède", "« Si j'avais surveillé le balcon, elles seraient restées au sec. »"),
        ("Ce que la seconde produit", "elle désamorce l'accusation d'en face avant qu'elle soit formulée."),
        ("La règle d'usage", "une ou deux fois dans une conversation. Cinq fois, c'est de la plainte."),
    ], cols=2,
       notes="C'est exactement ce qu'Amira fait dans le dialogue `prep`. "
             "Faire retrouver la réplique : « personne ne surveillait le "
             "balcon, et j'aurais dû y penser ».")

    d.piege('Attention',
            "« la photo que j'aurais pris »",
            "« la photo que j'aurais prise »",
            "Avec « avoir », le participe s'accorde avec le complément direct "
            "placé avant. « Que » reprend « la photo », donc « prise ». "
            "L'erreur est invisible à l'oral et très visible dans une lettre "
            "d'affaires — c'est-à-dire précisément là où elle coûte.",
            notes="Rappeler la règle en une phrase, puis faire trouver trois "
                  "autres exemples tirés du dossier d'Amira : les pièces "
                  "qu'elle aurait envoyées, l'évaluation qu'elle aurait "
                  "demandée.")

    d.pratique('Pratique', "Complétez l'hypothèse du passé",
               "Mettez le verbe au temps qui convient.", [
        ("Si j'avais lu le connaissement, je ne l'___ (signer).", "aurais pas signé"),
        ("Si on m'___ (offrir) une déclaration, j'en aurais fait une.", "avait offert"),
        ("Si les boîtes avaient été rentrées, elles n'___ (prendre) l'eau.", "auraient pas pris"),
        ("Si le chauffeur ___ (noter) la fente, nous ne discuterions pas.", "avait noté"),
        ("Si j'___ (savoir) que le portage n'était pas le transport…", "avais su"),
        ("Si la rampe avait été un de mes biens, elle ___ (être) couverte.", "aurait été"),
    ], corrige=True, cols=1,
       notes="C'est l'exercice `t2irr` du module, dans sa version projetée. "
             "Demander chaque fois dans quelle moitié de la phrase on est : "
             "condition ou conséquence. C'est le repère.")

    d.billet(
        "Écris une hypothèse du passé qui concède quelque chose dans ton propre dossier.",
        exemples=[
            "Commence par « si j'avais… ».",
            "Le reproche doit être adressé à toi, pas à l'autre.",
        ],
        notes="Cinq minutes. Ramasser. L'erreur la plus fréquente restera le "
              "conditionnel après « si » ; la seconde, l'accord du participe.")

    return d.save(dossier)
