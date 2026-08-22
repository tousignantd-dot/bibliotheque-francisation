# -*- coding: utf-8 -*-
"""B3 · Le, en, y : ne pas perdre le fil
Bloc B « Défi 1 · On m'explique la démarche » · couleur ambre · 75 min.
Source : exercice `t1repr` et sa mini-leçon. Savoir du programme : reprise de
l'information — associer le pronom « le » à une subordonnée, « en » à un GPrép
inanimé, « y » à un lieu ou à « à + chose ».
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B3', section='ambre',
        titre="Le, en, y : ne pas perdre le fil",
        chapeau="Quand Marie-Soleil dit « je le sais », le mot « le » ne "
                "désigne aucun objet : il remplace une phrase entière dite "
                "trente secondes plus tôt.",
        duree='75 minutes')

    d.titre(notes="Séance de grammaire du texte, la première du module. C'est ce qui "
                  "sépare vraiment le niveau 6 des niveaux 3 et 5 : la difficulté "
                  "n'est plus le mot, c'est ce à quoi il renvoie.")

    d.objectifs([
        "retrouver ce que remplace « le » dans une explication suivie ;",
        "employer « en » pour « de + une chose » ;",
        "employer « y » pour « à + une chose » et pour un lieu ;",
        "placer le pronom devant le verbe, toujours.",
    ], notes="Le premier objectif est un objectif de lecture et d'écoute, pas de "
             "production : on veut d'abord que l'élève retrouve le référent.")

    d.declencheur(
        'Observation', "« Je le sais. » Il sait quoi ?",
        pistes=[
            "Est-ce qu'on peut répondre sans la phrase d'avant ?",
            "Est-ce que « le » désigne un homme, une femme, une chose ?",
            "Qu'est-ce qui se passe si on perd la phrase d'avant ?",
        ],
        notes="Ne pas donner la réponse : la faire chercher deux minutes. La "
              "conclusion — « le » ne désigne rien du tout tant qu'on n'a pas reculé "
              "d'une phrase — est le cœur de la séance.")

    d.tableau('Analyse', "Trois pronoms, trois emplois",
              ['Le pronom', 'Ce qu\'il remplace'],
              [["le, l'", "une phrase entière déjà dite — Je le sais."],
               ["en", "de + une chose — Elle en parle."],
               ["y", "à + une chose, ou un lieu — J'y pense. Elle y va."],
               ["de lui, à elle", "une personne : on garde la préposition"]],
              cle=0,
              note="Chose : en, y. Personne : de lui, d'elle, à lui, à elle.",
              notes="Diapositive à photographier. La quatrième ligne évite l'erreur la "
                    "plus fréquente : « elle en parle » pour parler d'une collègue.")

    d.regle("Reculer d'une phrase",
            "Quand tu entends « le », « en » ou « y », demande-toi tout de suite : ça remplace quoi ?",
            precision="C'est là que se perd le fil d'une explication en cinq étapes. "
                      "Le mot est court, il passe vite, et il porte parfois toute la "
                      "phrase précédente. Reculer d'une phrase est un réflexe : il "
                      "s'installe en deux semaines et il sert pour toujours.",
            notes="Diapositive à photographier. Faire l'exercice à l'oral sur le "
                  "dialogue de B1 : relire trois phrases, arrêter à chaque pronom, "
                  "demander le référent.")

    d.cartes('Analyse', "Les verbes qui appellent chaque pronom", [
        ("Ils appellent « le »",
         "savoir, dire, croire, ignorer, comprendre, oublier, expliquer — tous suivis de « que ». Je le sais, il l'a dit, ils l'ignorent."),
        ("Ils appellent « en »",
         "parler de, avoir besoin de, s'occuper de, se souvenir de, être content de. Elle en parle, elle en a besoin."),
        ("Ils appellent « y »",
         "penser à, tenir à, s'habituer à, réfléchir à, participer à. J'y pense, le comité y tient."),
        ("Attention aux personnes",
         "Elle parle de sa collègue donne « elle parle d'elle », jamais « elle en parle ». Je pense à elle, jamais « j'y pense »."),
    ], notes="Diapositive à photographier. Ces listes se retiennent par l'usage, pas "
             "par cœur : y revenir chaque fois qu'un de ces verbes passe dans un "
             "dialogue.")

    d.pratique('Pratique', "Complète avec le, l', en ou y",
               "Regarde la partie soulignée de la première phrase.", [
        ("Marie-Soleil explique que la signature n'est pas requise. Yaneth ne ___ savait pas.", "le"),
        ("Elle parle souvent de la période d'essai. Elle ___ parle à chaque candidat.", "en"),
        ("Yaneth pense à sa rencontre. Elle ___ pense depuis mardi.", "y"),
        ("Ghislain a dit qu'aucune permission n'était nécessaire. Il ___ a répété deux fois.", "l'"),
        ("Le formulaire se dépose au bureau douze. On ___ dépose aussi les attestations.", "y"),
        ("Elle a besoin de son attestation. Elle ___ a besoin avant vendredi.", "en"),
    ], corrige=True,
       notes="Faire justifier chaque réponse par la préposition du verbe : « avoir "
             "besoin DE, donc en ». C'est la seule méthode qui tient sans mémoire.")

    d.piege('Piège', "chercher un objet derrière « le »",
            "reculer d'une phrase et chercher une idée",
            "« Je le sais » ne parle d'aucune chose. Le « le » renvoie à toute une "
            "idée — souvent une phrase avec « que ». Quand vous ne trouvez pas "
            "l'objet, c'est qu'il n'y en a pas : cherchez la phrase.",
            notes="Faire relire à voix haute la réplique de B1 : « c'est important que "
                  "vous le sachiez ». Le groupe doit pouvoir dire ce que « le » "
                  "remplace, mot pour mot.")

    d.pratique('Écoute', "Retrouver le référent",
               "L'enseignante lit deux phrases. Dites ce que le pronom remplace.", [
        ("Le comité choisit sur les compétences. Beaucoup de gens l'ignorent.", "que le comité choisit sur les compétences"),
        ("Elle a suivi la formation en mars. Elle en a gardé l'attestation.", "de la formation"),
        ("La rencontre a lieu à la cafétéria. Vingt-deux personnes s'y sont présentées.", "à la cafétéria"),
        ("Il faut remettre le formulaire avant vendredi. Ghislain le lui a rappelé.", "qu'il faut remettre le formulaire"),
    ], corrige=True,
       notes="Exercice d'écoute, livre fermé. Lire lentement, deux fois. Le dernier "
             "item porte deux pronoms : ne le donner qu'aux groupes rapides.")

    d.billet(
        "Écris deux phrases : la première dit quelque chose, la seconde le reprend.",
        exemples=[
            "Emploie « le », « en » ou « y » dans la seconde.",
            "Souligne dans la première ce que le pronom remplace.",
        ],
        notes="Cinq minutes. Ramasser : c'est la mesure de la séance. Ceux qui "
              "écrivent « elle en parle » pour une personne sont à reprendre en B4.")

    return d.save(dossier)
