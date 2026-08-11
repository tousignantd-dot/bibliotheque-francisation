# -*- coding: utf-8 -*-
"""C3 · Faire réparer : faire + infinitif.
Bloc C · couleur ambre (écriture) · 75 min.
Source : mini-leçon `t2faire`, exercices `t2faire`, `t2par` et `t2qui`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C3', section='ambre',
        titre='Faire réparer',
        chapeau="Dans un logement loué, vous ne réparez presque rien vous-même — c'est "
                "normal, et c'est même souvent interdit par le bail. Le français a une "
                "construction faite exactement pour cette situation.",
        duree='75 minutes')

    d.titre(notes="Séance très rentable : cette construction sert dans presque toutes les "
                  "phrases du module. La rattacher constamment au vécu des élèves.")

    d.objectifs([
        "employer faire suivi d'un infinitif pour dire qu'on fait faire l'action ;",
        "nommer la personne qui exécute le travail avec par ;",
        "conjuguer le verbe faire au présent, y compris ses deux formes irrégulières ;",
        "distinguer ce que je fais moi-même de ce que je fais faire.",
    ])

    d.regle('La nuance qui change tout',
            "« Je répare la serrure » et « je fais réparer la serrure » ne veulent pas dire la même chose.",
            precision="Dans le premier cas, j'ai les outils dans les mains. Dans le second, "
                      "quelqu'un vient la réparer et j'organise sa venue. Dans un logement "
                      "loué, c'est presque toujours la deuxième — et c'est aussi ce que "
                      "le bail prévoit.",
            notes="Ouvrir la séance là-dessus. Faire donner par le groupe trois choses "
                  "qu'ils font eux-mêmes et trois choses qu'ils font faire.")

    d.tableau('Analyse · 1 de 2', "faire + infinitif",
              ['Élément', 'Exemple', 'Remarque'],
              [["Sujet", "La propriétaire", "elle organise"],
               ["faire, conjugué", "fait", "seul verbe conjugué"],
               ["Verbe à l'infinitif", "venir un électricien", "il ne se conjugue jamais"]],
              cle=1,
              note="Les deux verbes se suivent directement, sans aucun mot entre eux. "
                   "La phrase complète : « La propriétaire fait venir un électricien. » "
                   "Elle ne vient pas elle-même : elle organise la venue.",
              notes="Insister sur « sans aucun mot entre eux » : c'est le premier piège.")

    d.tableau('Analyse · 2 de 2', "faire + infinitif + par",
              ['Élément', 'Exemple', 'Remarque'],
              [["Sujet", "Je", ""],
               ["faire + infinitif", "fais nettoyer", "les deux verbes collés"],
               ["Quoi", "le corridor", "ce sur quoi on agit"],
               ["Qui exécute", "par la compagnie d'entretien", "introduit par par"]],
              cle=1,
              note="Sans par, la phrase reste correcte : on ne dit simplement pas qui fait "
                   "le travail. C'est utile quand on ne le sait pas encore.",
              notes="Faire remarquer qu'on peut très bien dire « je fais nettoyer le "
                    "corridor » tout court. Le par est un ajout, pas une obligation.")

    d.tableau('Conjugaison', "Le verbe faire au présent",
              ['Personne', 'Forme', 'Attention'],
              [["je / tu", "je fais · tu fais", "régulier"],
               ["il / elle", "il fait · elle fait", "régulier"],
               ["nous", "nous faisons", "se dit « fe-zon », pas « fè-zon »"],
               ["vous", "vous faites", "pas de -ez, forme irrégulière"],
               ["ils / elles", "ils font · elles font", "court, comme sont et ont"]],
              cle=1,
              note="Vous faites est l'une des trois seules formes de ce type en français, "
                   "avec vous dites et vous êtes.",
              notes="Faire répéter « nous faisons » cinq fois : la prononciation est "
                    "contre-intuitive et personne ne la corrige spontanément.")

    d.pratique('Pratique', 'Complétez avec le verbe faire',
               "Attention à la personne et à la forme.", [
        ("La propriétaire ___ venir un électricien jeudi matin.", "fait"),
        ("Nous ___ installer un ventilateur dans la salle de bain.", "faisons"),
        ("Vous ___ réparer votre toiture par un couvreur.", "faites"),
        ("Les locataires du deuxième ___ changer leurs fenêtres.", "font"),
        ("Je ___ nettoyer le corridor par la compagnie d'entretien.", "fais"),
        ("Mon voisin ___ faire des travaux dans son appartement.", "fait — « faire faire » est correct"),
    ], corrige=True,
       notes="La dernière surprend toujours : « faire faire » est parfaitement correct "
             "quand on ne précise pas la nature des travaux.")

    d.piege('Rien entre les deux verbes',
            "Je fais à réparer la serrure.",
            "Je fais réparer la serrure.",
            "Rien ne se place entre faire et l'infinitif : ni à, ni de, ni rien d'autre. "
            "Les deux verbes se touchent. C'est une construction rare en français, où la "
            "plupart des verbes exigent justement une préposition — d'où l'erreur.",
            notes="Faire relire à voix haute cinq phrases correctes de suite pour installer "
                  "le rythme des deux verbes collés.")

    d.piege('Par, et non pour',
            "Je fais réparer la serrure pour le concierge.",
            "Je fais réparer la serrure par le concierge.",
            "Pour dirait que la réparation est un service rendu au concierge — comme si "
            "c'était sa serrure. C'est par qui indique qui exécute le travail. Une seule "
            "lettre de différence, et le sens s'inverse complètement.",
            notes="Faire produire les deux phrases avec la bonne intonation et demander au "
                  "groupe de dire, à chaque fois, qui tient le tournevis.")

    d.pratique('Pratique', 'Qui fait vraiment le travail ?',
               "Dans chaque phrase, qui exécute concrètement l'action ?", [
        ("La propriétaire fait réparer le toit.", "un couvreur, pas la propriétaire"),
        ("Je fais nettoyer le corridor par la compagnie d'entretien.", "la compagnie d'entretien"),
        ("Nous faisons installer un ventilateur.", "un installateur — non nommé ici"),
        ("Samir lave le plancher.", "Samir lui-même — pas de faire, donc il le fait"),
        ("Samir fait laver le plancher par le locataire.", "le locataire"),
    ], corrige=True,
       notes="Les deux dernières se comparent directement : même verbe, même personne, "
             "et pourtant deux situations opposées. C'est la meilleure vérification de "
             "la compréhension.")

    d.pratique('Pratique', 'Écrivez la phrase',
               "Employez faire + infinitif, et nommez qui exécute avec par.", [
        ("La toiture coule. La propriétaire organise la réparation.",
         "La propriétaire fait réparer la toiture par un couvreur."),
        ("Il n'y a pas de ventilateur. Vous organisez la pose.",
         "Vous faites installer un ventilateur par un installateur."),
        ("Le corridor est sale. Le concierge organise le nettoyage.",
         "Le concierge fait nettoyer le corridor par la compagnie d'entretien."),
        ("La serrure est brisée. Nous organisons le remplacement.",
         "Nous faisons changer la serrure par un serrurier."),
    ], corrige=True,
       notes="Production guidée. Accepter les variantes de vocabulaire ; corriger seulement "
             "la construction : faire conjugué, infinitif collé, par devant l'exécutant.")

    d.pratique('Vérification', 'Cinq questions rapides',
               "Répondez sans regarder vos notes.", [
        ("« La propriétaire fait réparer le toit. » Qui monte sur le toit ?", "un couvreur"),
        ("Nous ___ installer un ventilateur.", "faisons"),
        ("Je fais de réparer la porte, ou je fais réparer la porte ?", "je fais réparer la porte"),
        ("Pour dire qui exécute le travail, on emploie…", "par"),
        ("Vous ___ changer la serrure.", "faites"),
    ], corrige=True)

    d.billet(
        "Écrivez une phrase avec faire + infinitif + par, à propos de votre logement.",
        exemples=[
            "Trois éléments : qui organise · quel travail · qui exécute.",
            "Exemple : « Ma propriétaire fait changer les fenêtres par une compagnie. »",
        ],
        notes="Les billets réussis contiennent trois personnes différentes : celle qui "
              "parle, celle qui organise, celle qui exécute. C'est le critère de correction.")

    return d.save(dossier)
