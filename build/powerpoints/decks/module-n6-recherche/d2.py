# -*- coding: utf-8 -*-
"""D2 · Développer une réponse.
Bloc D « Défi 3 · L'entrevue » · couleur teal · 75 min. Fin du Défi 3.
Source : exercices `t3subj`, `t3conn` et `t3dev`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='D2', section='teal',
        titre="Développer une réponse",
        chapeau="On ne développe pas en parlant plus longtemps : on développe "
                "en donnant un exemple. Cinq mots l'annoncent, et une forme de "
                "verbe permet de placer ce qu'on n'a pas demandé.",
        duree='75 minutes')

    d.titre(notes="Séance dense : deux points de langue et une recette. Prévoir de "
                  "consacrer la dernière demi-heure à la pratique orale par deux.")

    d.objectifs([
        "employer les cinq connecteurs d'exemplification ;",
        "distinguer « par exemple » de « c'est-à-dire » ;",
        "employer le subjonctif après un verbe qui l'exige ;",
        "développer une réponse courte en trois temps.",
    ])

    d.declencheur(
        'Observation', "« J'ai de l'expérience. »",
        pistes=[
            "L'employeur vous croit-il ?",
            "Que faudrait-il ajouter ?",
            "Un exemple ? Un chiffre ? Un résultat ?",
            "Combien de phrases, au total ?",
        ],
        notes="Partir des réponses courtes recueillies en D1. Les reprendre au tableau "
              "et les faire développer par le groupe.")

    d.tableau('Les cinq connecteurs', "Chacun annonce autre chose",
              ['Le mot', 'Ce qu\'il annonce'],
              [["par exemple", "un cas parmi plusieurs — le plus courant"],
               ["notamment", "un cas particulièrement important"],
               ["entre autres", "il y en a d'autres qu'on ne nommera pas"],
               ["c'est-à-dire", "une explication, pas un exemple"],
               ["ainsi", "la conséquence, le résultat"]],
              cle=0,
              note="Un ou deux par réponse suffisent. Au-delà, le discours a l'air récité.",
              notes="Diapositive à photographier. La distinction entre « par exemple » et "
                    "« c'est-à-dire » est celle qui demande le plus de reprises.")

    d.pratique('Application', "Quel connecteur ?",
               "Complétez avec le mot qui convient.", [
        ("Je faisais plusieurs tâches, ___ recevoir les livraisons.", "par exemple"),
        ("Je préparais les commandes, ___ celles qui partaient le lendemain.", "notamment"),
        ("Je signalais les écarts, ___ les différences entre le papier et la tablette.", "c'est-à-dire"),
        ("Une entreprise comparable à la vôtre, ___ par la taille.", "entre autres"),
        ("J'ai vérifié tous les bons ; ___ , j'ai trouvé l'erreur.", "ainsi"),
    ], corrige=True,
       notes="« c'est-à-dire » est le seul qui n'ajoute rien de neuf : il redit "
             "autrement. C'est ce qui le distingue, et c'est très utile quand on emploie "
             "un mot technique dont on n'est pas sûr.")

    d.regle("Le subjonctif après certains verbes",
            "Il faut que je sois disponible dès lundi.",
            precision="Après « il faut que », « j'aimerais que », « je souhaite que », "
                      "« je préfère que », le verbe change de forme. Quatre irréguliers "
                      "suffisent en entrevue : être donne « que je sois » · avoir donne « que j'aie » · "
                      "savoir donne « que vous sachiez » · pouvoir donne « que je puisse ». Les autres "
                      "verbes se forment sur la forme de « ils » au présent, moins -ent.",
            notes="Diapositive à photographier. Ne pas déborder : quatre verbes "
                  "irréguliers, et la recette pour les réguliers.")

    d.pratique('Application', "Mettez le verbe au subjonctif",
               "Attention au dernier item.", [
        ("J'aimerais que vous ___ que j'ai six ans d'expérience. (savoir)", "sachiez"),
        ("Il faut que je ___ disponible dès le mois prochain. (être)", "sois"),
        ("Je souhaite que l'équipe ___ compter sur moi. (pouvoir)", "puisse"),
        ("L'employeur exige que chaque commis ___ deux ans d'expérience. (avoir)", "ait"),
        ("J'espère que ma candidature vous ___ . (intéresser)", "intéresse — indicatif !"),
    ], corrige=True,
       notes="Le dernier item est le piège : « espérer que » ne prend pas le subjonctif, "
             "et c'est l'erreur la plus fréquente en lettre de motivation.")

    d.piege("« J'espère que vous soyez bien »",
            "J'espère que vous soyez bien.",
            "J'espère que vous allez bien.",
            "« Espérer » ressemble à « souhaiter » par le sens, mais ne se comporte pas "
            "comme lui : il demande l'indicatif ordinaire. L'erreur se voit à la première "
            "ligne d'un courriel professionnel, là où on est le plus lu.",
            notes="Faire redire la bonne forme trois fois. C'est un automatisme à "
                  "installer, pas une règle à comprendre.")

    d.tableau('Recette', "Développer en trois temps",
              ['Le temps', 'Ce qu\'on dit'],
              [["1. La situation", "Où, quand, combien de temps. « Dans mon dernier emploi, pendant six ans… »"],
               ["2. Ce que vous faisiez", "Des verbes d'action et un chiffre. « Je tenais l'inventaire de 800 références. »"],
               ["3. Le résultat", "Ce que ça a donné. « Ainsi, nous n'avons jamais manqué de matériel. »"]],
              cle=0,
              note="Trois phrases. Quarante secondes. C'est la longueur qu'un employeur attend.",
              notes="Diapositive à photographier. Faire pratiquer par deux, en "
                    "alternance, avec le chronomètre.")

    d.billet(
        "Développez trois réponses courtes en trois temps.",
        exemples=[
            "« J'ai de l'expérience. » · « Je suis travaillant. » · « Je parle un peu français. »",
            "La dernière se dit en positif : qu'est-ce que vous savez faire en français ?",
        ],
        notes="La troisième est la plus utile du module : elle apprend à parler de son "
              "français sans s'excuser.")

    return d.save(dossier)
