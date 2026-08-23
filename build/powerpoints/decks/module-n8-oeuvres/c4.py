# -*- coding: utf-8 -*-
"""C4 · Dire son doute sans le déguiser
Bloc C « Défi 2 · Ce qui n'est pas écrit » · couleur ambre · 75 min.
Source : exercices `t2subj` et `t2temps`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C4', section='ambre',
        titre="Dire son doute sans le déguiser",
        chapeau="« Elle est en colère » ferme la porte. « Il se peut qu'elle "
                "soit en colère » la laisse ouverte. Le mode du verbe dit à "
                "quel titre vous parlez.",
        duree='75 minutes')

    d.titre(notes="Dernière séance du Défi 2. C'est la grammaire qui rend une "
                  "interprétation discutable : sans elle, toute lecture se donne pour "
                  "une certitude et la discussion s'arrête.")

    d.objectifs([
        "employer le subjonctif après les déclencheurs du doute ;",
        "employer l'indicatif après « il me semble que » et « je crois que » ;",
        "écrire les six formes irrégulières du subjonctif présent ;",
        "achever la reconnaissance du passé simple et du plus-que-parfait.",
    ], notes="Le deuxième objectif est celui qui se rate. « Il semble que » et « il me "
             "semble que » : un pronom de plus, et le mode change.")

    d.declencheur(
        'Observation', "Ces deux phrases engagent-elles autant celui qui parle ?",
        pistes=[
            "« Il se peut qu'elle soit en colère. »",
            "« Il me semble qu'elle est en colère. »",
            "Laquelle pouvez-vous contredire sans contredire la personne ?",
            "Laquelle diriez-vous devant dix-huit personnes du cercle ?",
        ],
        notes="La troisième question est la bonne : la première phrase se discute, la "
              "seconde engage son auteur. Les deux sont utiles ; ce sont deux outils "
              "différents, pas un juste et un faux.")

    d.tableau('Analyse', "Ce qui déclenche, ce qui ne déclenche pas",
              ['La tournure', 'Le mode'],
              [["il se peut que", "subjonctif"],
               ["il est possible que", "subjonctif"],
               ["bien que, quoique", "subjonctif"],
               ["il semble que", "subjonctif"],
               ["il me semble que", "indicatif"],
               ["je crois que, il paraît que", "indicatif"]],
              cle=1,
              notes="Diapositive à photographier. Donner la règle explicative à voix "
                    "haute plutôt que de la lire : si la tournure veut dire « je "
                    "pense », vous assumez, donc l'indicatif. Elle vaut mieux qu'une "
                    "liste à apprendre et couvre les cas absents du tableau.")

    d.regle("Six formes suffisent",
            "qu'elle soit, qu'elle ait, qu'elle fasse, qu'elle puisse, "
            "qu'elle aille, qu'elle sache.",
            precision="Pour tous les autres verbes, le subjonctif présent se fabrique "
                      "sur la troisième personne du pluriel du présent : ils prennent "
                      "donne qu'elle prenne, ils rendent donne qu'elle rende. Et pour "
                      "la plupart, il s'écrit exactement comme l'indicatif — ce sont "
                      "les six irréguliers qui font tout le travail.",
            notes="Diapositive à photographier. Le dire clairement : la difficulté du "
                  "subjonctif n'est pas sa forme, c'est de savoir quand l'employer.")

    d.piege('Piège', "« il me semble qu'elle soit »",
            "« il me semble qu'elle est »",
            "Avec le pronom, la tournure veut dire « je pense » : c'est une "
            "opinion assumée, donc l'indicatif. Sans le pronom, « il semble "
            "que » exprime une apparence dont personne ne se porte garant, donc "
            "le subjonctif. Un mot de deux lettres, et le mode change — c'est le "
            "couple qui piège tout le monde, y compris des locuteurs de langue "
            "maternelle.",
            notes="Écrire les deux phrases l'une sous l'autre et encadrer le « me ». "
                  "C'est le seul écart visible.")

    d.pratique('Pratique', "Subjonctif ou indicatif ?",
               "Complétez.", [
        ("Il se peut qu'elle ___ (être) en colère.", "soit"),
        ("Il me semble qu'elle ___ (être) en colère.", "est"),
        ("Bien que la corde ___ (rester) attachée...", "reste"),
        ("Il est possible que le narrateur ___ (vouloir) nous égarer.", "veuille"),
        ("Je crois que cette lecture ___ (rendre) compte de tout.", "rend"),
        ("Quoiqu'il ___ (avoir) raison sur la corde...", "ait"),
    ], corrige=True,
       notes="Exercice `t2subj` du module. Les deux premiers sont volontairement "
             "côte à côte : c'est le piège de la séance, et il vaut mieux le "
             "rencontrer ici que dans la lettre d'E2.")

    d.tableau('Analyse', "Reconnaître le passé simple",
              ['La terminaison', 'Les verbes'],
              [["-a, -èrent", "ceux en -er : elle poussa, ils signèrent"],
               ["-it, -irent", "la plupart : elle prit, il fit, elle dit"],
               ["-ut, -urent", "quelques-uns : elle fut, elle eut, il put"],
               ["-int, -inrent", "venir et sa famille : elle vint"]],
              cle=0,
              note="À reconnaître en lisant, jamais à produire en parlant.",
              notes="Diapositive à photographier. Reprendre le texte de C2 et faire "
                    "surligner tous les passés simples : il y en a une dizaine, et "
                    "ils sautent aux yeux une fois le tableau connu.")

    d.pratique('Pratique', "Passé simple ou plus-que-parfait ?",
               "Complétez.", [
        ("Les gens de l'atelier ___ (signer) la carte le matin.", "signèrent"),
        ("Personne ne ___ (dire) rien.", "dit"),
        ("Le poème que je ___ (lire) la veille m'était resté.", "avais lu"),
        ("Elle ___ (venir) sans prévenir.", "vint"),
        ("On ___ (commencer) sans elle.", "avait commencé"),
        ("Il ___ (paraître) que la pièce se joue jusqu'au 14.", "paraît"),
    ], corrige=True,
       notes="Exercice `t2temps` du module, seconde moitié. Le dernier n'est pas une "
             "erreur : il ramène « il paraît que » et son indicatif, pour que les "
             "deux points de la séance se croisent une fois.")

    d.billet(
        "Reprenez votre lecture de « La chaise du fond » et récrivez-la deux "
        "fois : une fois au subjonctif du doute, une fois à l'indicatif assumé.",
        exemples=[
            "« Il se peut que Gisèle ait choisi le fond pour que ça se voie. »",
            "« Il me semble que Gisèle a choisi le fond pour que ça se voie. »",
        ],
        notes="Ramasser, et demander en D1 laquelle des deux ils diraient au cercle. "
              "Les réponses varient, et la discussion est bonne : les deux se "
              "défendent selon ce qu'on veut obtenir.")

    return d.save(dossier)
