"""Ce que le client veut — les demandes de l'exercice-pont.

Le lexique seul ne fait pas vendre : ce qui fait rater une vente, c'est la
question du client dite vite, avec l'article, la couleur et la taille dans la
même phrase. L'employé entend la demande et choisit, parmi quatre variantes du
même article, celle que le client veut.

CHAQUE DEMANDE : (id, voix, phrase, article, couleur, taille[, ecartes])
- `article` : un id du lexique qui a un croquis (montré en GRIS dans
  l'exercice : c'est la pastille qui porte la couleur, pas le dessin) ;
- `couleur` : un id de couleur du lexique (pastille) ;
- `taille`  : tp · p · m · g · tg, ou None pour ce qui n'a pas de taille
  (tuque, foulard, casquette, mitaines).

Les autres cartes ne s'écrivent pas : elles se DÉDUISENT — une autre couleur,
une taille voisine, un article voisin du même rayon — et se disposent en CARRÉ
LATIN (chaque valeur deux fois). L'ancienne règle, un seul trait changé par
distracteur, rendait la bonne carte majoritaire : on la trouvait sans écouter
(audit de la boucle didactique, 24 septembre 2026, bloquant).

LES VOIX sont celles des clients, au débit NORMAL d'Azure — c'est-à-dire vite.
C'est la leçon, reprise de Chaussures Rivard : on ne dit pas que le client
parle vite, on le fait entendre. L'écran offre « Plus lentement » (le
navigateur étire, sans changer la hauteur). Trois voix de clients, jamais celle
de l'enseignante, qui dit les mots des planches.

LES DEMANDES QUI SE REPRENNENT (d21 à d28, audit de la boucle didactique,
24 septembre 2026) : le cran 3 du test mesure la reprise (« non, pas un
chandail »), la négation (« pas en rouge ») et le comparatif (« une taille plus
grande ») — l'exercice ne les faisait jamais entendre. Le 7e champ, `ecartes`,
nomme ce que la phrase ÉCARTE (article′, couleur′, taille′) ; les quatre cartes
se disposent en carré latin autour, comme partout. Phrases différentes de
celles du test.

Le français est celui du plancher : « vous l'auriez-tu », « c'est pour ma
femme ». Contenu inventé, aucun texte recopié.
"""

DEMANDES = [
    ("d01", "masculin_1", "Bonjour ! Je cherche un t-shirt noir, en grand.",                "t-shirt",     "noir",   "g"),
    ("d02", "feminin_2",  "Est-ce que vous avez cette jupe-là en rouge ? En petit.",        "jupe",        "rouge",  "p"),
    ("d03", "masculin_1", "Le polo, là, vous l'auriez-tu en vert, en moyen ?",              "polo",        "vert",   "m"),
    ("d04", "feminin_2",  "Je voudrais une tuque bleue, s'il vous plaît.",                  "tuque",       "bleu",   None),
    ("d05", "narrateur",  "Avez-vous des cotons ouatés gris ? Moi, je fais du très grand.", "coton-ouate", "gris",   "tg"),
    ("d06", "feminin_2",  "Je cherche une robe beige, en moyen.",                           "robe",        "beige",  "m"),
    ("d07", "masculin_1", "Un kangourou noir, en petit, ça se peut-tu ?",                   "kangourou",   "noir",   "p"),
    ("d08", "feminin_2",  "Il me faudrait un pantalon brun, en grand.",                     "pantalon",    "brun",   "g"),
    ("d09", "narrateur",  "Je cherche un foulard rouge, c'est pour ma femme.",              "foulard",     "rouge",  None),
    ("d10", "feminin_2",  "La camisole blanche, vous l'avez en très petit ?",               "camisole",    "blanc",  "tp"),
    ("d11", "masculin_1", "Un manteau marine, en grand, s'il vous plaît.",                  "manteau",     "marine", "g"),
    ("d12", "feminin_2",  "Je cherche une veste de laine rose, en moyen.",                  "cardigan",    "rose",   "m"),
    ("d13", "narrateur",  "Vous avez-tu des casquettes jaunes ?",                           "casquette",   "jaune",  None),
    ("d14", "feminin_2",  "Des leggings noirs en petit, s'il vous plaît.",                  "legging",     "noir",   "p"),
    ("d15", "masculin_1", "Je voudrais un col roulé gris, en moyen.",                       "col-roule",   "gris",   "m"),
    ("d16", "feminin_2",  "Avez-vous des shorts kaki en grand ?",                           "short",       "kaki",   "g"),
    ("d17", "narrateur",  "Une chemise blanche, en très grand. C'est pour un mariage.",     "chemise",     "blanc",  "tg"),
    ("d18", "feminin_2",  "Je cherche une blouse mauve, en petit.",                         "blouse",      "mauve",  "p"),
    ("d19", "masculin_1", "Le t-shirt, vous l'avez-tu en rouge ? En moyen.",                "t-shirt",     "rouge",  "m"),
    ("d20", "feminin_2",  "Des mitaines bleues pour mon garçon, s'il vous plaît.",          "mitaines",    "bleu",   None),
    # ── Qui se reprennent, nient ou comparent ──────────────────────────────
    ("d21", "feminin_2",  "Je cherche un chandail gris… non, pas gris : noir. En moyen.", "chandail", "noir", "m",
     ("col-roule", "gris", "g")),
    ("d22", "masculin_1", "Le polo en petit, c'est trop serré. Vous l'avez-tu une taille plus grande ? En bleu.",
     "polo", "bleu", "m", ("t-shirt", "rouge", "p")),
    ("d23", "narrateur",  "Pas la jupe : la robe. En noir, en grand, s'il vous plaît.", "robe", "noir", "g",
     ("jupe", "beige", "m")),
    ("d24", "feminin_2",  "Je voudrais la même tuque, mais pas en rouge : en bleu.", "tuque", "bleu", None,
     ("casquette", "rouge", None)),
    ("d25", "masculin_1", "J'ai pris un grand, c'est trop long. Le même pantalon en moyen, en gris.",
     "pantalon", "gris", "m", ("jogging", "noir", "g")),
    ("d26", "feminin_2",  "Une veste de laine, là… beige. Pas en petit : en moyen.", "cardigan", "beige", "m",
     ("chandail", "gris", "p")),
    ("d27", "narrateur",  "Des mitaines, pas des gants. Noires, pour mon garçon.", "mitaines", "noir", None,
     ("gants", "bleu", None)),
    ("d28", "masculin_1", "Le manteau marine, je le prendrais une taille plus petite. En moyen.",
     "manteau", "marine", "m", ("parka", "rouge", "g")),
]

# LE TRAIT QUI DÉCIDE (audit de la boucle didactique, tour 2, A3 majeur) : dans
# le carré latin, deux traits suffisaient toujours, et c'étaient l'article et la
# couleur — la taille ne décidait jamais, même quand la phrase la reprenait
# (« pas en petit : en moyen »). Désormais, quand il y a une taille, les quatre
# cartes s'organisent autour d'UN trait décisif : il varie seul, les deux autres
# varient ensemble. (A,C,T) (A,C,T′) (A′,C′,T) (A′,C′,T′) quand c'est la taille.
# Chaque valeur paraît encore deux fois : rien ne se devine à la majorité.
# Les demandes qui se reprennent nomment leur trait : celui que la phrase nie.
# Les autres le prennent à tour de rôle (taille, couleur, article).
DECISIF = {"d21": "c", "d22": "t", "d23": "a", "d25": "t", "d26": "t", "d28": "t"}

# Les couleurs qu'on peut mettre en face d'une autre sans ambiguïté à l'œil :
# marine contre noir, beige contre blanc se confondent sur un petit écran.
COULEURS_DISTRACTRICES = ["noir", "blanc", "gris", "bleu", "rouge", "vert", "jaune",
                          "rose", "mauve", "brun", "beige", "kaki", "marine"]
TAILLES = ["tp", "p", "m", "g", "tg"]
# Audit, tour 2 (D4) : le commentaire ci-dessus le disait, la liste ne le
# faisait pas. Une couleur n'est jamais opposée à celle qu'on confond avec elle.
CONFONDUES = {"marine": {"noir", "bleu"}, "noir": {"marine"}, "bleu": {"marine"},
              "beige": {"blanc", "brun"}, "blanc": {"beige"}, "brun": {"beige"}}
