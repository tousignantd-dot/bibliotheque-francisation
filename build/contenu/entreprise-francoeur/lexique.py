"""Le lexique de la Maison Francœur — la source unique du volet 1.

Tout ce qui viendra après (planches, cartes, exercices, traductions, voix) se
lit ICI. Rien ne se recopie ailleurs à la main.

CHAQUE ENTRÉE : (id, planche, mot, autre, dessin, note)

- `mot`    : le mot que le client dira au Québec, avec son article. C'est lui
             qui s'apprend, qui se dit et qui passe en tête (décision du
             24 septembre 2026 : « le mot d'ici en tête, l'autre en dessous »).
- `autre`  : l'autre mot qu'on entendra aussi — le français d'Europe, ou le mot
             neutre. Vide quand il n'y en a pas.
- `dessin` : ce qui sert d'image.
             "croquis"  — engendré seul, un vêtement sur fond blanc ;
             "pastille" — composée en HTML (couleurs, motifs simples) : ne coûte
                          rien et ne se trompe jamais de teinte ;
             ""         — pas d'image (une taille, un mot de service).
- `note`   : ce que le vendeur doit savoir en plus, ou le piège.

BROUILLON du 24 septembre 2026, à confronter à une visite de plancher : le
compte exact sort du magasin, pas de ce fichier.
"""

PLANCHES = [
    ("hauts",       "Les hauts"),
    ("bas",         "Les bas du corps"),
    ("robes",       "Robes et habits"),
    ("exterieur",   "L'extérieur"),
    ("dessous",     "Dessous et nuit"),
    ("chaussures",  "Les chaussures"),
    ("accessoires", "Les accessoires"),
    ("details",     "Le vêtement en détail"),
    ("couleurs",    "Couleurs, motifs, matières"),
    ("tailles",     "Tailles et coupes"),
    ("magasin",     "Le magasin"),
]

C, P, N = "croquis", "pastille", ""

LEXIQUE = [
    # ── Les hauts ────────────────────────────────────────────────────────
    ("t-shirt",        "hauts", "un t-shirt",            "un tee-shirt",        C, ""),
    ("chandail",       "hauts", "un chandail",           "un pull",             C, "Au Québec, « chandail » couvre presque tout haut à manches ; le client s'en sert pour un t-shirt aussi."),
    ("chemise",        "hauts", "une chemise",           "",                    C, ""),
    ("blouse",         "hauts", "une blouse",            "un chemisier",        C, ""),
    ("polo",           "hauts", "un polo",               "",                    C, ""),
    ("camisole",       "hauts", "une camisole",          "un débardeur",        C, ""),
    ("coton-ouate",    "hauts", "un coton ouaté",        "un sweat",            C, ""),
    ("kangourou",      "hauts", "un kangourou",          "un sweat à capuche",  C, "Le coton ouaté à capuchon et à poche devant."),
    ("cardigan",       "hauts", "une veste de laine",    "un cardigan",         C, ""),
    ("col-roule",      "hauts", "un col roulé",          "",                    C, "Désigne le vêtement ET le col."),
    # Note nuancée (audit, D4) : la trousse disait elle-même « veste de laine »
    # et « veste en jeans », qui ont des manches. Le piège porte sur le mot SEUL.
    ("veste",          "hauts", "une veste",             "un gilet sans manches", C, "PIÈGE : au Québec, « une veste » toute seule n'a pas de manches. « Une veste de laine », « une veste en jeans » en ont."),
    ("haut-court",     "hauts", "un haut court",         "un crop top",         C, ""),

    # ── Les bas du corps ─────────────────────────────────────────────────
    ("pantalon",       "bas", "un pantalon",             "",                    C, ""),
    ("jeans",          "bas", "des jeans",               "un jean",             C, "Au Québec, souvent au pluriel : « des jeans », « une paire de jeans »."),
    ("jupe",           "bas", "une jupe",                "",                    C, ""),
    ("short",          "bas", "des shorts",              "un short",            C, ""),
    ("legging",        "bas", "des leggings",            "un legging",          C, ""),
    ("cargo",          "bas", "un pantalon cargo",       "",                    C, ""),
    ("jogging",        "bas", "un pantalon de jogging",  "un jogging",          C, ""),
    ("salopette",      "bas", "une salopette",           "",                    C, ""),
    ("bermuda",        "bas", "un bermuda",              "",                    C, ""),
    ("pantalon-habit", "bas", "un pantalon habillé",     "",                    C, ""),

    # ── Robes et habits ──────────────────────────────────────────────────
    ("robe",           "robes", "une robe",              "",                    C, ""),
    ("robe-soiree",    "robes", "une robe de soirée",    "",                    C, ""),
    ("combinaison",    "robes", "une combinaison",       "",                    C, ""),
    ("habit",          "robes", "un habit",              "un costume",          C, "L'ensemble veston et pantalon. « Complet » s'entend aussi."),
    ("veston",         "robes", "un veston",             "",                    C, "La veste d'un habit, avec des manches. En France, on dit « une veste »."),
    ("tailleur",       "robes", "un tailleur",           "",                    C, ""),
    ("cravate",        "robes", "une cravate",           "",                    C, ""),
    ("noeud-pap",      "robes", "un nœud papillon",      "",                    C, ""),

    # ── L'extérieur ──────────────────────────────────────────────────────
    ("manteau",        "exterieur", "un manteau",        "",                    C, ""),
    ("parka",          "exterieur", "un parka",          "une parka",           C, "Le genre flotte : on entend les deux."),
    ("impermeable",    "exterieur", "un imperméable",    "",                    C, ""),
    ("coupe-vent",     "exterieur", "un coupe-vent",     "",                    C, ""),
    ("manteau-duvet",  "exterieur", "un manteau en duvet", "une doudoune",      C, ""),
    ("tuque",          "exterieur", "une tuque",         "un bonnet",           C, ""),
    ("foulard",        "exterieur", "un foulard",        "une écharpe",         C, "Au Québec, le foulard est celui de l'hiver."),
    ("cache-cou",      "exterieur", "un cache-cou",      "un tour de cou",      C, ""),
    ("mitaines",       "exterieur", "des mitaines",      "des moufles",         C, "PIÈGE : en France, une mitaine laisse les doigts à nu."),
    ("gants",          "exterieur", "des gants",         "",                    C, ""),
    ("cache-oreilles", "exterieur", "des cache-oreilles", "",                   C, ""),
    ("habit-neige",    "exterieur", "un habit de neige", "une combinaison de ski", C, "Surtout pour enfants."),

    # ── Dessous et nuit ──────────────────────────────────────────────────
    ("bas-chaussettes","dessous", "des bas",             "des chaussettes",     C, "PIÈGE : « des bas » ne veut pas dire « le bas du corps »."),
    ("collants",       "dessous", "des collants",        "",                    C, ""),
    ("brassiere",      "dessous", "une brassière",       "un soutien-gorge",    C, ""),
    ("culotte",        "dessous", "une culotte",         "des bobettes",        C, "« Des bobettes » : familier, on l'entend souvent."),
    ("boxer",          "dessous", "un boxer",            "un caleçon",          C, ""),
    ("pyjama",         "dessous", "un pyjama",           "",                    C, ""),
    ("jaquette",       "dessous", "une jaquette",        "une chemise de nuit", C, "PIÈGE : en France, une jaquette est un veston long."),
    ("robe-chambre",   "dessous", "une robe de chambre", "un peignoir",         C, ""),
    ("maillot",        "dessous", "un maillot de bain",  "",                    C, ""),
    ("sous-vetements", "dessous", "des sous-vêtements",  "",                    N, "Le nom du rayon."),

    # ── Les chaussures (à accorder avec Chaussures Rivard) ───────────────
    ("souliers",       "chaussures", "des souliers",     "des chaussures",      C, "Au Québec, « souliers » est le mot courant."),
    ("espadrilles",    "chaussures", "des espadrilles",  "des baskets",         C, "PIÈGE : en France, une espadrille est en toile à semelle de corde."),
    ("bottes",         "chaussures", "des bottes d'hiver", "",                  C, ""),
    ("bottes-pluie",   "chaussures", "des bottes de pluie", "",                 C, ""),
    ("bottillons",     "chaussures", "des bottillons",   "des bottines",        C, ""),
    ("sandales",       "chaussures", "des sandales",     "",                    C, ""),
    ("gougounes",      "chaussures", "des gougounes",    "des tongs",           C, ""),
    ("talons",         "chaussures", "des souliers à talons", "des escarpins",  C, ""),
    ("pantoufles",     "chaussures", "des pantoufles",   "des chaussons",       C, ""),
    ("claques",        "chaussures", "des claques",      "des couvre-chaussures", C, "Plus rare, mais un client plus âgé le dira."),

    # ── Les accessoires ──────────────────────────────────────────────────
    ("ceinture",       "accessoires", "une ceinture",    "",                    C, ""),
    ("sacoche",        "accessoires", "une sacoche",     "un sac à main",       C, "PIÈGE : « sacoche » est le sac à main au Québec."),
    ("portefeuille",   "accessoires", "un portefeuille", "",                    C, ""),
    ("casquette",      "accessoires", "une casquette",   "",                    C, ""),
    ("chapeau",        "accessoires", "un chapeau",      "",                    C, ""),
    ("lunettes-soleil","accessoires", "des lunettes de soleil", "",             C, ""),
    ("collier",        "accessoires", "un collier",      "",                    C, ""),
    ("boucles",        "accessoires", "des boucles d'oreilles", "",             C, ""),
    ("bracelet",       "accessoires", "un bracelet",     "",                    C, ""),
    ("montre",         "accessoires", "une montre",      "",                    C, ""),
    ("sac-dos",        "accessoires", "un sac à dos",    "",                    C, ""),
    ("parapluie",      "accessoires", "un parapluie",    "",                    C, ""),

    # ── Le vêtement en détail ────────────────────────────────────────────
    ("manche",         "details", "une manche",          "",                    C, "Manches courtes, manches longues."),
    ("col",            "details", "un col",              "",                    C, "Col rond, col en V, col roulé."),
    ("capuchon",       "details", "un capuchon",         "une capuche",         C, ""),
    ("poche",          "details", "une poche",           "",                    C, ""),
    ("fermeture",      "details", "une fermeture éclair", "un zipper",          C, "Le client dira souvent « un zipper »."),
    ("bouton",         "details", "un bouton",           "",                    C, ""),
    ("ourlet",         "details", "un ourlet",           "",                    C, "Le mot des retouches : « faire l'ourlet »."),
    ("doublure",       "details", "une doublure",        "",                    C, ""),
    ("poignet",        "details", "un poignet",          "",                    C, ""),
    ("bretelle",       "details", "une bretelle",        "",                    C, ""),
    ("taille-ceinture","details", "la taille",           "",                    C, "PIÈGE : aussi « la taille » = la grandeur. « Taille haute » parle de la ceinture."),
    ("etiquette-soin", "details", "l'étiquette d'entretien", "",               C, "Celle qui dit comment laver."),
    ("jambe",          "details", "une jambe",           "",                    C, "Du pantalon : « les jambes sont trop longues »."),
    ("cordon",         "details", "un cordon",           "",                    C, ""),

    # ── Couleurs ─────────────────────────────────────────────────────────
    ("noir",           "couleurs", "noir",               "",                    P, ""),
    ("blanc",          "couleurs", "blanc",              "",                    P, ""),
    ("gris",           "couleurs", "gris",               "",                    P, "Gris pâle, gris foncé."),
    ("marine",         "couleurs", "marine",             "bleu marine",         P, "Invariable : des chandails marine."),
    ("bleu",           "couleurs", "bleu",               "",                    P, ""),
    ("rouge",          "couleurs", "rouge",              "",                    P, ""),
    ("vert",           "couleurs", "vert",               "",                    P, ""),
    ("jaune",          "couleurs", "jaune",              "",                    P, ""),
    ("rose",           "couleurs", "rose",               "",                    P, ""),
    ("mauve",          "couleurs", "mauve",              "violet",              P, "Au Québec, « mauve » est le violet courant."),
    ("brun",           "couleurs", "brun",               "marron",              P, ""),
    ("beige",          "couleurs", "beige",              "",                    P, ""),
    ("kaki",           "couleurs", "kaki",               "",                    P, "Invariable."),
    ("bourgogne",      "couleurs", "bourgogne",          "bordeaux",            P, "Invariable."),
    # ── Motifs ───────────────────────────────────────────────────────────
    ("uni",            "couleurs", "uni",                "",                    P, "D'une seule couleur, sans motif."),
    ("raye",           "couleurs", "rayé",               "à rayures",           P, ""),
    ("carreaute",      "couleurs", "carreauté",          "à carreaux",          P, ""),
    ("fleuri",         "couleurs", "fleuri",             "à fleurs",            C, "Le seul motif qu'une pastille HTML ne rend pas bien."),
    ("pois",           "couleurs", "à pois",             "",                    P, ""),
    ("imprime",        "couleurs", "un imprimé",         "",                    C, ""),
    # ── Matières ─────────────────────────────────────────────────────────
    ("coton",          "couleurs", "le coton",           "",                    N, ""),
    ("laine",          "couleurs", "la laine",           "",                    N, ""),
    ("polyester",      "couleurs", "le polyester",       "",                    N, ""),
    # « Le denim » remplacé par « du jeans » le 24 septembre 2026 (Daniel) : aucune
    # voix HD ne le disait juste, et c'est le mot qu'on entend au plancher.
    # L'id reste « denim » : il est la clé des traductions et des traces.
    ("denim",          "couleurs", "du jeans",           "le denim",            N, "La toile bleue des jeans. On dit aussi « en jeans » : une veste en jeans."),
    ("cuir",           "couleurs", "le cuir",            "",                    N, "Et le similicuir."),
    ("lin",            "couleurs", "le lin",             "",                    N, ""),
    ("polar",          "couleurs", "le polar",           "la laine polaire",    N, ""),

    # ── Tailles et coupes ────────────────────────────────────────────────
    ("tp",             "tailles", "très petit",          "XS",                  N, "Le client dira aussi les lettres anglaises : « extra-small »."),
    ("p",              "tailles", "petit",               "S",                   N, ""),
    ("m",              "tailles", "moyen",               "M",                   N, "PIÈGE : « medium » s'entend autant que « moyen »."),
    ("g",              "tailles", "grand",               "L",                   N, ""),
    ("tg",             "tailles", "très grand",          "XL",                  N, ""),
    ("pointure",       "tailles", "la pointure",         "",                    N, "Pour les chaussures seulement."),
    ("ajuste",         "tailles", "ajusté",              "",                    C, ""),
    ("ample",          "tailles", "ample",               "",                    C, ""),
    ("serre",          "tailles", "trop serré",          "",                    N, ""),
    ("trop-grand",     "tailles", "trop grand",          "",                    N, ""),
    ("trop-long",      "tailles", "trop long",           "",                    N, ""),
    ("trop-court",     "tailles", "trop court",          "",                    N, ""),
    ("taille-haute",   "tailles", "taille haute",        "",                    C, ""),
    ("extensible",     "tailles", "extensible",          "ça étire",            N, "« Ça étire » au Québec."),

    # ── Le magasin ───────────────────────────────────────────────────────
    ("cabine",         "magasin", "la cabine d'essayage", "",                   C, ""),
    ("cintre",         "magasin", "un cintre",           "",                    C, ""),
    ("presentoir",     "magasin", "un présentoir",       "",                    C, ""),
    ("rayon",          "magasin", "un rayon",            "",                    C, "« Le rayon des enfants »."),
    ("etiquette-prix", "magasin", "l'étiquette de prix", "",                    C, ""),
    ("antivol",        "magasin", "l'antivol",           "",                    C, ""),
    ("caisse",         "magasin", "la caisse",           "",                    C, ""),
    ("recu",           "magasin", "le reçu",             "la facture",          C, "Le client dira « ma facture »."),
    ("sac",            "magasin", "un sac",              "",                    C, ""),
    ("reserve",        "magasin", "l'arrière-boutique",  "la réserve",          N, "« Je vais vérifier en arrière »."),
    ("vitrine",        "magasin", "la vitrine",          "",                    C, ""),
    ("mannequin",      "magasin", "un mannequin",        "",                    C, ""),
    ("miroir",         "magasin", "un miroir",           "",                    C, ""),
    ("carte-cadeau",   "magasin", "une carte-cadeau",    "",                    C, ""),
    ("solde",          "magasin", "en solde",            "en spécial",          N, "« C'est-tu en spécial ? »"),
    ("rabais",         "magasin", "un rabais",           "une réduction",       N, ""),
    ("echange",        "magasin", "un échange",          "",                    N, ""),
    ("remboursement",  "magasin", "un remboursement",    "",                    N, ""),
    ("retouches",      "magasin", "les retouches",       "",                    N, ""),
    ("mise-de-cote",   "magasin", "une mise de côté",    "",                    N, ""),
]


def par_planche():
    """{planche: [entrées]} dans l'ordre de PLANCHES."""
    out = {k: [] for k, _ in PLANCHES}
    for e in LEXIQUE:
        out[e[1]].append(e)
    return out


def verifier():
    ids = [e[0] for e in LEXIQUE]
    doubles = {i for i in ids if ids.count(i) > 1}
    assert not doubles, f"identifiants en double : {doubles}"
    connues = {k for k, _ in PLANCHES}
    inconnues = {e[1] for e in LEXIQUE} - connues
    assert not inconnues, f"planches inconnues : {inconnues}"
    assert all(e[4] in (C, P, N) for e in LEXIQUE)


if __name__ == "__main__":
    verifier()
    from collections import Counter
    print(len(LEXIQUE), "entrées ·", Counter(e[4] or "sans image" for e in LEXIQUE))
    for k, t in PLANCHES:
        print(f"  {t:28} {len(par_planche()[k])}")
