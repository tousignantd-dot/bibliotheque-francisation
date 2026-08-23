# -*- coding: utf-8 -*-
"""B4 · Quand nous aurons reçu le prix
Bloc B « Défi 1 · La réunion de production » · couleur ambre · 75 min.
Source du module : exercices `t1futant` et `t1repr`, mini-leçons du même nom.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B4', section='ambre',
        titre="Quand nous aurons reçu le prix",
        chapeau="Un échéancier n'est rien d'autre qu'une suite de « ceci avant "
                "cela ». Le français a un temps fait exactement pour ça, et "
                "sans lui on peut dire quand les choses se passent, mais pas "
                "dans quel ordre.",
        duree='75 minutes')

    d.titre(notes="Dernière séance du bloc B. Deux points de langue, tous deux tirés "
                  "de la présentation de monsieur Cormier : le futur antérieur de son "
                  "échéancier, et les reprises qui tiennent son texte ensemble.")

    d.objectifs([
        "former le futur antérieur : auxiliaire au futur, puis participe passé ;",
        "l'employer après quand, lorsque, dès que, une fois que, après que ;",
        "reprendre une idée sans la répéter, par un pronom ou par un nom ;",
        "éviter la reprise ambiguë, qui coûte plus cher que la répétition.",
    ], notes="Deux savoirs, une seule idée : ce qui fait qu'un long discours se suit. "
             "Le dire au groupe, sinon la séance a l'air de deux leçons collées.")

    d.declencheur(
        'Observation', "Deux façons de dire la même chose",
        pistes=[
            "« Quand nous recevrons le prix, nous déciderons. »",
            "« Quand nous aurons reçu le prix, nous déciderons. »",
            "Laquelle dit clairement ce qui se passe en premier ?",
            "Est-ce que la première est fausse, ou seulement moins précise ?",
        ],
        notes="Réponse à la dernière question : moins précise. Ne pas dire « faux » : "
              "les élèves entendront la première forme dans la rue, et se croiront "
              "trompés.")

    d.tableau('Analyse', "Le futur antérieur, en trois lignes",
              ['Ce qu\'il faut', 'Exemple'],
              [["Auxiliaire au futur", "j'aurai, nous aurons, elle sera"],
               ["Puis le participe passé", "terminé, reçu, arrivée, décidé"],
               ["Avec avoir", "nous aurons reçu, ils auront décidé"],
               ["Avec être, ça s'accorde", "la table sera arrivée, elle sera partie"],
               ["Aux pronominaux", "l'essai se sera terminé"]],
              cle=0,
              note="Le choix de l'auxiliaire est le même qu'au passé composé : « elle est partie » donne « elle sera partie ».",
              notes="Diapositive à photographier. La dernière rangée règle d'avance la "
                    "question qui vient toujours : quel auxiliaire ?")

    d.regle("Six mots appellent le futur antérieur",
            "quand, lorsque, dès que, aussitôt que, une fois que, après que.",
            precision="Après ces mots, si les deux actions sont au futur, la première "
                      "passe au futur antérieur. « Quand l'essai SERA TERMINÉ, on "
                      "décidera. » Attention : « après que » demande l'indicatif, pas "
                      "le subjonctif - c'est « avant que » qui prend le subjonctif. La "
                      "confusion est très répandue, y compris chez les francophones.",
            notes="Diapositive à photographier. La précision sur « après que » évitera "
                  "une erreur au bloc D, où le subjonctif arrive pour de bon.")

    d.pratique('Pratique', "Mettez au futur antérieur",
               "Le verbe entre parenthèses porte ce qui finit en premier.", [
        ("Quand l'essai ... (se terminer), nous déciderons.", "se sera terminé"),
        ("Une fois que nous ... (recevoir) la soumission, je la ferai circuler.", "aurons reçu"),
        ("Dès que les relevés ... (être) compilés, ils seront affichés.", "auront été"),
        ("Quand la table ... (arriver), il faudra former les emballeurs.", "sera arrivée"),
        ("Après que la direction ... (approuver) le budget, la commande partira.", "aura approuvé"),
        ("Quand vous ... (lire) le document joint, vous comprendrez.", "aurez lu"),
    ], corrige=True,
       notes="C'est l'exercice `t1futant` du module, qui en compte huit. Il est en "
             "`cols:1` : ses items font deux propositions et deux colonnes les "
             "rendraient illisibles.")

    d.tableau('Analyse', "Reprendre sans répéter",
              ['Le moyen', 'Exemple'],
              [["Le pronom", "Elle a relu la soumission. Elle LA trouve claire."],
               ["« en » et « y »", "Il a parlé du budget. Il EN a parlé longtemps."],
               ["Le nom qui résume", "Trois personnes blessées. CE CONSTAT a été présenté."],
               ["Le mot voisin", "la table élévatrice devient L'APPAREIL"],
               ["Le terme général", "Meubles Rive-du-Nord devient L'ENTREPRISE"]],
              cle=0,
              note="Le troisième est le plus utile au niveau où vous êtes : il demande de résumer, pas seulement de désigner.",
              notes="Diapositive à photographier. Faire chercher dans la présentation "
                    "de monsieur Cormier une reprise de chaque sorte : il y en a de "
                    "toutes.")

    d.piege('Écriture',
            "« Il a montré le plan au chef. Il l'a trouvé compliqué. »",
            "répéter le nom quand deux lectures sont possibles",
            "Qui a trouvé quoi compliqué ? La phrase a deux sens, et le lecteur "
            "choisira le mauvais une fois sur deux. Répéter le nom n'est pas élégant, "
            "mais c'est compris - et dans un écrit de travail, être compris passe "
            "avant être élégant.",
            notes="Faire produire deux lectures de la phrase par deux élèves "
                  "différents. C'est plus convaincant que l'explication.")

    d.pratique('Pratique', "Reprenez l'idée de la phrase précédente",
               "Écrivez le mot qui manque.", [
        ("Aïcha a préparé sa feuille. Elle ... a montrée à Thérèse.", "l'"),
        ("Il a parlé du budget. Il ... a parlé trois minutes.", "en"),
        ("Le programme est dans le classeur. Personne n'... a regardé.", "y"),
        ("Trois personnes se sont blessées. Ce ... a été présenté.", "constat"),
        ("On mesure, on trace, on essaie. Cette ... prendra deux mois.", "démarche"),
        ("Le comité a voté contre. Cette ... a surpris tout le monde.", "décision"),
    ], corrige=True,
       notes="C'est l'exercice `t1repr` du module. Les trois derniers items sont les "
             "plus difficiles et les plus payants : ils demandent de résumer la phrase "
             "précédente en un mot.")

    d.billet(
        "Écrivez l'échéancier de votre projet en trois phrases.",
        exemples=[
            "Une phrase avec « quand ... aura ... », une avec « dès que ».",
            "Donnez au moins deux dates précises.",
            "Reprenez votre projet une fois par un nom, sans le répéter.",
        ],
        notes="Ramasser. C'est la troisième pièce du projet de chacun, après le "
              "constat (A1) et l'objectif (B2). Le bloc C assemblera le tout.")

    return d.save(dossier)
