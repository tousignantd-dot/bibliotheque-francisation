# -*- coding: utf-8 -*-
"""B3 · « Dire pourquoi »
Bloc B « Défi 1 · L'invitation » · couleur ambre · 75 min. Grammaire.
Source : exercice `t1just`, mini-leçon `t1just`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B3', section='ambre',
        titre="Dire pourquoi : parce que, comme, puisque, donc",
        chapeau="Au niveau 5, le programme ne demande plus seulement "
                "d'accepter ou de refuser : il demande de le faire avec "
                "justification. La difficulté n'est pas de trouver la "
                "raison — c'est de l'attacher à la réponse.",
        duree='75 minutes')

    d.titre(notes="Séance de grammaire, mais annoncée par un besoin réel : les refus "
                  "écrits ramassés en B2 contiennent presque tous une raison mal "
                  "attachée. En lire deux ou trois, anonymement, avant de commencer.")

    d.objectifs([
        "attacher une raison à une réponse avec le bon mot ;",
        "placer « comme » et « puisque » en tête de phrase ;",
        "distinguer la raison de la conséquence ;",
        "donner une raison en une seule phrase.",
    ], notes="Le message à faire passer : retenir la géométrie avant le sens. Qui sait où "
             "va chaque mot ne les confond plus.")

    d.regle("La place, avant le sens",
            "« Comme » et « puisque » ouvrent la phrase. « Parce que » se "
            "met au milieu. « Donc » annonce la conséquence.",
            precision="Comme je travaille ce jour-là, je ne pourrai pas venir. · "
                      "Je ne pourrai pas venir parce que je travaille ce jour-là. · "
                      "Je travaille ce jour-là, donc je ne pourrai pas venir.",
            notes="Diapositive à photographier. Écrire les trois phrases au tableau l'une "
                  "sous l'autre et faire remarquer que le sens ne change pas : seule la "
                  "place de la raison change.")

    d.cartes("Quatre mots, quatre emplois", "Ce qui les distingue vraiment", [
        ("parce que",
         "La réponse d'abord, la raison ensuite. Le plus courant, le plus sûr."),
        ("comme",
         "La raison d'abord, en tête de phrase. Jamais au milieu."),
        ("puisque",
         "Quand la raison est déjà connue de l'autre. Sinon, ça sonne comme un reproche."),
        ("donc",
         "La conséquence, jamais la raison. Test : remplacer par « c'est pourquoi »."),
    ], notes="La troisième carte est la plus subtile et la plus utile socialement : "
             "« puisque » employé avec une raison inconnue de l'interlocuteur donne "
             "l'impression qu'on lui reproche son ignorance.")

    d.tableau('La même raison', "Quatre attaches pour une seule idée",
              ['Le mot', 'La phrase'],
              [["parce que", "Je ne pourrai pas venir parce que je travaille."],
               ["comme", "Comme je travaille ce jour-là, je ne pourrai pas venir."],
               ["puisque", "Puisqu'il pleut, on reporte la fête au dimanche."],
               ["donc", "Je travaille ce jour-là, donc je ne pourrai pas venir."],
               ["c'est que", "Je ne pourrai pas venir : c'est que je travaille de nuit."]],
              cle=1,
              notes="La cinquième ligne est une tournure parlée, chaleureuse, qui prépare "
                    "l'autre à entendre une explication. Elle s'entend beaucoup au Québec "
                    "et elle rassure : elle annonce qu'une raison vient.")

    d.pratique('Grammaire', "Le mot qui manque",
               "Complétez avec parce que, comme, puisque, donc ou c'est que.", [
        ("J'accepte avec plaisir, ___ ça fait trois ans que je ne connais personne.", "parce que"),
        ("___ je travaille de midi à minuit, je ne pourrai pas venir.", "Comme"),
        ("Je travaille ce samedi-là, ___ je ne pourrai pas être là.", "donc"),
        ("___ vous finissez à trois heures, passez donc prendre un café.", "Puisque"),
        ("Je ne peux pas venir : ___ je pars au Sénégal ce jour-là.", "c'est que"),
        ("Le plat est pour vingt personnes, ___ j'ai besoin de deux plaques.", "donc"),
    ], corrige=True,
       notes="Exercice t1just de l'activité. Pour chaque réponse, faire justifier par la "
             "place du mot dans la phrase, jamais par le sens seul : c'est la place qui "
             "décide et qui se retient.")

    d.piege("Mettre « comme » au milieu de la phrase",
            "Je ne pourrai pas venir comme je travaille.",
            "Comme je travaille, je ne pourrai pas venir.",
            "« Comme » ouvre la phrase, toujours. Au milieu, il faut « parce que ». "
            "C'est l'erreur la plus fréquente, parce que dans beaucoup de langues le "
            "mot équivalent peut aller aux deux endroits.",
            notes="Faire retourner la phrase à voix haute plutôt que de la corriger : "
                  "l'élève entend alors que « comme » veut le début.")

    d.piege("Employer « puisque » pour une raison que l'autre ignore",
            "Puisque je pars au Sénégal... (dit à quelqu'un qui l'ignore)",
            "Je ne peux pas venir parce que je pars au Sénégal.",
            "« Puisque » suppose une raison partagée. Si l'autre ne la connaît pas, "
            "vous avez l'air de lui reprocher son ignorance.",
            notes="Nuance de registre, rarement enseignée et souvent ressentie. La faire "
                  "entendre en disant la mauvaise version avec le ton qui va avec.")

    d.billet(
        "Écrivez la même raison de deux façons : avec « parce que », puis avec « comme ».",
        exemples=[
            "Une raison vraie, tirée de votre semaine.",
            "Vérifiez que « comme » est bien au début de la deuxième phrase.",
        ],
        notes="Le billet vérifie exactement le point de la séance. Corriger seulement la "
              "place du mot ; laisser passer le reste.")

    return d.save(dossier)
