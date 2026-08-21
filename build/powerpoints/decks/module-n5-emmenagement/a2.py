# -*- coding: utf-8 -*-
"""A2 · Déménagement ou camion.
Bloc A « Je découvre » · couleur indigo · graphie-phonie · 75 min.
Source : exercice `prPhon` et sa mini-leçon.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A2', section='indigo',
        titre="Déménagement ou camion ?",
        chapeau="Deux voyelles qui sortent par le nez, et une seule chose qui "
                "les sépare : les lèvres.",
        duree='75 minutes')

    d.titre(notes="Séance de prononciation. Le local doit être silencieux : ces deux sons "
                  "se distinguent mal si le groupe parle en même temps. Prévoir un miroir "
                  "de poche, ou faire travailler par deux, face à face.")

    d.objectifs([
        "entendre la différence entre le son « an » et le son « on » ;",
        "produire les deux sons en contrôlant ses lèvres ;",
        "lire an, am, en, em comme le son « an », et on, om comme le son « on » ;",
        "savoir que le nez se ferme devant un n ou un m double.",
    ])

    d.regle("Ce sont les lèvres qui décident",
            "Lèvres immobiles : le son « an ». Lèvres arrondies et avancées : le son « on ».",
            precision="L'air sort par le nez dans les deux cas — ce n'est donc pas le nez "
                      "qui fait la différence, contrairement à ce que les élèves croient "
                      "presque tous.",
            notes="Faire le geste soi-même, en exagérant. Demander au groupe de le refaire "
                  "en silence avant de produire le son.")

    d.tableau('Les deux sons', "Ce qu'on écrit, ce qu'on entend",
              ['On écrit', 'On entend', 'Exemples'],
              [["an · am · en · em", "le son « an »", "appartement · chambre · quarante · pendant"],
               ["on · om", "le son « on »", "camion · salon · plafond · maison · nom"]],
              cle=1,
              note="Les finales en -ment se disent toujours « an », jamais « in ».",
              notes="La ligne des finales en -ment est celle qui corrige le plus d'erreurs "
                    "d'un coup : appartement, déménagement, seulement, justement.")

    d.piege("Dire « appartemin »",
            "un appartemin, un déménagemin",
            "un appartement, un déménagement",
            "La finale -ment se prononce « man », bouche ouverte. C'est l'erreur la plus "
            "fréquente à ce niveau, et elle s'entend beaucoup parce que ces mots "
            "reviennent sans arrêt dans la situation.",
            notes="Faire répéter la série : appartement, déménagement, seulement, "
                  "justement, également. Cinq mots, trois fois.")

    d.cartes("Le test du doigt", "Une vérification qu'on peut faire seul", [
        ("Un doigt devant la bouche",
         "Dites « déménagement » : les lèvres ne bougent presque pas."),
        ("Le même doigt",
         "Dites « camion » : les lèvres avancent et touchent le doigt."),
        ("Si rien ne bouge",
         "Vous avez dit le son « an » deux fois. Recommencez en exagérant l'arrondi."),
        ("Devant un miroir",
         "Une seule fois suffit : ensuite, le doigt remplace le miroir."),
    ], notes="Faire faire le test à tout le groupe en même temps, en silence. C'est "
             "l'exercice le plus efficace de la séance, et il dure deux minutes.")

    d.regle("Un n ou un m double, et le nez se ferme",
            "bon / bonne · an / année · homme, personne, bonne",
            precision="Dès qu'un n ou un m est suivi d'une voyelle, la voyelle d'avant "
                      "redevient ordinaire. C'est pourquoi « an » et « année » ne se "
                      "ressemblent pas à l'oreille.",
            notes="Beaucoup d'élèves nasalisent « bonne » et « personne ». Faire opposer "
                  "les paires : bon/bonne, an/année, ton/tonne.")

    d.pratique('Écoute', "Quel son entendez-vous ?",
               "L'enseignante dit le mot ; le groupe lève une main pour le son « an », deux "
               "pour le son « on ».", [
        ("déménagement", "le son « an »"),
        ("camion", "le son « on »"),
        ("appartement", "le son « an »"),
        ("salon", "le son « on »"),
        ("chambre", "le son « an »"),
        ("plafond", "le son « on »"),
        ("quarante", "le son « an »"),
        ("maison", "le son « on »"),
    ], corrige=True,
       notes="Ce sont exactement les huit mots de l'exercice prPhon du module. Les faire "
             "d'abord ici à l'oral : les élèves arriveront à l'écran en terrain connu.")

    d.pratique('Production', "Les deux sons dans la même phrase",
               "Chacun lit une phrase à voix haute. Le groupe corrige les lèvres, "
               "pas le sens.", [
        ("Le camion du déménagement arrive à huit heures.", "« on » puis « an »"),
        ("Mon appartement a un grand salon.", "« an » puis « on »"),
        ("Il y a une tache au plafond de la chambre.", "« on » puis « an »"),
        ("Quarante centimètres, dans le coin du salon.", "« an » puis « on »"),
        ("Pendant que nous montions, mon garçon dormait.", "« an » puis « on »"),
        ("La maison est grande, l'appartement est petit.", "« on » puis « an »"),
    ], corrige=True,
       notes="Faire passer tout le monde. Corriger d'un geste des lèvres plutôt que d'un "
             "mot : c'est plus rapide et moins gênant.")

    d.billet(
        "Trouvez trois mots de votre quotidien avec le son de « camion ».",
        exemples=[
            "Un objet, un lieu, une personne : le salon, un bonbon, mon garçon.",
            "Dites-les à voix haute en vérifiant vos lèvres avec un doigt.",
        ],
        notes="Le billet fait chercher hors du vocabulaire du module, ce qui est le but : "
              "le son doit sortir de la situation.")

    return d.save(dossier)
