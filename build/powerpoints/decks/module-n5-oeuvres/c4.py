# -*- coding: utf-8 -*-
"""C4 · Reprendre l'œuvre sans se répéter
Bloc C « Défi 2 · Lire une bande dessinée » · couleur ambre · 75 min.
Source : exercices `t2repr` et `t2red`, mini-leçon `t2repr`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C4', section='ambre',
        titre="Reprendre l'œuvre sans se répéter",
        chapeau="Deux minutes sur une seule chose : si vous dites « le "
                "livre » quinze fois, la personne en face décroche avant la "
                "fin, sans savoir pourquoi. Le français règle ça en "
                "changeant de mot sans changer de sujet — et tout le monde "
                "suit sans y penser.",
        duree='75 minutes')

    d.titre(notes="Dernière séance du défi 2. Commencer par une démonstration : lire au "
                  "groupe un court paragraphe où « le livre » revient six fois. Le malaise "
                  "se voit sur les visages avant qu'on ait expliqué quoi que ce soit.")

    d.objectifs([
        "remplacer un mot précis par un mot plus général : album, livre, œuvre ;",
        "employer un mot voisin : le roman, l'histoire, le récit ;",
        "poser le déterminant démonstratif qui recolle : ce, cet, cette, ces ;",
        "décrire une planche d'un seul tenant, sans répéter le même mot.",
    ], notes="C'est un savoir du programme de niveau 5 : employer des procédés de "
             "substitution lexicale pour reprendre un référent. Le mot savant n'a pas à "
             "être dit ; ce qui compte, c'est que l'élève entende la répétition chez lui.")

    d.declencheur(
        'Écoute', "« J'ai lu un livre. Le livre est bon. Dans le livre, il y "
                  "a… » Qu'est-ce qui ne va pas ?",
        pistes=[
            "Est-ce que c'est incorrect, ou seulement lourd ?",
            "Par quels mots pourriez-vous remplacer le deuxième « livre » ?",
            "Et le troisième ?",
            "Est-ce qu'on peut commencer par « cette œuvre » ?",
        ],
        notes="La première piste est importante : rien n'est fautif dans la phrase de "
              "départ. C'est une question de discours, pas de grammaire — et c'est "
              "précisément ce que le niveau 5 ajoute au niveau 4.")

    d.regle("On va du précis vers le général, jamais l'inverse",
            "album, puis livre, puis œuvre — et c'est toujours le dernier nom "
            "cité qui commande.",
            precision="La première phrase doit dire ce que c'est : « c'est un album de "
                      "bande dessinée ». Les reprises viennent après et vivent de ce "
                      "que la première a posé. Commencer par « je vais vous parler de "
                      "cette œuvre » ne dit à personne ce que vous tenez dans les mains.",
            notes="Diapositive à photographier. Elle règle deux choses d'un coup : l'ordre "
                  "des reprises et l'interdiction de commencer par le mot général, vue à "
                  "la séance A1 et A3.")

    d.tableau('Trois chaînes de reprise', "La même œuvre, dite autrement à chaque phrase",
              ['On présente', 'Deuxième mention', 'Troisième mention'],
              [["C'est un album de BD", "ce livre", "cette œuvre"],
               ["C'est un roman", "l'histoire", "ce récit"],
               ["C'est une série", "les épisodes", "cette œuvre"],
               ["C'est un film", "cette histoire", "ce que j'ai vu"],
               ["Le personnage principal", "la femme", "elle"]],
              cle=1,
              notes="La dernière rangée montre la reprise par pronom, la plus économique. "
                    "Avertir tout de suite : après deux « elle », on remet un nom, sinon "
                    "l'auditeur reconstruit la mauvaise personne et ne s'en aperçoit que "
                    "trois phrases plus tard.")

    d.cartes("Deux procédés, un déterminant", "Ce qui fait tenir la reprise", [
        ("Le mot plus général",
         "album, puis livre, puis œuvre. Toujours vrai, jamais faux."),
        ("Le mot voisin",
         "le roman, l'histoire, le récit : chacun éclaire un côté différent."),
        ("Le déterminant démonstratif",
         "ce, cet, cette, ces — il dit « celle dont je viens de parler »."),
        ("Le pronom",
         "il, elle, ça : le plus court, mais jamais deux fois de suite."),
    ], notes="La troisième carte est un savoir du programme à part entière : le "
             "déterminant démonstratif non déictique. C'est lui qui fait le lien, autant "
             "que le nom — « cette histoire » ne montre rien, il renvoie à ce qui vient "
             "d'être dit.")

    d.pratique('Complétez', "Le bon mot de reprise",
               "œuvre · album · histoire · série · tome · livre", [
        ("C'est un album de bande dessinée. Cette ___ m'a pris deux soirées.", "œuvre"),
        ("J'ai commencé une série. Le premier ___ compte cinquante planches.", "tome"),
        ("Le roman se passe au bord de la mer. Cette ___ ressemble à la mienne.", "histoire"),
        ("Il y a quatre tomes en tout. La ___ complète est au rayon du fond.", "série"),
        ("Elle a emprunté une bande dessinée. Ce ___ se garde trois semaines.", "livre"),
        ("Ce film et ce roman racontent la même chose. Les deux ___ sont fortes.", "œuvres"),
    ], corrige=True,
       notes="C'est l'exercice `t2repr` du module interactif. La dernière ligne est la plus "
             "intéressante : un seul mot général reprend deux œuvres de supports "
             "différents. C'est ce qu'aucun mot précis ne peut faire.")

    d.piege("Changer pour un mot faux",
            "J'ai lu une série. Cet album se lit en une soirée.",
            "J'ai lu une série. Le premier tome se lit en une soirée.",
            "La reprise doit rester vraie : une série n'est pas un album, un tome n'est "
            "pas une planche. Quand on hésite, « l'œuvre » et « l'histoire » "
            "conviennent presque toujours et ne trahissent rien.",
            notes="Faire chercher au groupe deux autres reprises fausses possibles — « le "
                  "chapitre » pour une planche, « l'épisode » pour un tome. Les écrire au "
                  "tableau à côté des justes.")

    d.pratique('Production orale', "Décrivez une planche d'un seul tenant",
               "Quatre phrases. Reprenez l'œuvre autrement à chaque fois.", [
        ("1 — De quel album parlez-vous ? Le genre, le tome, la longueur.",),
        ("2 — Décrivez une case qui vous a marqué, sans rien dire de l'histoire.",),
        ("3 — Que font les bulles dans cette planche ? Y en a-t-il beaucoup ?",),
        ("4 — Reprenez l'œuvre trois fois de suite, avec trois mots différents.",),
    ], notes="C'est l'exercice `t2red` du module interactif. Consigne à l'auditeur : "
             "compter les répétitions. Quand quelqu'un dit trois fois le même mot, on "
             "lève la main sans interrompre — et le locuteur se corrige seul.")

    d.billet(
        "Écrivez trois phrases sur votre œuvre, avec trois reprises différentes.",
        exemples=[
            "Commencez par ce que c'est : un roman, un album, une série, un film.",
            "Puis « cette histoire », « ce livre », « cette œuvre » — pas deux fois le même.",
        ],
        notes="Ce billet ferme le défi 2 et alimente la production écrite du bloc E, où la "
              "répétition est le défaut le plus visible d'un carton de sept à dix phrases. "
              "Le dire au groupe en ramassant les billets.")

    return d.save(dossier)
