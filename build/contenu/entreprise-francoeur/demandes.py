"""Ce que le client veut — les demandes de l'exercice-pont.

Le lexique seul ne fait pas vendre : ce qui fait rater une vente, c'est la
question du client dite vite, avec l'article, la couleur et la taille dans la
même phrase. L'employé entend la demande et choisit, parmi quatre variantes du
même article, celle que le client veut.

CHAQUE DEMANDE : (id, voix, phrase, article, couleur, taille)
- `article` : un id du lexique qui a un croquis (montré en GRIS dans
  l'exercice : c'est la pastille qui porte la couleur, pas le dessin) ;
- `couleur` : un id de couleur du lexique (pastille) ;
- `taille`  : tp · p · m · g · tg, ou None pour ce qui n'a pas de taille
  (tuque, foulard, casquette, mitaines).

Les distracteurs ne s'écrivent pas : ils se DÉDUISENT — une autre couleur,
une taille voisine, un article voisin du même rayon. Chacun ne diffère de la
bonne réponse que par UN attribut, sans quoi l'exercice se réussit sans
écouter la phrase entière.

LES VOIX sont celles des clients, au débit NORMAL d'Azure — c'est-à-dire vite.
C'est la leçon, reprise de Chaussures Rivard : on ne dit pas que le client
parle vite, on le fait entendre. L'écran offre « Plus lentement » (le
navigateur étire, sans changer la hauteur). Trois voix de clients, jamais celle
de l'enseignante, qui dit les mots des planches.

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
]

# Les couleurs qu'on peut mettre en face d'une autre sans ambiguïté à l'œil :
# marine contre noir, beige contre blanc se confondent sur un petit écran.
COULEURS_DISTRACTRICES = ["noir", "blanc", "gris", "bleu", "rouge", "vert", "jaune",
                          "rose", "mauve", "brun", "beige", "kaki", "marine"]
TAILLES = ["tp", "p", "m", "g", "tg"]
