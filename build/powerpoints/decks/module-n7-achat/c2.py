# -*- coding: utf-8 -*-
"""C2 · Trois garanties sur la même auto
Bloc C « Défi 2 · La réclamation au comptoir » · couleur teal · écoute et
réponse · 75 min.
Source : exercice `t2trois` et sa mini-leçon ; faits vérifiés auprès de
l'Office de la protection du consommateur.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C2', section='teal',
        titre="Trois garanties sur la même auto",
        chapeau="Elles ne se remplacent pas : elles s'additionnent. La "
                "plupart des gens n'en connaissent qu'une, et c'est celle "
                "qui comporte le plus d'exclusions.",
        duree='75 minutes')

    d.titre(notes="Séance de contenu, la plus factuelle du module. Tout ce qui est dit "
                  "ici vient de l'Office de la protection du consommateur. Le préciser "
                  "au groupe : ce ne sont pas des conseils, ce sont des règles.")

    d.objectifs([
        "nommer les trois garanties et dire ce que chacune donne ;",
        "lire la table des catégories et en tirer une durée ;",
        "savoir dans quel ordre les invoquer ;",
        "savoir ce qu'un commerçant doit dire avant de vendre une garantie payante.",
    ], notes="Le quatrième objectif est le seul qui protège avant l'achat. Y consacrer "
             "dix minutes pleines, même si le module n'y revient qu'en D1.")

    d.declencheur(
        'Observation', "Combien de garanties pensez-vous avoir sur un bien acheté d'un commerçant ?",
        pistes=[
            "Celle du fabricant, quand elle existe.",
            "Celle qu'on vous a vendue, si vous l'avez prise.",
            "Y en a-t-il une que vous n'avez jamais payée ?",
            "Que se passe-t-il quand toutes les autres sont expirées ?",
        ],
        notes="La troisième question est la révélation de la séance. Laisser un silence "
              "après l'avoir posée : personne ne répond, et c'est exactement ce que "
              "montre le module.")

    d.tableau('Analyse', "Trois protections qui s'additionnent",
              ['La garantie', 'Ce qu\'elle donne'],
              [["Légale", "une durée raisonnable, vu le prix payé"],
               ["Bon fonctionnement", "une durée chiffrée, selon la catégorie"],
               ["Prolongée", "ce que le contrat dit, moins les exclusions"],
               ["Ce qu'on paie", "rien, rien, et le prix demandé"],
               ["Ce qui reste à la fin", "la légale, toujours"]],
              cle=0,
              notes="Diapositive à photographier. La dernière rangée est celle qu'on "
                    "retient : la garantie légale survit à toutes les autres, et c'est "
                    "pour ça qu'elle est la dernière ligne de défense.")

    d.tableau('Analyse', "La table des catégories",
              ['La catégorie', 'La durée'],
              [["A · 4 ans ou moins, 80 000 km", "6 mois ou 10 000 km"],
               ["B · 5 ans ou moins, 100 000 km", "3 mois ou 5 000 km"],
               ["C · 7 ans ou moins, 120 000 km", "1 mois ou 1 700 km"],
               ["D · au-delà", "aucune"],
               ["La règle commune", "la première limite atteinte arrête tout"]],
              cle=0,
              notes="Diapositive à photographier, la plus utile du module. Insister sur "
                    "deux choses : il faut réussir les deux conditions pour entrer dans "
                    "une catégorie, et D ne veut pas dire « aucun recours ».")

    d.regle("Catégorie D ne veut pas dire aucun recours",
            "Une auto de catégorie D n'a pas de garantie de bon fonctionnement ; la garantie légale, elle, reste.",
            precision="C'est l'erreur la plus coûteuse du domaine. La garantie légale "
                      "s'applique à tout bien vendu par un commerçant, quel que soit "
                      "l'âge du véhicule : le bien doit servir à un usage normal "
                      "pendant une durée raisonnable, compte tenu du prix payé. Sur une "
                      "vieille auto payée quatre mille dollars, les attentes sont "
                      "moindres — mais elles existent.",
            notes="Diapositive à photographier. Le « compte tenu du prix payé » est en "
                  "faveur du consommateur : plus on a payé, plus la durée attendue est "
                  "longue. Le dire dans ces mots-là.")

    d.pratique('Écoute', "Laquelle des trois ?",
               "Chaque énoncé décrit une seule garantie. Dites laquelle.", [
        ("Elle est écrite dans la loi et ne s'achète pas.", "légale"),
        ("Sa durée est d'un mois ou 1 700 km en catégorie C.", "bon fonctionnement"),
        ("Elle a coûté 1 200 $ et exclut les joints.", "prolongée"),
        ("Sa durée se lit sur l'étiquette du véhicule.", "bon fonctionnement"),
        ("On peut la résoudre par écrit dans les dix jours.", "prolongée"),
        ("Elle s'applique encore quand toutes les autres sont finies.", "légale"),
    ], corrige=True,
       notes="Neuf items dans le module ; en projeter six. Faire justifier chaque "
             "réponse par un mot de l'énoncé : « dix jours » et « étiquette » sont des "
             "indices infaillibles.")

    d.regle("Avant de vendre une garantie payante, le commerçant doit informer",
            "Il doit dire, verbalement et par écrit, que la garantie légale existe et ce qu'elle contient.",
            precision="Celui qui ne le fait pas est réputé passer sous silence un fait "
                      "important — une pratique interdite. Et l'acheteur dispose de dix "
                      "jours suivant la conclusion du contrat pour le résoudre, par un "
                      "simple avis écrit. Le délai court à compter du lendemain de "
                      "l'achat.",
            notes="Diapositive à photographier. Dix jours, c'est court : le dire "
                  "maintenant est la seule façon que le groupe s'en souvienne le jour "
                  "où il achètera.")

    d.pratique('Écoute', "Que répondre au comptoir ?",
               "On vous dit la phrase de gauche. Que répondez-vous ?", [
        ("C'est de l'usure normale.", "Vingt-quatre jours et 900 km : sur quoi vous appuyez-vous ?"),
        ("La garantie du fabricant est finie.", "Je ne l'invoque pas. Je parle de la garantie légale."),
        ("C'est écrit à la page trois du contrat.", "Cette exclusion vise la garantie que j'ai payée."),
        ("Une auto de sept ans, madame…", "Mon étiquette dit catégorie C : un mois ou 1 700 km."),
    ], corrige=True,
       notes="Faire jouer les quatre échanges debout, deux par deux, avant de passer "
             "au billet. Trois minutes suffisent et l'effet sur E1 est net.")

    d.billet(
        "Une auto de trois ans avec 130 000 kilomètres : quelle catégorie, et quelle garantie reste-t-il ?",
        exemples=[
            "Deux réponses courtes.",
            "Attention : les deux conditions comptent.",
        ],
        notes="Trois minutes. La réponse est D, et il reste la garantie légale. C'est "
              "le contrôle le plus honnête de la séance : il faut avoir compris les "
              "deux tableaux pour y répondre.")

    return d.save(dossier)
