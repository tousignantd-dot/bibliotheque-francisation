# -*- coding: utf-8 -*-
"""B3 · Le pronom « qui ».
Bloc B · couleur ambre (écriture) · 75 min.
Source : exercice `t1qui` et sa mini-leçon.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B3', section='ambre',
        titre="Le pronom « qui »",
        chapeau="« Juan suit un cours. Ce cours traite d'économie. » Deux phrases "
                "courtes et une répétition. Un seul mot les réunit et fait disparaître "
                "la répétition.",
        duree='75 minutes')

    d.titre(notes="Écrire les deux phrases du chapeau au tableau et demander au groupe "
                  "de n'en faire qu'une. Certains trouveront « qui » tout seuls.")

    d.objectifs([
        "joindre deux phrases avec le pronom « qui » ;",
        "retrouver le groupe de mots que « qui » reprend ;",
        "éviter la répétition d'un nom dans un message écrit ;",
        "reconnaître que « qui » est toujours suivi d'un verbe.",
    ])

    d.regle('La règle',
            "« Qui » remplace un groupe du nom et le relie à un verbe.",
            precision="« Juan suit un cours qui traite d'économie. » Le mot « qui » "
                      "reprend « un cours » et évite de le répéter. Il est toujours "
                      "suivi d'un verbe : c'est son repère le plus sûr.",
            notes="Écrire la règle au tableau. Le repère « toujours suivi d'un verbe » "
                  "servira à tous les exercices.")

    d.tableau('Analyse', "Comment deux phrases deviennent une",
              ['Étape', 'La phrase'],
              [["deux phrases", "Juan suit un cours. Ce cours traite d'économie."],
               ["le mot répété", "un cours / ce cours"],
               ["on remplace par qui", "Juan suit un cours qui traite d'économie."]],
              cle=0,
              note="« Qui » se place juste après le groupe qu'il reprend. Jamais ailleurs.",
              notes="Faire la même transformation avec trois autres paires de phrases, "
                    "au tableau, avec le groupe.")

    d.tableau('Analyse', "Ce que « qui » reprend",
              ['La phrase', 'Ce que « qui » reprend'],
              [["Voici le rapport qui doit être signé.", "le rapport"],
               ["Le collègue qui remplace Karim s'appelle Omar.", "le collègue"],
               ["J'ai trouvé la salle qui convient.", "la salle"],
               ["C'est l'infirmière qui nous a appelés.", "l'infirmière"],
               ["L'entreprise qui embauche est au centre-ville.", "l'entreprise"]],
              cle=1, props=[0.65, 0.35],
              notes="Dans tous les cas, c'est le groupe placé juste avant « qui ». "
                    "Faire souligner le groupe repris dans chaque phrase. Le motif est "
                    "toujours le même, et c'est ce qui rend la règle facile.")

    d.cartes('En apprendre plus', "Quatre choses à savoir en plus", [
        ("« Qui » est toujours suivi d'un verbe",
         "C'est le repère le plus sûr. « Le collègue qui remplace » — le verbe "
         "« remplace » suit immédiatement. S'il n'y a pas de verbe, ce n'est pas ce "
         "« qui »-là."),
        ("Le verbe s'accorde avec ce que « qui » reprend",
         "« Les employés qui étaient en retard » — pluriel, parce que « qui » reprend "
         "« les employés ». C'est l'erreur la plus fréquente."),
        ("« Qui » ne s'élide jamais",
         "On écrit « qui a », jamais « qu'a ». Contrairement à « que », qui devient "
         "« qu' » devant une voyelle."),
        ("Pourquoi c'est utile dans un message",
         "« Je vous écris au sujet du formulaire qui doit être signé » est plus court "
         "et plus clair que deux phrases séparées."),
    ], notes="La deuxième carte est la plus difficile et la plus utile. Y consacrer du "
             "temps : c'est elle qui distingue un écrit soigné.")

    d.pratique('Pratique · 1 de 4', "Que reprend « qui » ?",
               "Trouvez le groupe de mots placé juste avant.", [
        ("Voici le rapport qui doit être signé avant vendredi.", "le rapport"),
        ("Le collègue qui remplace Karim aujourd'hui s'appelle Omar.", "le collègue"),
        ("J'ai trouvé la salle qui convient pour la réunion.", "la salle"),
        ("C'est l'infirmière qui nous a appelés ce matin.", "l'infirmière"),
        ("L'entreprise qui embauche est située au centre-ville.", "l'entreprise"),
        ("La direction a averti les employés qui étaient en retard.", "les employés"),
    ], corrige=True,
       notes="Le dernier item est le plus difficile : le groupe repris n'est pas le sujet "
             "de la phrase principale. Le corriger en dernier.")

    d.pratique('Pratique · 2 de 4', "Joignez les deux phrases",
               "Employez « qui » pour éviter la répétition.", [
        ("Je vous écris au sujet du formulaire. Ce formulaire doit être signé.",
         "Je vous écris au sujet du formulaire qui doit être signé."),
        ("J'ai parlé à la secrétaire. Cette secrétaire s'occupe des inscriptions.",
         "J'ai parlé à la secrétaire qui s'occupe des inscriptions."),
        ("Voici le billet médical. Ce billet justifie mon absence.",
         "Voici le billet médical qui justifie mon absence."),
        ("Je cherche l'horaire. Cet horaire commence le mois prochain.",
         "Je cherche l'horaire qui commence le mois prochain."),
    ], corrige=True,
       notes="Faire souligner le mot répété avant de transformer. C'est cette étape que "
             "les élèves sautent, et c'est celle qui fait tout le travail.")

    d.piege("Le piège de l'accord du verbe",
            "Les employés qui était en retard.",
            "Les employés qui étaient en retard.",
            "Le verbe qui suit « qui » s'accorde avec le groupe repris, pas avec le mot "
            "« qui » lui-même. Ici, « qui » reprend « les employés » : le verbe est au "
            "pluriel. Le mot « qui » n'a pas de nombre propre — il emprunte celui du "
            "groupe qu'il remplace.",
            notes="Diapo à traiter lentement. Faire chercher le groupe repris avant de "
                  "conjuguer, systématiquement.")

    d.piege("Le piège de l'élision",
            "Le collègue qu'a remplacé Karim.",
            "Le collègue qui a remplacé Karim.",
            "« Qui » ne perd jamais son i, même devant une voyelle. « Qu' » est "
            "l'élision de « que », qui est un autre mot et n'est pas suivi d'un verbe "
            "directement. Si un verbe suit, c'est « qui », en entier.",
            notes="Ne pas développer la différence entre « qui » et « que » à ce niveau. "
                  "Le repère du verbe suffit.")

    d.pratique('Pratique · 3 de 4', "Accordez le verbe",
               "Cherchez d'abord le groupe que « qui » reprend.", [
        ("Les employés qui (être) ___ en retard doivent prévenir.", "étaient / sont"),
        ("Le formulaire qui (devoir) ___ être signé est sur le bureau.", "doit"),
        ("Les documents qui (manquer) ___ sont la preuve d'emploi et le formulaire.", "manquent"),
        ("La secrétaire qui (s'occuper) ___ des inscriptions est absente.", "s'occupe"),
        ("Les cours qui (commencer) ___ le mois prochain sont complets.", "commencent"),
    ], corrige=True,
       notes="Faire nommer le groupe repris à voix haute avant chaque réponse. Sans cette "
             "étape, l'exercice devient un jeu de hasard.")

    d.pratique('Pratique · 4 de 4', "Écrivez trois phrases avec « qui »",
               "Chacune doit parler d'un message, d'un retard ou d'un document.", [
        ("Un document", "Je vous envoie le billet médical qui justifie mon absence."),
        ("Une personne", "C'est la secrétaire qui m'a donné le formulaire."),
        ("Un cours", "Je suis le cours de francisation qui a lieu le matin."),
    ], corrige=True,
       notes="Corriger deux choses seulement : le verbe qui suit « qui », et son accord. "
             "Le reste viendra plus tard.")

    d.billet(
        "Écrivez deux phrases avec « qui ».",
        exemples=[
            "Soulignez le groupe de mots que « qui » reprend.",
            "Vérifiez que le verbe qui suit est accordé avec ce groupe.",
        ],
        notes="Corriger les billets en dehors du cours et rendre à la séance suivante. "
              "L'accord après « qui » demande une rétroaction individuelle.")

    return d.save(dossier)
