# -*- coding: utf-8 -*-
"""C3 · « En me levant » — le gérondif.
Bloc C « Défi 2 » · couleur ambre · 75 min. Écriture.
Source : exercice `t2ger` et sa mini-leçon.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n5-rendezvous/images/')


def build(dossier):
    d = Deck(
        code='C3', section='ambre',
        titre="« En me levant » — le gérondif",
        chapeau="« À quel moment ? » n'est pas une question d'heure : c'est "
                "une question de circonstance. La réponse tient dans une "
                "seule forme, et elle fait souvent le diagnostic.",
        duree='75 minutes')

    d.titre(notes="Rendre les billets de C2. Puis relire la réplique de Rachid : « En me "
                  "levant du lit, surtout. » Demander au groupe ce que la docteure apprend "
                  "grâce à ces quatre mots.")

    d.objectifs([
        "former le gérondif à partir du « nous » du présent ;",
        "garder le pronom des verbes pronominaux ;",
        "employer le gérondif pour dire le moment et pour dire la manière ;",
        "vérifier que le sujet est le même que celui du verbe principal.",
    ])

    d.declencheur(
        'Observation', "« J'ai des étourdissements. » — « À quel moment ? » Qu'est-ce "
                       "que la docteure cherche ?",
        image=IMG + 'prelevement-bras.jpg',
        pistes=[
            "Le matin, ou en se levant ? Est-ce pareil ?",
            "En marchant, en se penchant, à l'effort : ça change quoi ?",
            "Pourquoi la circonstance compte-t-elle plus que l'heure ?",
            "Comment dit-on ça en un seul mot ?",
        ],
        notes="La deuxième piste est la clé : le matin est une heure, en se levant est un "
              "mouvement. Le médecin cherche le mouvement.")

    d.regle("Le « nous » du présent, moins -ons, plus -ant",
            "nous levons donne en levant · nous montons donne en montant · nous marchons donne en marchant",
            precision="Trois verbes seulement échappent à la règle : être donne en étant, "
                      "avoir donne en ayant, savoir donne en sachant. Tous les autres, sans "
                      "exception, suivent le « nous ».",
            notes="Diapositive à photographier. Faire fabriquer cinq gérondifs à voix "
                  "haute, en partant chaque fois du « nous ».")

    d.cartes("Deux emplois, une seule forme", "Le moment, et la manière", [
        ("Le moment",
         "« J'ai des étourdissements en me levant. » = quand je me lève, au même instant."),
        ("La manière",
         "« Levez-vous en comptant jusqu'à dix. » = voilà comment s'y prendre."),
        ("Qui dit quoi",
         "Le premier, c'est vous qui le dites au médecin. Le second, c'est lui qui vous le dit."),
        ("La règle du sujet",
         "Le gérondif et le verbe principal ont le même sujet. Sinon, il faut « pendant que »."),
    ], notes="Quand un professionnel explique quoi faire, ce sont les gérondifs qui "
             "portent la marche à suivre. Le dire : ça change l'écoute.")

    d.piege("Oublier le pronom d'un verbe pronominal",
            "« J'ai mal en levant. »",
            "« J'ai mal en me levant. »",
            "Sans le pronom, ce n'est plus vous qui vous levez : vous levez quelque chose. "
            "Le pronom reste toujours devant le participe — en me levant, en vous levant, "
            "en s'assoyant.",
            notes="C'est l'erreur numéro un du gérondif. Faire répéter les trois formes en "
                  "chœur, puis les faire écrire.")

    d.tableau('Quatre circonstances à savoir dire',
              "Elles orientent le médecin",
              ['La circonstance', 'Ce qu\'elle suggère'],
              [["en me levant du lit", "le passage couché donne debout"],
               ["en montant l'escalier", "l'effort"],
               ["en me penchant", "un autre mouvement, une autre piste"],
               ["en travaillant assis", "pendant une activité qui dure"]],
              cle=0,
              notes="Ne pas expliquer la médecine : dire seulement que ces quatre phrases "
                    "ne mènent pas au même examen. C'est assez pour justifier l'effort.")

    d.pratique('Écriture', "Mettez au gérondif",
               "Le verbe est entre parenthèses.", [
        ("J'ai des étourdissements ___ (se lever) du lit.", "en me levant"),
        ("Ça m'arrive aussi ___ (monter) l'escalier.", "en montant"),
        ("Levez-vous en deux temps, ___ (compter) jusqu'à dix.", "en comptant"),
        ("___ (appeler) vingt-quatre heures à l'avance, on évite les frais.", "En appelant"),
        ("Il a compris ___ (prendre) la tension deux fois.", "en prenant"),
        ("___ (être) à jeun, le résultat est plus fiable.", "En étant"),
        ("J'ai noté la date ___ (écouter) l'agente.", "en écoutant"),
        ("On perd sa place ___ (arriver) en retard.", "en arrivant"),
    ], corrige=True, cols=2,
       notes="La sixième est l'un des trois irréguliers. La faire repérer avant de "
             "corriger.")

    d.billet(
        "Écrivez deux phrases avec un gérondif : une pour le moment, une pour la manière.",
        exemples=[
            "« J'ai mal en… » — la circonstance où ça arrive.",
            "« On évite… en… » — la façon de s'y prendre.",
        ],
        notes="Les phrases de moment entrent dans le récit oral de E1. Le dire, et garder "
              "les billets.")

    return d.save(dossier)
