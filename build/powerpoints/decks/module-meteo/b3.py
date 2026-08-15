# -*- coding: utf-8 -*-
"""B3 · Pendant, en, il y a, voilà.
Bloc B · couleur ambre (écriture) · 75 min.
Source : exercices `t1prep` et `t1choix` et leur mini-leçon.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B3', section='ambre',
        titre='Pendant, en, il y a, voilà',
        chapeau="« En dix minutes » ou « pendant dix minutes » ? Les deux existent, et "
                "ils ne disent pas la même chose : l'un mesure le travail fait, l'autre "
                "le temps passé.",
        duree='75 minutes')

    d.titre(notes="Écrire les deux au tableau et demander la différence. Personne ne la "
                  "trouvera tout de suite : c'est une des distinctions les plus fines du "
                  "français.")

    d.objectifs([
        "employer « pendant » pour marquer une durée ;",
        "employer « en » pour un moment ou un temps de réalisation ;",
        "employer « il y a » et « voilà » pour compter vers le passé ;",
        "choisir la bonne préposition selon ce qu'on veut dire.",
    ])

    d.tableau('Analyse', "Quatre prépositions de temps",
              ['La préposition', 'Ce qu\'elle marque', 'Un exemple'],
              [["pendant", "la durée d'une action", "Il a venté pendant toute la nuit."],
               ["en + mois, saison", "un moment de l'année", "L'atelier ferme en juillet."],
               ["il y a", "un point dans le passé", "Le verglas a frappé il y a trois jours."],
               ["voilà", "la même chose, à l'oral", "Diego a commencé voilà deux ans."]],
              cle=0, props=[0.24, 0.28, 0.48],
              notes="« Voilà » est du français parlé courant au Québec. Le signaler : "
                    "les élèves l'entendront et ne le trouveront pas dans leur méthode.")

    d.regle('Pendant ou en',
            "Pendant mesure le temps passé. En mesure le temps qu'il a fallu.",
            precision="« J'ai travaillé pendant dix minutes » : voilà combien de temps "
                      "j'ai travaillé. « J'ai rempli le rapport en dix minutes » : voilà "
                      "combien de temps il m'a fallu pour le finir.",
            notes="Diapo centrale de la séance. Faire produire deux phrases sur la même "
                  "tâche, avec chacune des deux prépositions.")

    d.cartes('Analyse', "Comment choisir entre pendant et en", [
        ("La tâche est-elle finie ?",
         "« En dix minutes » suppose qu'elle est finie. « Pendant dix minutes » ne dit "
         "rien de la fin : peut-être qu'elle continue."),
        ("Y a-t-il un résultat ?",
         "« J'ai fait le rapport en dix minutes » — le rapport existe. « J'ai travaillé "
         "pendant dix minutes » — on ne sait pas ce qui a été fait."),
        ("Le test du verbe",
         "Les verbes de production (faire, écrire, remplir, préparer) vont souvent avec "
         "« en ». Les verbes d'activité (travailler, venter, attendre) avec "
         "« pendant »."),
        ("Le cas facile",
         "Devant « toute la nuit », « toute la journée », « des heures » : c'est "
         "toujours « pendant »."),
    ], notes="La quatrième carte donne le cas simple. Commencer par lui : il couvre la "
             "moitié des emplois.")

    d.regle('Il y a et voilà',
            "Les deux comptent depuis aujourd'hui vers le passé.",
            precision="« Il y a trois jours » et « voilà trois jours » disent la même "
                      "chose. « Il y a » s'écrit et se dit ; « voilà » appartient "
                      "surtout à l'oral. Attention : « dans trois jours » regarde vers "
                      "le futur.",
            notes="Tracer une ligne du temps au tableau avec « aujourd'hui » au milieu. "
                  "Placer « il y a » à gauche et « dans » à droite.")

    d.pratique('Pratique · 1 de 4', "Pendant ou en ?",
               "La tâche est-elle finie, avec un résultat ?", [
        ("Josée remplit son rapport de chantier ___ dix minutes.", "en — le rapport est fini"),
        ("Les rafales souffleront ___ toute la nuit.", "pendant — une durée"),
        ("Diego a préparé le bardeau ___ deux heures.", "en ou pendant, selon le sens"),
        ("Il a venté ___ trois jours sans arrêt.", "pendant — une durée"),
        ("Prisca a fait le trajet ___ une heure et demie.", "en — le trajet est fini"),
    ], corrige=True,
       notes="Le troisième item accepte les deux : « en deux heures » dit qu'il a fini, "
             "« pendant deux heures » dit combien de temps il y a travaillé.")

    d.pratique('Pratique · 2 de 4', "Il y a, voilà, ou dans ?",
               "Vers le passé, ou vers le futur ?", [
        ("Le verglas a coupé le courant ___ trois jours.", "il y a — vers le passé"),
        ("Prisca a obtenu sa carte de compétence ___ six mois.", "voilà ou il y a"),
        ("Diego est arrivé au Québec ___ deux hivers.", "il y a"),
        ("L'avertissement sera levé ___ deux heures.", "dans — vers le futur"),
        ("Le chantier a commencé ___ un mois.", "il y a"),
    ], corrige=True,
       notes="Le quatrième item est le seul au futur. Le faire repérer avant de "
             "corriger : c'est le contraste qui enseigne.")

    d.piege("Le piège de « en » à la place de « pendant »",
            "Les rafales souffleront en toute la nuit.",
            "Les rafales souffleront pendant toute la nuit.",
            "Devant « toute la nuit », « toute la journée », « des heures », c'est "
            "toujours « pendant ». Ces expressions marquent une durée, pas un temps de "
            "réalisation — et « toute la nuit » ne peut pas être un résultat.",
            notes="Cas le plus fréquent et le plus facile à corriger. Faire mémoriser la "
                  "combinaison « pendant toute la… ».")

    d.piege("Le piège de « il y a » et « dans »",
            "Le verglas a coupé le courant dans trois jours.",
            "Le verglas a coupé le courant il y a trois jours.",
            "« Il y a » compte vers le passé, « dans » vers le futur. Les deux sont très "
            "courts et faciles à confondre. Le verbe aide : « a coupé » est au passé, "
            "donc c'est « il y a ».",
            notes="Faire vérifier le temps du verbe avant de choisir. C'est un test "
                  "mécanique et fiable.")

    d.pratique('Pratique · 3 de 4', "Écrivez la phrase",
               "Une préposition par phrase, celle qui est demandée.", [
        ("Avec « pendant » — une durée", "Il a venté pendant toute la nuit."),
        ("Avec « voilà » — un événement passé",
         "Diego a commencé son apprentissage voilà deux ans."),
        ("Avec « en » — un mois ou une saison", "Les couvreurs travaillent peu en janvier."),
        ("Avec « il y a » — un point dans le passé",
         "Le chantier a été interrompu il y a une semaine."),
    ], corrige=True,
       notes="Accepter toute phrase correcte. Vérifier une seule chose : la préposition "
             "demandée est-elle employée juste ?")

    d.pratique('Pratique · 4 de 4', "Choisissez la bonne réponse",
               "Une seule des deux est correcte.", [
        ("Le verglas a coupé le courant… (il y a trois jours / en trois jours)",
         "il y a trois jours"),
        ("Josée remplit son rapport… (pendant dix minutes / en dix minutes)",
         "en dix minutes"),
        ("Prisca a obtenu sa carte… (voilà six mois / pendant six mois)", "voilà six mois"),
        ("Les rafales souffleront… (en toute la nuit / pendant toute la nuit)",
         "pendant toute la nuit"),
        ("On refait rarement une toiture… (en février / pendant février)", "en février"),
        ("Diego est arrivé au Québec… (il y a deux hivers / pendant deux hivers)",
         "il y a deux hivers"),
    ], corrige=True,
       notes="Faire justifier chaque choix. Les six items couvrent les quatre "
             "prépositions et leurs pièges.")

    d.billet(
        "Écrivez quatre phrases, une avec chaque préposition.",
        exemples=[
            "Pendant · en · il y a · voilà.",
            "Toutes doivent parler de travail ou de météo.",
        ],
        notes="Corriger les billets en dehors du cours. Cette distinction demande une "
              "rétroaction individuelle.")

    return d.save(dossier)
