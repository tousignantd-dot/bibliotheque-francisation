# -*- coding: utf-8 -*-
"""Identité de module-n5-ecole — « Régler une affaire au centre » (niveau 5).

La situation du programme est « Communication avec le personnel de
l'établissement », domaine général de formation « Éducation et monde du
travail ».  `build/cadre.py 5 "Communication avec le personnel de
l'établissement"` rend un cadre très étroit : **deux intentions**, la même des
deux côtés de l'oral — « Échanger avec le personnel pour régler un problème
scolaire » en compréhension comme en production — et une en compréhension
écrite, « Lire un avis ou un document scolaire officiel ». Aucun lexique
rattaché : la liste des seize mots est composée à partir des intentions et des
savoirs, comme le script le demande quand il n'a rien à donner.

Deux savoirs du niveau nomment presque le module à eux seuls : « Règlement
d'un problème dans le cadre scolaire » et « Lecture d'un avis ou d'un document
scolaire officiel ». Un troisième, « Dépôt ou enregistrement d'un message dans
une boîte vocale », a décidé de la forme de la production orale : au centre, la
personne qu'on cherche n'est jamais là, et un message clair vaut une visite.

Ce qui distingue ce module de ses voisins
-----------------------------------------

**Il n'y a pas de module de niveau 4 sur cette situation** — le programme ne la
porte qu'aux niveaux 1, 2, 3 et 5. Les voisins sont donc plus bas, et l'écart
est celui du stade : au niveau 2, `module-n2-inscription` remplit un formulaire
au comptoir et `module-n2-couloirs` demande où est le local ; au niveau 3,
`module-n3-secretariat` (activité 86, à venir) restera au comptoir lui aussi.
Tous trois demandent un **renseignement**, en question-réponse. Ici, l'élève
n'a rien à demander qu'on puisse lui dire en une phrase : il expose une
situation qui le regarde et qui **dure** — trois semaines d'absence à venir,
un horaire qui ne tient plus, une preuve à obtenir avant une date limite. Cela
demande un discours suivi, une trace écrite, et la lecture d'un avis officiel
qui, lui, ne se discute pas.

Le voisin du niveau 4 qui s'en rapproche le plus est `module-travail`
(activité 39, « Absent ou en retard : que faire ? ») : on y téléphone à son
employeur le matin même pour dire qu'on sera en retard. La différence tient en
deux mots — **prévu** et **écrit**. Ici, l'absence est annoncée trois semaines
d'avance, elle passe par un formulaire, elle produit un avis en retour, et
elle se règle avec une institution qui garde un dossier.

Les faits du Québec, vérifiés et tenus au générique
---------------------------------------------------

Le centre, les personnes, les rues, les dates et les numéros de dossier sont
**inventés** : le « Centre d'éducation des adultes des Trois-Ponts » n'existe
pas, et attribuer un règlement à un vrai centre serait faire dire à une
institution ce qu'elle n'a pas dit.

Ce qui est réel et se dit tel quel : depuis 2020, une **commission scolaire**
s'appelle un **centre de services scolaire** ; un centre d'éducation des
adultes offre la francisation à temps plein le jour et à temps partiel le
soir ; le **relevé des apprentissages** est le document officiel du ministère
et il ne s'imprime pas au secrétariat, contrairement à une **attestation de
fréquentation scolaire**, qui, elle, se demande sur place ; le sigle du cours
de niveau 5 est **LAN-4059-8**, il vient du programme lui-même. Les élèves
inscrits à temps plein en francisation reçoivent une **allocation de
participation** et doivent justifier leurs absences pour la garder — le module
le dit ainsi, sans montant ni délai chiffré, parce que ces valeurs-là changent
et qu'un module ne doit pas les figer.

Le tutoiement et le vouvoiement
-------------------------------

Le module **vouvoie** l'élève d'un bout à l'autre, écran de fin compris. C'est
le seul choix cohérent : tout le module se passe devant un comptoir, au
téléphone avec un secrétariat ou dans un courriel à une conseillère. Amelia
vouvoie le personnel, le personnel la vouvoie, et les consignes font de même.
Le seul tutoiement du module est celui de Koffi, le camarade de classe, dans
le dialogue d'entrée — et il est là exprès, pour que la bascule s'entende.
"""

MANIFESTE = {
    'slug': 'module-n5-ecole',

    # `titre` et `niveau` viennent de `build/powerpoints/modules.py`.

    # L'apostrophe est échappée : le thème est injecté dans une chaîne
    # JavaScript à guillemets simples au moment du dépôt de la production
    # orale. Non échappée, elle ferme la chaîne et l'envoi meurt.
    'theme': "Communication avec le personnel de l\\'établissement",

    # Sarcelle : la couleur du niveau 5. Elle ne se choisit pas — voir
    # `build/couleurs_niveau.py`.
    'accent': '#0D7A6F',
    'accent_doux': '#DCF2EF',

    'ia_oral': "L'élève laisse un message dans la boîte vocale du secrétariat "
               "d'un centre d'éducation des adultes pour annoncer une absence "
               "prévue. Il se nomme et donne son groupe dès la première "
               "phrase, il dit combien de temps il sera absent et à partir de "
               "quelle date, il donne le motif en une phrase, il annonce au "
               "futur simple ce qu'il fera à son retour, il demande un "
               "renseignement par une interrogative indirecte — « je voudrais "
               "savoir si… », « pourriez-vous me dire quand… » — et il laisse "
               "un numéro où le rappeler. Il vouvoie du début à la fin et il "
               "reste poli sans être long.",

    'jr_cas': 'absence',
    'jr_role': 'jocelyne',
    'jr_scenario': 'ecole',
    'ia_jeu_de_role': "L'élève se présente au secrétariat d'un centre "
                      "d'éducation des adultes pour régler une affaire qui le "
                      "concerne : une absence de trois semaines à annoncer, un "
                      "changement de groupe à demander, ou une attestation à "
                      "obtenir. Il expose sa situation d'un seul tenant, il "
                      "pose ses questions sans les transformer en questions "
                      "directes empilées, il comprend ce que le personnel lui "
                      "répond sur les formulaires et les délais, et il repart "
                      "en redisant ce qu'il doit faire et pour quand.",

    'bravo': "🎉 Bravo, vous avez terminé le module « Régler une affaire au "
             "centre » !",
    'relance': "Vous pouvez revenir sur n\\'importe quel onglet pour "
               "pratiquer encore.",

    'residus_interdits': ['module-consultation', 'Yannick', 'Rosalie',
                          'Beaulieu', 'tendinite', 'Consulter au bon endroit',
                          'physiothérapie'],
}
