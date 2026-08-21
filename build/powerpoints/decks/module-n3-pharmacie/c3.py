# -*- coding: utf-8 -*-
"""C3 · Mon ordonnance, votre carte.
Bloc C « Défi 2 · Renouveler l'ordonnance » · couleur ambre (écriture) · 75 min.
Source : exercice `t2poss`, mini-leçon `t2poss`.

Savoirs du niveau : les déterminants non quantifiants possessifs.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C3', section='ambre',
        titre='Mon ordonnance, votre carte',
        chapeau="Au comptoir, on ne parle que de choses qui appartiennent à "
                "quelqu'un. Cinq petits mots, et c'est le nom qui suit qui "
                "décide — jamais la personne qui parle.",
        duree='75 minutes')

    d.titre(notes="Séance de langue et d'écriture. Le point est simple mais la faute est "
                  "tenace : beaucoup d'élèves choisissent le petit mot selon leur propre "
                  "genre. Nommer l'erreur tôt.")

    d.objectifs([
        "employer mon, ma et mes correctement ;",
        "comprendre votre et vos dans la bouche du pharmacien ;",
        "savoir pourquoi on dit « mon ordonnance » ;",
        "écrire six phrases justes.",
    ])

    d.declencheur(
        'Mise en situation', "« Votre carte, s'il vous plaît. » Que répondez-vous ?",
        pistes=[
            "« Voici ___ carte. » Quel petit mot ?",
            "Pourquoi le pharmacien dit-il « votre » et vous « ma » ?",
            "Est-ce que ça change si c'est un homme qui parle ?",
        ],
        notes="La dernière question est le cœur de la séance : non, ça ne change pas. "
              "Le faire découvrir plutôt que l'annoncer.")

    d.tableau('Analyse', "Ce qui est à moi, ce qui est à vous",
              ["", "Ce qui est à moi", "Ce qui est à vous"],
              [["masculin", "mon dossier", "votre dossier"],
               ["féminin", "ma carte", "votre carte"],
               ["devant une voyelle", "mon ordonnance", "votre ordonnance"],
               ["pluriel", "mes comprimés", "vos comprimés"]],
              cle=0,
              note="À vous : votre au singulier, vos au pluriel.",
              notes="Diapositive à photographier. Faire lire la colonne du milieu par un "
                    "élève, celle de droite par un autre : c'est le dialogue du comptoir.")

    d.regle("Ce n'est pas vous qui décidez",
            "« ma carte », même pour un homme",
            precision="Le petit mot suit le nom qui vient après, jamais la "
                      "personne qui parle. « Carte » est féminin : c'est « ma "
                      "carte » pour tout le monde. « Dossier » est masculin : "
                      "c'est « mon dossier » pour tout le monde.",
            notes="Diapositive à photographier. Faire dire « ma carte » par les hommes "
                  "du groupe et « mon dossier » par les femmes : le malaise se dissipe "
                  "en riant.")

    d.regle("La seule exception à retenir",
            "« mon ordonnance »",
            precision="Devant une voyelle, « ma » devient « mon » : mon "
                      "ordonnance, mon assurance, mon adresse. Le mot reste "
                      "féminin — on écrit « mon ordonnance est finie » avec un "
                      "e à la fin de « finie ».",
            notes="Diapositive à photographier. L'accord de l'adjectif est un détail "
                  "d'écrit : le montrer sans insister au niveau 3.")

    d.piege('Choix du mot',
            "« votre médicaments »",
            "« vos médicaments »",
            "« Votre » sert pour une seule chose, « vos » pour plusieurs. L'indice est "
            "au bout du nom : s'il y a un s, c'est « vos ». La même règle vaut pour "
            "« ma » et « mes ».",
            notes="Faire chercher le s au bout du nom dans cinq phrases écrites au "
                  "tableau. Le geste devient vite automatique.")

    d.pratique('Application', "Mon, ma, mes, votre ou vos ?",
               "Complétez chaque phrase.", [
        ("Voici ___ carte d'assurance maladie. (elle est à moi)", "ma"),
        ("___ ordonnance est finie depuis samedi. (elle est à moi)", "Mon"),
        ("« ___ nom, s'il vous plaît ? » demande la pharmacienne.", "Votre"),
        ("Je prends ___ comprimés le matin. (ils sont à moi)", "mes"),
        ("« ___ médicaments seront prêts dans vingt minutes. »", "Vos"),
        ("Le pharmacien regarde ___ dossier. (il est à moi)", "mon"),
    ], corrige=True,
       notes="Les six items de l'exercice interactif. Faire nommer chaque fois le genre "
             "et le nombre du nom qui suit : c'est là que se prend la décision.")

    d.pratique('Production', "Le même échange, des deux côtés",
               "En paires : l'un demande, l'autre répond.", [
        ("Le pharmacien demande la carte.", "« Votre carte, s'il vous plaît ? »"),
        ("Le client la donne.", "« Voici ma carte. »"),
        ("Le pharmacien annonce le délai.", "« Vos médicaments seront prêts dans vingt minutes. »"),
        ("Le client demande une précision.", "« Est-ce que mon ordonnance est encore bonne ? »"),
    ], corrige=False,
       notes="Faire changer les rôles au bout de trois minutes. Corriger seulement les "
             "possessifs : le reste du bloc C est déjà acquis.")

    d.billet(
        "Écrivez cinq phrases sur vos affaires : mon, ma, mes.",
        exemples=[
            "Mon dossier, ma carte, mes comprimés…",
            "Ajoutez une phrase avec « mon » devant une voyelle.",
        ],
        notes="Devoir court. Relever seulement le choix du petit mot : c'est la seule "
              "chose que la séance a enseignée.")

    return d.save(dossier)
