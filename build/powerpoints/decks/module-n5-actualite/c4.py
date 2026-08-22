# -*- coding: utf-8 -*-
"""C4 · « Sait-on qui l'a dit ? »
Bloc C « Défi 2 · Ce que les gens ont dit » · couleur ambre · 75 min.
Source : exercices `t2qui` et `t2red`, mini-leçon `t2qui`.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n5-actualite/images/')


def build(dossier):
    d = Deck(
        code='C4', section='ambre',
        titre="« Sait-on qui l'a dit ? »",
        chapeau="La rumeur commence là où le nom s'arrête. « Il paraît que "
                "le feu est parti d'une friteuse » : qui le dit ? Personne. "
                "Cette phrase-là fait circuler une information sans "
                "propriétaire, et personne ne peut ni la vérifier ni la "
                "corriger.",
        duree='75 minutes')

    d.titre(notes="Dernière séance du défi 2. Elle réunit tout : le mot de liaison de "
                  "C2, les pronoms de C3, et la source. Prévoir la seconde moitié de "
                  "la séance pour l'écriture des quatre paroles rapportées.")

    d.objectifs([
        "reconnaître une information qui n'a pas de source ;",
        "employer les formules qui portent un nom ;",
        "distinguer un témoin d'un porte-parole ;",
        "rapporter quatre paroles complètes, avec leur source.",
    ], notes="Le troisième objectif est culturel autant que linguistique : un témoin "
             "parle en son nom, un porte-parole engage un service. La distinction "
             "vaut pour tous les documents officiels que l'élève lira.")

    d.declencheur(
        'Observation', "Une femme parle devant plusieurs micros. "
                       "Qu'est-ce que sa parole engage ?",
        image=IMG + 'porte-parole-micros.jpg',
        pistes=[
            "Si elle est porte-parole, c'est la Ville qui parle par sa bouche.",
            "Le journal écrira « la Ville dit que », pas « madame Untel pense que ».",
            "Un témoin, lui, ne parle que pour lui : il raconte ce qu'il a vu.",
            "Et celui qui répète ce qu'il a entendu ne parle au nom de personne.",
        ],
        notes="La nuance de la deuxième piste a l'air petite et elle est énorme : "
              "c'est elle qui permet de tenir un service responsable de ce qu'il a "
              "dit. Prendre le temps de la faire reformuler par le groupe.")

    d.tableau('Deux colonnes', "Ce qui tient debout, ce qui vient de nulle part",
              ['Ça tient debout', 'Ça vient de nulle part'],
              [["Le Service de sécurité incendie dit que…", "Il paraît que…"],
               ["Une porte-parole de la Ville explique que…", "On dit que…"],
               ["Un témoin raconte qu'il…", "Tout le monde dit que…"],
               ["Selon L'Écho des Cantons…", "D'après ce que j'ai entendu…"],
               ["Les pompiers expliquent que…", "Les gens racontent que…"]],
              cle=0,
              notes="Faire remarquer ce qui sépare les deux colonnes : à gauche, on "
                    "peut aller voir. À droite, il n'y a personne à aller voir. C'est "
                    "le seul critère, et il est vérifiable en une seconde.")

    d.regle("Trois mots séparent une nouvelle d'une rumeur",
            "« Les pompiers disent que… » — et votre récit passe de la "
            "rumeur à la nouvelle.",
            precision="C'est le meilleur rapport effort-résultat de tout le module. "
                      "Les formules vagues ne sont pas interdites — mais quand vous "
                      "les employez, dites-le : « ça, je ne l'ai lu nulle part ».",
            notes="Diapositive à photographier. La deuxième phrase de la précision "
                  "est importante : on n'interdit pas de rapporter une rumeur, on "
                  "demande de la nommer comme telle.")

    d.cartes("Le bon verbe", "Chacun ajoute une couleur", [
        ("dire",
         "Neutre. Le verbe par défaut, et le plus fréquent dans un fait divers."),
        ("expliquer · rappeler",
         "Quand la parole éclaire, ou reprend une chose déjà dite."),
        ("affirmer · annoncer",
         "Quand c'est appuyé, ou quand c'est du neuf."),
        ("demander · raconter",
         "Pour une question, et pour un récit vécu."),
    ], notes="Le conseil à donner : ne pas mettre « affirmer » partout. Un verbe trop "
             "fort donne à la parole un poids que la personne ne lui a pas donné, et "
             "c'est déjà une forme d'opinion.")

    d.pratique('Jugement', "Sait-on de qui vient l'information ?",
               "Pour chaque phrase, dites si on sait qui parle.", [
        ("Le Service de sécurité incendie dit que le feu serait parti de la cuisine.", "on sait qui parle"),
        ("Il paraît que le propriétaire n'avait pas d'assurance.", "on ne sait pas"),
        ("Une porte-parole de la Ville explique que les sacs ont été distribués lundi.", "on sait qui parle"),
        ("Tout le monde dit que la rue est mal drainée depuis des années.", "on ne sait pas"),
        ("Un témoin raconte qu'il a vu trois vélos dans une remorque.", "on sait qui parle"),
        ("On dit que la police ne fait rien pour les vols de vélos.", "on ne sait pas"),
        ("Selon L'Écho des Cantons, onze personnes ont été hébergées.", "on sait qui parle"),
        ("D'après ce que j'ai entendu, ils vont démolir l'immeuble.", "on ne sait pas"),
    ], corrige=True,
       notes="Exercice t2qui de l'activité. Après la correction, demander pour deux "
             "phrases de la colonne « on ne sait pas » comment on pourrait les "
             "réparer. La réponse est toujours la même : aller chercher la source.")

    d.pratique('Écriture', "Quatre paroles à rapporter",
               "Nommez la personne, mettez le verbe au présent, une phrase complète.", [
        ("« L'enquête se poursuit et nous ne pouvons rien confirmer. » — le Service de sécurité incendie",
         "Le Service de sécurité incendie dit que l'enquête se poursuit et qu'il ne peut rien confirmer."),
        ("« Est-ce que la Ville va refaire le fossé au bout de la rue ? » — une résidente",
         "Une résidente demande si la Ville va refaire le fossé au bout de la rue."),
        ("« Notez le numéro de série de votre vélo. » — le Service de police de Sherbrooke",
         "Le Service de police de Sherbrooke demande aux gens de noter le numéro de série de leur vélo."),
        ("« J'ai vu passer trois vélos dans une remorque, vers minuit. » — un commerçant",
         "Un commerçant raconte qu'il a vu passer trois vélos dans une remorque, vers minuit."),
    ], corrige=True,
       notes="Exercice t2red de l'activité. La troisième est la plus difficile : une "
             "consigne à l'impératif se rapporte par « demander à quelqu'un de » plus "
             "l'infinitif. La montrer au tableau avant de laisser écrire.")

    d.piege("Rapporter une information sans sa source",
            "Le feu est parti d'une friteuse.",
            "Le Service de sécurité incendie dit que le feu serait parti de la cuisine.",
            "Sans source, votre phrase devient un fait — et la personne en face la "
            "répétera comme tel. Trois mots de plus, et chacun sait d'où vient "
            "l'information et ce qu'elle vaut.",
            notes="Dernier piège du défi 2 et le plus important du module. Le relier "
                  "au défi 3 : une information sans source et une opinion présentée "
                  "comme un fait produisent le même dégât.")

    d.billet(
        "Écrivez deux phrases : une avec source, une sans. Puis réparez la deuxième.",
        exemples=[
            "La deuxième peut commencer par « il paraît que » ou « on dit que ».",
            "Pour la réparer, ajoutez qui pourrait le dire, et vérifiez-le.",
        ],
        notes="Fin du défi 2. Ramasser : ces billets montrent bien qui a compris que "
              "la source n'est pas un ornement mais une partie de l'information.")

    return d.save(dossier)
