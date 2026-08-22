# -*- coding: utf-8 -*-
"""C4 · Le jour où, et il faut que
Bloc C « Défi 2 · Les papiers du chantier » · couleur teal · 75 min.
Source : exercices `t2ou` et `t2subj`, et leurs mini-leçons. Savoirs du
programme : employer des phrases subordonnées relatives avec le pronom relatif
« où », complément de lieu ou de temps ; employer obligatoirement le subjonctif
présent après quelques verbes introducteurs usuels + que.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C4', section='teal',
        titre="Le jour où, et il faut que",
        chapeau="Deux tournures qui font tenir un texte long : l'une colle "
                "deux phrases en une, l'autre transforme un ordre en "
                "demande.",
        duree='75 minutes')

    d.titre(notes="Dernière séance du bloc C, et elle porte deux points. Quarante "
                  "minutes pour « où », trente pour le subjonctif : le second est "
                  "connu de la plupart, mais mal employé à l'écrit.")

    d.objectifs([
        "réunir deux phrases avec « où » pour un lieu ;",
        "employer « où » pour un moment : le jour où, l'année où ;",
        "employer le subjonctif après il faut que, j'aimerais que ;",
        "choisir entre « de » + infinitif et « que » + subjonctif.",
    ], notes="Le quatrième objectif est celui qui reste flou chez la plupart des "
             "élèves du niveau 6. La règle est pourtant simple : même personne des "
             "deux côtés, infinitif.")

    d.declencheur(
        'Observation', "« Le mur nord, où la fissure a été relevée, présente dix-neuf pour cent. » Combien de phrases là-dedans ?",
        pistes=[
            "Peux-tu la couper en deux ?",
            "Quel mot fait la soudure ?",
            "Pourquoi un rapport écrit-il ainsi plutôt qu'en deux phrases ?",
        ],
        notes="Faire couper la phrase au tableau. La réponse à la troisième question : "
              "sans « où », le rapport répéterait le nom du mur toutes les deux "
              "lignes.")

    d.tableau('Analyse', "« où » pour un lieu, « où » pour un moment",
              ['Ce qu\'il reprend', 'Un exemple'],
              [["un mur", "le mur nord, où la fissure a été relevée"],
               ["un coin", "le coin du sous-sol où le puisard se trouve"],
               ["un jour", "le jour où on a ouvert le plancher"],
               ["une année", "l'année où la maison fut construite"]],
              cle=0,
              note="On n'écrit jamais « le jour que » : ça s'entend, ça ne s'écrit pas.",
              notes="Diapositive à photographier. L'emploi temporel est le plus "
                    "fréquent à l'écrit, et c'est celui que le niveau 6 ajoute.")

    d.tableau('Analyse', "La virgule change le sens",
              ['La phrase', 'Ce qu\'elle dit'],
              [["le mur où la fissure est", "lequel des murs : il y en a plusieurs"],
               ["le mur nord, où elle est,", "un renseignement sur un mur déjà nommé"],
               ["le jour où le permis arrive", "lequel des jours"],
               ["le 18, où il est arrivé,", "un ajout sur une date déjà nommée"]],
              cle=0,
              note="Les virgules vont par deux, ou pas du tout. Une seule est toujours une erreur.",
              notes="Diapositive à photographier. Le point est fin, mais il se corrige "
                    "en une minute et il se voit dans tous les textes du groupe.")

    d.pratique('Pratique', "Réunir avec « où »",
               "Faites une seule phrase.", [
        ("Le mur nord présente 19 %. La fissure a été relevée dans ce mur.",
         "Le mur nord, où la fissure a été relevée, présente 19 %."),
        ("Tout a changé ce jour-là. On a ouvert le plancher ce jour-là.",
         "Le jour où on a ouvert le plancher, tout a changé."),
        ("La maison fut construite en 1961. On ne posait pas de membrane cette année-là.",
         "L'année où la maison fut construite, on ne posait pas de membrane."),
        ("Le coin est le plus humide. Le puisard se trouve dans ce coin.",
         "Le coin où le puisard se trouve est le plus humide."),
    ], corrige=True,
       notes="Faire écrire la phrase entière, pas seulement le mot manquant. C'est la "
             "soudure qu'on travaille, et elle demande de relire la phrase complète.")

    d.tableau('Analyse', "Les verbes qui commandent le subjonctif",
              ['La famille', 'Les verbes'],
              [["la nécessité", "il faut que, il est important que"],
               ["la volonté", "je veux que, j'exige que, je demande que"],
               ["le souhait", "je souhaite que, j'aimerais que"],
               ["l'attente", "avant que, en attendant que"]],
              cle=0,
              note="Cinq irréguliers suffisent : sois, aie, fasse, aille, puisse.",
              notes="Diapositive à photographier. Signaler que « après que » ne "
                    "commande pas le subjonctif, même si presque tout le monde le "
                    "dit ainsi.")

    d.regle("La langue de la demande écrite",
            "« Ajoutez une phrase » est un ordre ; « j'aimerais que vous ajoutiez une phrase » est une demande.",
            precision="La différence tient au verbe qui suit « que », et ce verbe est "
                      "au subjonctif. Ce n'est pas une politesse décorative : dans un "
                      "courriel à quelqu'un que vous payez, l'impératif se lit comme "
                      "un reproche, et le subjonctif comme une demande ferme et "
                      "normale.",
            notes="Diapositive à photographier. Faire le lien avec E2 : le courriel de "
                  "la production écrite en demande un.")

    d.pratique('Pratique', "Mettre au subjonctif",
               "Complétez avec le verbe entre parenthèses.", [
        ("Il faut que le mur ___ (être) sec avant qu'on referme.", "soit"),
        ("J'aimerais que vous ___ (écrire) cette phrase dans la soumission.", "écriviez"),
        ("Kettly souhaite que Doïna ___ (avoir) une réserve.", "ait"),
        ("Il est important que nous ___ (faire) vérifier la licence.", "fassions"),
        ("Fernand demande que Doïna lui ___ (répondre) avant le 15.", "réponde"),
        ("Il faudrait que vous ___ (pouvoir) commencer avant les pluies.", "puissiez"),
    ], corrige=True,
       notes="Faire remarquer que quatre des six sont des irréguliers de la liste : "
             "c'est normal, ce sont les verbes qu'on emploie le plus.")

    d.billet(
        "Écris une demande que tu ferais à un entrepreneur, avec « j'aimerais que ».",
        exemples=[
            "Une phrase.",
            "Demande une seule chose, et donne une date.",
        ],
        notes="Trois minutes. Fin du bloc C. Annoncer le bloc D : on ouvre le "
              "plancher, et ce qu'on trouve n'était pas dans le prix.")

    return d.save(dossier)
