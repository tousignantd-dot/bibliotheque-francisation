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
    ("veste",           ["veston", "manteau", "coton-ouate"]),
    ("bas-chaussettes", ["pantalon", "collants", "legging"]),
    ("sacoche",         ["sac-dos", "sac", "portefeuille"]),
    ("mitaines",        ["gants", "cache-oreilles", "foulard"]),
    ("jaquette",        ["veston", "robe-chambre", "robe"]),
    ("espadrilles",     ["sandales", "pantoufles", "souliers"]),
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
# Le client pose sa question, l'employé répond au micro. L'enregistrement reste
# sur l'appareil ; le formateur l'écoute avec l'employé et note sur trois
# crans. Rien n'est corrigé par l'écran, rien n'est envoyé.
D = [
    ("d1", "masculin_1", "Excusez-moi, les cabines d'essayage, c'est où ?"),
    ("d2", "feminin_2",  "Avez-vous ce chandail-là en moyen ? Je le trouve pas."),
]
ORAL = ["Pas de réponse", "Des mots", "Une phrase qu'on comprend"]

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
