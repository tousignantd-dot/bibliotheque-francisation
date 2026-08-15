# -*- coding: utf-8 -*-
"""C4 · Privé, coopérative, HLM.
Bloc C · couleur foret (vocabulaire et culture) · 55 min.
Source : mini-leçon `t2coop`, exercice `t2coop` et son encadré culturel.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C4', section='foret',
        titre="Trois façons d'habiter au Québec",
        chapeau="Quand on cherche un logement, on rencontre trois modèles très différents. "
                "Vos droits, vos coûts et vos obligations ne sont pas les mêmes dans les "
                "trois. Une coopérative n'est ni un logement privé, ni un HLM.",
        duree='55 minutes')

    d.titre(notes="Séance de culture québécoise. Beaucoup d'élèves cherchent activement un "
                  "logement : c'est une séance qui sert immédiatement. Prévoir des "
                  "questions personnelles.")

    d.objectifs([
        "distinguer le logement locatif privé, la coopérative d'habitation et le HLM ;",
        "savoir qui décide et qui paie dans chacun des trois modèles ;",
        "savoir à qui s'adresser quand un problème survient ;",
        "connaître ce qu'on obtient — et ce qu'on doit donner — en coopérative.",
    ])

    d.declencheur('Mise en route', "Dans quel type de logement habitez-vous ?", pistes=[
        "Est-ce qu'il y a un propriétaire, une compagnie, ou un organisme ?",
        "Est-ce que vous participez à des réunions ou à l'entretien ?",
        "Est-ce que votre loyer dépend de votre revenu ?",
        "Ces trois questions suffisent à distinguer les trois modèles.",
    ], notes="Tour de table rapide. Ne pas insister si quelqu'un ne veut pas répondre : "
             "le type de logement touche au revenu, et c'est une information privée.")

    d.tableau('Modèle 1', "Le logement locatif privé",
              ['Question', 'Réponse', ''],
              [["Qui décide ?", "la personne propriétaire", "seule"],
               ["Qui paie les réparations ?", "la personne propriétaire", "c'est son immeuble"],
               ["Que fait le locataire ?", "payer le loyer, signaler", "rien de plus"]],
              cle=1,
              note="C'est le modèle le plus courant, et aussi celui où le loyer est le plus "
                   "élevé, parce que la personne propriétaire cherche un rendement. "
                   "L'immeuble d'Oksana est un immeuble privé.",
              notes="Relier au module : madame Rioux décide et paie. C'est pour ça qu'Oksana "
                    "n'a pas à choisir l'électricien elle-même.")

    d.tableau('Modèle 2', "La coopérative d'habitation",
              ['Question', 'Réponse', ''],
              [["Qui décide ?", "les membres, par vote", "ensemble"],
               ["Qui paie ?", "la coopérative", "sans profit"],
               ["Que fait le membre ?", "payer, participer, siéger", "du temps en plus"]],
              cle=1,
              note="L'immeuble appartient collectivement à celles et ceux qui y habitent. "
                   "Chaque membre est à la fois locataire de son logement et copropriétaire "
                   "de l'immeuble.",
              notes="La double qualité — locataire ET copropriétaire — est le point le plus "
                    "difficile. Le faire reformuler par deux élèves.")

    d.regle('Modèle 3 · le HLM',
            "Une habitation à loyer modique est un logement social géré par un office public.",
            precision="Le loyer y est calculé selon le revenu — souvent autour de 25 % du "
                      "revenu du ménage — et l'accès se fait par une liste d'attente, selon "
                      "des critères précis. Ce n'est ni un immeuble privé ni un groupe qui "
                      "se gère lui-même : c'est un programme public.",
            notes="Ne pas s'étendre sur les critères d'admissibilité : ils changent, et ce "
                  "n'est pas l'objet du cours. Renvoyer à l'office d'habitation de la ville.")

    d.regle('Le résumé en une ligne',
            "Privé : le marché. Coopérative : un groupe qui se gère lui-même. HLM : un programme public selon le revenu.",
            precision="Trois logiques différentes, trois interlocuteurs différents quand un "
                      "problème survient. Mais dans les trois cas, le réflexe reste "
                      "exactement le même : signaler tôt, et garder une trace écrite.",
            notes="C'est la diapo à photographier. La dernière phrase relie la séance à "
                  "tout le reste du module.")

    d.pratique('Pratique', "Qui règle le problème ?",
               "Le calorifère ne chauffe plus. À qui vous adressez-vous ?", [
        ("Dans un logement privé", "on prévient la propriétaire — elle décide et elle paie"),
        ("Dans une coopérative", "on prévient le comité d'entretien — les membres s'en occupent"),
        ("Dans un HLM", "on prévient l'office d'habitation — un organisme public gère l'immeuble"),
    ], corrige=True,
       notes="Faire remarquer que la phrase à dire reste identique dans les trois cas. "
             "Seul le destinataire change.")

    d.vocabulaire('Vocabulaire', "Les mots à retenir", [
        ("une part sociale", "Ce qu'on achète pour devenir membre d'une coopérative."),
        ("un membre", "Une personne qui habite la coopérative et participe à sa gestion."),
        ("le comité d'entretien", "Le groupe de membres qui s'occupe des réparations."),
        ("un office d'habitation", "L'organisme public qui gère les HLM d'une ville."),
        ("le logement social", "Un logement dont le loyer est adapté au revenu."),
    ], notes="« Part sociale » est le mot le plus important de la séance : il explique "
             "toute la différence avec un condo.")

    d.piege('La première confusion',
            "En coopérative, j'achète mon logement.",
            "En coopérative, je deviens membre.",
            "On n'achète pas un logement : on achète une part sociale de la coopérative. "
            "En partant, on récupère sa part — pas la valeur du logement. La coopérative "
            "reste propriétaire. C'est la différence essentielle avec un condo, et elle "
            "surprend beaucoup de gens au moment de déménager.",
            notes="Erreur coûteuse dans la vie réelle. La dire clairement, sans "
                  "dramatiser : la coopérative reste un excellent modèle, ce n'est "
                  "simplement pas un placement.")

    d.piege('La deuxième confusion',
            "Coopérative et HLM, c'est la même chose.",
            "La coopérative se gère elle-même ; le HLM est géré par un office public.",
            "Les deux offrent des loyers plus bas que le marché, ce qui explique la "
            "confusion. Mais le fonctionnement n'a rien à voir : dans un cas, ce sont les "
            "résidents qui décident et qui donnent du temps ; dans l'autre, c'est un "
            "organisme public qui gère, et le loyer suit le revenu.",
            notes="Faire donner le critère par le groupe : « qui décide ? ». C'est la "
                  "question qui sépare les deux.")

    d.pratique('Vérification', 'Vrai ou faux',
               "Répondez sans regarder vos notes.", [
        ("Dans une coopérative, les membres sont locataires et copropriétaires.", "VRAI"),
        ("Le loyer y est généralement plus cher que sur le marché privé.", "FAUX — moins cher, sans profit"),
        ("Les membres participent à la gestion de l'immeuble.", "VRAI"),
        ("Quand un membre quitte son logement, il revend sa part comme un condo.", "FAUX — il récupère sa part sociale"),
        ("Les premières coopératives québécoises datent des années 1970.", "VRAI"),
        ("Être membre n'exige aucune participation personnelle.", "FAUX — du temps est exigé"),
    ], corrige=True,
       notes="Il existe plus de mille coopératives d'habitation au Québec. Le mentionner : "
             "ce n'est pas un modèle marginal.")

    d.billet(
        "Dans quel type de logement habitez-vous, et à qui vous adressez-vous en cas de problème ?",
        exemples=[
            "Une phrase. Vous n'avez pas à écrire votre adresse.",
            "Exemple : « J'habite un logement privé ; je m'adresse à mon propriétaire. »",
        ],
        notes="Fin du bloc C. Rappeler que la séance D1 portera sur les situations qu'on ne "
              "tolère plus — et reprendre les billets de la séance C1.")

    return d.save(dossier)
