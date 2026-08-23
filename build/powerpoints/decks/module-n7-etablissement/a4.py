# -*- coding: utf-8 -*-
"""A4 · La fiche du programme, lue jusqu'en bas
Bloc A « Je découvre » · couleur teal · 90 min. Compréhension écrite.
Source : exercice `prFiche` (type texte) et sa mini-leçon.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A4', section='teal',
        titre="La fiche du programme, lue jusqu'en bas",
        chapeau="Le haut d'une fiche donne envie ; le bas engage. Les "
                "conditions d'admission et ce qui vient après le diplôme "
                "sont toujours écrits, jamais mis en avant.",
        duree='90 minutes')

    d.titre(notes="Séance de lecture, longue. Distribuer la fiche sur papier : lire un "
                  "document administratif à l'écran ne se travaille pas de la même "
                  "façon, et le crayon dans la marge fait partie de la méthode.")

    d.objectifs([
        "trouver dans une fiche les conditions d'admission ;",
        "distinguer les trois portes de l'admission à un diplôme ;",
        "vérifier si un diplôme suffit pour exercer un métier ;",
        "repérer le nombre de places et le nombre de demandes.",
    ], notes="Le troisième objectif est celui qu'on saute toujours. Il change le plan "
             "de carrière qu'on présentera au bloc C : deux étapes au lieu d'une.")

    d.declencheur(
        'Observation', "Que regardez-vous en premier sur une fiche de programme ?",
        pistes=[
            "La durée ? Le métier ? Les conditions ?",
            "Lisez-vous ce qui est écrit sous les titres administratifs ?",
            "Savez-vous ce qu'il faut avoir avant de vous inscrire ?",
            "Un diplôme suffit-il toujours pour travailler ?",
        ],
        notes="La dernière question ouvre la séance : pour plusieurs métiers, la "
              "réponse est non, et presque personne ne le sait avant de commencer.")

    d.regle("Trois questions pour n'importe quelle fiche",
            "Qu'est-ce qu'il faut avoir avant ? Combien de temps, à quel rythme ? Le "
            "diplôme suffit-il pour travailler ?",
            precision="Les trois réponses sont toujours écrites, jamais mises en "
                      "avant. Elles décident si l'on peut s'inscrire, quand, et ce "
                      "qu'il restera à faire une fois le diplôme obtenu.",
            notes="Diapositive à photographier. Faire chercher les trois réponses dans "
                  "la fiche distribuée, en quinze minutes, avant tout commentaire.")

    d.tableau('Analyse', "Les trois portes de l'admission",
              ['La porte', 'Ce qu\'elle demande'],
              [['le diplôme', "le diplôme d'études secondaires, ou un équivalent reconnu"],
               ['les unités', "16 ans au 30 septembre et les unités demandées du secondaire"],
               ['les préalables', "18 ans et la réussite du test de développement général"]],
              cle=0,
              note="La troisième porte existe précisément pour les personnes qui n'ont "
                   "pas fait leur secondaire ici.",
              notes="Trois rangées et une note : le contrôle de densité l'accepte. "
                    "Préciser que le test de développement général ne doit être "
                    "précédé d'aucun exercice préparatoire ni d'aucun prétest — c'est "
                    "une règle du ministère, et elle explique pourquoi personne ne "
                    "vend de cours de préparation.")

    d.regle("Le diplôme n'est pas toujours le dernier papier",
            "Pour plusieurs métiers, un ordre professionnel délivre le permis, et il "
            "ajoute ses propres conditions.",
            precision="En santé, assistance et soins infirmiers, le diplôme compte "
                      "1 800 heures ; le permis, lui, vient de l'Ordre des infirmières "
                      "et infirmiers auxiliaires du Québec, et il faut réussir son "
                      "examen professionnel.",
            notes="Diapositive à photographier. Faire chercher dans la fiche les mots "
                  "« ordre », « permis » et « examen » : ils sont toujours quelque "
                  "part, presque toujours au bas de la page.")

    d.pratique('Lecture', "Qu'est-ce que la fiche répond ?",
               "Retrouvez dans le document le passage qui répond à chaque question.", [
        ("Combien d'heures dure la formation ?", "1 800 heures, à temps plein, le jour"),
        ("À quel métier mène ce diplôme ?", "infirmière ou infirmier auxiliaire"),
        ("Qui délivre le droit d'exercer ?", "l'Ordre, après son examen professionnel"),
        ("Que peut faire une personne de 18 ans sans les unités ?", "les préalables fonctionnels, avec le test de développement général"),
        ("Combien de places, pour combien de demandes ?", "24 places, 68 candidatures l'an dernier"),
        ("Qu'arrive-t-il aux personnes retenues sans place ?", "elles sont inscrites sur la liste d'attente"),
    ], corrige=True,
       notes="Faire souligner le passage dans la fiche plutôt que recopier la réponse. "
             "C'est la compétence visée : retrouver, pas résumer.")

    d.vocabulaire('Vocabulaire', "Quatre mots de la fiche", [
        ("le contingentement", "Le fait de limiter le nombre de places offertes dans un programme."),
        ("les préalables fonctionnels", "La voie d'admission ouverte à 18 ans, avec le test de développement général."),
        ("un ordre professionnel", "L'organisme qui délivre le permis d'exercer un métier réglementé."),
        ("un stage", "La période de la formation qui se passe en milieu de travail."),
    ], notes="« Les préalables fonctionnels » ne s'emploie qu'au pluriel. Le faire "
             "remarquer : c'est le terme exact des documents officiels, et l'élève le "
             "reverra au comptoir.")

    d.billet("Écris les deux étapes qu'il faut franchir avant de travailler comme "
             "infirmière auxiliaire.",
             exemples=["Réussir le diplôme de 1 800 heures.",
                       "Réussir l'examen de l'Ordre pour obtenir le permis."],
             notes="Ramasser les billets. Un élève qui n'écrit qu'une étape n'a pas lu "
                   "jusqu'au bas de la fiche, et c'est exactement ce que la séance "
                   "voulait attraper.")

    return d.save(dossier)
