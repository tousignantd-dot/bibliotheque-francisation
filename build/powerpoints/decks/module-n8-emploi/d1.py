# -*- coding: utf-8 -*-
"""D1 · Ce qui existe, et ce que ça demande.
Bloc D « Défi 3 · Se perfectionner » · couleur acier · 60 min.
Source : dialogue `t3`, exercices `t3vf` et `t3texte`.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n8-emploi/images/')


def build(dossier):
    d = Deck(
        code='D1', section='acier',
        titre="Ce qui existe, et ce que ça demande",
        chapeau="Trois avenues pour se perfectionner quand on travaille "
                "déjà : l'attestation du soir, la formation payée par "
                "l'employeur, et la reconnaissance de ce qu'on sait déjà faire.",
        duree='60 minutes')

    d.titre(notes="Ouverture du Défi 3. Séance à haute valeur pratique : plusieurs "
                  "élèves ignorent l'existence de la reconnaissance des acquis, et "
                  "c'est souvent la voie qui leur convient.")

    d.objectifs([
        "comprendre un entretien d'information long et nuancé ;",
        "lire un texte informatif sur la formation en entreprise ;",
        "distinguer les trois avenues de perfectionnement ;",
        "savoir dans quel cas se trouve son propre employeur.",
    ], notes="L'objectif 4 change l'argument de la demande. Au-dessus de deux millions "
             "de masse salariale : « la dépense est déjà prévue ». En dessous : « voici "
             "ce qu'elle vous rapporte ».")

    d.declencheur(
        'Observation', "Qu'est-ce que vous aimeriez apprendre ?",
        image=IMG + 'cours-du-soir.jpg',
        pistes=[
            "Quelle partie de votre travail ne maîtrisez-vous pas ?",
            "Qu'est-ce que ça vous coûte, en temps, chaque mois ?",
            "Avez-vous déjà fait ce métier ailleurs ?",
            "Qui paierait la formation, selon vous ?",
        ],
        notes="La deuxième piste est la clé du Défi 3 : c'est le chiffre qui deviendra "
              "l'argument de la demande écrite.")

    d.dialogue('Dialogue · 1 de 3', "Trois avenues", [
        ("NADIA", "J'aimerais me perfectionner sur la gestion des comptes fournisseurs, sauf que je ne sais pas ce qui existe.", True),
        ("CLAUDIA", "Il y a trois avenues. L'attestation d'études, offerte le soir. Les formations sur mesure achetées par les entreprises. Et la reconnaissance des acquis.", True),
        ("NADIA", "J'ai tenu la comptabilité d'une école en Algérie pendant quatre ans, mais avec un logiciel qui n'existe pas ici.", True),
        ("CLAUDIA", "Le logiciel s'apprend en quelques semaines. Ce qui compte, c'est ce que vous savez du métier. Ça ne s'oublie pas et ça se fait reconnaître.", True),
    ], consigne="Écoutez d'abord, diapositive masquée.",
       notes="La réplique de Claudia sur le logiciel mérite d'être relue au groupe. "
             "Beaucoup se croient disqualifiés par un outil qu'ils ne connaissent pas.")

    d.dialogue('Dialogue · 2 de 3', "Demander de la bonne façon", [
        ("CLAUDIA", "Un employeur ne dit pas oui à « j'aimerais suivre un cours ». Il dit oui à « voici ce que ça coûte, voici ce que ça vous rapporte ».", True),
        ("NADIA", "Autrement dit, j'arrive avec le problème réglé au lieu d'arriver avec une demande.", True),
        ("CLAUDIA", "Exactement. Chiffrez-le : combien d'heures les erreurs de facturation vous prennent-elles chaque mois ?", True),
        ("NADIA", "Facilement trois heures. Peut-être quatre.", True),
    ], notes="Nadia reformule avec « autrement dit » — la formule de C2, réemployée "
             "spontanément. Le faire remarquer : c'est le signe que le module tient.")

    d.dialogue('Dialogue · 3 de 3', "Écrire, pas dire", [
        ("CLAUDIA", "Quarante heures par année. C'est ça que vous mettez dans votre demande, pas votre envie d'apprendre.", True),
        ("NADIA", "C'est un peu froid, dit comme ça.", True),
        ("CLAUDIA", "C'est froid, oui, mais c'est la langue dans laquelle une décision se prend.", True),
        ("CLAUDIA", "Écrivez votre demande par courriel, pas de vive voix. Ça se relit, ça se transfère, et ça laisse une trace de la date.", True),
    ], notes="La dernière réplique justifie la production écrite de E2. Elle rejoint "
             "aussi la règle de A3 : tout ce qui s'écrit passe au registre standard.")

    d.tableau('Analyse', "Trois avenues, trois conditions",
              ['L\'avenue', 'Ce qu\'elle demande'],
              [["L'attestation d'études", "des cours le soir, à partir de 18 h 30"],
               ["La formation sur mesure", "que l'employeur l'achète pour ses employés"],
               ["La reconnaissance des acquis", "un dossier et une entrevue avec un spécialiste du métier"]],
              cle=0,
              note="La troisième ne fait pas apprendre : elle fait créditer ce qui est déjà su.",
              notes="Diapositive à photographier. Donner les coordonnées du service de "
                    "reconnaissance des acquis du centre de services scolaire local.")

    d.cartes("Le texte informatif", "Se former quand on est déjà en emploi", [
        ("La loi dite « du 1 % »",
         "Les employeurs dont la masse salariale dépasse deux millions de dollars doivent investir au moins 1 % en formation du personnel."),
        ("S'ils n'investissent pas",
         "Ils versent la différence à un fonds public. La somme est dépensée de toute façon : mieux vaut qu'elle serve à leurs employés."),
        ("Les entreprises plus petites",
         "Elles ne sont pas visées par l'obligation. Elles peuvent tout de même former, et beaucoup le font."),
        ("Ce que ça change pour vous",
         "L'argument n'est pas le même selon le cas. Savoir lequel s'applique double vos chances."),
    ], notes="Données vérifiées auprès de la Commission des partenaires du marché du "
             "travail et de Revenu Québec. Ne rien ajouter de mémoire.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "D'après l'entretien et le texte.", [
        ("Claudia présente trois avenues.", "vrai"),
        ("Selon elle, le logiciel est le plus difficile à rattraper.", "faux — il s'apprend en quelques semaines"),
        ("La reconnaissance des acquis passe par une entrevue.", "vrai"),
        ("Il faut mettre son envie d'apprendre au cœur de la demande.", "faux — le chiffre, pas l'envie"),
        ("L'obligation du 1 % vise les masses salariales de plus de deux millions.", "vrai"),
        ("Toutes les entreprises du Québec sont visées.", "faux"),
        ("Claudia conseille de faire la demande de vive voix.", "faux — par courriel"),
    ], corrige=True,
       notes="Deux écoutes pour l'entretien, une lecture silencieuse pour le texte.")

    d.billet(
        "Chiffrez ce qu'une lacune vous coûte, en heures par mois.",
        exemples=[
            "Multipliez par douze : c'est votre argument.",
            "Nommez la formation qui règlerait le problème.",
        ],
        notes="Ce chiffre est le cœur de la demande écrite de E2. Sans lui, il n'y a "
              "pas de demande, seulement un souhait.")

    return d.save(dossier)
