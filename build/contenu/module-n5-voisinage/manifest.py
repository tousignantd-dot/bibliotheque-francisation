# -*- coding: utf-8 -*-
"""Identité de module-n5-voisinage — « La ruelle en fête » (niveau 5,
activité 68).

Ce que le programme demande ici, et qui a décidé de la forme du module : la
situation « Relations sociales » du niveau 5 donne dix intentions, et une
seule d'entre elles est du bavardage. Recevoir des nouvelles (CO et CE) est
la porte d'entrée ; tout le reste est de l'action — accepter ou refuser
**avec justification** une offre ou une invitation, féliciter quelqu'un,
enregistrer un message d'accueil téléphonique, laisser un message
téléphonique, rédiger un mot à partir des notes prises en écoutant un
message, clavarder ou rédiger un bref courriel pour donner des nouvelles.
D'où trois défis qui suivent ces intentions plutôt que le fil d'une amitié :
l'invitation, le message, les félicitations.

Aucun lexique n'est fourni pour cette situation — le document de progression
du lexique ne la couvre pas. Les seize mots de FC_CARDS s'inventent à partir
des savoirs du niveau : « Conversation avec un voisin », « Acceptation ou
refus d'une offre ou d'une invitation », « Félicitations », « Dépôt ou
enregistrement d'un message dans une boîte vocale », « Partage de
renseignements par lettre ou par courriel à propos d'un projet à venir »,
« Organisation d'un évènement ».

Ce que ce module N'EST PAS, et pourquoi :

- ce n'est pas `module-relations` (48), au niveau 4, qui porte la même
  situation. Là-bas, deux inconnus se rencontrent dans une activité de loisir
  et se racontent leurs semaines et leur passé : personne n'a rien à demander,
  rien à refuser, rien à écrire. Ici l'échange se prolonge et se justifie — il
  y a une date, une heure, un plat à apporter, un oui ou un non à donner, et
  la moitié du module passe par le téléphone et par l'écrit ;
- ce n'est pas `module-n5-travail` (67), dont la boîte vocale et la note
  d'appel sont celles d'un bureau. Ici le répondeur est celui de la maison, le
  message se laisse à une voisine qu'on connaît, la note se laisse sur une
  table de cuisine, et les félicitations sont sincères plutôt que polies. Le
  module dit lui-même la différence, dans la mini-leçon `t2acc` ;
- ce n'est pas `module-n5-emmenagement` (63) ni `module-n5-degat` (62), où le
  voisinage est un problème à régler avec un propriétaire. Ici personne n'a de
  problème : c'est une fête, et la difficulté est sociale, pas administrative.

Le niveau 5 demande des **discours simples mais organisés**. D'où la
justification exigée à chaque acceptation et à chaque refus, le message
téléphonique reconstruit en mot écrit au discours rapporté, et les nouvelles
racontées au passé composé et à l'imparfait en trois ou quatre phrases
enchaînées — plutôt qu'une suite de questions-réponses.

Le vouvoiement est tenu du début à la fin, y compris dans l'écran de fin. Ce
n'est pas un choix de politesse mais un fait observable des immeubles
montréalais : entre voisins d'un même immeuble, on se vouvoie tant que
personne n'a proposé autre chose, même après des années. C'est aussi ce qui
distingue le module de son voisin du niveau 4, où l'on se tutoie d'emblée
entre participants d'une activité de loisir.

Les faits québécois employés sont réels : les ruelles vertes existent depuis
les années 1990 et sont aménagées par les arrondissements avec les riverains ;
la Fête des voisins se tient au Québec le premier samedi de juin ; le bac brun
recueille les résidus alimentaires ; la cérémonie de citoyenneté se termine
par le serment et la remise du certificat. L'immeuble, la ruelle, les
personnes, les dates et les numéros de téléphone sont inventés.
"""

MANIFESTE = {
    'slug': 'module-n5-voisinage',

    # `titre` et `niveau` viennent de `build/powerpoints/modules.py`.

    'theme': 'Relations sociales',

    # Sarcelle : la couleur du niveau 5. Posée par build/couleurs_niveau.py,
    # qui la relit dans colors.css — ne pas la choisir à la main.
    'accent': '#0D7A6F',
    'accent_doux': '#DCF2EF',

    'ia_oral': "L'élève laisse un message sur le répondeur d'une voisine "
               "pour l'inviter à la fête de la ruelle. Vérifier qu'il se "
               "nomme et dit d'où il appelle dès la première phrase, qu'il "
               "donne la date, l'heure et l'endroit, qu'il dit ce qu'il faut "
               "apporter, qu'il demande une réponse et dit comment on peut le "
               "joindre, et qu'il termine par une formule de politesse. "
               "Vérifier aussi le registre : vouvoiement tenu du début à la "
               "fin, ton chaleureux mais phrases courtes, une idée à la fois. "
               "Le message doit tenir en trente à quarante-cinq secondes : "
               "signaler ce qui est de trop plutôt que d'exiger un "
               "vocabulaire savant.",

    'jr_cas': 'invitation',
    'jr_role': 'invitee',
    'jr_scenario': 'voisinage',
    'ia_jeu_de_role': "L'élève parle avec un voisin de son immeuble. Il "
                      "demande ce qu'il ne sait pas — la date, l'heure, "
                      "l'endroit, ce qu'il faut apporter, ce qui arrive s'il "
                      "pleut — avant de répondre ; il donne ensuite un oui ou "
                      "un non clair, jamais un « on verra » ; il dit pourquoi "
                      "en une phrase, sans raconter sa vie ; et s'il refuse, "
                      "il propose lui-même autre chose plutôt que de laisser "
                      "l'invitation tomber. Quand la nouvelle est bonne, il "
                      "félicite avec une phrase exclamative avant de poser ses "
                      "questions. Le vouvoiement se tient du début à la fin.",

    'bravo': "🎉 Bravo, vous avez terminé le module « La ruelle en fête » !",
    'relance': "Vous pouvez revenir sur n\\'importe quel onglet pour "
               "pratiquer encore.",

    'residus_interdits': ['module-consultation', 'Yannick', 'Rosalie', 'Beaulieu',
                          'tendinite', 'Consulter au bon endroit', 'physiothérapie'],
}
