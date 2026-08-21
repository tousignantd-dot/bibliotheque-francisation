# -*- coding: utf-8 -*-
"""Identité de module-n2-neige — « Il fait froid, je m'habille ».

Huitième module court du dépôt, septième du niveau 2. La situation du
programme est « Météo ». Elle n'a qu'**une seule** intention de
communication — « comprendre un bulletin météo », en compréhension écrite —
et c'est elle qui décide de tout : Défi 1 est le bulletin lui-même, Défi 2 est
ce qu'on en fait le matin, c'est-à-dire s'habiller autrement. Rien n'a été
ajouté autour.

Distinct de `module-meteo` (niveau 4, activité 42), qui lit un bulletin
détaillé et un avertissement de vigilance avec la poudrerie, le grésil, les
rafales et le facteur éolien : ici, trois mots et un chiffre suffisent — le
mot du temps, le nombre de degrés, et le signe qui est devant. Distinct aussi
de `module-n3-vetements` (niveau 3), qui essaie du linge dans un magasin et en
demande la taille : la tuque et les mitaines ne s'achètent pas ici, elles se
mettent avant de sortir.
"""

MANIFESTE = {
    'slug': 'module-n2-neige',

    # `titre` et `niveau` viennent de `build/powerpoints/modules.py`.

    'theme': 'Météo',

    # Couleur du niveau 2, posée par `build/couleurs_niveau.py`.
    'accent': '#A83A22',
    'accent_doux': '#FBEAE4',

    'ia_oral': "L'élève dit le temps qu'il fait ce matin : il choisit le mot "
               "du temps (il neige, il pleut, il vente, il fait beau, il fait "
               "froid), il donne la température en degrés avec « moins » ou "
               "« plus » devant, et il dit ce qu'il met pour sortir. Phrases "
               "très courtes, au présent, sans subordonnée. Le vouvoiement "
               "doit être tenu du début à la fin.",

    'jr_cas': 'matin',
    'jr_role': 'moi',
    'jr_scenario': 'meteo',
    'ia_jeu_de_role': "L'élève parle de la météo avec un voisin : il demande "
                      "le temps qu'il fait, il demande la température, il "
                      "répète le nombre de degrés pour vérifier, il demande "
                      "de répéter quand ça va trop vite, et il dit ce qu'il "
                      "met pour sortir.",

    'bravo': "🎉 Bravo, tu as terminé le module « Il fait froid, je m\\'habille » !",
    'relance': "Tu peux revenir sur n\\'importe quel onglet pour pratiquer "
               "encore.",

    'residus_interdits': ['module-consultation', 'Yannick', 'Rosalie', 'Beaulieu',
                          'tendinite', 'Consulter au bon endroit', 'physiothérapie'],
}
