# -*- coding: utf-8 -*-
"""Identité de module-n5-quebec — « Une semaine au Bic » (niveau 5,
activité 70).

Ce que le programme demande ici, et qui a décidé de la forme du module.
`build/cadre.py 5 "Déplacements dans tout le Québec"` rend **trois intentions
de communication**, et elles ne parlent pas du tout de circulation urbaine :
*s'informer sur les régions du Québec* et *échanger avec les vacanciers ou les
gens de la région visitée*, chacune en compréhension et en production orales,
puis *lire de l'information sur les régions du Québec* en compréhension
écrite. La situation, c'est donc **sortir de la ville** : on se renseigne, on
réserve, on lit, on part, et on parle à des gens qu'on ne reverra pas.

Les trois défis sont ces trois intentions, dans l'ordre où elles se
présentent à quelqu'un qui part :

1. se renseigner et réserver de vive voix, au comptoir de la gare d'autocars ;
2. lire ce qui est écrit sur la région — l'horaire, la fiche du parc, la
   politique de bagages, les tarifs ;
3. échanger sur place, avec l'hôtesse du gîte et avec un autre vacancier.

Le programme ne fournit **aucun lexique** pour cette situation ; le script le
dit au lieu d'afficher une liste vide. Les seize mots du banc sont donc
composés à partir des six points du savoir « Consultation et partage de
renseignements touristiques » — régions et caractéristiques régionales,
attraits, parcs, musées, loisirs, hébergement, restauration, bagages,
itinéraires, moyens de transport, dépliants et sites Web, commande ou
réservation en ligne — et des deux points de « Conversation avec des vacanciers
ou des personnes de la région visitée » : la conversation spontanée sur les
vacances et les salutations d'usage.

Ce que ce module N'EST PAS, et pourquoi :

- ce n'est pas `module-n5-transport` (69), livré deux heures plus tôt au même
  niveau. Celui-là est un module d'écoute : une voix de radio annonce que la
  route habituelle est bloquée, et tout le travail est de la comprendre du
  premier coup. Ici la route n'est pas bloquée, elle est simplement longue :
  il y a un horaire à lire, un billet à acheter, une valise à mettre en soute
  et cinq cents kilomètres à faire ;
- ce n'est pas `module-deplacement` (niveau 4), qui compose un trajet dans une
  ville et lit un plan de métro. Ici on quitte la ville pour une semaine, on
  ne cherche pas une station : on choisit une région, un moyen de transport et
  des dates ;
- ce n'est pas `module-n3-metro` (79), au niveau 3, qui achète un titre de
  transport à un guichet et repart le jour même.

Le niveau 5 demande des **discours simples mais organisés**. D'où l'exigence
tenue partout : l'élève ne pose pas une question à la fois, il expose une
demande complète — où il va, quand, pour combien de temps, à combien de
personnes, avec quels bagages — et il en écoute la réponse jusqu'au bout. La
même exigence à l'écrit : le courriel du module raconte un projet du début à
la fin, au futur simple, pas en trois phrases détachées.

Le vouvoiement et le tutoiement sont tenus chacun à leur place, et cette
frontière est une matière du module — le programme la nomme « salutations
d'usage ». Thuy tutoie Camille, sa collègue de cuisine ; elle vouvoie Serge au
comptoir, Rose-Aimée au gîte et Denis sur le sentier, et personne ne lui
propose de se tutoyer avant le dernier jour.

Les faits québécois employés sont réels et ont été vérifiés, jamais devinés :

- la **Gare d'autocars de Montréal** est au 1717, rue Berri, à l'angle de la
  rue Ontario, à côté de la station Berri-UQAM ; elle est ouverte 24 heures et
  son guichet est ouvert de 5 h 30 à 23 h 15 ; près de trois cents autocars y
  passent chaque jour ;
- **Orléans Express** est le principal transporteur interurbain du Québec ; son
  territoire va de Montréal à Gaspé en passant par Trois-Rivières, Québec, le
  Bas-Saint-Laurent et le Centre-du-Québec, avec des départs quotidiens ;
- sa **politique de bagages** : un bagage à main par personne, cinq kilos au
  maximum et cent quinze centimètres en dimensions linéaires, plus deux bagages
  en soute. Ce qui dépasse voyage par le service de messagerie **Expedibus**,
  au poids et selon la destination. La réservation se fait en ligne sur
  orleansexpress.com ou au téléphone, au 1 833 449-6444, tous les jours de
  l'année ;
- **l'Océan** de VIA Rail relie Montréal à Halifax trois fois par semaine — les
  départs de Montréal sont le mercredi, le vendredi et le dimanche à 18 h 30 —
  et il s'arrête à Rivière-du-Loup, Rimouski, Matapédia, Miramichi et Moncton.
  Le trajet complet jusqu'à Halifax dure une vingtaine d'heures ;
- le **parc national du Bic** est un parc de la Sépaq, dans le Bas-Saint-Laurent,
  à l'ouest de Rimouski : trente-trois kilomètres carrés de caps, de baies,
  d'anses, d'îles et de montagnes au bord du fleuve. Son camping compte quatre
  secteurs — Tombolo, Rioux, La Coulée et Rivière-du-Sud-Ouest — et l'on peut y
  louer du prêt-à-camper. La Sépaq gère vingt-trois parcs nationaux du Québec
  et un parc marin ;
- **Bonjour Québec** est le site touristique officiel du gouvernement du Québec.

Les personnes, le gîte, la résidence pour aînés, les heures de départ précises
et les prix cités dans les exercices sont inventés : un tarif change trop vite
pour être écrit dans un module, et le module apprend à le demander plutôt qu'à
le retenir.
"""

MANIFESTE = {
    'slug': 'module-n5-quebec',

    # `titre` et `niveau` viennent de `build/powerpoints/modules.py`.

    'theme': 'Déplacements dans tout le Québec',

    # Sarcelle : la couleur du niveau 5. Posée par build/couleurs_niveau.py,
    # qui la relit dans colors.css — ne pas la choisir à la main.
    'accent': '#0D7A6F',
    'accent_doux': '#DCF2EF',

    'ia_oral': "L'élève laisse un message sur la boîte vocale d'un gîte "
               "pour réserver une chambre et poser ses questions avant de "
               "partir en région. Vérifier six choses, dans cet ordre : il se "
               "nomme et dit d'où il appelle dès la première phrase ; il dit "
               "quelles dates et combien de nuits, avec des chiffres et non "
               "des « bientôt » ; il dit combien de personnes ; il pose deux "
               "questions au moins, formulées poliment — « Je voudrais "
               "savoir si… », « Pourriez-vous me dire à quelle heure… » ; il "
               "dit comment il arrivera, avec le moyen de transport et "
               "l'heure ; il laisse un numéro de téléphone, dit lentement. "
               "Vérifier aussi le registre : vouvoiement tenu du début à la "
               "fin, ton posé, une information par phrase. Le message doit "
               "tenir en trente à quarante-cinq secondes : signaler ce qui "
               "est de trop plutôt que d'exiger un vocabulaire savant.",

    'jr_cas': 'depart',
    'jr_role': 'prepose',
    'jr_scenario': 'regions',
    'ia_jeu_de_role': "L'élève prépare un voyage dans une région du Québec et "
                      "il parle à quelqu'un qui a l'information : un préposé "
                      "au comptoir des autocars, ou une personne qui habite la "
                      "région. Il doit tenir un discours organisé, pas poser "
                      "une question à la fois : où il va, quand, pour combien "
                      "de temps, à combien de personnes, et ce qu'il veut "
                      "savoir. Les dates et les heures se disent en chiffres. "
                      "Les questions se posent poliment, avec « Est-ce que je "
                      "pourrais… », « Je voudrais savoir si… », « Pourriez-vous "
                      "me dire… ». Les lieux se disent avec la bonne "
                      "préposition — à Rimouski, en Gaspésie, au "
                      "Bas-Saint-Laurent, dans les Laurentides. Le "
                      "vouvoiement se tient du début à la fin : ce sont des "
                      "inconnus.",

    'bravo': "🎉 Bravo, vous avez terminé le module « Une semaine au Bic » !",
    'relance': "Vous pouvez revenir sur n\\'importe quel onglet pour "
               "pratiquer encore.",

    'residus_interdits': ['module-consultation', 'Yannick', 'Rosalie', 'Beaulieu',
                          'tendinite', 'Consulter au bon endroit', 'physiothérapie'],
}
