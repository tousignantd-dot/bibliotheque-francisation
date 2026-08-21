# -*- coding: utf-8 -*-
"""B3 · En huit heures, pour une semaine
Bloc B « Défi 1 » · couleur ambre · 75 min. Écriture et grammaire.
Source : exercice `t1dur` et sa mini-leçon (dire la durée).
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B3', section='ambre',
        titre="En huit heures, pour une semaine",
        chapeau="Trois façons de parler du temps, et elles ne disent pas la "
                "même chose : « en huit heures » dit combien de temps ça "
                "prend, « pour une semaine » dit combien de temps on reste, "
                "« depuis trois ans » dit depuis quand ça dure.",
        duree='75 minutes')

    d.titre(notes="Séance de grammaire. La confusion entre « en », « pour », « dans » "
                  "et « depuis » est universelle et elle a des conséquences réelles au "
                  "comptoir : « je pars dans une semaine » et « je pars pour une "
                  "semaine » font vendre deux billets différents.")

    d.objectifs([
        "dire une durée de trajet avec « en » ;",
        "dire une durée de séjour avec « pour » ;",
        "dire un moment futur avec « dans » ;",
        "dire depuis quand une situation dure avec « depuis ».",
    ], notes="Les quatre objectifs sont quatre prépositions et une seule idée : de "
             "quel temps parle-t-on ? Poser la question ainsi à chaque exemple.")

    d.regle("Quatre mots, quatre questions",
            "« En » : combien de temps ça prend. « Pour » : combien de temps "
            "on reste. « Dans » : à partir de maintenant. « Depuis » : "
            "depuis quel moment.",
            precision="La phrase ne dit pas laquelle choisir : c'est la question "
                      "qu'on se pose qui la choisit.",
            notes="Diapositive à photographier. Faire poser la question à voix haute "
                  "avant chaque réponse dans les exercices : « je demande quoi ? ». "
                  "L'automatisme vient de là, pas de la liste.")

    d.tableau('Quatre phrases', "La même semaine, quatre sens",
              ['La phrase', 'Ce que ça veut dire'],
              [["Je pars dans une semaine", "Le départ est le 28"],
               ["Je pars pour une semaine", "Je reviens le 4"],
               ["J'y vais en huit heures", "Le trajet dure huit heures"],
               ["Je suis ici depuis trois ans", "Je suis arrivée en 2023"]],
              cle=1,
              notes="Faire compléter la colonne de droite avec de vraies dates. Les deux "
                    "premières lignes sont celles qui coûtent cher : le préposé vend "
                    "selon ce qu'on lui dit.")

    d.cartes("Deux erreurs qui se paient", "Au comptoir, elles changent le billet", [
        ("« Je pars dans une semaine »",
         "Le préposé cherche un départ le 28 septembre."),
        ("« Je pars pour une semaine »",
         "Le préposé cherche un retour le 4 octobre."),
        ("« En huit heures »",
         "C'est la durée du trajet, pas l'heure du départ."),
        ("« À huit heures »",
         "Là, c'est l'heure du départ. Un seul mot de différence."),
    ], notes="La dernière paire — « en » et « à » — est la plus fine et la plus utile. "
             "La faire répéter avec de vraies heures : « je pars à sept heures et "
             "j'arrive en huit heures ».")

    d.pratique('Choix', "Complétez avec en, pour, dans ou depuis",
               "À l'oral, puis à l'écrit.", [
        ("L'autocar fait le trajet … huit heures.", "en"),
        ("Je réserve le gîte … six nuits.", "pour"),
        ("Nous partons … trois jours, le lundi 28.", "dans"),
        ("Elle habite Montréal … trois ans.", "depuis"),
        ("Le train met vingt heures … se rendre à Halifax.", "pour — attention : ici « pour » introduit le but"),
        ("Je serai à Rimouski … le 4 octobre.", "jusqu'au — aucune des quatre ne convient"),
    ], corrige=True,
       notes="Les deux dernières lignes sortent volontairement du cadre : elles "
             "apprennent qu'une liste de quatre mots ne couvre pas tout le français, et "
             "que « jusqu'à » existe. Ne pas les traiter comme des pièges à punir.")

    d.tableau("Dire l'heure et la durée", "Deux systèmes qui cohabitent",
              ["On dit", "Quand"],
              [["sept heures", "l'heure d'un départ"],
               ["huit heures dix", "une durée, avec les minutes"],
               ["vingt minutes avant", "un décalage par rapport à une heure"],
               ["six nuits", "un séjour se compte en nuits"]],
              cle=1,
              notes="La dernière ligne surprend et elle est vraie de tout "
                    "l'hébergement : un gîte, un hôtel et un camping facturent des "
                    "nuits, pas des jours. Thuy reste « six nuits » et sept jours.")

    d.piege("Compter son séjour en jours devant un hôtelier",
            "Je reste sept jours.",
            "Je reste six nuits, du 28 au 4.",
            "L'hébergement se compte en nuits partout au Québec. « Sept jours » "
            "oblige l'hôtelier à redemander les dates, et une erreur d'une nuit "
            "arrive vite quand chacun compte à sa façon.",
            notes="Faire calculer au groupe : du lundi 28 au dimanche 4, combien de "
                  "nuits ? La réponse — six — n'est évidente pour personne du premier "
                  "coup, et c'est justement pour ça qu'on donne les dates.")

    d.billet(
        "Écrivez deux phrases sur votre voyage : une avec « en », une avec « pour ».",
        exemples=[
            "La première dit la durée du trajet, la seconde la durée du séjour.",
            "Ajoutez les dates entre parenthèses pour vérifier votre compte de nuits.",
        ],
        notes="Ramasser les billets. Le compte de nuits est ce qu'il faut vérifier : "
              "c'est là que les erreurs se voient, et elles se corrigent en une ligne.")

    return d.save(dossier)
