# -*- coding: utf-8 -*-
"""Identité de module-n7-recherche — « Chercher un emploi en région » (niveau 7).

Situation « Recherche d'emploi » du programme, domaine Éducation et monde du
travail. Trois intentions seulement, et elles sont d'une netteté rare :
s'informer sur les **activités économiques régionales du Québec** en écoutant
(CO), s'informer sur les mêmes activités en lisant (CE), et **rédiger un
curriculum vitæ et une lettre d'accompagnement** (PE). Le module ne les élargit
pas : il les prend au mot.

D'où viennent les productions. La production écrite est l'intention même du
programme — le CV et la lettre. La production orale, elle, n'a aucune intention
dans cette situation : elle se tire des **attentes de fin de cours** du
niveau 7, qui sont productives et communes à tout le cours — « il expose les
avantages et les inconvénients de deux situations ou contextes pour prendre une
décision durant une négociation » et « en classe, il fait un exposé informel
sur un thème concret en fonction de ses centres d'intérêts ». D'où l'exposé de
deux minutes qui compare deux régions et conclut. Le jeu de rôle vient de la
même source : « au cours d'une entrevue de sélection […], il répond de façon
complète à des questions ouvertes concernant son expérience de travail, sa
formation et ses projets professionnels ».

Ce qui distingue ce module de ses deux voisins de situation — et la phrase a
été écrite avant que le scénario soit inventé :

· `module-n3-recherche-emploi` (activité 83) **offre ses services de vive
  voix** : on entre au commerce, on demande si on engage, on laisse son nom.
· `module-n6-recherche` (activité 59) **répond à une offre précise** : on lit
  l'annonce détaillée, on écrit sa lettre de motivation, on passe l'entrevue.
· Celui-ci, le niveau 7, **s'oriente avant de postuler** : on lit et on écoute
  l'économie d'une région pour décider *où* chercher, puis on taille son CV et
  sa lettre d'accompagnement pour ce marché-là. Le travail n'est plus de se
  présenter, c'est de comparer des territoires et de se rendre lisible pour
  celui qu'on a choisi.

Attention à ne pas empiéter sur `module-n7-emploi` (activité 109), écrit en
parallèle : « Recherche d'emploi », c'est **avant** l'embauche — l'offre, la
candidature, l'entrevue. « Emploi », c'est une fois en poste.

Les faits québécois sont vérifiés, pas devinés (22 août 2026) : l'Évaluation
comparative des études effectuées hors du Québec est un **avis d'expert** du
gouvernement du Québec qui n'est ni une équivalence de diplôme ni un permis
d'exercice ; la **salle multiservice** d'un bureau de Services Québec est
gratuite et donne accès à des postes informatiques, à de la documentation
régionale et à **IMT en ligne**, qui couvre plus de 500 métiers et professions
avec leurs salaires et leurs perspectives ; le portrait socioéconomique du
**Saguenay–Lac-Saint-Jean** publié par le gouvernement du Québec donne un PIB
régional de 15,5 G$, 137 100 emplois, une fabrication à 11,2 % de l'emploi
tournée vers la transformation des ressources naturelles, une construction à
8,9 % et un secteur primaire à 4,2 %, soit le double de la moyenne
québécoise ; les prestations régulières d'**assurance-emploi** valent 55 % de
la rémunération hebdomadaire moyenne assurable, le maximum de la rémunération
assurable est de 68 900 $ en 2026 et la prestation hebdomadaire maximale de
729 $. Tout le reste — les personnes, l'entreprise Alumico, les adresses, les
dates — est inventé.
"""

MANIFESTE = {
    'slug': 'module-n7-recherche',

    # `titre` et `niveau` viennent de `build/powerpoints/modules.py`.

    'theme': "Recherche d\\'emploi",

    # Indigo : la couleur du niveau 7. Elle ne se choisit pas — voir
    # `build/couleurs_niveau.py`.
    'accent': '#3B49A0',
    'accent_doux': '#E8EAFA',

    'ia_oral': "L'élève fait un exposé informel de deux minutes devant sa "
               "classe : il compare deux régions du Québec où il pourrait "
               "chercher du travail, expose les avantages et les "
               "inconvénients de chacune en s'appuyant sur des chiffres, puis "
               "annonce sa décision et la justifie. Il vouvoie son auditoire "
               "et emploie des comparatifs et des superlatifs de degré.",

    'jr_cas': 'labo',
    'jr_role': 'candidat',
    'jr_scenario': 'recherche',
    'ia_jeu_de_role': "L'élève téléphone à un employeur d'une autre région "
                      "pour s'informer avant de postuler : il se présente, "
                      "dit d'où il appelle, pose des questions ouvertes sur "
                      "le secteur, les quarts de travail et les exigences du "
                      "poste, explique en quoi son expérience s'y rattache, "
                      "et emploie le conditionnel de politesse.",

    # L'apostrophe s'échappe : les deux valeurs sont injectées dans la même
    # chaîne JavaScript à guillemets simples.
    'bravo': "🎉 Bravo, vous avez terminé le module "
             "« Chercher un emploi en région » !",
    'relance': "Vous pouvez revenir sur n\\'importe quel onglet pour "
               "pratiquer encore.",

    'residus_interdits': ['module-consultation', 'Yannick', 'Rosalie', 'Beaulieu',
                          'tendinite', 'Consulter au bon endroit', 'physiothérapie'],
}
