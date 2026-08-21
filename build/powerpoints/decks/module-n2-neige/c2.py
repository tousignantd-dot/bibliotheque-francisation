# -*- coding: utf-8 -*-
"""C2 · Quel temps fait-il ?
Bloc C « Défi 2 · Je m'habille pour dehors » · couleur ambre · 75 min.
Source : dialogue `t2b`, exercices `t2quest` et `t2b`, mini-leçon « Poser une
question sur le temps ».

Jusqu'ici, l'élève recevait le temps qu'il fait — la radio le disait, la mère
le disait. C2 lui donne la question, qui est la seule façon d'obtenir
l'information quand il n'y a pas de bulletin sous la main : à la porte, au
téléphone, à l'arrêt d'autobus.

La séance finit sur le jour de tempête, qui est la journée où toute cette
compréhension sert vraiment : trente centimètres, les autobus en retard, le
centre fermé — et la décision de ne pas sortir.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n2-neige/images/')

VOC = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n2-neige/vocab/')


def build(dossier):
    d = Deck(
        code='C2', section='ambre',
        titre="Quel temps fait-il ?",
        chapeau="Poser une question sur le temps, et comprendre un jour de "
                "tempête.",
        duree='75 minutes')

    d.titre(notes="Reprendre les trois phrases du billet de C1 : deux ou trois élèves "
                  "les lisent. Puis poser la question du titre au groupe, pour de "
                  "vrai, en regardant par la fenêtre.")

    d.objectifs([
        "poser la question « Quel temps fait-il ? » ;",
        "vérifier une seule chose avec « est-ce qu'il… ? » ;",
        "demander la température en degrés ;",
        "comprendre un avis de tempête et ce qu'il change.",
    ])

    d.declencheur(
        'Observation', "Trente centimètres de neige. Qu'est-ce qui change ?",
        image=IMG + 'temps-neige.jpg',
        pistes=[
            "Qu'est-ce qu'on voit sur la photo ?",
            "Est-ce que l'autobus passe à l'heure ?",
            "Est-ce que le cours a lieu ?",
            "Comment est-ce que vous le savez ?",
        ],
        notes="La quatrième piste est celle qui compte : la plupart des élèves ne "
              "savent pas où l'annonce de fermeture se trouve. Le montrer avant la "
              "fin de la séance.")

    d.regle("Quatre mots suffisent pour savoir",
            "Quel temps fait-il ?",
            precision="Pour vérifier une seule chose : « Est-ce qu'il neige ? » "
                      "Pour la température : « Il fait combien de degrés ? » Et "
                      "quand ça va trop vite : « Pouvez-vous répéter, s'il vous "
                      "plaît ? »",
            notes="Diapositive à photographier. Faire poser chacune des quatre "
                  "questions à voix haute, en faisant monter la voix à la fin.")

    d.tableau('Analyse', "Quatre questions, et à qui on les pose",
              ["La question", "Quand on s'en sert"],
              [["Quel temps fait-il ?", "La question complète, à n'importe qui."],
               ["Est-ce qu'il neige ?", "Pour vérifier une seule chose."],
               ["Il fait combien de degrés ?", "Quand on veut le nombre."],
               ["Il fait froid ?", "La version courte, celle qu'on entend le plus."],
               ["Pouvez-vous répéter ?", "Quand la réponse est allée trop vite."]],
              cle=1,
              note="La dernière rangée est la plus utile des cinq.",
              notes="Diapositive à photographier. Insister : demander de répéter n'est "
                    "pas un aveu d'échec, c'est une stratégie enseignée.")

    d.pratique('Pratique · 1', "Complétez la question",
               "Un mot par espace.", [
        ("___ temps fait-il aujourd'hui ?", "Quel"),
        ("Est-ce ___ il neige ?", "qu'"),
        ("Il fait ___ de degrés ?", "combien"),
        ("Pouvez-vous ___, s'il vous plaît ?", "répéter"),
        ("___ temps fait-il demain ?", "Quel"),
    ], corrige=True, cols=1,
       notes="Faire poser chaque question à un voisin après la correction, et "
             "obliger le voisin à répondre. Une question sans réponse ne s'apprend "
             "pas.")

    d.dialogue('Dialogue', "Ne sortez pas aujourd'hui", [
        ("ROLAND", "Madame Berrada ! Ne sortez pas aujourd'hui.", True),
        ("ZINA", "Pourquoi ? Il y a mon cours.", True),
        ("ROLAND", "Il y a une tempête. Trente centimètres de neige.", True),
        ("ZINA", "Et mon cours de français ?", True),
        ("ROLAND", "Le centre est fermé. C'est à la radio.", True),
        ("ZINA", "Ah bon. Alors je reste à la maison.", True),
    ], consigne="Écoutez, puis dites pourquoi Zina reste à la maison.",
       notes="Deux raisons, pas une : la tempête, et le centre fermé. Faire donner "
             "les deux avant de passer à la suite.")

    d.vocabulaire('Vocabulaire', "Les mots d'un jour de tempête", [
        ("une tempête", "Beaucoup de neige et beaucoup de vent, en même temps."),
        ("un centimètre", "La mesure de la neige tombée : trente centimètres."),
        ("fermé", "Le centre, l'école, la garderie n'ouvrent pas ce jour-là."),
        ("en retard", "L'autobus ne passe pas à l'heure écrite sur l'horaire."),
    ], notes="Diapositive à photographier. Montrer trente centimètres avec les mains : "
             "le nombre ne veut rien dire tant qu'on ne l'a pas vu.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après le dialogue de la tempête.", [
        ("Monsieur Pelchat dit de ne pas sortir.", "vrai"),
        ("Il tombe trente centimètres de neige.", "vrai"),
        ("Les autobus sont à l'heure.", "faux - ils sont en retard"),
        ("Le centre de formation est fermé.", "vrai"),
        ("Demain, il fait beau.", "vrai"),
    ], corrige=True, cols=1,
       notes="Le troisième est le seul faux. Faire repérer le mot qui le décide — "
             "« en retard » — plutôt que de le donner.")

    d.regle("Un jour de tempête, on reste à la maison",
            "Je ne sors pas. Je regarde à la radio si le centre est ouvert.",
            precision="L'annonce se fait le matin même, avant sept heures, à la "
                      "radio et sur le site du centre. Le lendemain, la neige est "
                      "encore là, mais le ciel est bleu : il fait souvent beau après "
                      "une tempête.",
            notes="Diapositive à photographier. Ouvrir le site du centre en direct et "
                  "montrer où l'avis apparaît. Deux minutes, et c'est le geste le "
                  "plus utile du module.")

    d.pratique('Pratique · deux par deux', "Est-ce qu'il y a de l'école ?",
               "Quinze minutes, debout. A appelle son voisin, B répond.", [
        ("Étape 1", "A demande : « Bonjour. Quel temps fait-il ce matin ? »"),
        ("Étape 2", "B répond avec le temps et la température."),
        ("Étape 3", "A demande : « Est-ce que le centre est ouvert ? »"),
        ("Étape 4", "A demande de répéter une fois, puis remercie."),
    ], cols=1,
       notes="L'étape 4 est obligatoire, même si A a tout compris : c'est la phrase "
             "qu'on veut voir sortir toute seule à la fin du module.")

    d.billet(
        "Trouvez où votre centre annonce les fermetures, et écrivez-le.",
        exemples=[
            "À la radio, à 6 h 30.",
            "Sur le site du centre.",
            "Mon enseignante envoie un message.",
        ],
        notes="Devoir de deux minutes, mais qui règle un vrai problème. Vérifier au "
              "début de E1 que chacun a une réponse.")

    return d.save(dossier)
