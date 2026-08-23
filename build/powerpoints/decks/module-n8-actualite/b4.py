# -*- coding: utf-8 -*-
"""B4 · Nommer la même chose autrement, et savoir d'où ça vient
Bloc B « Défi 1 » · couleur framboise · 75 min.
Source : exercices `t1nommer` et `t1source`, mini-leçon `t1nommer` (le
cadrage lexical), et les mots de vocabulaire de la tâche `t1`.
"""
from theme import Deck

import pathlib

IMG = str(pathlib.Path(__file__).resolve().parents[4]
          / 'assets' / 'interactive' / 'module-n8-actualite' / 'images') + '/'


def build(dossier):
    d = Deck(
        code='B4', section='framboise',
        titre="Le mot choisi n'est jamais neutre",
        chapeau="Deux journaux peuvent écrire sur les mêmes onze hectares "
                "sans employer un seul mot commun. Le lecteur croit avoir lu "
                "un fait : il a lu un choix de mots.",
        duree='75 minutes')

    d.titre(notes="Séance de vocabulaire et de lecture critique, dernière du bloc B. "
                  "Commencer par relire deux billets de B3 : les questions relevées "
                  "montrent déjà que le groupe lit autrement qu'au début du bloc.")

    d.objectifs([
        "reconnaître plusieurs façons de nommer une même chose ;",
        "dire ce que chaque désignation fait entendre ;",
        "choisir une désignation vérifiable quand on écrit soi-même ;",
        "rattacher chaque renseignement du reportage à sa source.",
    ], notes="Les trois premiers objectifs préparent la lettre du défi 3 ; le "
             "quatrième ferme le défi 1 et ouvre le défi 2, où l'on discutera une "
             "thèse plutôt que des chiffres.")

    d.declencheur(
        'Observation', "Trois hectares de gravier, ou l'ancienne cour de voirie ?",
        image=IMG + 'remblai-voirie.jpg',
        pistes=[
            "« un terrain vague à l'abandon »",
            "« l'ancienne cour de voirie de la Ville »",
            "« le terrain municipal du lot 3 214 »",
            "Laquelle des trois pourriez-vous aller vérifier ?",
        ],
        notes="La troisième est la seule vérifiable, et c'est la plus ennuyeuse des "
              "trois. Le faire remarquer : c'est un bon signe, et c'est la "
              "désignation à employer dans une lettre.")

    d.vocabulaire('Vocabulaire', "Quatre mots du défi 1", [
        ("un parti pris",
         "Le fait de pencher d'un côté avant même d'examiner la question."),
        ("une source",
         "La personne ou le document d'où vient un renseignement rapporté."),
        ("un boisé",
         "Un petit terrain couvert d'arbres, souvent en ville ou juste à côté."),
        ("un remblai",
         "Un terrain rempli de terre et de gravier rapportés, où presque rien ne pousse."),
    ], notes="Faire répéter chaque mot avec son article. Les deux derniers désignent "
             "les deux moitiés du même terrain : c'est déjà toute la leçon de la "
             "séance.")

    d.cartes('Analyse', "Trois familles de désignations", [
        ("Le mot neutre",
         "Le terrain municipal du lot 3 214. Onze hectares, dont quatre "
         "boisés. Administratif, ennuyeux, et vérifiable. Employez-le au "
         "moins une fois dans une lettre : cela montre que vous connaissez "
         "le dossier et pas seulement votre camp."),
        ("Le mot qui grossit ou qui rapetisse",
         "Le conseil a bradé un bien public. Le conseil a régularisé la "
         "situation d'un lot. Le conseil a cédé un terrain pour un dollar. "
         "Les trois se défendent ; un seul se vérifie."),
        ("Le mot qui contient déjà la conclusion",
         "Un saccage. Un enterrement. Un cadeau au promoteur. Il conclut à "
         "la place du lecteur, et c'est ce qui rend une lettre attaquable. "
         "Gardez-en un, au plus, et placez-le à la fin."),
    ], notes="Faire produire trois désignations du même objet par le groupe, sur autre "
             "chose que le boisé : un stationnement, une école fermée, une piste "
             "cyclable. Le procédé se voit mieux sur un objet sans enjeu.")

    d.tableau('Analyse', "Huit façons de nommer les mêmes onze hectares",
              ['La désignation', 'Ce qu\'elle fait entendre'],
              [["le boisé Sainte-Perpétue",
                "un lieu qui a un nom, donc une histoire"],
               ["un terrain municipal sous-utilisé",
                "une ressource qui dort et qu'on gaspille"],
               ["un actif de la Ville",
                "un bien qui s'évalue en dollars, donc qui se vend"],
               ["le poumon vert du quartier",
                "un organe vital dont la perte serait une atteinte"],
               ["l'ancienne cour de voirie",
                "un endroit déjà abîmé, qu'on ne perdrait pas"],
               ["le futur quartier Sainte-Perpétue",
                "une chose déjà faite, dont il reste à fixer la date"]],
              cle=0,
              notes="Diapositive à photographier. Faire classer les six en deux "
                    "colonnes, pour le projet et contre : le groupe y arrive sans "
                    "connaître le dossier, ce qui prouve que le mot travaille seul.")

    d.piege('Piège', "reprendre le mot de l'adversaire pour le contester",
            "le remplacer sans le commenter",
            "Écrire « ce n'est pas un terrain vague » installe quand même "
            "l'image du terrain vague dans la tête du lecteur, qui la "
            "gardera. Écrivez « le boisé », donnez le nombre d'arbres, et "
            "laissez l'autre mot de côté. Un texte qui n'emploie que le "
            "vocabulaire d'un camp ne convainc que ce camp.",
            notes="Défaut très fréquent dans les premières lettres. La personne qu'on "
                  "veut atteindre est celle qui hésite, et elle repère le vocabulaire "
                  "militant en trois lignes.")

    d.pratique('Pratique 1 de 2', "D'où vient ce qu'on vous dit ?",
               "La Ville, le comité, ou le promoteur ?", [
        ("Le rezonage du terrain de l'aréna prendrait vingt et un mois.", "la Ville"),
        ("Trois cent quarante-deux arbres ont été dénombrés.", "le comité"),
        ("Quatre-vingt-dix arbres seront abattus, replantés à deux pour un.", "le promoteur"),
        ("Le terrain coûtait onze mille dollars par année en entretien.", "la Ville"),
        ("Le financement du projet expire en mars.", "le promoteur"),
        ("Le vote a été pris à vingt-deux heures cinquante devant onze personnes.", "le comité"),
    ], corrige=True,
       notes="Faire ajouter à chaque réponse : est-ce que cette source est "
             "désintéressée sur ce point-là ? Aucune des trois ne l'est, et ce n'est "
             "pas une raison de rejeter le renseignement.")

    d.pratique('Pratique 2 de 2', "Récrivez de façon vérifiable",
               "Remplacez le mot chargé par ce qu'on peut aller vérifier.", [
        ("Le conseil a bradé le boisé.", "le conseil a cédé le terrain pour un dollar"),
        ("C'est un saccage.", "quatre-vingt-dix arbres au moins seront abattus"),
        ("Un cadeau au promoteur.", "une cession pour un dollar, contre quarante-cinq logements"),
        ("Ce n'est qu'un terrain vague.", "trois hectares de remblai, quatre hectares d'érables"),
    ], corrige=True,
       notes="Faire lire les deux versions à voix haute, l'une après l'autre. La "
             "version vérifiable est moins satisfaisante à dire et beaucoup plus "
             "difficile à contredire : c'est le marché qu'on propose aux élèves.")

    d.billet(
        "Écoutez la chronique de Grégoire Ferland avant la prochaine séance, et notez en une phrase ce qu'il pense.",
        exemples=[
            "Une seule phrase, et sans les mots « intéressant » ni « bizarre ».",
            "Notez aussi le moment où il donne raison au comité.",
        ],
        notes="Devoir, et entrée directe dans le bloc C : la phrase demandée est la "
              "thèse, et le moment repéré est la concession. Les deux se nommeront en "
              "C1 ; ici, on les fait seulement remarquer.")

    return d.save(dossier)
