# -*- coding: utf-8 -*-
"""C2 · Ce, cet, cette, ces.
Bloc C « Défi 2 · Trouver le rayon et demander » · couleur ambre (écriture) · 60 min.
Source : exercice `t2ce`, mini-leçon `t2ce`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C2', section='ambre',
        titre='Cette laveuse-là',
        chapeau="Quand le mot manque, le doigt et quatre petits mots "
                "suffisent. Ce, cet, cette, ces : les déterminants qui "
                "montrent sont les plus utiles du magasin.",
        duree='60 minutes')

    d.titre(notes="Séance d'écriture. Prévoir des objets de la classe à désigner : la "
                  "règle se comprend en montrant, pas en expliquant.")

    d.objectifs([
        "employer ce, cet, cette et ces devant un nom ;",
        "choisir cet devant un mot qui commence par une voyelle ;",
        "ajouter le -là qui montre, comme on le dit ici ;",
        "écrire une question en montrant un appareil.",
    ])

    d.regle("Quatre mots pour montrer",
            "ce  ·  cet  ·  cette  ·  ces",
            precision="Ils remplacent « un » et « une » quand on désigne "
                      "quelque chose qu'on a devant les yeux. Le vendeur suit "
                      "le doigt, et la conversation avance.",
            notes="Diapo à photographier. Montrer quatre objets de la classe et faire "
                  "dire la forme juste par quatre élèves différents.")

    d.tableau('Analyse', "Lequel devant quel mot ?",
              ['On dit', 'Devant', 'Exemple'],
              [["ce", "un mot masculin", "ce modèle, ce rayon"],
               ["cet", "un masculin à voyelle", "cet aspirateur, cet ordinateur"],
               ["cette", "un mot féminin", "cette laveuse, cette affichette"],
               ["ces", "tous les pluriels", "ces laveuses, ces modèles"]],
              cle=0,
              note="Cet et cette se prononcent pareil : la différence s'écrit "
                   "seulement.",
              notes="Diapo à photographier. Insister sur la ligne « cet » : c'est la "
                    "seule qui existe pour une raison de prononciation.")

    d.cartes("Le petit -là qui montre", "Trois choses à savoir", [
        ("C'est la langue d'ici",
         "« Cette laveuse-là », « ce modèle-là ». On l'entend partout au Québec, dans "
         "tous les commerces."),
        ("Il n'est pas obligatoire",
         "« Cette laveuse » est parfaitement correct. Le -là rend seulement le geste "
         "plus clair."),
        ("Il s'écrit avec un trait d'union",
         "cette laveuse-là, ce modèle-là. Le trait d'union relie le nom et le petit mot."),
    ], cols=3,
       notes="Faire écouter la différence : « cette laveuse » et « cette laveuse-là ». "
             "La seconde forme accompagne le doigt.")

    d.pratique('Écriture', "Ce, cet, cette ou ces ?",
               "Complétez chaque phrase.", [
        ("___ laveuse-là est dans la circulaire.", "cette"),
        ("___ modèle coûte 849 $.", "ce"),
        ("___ aspirateur est en spécial.", "cet"),
        ("___ réfrigérateurs sont trop grands pour ma cuisine.", "ces"),
        ("Je voudrais essayer ___ ordinateur portable.", "cet"),
        ("___ affichette dit vingt-sept pouces.", "cette"),
    ], corrige=True,
       notes="Faire écrire d'abord. À la correction, demander chaque fois pourquoi : "
             "le genre, ou la voyelle.")

    d.piege("Dire « ce aspirateur »",
            "ce aspirateur",
            "cet aspirateur",
            "Deux voyelles qui se cognent : la bouche s'arrête. C'est exactement pour "
            "éviter ça que « cet » existe. Dès qu'un mot masculin commence par une "
            "voyelle, on met « cet », sans réfléchir.",
            notes="Faire prononcer la forme fautive à voix haute : les élèves entendent "
                  "eux-mêmes pourquoi elle ne tient pas.")

    d.pratique('Production', "Montrez et demandez",
               "Formez la question à voix haute.", [
        ("la laveuse blanche", "Cette laveuse-là, elle coûte combien ?"),
        ("le micro-ondes noir", "Ce micro-ondes-là, il coûte combien ?"),
        ("l'aspirateur en haut", "Cet aspirateur-là, il coûte combien ?"),
        ("les deux réfrigérateurs", "Ces réfrigérateurs-là coûtent combien ?"),
    ], corrige=True,
       notes="Exercice debout, en montrant du doigt une image projetée. Le geste et la "
             "phrase se retiennent ensemble.")

    d.billet(
        "Écrivez quatre phrases avec ce, cet, cette et ces.",
        exemples=[
            "Une pour chaque forme, avec un appareil différent.",
            "Ajoutez le -là dans au moins deux phrases.",
        ],
        notes="Devoir d'écriture. Ramasser : la confusion cet/cette se corrige ici, une "
              "fois pour toutes.")

    return d.save(dossier)
