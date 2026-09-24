"""Le test de positionnement de la Maison Francœur (étape 3).

Il sert à UNE chose : régler le palier du jeu de rôle (étape 4). Ce n'est pas un
examen et il ne s'annonce pas comme tel. Dix à douze minutes, repassé à la fin
de la formation : l'écart entre les deux passations est la preuve
d'apprentissage qu'un acheteur demande (niveau 2 de Kirkpatrick).

QUATRE PARTIES
  A · reconnaître un mot entendu          (voix des planches)
  B · comprendre un client                (voix de clients, débit normal)
  C · comprendre une consigne de la gérante
  D · répondre à voix haute               (enregistré sur l'appareil, écouté
                                           par le formateur — jamais envoyé)

LA RÈGLE ADAPTATIVE, la même pour A, B et C : on part au cran 1. À un cran,
trois bonnes réponses le valident et font monter ; deux erreurs arrêtent la
partie. Le niveau d'une partie est le dernier cran validé (0 à 3). Personne ne
subit douze questions trop dures ; quelqu'un d'à l'aise en fait neuf.

AUCUNE RÉTROACTION pendant le test : ni vert ni rouge. C'est un test.

DES PHRASES NEUVES : aucune demande ni consigne n'est reprise des exercices,
sinon le test mesurerait la mémoire des exercices. La partie A, elle, porte
forcément sur les mots des planches — c'est ce qu'elle mesure.

LE PALIER se PROPOSE ; le formateur le confirme (le diagnostic reste à
l'enseignant). Rien de nominatif : le résultat vit sur l'appareil.
"""

# ── A · les mots ─────────────────────────────────────────────────────────
# Cran 1 : distracteurs d'AUTRES rayons (déduits). Cran 2 : du MÊME rayon
# (déduits). Cran 3 : les pièges, distracteurs écrits à la main — c'est le
# faux ami qu'on veut voir tomber.
A_CRAN1 = ["t-shirt", "pantalon", "tuque", "souliers", "sac-dos", "robe"]
A_CRAN2 = ["cardigan", "bermuda", "bottillons", "collants", "cache-cou", "combinaison"]
A_CRAN3 = [
    # Audit, tour 2 (F1, majeur) : les pièges étaient TOUS dans la forme 1 — la
    # passation finale (forme 2) ne les mesurait plus. Chaque forme en porte
    # maintenant trois, tirés de la même liste de six, et trois items de
    # discrimination fine. Aucun distracteur n'est défendable : le build refuse
    # un distracteur dont la note du lexique nomme la cible, et l'inverse.
    ("veste",           ["manteau-duvet", "coton-ouate", "chemise"]),
    ("sacoche",         ["sac-dos", "ceinture", "portefeuille"]),  # « un sac » : défendable
    ("jaquette",        ["veston", "robe-chambre", "robe"]),
    ("camisole",        ["t-shirt", "haut-court", "brassiere"]),
    ("robe-chambre",    ["pyjama", "manteau", "robe"]),
    ("claques",         ["souliers", "bottes-pluie", "pantoufles"]),
]

# ── B · le client ────────────────────────────────────────────────────────
# (id, cran, voix, phrase, bonne, ecartes)
# bonne : (article, couleur, taille). Aux crans 1 et 2, les autres cartes sont
# DÉDUITES (None). Au cran 3, on écrit les valeurs que la phrase ÉCARTE —
# (article′, couleur′, taille′) : ce qu'elle nie, reprend ou compare.
#
# LES QUATRE CARTES SE DISPOSENT EN CARRÉ LATIN (audit de la boucle
# didactique, 24 septembre 2026, bloquant) : (A,C,T) (A,C′,T′) (A′,C,T′)
# (A′,C′,T). Chaque valeur paraît exactement deux fois. L'ancienne règle — trois
# distracteurs qui changent chacun UN trait — faisait de la bonne carte la
# majoritaire sur chaque trait : 9 items sur 14 se réussissaient sans écouter.
B = [
    ("b11", 1, "feminin_2",  "Je cherche une tuque.",                ("tuque", "gris", None),     None),
    ("b12", 1, "masculin_1", "Avez-vous des gants ?",                ("gants", "gris", None),     None),
    ("b13", 1, "narrateur",  "Je cherche une ceinture.",             ("ceinture", "gris", None),  None),
    ("b14", 1, "feminin_2",  "Où sont les robes ?",                  ("robe", "gris", None),      None),
    ("b15", 1, "masculin_1", "Je voudrais des bottes d'hiver.",      ("bottes", "gris", None),    None),
    ("b21", 2, "feminin_2",  "Avez-vous une jupe noire, en grand ?", ("jupe", "noir", "g"),       None),
    ("b22", 2, "masculin_1", "Je cherche un pantalon gris, en moyen.", ("pantalon", "gris", "m"), None),
    ("b23", 2, "narrateur",  "Une tuque rouge pour mon gars, s'il vous plaît.", ("tuque", "rouge", None), None),
    ("b24", 2, "feminin_2",  "La robe, vous l'avez-tu en bleu, en petit ?", ("robe", "bleu", "p"), None),
    ("b25", 2, "masculin_1", "Il me faudrait un polo blanc, en très grand.", ("polo", "blanc", "tg"), None),
    ("b31", 3, "masculin_1",
     "Je cherche un chandail… non, pas un chandail, un coton ouaté. Gris. En grand.",
     ("coton-ouate", "gris", "g"), ("chandail", "noir", "m")),
    ("b32", 3, "feminin_2",
     "C'est pour ma fille. Elle fait du petit, pis le rose, elle haït ça. "
     "Auriez-vous la même robe en bleu ?",
     ("robe", "bleu", "p"), ("jupe", "rose", "m")),
    ("b33", 3, "narrateur",
     "Mon garçon a grandi : le moyen, c'est rendu trop serré. "
     "Avez-vous le même kangourou, une taille plus grande ? En noir.",
     ("kangourou", "noir", "g"), ("coton-ouate", "gris", "m")),
    ("b34", 3, "feminin_2",
     "Je le veux pas en noir, j'en ai déjà un. Le manteau, là, vous l'avez-tu en rouge ? En moyen.",
     ("manteau", "rouge", "m"), ("impermeable", "noir", "g")),
]

# ── C · la gérante ───────────────────────────────────────────────────────
# (id, cran, phrase, question, bonne, distracteurs) — des id du lexique qui ont
# un croquis. La gérante tutoie : c'est ainsi qu'on parle entre collègues.
# Au cran 3, les distracteurs sont les autres objets NOMMÉS dans la phrase :
# on ne réussit pas en reconnaissant un mot, il faut comprendre ce qu'on en dit.
# Le trait décisif des demandes à reprise (voir demandes.DECISIF) : celui que
# la phrase nie. Au cran 2, les items avec taille le prennent à tour de rôle.
DECISIF = {"b31": "a", "b32": "c", "b33": "t", "b34": "c", "b62": "t", "b63": "a", "b64": "c"}

C = [
    ("c11", 1, "Va chercher des cintres, s'il te plaît.",
     "Qu'est-ce que la gérante vous demande d'aller chercher ?", "cintre", ["sac", "miroir", "carte-cadeau"]),
    ("c12", 1, "Apporte-moi des sacs.",
     "Qu'est-ce que la gérante vous demande d'apporter ?", "sac", ["cintre", "recu", "etiquette-prix"]),
    ("c13", 1, "Va voir à la caisse.",
     "Où la gérante vous envoie-t-elle ?", "caisse", ["cabine", "vitrine", "miroir"]),
    ("c14", 1, "Les cabines sont en désordre. Vas-y.",
     "Où la gérante vous envoie-t-elle ?", "cabine", ["caisse", "vitrine", "presentoir"]),
    ("c21", 2, "Quand t'auras fini, mets les jeans sur le présentoir, en avant.",
     "Où faut-il mettre les jeans ?", "presentoir", ["vitrine", "cabine", "caisse"]),
    ("c22", 2, "Le client, là-bas, cherche des bottes de pluie. Montre-lui le rayon, au fond.",
     "Que cherche le client ?", "bottes-pluie", ["bottes", "espadrilles", "sandales"]),
    ("c23", 2, "Il manque des étiquettes de prix sur les foulards. Va en chercher en arrière.",
     "Qu'est-ce qu'il faut aller chercher ?", "etiquette-prix", ["recu", "carte-cadeau", "antivol"]),
    ("c24", 2, "Enlève l'antivol avant de mettre le chandail dans le sac.",
     "Qu'est-ce qu'il faut enlever ?", "antivol", ["etiquette-prix", "cintre", "sac"]),
    ("c31", 3, "Avant de fermer, ramasse les cintres dans les cabines, vide la caisse, "
               "pis touche pas à la vitrine : c'est moi qui la fais demain.",
     "Qu'est-ce qu'il ne faut PAS toucher ?", "vitrine", ["cabine", "caisse", "cintre"]),
    ("c32", 3, "On a reçu des manteaux pis des parkas. Les manteaux, tu les sors ; "
               "les parkas, laisse-les dans les boîtes jusqu'à lundi.",
     "Qu'est-ce qu'il faut laisser dans les boîtes ?", "parka", ["manteau", "impermeable", "manteau-duvet"]),
    ("c33", 3, "La cliente veut essayer la robe de soirée, pas la robe de chambre. "
               "Trouve-lui une cabine.",
     "Quel article la cliente veut-elle essayer ?", "robe-soiree", ["robe-chambre", "robe", "jaquette"]),
    ("c34", 3, "Si quelqu'un veut faire un retour, envoie-le à la caisse, pas aux cabines, "
               "pis demande-lui son reçu.",
     "Qu'est-ce qu'il faut demander au client ?", "recu", ["carte-cadeau", "etiquette-prix", "sac"]),
]
VOIX_GERANTE = "enseignante"

# ── D · répondre à voix haute ────────────────────────────────────────────
# Audit de la boucle didactique, 24 septembre 2026 (F1, majeur) : les deux
# questions d'avant (« où sont les cabines ? ») n'exigeaient aucun geste. Chaque
# item exige maintenant UN geste des objectifs O3 et O4. L'enregistrement reste
# sur l'appareil ; le formateur l'écoute et note contre le geste attendu.
# (id, voix, phrase du client, geste attendu, exemples de réponse, rapide)
D = [
    ("d1", "masculin_1",
     "Bonjour, oui, je cherche le chandail gris de la vitrine en moyen, pis aussi une tuque, vous avez-tu ça ?",
     "Faire répéter", "« Un instant, s'il vous plaît. Pouvez-vous répéter plus lentement ? »", True),
    ("d2", "feminin_2", "Avez-vous ce chandail-là ?",
     "Faire préciser", "« Quelle taille ? » ou « Quelle couleur ? »", False),
    ("d3", "masculin_1",
     "Il vous reste-tu ce manteau-là en moyen ? Vous pouvez me le garder jusqu'à samedi, c'est sûr ?",
     "Vérifier sans promettre", "« Je vais vérifier en arrière. »", False),
    ("d4", "feminin_2", "Je veux me faire rembourser ce coton ouaté. J'ai pas mon reçu.",
     "Passer le relais", "« Un instant. Je vais chercher la gérante. »", False),
]
# Audit, tour 2 (F1, majeur) : la partie D était la même aux deux passations et
# reprenait presque mot pour mot les dialogues modèles (d3 ≈ m3, d4 ≈ m5). D2 :
# quatre situations NEUVES pour la seconde forme — autres articles, autres
# raisons (une mise de côté avec dépôt), aucune reprise des modèles ni de
# « Ce que je réponds ». Les mêmes quatre gestes, dans le même ordre.
D2 = [
    ("d5", "feminin_2",
     "Allo, je cherche des bas de laine pour la chasse, gris ou bruns, pis en grand si vous en avez encore.",
     "Faire répéter", "« Excusez-moi, pouvez-vous répéter lentement ? »", True),
    ("d6", "masculin_1", "Vous avez-tu des bottes ?",
     "Faire préciser", "« Pour l'hiver ou pour la pluie ? » ou « Quelle pointure ? »", False),
    ("d7", "feminin_2",
     "La robe noire de la vitrine, il en reste-tu en petit ? Je la veux pour ce soir.",
     "Vérifier sans promettre", "« Une robe noire en petit. Je regarde en arrière. »", False),
    ("d8", "masculin_1",
     "Pouvez-vous me mettre ce parka de côté jusqu'à la semaine prochaine ? Je paierais la moitié tout de suite.",
     "Passer le relais", "« Je ne peux pas décider ça. Je demande à la gérante. »", False),
]

# La clé et la grille ne s'affichent PAS à l'employé (audit, tour 2 : il voyait
# le geste attendu et la réponse modèle, et cochait lui-même « a fait le
# geste »). Le formateur ouvre « Pour le formateur » avec ce code, imprimé dans
# le guide du formateur et nulle part sur l'écran de l'employé.
CODE_FORMATEUR = "2413"

# La grille du formateur, la même pour chaque item : le geste, pas la grammaire.
ORAL = ["A fait le geste", "A deviné ou promis", "Pas de réponse"]

# ── La seconde forme, pour la dernière passation ─────────────────────────
# Audit (F1, majeur) : le test repassé reprenait les MÊMES items, et la partie
# A les MÊMES MP3 que les planches — l'écart mêlait apprentissage et souvenir.
# Forme 2 : mêmes crans, même difficulté, items différents. La première
# passation prend la forme 1, la suivante la forme 2, puis on alterne. La
# partie A est dite par une voix de client (sons/test/a-<id>.mp3), jamais par
# la voix des planches.
A2_CRAN1 = ["chemise", "jupe", "casquette", "sandales", "parapluie", "manteau"]
A2_CRAN2 = ["polo", "salopette", "gougounes", "boxer", "cache-oreilles", "tailleur"]
A2_CRAN3 = [
    ("bas-chaussettes", ["pantalon", "collants", "legging"]),
    ("mitaines",        ["gants", "cache-oreilles", "foulard"]),
    ("espadrilles",     ["sandales", "pantoufles", "souliers"]),
    # Audit, tour 2 (D4) : « kangourou » (un coton ouaté à capuchon) et
    # « tailleur » (un habit de femme) étaient des réponses défendables.
    ("coton-ouate",     ["col-roule", "cardigan", "t-shirt"]),
    ("habit",           ["chemise", "cravate", "manteau"]),
    ("habit-neige",     ["manteau-duvet", "parka", "manteau"]),
]
B2 = [
    ("b41", 1, "masculin_1", "Je cherche une casquette.",        ("casquette", "gris", None), None),
    ("b42", 1, "feminin_2",  "Avez-vous des sandales ?",         ("sandales", "gris", None), None),
    ("b43", 1, "narrateur",  "Je voudrais un imperméable.",      ("impermeable", "gris", None), None),
    ("b44", 1, "feminin_2",  "Où sont les pyjamas ?",            ("pyjama", "gris", None), None),
    ("b45", 1, "masculin_1", "Je cherche une cravate.",          ("cravate", "gris", None), None),
    ("b51", 2, "feminin_2",  "Avez-vous une blouse blanche, en moyen ?", ("blouse", "blanc", "m"), None),
    ("b52", 2, "masculin_1", "Je cherche des shorts noirs, en grand.",   ("short", "noir", "g"), None),
    ("b53", 2, "narrateur",  "Un foulard vert, s'il vous plaît.",        ("foulard", "vert", None), None),
    ("b54", 2, "feminin_2",  "La jupe, l'avez-vous en beige, en petit ?", ("jupe", "beige", "p"), None),
    ("b55", 2, "masculin_1", "Il me faudrait un coton ouaté bleu, en très grand.", ("coton-ouate", "bleu", "tg"), None),
    ("b61", 3, "masculin_1", "Je cherche des bottes… non, des bottillons. Bruns, pas noirs.",
     ("bottillons", "brun", None), ("bottes", "noir", None)),
    ("b62", 3, "feminin_2",
     "C'est pour mon mari. Il fait du grand, mais le grand, c'est trop serré. Le même polo, une taille plus grande. En bleu.",
     ("polo", "bleu", "tg"), ("t-shirt", "vert", "g")),
    ("b63", 3, "narrateur",  "Pas la chemise : le polo. En blanc. Moyen.",
     ("polo", "blanc", "m"), ("chemise", "bleu", "g")),
    ("b64", 3, "feminin_2",  "Je l'aime pas en rouge. Vous avez-tu la même robe en vert ? En petit.",
     ("robe", "vert", "p"), ("jupe", "rouge", "m")),
]
C2 = [
    ("k11", 1, "Va chercher les tuques en arrière.", "Qu'est-ce qu'il faut aller chercher ?",
     "tuque", ["casquette", "foulard", "mitaines"]),
    ("k12", 1, "Plie les chandails.", "Qu'est-ce qu'il faut plier ?",
     "chandail", ["chemise", "pantalon", "t-shirt"]),
    ("k13", 1, "Va voir à la vitrine.", "Où faut-il aller ?",
     "vitrine", ["caisse", "cabine", "presentoir"]),
    ("k14", 1, "Apporte des cintres à la cabine deux.", "Qu'est-ce qu'il faut apporter ?",
     "cintre", ["sac", "miroir", "etiquette-prix"]),
    ("k21", 2, "Mets les foulards sur le présentoir, en avant.", "Qu'est-ce qu'il faut mettre sur le présentoir ?",
     "foulard", ["tuque", "gants", "cravate"]),
    ("k22", 2, "La dame, là-bas, cherche des bottes d'hiver. Montre-lui le rayon.", "Que cherche la dame ?",
     "bottes", ["bottes-pluie", "bottillons", "pantoufles"]),
    ("k23", 2, "Il n'y a plus de sacs à la caisse. Va en chercher.", "Qu'est-ce qui manque ?",
     "sac", ["recu", "carte-cadeau", "cintre"]),
    ("k24", 2, "Mets un antivol sur chaque manteau.", "Qu'est-ce qu'il faut mettre sur les manteaux ?",
     "antivol", ["etiquette-prix", "cintre", "sac"]),
    ("k31", 3, "Plie les chandails, range les jeans, pis touche pas aux robes : je les change demain.",
     "Qu'est-ce qu'il ne faut PAS toucher ?", "robe", ["chandail", "jeans", "pantalon"]),
    ("k32", 3, "On a reçu des bottes pis des souliers. Les bottes, en avant ; les souliers, laisse-les en arrière.",
     "Qu'est-ce qu'il faut laisser en arrière ?", "souliers", ["bottes", "espadrilles", "sandales"]),
    ("k33", 3, "Le client veut essayer le veston, pas l'habit au complet. Trouve-lui une cabine.",
     "Qu'est-ce que le client veut essayer ?", "veston", ["habit", "tailleur", "chemise"]),
    ("k34", 3, "Si quelqu'un veut une carte-cadeau, envoie-le à la caisse, pas à moi.",
     "Où faut-il envoyer le client ?", "caisse", ["cabine", "vitrine", "presentoir"]),
]

# Les seuils des objectifs (cadrage, O1-O5), affichés au résultat par partie.
# Audit, tour 2 (F1, majeur) : le seuil se lisait sur le taux brut de toutes
# les réponses, qui dépend de l'ordre des erreurs dans un test adaptatif. Un
# objectif est maintenant ATTEINT quand le cran qui porte sa tâche est validé :
#   A · cran 3 — les mots, pièges compris (O1) ;
#   B · cran 2 — article, couleur ET taille dans la même phrase (O2) ;
#   C · cran 2 — une consigne de deux éléments (O5).
# Le libellé est pour l'employé : aucun code « O1 » à l'écran.
SEUILS = {"A": (3, "Reconnaître le mot, pièges compris"),
          "B": (2, "Comprendre la demande : article, couleur et taille"),
          "C": (2, "Comprendre une consigne de la gérante")}

# Le palier, sur la somme des trois parties corrigées (0 à 9). La partie B
# pèse plus : c'est elle qui décide du jeu de rôle — un employé qui ne comprend
# pas un client ne peut pas être « à l'aise », quels que soient ses mots.
# La règle est ÉCRITE ICI EN DONNÉES et appliquée par la page, une seule fois :
#   somme <= DEBUTANT_MAX ou B == 0           → débutant
#   somme >= AISE_MIN et B >= AISE_B_MIN      → à l'aise
#   sinon                                     → fonctionnel
DEBUTANT_MAX, AISE_MIN, AISE_B_MIN = 3, 7, 2
PALIERS = [("debutant", "Débutant", "niveaux 1-2"),
           ("fonctionnel", "Fonctionnel", "niveau 3"),
           ("aise", "À l'aise", "niveau 4 et plus")]
