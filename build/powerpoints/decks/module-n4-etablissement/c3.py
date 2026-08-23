# -*- coding: utf-8 -*-
"""C3 · Lui et leur : remplacer la personne
Bloc C « Défi 2 · Les messages qu'on me laisse » · couleur ambre · 75 min.
Source du module : exercice `t2lui` et sa mini-leçon.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C3', section='ambre',
        titre="Lui et leur : remplacer la personne",
        chapeau="Deux petits mots qui évitent de répéter « madame "
                "Sansregret » quatre fois dans le même message. C'est la "
                "construction avec « à » qui les commande, et rien d'autre.",
        duree='75 minutes')

    d.titre(notes="Séance de grammaire. Commencer par lire à voix haute un court "
                  "paragraphe où le nom est répété cinq fois, puis le même avec les "
                  "pronoms. Le groupe entend tout de suite lequel des deux sonne "
                  "français.")

    d.objectifs([
        "reconnaître la construction avec « à » qui appelle lui ou leur ;",
        "employer « lui » pour une personne, homme ou femme ;",
        "employer « leur » pour plusieurs, sans jamais de « s » ;",
        "placer le pronom devant le verbe, sauf à l'impératif positif.",
    ], notes="Le deuxième objectif est celui qui surprend. « Lui » ne veut pas dire « un "
             "homme » : c'est la découverte de la séance, et elle se fait en trente "
             "secondes.")

    d.regle("Lui vaut pour une personne, quelle qu'elle soit",
            "Je parle à Fabien : je lui parle. Je parle à Murielle : je lui "
            "parle.",
            precision="Un seul mot pour les deux. « Lui » ne dit rien du "
                      "genre de la personne.",
            notes="Diapositive à photographier. Signaler qu'il existe un autre « lui », "
                  "celui de « avec lui » et « chez lui », qui désigne un homme : ce "
                  "n'est pas le même mot, et il vient après une préposition.")

    d.tableau('Les verbes qui appellent lui et leur', "Tous avec « à »",
              ['Le verbe', 'La phrase'],
              [["parler à", "Je lui parle après le cours."],
               ["téléphoner à", "Elle lui téléphone au poste 224."],
               ["écrire à", "Je lui écris ce soir."],
               ["remettre à", "Je lui remets la note jeudi."],
               ["demander à", "Je vais lui demander le numéro."],
               ["répondre à", "L'enseignant leur répond après le cours."]],
              cle=1,
              notes="Faire chercher le « à » dans chaque verbe : c'est le seul indice "
                    "fiable. Les élèves qui apprennent la liste par cœur oublient ; "
                    "ceux qui cherchent le « à » ne se trompent plus.")

    d.cartes("Leur, sans « s »", "Ne pas confondre deux mots identiques", [
        ("Le pronom : leur",
         "Devant un verbe. Il ne prend jamais de « s » : il leur répond."),
        ("Le déterminant : leur, leurs",
         "Devant un nom. Il s'accorde : leur papier, leurs papiers."),
        ("Le test en une seconde",
         "Le mot qui suit est-il un verbe ? Alors jamais de « s »."),
        ("La faute type",
         "« il leurs répond » — le « s » n'a rien à faire là."),
    ], notes="Écrire au tableau « il leur répond » et « leurs papiers » côte à côte. La "
             "différence se voit d'un coup d'œil, et elle se retient par le mot qui "
             "suit, pas par une règle.")

    d.regle("Le pronom passe devant le verbe",
            "Je lui téléphone. Je lui ai téléphoné. Je vais lui téléphoner.",
            precision="Au passé composé, devant l'auxiliaire — jamais entre "
                      "l'auxiliaire et le participe.",
            notes="« J'ai lui parlé » est la faute qui reste le plus longtemps. La "
                  "corriger par reformulation : répéter la phrase juste, et continuer.")

    d.pratique('Complétez', "Lui ou leur ?",
               "Une seule forme convient.", [
        ("Madame Sansregret a téléphoné : elle ___ a laissé un message.", "lui"),
        ("Nourhane écrit à monsieur Corriveau : elle ___ remet sa note.", "lui"),
        ("Les élèves ont des questions : l'enseignant ___ répond.", "leur"),
        ("Wilner connaît le numéro : je vais ___ demander.", "lui"),
        ("Le secrétariat écrit aux parents : il ___ envoie un avis.", "leur"),
        ("Si vous ne comprenez pas, rappelez-___ avant midi.", "lui"),
    ], corrige=True,
       notes="La deuxième et la quatrième vérifient que « lui » vaut pour un homme "
             "comme pour une femme. La sixième vérifie l'impératif : le pronom passe "
             "derrière, avec un trait d'union.")

    d.pratique('Remplacez', "La phrase longue, puis la courte",
               "Remplacez le nom par le pronom.", [
        ("Elle téléphone à madame Sansregret.", "Elle lui téléphone."),
        ("Elle remet la note à monsieur Corriveau.", "Elle lui remet la note."),
        ("L'enseignant répond aux élèves.", "Il leur répond."),
        ("Le secrétariat écrit aux parents.", "Il leur écrit."),
        ("Je demande le numéro à Wilner.", "Je lui demande le numéro."),
        ("J'ai parlé à la secrétaire ce matin.", "Je lui ai parlé ce matin."),
    ], corrige=True,
       notes="La dernière est au passé composé et c'est là que le pronom se déplace mal. "
             "La faire écrire au tableau, puis effacer et refaire dire de mémoire.")

    d.piege("Placer le pronom après le verbe",
            "J'ai lui parlé hier matin.",
            "Je lui ai parlé hier matin.",
            "Le pronom passe devant l'auxiliaire, jamais entre l'auxiliaire et "
            "le participe. La seule exception est l'impératif positif : "
            "« parlez-lui ».",
            notes="Faire relire les six phrases de l'exercice précédent en insistant "
                  "sur la place du pronom. C'est un déplacement, pas une règle : le "
                  "montrer avec la main au tableau fonctionne mieux qu'une explication.")

    d.tableau('Dans les messages du module', "Six phrases réelles",
              ['Qui', 'La phrase'],
              [["une personne", "Elle lui a laissé un message ce matin."],
               ["une personne", "Je lui remets ma note jeudi, en classe."],
               ["plusieurs", "L'enseignant leur répond après le cours."],
               ["plusieurs", "Le secrétariat leur envoie un avis chaque session."],
               ["avec deux verbes", "Je vais lui demander le numéro à la pause."],
               ["à l'impératif", "Rappelez-lui avant midi, s'il vous plaît."]],
              cle=1,
              notes="Faire dire les six à voix haute, en chaîne, sans pause. C'est un "
                    "exercice de fluidité : le pronom doit se coller au verbe sans "
                    "qu'on y pense.")

    d.billet(
        "Écrivez deux phrases : une avec « lui », une avec « leur », à "
        "propos de votre centre.",
        exemples=[
            "Vérifiez que le verbe se construit avec « à ».",
            "Pas de « s » sur « leur » devant un verbe.",
        ],
        notes="Ramasser. Le « s » fautif se voit d'un coup d'œil ; l'erreur de place, "
              "un peu moins. Marquer les deux et rendre les billets en C4.")

    return d.save(dossier)
