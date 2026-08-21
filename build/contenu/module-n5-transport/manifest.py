# -*- coding: utf-8 -*-
"""Identité de module-n5-transport — « Ça bloque ce matin » (niveau 5,
activité 69).

Ce que le programme demande ici, et qui a décidé de la forme du module. La
situation « Déplacements dans une ville » du niveau 5 ne donne **qu'une seule
intention de communication**, et elle est en compréhension orale : *suivre un
bulletin de circulation routière*. Une seule. C'est peu, et c'est décisif : le
module n'est pas un module de déplacement, c'est un module d'écoute. On y
écoute une voix rapide annoncer que la route prévue ne passe plus, on en tire
ce qui touche son propre trajet, et on explique ensuite le détour et le retard
à quelqu'un qui n'a rien entendu.

Le savoir « Écoute d'un bulletin de circulation routière » du niveau donne
sept points de lexique et ils ont tous servi : l'état des routes ; les mots de
l'incident (carambolage, mise en portefeuille, embouteillage, bouchon,
ralentissement, détour) ; les directives (« Empruntez le pont X ») ; les types
de véhicules (remorqueuse, train routier, véhicule d'urgence) ; les mots de la
route (voie, accotement, chaussée, nid-de-poule) ; les villes et régions du
Québec ; la localisation temporelle et spatiale. Aucun lexique n'est fourni
pour la situation elle-même — la liste des seize mots s'invente à partir de ces
sept points.

Ce que ce module N'EST PAS, et pourquoi :

- ce n'est pas `module-deplacement` (niveau 4), qui porte la même situation.
  Là-bas on compose un trajet et on lit un plan de métro pour se rendre
  quelque part ; ici on ne cherche pas son chemin, on apprend que celui qu'on
  connaît est bloqué, et tout le travail est de comprendre une voix qui parle
  vite ;
- ce n'est pas `module-n3-metro` (79), au niveau 3, où l'on achète le bon
  titre de transport et où l'on demande son chemin à quelqu'un qui répond.
  Ici personne ne répond : un bulletin de circulation ne prend pas de
  questions, il faut le prendre tel qu'il vient, du premier coup ;
- ce n'est pas `module-n2-autobus` (niveau 2), qui lit une heure dans un
  horaire imprimé. Ici l'information n'est pas imprimée, elle est dite une
  fois, et la durée annoncée change pendant qu'on parle.

Le niveau 5 demande des **discours simples mais organisés**. D'où l'exigence
tenue partout : l'élève ne répond pas à des questions, il explique — ce qui
bloque, où exactement, depuis quand, pour combien de temps, par où passer à la
place et à quelle heure on arrivera. Six informations enchaînées, dans l'ordre,
c'est cela le module.

Le tutoiement et le vouvoiement sont tenus chacun à leur place et cette
frontière est elle-même une matière du module : Tereza et Amine se tutoient
parce qu'ils font la route ensemble tous les matins depuis deux ans ; Tereza
vouvoie Ghislaine Lachance, la responsable de l'atelier, à qui elle téléphone
pour annoncer son retard.

Les faits québécois employés sont réels et ont été vérifiés, jamais devinés :
Québec 511 est le service d'information routière du ministère des Transports
(ligne téléphonique 511 et site quebec511.info) ; le pont Jacques-Cartier et
le pont Samuel-De Champlain relient la Rive-Sud à Montréal, le pont-tunnel
Louis-Hippolyte-La Fontaine relie Montréal à la Rive-Sud par l'autoroute 25 ;
l'autoroute 40 s'appelle la Métropolitaine dans sa portion montréalaise et
l'autoroute 15 la Décarie ; la ligne jaune du métro relie Longueuil à
Berri-UQAM et la ligne orange dessert Du Collège et Côte-Vertu, à
Saint-Laurent ; le RTL est le réseau d'autobus de Longueuil et exo celui des
trains de banlieue ; on signale un nid-de-poule au 311 à Montréal ; les
nids-de-poule apparaissent au dégel, au printemps. Les personnes, l'atelier,
l'adresse, la station de radio et les heures sont inventés.
"""

MANIFESTE = {
    'slug': 'module-n5-transport',

    # `titre` et `niveau` viennent de `build/powerpoints/modules.py`.

    'theme': 'Déplacements dans une ville',

    # Sarcelle : la couleur du niveau 5. Posée par build/couleurs_niveau.py,
    # qui la relit dans colors.css — ne pas la choisir à la main.
    'accent': '#0D7A6F',
    'accent_doux': '#DCF2EF',

    'ia_oral': "L'élève laisse un message sur la boîte vocale de la "
               "responsable de son atelier pour annoncer qu'il sera en "
               "retard, à cause d'une entrave qu'il vient d'entendre au "
               "bulletin de circulation. Vérifier six choses, dans cet "
               "ordre : il se nomme et dit d'où il appelle dès la première "
               "phrase ; il dit ce qui bloque avec le mot juste — un "
               "accident, des travaux, un carambolage, une panne ; il dit "
               "où, avec une préposition juste — sur la 40, entre deux "
               "sorties, à la hauteur de, en direction de ; il dit depuis "
               "quand et pour combien de temps encore ; il annonce une "
               "heure d'arrivée en chiffres, jamais un « bientôt » ; il dit "
               "ce qu'il faut faire en attendant. Vérifier aussi le "
               "registre : vouvoiement tenu du début à la fin, ton calme, "
               "phrases courtes, une information à la fois. Le message doit "
               "tenir en trente à quarante-cinq secondes : signaler ce qui "
               "est de trop plutôt que d'exiger un vocabulaire savant.",

    'jr_cas': 'pont',
    'jr_role': 'collegue',
    'jr_scenario': 'circulation',
    'ia_jeu_de_role': "L'élève explique à quelqu'un qui n'a pas écouté la "
                      "radio ce qui bloque la route. Il doit tenir un "
                      "discours suivi, pas répondre à des questions : ce qui "
                      "bloque, où exactement, depuis quand, pour combien de "
                      "temps encore, par où passer à la place, et à quelle "
                      "heure on arrivera. « Ça bloque » ne suffit jamais : la "
                      "place se dit avec une préposition juste — sur "
                      "l'autoroute 40, entre la sortie X et la sortie Y, à la "
                      "hauteur du pont, en direction de l'ouest, dans les "
                      "deux sens. Le détour se dit dans l'ordre et jusqu'au "
                      "bout, pas par bribes. L'heure d'arrivée se dit en "
                      "chiffres. Le tutoiement se tient avec le collègue de "
                      "covoiturage, le vouvoiement avec la responsable de "
                      "l'atelier.",

    'bravo': "🎉 Bravo, vous avez terminé le module « Ça bloque ce matin » !",
    'relance': "Vous pouvez revenir sur n\\'importe quel onglet pour "
               "pratiquer encore.",

    'residus_interdits': ['module-consultation', 'Yannick', 'Rosalie', 'Beaulieu',
                          'tendinite', 'Consulter au bon endroit', 'physiothérapie'],
}
