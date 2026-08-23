# -*- coding: utf-8 -*-
"""A4 · Retard, absence, abandon : trois mots, trois cases
Bloc A « Je découvre » · couleur ambre · 75 min.
Source du module : exercice `prMot` et sa mini-leçon.
"""
import os
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n4-etablissement/images/')


def img(nom):
    chemin = IMG + nom
    return chemin if os.path.exists(chemin) else None


def build(dossier):
    d = Deck(
        code='A4', section='ambre',
        titre="Retard, absence, abandon : trois mots, trois cases",
        chapeau="Quand vous téléphonez, la personne du secrétariat ouvre "
                "votre dossier et doit cocher quelque chose. Le système ne "
                "connaît que trois situations, et « je ne peux pas venir » "
                "n'en est aucune.",
        duree='75 minutes')

    d.titre(notes="Dernière séance du bloc A. Elle ferme le vocabulaire et ouvre le "
                  "bloc B. Commencer par écrire les trois mots au tableau, en colonne, "
                  "et demander au groupe de les définir avant toute explication : les "
                  "réponses montrent tout de suite où sont les confusions.")

    d.objectifs([
        "choisir le mot juste entre retard, absence et abandon ;",
        "employer « empêchement » quand la raison est privée ;",
        "dire une date exacte plutôt que « aujourd'hui » ;",
        "donner un motif en une seule phrase.",
    ], notes="Le troisième objectif paraît mineur et ne l'est pas : un message est "
             "écouté deux heures après avoir été laissé, et « aujourd'hui » n'a alors "
             "plus de sens.")

    d.regle("Nommez la case, pas votre embarras",
            "Un retard : vous venez plus tard. Une absence : vous ne venez "
            "pas. Un abandon : vous ne revenez plus.",
            precision="« Je ne peux pas venir » ne dit ni la durée, ni la "
                      "nature : la personne devra vous rappeler.",
            notes="Diapositive à photographier. C'est la règle la plus utile du bloc A, "
                  "et elle vaut aussi au travail, chez le médecin et à la garderie.")

    d.tableau('Les trois cases', "Ce que chacune déclenche",
              ['Le mot', 'Ce qui suit'],
              [["Un retard", "Rien à fournir. L'enseignant garde vos feuilles."],
               ["Une absence", "Une note écrite et signée, remise au comptoir."],
               ["Un abandon", "Un écrit, avant la date limite, sinon un échec."]],
              note="Trois mots, trois suites différentes. C'est pour cela qu'on "
                   "les distingue.",
              notes="Faire remarquer que le retard est le seul qui ne demande aucun "
                    "papier. Beaucoup d'élèves ne signalent pas leurs retards en "
                    "croyant que ce sera compliqué.")

    d.declencheur(
        'Observation', "Un arrêt d'autobus sous la neige, et pas d'autobus. "
                       "Qu'est-ce que vous faites ?",
        image=img('autobus-neige-arret.jpg'),
        pistes=[
            "Vous appelez, ou vous attendez de voir ?",
            "Vous dites que c'est un retard ou une absence ?",
            "À quelle heure appelez-vous : maintenant, ou en arrivant ?",
            "Qu'est-ce que vous dites en une seule phrase ?",
        ],
        notes="La troisième piste est celle qui compte : on appelle avant l'heure du "
              "cours, pas après. Un retard signalé à neuf heures et demie n'est plus un "
              "retard signalé, c'est une nouvelle.")

    d.cartes("Le mot poli pour tout le reste", "Quand la raison est privée", [
        ("Un empêchement",
         "Ce qui survient et vous empêche de venir, sans que ce soit votre choix."),
        ("Un empêchement familial",
         "Précisé, mais toujours sans détail. Personne ne demande la suite."),
        ("Ce que ça permet",
         "Rester exact sans rien raconter de sa vie privée."),
        ("Ce que ça ne remplace pas",
         "Le mot de la case : dites aussi si c'est un retard ou une absence."),
    ], notes="La quatrième carte évite un malentendu fréquent : « empêchement » donne "
             "la raison, pas la nature. On dit « je serai absente à cause d'un "
             "empêchement familial », les deux ensemble.")

    d.regle("La date, jamais « aujourd'hui »",
            "Dites le jour et le quantième : lundi le 14 septembre.",
            precision="Votre message est écouté deux heures plus tard, "
                      "parfois le lendemain.",
            notes="Faire dire à chacun la date du jour à voix haute, à la québécoise : "
                  "« lundi le 14 septembre ». La tournure surprend les élèves qui "
                  "viennent d'ailleurs et qui disent « lundi 14 ».")

    d.pratique('Le bon mot', "Complétez la phrase",
               "Retard, absence, abandon ou empêchement ?", [
        ("L'autobus n'est pas passé : j'aurai vingt minutes de ___.", "retard"),
        ("Je serai ___ toute la journée de lundi.", "absente"),
        ("Je vous écris pour vous annoncer mon ___ du cours du soir.", "abandon"),
        ("J'ai un ___ familial ce matin.", "empêchement"),
        ("Je devrai quitter à onze heures : ce n'est pas une ___ complète.", "absence"),
        ("Un ___ annoncé par écrit n'est pas un échec.", "abandon"),
    ], corrige=True,
       notes="La cinquième est celle qui divise le groupe. Trancher : un départ avant "
             "la fin se signale comme un départ, en donnant l'heure. Le centre n'a pas "
             "de case pour ça, mais l'enseignant, oui.")

    d.pratique('La phrase complète', "Une situation, une phrase",
               "Dites la phrase que vous laisseriez.", [
        ("Votre enfant est malade et vous allez à la clinique.",
         "Je serai absente aujourd'hui, lundi le 14, parce que mon fils est malade."),
        ("L'autobus n'est pas passé.",
         "J'aurai environ une heure de retard à cause de l'autobus."),
        ("Vous arrêtez le cours du soir.",
         "Je vous écris pour abandonner le cours d'informatique du soir."),
        ("La raison est privée.",
         "J'ai un empêchement familial ce matin et je serai absente."),
        ("Vous partez avant la fin du cours.",
         "Je devrai quitter à onze heures pour un rendez-vous."),
        ("Vous rapportez le papier d'hier.",
         "Je vous remets le papier qui justifie mon absence d'hier."),
    ], corrige=True,
       notes="Faire dire chaque phrase debout, à voix haute, comme au téléphone. Ce "
             "sont six phrases toutes faites : elles serviront telles quelles en E1.")

    d.piege("Raconter le détail",
            "Il a commencé à pleurer vers deux heures, après il a vomi, et là "
            "j'ai appelé Info-Santé...",
            "Mon fils est malade et j'ai un rendez-vous à la clinique.",
            "La boîte vocale coupe, la personne qui écoute a quarante messages, "
            "et l'essentiel se perd dans le milieu. Une phrase, une seule. "
            "Personne ne vérifie et personne ne juge.",
            notes="Ce piège vient d'une bonne intention : on croit qu'un motif détaillé "
                  "est un motif crédible. Dire au groupe que c'est l'inverse — un motif "
                  "court est un motif de personne qui sait comment ça marche.")

    d.billet(
        "Écrivez une phrase complète pour une absence que vous avez eue "
        "cette année, avec la date et le motif.",
        exemples=[
            "Une seule phrase, avec la date exacte.",
            "Le motif en une phrase, avec « parce que » ou « à cause de ».",
        ],
        notes="Ramasser les billets : ils servent en B1, où chacun transformera sa "
              "phrase en message complet de cinq morceaux.")

    return d.save(dossier)
