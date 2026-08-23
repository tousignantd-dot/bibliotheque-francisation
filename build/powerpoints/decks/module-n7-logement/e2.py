# -*- coding: utf-8 -*-
"""E2 · Écris ta réponse à l'avis
Bloc E « Je me lance » · couleur framboise · production écrite et bilan ·
75 min.
Source : bloc `appli` de `custom.js` — production écrite et ses huit
exigences —, banc FC_CARDS, autoévaluation en seize énoncés.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='E2', section='framboise',
        titre="Écris ta réponse à l'avis",
        chapeau="Dernière séance : une lettre de dix à quatorze phrases, en "
                "trois paragraphes. Ce que tu as reçu, ce que tu proposes, "
                "ce que tu demandes.",
        duree='75 minutes')

    d.titre(notes="Dernière séance du module. Rendre les décisions écrites au billet "
                  "de E1 : la lettre découle de la décision. Prévoir quarante minutes "
                  "d'écriture réelle, et garder le bilan pour la fin.")

    d.objectifs([
        "rédiger une lettre formelle de dix à quatorze phrases ;",
        "organiser le texte en trois paragraphes, un par idée ;",
        "employer une concession, une demande au conditionnel et une condition au subjonctif ;",
        "évaluer ce qu'on est maintenant capable de faire.",
    ], notes="Ce sont les attentes de fin de cours du niveau 7 : rédiger un texte "
             "formel simple, à l'aide d'un modèle, en organisant ses idées à l'aide de "
             "paragraphes reliés par des connecteurs.")

    d.declencheur(
        'Mise en situation', "Une réponse écrite, et pourquoi elle vaut mieux qu'un appel",
        pistes=[
            "Qui va lire cette lettre, et quand ?",
            "Que se passe-t-il si vous téléphonez plutôt que d'écrire ?",
            "Par quoi commencez-vous : le reproche ou le fait ?",
            "Qu'est-ce que vous demandez, exactement, à la fin ?",
        ],
        notes="La deuxième question est la vraie : un appel ne laisse aucune trace, et "
              "c'est la trace qui compte quand le délai se calcule en mois.")

    d.tableau('Analyse', "Trois paragraphes, trois travaux",
              ['Le paragraphe', 'Ce quon y met'],
              [["1 · Pourquoi vous écrivez", "l'avis reçu, sa date, ce que vous répondez"],
               ["2 · Les faits", "le montant proposé, la fenêtre, votre contre-proposition"],
               ["3 · Ce que vous demandez", "une réponse écrite, et sous quel délai"],
               ["L'objet", "court, précis, sans phrase complète"],
               ["La fin", "une salutation fermée, et votre nom"]],
              cle=0,
              notes="Diapositive à photographier, et à laisser affichée pendant "
                    "l'écriture. Elle remplace toute autre consigne.")

    d.cartes('Production écrite', "Quatre phrases à placer, quatre outils du module", [
        ("La concession", "« Je comprends que vos taxes et votre assurance ont augmenté cette année, cela dit… »"),
        ("La demande au conditionnel", "« Accepteriez-vous de ramener la hausse à cinquante-cinq dollars ? »"),
        ("La condition au subjonctif", "« J'accepterais cette hausse à condition que la fenêtre soit examinée avant l'automne. »"),
        ("La phrase emphatique", "« Ce qui me préoccupe, ce n'est pas la hausse elle-même, c'est son montant d'un seul coup. »"),
    ], notes="Les quatre phrases sont des modèles de forme, pas de contenu : chacun "
             "écrit les siennes avec ses propres chiffres. Le dire explicitement.")

    d.regle("Écrivez ce que vous faites, pas ce que vous pensez de lui",
            "Une lettre qui s'en tient aux faits, aux dates et à un montant obtient un écrit en retour.",
            precision="Le propriétaire ne changera pas d'avis parce que vous lui aurez "
                      "dit qu'il exagère ; il changera d'avis parce qu'un montant, une "
                      "date et une contrepartie sont posés devant lui. Et c'est la "
                      "réponse écrite qui compte : c'est elle que vous relirez en "
                      "novembre, quand personne ne se souviendra de la conversation "
                      "dans la cuisine.",
            notes="Diapositive à photographier. C'est aussi le critère principal de la "
                  "correction : on évalue ce que la lettre demande, pas ce qu'elle "
                  "ressent.")

    d.pratique('Vocabulaire', "Les seize mots du module, un dernier tour",
               "Donnez la définition de mémoire, puis vérifiez avec les cartes.", [
        ("un avis de modification · un délai de réponse", "le papier reçu et le mois pour répondre"),
        ("une contrepartie · un compromis", "ce qu'on offre, et le point où les deux reculent"),
        ("un courtier immobilier · un contrat de courtage", "pour qui il travaille, et le papier qui le dit"),
        ("les frais de copropriété · le fonds de prévoyance", "ce qu'on paie chaque mois, et ce qu'on met de côté"),
        ("une promesse d'achat · une inspection préachat", "ce qui engage, et ce qui protège"),
        ("la mise de fonds · les droits de mutation", "l'argent de départ, et la facture qui suit"),
    ], corrige=True,
       notes="Par paires, cinq minutes. Les seize mots du banc, regroupés deux à deux "
             "par le lien qui les unit : c'est ainsi qu'ils se retiennent.")

    d.billet(
        "Qu'est-ce que tu es capable de faire aujourd'hui, que tu ne faisais pas avant ce module ?",
        exemples=[
            "Une phrase, sur le logement ou ailleurs.",
            "L'autoévaluation en seize énoncés est dans le module.",
        ],
        notes="Cinq minutes, à la toute fin. Faire lire trois billets à voix haute. "
              "Rappeler que l'autoévaluation du module reste ouverte à la maison.")

    return d.save(dossier)
