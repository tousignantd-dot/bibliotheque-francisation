# -*- coding: utf-8 -*-
"""Identité de module-n7-publicite — « Ce que la publicité ne dit pas » (niveau 7).

Situation « Publicité » du programme, domaine Culture et médias. Deux
intentions, et c'est deux fois la même phrase : **comprendre une publicité
comportant un message implicite**, une fois en écoutant, une fois en lisant.
Tout le module tient dans le mot *implicite*.

Pourquoi trois défis et non deux. La grille ne se déduit pas du nombre
d'intentions — le pilote du niveau 6 l'a écrit et le module du logement l'a
confirmé : le test est de pouvoir nommer trois façons distinctes d'entrer dans
la situation, chacune avec son dialogue et ses six exercices. Elles se nomment
sans peine ici, et la troisième n'est pas un canal de plus :

· ce qu'on **entend** — la publicité radio, son débit, sa mention légale ;
· ce qu'on **lit** — l'astérisque, les petits caractères, le prix annoncé ;
· ce qui **ne se présente pas comme une publicité** — le témoignage, la
  publication commanditée, la publicité qui vise un enfant, l'affichage.

Le troisième défi ne répète pas le deuxième : il change de statut juridique,
pas de support. C'est là que le module cesse d'apprendre à lire pour apprendre
à **reconnaître**, et c'est ce qui sépare le niveau 7 du niveau 4.

Ce qui distingue ce module de son voisin de situation, en une phrase, écrite
avant que le scénario soit inventé : `module-pub` (niveau 4) apprend à lire ce
que la publicité **dit** — quoi, quand, où, combien, pour qui ; celui-ci
apprend à repérer ce qu'elle **fait** — le procédé, l'astérisque, le
témoignage, la comparaison sans référence, l'influence. Au niveau 4, Solange
prépare une capsule et cherche l'information factuelle. Au niveau 7, Yamilé a
déjà signé, et elle veut comprendre pourquoi.

D'où viennent les productions. La situation n'a **aucune** intention de
production : ses deux intentions sont de compréhension. Les trois tâches de
« Je me lance » se tirent donc des **attentes de fin de cours** du niveau 7,
qui sont communes à tout le cours et qui, elles, sont productives — « en
classe, il fait un exposé informel sur un thème concret en fonction de ses
centres d'intérêts » (l'exposé qui démonte une publicité), « à l'aide d'un
modèle, il rédige une lettre de réclamation » (la lettre au marchand), et
« dans le contexte d'achat de biens, il manifeste sa déception et son
mécontentement en formulant une réclamation » (le jeu de rôle au téléphone).
C'est écrit ici pour que le relecteur suivant ne prenne pas ces tâches pour
une invention hors programme.

**Les faits québécois sont vérifiés, pas devinés** (23 août 2026), et aucune
entreprise n'est réelle :

· Loi sur la protection du consommateur — l'article **218** veut qu'on juge
  une représentation sur **l'impression générale** qu'elle donne et, s'il y a
  lieu, sur le sens littéral des mots ; l'article **219** interdit à tout
  commerçant, fabricant ou publicitaire de faire une représentation fausse ou
  trompeuse ; l'article **228** interdit d'**omettre un fait important** ;
  l'article **224 c)** veut que le prix annoncé soit le prix **tout inclus** —
  aucun frais ne peut s'y ajouter à la caisse, seules la TPS et la TVQ en sont
  exclues, et le prix total doit ressortir **plus nettement** que les montants
  qui le composent ; les articles **248 et 249** interdisent la publicité
  commerciale destinée aux personnes de **moins de 13 ans**, l'article 249
  donnant les trois critères qui servent à trancher : le **but** de la
  publicité, la **façon** de la présenter, et le **moment et l'endroit** où
  elle paraît. (Source : Office de la protection du consommateur.)
· Le **Code canadien des normes de la publicité** compte **quatorze
  articles** ; l'article 1 porte sur l'exactitude et la clarté, l'article 2 sur
  les **techniques de publicité déguisée** — aucune publicité ne doit être
  présentée dans un format qui cache qu'elle est une publicité —, l'article 3
  sur les réclamations de prix, l'article 6 sur la publicité comparative,
  l'article 7 sur les **témoignages**, qui doivent refléter l'opinion véritable
  et raisonnablement actuelle de la personne qui les donne, et l'article 12 sur
  la publicité destinée aux enfants. L'organisme s'appelle **Normes de la
  publicité** et reçoit les plaintes du public. (Source : Normes de la
  publicité ; page de l'Office de la protection du consommateur sur les normes
  canadiennes.)
· Charte de la langue française — l'affichage public et la publicité
  commerciale se font **en français** ; ils peuvent se faire à la fois en
  français et dans une autre langue, pourvu que le français y figure de façon
  **nettement prédominante**. Depuis le **1er juin 2025**, quand un nom
  d'entreprise ou une marque de commerce dans une autre langue paraît dans un
  affichage **visible de l'extérieur**, le texte français doit occuper un
  espace **au moins deux fois plus grand** et avoir une visibilité, une
  permanence et un éclairage équivalents. (Source : Office québécois de la
  langue française.)

Tout le reste est inventé : les personnes — Yamilé Betancourt, Réginald Nadon,
Doriane Pageau, Maxime Sarrazin, Valeria —, le Carrefour budgétaire de la
Rivière-du-Nord, et les cinq entreprises du module — Élan Cardio, Boréa
Literie, Croque-Lune, Trotti-Vent, Le Sillon. **Aucune marque réelle
n'apparaît nulle part**, ni dans les dialogues, ni dans les exercices, ni dans
les images.

**Une contrainte propre à ce module, et la trouvaille qu'elle a produite.**
La situation appelle des images qui portent du texte : une publicité *est* du
texte. Or la règle 1 des images de la vague 7 l'interdit, et pour une raison
qui ne se négocie pas — le modèle écrit du charabia, et l'élève de niveau 7 le
lit. La sortie n'est pas de contourner la règle mais de **déplacer le texte** :
le texte publicitaire se compose en HTML dans l'exercice, où il est correct,
relisible et modifiable, et l'image ne montre que la **scène autour** —
l'abribus vu de loin sous la neige, la boîte aux lettres qui déborde, le
téléviseur allumé dans un salon vide, la console du studio de radio. Le
gabarit sait afficher un bandeau, un encadré et un texte suivi (type `texte`) :
il n'a jamais eu besoin d'une image pour montrer une annonce.
"""

MANIFESTE = {
    'slug': 'module-n7-publicite',

    # `titre` et `niveau` viennent de `build/powerpoints/modules.py`.

    'theme': 'Publicité',

    # Indigo : la couleur du niveau 7. Elle ne se choisit pas — voir
    # `build/couleurs_niveau.py`.
    'accent': '#3B49A0',
    'accent_doux': '#E8EAFA',

    'ia_oral': "L'élève fait un exposé informel de deux minutes devant sa "
               "classe : il présente une publicité qu'il a rencontrée, dit ce "
               "qu'elle montre, puis ce qu'elle promet sans le dire, puis ce "
               "qu'elle ne dit pas du tout, et il conclut en nommant le "
               "procédé employé. Il vouvoie son auditoire, emploie des "
               "phrases emphatiques pour mettre en relief le procédé et des "
               "marqueurs de concession pour nuancer.",

    'jr_cas': 'abonnement',
    'jr_role': 'client',
    'jr_scenario': 'publicite',
    'ia_jeu_de_role': "L'élève téléphone au service à la clientèle d'une "
                      "entreprise après avoir vu une publicité : il expose "
                      "calmement ce que l'annonce laissait croire, demande ce "
                      "qu'elle ne disait pas, fait préciser les montants et "
                      "les délais, et demande une confirmation écrite. Il "
                      "emploie le conditionnel de politesse, la restriction "
                      "« ne… que » et des reformulations comme « autrement "
                      "dit ».",

    # L'apostrophe s'échappe : les deux valeurs sont injectées dans la même
    # chaîne JavaScript à guillemets simples.
    'bravo': "🎉 Bravo, vous avez terminé le module "
             "« Ce que la publicité ne dit pas » !",
    'relance': "Vous pouvez revenir sur n\\'importe quel onglet pour "
               "pratiquer encore.",

    'residus_interdits': ['module-consultation', 'Yannick', 'Rosalie', 'Beaulieu',
                          'tendinite', 'Consulter au bon endroit', 'physiothérapie'],
}
