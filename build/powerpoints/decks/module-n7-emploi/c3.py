# -*- coding: utf-8 -*-
"""C3 · Mettre en avant ce qui compte
Bloc C « Défi 2 · Le poste 4 » · couleur ambre · 75 min.
Source du module : exercices `t2emph` et `t2passif`, mini-leçons du même nom.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C3', section='ambre',
        titre="Mettre en avant ce qui compte",
        chapeau="Dans une phrase ordinaire, tous les mots ont le même poids. "
                "Or vous voulez qu'on retienne un mot sur douze. Parler plus "
                "fort ne sert à rien : le volume ne désigne rien. Changer la "
                "construction, oui.",
        duree='75 minutes')

    d.titre(notes="Deux constructions au programme du niveau 7 : la mise en relief "
                  "(cinq points de savoir) et la phrase passive (deux). Elles vont "
                  "ensemble parce qu'elles font le même travail : décider de ce que la "
                  "phrase met en avant.")

    d.objectifs([
        "mettre un sujet en avant avec « ce qui... c'est » ;",
        "mettre un complément en avant avec « ce que... c'est » et « ce dont... c'est » ;",
        "choisir entre « c'est... qui » et « c'est... que » ;",
        "reconnaître une phrase passive et voir qui n'y est pas nommé.",
    ], notes="Le troisième objectif est le seul qui porte sur une faute possible. Les "
             "autres portent sur des choix.")

    d.declencheur(
        'Observation', "La même information, deux fois",
        pistes=[
            "« Se pencher quatre-vingt-deux fois use le dos. »",
            "« Ce qui use le dos, c'est de se pencher quatre-vingt-deux fois. »",
            "Quelle est la dernière chose que vous entendez dans chaque phrase ?",
            "Laquelle reste dans la tête ?",
        ],
        notes="Lire les deux à voix haute, deux fois. Faire nommer par le groupe ce "
              "qui change : rien du contenu, tout de la place. Le mot important arrive "
              "à la fin, là où l'oreille l'attrape.")

    d.tableau('Analyse', "Quatre façons de mettre en relief",
              ['La construction', 'Exemple'],
              [["ce qui... c'est", "Ce qui use le dos, C'EST de se pencher."],
               ["ce que... c'est", "Ce que je demande, C'EST l'autorisation."],
               ["ce dont... c'est", "Ce dont j'ai besoin, C'EST d'une soumission."],
               ["c'est... qui", "C'est la répétition QUI blesse, pas le poids."],
               ["c'est... que", "C'est le prix QUE j'attends."]],
              cle=0,
              note="« qui » quand le mot mis en avant fait l'action, « que » quand il la subit.",
              notes="Diapositive à photographier. « Ce dont » est la forme que les "
                    "apprenants évitent le plus, et celle qui impressionne le plus "
                    "quand elle est juste. Le dire.")

    d.regle("Le test de « qui » et de « que »",
            "Remplacez le mot par « elle » : si « elle blesse » se dit, c'est « qui ».",
            precision="« C'est la répétition qui blesse » - on peut dire « elle "
                      "blesse », donc « qui ». « C'est le prix que j'attends » - on ne "
                      "dit pas « il j'attends », mais « je l'attends », donc « que ». "
                      "Le test prend deux secondes et il ne se trompe jamais.",
            notes="Diapositive à photographier. Faire appliquer le test à voix haute "
                  "sur quatre exemples avant de passer à la pratique.")

    d.pratique('Pratique', "Réécrivez en mettant en relief",
               "Le mot souligné doit ressortir.", [
        ("Se pencher use le dos. Devient : Ce qui use le dos, ... de se pencher.", "c'est"),
        ("Je demande l'autorisation. Devient : Ce que je demande, ... l'autorisation.", "c'est"),
        ("La répétition blesse. Devient : C'est la répétition ... blesse.", "qui"),
        ("J'attends le prix. Devient : C'est le prix ... j'attends.", "que"),
        ("J'ai besoin d'une soumission. Devient : Ce dont j'ai besoin, ... d'une soumission.", "c'est"),
        ("Monsieur Cormier a demandé la copie. Devient : C'est monsieur Cormier ... a demandé la copie.", "qui"),
    ], corrige=True,
       notes="C'est l'exercice `t2emph` du module, qui en compte huit. En `cols:1` : "
             "les items font deux propositions.")

    d.tableau('Analyse', "La phrase passive, en trois mouvements",
              ['Le mouvement', 'Ce qui se passe'],
              [["1 · Le complément monte", "Thérèse a signalé LE RISQUE, donc Le risque..."],
               ["2 · Le verbe passe à être", "...a été signalé..."],
               ["3 · Le sujet part", "...par Thérèse. Ou il disparaît."],
               ["Le repère", "être conjugué + participe, et le sujet ne fait rien"],
               ["L'accord", "avec être, le participe suit le sujet"]],
              cle=0,
              note="Attention : « elle est partie » n'est pas une passive. Partir se conjugue avec être, et le sujet fait bien l'action.",
              notes="Diapositive à photographier. La note évite la confusion la plus "
                    "coûteuse : tout ce qui a « être » n'est pas passif.")

    d.pratique('Pratique', "La même chose, dite autrement",
               "Trouvez la phrase passive.", [
        ("Thérèse a signalé le risque.", "Le risque a été signalé par Thérèse."),
        ("On affichera les résultats au babillard.", "Les résultats seront affichés au babillard."),
        ("Les travailleurs ont élu Thérèse Lapointe.", "Thérèse Lapointe a été élue par les travailleurs."),
        ("Personne n'a corrigé le poste 4.", "Le poste 4 n'a pas été corrigé."),
        ("Le fournisseur nous livrera la table.", "La table nous sera livrée."),
    ], corrige=True,
       notes="C'est l'exercice `t2passif` du module. Le programme demande de "
             "reconnaître la passive, pas d'en fabriquer sans arrêt : le dire, pour "
             "que personne ne reparte en écrivant tout au passif.")

    d.piege('Écriture',
            "« Des erreurs ont été commises. »",
            "nommer qui, quand le nom compte",
            "La passive permet de ne pas nommer, et c'est souvent utile : personne "
            "n'a besoin de savoir qui tiendra le rouleau de papier collant au "
            "babillard. Elle devient malhonnête quand elle efface un responsable "
            "qu'on devrait nommer. Le test, à faire sur vos propres textes : ajoutez "
            "« par qui ? » après chaque passive. Si la réponse compte et n'y est pas, "
            "remettez-la.",
            notes="Faire chercher dans le compte rendu du module (exercice `t1compte`) "
                  "les passives dont l'auteur est absent : il y en a plusieurs, et "
                  "toutes sont légitimes. Le contraste rend la règle claire.")

    d.billet(
        "Réécrivez trois phrases de votre évaluation en mettant en relief.",
        exemples=[
            "Une avec « ce qui... c'est ».",
            "Une avec « c'est... qui ».",
            "Une phrase passive, et dites pourquoi vous ne nommez pas l'auteur.",
        ],
        notes="Ramasser. La dernière consigne est la plus formatrice : elle oblige à "
              "justifier une absence, ce qui est exactement le travail de relecture "
              "qu'on veut installer.")

    return d.save(dossier)
