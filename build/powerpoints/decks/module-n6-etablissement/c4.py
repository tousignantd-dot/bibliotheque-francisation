# -*- coding: utf-8 -*-
"""C4 · Le temps qu'on écrit et qu'on ne parle pas
Bloc C « Défi 2 » · couleur ambre · 75 min. Passé simple, en reconnaissance.
Source : exercice `t2ps`, sa mini-leçon, et le vocabulaire du défi 2.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C4', section='ambre',
        titre="Le temps qu'on écrit et qu'on ne parle pas",
        chapeau="« Le centre ouvrit ses portes en 1968. » Personne ne dit "
                "cela à voix haute, et vous le lirez sur la première page de "
                "presque toutes les brochures.",
        duree='75 minutes')

    d.titre(notes="Séance courte en règles, longue en lecture. Le programme ne "
                  "demande que de reconnaître et d'associer : ne jamais faire écrire "
                  "un passé simple, même à un élève rapide qui le demande.")

    d.objectifs([
        "reconnaître un verbe courant au passé simple, à la 3e personne ;",
        "associer une forme au passé simple à son passé composé ;",
        "continuer à lire sans s'arrêter sur ce temps ;",
        "réemployer les trois mots des écrits officiels.",
    ], notes="Le troisième objectif est le vrai : le passé simple porte le décor "
             "d'un document, jamais l'information qui oblige.")

    d.declencheur(
        'Observation', "Avez-vous déjà lu une phrase que personne ne dit ?",
        pistes=[
            "« Il ouvrit », « ils décidèrent », « ce fut »…",
            "Où avez-vous vu ces formes ?",
            "Est-ce que ça vous a arrêté dans votre lecture ?",
        ],
        notes="Beaucoup d'élèves l'ont rencontré dans un livre pour enfants ou dans "
              "un manuel. Le nommer enfin soulage : ils croyaient avoir mal lu.")

    d.tableau('Analyse', "Trois familles de terminaisons",
              ['Les verbes en', 'Ce que ça donne'],
              [["-er", "il ferma, ils fermèrent"],
               ["-ir et beaucoup d'autres", "il ouvrit, ils ouvrirent"],
               ["une troisième famille", "il reçut, ils reçurent"]],
              cle=0,
              note="Vous ne le rencontrerez presque jamais ailleurs qu'à la 3e personne : un historique parle de gens absents.",
              notes="Diapositive à photographier. Ne pas donner de tableau de "
                    "conjugaison complet : ce serait faire écrire ce que le programme "
                    "demande seulement de reconnaître.")

    d.tableau('Analyse', "Les quatre qui reviennent partout",
              ['On lit', 'On dirait'],
              [["il fut", "il a été"],
               ["il eut", "il a eu"],
               ["il fit", "il a fait"],
               ["il devint", "il est devenu"]],
              cle=0,
              note="Ces quatre-là suffisent à comprendre la moitié des historiques d'établissement.",
              notes="Diapositive à photographier. Les faire répéter en chœur, deux "
                    "fois. C'est la seule mémorisation demandée de toute la séance.")

    d.regle("Traduisez dans votre tête et continuez",
            "Le passé simple porte le décor d'un document, jamais l'information qui vous oblige.",
            precision="Une brochure raconte l'histoire du centre en passé simple, "
                      "puis donne ses conditions au présent et ses obligations au "
                      "futur. Le passage au présent est le signal : c'est là que ça "
                      "vous concerne.",
            notes="Diapositive à photographier. Faire vérifier dans la description du "
                  "programme de C1 : l'historique est au passé simple, les voies "
                  "d'admission au présent. Le groupe le voit d'un coup.")

    d.pratique('Pratique', "Que dirait-on à voix haute ?",
               "Récrivez chaque forme au passé composé.", [
        ("Le centre ouvrit ses portes en 1968.", "a ouvert"),
        ("Les commissaires décidèrent d'agrandir.", "ont décidé"),
        ("L'école devint un centre d'éducation des adultes.", "est devenue"),
        ("Le pavillon reçut ses premiers élèves.", "a reçu"),
        ("Les travaux durèrent deux ans.", "ont duré"),
        ("On y fit une bibliothèque.", "a fait"),
        ("Ce fut le premier du genre dans la région.", "ça a été"),
    ], corrige=True, cols=2,
       notes="Attention au troisième : « devenir » prend l'auxiliaire être et "
             "s'accorde. C'est le seul du lot, et c'est le plus utile.")

    d.piege('Écriture',
            "essayer d'en écrire un dans un courriel",
            "écrire au passé composé, comme tout le monde",
            "Un passé simple dans un courriel au secrétariat serait déplacé, "
            "et souvent faux. Même les gens qui écrivent les brochures "
            "n'écrivent pas ainsi leurs propres courriels. Le programme "
            "demande de le reconnaître, jamais de le produire.",
            notes="Le dire clairement aux élèves rapides, qui voudront l'employer "
                  "pour bien faire. Leur donner autre chose à faire : les connecteurs "
                  "de point de vue de D2, qui les serviront vraiment.")

    d.vocabulaire('Vocabulaire', "Les trois mots des écrits officiels", [
        ("un avis officiel", "Un écrit qui informe d'une décision et qui ne se discute pas au comptoir."),
        ("une admission conditionnelle", "Une acceptation qui ne tient que si une condition est remplie avant une date."),
        ("un encadré", "La partie d'un document entourée d'un trait, où l'on met ce qu'il ne faut pas manquer."),
    ], notes="Trois mots seulement, mais ce sont ceux de la production écrite de E2. "
             "Les faire employer dans une phrase orale avant de terminer.")

    d.billet(
        "Résume en trois phrases ce que ton avis te demande.",
        exemples=[
            "Phrase 1 : ce que le centre a décidé.",
            "Phrase 2 : la condition. Phrase 3 : la date.",
        ],
        notes="Cinq minutes. C'est le brouillon du premier paragraphe du courriel de "
              "E2. Le dire, pour que le travail ne paraisse pas gratuit.")

    return d.save(dossier)
