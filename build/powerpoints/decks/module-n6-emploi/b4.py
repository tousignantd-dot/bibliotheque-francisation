# -*- coding: utf-8 -*-
"""B4 · Il faut que vous remplissiez
Bloc B « Défi 1 · On m'explique la démarche » · couleur ambre · 75 min.
Source : exercices `t1subj` et `t1chiffres`, mini-leçon `t1subj`. Savoir du
programme : employer obligatoirement le subjonctif présent après quelques
verbes introducteurs usuels + que ; distinguer verbe + de et verbe + que.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B4', section='ambre',
        titre="Il faut que vous remplissiez",
        chapeau="L'indicatif raconte ce qui se passe ; le subjonctif dit ce "
                "qu'on veut, ce qu'on exige, ce qu'on souhaite. Une démarche "
                "est faite de choses qu'il faut faire.",
        duree='75 minutes')

    d.titre(notes="Dernière séance du bloc B. Elle ferme le Défi 1 par le mode de la "
                  "consigne, et elle reprend les chiffres du dialogue en deuxième "
                  "écoute.")

    d.objectifs([
        "reconnaître les verbes qui appellent le subjonctif ;",
        "former le subjonctif présent des verbes courants ;",
        "savoir que « espérer » fait exception ;",
        "choisir entre « de » et un infinitif, ou « que » et un subjonctif.",
    ], notes="Le troisième objectif règle à lui seul la moitié des fautes : « espérer » "
             "est le verbe de cette famille qu'on emploie le plus.")

    d.declencheur(
        'Observation', "Combien de fois entends-tu « il faut que » dans une journée de travail ?",
        pistes=[
            "Qui le dit : le chef d'équipe, un collègue, toi-même ?",
            "Qu'est-ce qui vient juste après ?",
            "Est-ce que ça sonne pareil que « il faut » tout seul ?",
        ],
        notes="La troisième question ouvre la distinction de la fin de séance : « il "
              "faut remplir » (tout le monde) contre « il faut que vous remplissiez » "
              "(vous). Ne pas la traiter tout de suite.")

    d.tableau('Analyse', "Les verbes qui l'appellent",
              ['Le verbe', 'Un exemple'],
              [["il faut que", "Il faut que vous remplissiez le formulaire."],
               ["je veux que", "Ghislain veut que son équipe sache ce qui est écrit."],
               ["je souhaite que", "Le comité souhaite que les candidats soient prêts."],
               ["je demande que", "L'entreprise demande que chacun reçoive une réponse."],
               ["mais : j'espère que", "J'espère qu'elle obtiendra le poste. — indicatif"]],
              cle=0,
              note="Une seule exception, et c'est le verbe le plus employé de la famille.",
              notes="Diapositive à photographier. Six rangées, c'est le maximum lisible "
                    "de loin : ne rien y ajouter.")

    d.regle("La recette du subjonctif",
            "On part du « ils » du présent, on enlève -ent, on ajoute e, es, e, ions, iez, ent.",
            precision="Ils remplissent donne « que je remplisse, que tu remplisses, "
                      "qu'il remplisse ». Nous et vous reprennent la forme de "
                      "l'imparfait : que nous remplissions, que vous remplissiez. "
                      "Quatre irréguliers à savoir par cœur : que je sois, que j'aie, "
                      "que je fasse, que j'aille.",
            notes="Diapositive à photographier. Faire conjuguer « remplir » et "
                  "« recevoir » au tableau par deux élèves ; les autres suivent la "
                  "recette à voix haute.")

    d.pratique('Pratique', "Mets le verbe au subjonctif",
               "Le verbe à employer est entre parenthèses.", [
        ("Il faut que vous ___ (remplir) le formulaire RH-04.", "remplissiez"),
        ("Il faut que Yaneth ___ (avoir) six mois d'ancienneté.", "ait"),
        ("Le comité souhaite que les candidats ___ (être) prêts.", "soient"),
        ("Ghislain veut que son équipe ___ (savoir) ce qui est écrit.", "sache"),
        ("Il est important que tu ___ (faire) ta demande avant vendredi.", "fasses"),
        ("J'espère qu'elle ___ (obtenir) le poste.", "obtiendra - pas de subjonctif"),
    ], corrige=True,
       notes="Le dernier item est un piège annoncé : le lire à voix haute avant que le "
             "groupe écrive, et demander pourquoi il est différent.")

    d.piege('Piège', "je souhaite que je parte tôt",
            "je souhaite partir tôt",
            "Quand c'est la même personne des deux côtés, on emploie l'infinitif, pas "
            "« que ». Deux personnes différentes, alors seulement : « je souhaite que "
            "tu partes ». Même chose avec « il faut » : « il faut remplir » vaut pour "
            "tout le monde, « il faut que vous remplissiez » vaut pour vous.",
            notes="C'est ici qu'on répond à la troisième piste du déclencheur. Faire "
                  "produire les deux formes par le même élève, l'une après l'autre.")

    d.tableau('Deuxième écoute', "Les chiffres exacts de la démarche",
              ['La question', 'La réponse'],
              [["Étapes", "cinq, dans l'ordre"],
               ["Ancienneté", "six mois"],
               ["Formulaire", "RH-04"],
               ["Comité", "trente minutes"],
               ["Réponse écrite", "dans les cinq jours ouvrables"],
               ["Période d'essai", "trente jours travaillés"]],
              cle=0,
              notes="Ces chiffres reviennent au compte rendu du Défi 3. "
                    "Faire l'exercice à l'écoute avant de projeter la réponse : "
                    "réécouter le dialogue de B1 et arrêter à chaque chiffre.")

    d.pratique('Bilan du bloc', "Redis la démarche à ton voisin",
               "En équipes de deux, à voix haute. Deux minutes chacun.", [
        ("Nomme les cinq étapes dans l'ordre.", "sans regarder les notes"),
        ("Donne un délai précis pour au moins deux étapes.", "vendredi 25, 16 h · cinq jours ouvrables"),
        ("Emploie une fois « il faut que » avec un subjonctif.", "il faut que tu aies six mois"),
        ("Emploie une fois « le », « en » ou « y ».", "je le sais · elle en a besoin"),
        ("Termine par ce que tu ferais à sa place.", "à mon avis, je me présenterais"),
    ], corrige=True,
       notes="Répétition générale de la production orale d'E1, en petit. Circuler et "
             "noter qui saute une étape : ce sont ceux à reprendre avant le bloc E.")

    d.billet(
        "Écris une phrase avec « il faut que » sur ton propre travail.",
        exemples=[
            "Une seule phrase.",
            "Souligne le verbe au subjonctif.",
        ],
        notes="Trois minutes. Ramasser : c'est la mesure du bloc B. Les phrases tirées "
              "du vrai travail des élèves ouvrent bien le bloc C.")

    return d.save(dossier)
