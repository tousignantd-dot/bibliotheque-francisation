# -*- coding: utf-8 -*-
"""A4 · Les diaporamas de séance — ce que l'enseignant projette, sans rien faire.

Section teal · l'annexe qui montre le diaporama d'une séance, bloc par bloc.
C'est le document le plus convaincant devant des enseignants, parce qu'il
répond à la seule question qu'ils se posent : « qu'est-ce que je fais lundi
matin, de 8 h à midi ? ».

Attention à ne pas confondre : ce diaporama-ci **parle** des diaporamas de
séance, il n'en fait pas partie. C'est une annexe de la trousse de présentation.

Source : `assets/presentations/powerpoints-enseignant.html`.
"""
from theme import Deck
from chiffres import CH, n
from vues import ecran, poser


def build(dossier):
    d = Deck(
        code='A4', section='teal',
        titre="Les diaporamas de séance",
        chapeau="%s diaporamas, un par séance, %s diapositives en tout, et %s notes de "
                "présentateur qui disent quoi faire à chaque page. Douze types de "
                "diapositives, pas un de plus."
                % (n(CH['decks']), n(CH['diapos']), n(CH['notes'])),
        duree='6 minutes')

    d.titre(surtitre="ANNEXE  ·  LA SÉANCE",
            notes="Annexe. Devant des enseignants, c'est souvent elle qu'il faut "
                  "projeter en premier : elle répond à « qu'est-ce que je fais lundi "
                  "matin ? », qui passe avant toutes les questions de gouvernance.")

    d.regle("Ce que ce diaporama-ci démontre",
            "Vous êtes en train de regarder le produit se présenter lui-même.",
            precision="Cette diapositive sort du même thème que les %s diaporamas de "
                      "séance : mêmes gabarits, même typographie, mêmes règles de "
                      "couleur. Ce que vous voyez ici, l'enseignant l'a en classe."
                      % n(CH['decks']),
            notes="À dire une seule fois, et sans y insister : la salle le remarque "
                  "seule si on lui laisse deux secondes.")

    ecran(d, "Une séance, bloc par bloc", "Elle s'ouvre sur son objectif",
          poser('mat', '11-diapo-objectifs'),
          "Quatre points, pas plus. L'enseignant sait ce qu'il vise ; les élèves "
          "savent où ils vont.",
          notes="Une séance dure quatre heures. Sans objectif annoncé, elle se "
                "raconte au lieu de se dérouler.")

    ecran(d, "Une séance, bloc par bloc", "La règle, seule et grosse",
          poser('mat', '12-diapo-regle'),
          "Un énoncé par diapositive. C'est celle que les élèves photographient — "
          "elle est composée pour ça.",
          notes="Détail qui fait sourire, mais il est mesuré : une règle qui tient "
                "dans une photo de téléphone se retrouve dans les notes de l'élève.")

    ecran(d, "Une séance, bloc par bloc", "L'exercice projeté",
          poser('mat', '13-diapo-exercice'),
          "Le même exercice que dans le module interactif, en texte composé pour "
          "être lu du fond de la salle.",
          notes="Ce n'est pas une capture d'écran de l'exercice : c'est l'exercice "
                "recomposé. Une image projetée ne se lit pas de la dernière rangée.")

    ecran(d, "Une séance, bloc par bloc", "Puis son corrigé, à la même place",
          poser('mat', '14-diapo-corrige'),
          "La diapositive suivante porte les réponses. L'enseignant n'a rien à "
          "chercher, rien à préparer, rien à improviser.",
          notes="C'est ce qui permet à un remplaçant de donner la séance. Le dire : "
                "les directions y pensent avant les enseignants.")

    ecran(d, "Une séance, bloc par bloc", "Le piège, avant qu'il tombe",
          poser('mat', '15-diapo-piege'),
          "Ce qu'on entend souvent, à côté de ce qu'il faut dire. L'erreur "
          "fréquente est traitée avant qu'un élève la commette.",
          notes="C'est le bloc que les enseignants d'expérience apprécient le plus : "
                "il dit ce que quinze ans de classe apprennent.")

    ecran(d, "Une séance, bloc par bloc", "Le billet de sortie",
          poser('mat', '16-diapo-billet'),
          "La dernière diapositive ferme la séance sur une question. Elle dit à "
          "l'enseignant si ce qu'il vient de faire a pris.",
          notes="Le seul bloc noir de la séance, et c'est voulu : un seul bloc foncé "
                "par document, sinon plus rien ne ressort.")

    ecran(d, "Toutes ensemble", "Seize séances d'un module",
          poser('mat', '17-planche-vignettes'),
          "L'enseignant choisit sa séance en la voyant, pas en lisant un nom de "
          "fichier.",
          notes="Montrer la planche quelques secondes seulement. Ce qu'elle dit tient "
                "en un coup d'œil : c'est déjà fait, et c'est cohérent.")

    d.billet("La question à poser : combien d'heures par semaine vos enseignants "
             "passent-ils à fabriquer ce que vous venez de voir ?",
             exemples=["%s heures de classe sont déjà préparées." % n(CH['heures']),
                       "Le matériel s'ouvre : un enseignant dépose sa version à côté."],
             notes="Même question que dans P1, et c'est voulu — la trousse répète trois "
                   "fois ce qui doit rester. Rappeler que rien n'est verrouillé : le "
                   "dépôt accepte une version d'enseignant sans écraser l'officielle.")

    return d.save(dossier)
