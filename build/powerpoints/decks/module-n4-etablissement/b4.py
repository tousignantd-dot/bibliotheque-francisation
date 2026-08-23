# -*- coding: utf-8 -*-
"""B4 · Ranger le message dans le temps, et le chronométrer
Bloc B « Défi 1 · Le répondeur du centre » · couleur ambre · 75 min.
Source du module : exercices `t1ordre` et `t1tri`, mini-leçon `t1ordre`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B4', section='ambre',
        titre="Ranger le message dans le temps",
        chapeau="D'abord, ensuite, enfin. Trois mots qui ne coûtent rien à "
                "dire et qui transforment un message confus en message "
                "clair, sans qu'un seul renseignement soit ajouté.",
        duree='75 minutes')

    d.titre(notes="Dernière séance du bloc B. Elle sert à assembler : la grammaire des "
                  "trois séances précédentes se déverse dans un message complet, qu'on "
                  "chronomètre à la fin. Prévoir un chronomètre projeté ou celui d'un "
                  "téléphone.")

    d.objectifs([
        "employer d'abord, ensuite et enfin pour ranger un message ;",
        "construire « avant de » et « après avoir » avec un infinitif ;",
        "trier ce qui a sa place dans un message d'une minute ;",
        "dire un message complet en cinquante secondes.",
    ], notes="Le troisième objectif est le plus utile et le moins grammatical. Y "
             "consacrer la deuxième moitié de la séance.")

    d.regle("Trois mots suffisent",
            "D'abord, je me nomme. Ensuite, je dis quel jour. Enfin, je "
            "laisse mon numéro.",
            precision="Sans eux, un message d'une minute ressemble à une "
                      "seule longue phrase.",
            notes="Diapositive à photographier. Faire dire les trois phrases par le "
                  "groupe entier, debout, deux fois. Elles seront la colonne "
                  "vertébrale de la production orale en E1.")

    d.cartes("Avant de, après avoir", "Deux mots pour deux actions", [
        ("Avant de + infinitif",
         "Avant de parler, attendez le signal sonore."),
        ("Après avoir + participe",
         "Après avoir écouté le menu, j'ai appuyé sur le 1."),
        ("Une seule condition",
         "La même personne fait les deux actions. Sinon, il faut une phrase complète."),
        ("Avec être",
         "Après être allée à la clinique, je suis rentrée. Le participe s'accorde."),
    ], notes="La quatrième carte anticipe D2. La signaler sans l'expliquer : l'accord "
             "du participe passé avec être aura sa séance entière.")

    d.tableau('Deux actions, deux sens', "La même paire, dans les deux ordres",
              ['Avant de', 'Après avoir'],
              [["Avant d'appuyer, écoutez le menu.", "Après avoir écouté le menu, appuyez."],
               ["Avant de parler, attendez le signal.", "Après avoir entendu le signal, parlez."],
               ["Avant de remettre la note, copiez-la.", "Après avoir fait la copie, descendez."],
               ["Avant de raccrocher, redites le numéro.", "Après avoir laissé le message, raccrochez."]],
              cle=1,
              notes="Masquer une colonne, faire produire l'autre. C'est l'exercice qui "
                    "installe la construction : dire la même chose dans les deux sens "
                    "fait cesser l'hésitation.")

    d.piege("Dire « avant parler »",
            "Avant parler, j'attends le signal.",
            "Avant de parler, j'attends le signal.",
            "Devant un verbe, c'est toujours « avant de ». Devant un nom, en "
            "revanche, on dit « avant le cours », sans « de ». Les deux "
            "constructions existent, et c'est le mot qui suit qui décide.",
            notes="Donner les deux exemples côte à côte au tableau : « avant le cours » "
                  "et « avant de commencer ». La règle se voit alors sans être "
                  "énoncée.")

    d.pratique('Complétez', "D'abord, ensuite, enfin, avant de, après avoir",
               "Un seul mot par phrase.", [
        ("___, je me nomme et je donne mon groupe.", "D'abord"),
        ("___, je dis quel jour je serai absente et pourquoi.", "Ensuite"),
        ("___, je laisse mon numéro de téléphone deux fois.", "Enfin"),
        ("___ parler, attendez le signal sonore.", "Avant de"),
        ("___ écouté le menu, elle a appuyé sur le 1.", "Après avoir"),
        ("___ raccrocher, redites votre numéro lentement.", "Avant de"),
    ], corrige=True,
       notes="Les trois premières se font en une minute. Prendre le temps sur les "
             "trois dernières : c'est la construction, pas le sens, qui demande du "
             "travail.")

    d.regle("Une minute, c'est beaucoup",
            "Cinq morceaux tiennent en cinquante secondes. Ce qui déborde, "
            "c'est l'explication.",
            precision="Personne ne vérifie votre motif. Personne ne le juge. "
                      "Une phrase suffit.",
            notes="Chronométrer devant le groupe : lire le message complet de Nourhane "
                  "à voix haute, à vitesse normale. Il fait quarante-huit secondes. La "
                  "démonstration règle la question mieux que l'argument.")

    d.pratique('Tri', "On la garde, ou on la coupe ?",
               "Dans un message d'une minute.", [
        ("Ici Nourhane Ouazzani, groupe 6, francisation de jour.", "on la garde"),
        ("Mon fils a commencé à pleurer vers deux heures du matin.", "on la coupe"),
        ("Je serai absente aujourd'hui, lundi le 14.", "on la garde"),
        ("Excusez-moi vraiment, je suis désolée, je m'excuse encore.", "on la coupe"),
        ("Je serai en classe demain matin.", "on la garde"),
        ("Vous pouvez me rappeler au 450 555-0147. Je répète.", "on la garde"),
    ], corrige=True,
       notes="Faire dire pourquoi on coupe, à chaque fois. Les deux raisons sont "
             "toujours les mêmes : c'est du détail, ou c'est de l'excuse. Ni l'un ni "
             "l'autre n'entre dans un dossier.")

    d.pratique('Assemblage', "Votre message, en cinq morceaux",
               "Reprenez votre billet de B1 et complétez-le.", [
        ("Morceau 1", "Bonjour, ici (nom complet), groupe (numéro), francisation."),
        ("Morceau 2", "Je vous appelle pour signaler (le mot) (la date exacte)."),
        ("Morceau 3", "Le motif, en une seule phrase."),
        ("Morceau 4", "Ce que vous ferez, au futur : je serai, je remettrai."),
        ("Morceau 5", "Mon numéro est le (...). Je répète : (...). Merci, bonne journée."),
    ], notes="Faire écrire les cinq morceaux, puis faire lire par paires, l'un tourné "
             "vers le mur. Chronométrer : viser entre quarante-cinq et soixante "
             "secondes. Ceux qui dépassent coupent l'explication, jamais le numéro.")

    d.billet(
        "Écrivez votre message complet, les cinq morceaux, et notez combien "
        "de secondes il vous prend.",
        exemples=[
            "Entre quarante-cinq et soixante secondes.",
            "Si vous dépassez, coupez dans le motif, jamais dans le numéro.",
        ],
        notes="Ramasser : c'est le brouillon de la production orale de E1. Le rendre "
              "annoté à la séance suivante plutôt que de le corriger en classe.")

    return d.save(dossier)
