# -*- coding: utf-8 -*-
"""C2 · Le présent de l'indicatif.
Bloc C · couleur ambre (écriture) · 75 min.
Source : exercice `t2present` et sa mini-leçon.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C2', section='ambre',
        titre="Le présent de l'indicatif",
        chapeau="« J'ai mal », « je suis fatigué », « je peux marcher » : trois phrases "
                "de consultation, trois verbes irréguliers. Le présent est le temps de "
                "la salle d'attente.",
        duree='75 minutes')

    d.titre(notes="Séance de conjugaison. Commencer par faire dire au groupe cinq "
                  "phrases sur son état en ce moment. Relever les verbes employés au "
                  "tableau : ce seront presque toujours avoir, être et pouvoir.")

    d.objectifs([
        "conjuguer un verbe régulier en -er aux six personnes ;",
        "conjuguer avoir, être et pouvoir sans hésiter ;",
        "écrire la terminaison qu'on n'entend pas ;",
        "employer le présent pour décrire un symptôme actuel.",
    ])

    d.regle('Le temps de maintenant',
            "Le présent dit ce qui est vrai en ce moment : un symptôme, un état, une habitude.",
            precision="C'est le premier temps de toute consultation. Yannick l'emploie "
                      "d'un bout à l'autre : « j'ai mal », « je ne peux pas plier », "
                      "« nous sommes dans la salle d'attente ».",
            notes="Rappeler que le passé composé viendra plus tard, au module 2. Ici, "
                  "tout se dit au présent.")

    d.tableau('Analyse', "Les verbes réguliers en -er",
              ['La personne', 'La forme', 'La terminaison'],
              [["je", "je soulève", "-e"],
               ["tu", "tu soulèves", "-es"],
               ["il, elle", "elle soulève", "-e"],
               ["nous", "nous soulevons", "-ons"],
               ["vous", "vous soulevez", "-ez"],
               ["ils, elles", "elles soulèvent", "-ent"]],
              cle=2,
              notes="C'est le plus grand groupe de verbes du français. Faire remarquer "
                    "que quatre formes sur six se prononcent pareil : je, tu, il et ils. "
                    "La différence est écrite, pas entendue.")

    d.regle("La règle qui coûte le plus de points",
            "Les terminaisons -e, -es, -e et -ent se prononcent toutes de la même façon.",
            precision="« Il soulève » et « ils soulèvent » se disent exactement pareil. "
                      "À l'oral, personne ne peut vous corriger. À l'écrit, c'est "
                      "l'erreur la plus visible. Il faut donc regarder le sujet, pas "
                      "écouter le verbe.",
            notes="Diapo centrale de la séance. La laisser affichée pendant les deux "
                  "premiers exercices.")

    d.tableau('Analyse', "Trois verbes irréguliers, à savoir par cœur",
              ['avoir', 'être', 'pouvoir'],
              [["j'ai", "je suis", "je peux"],
               ["tu as", "tu es", "tu peux"],
               ["il a", "il est", "il peut"],
               ["nous avons", "nous sommes", "nous pouvons"],
               ["vous avez", "vous êtes", "vous pouvez"],
               ["ils ont", "ils sont", "ils peuvent"]],
              notes="Trois verbes, dix-huit formes. Ce sont les trois verbes les plus "
                    "fréquents du français : ce qui est appris ici sert partout ailleurs.")

    d.cartes('Ouvrir la mini-leçon', "Ce qui n'est pas dans le tableau", [
        ("Les accents de « soulever »",
         "Le e du radical prend un accent grave quand la terminaison est muette : je "
         "soulève, mais nous soulevons. Même chose pour « lever », « emmener »."),
        ("« pouvoir » au je et au tu",
         "Je peux, tu peux — avec un x, jamais un t. Le t apparaît seulement à la "
         "troisième personne : il peut."),
        ("Le présent pour une habitude",
         "« Je soulève des boîtes toute la soirée » ne décrit pas maintenant, mais "
         "chaque soir. Le présent sert aussi à ça."),
        ("Le présent pour un futur proche",
         "« Je reviens dans une semaine » se dit au présent, même si c'est dans le "
         "futur. Très courant en consultation."),
    ], notes="La quatrième carte surprend souvent. Faire trouver d'autres exemples : "
             "« je pars demain », « le médecin arrive dans dix minutes ».")

    d.pratique('Pratique · 1 de 3', 'Écrivez le verbe au présent',
               "Regardez le sujet avant d'écrire la terminaison.", [
        ("Yannick (avoir) ___ mal au genou depuis cette nuit.", "a"),
        ("Nous (être) ___ dans la salle d'attente.", "sommes"),
        ("Vous (pouvoir) ___ vous asseoir ici.", "pouvez"),
        ("Les employés (soulever) ___ des boîtes toute la soirée.", "soulèvent"),
        ("Je (prendre) ___ un numéro au triage.", "prends"),
        ("La docteure (examiner) ___ le genou.", "examine"),
    ], corrige=True,
       notes="La quatrième est celle qui décide : sujet pluriel, terminaison -ent qu'on "
             "n'entend pas. Faire souligner le sujet avant de corriger.")

    d.piege('Le piège du « nous »',
            "Nous soulève des boîtes.",
            "Nous soulevons des boîtes.",
            "Le sujet « nous » demande toujours la terminaison -ons, dans tous les "
            "verbes sauf « être ». C'est une terminaison qui s'entend : si vous la "
            "prononcez, vous ne l'oublierez pas à l'écrit.",
            notes="Faire dire « nous soulevons » à voix haute cinq fois. L'oreille "
                  "corrige ici mieux que la règle.")

    d.piege('Le piège du « je peux »',
            "Je peut vous aider.",
            "Je peux vous aider.",
            "« Pouvoir » prend un x au je et au tu, un t seulement au il. C'est une "
            "particularité de trois verbes seulement : pouvoir, vouloir, valoir. Elle "
            "s'apprend par la forme, pas par une règle générale.",
            notes="Écrire les trois verbes au tableau. Beaucoup d'élèves écrivent « je "
                  "veut » aussi : la même correction règle les deux.")

    d.pratique('Pratique · 2 de 3', 'Singulier ou pluriel ?',
               "Le verbe est écrit. Le sujet est-il singulier ou pluriel ?", [
        ("Ils examinent le patient.", "PLURIEL — terminaison -ent"),
        ("Elle examine le patient.", "SINGULIER — terminaison -e"),
        ("Vous avez de la fièvre.", "PLURIEL (ou vouvoiement)"),
        ("Il peut marcher.", "SINGULIER — terminaison -t"),
        ("Nous sommes en retard.", "PLURIEL — terminaison -ommes"),
        ("Tu es à la clinique.", "SINGULIER"),
    ], corrige=True, cols=2,
       notes="Exercice de lecture, pas d'écriture : on part de la terminaison pour "
             "retrouver le sujet. C'est le sens inverse de l'exercice précédent, et il "
             "installe la règle plus solidement.")

    d.pratique('Pratique · 3 de 3', "Décrivez votre état au présent",
               "Une phrase par situation, verbe conjugué correctement.", [
        ("Vous avez mal au dos depuis ce matin.", "J'ai mal au dos depuis ce matin."),
        ("Vous et votre collègue êtes fatigués.", "Nous sommes fatigués."),
        ("Votre voisin ne peut pas marcher.", "Il ne peut pas marcher."),
        ("Vos collègues soulèvent des charges tous les jours.",
         "Ils soulèvent des charges tous les jours."),
    ], corrige=True,
       notes="Faire écrire au tableau par quatre élèves différents. Corriger seulement "
             "la terminaison du verbe, rien d'autre.")

    d.billet(
        "Écrivez trois phrases au présent sur votre état en ce moment.",
        exemples=[
            "Une avec « avoir », une avec « être », une avec un verbe en -er.",
            "Soulignez la terminaison de chaque verbe.",
        ],
        notes="Corriger les terminaisons seulement. Les rendre à la séance suivante, "
              "avant l'exercice de négation : c'est la même conjugaison qui sert.")

    return d.save(dossier)
