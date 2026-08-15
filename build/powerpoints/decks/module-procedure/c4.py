# -*- coding: utf-8 -*-
"""C4 · L'impératif, avec et sans pronom.
Bloc C · couleur ambre (écriture) · 75 min.
Source : exercices `t2imper` et `t2pronom`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C4', section='ambre',
        titre="L'impératif",
        chapeau="« Arrêtez la machine. Prenez une photo. Avertissez votre superviseur. » "
                "C'est la forme de toutes les consignes de sécurité — et elle "
                "s'apprend en une séance.",
        duree='75 minutes')

    d.titre(notes="Séance double : l'impératif d'abord, le pronom ensuite. Prévoir une "
                  "pause nette au milieu.")

    d.objectifs([
        "écrire une consigne à l'impératif, deuxième personne du pluriel ;",
        "connaître les trois formes irrégulières ;",
        "écrire une interdiction à l'impératif ;",
        "placer un pronom complément après le verbe, avec un trait d'union.",
    ])

    d.regle("La règle",
            "On prend la forme « vous » du présent et on enlève le sujet.",
            precision="Vous remplissez donne Remplissez. Vous prenez donne Prenez. Vous "
                      "attendez donne Attendez. Rien d'autre ne change : ni la "
                      "terminaison, ni l'orthographe.",
            notes="Écrire la méthode au tableau. Elle fonctionne pour tous les verbes "
                  "sauf trois, qui viendront à la diapo suivante.")

    d.tableau('Analyse', "Du présent à l'impératif",
              ['Au présent', "À l'impératif"],
              [["vous remplissez", "Remplissez"],
               ["vous prenez", "Prenez"],
               ["vous attendez", "Attendez"],
               ["vous arrêtez", "Arrêtez"],
               ["vous avertissez", "Avertissez"]],
              cle=1,
              note="Un seul changement : le sujet « vous » disparaît. Le verbe reste "
                   "identique.",
              notes="Faire lire les deux colonnes à voix haute. La différence s'entend à "
                    "peine, et c'est ce qui rend la forme facile.")

    d.regle('Les trois irrégulières',
            "Être donne soyez. Avoir donne ayez. Aller donne allez.",
            precision="Trois verbes seulement, et ils reviennent constamment dans les "
                      "consignes : « Soyez prudent », « Ayez votre carte avec vous », "
                      "« Allez à la réception ». À apprendre par cœur.",
            notes="Écrire les trois au tableau et les y laisser. « Allez » est régulier "
                  "en apparence, mais il s'écrit sans s au singulier : le mentionner.")

    d.pratique('Pratique · 1 de 4', "Écrivez la consigne à l'impératif",
               "Deuxième personne du pluriel, sans le sujet.", [
        ("Vous devez arrêter la machine immédiatement.", "Arrêtez la machine immédiatement."),
        ("Vous devez prendre une photo du bris.", "Prenez une photo du bris."),
        ("Vous devez remplir le formulaire de signalement.", "Remplissez le formulaire de signalement."),
        ("Vous devez avertir votre superviseur.", "Avertissez votre superviseur."),
        ("Vous devez attendre les instructions.", "Attendez les instructions."),
    ], corrige=True,
       notes="Les cinq consignes sont celles du signalement d'un bris, vues en D2. Le "
             "signaler : on écrit ici ce qu'on lira là-bas.")

    d.regle("L'interdiction",
            "Ne + le verbe à l'impératif + pas ou jamais.",
            precision="« Ne réparez pas la machine vous-même. » « Ne tentez jamais de "
                      "réparer l'équipement. » Les deux morceaux de la négation "
                      "encadrent le verbe, exactement comme au présent.",
            notes="Lier au module 1, séance C3 : la négation ne change pas de "
                  "construction, seul le verbe change de forme.")

    d.pratique('Pratique · 2 de 4', "Écrivez l'interdiction",
               "Ne … pas, ou ne … jamais si c'est absolu.", [
        ("Vous ne devez pas réparer la machine vous-même.",
         "Ne réparez pas la machine vous-même."),
        ("Il ne faut jamais toucher à l'équipement brisé.",
         "Ne touchez jamais à l'équipement brisé."),
        ("Vous ne devez pas envoyer la demande sans photo.",
         "N'envoyez pas la demande sans photo."),
        ("Il ne faut pas jeter le reçu original.", "Ne jetez pas le reçu original."),
    ], corrige=True,
       notes="Le troisième item demande l'élision : « N'envoyez ». Le corriger en "
             "dernier, avec la règle du module 1.")

    # ── seconde partie · le pronom ─────────────────────────────────
    d.regle("Le pronom à l'impératif",
            "Il se place APRÈS le verbe, relié par un trait d'union.",
            precision="« Vous soumettez la demande » devient « Soumettez-la ». C'est "
                      "l'inverse de la phrase normale, où le pronom passe devant le "
                      "verbe. L'impératif est le seul cas où il passe derrière.",
            notes="Lier au module 2, séance C2 : là-bas, toujours devant. Ici, toujours "
                  "derrière. Le contraste doit être explicite.")

    d.tableau('Analyse', "Devant ou derrière",
              ['La phrase', 'Où va le pronom'],
              [["Vous la soumettez.", "devant — phrase normale"],
               ["Soumettez-la.", "derrière — impératif"],
               ["Vous ne la soumettez pas.", "devant — négative"],
               ["Ne la soumettez pas.", "devant — impératif négatif"]],
              cle=1,
              note="À l'impératif négatif, le pronom revient devant. Seul l'impératif "
                   "affirmatif le place derrière.",
              notes="La quatrième ligne surprend. La traiter lentement : c'est la seule "
                    "exception à l'exception.")

    d.cartes('En apprendre plus', "Quatre choses à savoir en plus", [
        ("Me devient moi, te devient toi",
         "« Vous me remettez le formulaire » devient « Remettez-moi le formulaire ». "
         "Seulement à l'impératif affirmatif."),
        ("Deux pronoms, un ordre fixe",
         "« Demandez-le-lui. » Le pronom d'objet vient avant celui de la personne, "
         "reliés par des traits d'union."),
        ("Le trait d'union est obligatoire",
         "« Soumettez la » sans trait d'union se lit comme « soumettez la demande ». Le "
         "trait d'union est ce qui dit que « la » est un pronom."),
        ("À la négative, tout redevient normal",
         "« Ne la soumettez pas. » Pas de trait d'union, pronom devant. C'est la "
         "construction ordinaire."),
    ], notes="La deuxième carte dépasse un peu le niveau. La montrer et passer : elle "
             "apparaît dans les exercices, mais on ne l'exige pas.")

    d.pratique('Pratique · 3 de 4', "Remplacez par un pronom",
               "Le pronom se place après le verbe, avec un trait d'union.", [
        ("Vous avisez le superviseur de ce changement.", "Avisez-le de ce changement."),
        ("Vous préparez les documents pour la demande.", "Préparez-les."),
        ("Vous me contactez si vous avez des questions.", "Contactez-moi si vous avez des questions."),
        ("Tu m'appelles dès que la demande est approuvée.", "Appelle-moi dès que la demande est approuvée."),
        ("Vous demandez le formulaire à la commis.", "Demandez-le-lui."),
    ], corrige=True,
       notes="Le dernier item a deux pronoms. Le corriger en dernier, sans en faire une "
             "exigence pour tous.")

    d.piege("Le piège du trait d'union",
            "Soumettez la.",
            "Soumettez-la.",
            "Sans trait d'union, « la » se lit comme un déterminant et le lecteur attend "
            "un nom : « soumettez la demande ». Le trait d'union est ce qui transforme "
            "le mot en pronom. Ce n'est pas un détail de présentation.",
            notes="Faire lire les deux versions à voix haute : elles se disent pareil. "
                  "C'est justement pour cela que l'écrit a besoin du trait d'union.")

    d.piege("Le piège de la négative",
            "Ne soumettez-la pas.",
            "Ne la soumettez pas.",
            "À l'impératif négatif, le pronom repasse devant le verbe et le trait "
            "d'union disparaît. C'est la construction ordinaire, celle du module 2. "
            "Seul l'impératif affirmatif place le pronom derrière.",
            notes="Faire écrire les deux formes côte à côte pour trois verbes. Le "
                  "contraste installe la règle mieux que l'explication.")

    d.pratique('Pratique · 4 de 4', "Affirmatif ou négatif ?",
               "Écrivez la consigne avec le pronom au bon endroit.", [
        ("Soumettre la demande — affirmatif", "Soumettez-la."),
        ("Soumettre la demande — négatif", "Ne la soumettez pas."),
        ("Joindre le reçu — affirmatif", "Joignez-le."),
        ("Jeter le reçu — négatif", "Ne le jetez pas."),
    ], corrige=True,
       notes="Exercice apparié : même verbe, deux formes. C'est le contraste qui "
             "enseigne, pas la répétition.")

    d.billet(
        "Écrivez quatre consignes de travail à l'impératif.",
        exemples=[
            "Deux affirmatives, une interdiction, une avec un pronom.",
            "Vérifiez le trait d'union dans celle qui a un pronom.",
        ],
        notes="Corriger la forme du verbe et la place du pronom. Rendre avant D2, où ces "
              "consignes seront lues dans une vraie directive.")

    return d.save(dossier)
