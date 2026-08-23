# -*- coding: utf-8 -*-
"""D2 · Ils, si petit que, et « un matelas » en général
Bloc D « Défi 3 » · couleur ambre · 75 min.
Source : exercices `t3ils`, `t3int` et `t3gen`, et leurs mini-leçons.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='D2', section='ambre',
        titre="« Ils » sans nom, et « un matelas » en général",
        chapeau="Trois tournures que la publicité emploie sans arrêt : un "
                "pronom qui ne désigne personne, un degré qui entraîne une "
                "conséquence, et une vérité générale qui vous laisse conclure.",
        duree='75 minutes')

    d.titre(notes="Dernière séance du Défi 3, et la plus chargée du module : trois "
                  "points de langue. Si le temps manque, sacrifier le troisième et "
                  "le reprendre en E1 — mais ne pas sacrifier le premier.")

    d.objectifs([
        "retrouver le référent d'un « ils » qui n'a pas d'antécédent ;",
        "lier deux idées par un degré et sa conséquence ;",
        "distinguer une vérité générale d'un cas particulier ;",
        "voir comment la publicité passe de l'une à l'autre.",
    ], notes="Le quatrième objectif relie les trois points : c'est le message "
             "implicite dans sa forme la plus pure.")

    d.declencheur(
        'Observation', "Qui, ils ?",
        pistes=[
            "« Ils me l'ont envoyée. » Qui ?",
            "« Ils ont encore augmenté les prix. » Qui ?",
            "« Ils disent que c'est le meilleur produit. » Qui ?",
            "Laquelle des trois n'a aucune réponse possible ?",
        ],
        notes="La troisième n'en a aucune, et c'est le cas dangereux : « ils » sert "
              "à donner une caution qui n'existe pas. Laisser le groupe le trouver.")

    d.tableau('Analyse', "Trois questions qui trouvent le référent",
              ['La question', 'Ce qu\'elle donne'],
              [["De quoi parle la phrase ?", "le domaine : un produit, une loi, un prix"],
               ["Qui pose ce geste ?", "une entreprise, un organisme, une autorité"],
               ["Qui a été nommé avant ?", "parfois rien, et c'est une réponse"]],
              cle=0,
              note="Le référent est presque toujours un groupe, jamais une personne.",
              notes="Diapositive à photographier. La réponse vient presque toujours à "
                    "la deuxième question : le geste désigne son auteur.")

    d.pratique('Pratique', "Qui, ils ?",
               "Écrivez qui le pronom désigne, en un groupe de mots.", [
        ("J'ai reçu la trottinette. Ils me l'ont envoyée.", "l'entreprise qui la vend"),
        ("Le tarif a monté. Ils ont changé les conditions.", "le centre, l'entreprise"),
        ("Ils interdisent la publicité aux moins de treize ans.", "la loi, le gouvernement du Québec"),
        ("Ils reçoivent les plaintes du public.", "Normes de la publicité"),
        ("Ils vérifient la langue des enseignes.", "l'Office québécois de la langue française"),
        ("Ils disent que c'est le meilleur produit.", "personne : aucun nom n'existe"),
    ], corrige=True,
       notes="Exercice `t3ils` du module. Le dernier est le seul qui compte vraiment : "
             "une caution qu'on ne peut pas nommer n'est pas une caution.")

    d.regle("Le degré entraîne une conséquence",
            "Le caractère est si petit qu'on ne le lit pas. La voix va "
            "tellement vite qu'on ne comprend rien.",
            precision="Trois modèles : « si » ou « tellement » + que, suivi de "
                      "l'indicatif ; « assez » ou « suffisamment » + pour que, suivi "
                      "du subjonctif ; « trop » + pour que, suivi du subjonctif aussi. "
                      "Devant un nom, c'est « tellement de », jamais « si de ».",
            notes="Diapositive à photographier. Ces tournures décrivent exactement les "
                  "procédés du module : trop petit, trop rapide, tellement de "
                  "conditions.")

    d.cartes('Analyse', "Trois modèles, trois nuances", [
        ("si … que + indicatif", "Le caractère est si petit qu'on ne le lit pas."),
        ("assez … pour que + subjonctif", "Le prix est assez bas pour qu'on signe sans réfléchir."),
        ("trop … pour que + subjonctif", "L'écriture est trop fine pour que je la lise."),
        ("tellement de … que", "Il y a tellement de conditions que personne ne les lit."),
    ], cols=1,
       notes="Après « que » tout court : indicatif. Après « pour que » : subjonctif, "
             "toujours. C'est la seule chose à retenir de ce point.")

    d.tableau('Analyse', "Toute la catégorie, ou un cas précis ?",
              ['La phrase', 'Ce dont elle parle'],
              [["Un matelas, ça dure dix ans.", "toute la catégorie"],
               ["Il y a un matelas à 40 %.", "un cas précis"],
               ["La publicité, ça travaille.", "toute la catégorie"],
               ["Cet abonnement-là vous engage.", "un cas précis"]],
              cle=0,
              note="La reprise par « ça » est le signe le plus sûr du sens général.",
              notes="Diapositive à photographier. Le test : ajoutez « en général » à "
                    "la phrase. Si elle tient, c'est du général.")

    d.piege('Lecture',
            "« Un bon matelas, ça change une vie » promet quelque chose",
            "cette phrase ne parle pas du matelas de l'annonce",
            "La publicité affirme au général — une vérité qu'on ne peut pas "
            "contester — puis vous laisse appliquer cette vérité au produit "
            "précis qu'elle vend, ce qu'elle n'a jamais promis. Le glissement "
            "se fait dans votre tête, et il ne laisse aucune trace dans le "
            "texte.",
            notes="C'est le message implicite dans sa forme la plus pure, et c'est la "
                  "dernière chose que le module apprend. Prendre le temps.")

    d.billet(
        "Écrivez deux phrases sur votre annonce : une avec « si… que », une au sens général.",
        exemples=[
            "« Le caractère est si petit que… »",
            "« Un abonnement, ça… »",
        ],
        notes="Devoir de production. Ces deux phrases sont exactement celles qui "
              "manquent aux exposés de E1 : les élèves décrivent, et ne concluent pas.")

    return d.save(dossier)
