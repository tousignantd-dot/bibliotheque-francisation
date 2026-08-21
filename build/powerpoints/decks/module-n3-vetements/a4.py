# -*- coding: utf-8 -*-
"""A4 · Un manteau, une tuque.
Bloc A « Je découvre » · couleur ambre (écriture) · 60 min.
Source : exercice `prGenre`, mini-leçon `prGenre`, banc `FC_CARDS`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A4', section='ambre',
        titre='Un manteau, une tuque',
        chapeau="Rien dans un vêtement ne dit s'il est masculin ou féminin. "
                "Il n'y a donc rien à comprendre — il y a quelque chose à "
                "ranger : on apprend le mot avec son article.",
        duree='60 minutes')

    d.titre(notes="Séance d'écriture. Reprendre le billet de sortie de A1 : la plupart des "
                  "élèves ont écrit les vêtements sans article. C'est le point de départ.")

    d.objectifs([
        "employer « un », « une » et « des » devant un vêtement ;",
        "savoir que le genre ne se devine pas ;",
        "employer « une paire de » pour ce qui va par deux ;",
        "écrire les seize mots du module avec leur article.",
    ])

    d.declencheur(
        'Question', "Pourquoi « un manteau » et « une veste » ?",
        pistes=[
            "Les deux se portent au même endroit.",
            "Les deux servent à la même chose.",
            "Qu'est-ce qui décide, alors ?",
            "Comment fait-on dans votre langue ?",
        ],
        notes="La réponse est : rien ne décide. Le dire franchement soulage — beaucoup "
              "d'élèves cherchent une règle qui n'existe pas.")

    d.tableau('Analyse', "Le genre des mots du module",
              ['Masculin — un', 'Féminin — une'],
              [["un manteau", "une tuque"],
               ["un chandail", "une jupe"],
               ["un pantalon", "une cabine"],
               ["un foulard", "une étiquette"],
               ["un cintre", "une facture"]],
              cle=0,
              note="À apprendre par cœur, avec l'article.",
              notes="Diapo à photographier. Faire recopier dans le carnet, en deux "
                    "colonnes, et ajouter « un rabais » et « une taille ».")

    d.regle("Ce qui va par deux prend « des »",
            "des bottes, des mitaines, des gants, des bas",
            precision="Ce sont deux objets qu'on achète ensemble : on ne dit jamais « une "
                      "botte » en magasinant. Pour en compter une, on dit « <b>une paire "
                      "de</b> bottes ». Même chose pour les souliers et les chaussettes.",
            notes="Diapo à photographier. Faire remarquer que « une paire de » est suivi du "
                  "pluriel : une paire de bottes, pas de botte.")

    d.cartes("Trois façons de retenir le genre", "Ce qui marche vraiment", [
        ("Écrire l'article avec le mot",
         "Dans le carnet, jamais « manteau » tout seul : toujours « un manteau ». Deux "
         "lettres de plus, et la question est réglée pour toujours."),
        ("Dire le mot dans une phrase",
         "« Je cherche <b>un</b> manteau. » Un mot isolé se perd ; une phrase se retient."),
        ("Se méfier des ressemblances",
         "Un mot qui finit par un e muet est souvent féminin — souvent, pas toujours : "
         "« un cintre » finit par un e."),
    ], notes="La première carte est la seule qui compte vraiment. Les deux autres aident.")

    d.piege("Chercher une logique",
            "Le manteau est plus gros, donc masculin.",
            "Il n'y a aucune logique : on apprend.",
            "Une veste est féminine et un manteau masculin, pour la même chose portée au "
            "même endroit. Chercher une règle fait perdre du temps et donne de fausses "
            "certitudes ; ranger le mot avec son article règle la question.",
            notes="Rassurer : les enfants d'ici mettent des années à tout savoir, et se "
                  "trompent encore à l'oral.")

    d.vocabulaire('Vocabulaire', "Les seize mots du module", [
        ("un manteau", "Le grand vêtement qu'on met par-dessus les autres pour sortir."),
        ("une tuque", "Le chapeau de laine qui couvre les oreilles, l'hiver."),
        ("un chandail", "Le vêtement du haut du corps, avec ou sans manches longues."),
        ("des bottes", "Les chaussures hautes qui protègent de la neige."),
        ("rayé", "Se dit d'un tissu à lignes. Le contraire est « uni »."),
        ("foncé", "Se dit d'une couleur proche du noir. Le contraire est « pâle »."),
        ("la taille", "La grandeur du vêtement : petit, moyen ou grand."),
        ("une cabine d'essayage", "La petite pièce fermée où on essaie le vêtement."),
    ], notes="Première moitié du banc. La seconde est en D2. Faire répéter chaque mot avec "
             "son article.")

    d.pratique('Pratique', "Un, une ou des ?",
               "Complétez chaque phrase.", [
        ("Je cherche ___ manteau d'hiver.", "un"),
        ("Elle porte ___ tuque grise.", "une"),
        ("Il me faut ___ chandail de laine.", "un"),
        ("Où est ___ cabine d'essayage ?", "la"),
        ("Gardez ___ facture dans votre poche.", "la"),
        ("J'achète ___ paire de bottes.", "une"),
    ], corrige=True,
       notes="Utiliser l'exercice 5 du module. Faire lire la phrase entière à voix haute "
             "après correction : c'est la phrase qui fixe l'article, pas le tableau.")

    d.billet(
        "Recopiez vos cinq vêtements de la séance A1, avec leur article.",
        exemples=[
            "Et ajoutez-en trois autres, de votre choix.",
            "Vérifiez dans le banc de mots du module.",
        ],
        notes="Fin du bloc A. Ramasser les billets : ils disent qui a compris le genre et "
              "qui devra être suivi pendant le défi 1.")

    return d.save(dossier)
