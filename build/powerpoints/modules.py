# -*- coding: utf-8 -*-
"""
Le registre des modules produits par ce dossier
================================================

Un seul endroit dit, pour chaque module : son numéro, le titre affiché en pied
de page, l'ordre d'enseignement de ses séances et le nom de ses blocs. Tout le
reste — `build.py`, `build_fiches.py`, `theme.py`, `fiche.py`,
`build/materiel.py` — s'y rapporte au lieu de porter une constante à soi.

Le champ `niveau` dit à quel niveau du programme le module appartient. Il est
lu par `build/module.py` (qui le pose dans le HTML du module) et par
`build_fiches.py` (l'en-tête des fiches élèves) : aucun générateur ne doit
réécrire « niveau 4 » en dur. Les slugs restent **globalement uniques** — un
`module-sante` de niveau 6 devrait porter un autre slug, sinon il écraserait
celui du niveau 4, les dossiers de sortie étant à plat.

Le **slug** est la clé : c'est celui de `assets/interactive/<slug>/`, donc
celui de `assets/powerpoints/<slug>/` et le préfixe des fiches. C'est lui qui
relie un fichier produit à son activité dans le dépôt de matériel.

**Le nombre de séances suit le nombre de défis du module**, pas une grille
imposée : les modules à trois défis se répartissent 4-4-4-2-2, ceux à deux
défis 4-5-5-2. Seize séances dans les deux cas, mais un module qui n'a pas de
« Défi 3 » n'a pas de bloc D — inventer une séance sans contenu serait pire
que de n'en pas avoir.

Le module actif est posé par le script d'entrée (`choisir()`), avant que les
decks ne soient importés : ceux-ci font `from theme import Deck`, et `Deck`
lit ici son numéro et son titre.
"""

GRILLE_3_DEFIS = ['a1', 'a2', 'a3', 'a4', 'b1', 'b2', 'b3', 'b4',
                  'c1', 'c2', 'c3', 'c4', 'd1', 'd2', 'e1', 'e2']
GRILLE_2_DEFIS = ['a1', 'a2', 'a3', 'a4', 'b1', 'b2', 'b3', 'b4', 'b5',
                  'c1', 'c2', 'c3', 'c4', 'c5', 'e1', 'e2']
# Huit séances, deux blocs de quatre heures — le format des niveaux 1 et 2.
# Les deux grilles ci-dessus en font seize : c'est trop long pour un débutant
# qui n'a pas encore l'alphabet, et l'utilisateur a tranché en ce sens le
# 20 août 2026. Un bloc A de découverte, deux défis courts, une séance de
# production. Pas de bloc « Je retiens des mots » séparé : le vocabulaire se
# révise dans la dernière séance.
GRILLE_COURTE = ['a1', 'a2', 'a3', 'b1', 'b2', 'c1', 'c2', 'e1']


def _blocs(defi1, defi2, defi3=None):
    b = {'A': 'Je découvre', 'B': f'Défi 1 · {defi1}', 'C': f'Défi 2 · {defi2}',
         'E': 'Je me lance'}
    if defi3:
        b['D'] = f'Défi 3 · {defi3}'
    return b


MODULES = {
    'module-consultation': {
        'numero': 1, 'activite': 35, 'niveau': 4,
        'titre': 'Consulter au bon endroit',
        'chapeau': "Décrire une douleur, choisir le bon service, comprendre "
                   "les conseils.",
        'seances': GRILLE_3_DEFIS,
        'blocs': _blocs('Le triage', "L'examen", 'Le formulaire'),
    },
    'module-urgence': {
        'numero': 2, 'activite': 36, 'niveau': 4,
        'titre': 'Une urgence au travail',
        'chapeau': "Réagir vite, appeler le bon service, raconter ce qui est "
                   "arrivé.",
        'seances': GRILLE_3_DEFIS,
        'blocs': _blocs("À l'urgence", 'Les soins', "À l'accueil"),
    },
    'module-sante': {
        'numero': 3, 'activite': 34, 'niveau': 4,
        'titre': 'Prendre rendez-vous et aller à la pharmacie',
        'chapeau': "Appeler une clinique, dire comment on se sent, comprendre "
                   "les consignes du pharmacien.",
        'seances': GRILLE_2_DEFIS,
        'blocs': _blocs('À la pharmacie', 'La langue'),
    },
    'module-travail': {
        'numero': 4, 'activite': 39, 'niveau': 4,
        'titre': 'Absent ou en retard : que faire ?',
        'chapeau': "Prévenir son superviseur, justifier un retard, écrire un "
                   "courriel.",
        'seances': GRILLE_3_DEFIS,
        'blocs': _blocs('Le message', 'Le retard', 'Le courriel'),
    },
    'module-procedure': {
        'numero': 5, 'activite': 40, 'niveau': 4,
        'titre': 'Quelle est la procédure ?',
        'chapeau': "Comprendre une procédure, suivre des étapes, lire une "
                   "directive.",
        'seances': GRILLE_3_DEFIS,
        'blocs': _blocs('La demande de remboursement', 'Soumettre sa demande',
                        'Avez-vous lu les directives ?'),
    },
    'module-nouvelles': {
        'numero': 6, 'activite': 41, 'niveau': 4,
        'titre': "C'est l'heure des nouvelles",
        'chapeau': "Comprendre un fait divers à l'oral et à l'écrit, puis en "
                   "raconter un.",
        'seances': GRILLE_2_DEFIS,
        'blocs': _blocs('As-tu écouté les nouvelles ?',
                        "Qu'est-ce que tu lis ?"),
    },
    'module-meteo': {
        'numero': 7, 'activite': 42, 'niveau': 4,
        'titre': 'Quelles sont les prévisions ?',
        'chapeau': "Comprendre un bulletin, lire une alerte, décider d'une "
                   "journée de travail.",
        'seances': GRILLE_2_DEFIS,
        'blocs': _blocs('Le bulletin de six heures',
                        'Lire une alerte avant de partir'),
    },
    'module-pub': {
        'numero': 8, 'activite': 43, 'niveau': 4,
        'titre': 'Des publicités efficaces',
        'chapeau': "Reconnaître les éléments et les valeurs d'une publicité, "
                   "puis en écrire une.",
        'seances': GRILLE_2_DEFIS,
        'blocs': _blocs('Trente secondes en ondes',
                        'Deux affiches sur le babillard'),
    },
    'module-logement': {
        'numero': 9, 'activite': 44, 'niveau': 4,
        'titre': 'Comment est le logement ?',
        'chapeau': "Visiter, poser les bonnes questions, comparer deux "
                   "logements.",
        'seances': GRILLE_3_DEFIS,
        'blocs': _blocs('Poser les bonnes questions', 'Ce qui compte pour moi',
                        'Un logement pour chaque besoin'),
    },
    'module-probleme': {
        'numero': 10, 'activite': 45, 'niveau': 4,
        'titre': 'Pouvez-vous régler le problème ?',
        'chapeau': "Signaler un problème, faire respecter ses droits, se "
                   "plaindre efficacement.",
        'seances': GRILLE_3_DEFIS,
        'blocs': _blocs('Un problème dans le logement',
                        "Des problèmes dans l'immeuble",
                        'Une situation inacceptable'),
    },
    'module-relations': {
        'numero': 11, 'activite': 48, 'niveau': 4,
        'titre': 'Des nouvelles à donner',
        'chapeau': "Parler de ses semaines, raconter une expérience "
                   "personnelle, donner des nouvelles par écrit.",
        'seances': GRILLE_3_DEFIS,
        'blocs': _blocs('Ce que je fais de mes semaines',
                        "Ce que j'ai vécu",
                        'Donner des nouvelles'),
    },
    'module-deplacement': {
        'numero': 12, 'activite': 49, 'niveau': 4,
        'titre': 'Trouver son chemin',
        'chapeau': "Demander un itinéraire, le suivre, l'expliquer à son tour, "
                   "et comprendre les annonces en chemin.",
        'seances': GRILLE_3_DEFIS,
        'blocs': _blocs('Demander son chemin',
                        'Expliquer le chemin',
                        "Les messages qu'on entend"),
    },
    'module-activite': {
        'numero': 13, 'activite': 50, 'niveau': 4,
        'titre': "S'inscrire à une activité",
        'chapeau': "S'informer sur une activité, comprendre les consignes du "
                   "moniteur, lire un dépliant et s'inscrire.",
        'seances': GRILLE_3_DEFIS,
        'blocs': _blocs("S'informer sur une activité",
                        'Comprendre et donner des consignes',
                        "Le dépliant et l'inscription"),
    },
    'module-alimentation': {
        'numero': 14, 'activite': 51, 'niveau': 4,
        'titre': "Faire l'épicerie",
        'chapeau': "S'informer sur un produit, commander à un comptoir, lire "
                   "une étiquette et un mode d'emploi.",
        'seances': GRILLE_3_DEFIS,
        'blocs': _blocs("S'informer sur un produit",
                        'Commander à un comptoir',
                        "L'étiquette et le mode d'emploi"),
    },
    'module-achat': {
        'numero': 15, 'activite': 52, 'niveau': 4,
        'titre': 'Acheter un appareil',
        'chapeau': "S'informer sur un appareil, comprendre la garantie, le "
                   "paiement et la livraison, puis lire le mode d'emploi.",
        'seances': GRILLE_3_DEFIS,
        'blocs': _blocs("S'informer sur l'appareil",
                        'La garantie et la livraison',
                        "Le mode d'emploi"),
    },
    'module-restaurant': {
        'numero': 16, 'activite': 53, 'niveau': 4,
        'titre': 'Au restaurant',
        'chapeau': "Lire un menu, commander en salle à manger, demander ce "
                   "qu'il faut pendant le repas, et payer.",
        'seances': GRILLE_3_DEFIS,
        'blocs': _blocs('Lire le menu et commander',
                        'Pendant le repas',
                        "L'addition"),
    },
    'module-vetements': {
        'numero': 18, 'activite': 54, 'niveau': 4,
        'titre': 'Acheter des vêtements',
        'chapeau': "S'informer sur un vêtement, l'essayer, comprendre son "
                   "entretien, et savoir comment l'échanger.",
        'seances': GRILLE_3_DEFIS,
        'blocs': _blocs('Trouver sa taille',
                        "L'avis et l'entretien",
                        "Échanger et se faire rembourser"),
    },

    # ── Niveau 1 ────────────────────────────────────────────────────
    # Premier module court du projet : huit séances, deux défis, deux blocs
    # de quatre heures. Seize séances sont trop longues pour un grand
    # débutant qui n'a pas encore l'alphabet.
    'module-n1-presenter': {
        'numero': 1, 'activite': 56, 'niveau': 1,
        'titre': 'Je me présente',
        'chapeau': "Dire son nom et l'épeler, dire d'où on vient et ce qu'on "
                   "parle, saluer et remercier.",
        'seances': GRILLE_COURTE,
        'blocs': _blocs('Se présenter', 'Saluer et remercier'),
    },

    # Deuxième module du niveau 1. La situation du programme est « Salle de
    # classe », et le niveau 1 n'en tire que deux intentions, toutes deux en
    # compréhension orale : comprendre de l'information sur le fonctionnement
    # de la classe, et comprendre une consigne. Le module ne demande donc
    # jamais à l'élève d'expliquer quoi que ce soit — il écoute, il montre,
    # il fait. Distinct de `module-n2-classe` (89), qui traite la même
    # situation au niveau 2 : là-bas on lit une directive écrite, on demande
    # une permission, on annonce une absence et on explique le
    # fonctionnement de la classe à quelqu'un ; ici une consigne fait deux
    # mots, la réponse de l'élève est un geste, et le seul texte lu est
    # l'heure sur une horloge.
    'module-n1-classe': {
        'numero': 4, 'activite': 98, 'niveau': 1,
        'titre': 'Regardez le tableau',
        'chapeau': "Comprendre une consigne courte, nommer les objets de la "
                   "classe, comprendre l'heure du cours et l'horaire de la "
                   "semaine.",
        'seances': GRILLE_COURTE,
        'blocs': _blocs('La consigne', "L'heure et l'horaire"),
    },

    # Deuxième module du niveau 1. La situation du programme est
    # « Inscription », dont les deux intentions tiennent en une phrase
    # chacune : comprendre une demande de renseignements personnels et y
    # répondre ; lire un formulaire d'inscription et y transcrire des
    # renseignements. Distinct de `module-n1-presenter`, qui apprend à *dire*
    # son nom à l'oral : ici, on l'*écrit* dans une case, avec la date de
    # naissance, l'adresse abrégée et le téléphone. Distinct aussi de
    # `module-n2-inscription`, qui ajoute la petite annonce, le dialogue au
    # secrétariat et la case « scolarité » — au niveau 1, on ne quitte jamais
    # la fiche posée sur la table.
    'module-n1-inscription': {
        'numero': 2, 'activite': 96, 'niveau': 1,
        'titre': 'Je remplis ma fiche',
        'chapeau': "Comprendre une question sur son identité, y répondre, et "
                   "écrire ses renseignements dans les cases d'une fiche "
                   "d'inscription.",
        'seances': GRILLE_COURTE,
        'blocs': _blocs('Le nom et la date de naissance',
                        "L'adresse et le téléphone"),
    },

    # Troisième module du niveau 1. La situation du programme est
    # « Orientation dans l'établissement » et elle n'a **qu'une** intention de
    # communication, en compréhension écrite : décoder des panneaux avec ou
    # sans pictogrammes. Distinct de `module-n2-couloirs` (niveau 2,
    # activité 90), qui traite la même situation un niveau plus haut : là on
    # lit un plan mural, on comprend qu'un 214 est au deuxième étage et on
    # demande son chemin ; ici, l'élève ne va nulle part tout seul — il lit
    # une porte. Un dessin, un mot, une réponse.
    'module-n1-orientation': {
        'numero': 3, 'activite': 97, 'niveau': 1,
        'titre': 'Je lis les panneaux du centre',
        'chapeau': "Reconnaître le dessin d'un panneau, lire le nom du lieu "
                   "écrit à côté, et comprendre ce qui est permis ou interdit.",
        'seances': GRILLE_COURTE,
        'blocs': _blocs('Le mot sur la porte', 'Le panneau qui dit quoi faire'),
    },

    # ── Niveau 2 ────────────────────────────────────────────────────
    # Deuxième module court : huit séances, deux défis. Distinct de
    # `module-deplacement` (niveau 4), qui porte sur le trajet complet et le
    # métro ; ici, on demande son chemin et on lit un horaire d'autobus.
    'module-n2-autobus': {
        'numero': 1, 'activite': 57, 'niveau': 2,
        'titre': "Prendre l'autobus",
        'chapeau': "Demander son chemin, comprendre une direction, trouver "
                   "l'arrêt et lire l'horaire de l'autobus.",
        'seances': GRILLE_COURTE,
        'blocs': _blocs('Demander son chemin', "L'autobus et l'horaire"),
    },

    # Troisième module court du dépôt, deuxième du niveau 2. La situation du
    # programme est « Achat d'aliments ou de produits d'entretien », dont
    # l'unique intention est en compréhension écrite : lire une circulaire,
    # une étiquette, une affichette pour y repérer un prix et une mesure.
    # C'est ce qui le distingue de `module-n3-epicerie` (trouver, choisir,
    # payer) et de `module-alimentation` (niveau 4) : ici on ne parle presque
    # pas, on lit des chiffres et des formats avant de remplir son panier.
    'module-n2-panier': {
        'numero': 2, 'activite': 87, 'niveau': 2,
        'titre': 'Remplir mon panier',
        'chapeau': "Lire une circulaire, une étiquette et une affichette : "
                   "repérer le prix, le format et la quantité.",
        'seances': GRILLE_COURTE,
        'blocs': _blocs('Lire la circulaire', "L'étiquette et l'affichette"),
    },

    # Quatrième module court du dépôt, troisième du niveau 2. La situation
    # du programme est « Relations sociales ». Le niveau 1
    # (`module-n1-presenter`) apprend à dire son nom ; ici on entre dans un
    # échange court avec quelqu'un qu'on recroisera — on salue, on répond à
    # « ça va ? », on dit ce qu'on fait de sa journée, on comprend une demande
    # d'aide, on remercie et on souhaite. Distinct de `module-relations`
    # (niveau 4), qui tient une conversation suivie et raconte au passé.
    'module-n2-bonjour': {
        'numero': 3, 'activite': 88, 'niveau': 2,
        'titre': 'Bonjour, ça va ?',
        'chapeau': "Saluer un voisin, répondre à « ça va ? », dire ce qu'on "
                   "fait de sa journée, remercier et souhaiter.",
        'seances': GRILLE_COURTE,
        'blocs': _blocs('Ça va ? Et toi ?', 'Merci et bonne fête'),
    },

    # Cinquième module court du dépôt, quatrième du niveau 2. La situation du
    # programme est « Salle de classe », et ses trois intentions tiennent
    # toutes dans la même salle : comprendre une directive à l'oral et à
    # l'écrit, puis donner des renseignements sur le fonctionnement de la
    # classe. C'est la seule situation où l'élève parle de l'endroit où il est
    # assis : aucun module du dépôt ne la portait. Distinct de
    # `module-n2-bonjour`, qui salue un voisin dans un immeuble, et de
    # `module-procedure` (niveau 4), qui suit une marche à suivre écrite de
    # plusieurs étapes ; ici, une consigne fait trois mots et commence par un
    # verbe.
    'module-n2-classe': {
        'numero': 4, 'activite': 89, 'niveau': 2,
        'titre': 'Ouvrez votre cahier',
        'chapeau': "Comprendre une consigne, nommer les objets de la classe, "
                   "demander une permission et prévenir d'un retard.",
        'seances': GRILLE_COURTE,
        'blocs': _blocs("La consigne de l'enseignante",
                        'Permission, retard, absence'),
    },

    # Niveau 5 du programme au sens des situations : « Orientation dans
    # l'établissement ». Trois intentions seulement, et elles disent toutes la
    # même chose — se renseigner sur la localisation, en donner, lire le plan
    # d'un établissement de formation. Le module tient donc entièrement sur
    # les repères du bâtiment : un numéro de porte, un étage, un corridor.
    # Distinct de `module-n2-autobus` (57), qui est dehors et se repère à des
    # noms de rues ; distinct de `module-n2-classe` (89), qui ne quitte pas
    # une seule salle. Ici l'élève circule, et ce qui le guide est un chiffre.
    'module-n2-couloirs': {
        'numero': 5, 'activite': 90, 'niveau': 2,
        'titre': 'Où est le local 214 ?',
        'chapeau': "Lire le plan du centre, comprendre un numéro de porte, "
                   "demander son chemin et l'indiquer à quelqu'un.",
        'seances': GRILLE_COURTE,
        'blocs': _blocs('Le plan et les numéros',
                        'Demander son chemin'),
    },

    # Septième module court du dépôt, sixième du niveau 2. La situation du
    # programme est « Inscription ». Distinct de `module-n2-couloirs` (90),
    # qui circule dans le même bâtiment : ici, l'élève ne cherche pas une
    # porte, il remplit un papier — une annonce à lire, un formulaire à
    # remplir, un nom à épeler case par case.
    'module-n2-inscription': {
        'numero': 6, 'activite': 91, 'niveau': 2,
        'titre': "Je m'inscris au cours de français",
        'chapeau': "Lire une petite annonce de cours, prendre en note la date, "
                   "l'heure et le lieu, épeler son nom et remplir un "
                   "formulaire d'inscription.",
        'seances': GRILLE_COURTE,
        'blocs': _blocs('La petite annonce', "Le formulaire d'inscription"),
    },

    # Huitième module court du dépôt, septième du niveau 2. La situation du
    # programme est « Météo », et elle n'a qu'**une seule** intention :
    # comprendre un bulletin météo, en compréhension écrite. Tout le module
    # tient dans ce geste — trois mots et un chiffre — et dans ce qu'on en
    # fait le matin : s'habiller autrement. Distinct de `module-meteo`
    # (niveau 4), qui lit un bulletin détaillé et une alerte de vigilance ;
    # ici, l'élève cherche le mot du temps, le nombre de degrés et le signe
    # qui est devant.
    'module-n2-neige': {
        'numero': 7, 'activite': 92, 'niveau': 2,
        'titre': "Il fait froid, je m'habille",
        'chapeau': "Comprendre un bulletin météo simple, lire une "
                   "température au-dessus et au-dessous de zéro, dire le "
                   "temps qu'il fait et choisir ses vêtements pour la "
                   "journée.",
        'seances': GRILLE_COURTE,
        'blocs': _blocs('Le bulletin du matin', "Je m'habille pour dehors"),
    },

    # Neuvième module court du dépôt, huitième du niveau 2. La situation du
    # programme est « Transactions bancaires », et ses deux intentions
    # découpent le module d'elles-mêmes : « effectuer des opérations
    # courantes au guichet » en compréhension écrite, « libeller un chèque »
    # en production écrite. Distinct de `module-banque` (niveau 4), dont
    # l'élève va au comptoir, parle à un conseiller et compare des forfaits
    # dans une brochure ; ici, personne n'ouvre de compte : on lit six
    # phrases sur un écran, on tape quatre chiffres, on prend ses billets,
    # puis on remplit les cinq cases d'un chèque.
    'module-n2-guichet': {
        'numero': 8, 'activite': 93, 'niveau': 2,
        'titre': "Je retire de l'argent",
        'chapeau': "Suivre les phrases d'un guichet automatique, retirer un "
                   "montant en dollars, comprendre un relevé et des frais, "
                   "et remplir un chèque au complet.",
        'seances': GRILLE_COURTE,
        'blocs': _blocs('Au guichet automatique', 'Je fais un chèque'),
    },

    # Dixième module court du dépôt, neuvième du niveau 2. La situation du
    # programme est « Démarches à la poste », et son cadre décide de tout :
    # `build/cadre.py 2 "Démarches à la poste"` ne rend que **deux**
    # intentions, toutes les deux écrites — « lire et remplir un formulaire »
    # (compréhension et production écrites) et « adresser une enveloppe »
    # (production écrite). Défi 1 est donc l'enveloppe, Défi 2 le formulaire.
    # Distinct de `module-n3-poste` (niveau 3, activité 80), qui porte la même
    # situation un niveau plus haut : là-bas l'unique intention est orale — on
    # s'informe au comptoir, on compare deux vitesses, on demande un
    # mandat-poste. Ici la parole tient en trois mots et tout se joue sur le
    # papier : les cinq lignes d'une adresse, le code postal, les cases d'un
    # formulaire et l'endroit où l'on signe.
    'module-n2-colis': {
        'numero': 9, 'activite': 94, 'niveau': 2,
        'titre': "J'envoie une lettre et un colis",
        'chapeau': "Nommer ce qu'on envoie, écrire les cinq lignes d'une "
                   "adresse du Québec sur une enveloppe, remplir le "
                   "formulaire d'un colis et lire un avis de livraison.",
        'seances': GRILLE_COURTE,
        'blocs': _blocs("J'écris l'adresse", 'Je remplis le formulaire'),
    },

    # Dixième et dernier module du niveau 2. La situation du programme,
    # « Communication avec le personnel de l'établissement de formation »,
    # porte trois intentions : s'informer sur le fonctionnement du centre à
    # l'oral (comprise et produite), comprendre la même information à l'écrit,
    # et **lire un avis simple**. D'où les deux défis : le comptoir d'abord,
    # le papier affiché ensuite.
    #
    # À ne pas confondre avec `module-n3-secretariat` (niveau 3, activité 86),
    # qui traite la même porte avec des justifications, un billet du médecin
    # et du passé. Ici, on demande un papier en une phrase et on lit quatre
    # lignes sur une porte.
    'module-n2-secretaire': {
        'numero': 10, 'activite': 95, 'niveau': 2,
        'titre': 'Je vais au secrétariat',
        'chapeau': "Nommer le personnel du centre, trouver le secrétariat et "
                   "son local, demander un papier ou une heure au comptoir, "
                   "prévenir d'une absence et lire un avis affiché sur la "
                   "porte.",
        'seances': GRILLE_COURTE,
        'blocs': _blocs('Au comptoir du secrétariat',
                        "Je préviens et je lis l'avis"),
    },

    # ── Niveau 3 ────────────────────────────────────────────────────
    'module-n3-epicerie': {
        'numero': 1, 'activite': 55, 'niveau': 3,
        'titre': "À l'épicerie",
        'chapeau': "Trouver un produit, comprendre un numéro d'allée, lire la "
                   "circulaire et vérifier sa facture.",
        'seances': GRILLE_3_DEFIS,
        'blocs': _blocs('Trouver le produit',
                        'Choisir',
                        'À la caisse'),
    },

    # `module-vetements` (niveau 4, activité 54) traite la même situation du
    # programme, mais son élève essaie, demande un avis, lit l'étiquette
    # d'entretien et va se faire rembourser. Au niveau 3, les deux seules
    # intentions sont « s'informer sur un vêtement » et « lire une étiquette » :
    # on reste au plus concret — nommer le vêtement, dire sa taille, comparer
    # deux prix, et comprendre ce que le pictogramme interdit.
    'module-n3-vetements': {
        'numero': 2, 'activite': 75, 'niveau': 3,
        'titre': 'Magasiner du linge',
        'chapeau': "Nommer un vêtement et sa couleur, dire sa taille, "
                   "comparer deux prix et lire une étiquette.",
        'seances': GRILLE_3_DEFIS,
        'blocs': _blocs("Demander ce qu'on cherche",
                        'Comparer deux prix',
                        "L'étiquette et le paiement"),
    },
    'module-n3-electro': {
        'numero': 3, 'activite': 76, 'niveau': 3,
        'titre': 'Acheter un appareil',
        'chapeau': "Lire une circulaire, trouver le rayon, demander le prix "
                   "d'un appareil, payer et faire livrer.",
        'seances': GRILLE_3_DEFIS,
        'blocs': _blocs('Lire la circulaire',
                        'Trouver le rayon et demander',
                        'Payer et faire livrer'),
    },
    'module-n3-restaurant': {
        'numero': 4, 'activite': 77, 'niveau': 3,
        'titre': 'Commander au comptoir',
        'chapeau': "Lire le tableau du menu, commander un format au "
                   "comptoir, comprendre le préposé et demander ce qui "
                   "manque.",
        'seances': GRILLE_3_DEFIS,
        'blocs': _blocs('Lire le menu',
                        'Commander au comptoir',
                        'Comprendre le préposé'),
    },
    # Au niveau 3, la pharmacie tient tout un module, sans médecin : le
    # programme n'y met que trois intentions, et elles sont étroites —
    # « décrire un problème de santé courant » et « demander le renouvellement
    # de l'ordonnance d'un médicament » en production orale, « lire une
    # posologie » en compréhension écrite. Les trois défis sont ces trois
    # intentions, dans cet ordre.
    #
    # `module-consultation` (niveau 4, activité 45) mêle la pharmacie au
    # rendez-vous médical : on y choisit le bon endroit où consulter, on
    # raconte l'histoire de son mal, on remplit des formulaires. Ici, il n'y a
    # ni médecin, ni salle d'attente, ni papier à remplir : il y a deux
    # comptoirs, une carte d'assurance maladie et une étiquette à lire.
    'module-n3-pharmacie': {
        'numero': 5, 'activite': 78, 'niveau': 3,
        'titre': 'Aller à la pharmacie',
        'chapeau': "Dire ce qui ne va pas depuis quand, faire renouveler une "
                   "ordonnance et lire la posologie sur l'étiquette.",
        'seances': GRILLE_3_DEFIS,
        'blocs': _blocs('Dire ce qui ne va pas',
                        "Renouveler l'ordonnance",
                        'Lire la posologie'),
    },
    # Au niveau 3, « Déplacement dans une ville » n'a que trois intentions et
    # elles disent toutes la même chose : demander, comprendre et lire
    # l'information **pour acheter un titre de transport**. Le module ne parle
    # donc pas du trajet — pas d'itinéraire, pas de direction, pas de
    # terminus : un comptoir, une carte, une grille de tarifs et de l'argent.
    #
    # Trois voisins, et aucun recoupement. `module-deplacement` (niveau 4)
    # fait le trajet complet et ne s'arrête à aucun guichet ;
    # `module-n2-autobus` (niveau 2) demande son chemin et lit un horaire ;
    # `module-n2-couloirs` (niveau 2) se repère aux numéros d'un bâtiment.
    'module-n3-metro': {
        'numero': 6, 'activite': 79, 'niveau': 3,
        'titre': 'Le bon titre de transport',
        'chapeau': "Comprendre les titres et les prix qu'on vous nomme au "
                   "comptoir, acheter le bon titre pour ses déplacements et "
                   "lire la grille des tarifs affichée.",
        'seances': GRILLE_3_DEFIS,
        'blocs': _blocs("Comprendre ce qu'on me répond",
                        'Demander au guichet',
                        'Lire la grille des tarifs'),
    },
    # `build/cadre.py 3 "Démarches à la poste"` est le cadre le plus étroit de
    # tout le niveau : **une seule intention de communication**, « s'informer
    # pour obtenir un produit ou un service », inscrite deux fois — en
    # compréhension orale et en production orale. Aucune compréhension écrite,
    # aucune production écrite. Le module est donc entièrement une affaire de
    # comptoir parlé : on demande, on écoute la réponse, on redemande. Les
    # trois défis sont les trois moments de cette même intention — se
    # renseigner avant de choisir, choisir et payer, obtenir un service.
    #
    # Aucun voisin : la situation « Démarches à la poste » n'existe qu'aux
    # niveaux 2 et 3 du programme, et aucun module du dépôt ne l'avait
    # traitée. Ce qui la sépare des six autres comptoirs du niveau 3
    # (épicerie, vêtements, électro, restaurant, pharmacie, métro) : ici
    # l'objet part sans vous, et tout ce qui se dit porte sur un moment qu'on
    # ne verra pas — le prix d'un service rendu ailleurs, un délai, une
    # signature à l'autre bout.
    'module-n3-poste': {
        'numero': 7, 'activite': 80, 'niveau': 3,
        'titre': 'Le colis de Yassine',
        'chapeau': "Se renseigner au comptoir d'un bureau de poste avant de "
                   "choisir, dire ce que contient son colis et payer le bon "
                   "envoi, puis demander un service : ramasser un colis, "
                   "faire suivre son courrier.",
        'seances': GRILLE_3_DEFIS,
        'blocs': _blocs("Demander avant de choisir",
                        "Dire ce qu'il y a dedans, et payer",
                        "Le carton dans la boîte aux lettres"),
    },
    # `build/cadre.py 3 "Location d’un logement"` donne **deux** intentions,
    # et elles tiennent en deux gestes : « demander et comprendre des
    # renseignements sur le logement pendant une visite » (compréhension et
    # production orales) et « lire des petites annonces simples »
    # (compréhension écrite). Aucune production écrite rattachée à la
    # situation. Le module s'arrête donc là où le programme s'arrête : une
    # annonce qu'on décode, un appel qu'on passe pour prendre rendez-vous,
    # trois questions qu'on pose sur place. Ni bail à lire, ni comparaison
    # argumentée, ni démarche au tribunal.
    #
    # Deux voisins, aucun recoupement. `module-logement` (niveau 4, module 9)
    # visite deux logements et les compare pour choisir ; `module-n5-logement`
    # fait la démarche entière — l'appel avec prise de notes, la visite, le
    # bail et l'avis de renouvellement. Ici, l'élève ne compare rien et ne
    # signe rien : il lit six lignes d'annonce, il téléphone, il demande.
    'module-n3-loyer': {
        'numero': 8, 'activite': 81, 'niveau': 3,
        'titre': 'Trois questions avant de louer',
        'chapeau': "Lire une petite annonce de logement, téléphoner pour "
                   "prendre rendez-vous, puis poser ses questions pendant la "
                   "visite.",
        'seances': GRILLE_3_DEFIS,
        'blocs': _blocs("Lire la petite annonce",
                        "Téléphoner pour visiter",
                        "Poser mes questions sur place"),
    },
    # `build/cadre.py 3 "Relations sociales"` a décidé de la forme de ce
    # module, et son verdict est franc : **treize intentions, dont dix orales**
    # — comprendre et formuler une invitation, comprendre et donner une
    # permission, se présenter et présenter quelqu'un, complimenter, décrire un
    # objet, une personne ou un problème. La compréhension écrite n'en compte
    # qu'une (lire une description) et la production écrite deux (rédiger une
    # invitation, décrire). Le module est donc une suite de conversations
    # d'escalier, et non un module de papiers : les deux seuls écrits sont un
    # carton d'invitation et une petite affiche de description.
    #
    # Trois voisins sur le même sujet, aucun recoupement. `module-n2-bonjour`
    # (niveau 2) s'arrête au salut et au « ça va ? » ; `module-relations`
    # (niveau 4) donne des nouvelles et raconte une expérience passée ;
    # `module-n5-voisinage` (niveau 5) organise une fête de ruelle et
    # argumente son refus. Ici, au niveau 3, on entretient le lien court et
    # régulier de l'immeuble : demander la permission, inviter, remercier,
    # décrire ce qui manque.
    'module-n3-voisins': {
        'numero': 9, 'activite': 82, 'niveau': 3,
        'titre': "L'escalier de la rue Dézéry",
        'chapeau': "Se présenter et présenter quelqu'un dans son immeuble, "
                   "demander et donner une permission, inviter ses voisins et "
                   "répondre à une invitation, puis décrire une personne ou "
                   "un objet perdu.",
        'seances': GRILLE_3_DEFIS,
        'blocs': _blocs("Est-ce que je peux ?",
                        "Venez prendre un café",
                        "Il est comment ?"),
    },
    # `build/cadre.py 3 "Emploi"` a décidé de la forme de ce module : six
    # intentions, dont six orales sur huit — demander une permission et en
    # comprendre la réponse, demander de l'aide ou un service et en comprendre
    # la réponse, comprendre une consigne, répondre à une demande de service.
    # La compréhension écrite n'en compte qu'une (lire des consignes simples)
    # et la production écrite une seule (prendre en note une directive). Le
    # module se tient donc debout, pendant le quart : ses deux seuls écrits
    # sont l'horaire affiché au mur et le petit mot laissé au chef d'équipe.
    #
    # Quatre voisins sur la même situation, aucun recoupement. `module-travail`
    # (niveau 4) est celui de l'absence : prévenir, justifier un retard, écrire
    # un courriel. `module-n5-travail` (niveau 5) traite des relations
    # d'équipe, `module-n8-emploi` (niveau 8) d'une erreur de paie et d'une
    # réunion. Ici, au niveau 3, on est **présent** et la journée se déroule :
    # l'heure, la tâche, et la question qu'on ose poser.
    'module-n3-horaire': {
        'numero': 11, 'activite': 84, 'niveau': 3,
        'titre': 'Mon quart de travail',
        'chapeau': "Lire son horaire et dire les heures d'un quart, demander "
                   "une permission ou de l'aide et comprendre la réponse, "
                   "puis comprendre une consigne, la noter et dire où on en "
                   "est dans sa tâche.",
        'seances': GRILLE_3_DEFIS,
        'blocs': _blocs("Mon quart commence à quelle heure ?",
                        "Est-ce que je peux vous demander ?",
                        "Trois choses avant midi"),
    },
    # « Recherche d'emploi » au niveau 3. `module-n6-recherche` (niveau 6)
    # fait passer une entrevue : parcours, arguments, questions au recruteur.
    # `module-travail` (niveau 4) part d'un emploi déjà obtenu — l'horaire,
    # les tâches, le remplacement à demander. Ici l'emploi n'existe pas
    # encore : on lit une affiche, on pousse la porte, on demande si ça
    # engage, on laisse son nom et son numéro.
    'module-n3-recherche-emploi': {
        'numero': 10, 'activite': 83, 'niveau': 3,
        'titre': 'On embauche',
        'chapeau': "Offrir ses services en personne, lire une offre d'emploi "
                   "simple, remplir un formulaire de demande d'emploi et "
                   "rédiger une courte annonce.",
        'seances': GRILLE_3_DEFIS,
        'blocs': _blocs("Est-ce que vous engagez ?",
                        "L'annonce dit quoi ?",
                        "Mon nom sur le papier"),
    },
    'module-n3-secretariat': {
        'numero': 13, 'activite': 86, 'niveau': 3,
        'titre': "L'absence de Nawel",
        'chapeau': "Prévenir le secrétariat qu'on va manquer un cours, "
                   "apporter un billet pour justifier une absence, puis dire "
                   "et écrire au personnel qu'on doit arrêter.",
        'seances': GRILLE_3_DEFIS,
        'blocs': _blocs("Prévenir avant",
                        "Le billet d'absence",
                        "Quand on doit arrêter"),
    },
    # `build/cadre.py 3 "Participation à une activité culturelle ou sportive"`
    # a décidé de la forme de ce module, et il fait mentir l'attente : au
    # niveau 3, cette situation **parle**. Quatre intentions, dont une en
    # production orale — « demander et comprendre des renseignements pour
    # choisir une activité » — la même en compréhension orale, plus deux
    # lectures très précises : « lire une brève description de film dans un
    # téléhoraire » et « lire une recette » (dont les consignes se
    # comprennent aussi à l'oral). Le module est donc bâti sur des dialogues,
    # et ses deux seuls papiers — le feuillet du ciné-club et la recette —
    # sont exactement ceux que le programme nomme.
    #
    # `module-activite` (niveau 4, activité 50) traite la même situation, mais
    # s'y **inscrit** : dépliant, consignes du moniteur, formulaire à remplir.
    # Ici, on ne s'inscrit pas — on se renseigne avant de choisir : quand,
    # combien, où, et quoi apporter.
    'module-n3-loisirs': {
        'numero': 12, 'activite': 85, 'niveau': 3,
        'titre': 'Choisir une activité au centre',
        'chapeau': "Demander l'horaire, le tarif et ce qu'il faut apporter, "
                   "lire une brève description de film dans un téléhoraire, "
                   "puis suivre les consignes d'une recette.",
        'seances': GRILLE_3_DEFIS,
        'blocs': _blocs("Quand, combien, quoi apporter ?",
                        "Le ciné-club du vendredi",
                        "La cuisine collective"),
    },
    # ── Niveau 5 ────────────────────────────────────────────────────
    # `module-logement` (niveau 4) traite la même situation du programme, mais
    # s'arrête à la visite et à la comparaison. Ici, on téléphone, on prend des
    # notes et on lit son bail — d'où un slug qui porte le niveau.
    'module-n5-logement': {
        'numero': 1, 'activite': 58, 'niveau': 5,
        'titre': 'Louer un logement',
        'chapeau': "Se renseigner par téléphone et prendre des notes, "
                   "comprendre et donner des renseignements pendant une "
                   "visite, lire son bail et son avis de renouvellement.",
        'seances': GRILLE_3_DEFIS,
        'blocs': _blocs("L'appel",
                        'La visite',
                        'Le bail'),
    },

    'module-n5-degat': {
        'numero': 2, 'activite': 62, 'niveau': 5,
        'titre': "Un dégât d'eau",
        'chapeau': "Décrire un dégât et raconter ce qui s'est passé, lire "
                   "l'avis de travaux affiché dans l'immeuble, puis "
                   "argumenter jusqu'au bout de la démarche : réduction de "
                   "loyer et réclamation d'assurance.",
        'seances': GRILLE_3_DEFIS,
        'blocs': _blocs('Le constat',
                        "L'avis",
                        'La réclamation'),
    },

    # La situation « Emménagement dans un nouveau logement » n'existe pas au
    # niveau 4 : elle commence au 5. Elle ne recoupe ni `module-n5-logement`
    # (58), qui s'arrête à la signature du bail, ni `module-n5-degat` (62), qui
    # répare. Ici le bail est signé et tout ce qui suit reste à faire.
    'module-n5-emmenagement': {
        'numero': 3, 'activite': 63, 'niveau': 5,
        'titre': 'Emménager dans un nouveau logement',
        'chapeau': "Réserver un service de déménagement au téléphone et "
                   "diriger les déménageurs le jour venu, changer son adresse "
                   "et faire brancher ses services, puis se présenter à ses "
                   "voisins et comprendre les usages de l'immeuble.",
        'seances': GRILLE_3_DEFIS,
        'blocs': _blocs('Le camion',
                        "La nouvelle adresse",
                        'Les voisins'),
    },

    # « Utilisation des services publics » : le programme n'en donne que trois
    # intentions — demander et comprendre des renseignements par téléphone, et
    # comprendre un formulaire complexe, une brochure ou un site Web. Le
    # domaine général de formation est « Consommation et environnement », d'où
    # l'angle municipal. Ne recoupe pas `module-n5-emmenagement` (63), qui fait
    # brancher les services le jour du déménagement : ici tout est branché
    # depuis huit mois, et c'est le service qui a mal fonctionné.
    'module-n5-services': {
        'numero': 4, 'activite': 64, 'niveau': 5,
        'titre': 'Les services de ma ville',
        'chapeau': "Comprendre une brochure officielle, téléphoner à un "
                   "service public et noter un numéro de requête, lire un "
                   "site Web et un formulaire complexe, puis se présenter "
                   "au guichet avec les bonnes pièces.",
        'seances': GRILLE_3_DEFIS,
        'blocs': _blocs("L'appel",
                        "L'écran",
                        'Le guichet'),
    },

    # « Consultation d'un professionnel de la santé », niveau 5. Le programme
    # n'y donne qu'une intention, en CO et en PO : prendre, annuler ou modifier
    # un rendez-vous par téléphone. Le module 1 du niveau 4 (« Consulter au bon
    # endroit ») choisit le bon service et décrit une douleur au triage ; ici
    # l'élève tient le rendez-vous d'un bout à l'autre — il le prend, il raconte
    # trois mois de symptômes dans le bureau, puis il le déplace et l'annule
    # sans perdre sa place.
    'module-n5-rendezvous': {
        'numero': 5, 'activite': 65, 'niveau': 5,
        'titre': 'Prendre rendez-vous chez le médecin',
        'chapeau': "Téléphoner à une clinique pour obtenir un rendez-vous, "
                   "raconter un problème de santé qui dure depuis des mois, "
                   "comprendre l'explication du médecin et poser ses "
                   "questions, puis déplacer ou annuler un rendez-vous dans "
                   "les règles.",
        'seances': GRILLE_3_DEFIS,
        'blocs': _blocs("L'appel à la clinique",
                        'Dans le bureau',
                        'Déplacer ou annuler'),
    },

    # « Urgence et hospitalisation », niveau 5. Le programme n'y donne qu'une
    # intention, en CO et en PO : téléphoner au 9-1-1 et au 8-1-1. Le module 2
    # du niveau 4 (« Une urgence au travail ») fait raconter un accident déjà
    # arrivé, à l'urgence puis à l'accueil ; ici l'élève est celui qui
    # accompagne — il compose le 9-1-1 pendant que ça se passe, il traverse le
    # triage et l'attente, puis il suit une hospitalisation de trois jours et
    # donne des nouvelles.
    'module-n5-urgence': {
        'numero': 6, 'activite': 66, 'niveau': 5,
        'titre': "Une nuit à l'urgence",
        'chapeau': "Reconnaître ce qui relève du 8-1-1 et ce qui relève du "
                   "9-1-1, mener un appel d'urgence sans perdre le fil, "
                   "raconter au triage ce qui est arrivé, puis comprendre "
                   "une hospitalisation et donner des nouvelles à ses "
                   "proches.",
        'seances': GRILLE_3_DEFIS,
        'blocs': _blocs("L'appel au 9-1-1",
                        "Le triage et l'attente",
                        "L'étage et le congé"),
    },

    # Niveau 5 · Emploi. Le cadre du programme ne parle pas ici de relations
    # d'équipe mais d'écrits de travail : comprendre et nommer les étapes
    # d'une démarche administrative simple, enregistrer un message dans sa
    # boîte vocale, lire un mode d'emploi, rédiger des notes d'utilisation du
    # matériel, un court message à partir de notes, et un courriel de réponse
    # automatique en cas d'absence. Rien à voir avec `module-travail` (39),
    # qui annonce une absence par téléphone, ni avec `module-n8-emploi` (61),
    # qui fait tenir son bout, ni avec `module-n6-recherche` (59), qui
    # cherche un emploi : ici l'emploi est déjà obtenu, et c'est la paperasse
    # du poste qu'il faut apprendre.
    'module-n5-travail': {
        'numero': 7, 'activite': 67, 'niveau': 5,
        'titre': "Le travail par écrit",
        'chapeau': "Enregistrer un message d'accueil et prendre une note "
                   "d'appel, lire et écrire un mode d'emploi du matériel de "
                   "bureau, puis nommer les étapes d'une demande de congé et "
                   "régler son courriel d'absence.",
        'seances': GRILLE_3_DEFIS,
        'blocs': _blocs("La boîte vocale et la note",
                        "Le mode d'emploi",
                        "La demande de congé"),
    },

    # Niveau 5 · Relations sociales. Le cadre du programme donne dix
    # intentions, et elles ne parlent presque pas de bavardage : accepter ou
    # refuser avec justification une offre ou une invitation, féliciter
    # quelqu'un, enregistrer un message d'accueil téléphonique, laisser un
    # message téléphonique, rédiger un mot à partir des notes prises en
    # écoutant un message, clavarder ou écrire un bref courriel pour donner
    # des nouvelles. Recevoir et donner des nouvelles n'est plus la matière du
    # module : c'en est le fil. Ne recoupe pas `module-relations` (48), au
    # niveau 4, où l'on raconte ses semaines et son passé dans une activité de
    # loisir ; ici l'échange se prolonge et se justifie, et il passe autant par
    # le téléphone et l'écrit que par la conversation. Ne recoupe pas non plus
    # `module-n5-travail` (67), dont la boîte vocale et la note d'appel sont
    # celles d'un bureau : ici le répondeur est celui de la maison, le mot se
    # laisse sur une table et les félicitations sont sincères, pas polies.
    'module-n5-voisinage': {
        'numero': 8, 'activite': 68, 'niveau': 5,
        'titre': "La ruelle en fête",
        'chapeau': "Accepter ou refuser une invitation en disant pourquoi, "
                   "laisser un message sur un répondeur et en tirer un mot "
                   "lisible, puis donner des nouvelles et féliciter "
                   "quelqu'un, de vive voix comme par écrit.",
        'seances': GRILLE_3_DEFIS,
        'blocs': _blocs("L'invitation",
                        "Le message et le mot",
                        "Les nouvelles et les félicitations"),
    },

    # Niveau 5 · « Déplacements dans une ville ». Le programme ne donne ici
    # qu'une seule intention, et elle est en compréhension orale : suivre un
    # bulletin de circulation routière. Le module est donc bâti sur elle
    # seule — on écoute une voix qui annonce ce qui bloque, on en tire ce qui
    # touche son trajet, et on explique ensuite le détour et le retard.
    # Rien à voir avec `module-deplacement` (niveau 4), où l'on compose un
    # trajet et où l'on lit un plan de métro pour se rendre quelque part ;
    # rien à voir non plus avec `module-n3-metro` (79), qui achète le bon
    # titre de transport, ni avec `module-n2-autobus`, qui lit un horaire.
    'module-n5-transport': {
        'numero': 9, 'activite': 69, 'niveau': 5,
        'titre': "\u00c7a bloque ce matin",
        'chapeau': "Suivre un bulletin de circulation, comprendre ce qui "
                   "bloque la route et depuis quand, choisir un autre chemin, "
                   "puis expliquer son retard de vive voix et par \u00e9crit.",
        'seances': GRILLE_3_DEFIS,
        'blocs': _blocs("Ce qui bloque la route",
                        "Le bulletin de 6\u202fh\u202f50",
                        "Le trajet refait"),
    },

    # Niveau 5 · « Déplacements dans tout le Québec ». Le cadre donne trois
    # intentions, et aucune ne parle de circulation : s'informer sur les
    # régions du Québec et échanger avec les vacanciers ou les gens de la
    # région visitée, chacune à l'oral, puis lire de l'information sur les
    # régions. La situation, c'est sortir de la ville — on se renseigne, on
    # réserve, on lit, on part, et on parle à des gens qu'on ne reverra pas.
    # Rien à voir avec `module-n5-transport` (69), livré le même jour au même
    # niveau, où la route est bloquée et où tout le travail est d'écouter un
    # bulletin ; ici la route n'est pas bloquée, elle est longue : un horaire
    # interurbain à lire, un billet à acheter, une valise à mettre en soute et
    # cinq cents kilomètres à faire. Rien à voir non plus avec
    # `module-deplacement` (niveau 4), qui compose un trajet dans une ville et
    # lit un plan de métro, ni avec `module-n3-metro` (79), qui achète un
    # titre au guichet et repart le jour même.
    'module-n5-quebec': {
        'numero': 10, 'activite': 70, 'niveau': 5,
        'titre': "Une semaine au Bic",
        'chapeau': "Se renseigner et réserver de vive voix au comptoir des "
                   "autocars, lire l'horaire, la fiche du parc et la "
                   "politique de bagages, puis jaser avec l'hôtesse du gîte "
                   "et les gens de la région.",
        'seances': GRILLE_3_DEFIS,
        'blocs': _blocs("Au comptoir de la gare d'autocars",
                        "Ce qui est écrit sur la région",
                        "Sur place, avec les gens de la région"),
    },

    # « Suivi de l'actualité », niveau 5. Le programme n'y donne qu'une seule
    # intention, en compréhension écrite : comprendre un fait divers dans un
    # journal. Le module est bâti sur elle et sur ce que le niveau 5 demande
    # d'en faire — un discours simple mais organisé : on lit, on raconte à
    # quelqu'un qui n'a pas lu, on rapporte ce que les gens ont dit, puis on
    # donne son avis. Ne recoupe pas `module-nouvelles` (41), au niveau 4, où
    # l'on écoute le bulletin et où l'on répond à des questions de repérage ;
    # ici la lecture n'est qu'un point de départ et tout le travail est de
    # restituer. Ne recoupe pas non plus `module-n7-actualite` (60), qui
    # démêle les genres du journalisme et intervient dans un blogue, ni
    # `module-n5-transport` (69), qui écoute un bulletin de circulation pour
    # refaire son trajet le matin même.
    'module-n5-actualite': {
        'numero': 11, 'activite': 71, 'niveau': 5,
        'titre': 'Raconter une nouvelle',
        'chapeau': "Lire un fait divers dans le journal local, le raconter à "
                   "quelqu'un qui ne l'a pas lu, rapporter ce que les gens "
                   "ont dit et donner son avis.",
        'seances': GRILLE_3_DEFIS,
        'blocs': _blocs("Ce qui est arrivé",
                        'Ce que les gens ont dit',
                        "Ce que j'en pense"),
    },

    # Niveau 5, situation « Météo ». La météo n'y est plus une information
    # mais une contrainte : quelqu'un attend une décision, et cette décision
    # engage trente personnes. Ne recoupe pas `module-meteo` (34), au niveau
    # 4, qui écoute le bulletin pour savoir quoi mettre pour sortir, ni
    # `module-n2-neige`, qui n'en garde que les trois mots du matin. Ne
    # recoupe pas non plus `module-n5-transport` (69), même niveau, où la
    # décision porte sur son propre trajet du matin même : ici elle porte sur
    # un groupe et sur la semaine prochaine, ce qui oblige au futur simple.
    'module-n5-saisons': {
        'numero': 12, 'activite': 72, 'niveau': 5,
        'titre': 'Quand la m\u00e9t\u00e9o d\u00e9cide',
        'chapeau': "Distinguer une veille d'un avertissement, tirer d'un "
                   "bulletin ce qui est annonc\u00e9 et pour quand, d\u00e9cider si "
                   "une activit\u00e9 est maintenue, report\u00e9e ou annul\u00e9e, puis "
                   "dire pourquoi et ce qu'il faut apporter.",
        'seances': GRILLE_3_DEFIS,
        'blocs': _blocs("Ce que l'avertissement annonce",
                        'La d\u00e9cision, et pourquoi',
                        "Ce qu'il faut apporter"),
    },

    'module-n5-oeuvres': {
        'numero': 13, 'activite': 73, 'niveau': 5,
        'titre': 'Le club du jeudi',
        'chapeau': "Raconter une histoire sans la dévoiler, lire une planche "
                   "de bande dessinée, dire ce qu'on a aimé d'une œuvre et "
                   "le justifier devant des gens qui ne sont pas d'accord.",
        'seances': GRILLE_3_DEFIS,
        'blocs': _blocs("Ce que raconte l'histoire",
                        'Lire une bande dessinée',
                        "Dire ce qu'on en pense"),
    },

    # Quatorzième et dernière situation du niveau 5. La situation existe aussi
    # aux niveaux 1 à 3 — jamais au 4 — et le niveau 2 comme le niveau 3 la
    # traitent au comptoir : on s'inscrit, on demande où est le local, on
    # rapporte un billet d'absence de la veille. Ici, l'élève ne vient pas
    # chercher un renseignement : il vient exposer une situation qui le
    # regarde, lui, et qui dure — trois semaines d'absence à venir, un horaire
    # qui ne tient plus, une preuve à obtenir. Il faut donc un discours
    # organisé, une trace écrite, et la lecture d'un avis officiel qui, lui,
    # ne se négocie pas.
    'module-n5-ecole': {
        'numero': 14, 'activite': 74, 'niveau': 5,
        'titre': 'Régler une affaire au centre',
        'chapeau': "Annoncer une absence prolongée au secrétariat, lire un "
                   "avis officiel du centre jusqu'à la date limite, et "
                   "demander par écrit un changement à son dossier.",
        'seances': GRILLE_3_DEFIS,
        'blocs': _blocs("Prévenir de son absence",
                        "Lire l'avis du centre",
                        'Demander un changement'),
    },

    'module-n6-recherche': {
        'numero': 1, 'activite': 59, 'niveau': 6,
        'titre': "Chercher un emploi",
        'chapeau': "Lire une offre d'emploi détaillée, s'informer sur "
                   "l'entreprise, remplir une demande et offrir ses services "
                   "en entrevue.",
        'seances': GRILLE_3_DEFIS,
        'blocs': _blocs("L'offre d'emploi",
                        'La demande',
                        "L'entrevue"),
    },

    # Pilote du niveau 6 (vague 5). La situation « Suivi de l'actualité » n'a
    # au niveau 6 que des intentions de **compréhension** — une orale, trois
    # écrites — et cinq genres à distinguer : chronique pratique, entrevue,
    # documentaire, fait divers, courrier des lecteurs. Trois défis, donc
    # GRILLE_3_DEFIS : la raison est écrite dans `docs/vagues-suivantes.md`.
    # Ne recoupe ni `module-n5-actualite` (71), qui n'a qu'un genre et un seul
    # travail — raconter un fait divers —, ni `module-n7-actualite` (60), qui
    # démêle le fait de l'opinion chez un auteur qui la cache.
    'module-n6-actualite': {
        'numero': 2, 'activite': 99, 'niveau': 6,
        'titre': "Suivre un sujet dans les médias",
        'chapeau': "Reconnaître les cinq genres de l'actualité, suivre une "
                   "chronique pratique et une entrevue longue, lire un fait "
                   "divers et le courrier des lecteurs, puis écrire au "
                   "journal.",
        'seances': GRILLE_3_DEFIS,
        'blocs': _blocs('La chronique pratique',
                        "L'entrevue et le documentaire",
                        'Le courrier des lecteurs'),
    },

    # Vague 6, niveau 6. `build/cadre.py 6 "Emploi"` donne **cinq** intentions
    # — une orale en compréhension (comprendre des explications sur les étapes
    # d'une démarche administrative), une orale en production (décrire ces
    # étapes), deux écrites en compréhension (lire de la documentation interne
    # reliée à son emploi, lire un compte rendu) et une écrite en production
    # (rédiger un courriel dans le contexte de relations professionnelles).
    # C'est la situation la mieux fournie du niveau, et les trois défis
    # sortent d'elle seule : un même dossier — une candidature à un poste
    # affiché à l'interne — repris sous trois genres, l'explication de vive
    # voix, la documentation interne, le compte rendu de rencontre.
    #
    # Ne recoupe aucun voisin. `module-travail` (39, niveau 4) prévient d'une
    # absence et justifie un retard. `module-n3-horaire` (84, niveau 3) tient
    # debout pendant le quart : l'heure, la tâche, la question qu'on ose
    # poser. `module-n5-travail` (67, niveau 5) traite des relations d'équipe.
    # `module-n6-recherche` (59, même niveau) cherche un emploi qu'on n'a pas
    # encore ; ici l'emploi est acquis depuis deux ans et c'est **à l'interne**
    # qu'on bouge. `module-n8-emploi` (61, niveau 8) fait tenir son bout.
    'module-n6-emploi': {
        'numero': 3, 'activite': 100, 'niveau': 6,
        'titre': "Le poste affiché à l'interne",
        'chapeau': "Comprendre les étapes d'une démarche administrative "
                   "expliquées de vive voix, lire la documentation interne de "
                   "son milieu de travail et un compte rendu de rencontre, "
                   "puis décrire la démarche et écrire un courriel "
                   "professionnel.",
        'seances': GRILLE_3_DEFIS,
        'blocs': _blocs("On m'explique la démarche",
                        'Ce que disent les documents',
                        'Le compte rendu'),
    },

    'module-n7-actualite': {
        'numero': 1, 'activite': 60, 'niveau': 7,
        'titre': "Suivre l'actualité",
        'chapeau': "Écouter un reportage en plusieurs écoutes, lire un "
                   "article informatif, démêler le fait de l'opinion dans "
                   "une chronique, puis intervenir dans un blogue.",
        'seances': GRILLE_3_DEFIS,
        'blocs': _blocs('Le reportage',
                        "L'article",
                        "L'opinion"),
    },

    'module-n8-emploi': {
        'numero': 1, 'activite': 61, 'niveau': 8,
        'titre': "Tenir son bout au travail",
        'chapeau': "Comprendre ses tâches en détail, régler un problème de "
                   "paie, intervenir dans une réunion de décision et demander "
                   "une formation.",
        'seances': GRILLE_3_DEFIS,
        'blocs': _blocs('Une erreur sur la paie',
                        'La réunion',
                        'Se perfectionner'),
    },
}

# L'ordre d'affichage : par niveau, puis par numéro à l'intérieur du niveau.
# Les dix-huit modules du niveau 4 portaient des numéros uniques, et trier sur
# le seul numéro suffisait. À partir du moment où chaque niveau recommence à
# 1 — le chantier des sept autres niveaux, août 2026 —, sept modules portent le
# numéro 1 : sans le niveau en première clé, ils se mêlent aux modules du 4.
ORDRE = sorted(MODULES, key=lambda s: (MODULES[s].get('niveau', 4),
                                       MODULES[s]['numero']))

_ACTIF = None


def choisir(slug):
    """Pose le module actif. À appeler **avant** d'importer un deck : les
    decks construisent leur `Deck` à l'import de leur fonction `build`, et
    `Deck` lit ici le numéro et le titre à mettre en pied de page."""
    global _ACTIF
    if slug not in MODULES:
        raise SystemExit(
            f"Module inconnu : {slug}\nModules connus : "
            + ', '.join(ORDRE))
    _ACTIF = slug
    return MODULES[slug]


def slug_actif():
    if _ACTIF is None:
        raise RuntimeError(
            "Aucun module actif : appelez modules.choisir('<slug>') avant "
            "d'importer un deck.")
    return _ACTIF


def actif():
    return MODULES[slug_actif()]
