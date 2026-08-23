# -*- coding: utf-8 -*-
"""C4 · Reprendre sans répéter, et ne pas conclure à la place de l'autre
Bloc C « Défi 2 · Redire ce qui a été dit » · couleur teal · écoute et
réponds · 75 min.
Source : exercices `t2repr` et `t2fait`, et leurs mini-leçons.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C4', section='teal',
        titre="Reprendre sans répéter, et ne pas conclure à la place de l'autre",
        chapeau="Une lettre qui répète huit fois « le tapis roulant » se lit "
                "huit fois moins bien. Et une phrase qui glisse du fait à "
                "l'opinion fait douter de tout le reste.",
        duree='75 minutes')

    d.titre(notes="Dernière séance du défi 2. Elle réunit les deux points qui séparent "
                  "un compte rendu solide d'un récit qu'on n'écoute qu'à moitié.")

    d.objectifs([
        "reprendre un sujet par un pronom, un synonyme ou un nom ;",
        "reconnaître le « ils » sans référent et savoir ne pas l'écrire ;",
        "distinguer un fait rapporté d'une interprétation ;",
        "annoncer une conclusion au lieu de la faire passer pour un constat.",
    ], notes="Le quatrième objectif produit un effet contre-intuitif : annoncer son "
             "incertitude sur un point renforce la crédibilité de tout le reste.")

    d.declencheur(
        'Observation', "« Il ne veut pas faire d'effort. » Comment le vérifier ?",
        pistes=[
            "Est-ce que quelqu'un peut confirmer cette phrase ?",
            "Même lui ?",
            "Et « il m'a dit qu'il ne pouvait pas changer d'heure » ?",
            "Laquelle des deux tiendrait devant un tribunal ?",
        ],
        notes="La différence est simple à énoncer et difficile à tenir : un fait se "
              "vérifie auprès de l'autre, une interprétation ne se vérifie nulle part.")

    d.cartes('Analyse', "Quatre façons de reprendre son sujet", [
        ("Le pronom", "L'appareil est au-dessus de ma chambre. Il y est depuis janvier. À courte portée seulement."),
        ("La substitution lexicale", "un tapis roulant, l'appareil, cet équipement. Trois mots pour la même chose."),
        ("La nominalisation", "Il a refusé de changer d'heure. Ce refus ne m'a pas surprise. La plus efficace à l'écrit."),
        ("Le ça de quantité", "Quinze matins de suite, ça ne s'appelle plus de la malchance. À l'oral seulement."),
    ], notes="La nominalisation est ce qui donne à une lettre son allure de dossier. "
             "Le mot « ce » ou « cette » devant le nom est ce qui fait le lien.")

    d.tableau('Analyse', "Nominaliser : la phrase devient un nom",
              ['La phrase', 'Le nom qui la reprend'],
              [["Il a refusé de changer d'heure.", "Ce refus"],
               ["Le caoutchouc a été posé.", "Cette installation"],
               ["Il s'est engagé à le déplacer.", "Cet engagement"],
               ["Nous nous sommes parlé le 19.", "Cette conversation"],
               ["Le bruit s'est répété.", "Cette répétition"]],
              cle=1,
              notes="Diapositive à photographier. Sans « ce » ou « cette », la reprise "
                    "ne se voit pas et le lecteur croit qu'on parle d'autre chose.")

    d.regle("Un fait se vérifie, une interprétation non",
            "Si on posait la question à l'autre, pourrait-il confirmer ou nier ?",
            precision="« Il m'a dit qu'il ne pouvait pas changer d'heure » : il "
                      "confirmera ou il niera, il n'y a pas de troisième possibilité. "
                      "« Il ne veut pas faire d'effort » : personne ne peut le "
                      "confirmer, pas même lui. Cette phrase dit quelque chose de vous, "
                      "pas de lui.",
            notes="Diapositive à photographier. Un fait n'est pas forcément favorable : "
                  "« il a refusé » en est un, et il vaut mieux l'écrire soi-même.")

    d.piege('Compte rendu',
            "Il se moque de ce que je vis",
            "Il m'a dit qu'il regarderait ; trois semaines plus tard, rien n'a bougé",
            "On ne renonce pas à sa conclusion : on la présente comme une conclusion, "
            "après les faits qui la soutiennent. « J'en conclus qu'il a oublié — mais "
            "ce n'est que ma lecture. » Cinq mots signalent une conclusion : j'en "
            "conclus que, j'ai l'impression que, il me semble que, à mon avis, "
            "manifestement.",
            notes="Faire chercher au groupe les verbes qui trahissent une "
                  "interprétation : il veut, il cherche à, il fait exprès, il se moque.")

    d.pratique('Pratique', "Un fait ou une interprétation ?",
               "Dites de quel côté chaque phrase tombe.", [
        ("Il m'a dit qu'il ne pouvait pas changer son heure.", "un fait"),
        ("Il ne veut pas faire d'effort.", "une interprétation"),
        ("Le caoutchouc a été posé le 26 février.", "un fait"),
        ("Il a posé le caoutchouc juste pour avoir la paix.", "une interprétation"),
        ("L'appareil n'a pas été déplacé au 12 mars.", "un fait"),
        ("Il se moque complètement de ce que je vis.", "une interprétation"),
        ("Il m'a dit qu'il aimait mieux ça qu'une lettre dans sa porte.", "un fait"),
    ], corrige=True,
       notes="Faire réécrire les trois interprétations en trois temps : le fait, le "
             "second fait, puis « j'en conclus que ». C'est le vrai exercice.")

    d.billet(
        "Écris un fait, puis ta conclusion — et sépare-les par « j'en conclus que ».",
        exemples=[
            "Le fait d'abord, avec une date si tu en as une.",
            "La conclusion ensuite, annoncée comme telle.",
        ],
        notes="Deux minutes. Fin du défi 2 : le groupe sait rapporter. Le défi 3 lui "
              "apprend à écrire.")

    return d.save(dossier)
