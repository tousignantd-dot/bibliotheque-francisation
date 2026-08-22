# -*- coding: utf-8 -*-
"""C2 · Lire un texte suivi, et trier ce qu'il dit
Bloc C « Défi 2 · La biographie de la réalisatrice » · couleur teal · 75 min.
Source : exercices `t2texte` et `t2idees`, et leurs mini-leçons.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C2', section='teal',
        titre="Lire un texte suivi, et trier ce qu'il dit",
        chapeau="Un texte suivi ne se lit pas comme une liste de phrases. "
                "Chercher une réponse dans un texte, c'est retrouver un "
                "passage précis — pas se souvenir d'une impression.",
        duree='75 minutes')

    d.titre(notes="Deuxième séance du Défi 2. C'est la séance qui prépare l'exercice "
                  "de type « texte » de l'activité interactive : l'élève y clique "
                  "dans le texte le passage qui répond à chaque question.")

    d.objectifs([
        "retrouver dans un texte le passage exact qui répond à une question ;",
        "distinguer l'idée principale d'un paragraphe de ses détails ;",
        "ranger les dates d'une biographie sur une ligne du temps ;",
        "garder les chiffres qui expliquent, jeter ceux qui précisent.",
    ], notes="Le premier objectif est le geste de lecture du niveau 6 : on ne demande "
             "pas ce que le texte raconte, on demande où il le dit.")

    d.declencheur(
        'Observation', "Où, exactement, le texte répond-il à cette question ?",
        pistes=[
            "« Dans combien de salles le film est-il sorti ? »",
            "Trouve la phrase, puis souligne le passage précis.",
            "Combien de mots as-tu soulignés ?",
            "Est-ce que tu aurais pu répondre sans relire ?",
        ],
        notes="Faire souligner sur la feuille verte, physiquement. La différence entre "
              "« je crois que c'est huit » et un passage souligné est toute la "
              "séance.")

    d.tableau('Analyse', "La ligne du temps d'Aurélie Pichette",
              ['L\'année', 'Ce qui arrive'],
              [["1951", "naissance à Rimouski"],
               ["1972", "entrée dans une salle de montage, pour onze ans"],
               ["1979", "premier court métrage, projeté trois fois"],
               ["1994", "le long métrage sort dans huit salles"],
               ["2007", "elle cesse de tourner et se met à enseigner"],
               ["2016", "rétrospective à la salle Beauchemin"]],
              cle=0,
              note="Le texte ne donne pas ces dates dans cet ordre : c'est le lecteur qui les range.",
              notes="Diapositive à photographier. Faire construire la ligne du temps "
                    "par le groupe, au tableau, avant de projeter celle-ci.")

    d.regle("Chercher un passage, pas un souvenir",
            "À chaque question, on retourne au texte et on met le doigt dessus.",
            precision="C'est ce que l'activité interactive demande : choisir une "
                      "question, puis cliquer dans le texte le passage qui y répond. "
                      "Répondre de mémoire fonctionne une fois sur deux, et l'autre "
                      "fois on ne sait pas qu'on s'est trompé.",
            notes="Diapositive à photographier. Annoncer l'exercice 2 du Défi 2 dans "
                  "l'activité : c'est exactement ce geste-là, en version cliquable.")

    d.regle("L'idée principale et le détail",
            "Retire la phrase. Si le paragraphe tient encore debout, c'était un détail.",
            precision="L'idée principale répond à « de quoi parle ce paragraphe ? ». "
                      "Le détail répond à « quand ? combien ? où exactement ? ». Un "
                      "chiffre est presque toujours un détail — presque : onze ans de "
                      "montage porte tout le paragraphe, parce que c'est ce qui "
                      "explique la suite.",
            notes="Diapositive à photographier. Le test du retrait se fait à voix "
                  "haute, phrase par phrase, sur le premier paragraphe.")

    d.pratique('Compréhension', "Où le texte le dit-il ?",
               "Retrouvez le passage exact, puis recopiez-le.", [
        ("Qu'est-elle allée étudier à Montréal ?", "étudier la comptabilité à Montréal"),
        ("Combien de temps est-elle restée au montage ?", "y resta onze ans"),
        ("Qu'est-il arrivé à son premier court métrage ?", "ne fut projeté que trois fois"),
        ("Dans combien de salles le film est-il sorti ?", "dans huit salles seulement"),
        ("Où le film a-t-il été présenté en premier ?", "à Sherbrooke"),
        ("Qu'a-t-elle fait à la rétrospective ?", "elle refusa de parler avant la projection"),
    ], corrige=True,
       notes="Exiger le passage recopié, pas une reformulation. C'est la seule façon "
             "de vérifier qu'ils l'ont trouvé et non deviné.")

    d.pratique('Compréhension', "Idée principale ou détail ?",
               "Classez chaque phrase du texte.", [
        ("Elle a appris son métier au montage, et non dans une école.", "idée principale"),
        ("Elle est née à Rimouski en 1951.", "détail"),
        ("Son premier long métrage n'est venu qu'après quinze ans.", "idée principale"),
        ("Le court métrage durait douze minutes.", "détail"),
        ("La critique fut sévère, mais le public est revenu.", "idée principale"),
        ("Le film est sorti dans huit salles.", "détail"),
    ], corrige=True, cols=2,
       notes="Faire appliquer le test du retrait pour chaque item contesté. Le groupe "
             "discute surtout du premier : c'est bon signe.")

    d.piege("Chercher chaque mot inconnu au dictionnaire",
            "Je m'arrête à « rétrospective » et je cherche.",
            "Je continue, et je cherche à la fin du paragraphe.",
            "Un texte suivi se perd quand on s'arrête. Le sens d'un mot inconnu "
            "s'éclaire souvent trois lignes plus loin, et il ne coûte alors rien. "
            "S'arrêter à chaque mot coûte, lui, le fil du texte — qui est justement "
            "ce que le niveau 6 demande de tenir.",
            notes="Chronométrer les deux façons de faire sur le même paragraphe, en "
                  "classe. La démonstration est plus convaincante que l'argument.")

    d.billet(
        "Écris une question dont la réponse est dans la biographie.",
        exemples=[
            "Une question, et le passage qui y répond.",
            "On les échangera à la prochaine séance.",
        ],
        notes="Trois minutes. Les questions des élèves sont souvent meilleures que "
              "celles du manuel, et les échanger fait travailler deux fois.")

    return d.save(dossier)
