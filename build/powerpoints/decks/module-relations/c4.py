# -*- coding: utf-8 -*-
"""C4 · Le [t] qu'on entend et qu'on n'écrit pas.
Bloc C · couleur acier · 55 min.
Source : mini-leçon `t2liaison`, exercices `t2liaison` et `t2b`, dialogue `t2b`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C4', section='acier',
        titre="Le [t] qu'on entend et qu'on n'écrit pas",
        chapeau="« Je suis-t-arrivée ». Vous l'avez entendu, et vous avez "
                "cherché un mot qui n'existe pas. Ce [t] est réel, très "
                "fréquent — et il ne s'écrit jamais.",
        duree='55 minutes')

    d.titre(notes="Séance d'écoute courte. Prévoir le son. Elle clôt le bloc C et libère "
                  "beaucoup d'élèves d'une confusion qu'ils traînent depuis des mois.")

    d.objectifs([
        "reconnaître la liaison en [t] entre être et un participe passé ;",
        "savoir qu'elle ne s'écrit pas ;",
        "s'en servir comme indice : ce [t] annonce l'auxiliaire être, donc l'accord ;",
        "comprendre un récit au passé malgré cette liaison.",
    ])

    d.declencheur(
        'Écoute', "Qu'entendez-vous entre les deux mots ?",
        pistes=[
            "« Je suis arrivée le douze janvier. »",
            "« J'ai eu mal aux oreilles. »",
            "Dans laquelle des deux entendez-vous un petit [t] ?",
            "Ce [t], est-il écrit quelque part ?",
        ],
        notes="Faire écouter les deux extraits du module (exercice 4 du Défi 2) deux fois "
              "avant toute explication. Demander de lever la main quand on entend le [t].")

    d.tableau('Analyse', "Où le [t] apparaît",
              ['Ce qu\'on écrit', 'Ce qu\'on entend souvent'],
              [["je suis arrivée", "je suis-t-arrivée"],
               ["tu es allée", "tu es-t-allée"],
               ["je suis entrée", "je suis-t-entrée"],
               ["j'ai eu mal", "j'ai eu mal — pas de [t]"]],
              cle=3,
              note="La dernière ligne est la clé : avec avoir, ce [t] n'apparaît jamais.",
              notes="Faire lire la colonne de droite à voix haute par le groupe. "
                    "L'exagération aide ici.")

    d.regle("Ce que ce [t] vous apprend",
            "Si vous l'entendez, l'auxiliaire est être — donc le participe s'accorde.",
            precision="C'est un indice gratuit. « Je suis-t-arrivée » vous dit à l'oreille "
                      "qu'il faudra écrire un -e. « J'ai eu » ne le dit pas, et il n'y a "
                      "rien à accorder.",
            notes="Faire le lien explicite avec l'accord vu en C2. C'est la raison "
                  "pédagogique de cette séance.")

    d.regle('Faut-il le dire soi-même ?',
            "Non. Le reconnaître suffit.",
            precision="Cette liaison n'appartient pas au français soigné et n'est pas "
                      "obligatoire. Le programme du cours demande de la reconnaître, pour "
                      "comprendre ses interlocuteurs. Vous pouvez très bien ne jamais la "
                      "produire.",
            notes="Le dire clairement. Certains élèves voudront l'imiter pour « parler comme "
                  "ici » : ce n'est ni nécessaire ni déconseillé.")

    d.piege("Écrire le [t] qu'on entend",
            "Je suis t'arrivée le douze janvier.",
            "Je suis arrivée le douze janvier.",
            "Ce son n'existe qu'à l'oral. Entre l'auxiliaire et le participe, il n'y a "
            "rien à écrire. L'erreur vient presque toujours d'élèves qui apprennent "
            "beaucoup à l'oreille — c'est bon signe, mais il faut faire la correction.",
            notes="Rassurer : cette faute est le signe d'une bonne oreille, pas d'une "
                  "mauvaise mémoire.")

    d.pratique('Pratique', "Avec ou sans [t] ?",
               "Écoutez et dites si vous entendez la liaison.", [
        ("Je suis arrivée le douze janvier.", "[t] — auxiliaire être"),
        ("J'ai eu mal aux oreilles.", "pas de [t] — auxiliaire avoir"),
        ("Tu es allée au tournoi ?", "[t] — auxiliaire être"),
        ("J'ai compris ce jour-là.", "pas de [t] — auxiliaire avoir"),
        ("Je suis entrée dans le gymnase.", "[t] — auxiliaire être"),
        ("Elle a choisi son nom hier soir.", "pas de [t] — auxiliaire avoir"),
    ], corrige=True,
       notes="Utiliser l'exercice 4 du module. Deux écoutes avant de donner la réponse.")

    d.dialogue('Dialogue', "Le déménagement de Chantal", [
        ("CHANTAL", "J'ai déménagé neuf fois avant d'avoir trente ans.", False),
        ("CHANTAL", "Le pire, c'était le premier juillet il y a dix ans. Il pleuvait, on n'avait pas de camion.", True),
        ("CHANTAL", "Mon frère avait une petite voiture. On a fait onze voyages.", True),
        ("MARIAMA", "Et le nouvel appartement, il était comment ?", False),
    ], consigne="Repérez le décor et les évènements, comme en C2.",
       notes="Ce dialogue réutilise tout le bloc C : imparfait du décor, passé composé des "
             "évènements, et la fin du dialogue contient « à cause du bruit », qui annonce "
             "D2. Ne pas l'expliquer.")

    d.billet(
        "Écoutez une conversation cette semaine et notez une phrase où vous entendez ce [t].",
        exemples=[
            "À la radio, au travail, dans l'autobus.",
            "Écrivez la phrase correctement, sans le [t].",
        ],
        notes="Excellent point de départ pour D1 : lire deux ou trois relevés à voix haute.")

    return d.save(dossier)
