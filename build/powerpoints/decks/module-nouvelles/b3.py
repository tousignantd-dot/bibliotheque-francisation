# -*- coding: utf-8 -*-
"""B3 · C'est… qui, c'est… que.
Bloc B · couleur ambre (écriture) · 75 min.
Source : exercices `t1souligne` et `t1cocher`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B3', section='ambre',
        titre="C'est… qui, c'est… que",
        chapeau="« C'est Noah qui a eu l'idée. » Pourquoi pas simplement « Noah a eu "
                "l'idée » ? Parce qu'on veut insister sur Noah — et le français a une "
                "construction faite pour ça.",
        duree='75 minutes')

    d.titre(notes="Écrire les deux phrases au tableau et faire dire les deux à voix "
                  "haute. Demander ce que la première ajoute. Le groupe répondra "
                  "« on insiste » : c'est la leçon.")

    d.objectifs([
        "mettre un élément en évidence avec c'est… qui ou c'est… que ;",
        "choisir entre « qui » et « que » selon la fonction de l'élément ;",
        "employer « ce sont » quand l'élément est au pluriel ;",
        "reconnaître une mise en évidence dans un texte.",
    ])

    d.regle('La règle',
            "C'est + l'élément à mettre en évidence + qui ou que + le reste.",
            precision="« Noah a eu l'idée » devient « C'est Noah qui a eu l'idée ». "
                      "L'élément mis en évidence passe au début, encadré par « c'est » "
                      "et « qui ».",
            notes="Écrire la formule au tableau : C'EST + élément + QUI/QUE + le reste. "
                  "Elle vaut pour tous les exercices de la séance.")

    d.tableau('Analyse', "Qui ou que : la fonction décide",
              ['La phrase de départ', 'La mise en évidence', 'Le mot'],
              [["Noah a eu l'idée.", "C'est Noah qui a eu l'idée.", "qui"],
               ["La classe a fabriqué cette affiche.", "C'est cette affiche que la classe a fabriquée.", "que"],
               ["La voisine a vu le chat hier matin.", "C'est hier matin que la voisine a vu le chat.", "que"]],
              cle=2, props=[0.3, 0.55, 0.15],
              notes="La règle : « qui » quand l'élément mis en évidence est le sujet, "
                    "« que » dans tous les autres cas. Le dire ainsi, c'est suffisant.")

    d.regle('Le test',
            "Si l'élément fait l'action, c'est « qui ». Sinon, c'est « que ».",
            precision="« C'est Noah qui a eu l'idée » — Noah fait l'action d'avoir "
                      "l'idée. « C'est cette affiche que la classe a fabriquée » — "
                      "l'affiche ne fabrique rien, c'est la classe qui fabrique.",
            notes="Faire poser la question « qui fait l'action ? » avant chaque choix. "
                  "C'est le même test qu'on emploiera pour la voix passive, en B4.")

    d.regle('Singulier et pluriel',
            "C'est… pour le singulier. Ce sont… pour le pluriel.",
            precision="« C'est cette voisine qui a reconnu le chat. » « Ce sont les "
                      "élèves qui ont fabriqué les affiches. » L'accord se fait avec "
                      "l'élément mis en évidence, pas avec le reste de la phrase.",
            notes="À l'oral, « c'est les élèves » s'entend souvent. Le signaler comme un "
                  "usage familier : à l'écrit, on écrit « ce sont ».")

    d.pratique('Pratique · 1 de 4', "Quel élément est mis en évidence ?",
               "Le mot ou le groupe placé entre « c'est » et « qui » ou « que ».", [
        ("C'est cette voisine qui a reconnu le chat.", "cette voisine"),
        ("Ce sont les élèves qui ont fabriqué les affiches.", "les élèves"),
        ("C'est hier matin que la voisine a vu le chat.", "hier matin"),
        ("C'est Noah qu'on doit remercier.", "Noah"),
        ("C'est à Gatineau que l'histoire s'est passée.", "à Gatineau"),
    ], corrige=True,
       notes="Faire souligner l'élément dans chaque phrase. Il est toujours au même "
             "endroit : c'est ce qui rend la construction facile à repérer.")

    d.pratique('Pratique · 2 de 4', "Qui ou que ?",
               "L'élément mis en évidence fait-il l'action ?", [
        ("C'est Noah ___ a eu l'idée.", "qui — Noah fait l'action"),
        ("C'est cette affiche ___ la classe a fabriquée.", "que — la classe fabrique"),
        ("C'est hier matin ___ la voisine a vu le chat.", "que — le matin ne fait rien"),
        ("Ce sont les élèves ___ ont amassé les mitaines.", "qui — les élèves font l'action"),
        ("C'est le chat ___ la voisine a reconnu.", "que — la voisine reconnaît"),
    ], corrige=True,
       notes="Faire poser la question « qui fait l'action ? » à voix haute avant chaque "
             "réponse. Sans elle, l'exercice devient un jeu de hasard.")

    d.pratique('Pratique · 3 de 4', "Mise en évidence ou non ?",
               "Toutes les phrases commencent par « c'est » ou « ce sont ».", [
        ("C'est une très belle histoire.", "NON — c'est une phrase ordinaire"),
        ("La fillette qui a perdu son chat est soulagée.", "NON — pas de « c'est »"),
        ("C'est cette affiche que la classe a fabriquée.", "OUI"),
        ("Ce sont de jolies décorations.", "NON — pas de « qui » ni de « que »"),
        ("Ce sont les élèves qui ont informé l'enseignante.", "OUI"),
    ], corrige=True,
       notes="Le critère : il faut « c'est » ET « qui » ou « que ». Un seul des deux ne "
             "suffit pas. C'est l'exercice le plus discriminant de la séance.")

    d.piege("Le piège du « c'est » ordinaire",
            "« C'est une belle histoire » met « une belle histoire » en évidence.",
            "Il faut « c'est » ET « qui » ou « que ».",
            "« C'est une belle histoire » est une phrase ordinaire : elle dit ce qu'est "
            "la chose. La mise en évidence exige les deux morceaux — « c'est » au début "
            "et « qui » ou « que » après l'élément.",
            notes="Faire chercher les deux morceaux dans chaque phrase de l'exercice "
                  "précédent. La méthode est mécanique.")

    d.piege("Le piège du pluriel",
            "C'est les élèves qui ont amassé les mitaines.",
            "Ce sont les élèves qui ont amassé les mitaines.",
            "Devant un élément pluriel, on écrit « ce sont ». À l'oral, « c'est les "
            "élèves » s'entend partout au Québec et personne ne le corrigera. À l'écrit, "
            "dans un texte de nouvelles ou un courriel, il faut « ce sont ».",
            notes="Nuance de registre à présenter honnêtement : ce n'est pas une faute "
                  "de langue, c'est une différence entre l'oral et l'écrit.")

    d.pratique('Pratique · 4 de 4', "Mettez l'élément en évidence",
               "Transformez la phrase.", [
        ("Noah a eu l'idée de la collecte.", "C'est Noah qui a eu l'idée de la collecte."),
        ("Les élèves ont amassé les mitaines.", "Ce sont les élèves qui ont amassé les mitaines."),
        ("La classe a fabriqué cette affiche.", "C'est cette affiche que la classe a fabriquée."),
        ("La voisine a vu le chat hier matin.", "C'est hier matin que la voisine a vu le chat."),
        ("L'histoire s'est passée à Gatineau.", "C'est à Gatineau que l'histoire s'est passée."),
    ], corrige=True,
       notes="Les deux derniers items mettent en évidence un moment et un lieu : c'est "
             "toujours « que ». Le signaler à la correction.")

    d.billet(
        "Écrivez trois phrases avec une mise en évidence.",
        exemples=[
            "Une avec « qui », une avec « que », une avec « ce sont ».",
            "Elles doivent parler d'une nouvelle du module.",
        ],
        notes="Corriger le choix entre qui et que, et l'accord de « ce sont ». Rendre "
              "avant B4 : la voix passive emploie le même test.")

    return d.save(dossier)
