"""Les exercices de Chez Jocelyne (étape 2), le contenu seul.

    python3 build/contenu/entreprise-restaurant/exercices.py   # vérifie et compte

Alignés sur les objectifs du cadrage (restauration_etape0.py) :
  O1 la consigne du chef ........ CONSIGNES (et « Je le redis »)
  O2 l'allergie ................. ALLERGIES, règle REGLE écrite UNE fois
  O3 les mots ................... le lexique lui-même, plus PIEGES
  O4 la commande modifiée ....... COMMANDES (et « Je le redis »)

Ce sont des phrases d'ENTRAÎNEMENT : le test (étape 3) en aura d'autres, jamais
celles-ci. Les voix : le chef = Thierry HD, au débit normal (une consigne ne se
dit pas lentement ; l'écran offre « Plus lentement ») ; les clients alternent
Sylvie et Thierry ; le modèle de l'employé (« Je le redis ») = Sylvie.

Leçons reprises de Francœur et de l'hôtel (skill trousse-de-metier) :
  · une consigne qui nomme plusieurs objets met les AUTRES objets nommés parmi
    les choix, sinon on réussit en reconnaissant un seul mot (vérifié plus bas) ;
  · la commande se répond sur une carte à trois traits (plat, changement,
    ingrédient) disposés en CARRÉ LATIN : chaque valeur deux fois, le vote
    majoritaire ne désigne pas la bonne (vérifié à la construction de la page) ;
  · une phrase qui se reprend (« une poutine… non, des frites ») a pour
    distracteur ce qu'elle écarte ;
  · l'allergie se répond par des ACTES ; la règle est affichée avant la série,
    la conséquence après le choix ; chaque série porte un contre-exemple où le
    geste prudent n'est pas le bon (une simple préférence).
"""

# ── O1 · La consigne du chef ───────────────────────────────────────────────
# (id, phrase du chef, question, bonne, [distracteurs], ce que l'employé redit)
CONSIGNES = [
    ("c01", "Coupe les carottes en dés, pas en julienne.", "Comment faut-il couper les carottes ?",
     "en-des", ["julienne", "trancher", "eplucher"], "Oui, chef : les carottes en dés."),
    ("c02", "Va chercher du fromage en grains dans la chambre froide.", "Qu'est-ce qu'il faut aller chercher ?",
     "fromage-grains", ["fromage", "chambre-froide", "frigo"], "Oui, chef : du fromage en grains."),
    ("c03", "Mets les frites dans la friteuse, pas sur la plaque.", "Où vont les frites ?",
     "friteuse", ["plaque", "four", "frites"], "Oui, chef : les frites dans la friteuse."),
    ("c04", "Coupe-moi trois tomates, pis après, lave la planche.", "Qu'est-ce qu'il faut laver ?",
     "planche", ["tomate", "couteau-chef", "bac"], "Oui, chef : trois tomates, pis je lave la planche."),
    ("c05", "J'ai besoin de la passoire pour les pâtes, vite !", "Qu'est-ce que le chef veut ?",
     "passoire", ["pates", "chaudron", "rape"], "Oui, chef : la passoire."),
    ("c06", "Sors le poulet du congélateur pis mets-le dans le frigo.", "Où va le poulet ?",
     "frigo", ["congelateur", "poulet", "chambre-froide"], "Oui, chef : le poulet dans le frigo."),
    ("c07", "Donne-moi la poêle, pas le chaudron.", "Qu'est-ce que le chef veut ?",
     "poele", ["chaudron", "poele-appareil", "plaque"], "Oui, chef : la poêle."),
    ("c08", "Il manque de laitue dans le bac. Remplis-le.", "Qu'est-ce qui manque ?",
     "laitue", ["bac", "oignon", "tomate"], "Oui, chef : de la laitue dans le bac."),
    ("c09", "Mets des gants avant de toucher au poulet cru.", "Qu'est-ce qu'il faut mettre ?",
     "gants", ["poulet", "tablier", "filet"], "Oui, chef : je mets des gants."),
    ("c10", "Prends le thermomètre pis vérifie la soupe.", "Avec quoi faut-il vérifier la soupe ?",
     "thermometre", ["soupe-jour", "louche", "etiquette"], "Oui, chef : je vérifie la soupe au thermomètre."),
    ("c11", "Oublie pas l'étiquette sur le bac de carottes.", "Qu'est-ce qu'il faut mettre sur le bac ?",
     "etiquette", ["bac", "carotte", "thermometre"], "Oui, chef : une étiquette sur le bac."),
    ("c12", "Les assiettes sales, mets-les dans le lave-vaisselle, pas dans l'évier.", "Où vont les assiettes sales ?",
     "lave-vaisselle", ["evier", "assiette", "bac-vaisselle"], "Oui, chef : dans le lave-vaisselle."),
    ("c13", "Va chercher des patates pis l'éplucheur.", "Quel outil faut-il apporter ?",
     "eplucheur", ["patates", "couteau-chef", "rape"], "Oui, chef : des patates pis l'éplucheur."),
    ("c14", "Mets le pâté chinois au four.", "Où va le pâté chinois ?",
     "four", ["plaque", "friteuse", "poele-appareil"], "Oui, chef : le pâté chinois au four."),
    ("c15", "Râpe-moi du fromage. La râpe est à côté de l'évier.", "Avec quoi faut-il travailler ?",
     "rape", ["fromage", "evier", "eplucheur"], "Oui, chef : je râpe du fromage."),
    ("c16", "Avant de servir, lave la planche au désinfectant, pis change de tablier.", "Qu'est-ce qu'il faut changer ?",
     "tablier", ["desinfectant", "planche", "gants"], "Oui, chef : je change de tablier."),
]

# ── O4 · La commande modifiée ──────────────────────────────────────────────
# (id, voix, phrase du client, bonne (plat, changement, ingrédient),
#  autre (plat, changement, ingrédient), ce que l'employé redit)
# Les changements : sans · extra · a-part. La carte montre le plat en croquis,
# le changement ÉCRIT, l'ingrédient en croquis.
COMMANDES = [
    ("k01", "f", "Bonjour ! Un hamburger sans oignons, s'il vous plaît.",
     ("hamburger", "sans", "oignon"), ("club", "extra", "fromage"), "Un hamburger sans oignons, c'est bien ça ?"),
    ("k02", "m", "Je vais prendre une poutine, avec un extra fromage.",
     ("poutine", "extra", "fromage"), ("frites", "a-part", "bacon"), "Une poutine, extra fromage, c'est bien ça ?"),
    ("k03", "f", "Un club sandwich, mais sans tomates.",
     ("club", "sans", "tomate"), ("hamburger", "extra", "laitue"), "Un club sans tomates, c'est bien ça ?"),
    ("k04", "m", "Les crêpes, avec le sirop à part, s'il vous plaît.",
     ("crepes", "a-part", "sirop-erable"), ("pain-dore", "sans", "beurre"), "Des crêpes, le sirop à part, c'est bien ça ?"),
    ("k05", "f", "Des œufs-bacon… avec un extra bacon.",
     ("oeufs-bacon", "extra", "bacon"), ("crepes", "sans", "champignon"), "Des œufs-bacon, extra bacon, c'est bien ça ?"),
    ("k06", "m", "Une poutine… non, attendez : des frites, avec le fromage à part.",
     ("frites", "a-part", "fromage"), ("poutine", "sans", "oignon"), "Des frites, le fromage à part, c'est bien ça ?"),
    ("k07", "f", "Un hamburger avec un extra bacon.",
     ("hamburger", "extra", "bacon"), ("club", "sans", "fromage"), "Un hamburger, extra bacon, c'est bien ça ?"),
    ("k08", "m", "Le club, mais sans bacon.",
     ("club", "sans", "bacon"), ("hamburger", "extra", "tomate"), "Un club sans bacon, c'est bien ça ?"),
    ("k09", "f", "Des rôties, avec le beurre à part.",
     ("roties", "a-part", "beurre"), ("pain-dore", "sans", "sirop-erable"), "Des rôties, le beurre à part, c'est bien ça ?"),
    ("k10", "m", "Une poutine sans… non, avec un extra de champignons.",
     ("poutine", "extra", "champignon"), ("frites", "sans", "fromage"), "Une poutine, extra champignons, c'est bien ça ?"),
    ("k11", "f", "Du pain doré, sans sirop.",
     ("pain-dore", "sans", "sirop-erable"), ("crepes", "a-part", "beurre"), "Du pain doré sans sirop, c'est bien ça ?"),
    ("k12", "m", "Un hamburger, avec les oignons à part.",
     ("hamburger", "a-part", "oignon"), ("club", "extra", "laitue"), "Un hamburger, les oignons à part, c'est bien ça ?"),
]
CHANGEMENTS = {"sans": "sans", "extra": "extra", "a-part": "à part"}

# ── O2 · L'allergie ────────────────────────────────────────────────────────
# LA RÈGLE, écrite ici une fois, affichée avant la série et citée après.
REGLE = ("Une allergie, c'est sérieux : on la fait répéter, on l'écrit sur la commande, "
         "on la dit à la cuisine. On ne dit JAMAIS « il n'y en a pas » sans avoir vérifié. "
         "Une simple préférence (« je n'aime pas ») n'est pas une allergie : on l'écrit, c'est tout.")

# (id, qui parle, voix, phrase, contre-exemple ?, [(acte, statut)]) —
# statut : "juste" · "faux" · "grave" (l'erreur éliminatoire de l'objectif O2).
# « qui » : client (je suis en salle) · salle (le serveur parle à la cuisine) ·
# chef (je suis en cuisine).
ALLERGIES = [
    ("a01", "client", "f", "Je suis allergique aux arachides. Est-ce qu'il y en a dans le pouding chômeur ?", False, [
        ("Je vérifie avec la cuisine, puis je reviens.", "juste"),
        ("Non, il n'y en a pas dans le pouding.", "grave"),
        ("Je vous conseille de ne pas prendre de dessert.", "faux")]),
    ("a02", "client", "m", "Mon fils a une allergie au lait. La poutine, c'est correct pour lui ?", False, [
        ("Non, il y a du fromage. Je vérifie le reste.", "juste"),
        ("Oui, la poutine, c'est correct pour lui.", "grave"),
        ("Il peut enlever le fromage lui-même, dans l'assiette.", "grave")]),
    ("a03", "salle", "f", "Table quatre, le club : allergie au sésame !", False, [
        ("Je redis « allergie au sésame » et je change de pain.", "juste"),
        ("J'enlève les graines du pain avec un couteau.", "grave"),
        ("Je continue : un club, ça n'a jamais de sésame, voyons.", "grave")]),
    ("a04", "client", "m", "Est-ce qu'il y a des noix dans la tarte au sucre ?", False, [
        ("Je vérifie avec la cuisine, puis je vous le dis.", "juste"),
        ("Non, jamais : c'est juste du sucre et de la crème.", "grave"),
        ("Je ne sais pas, désolé. Voulez-vous autre chose ?", "faux")]),
    ("a05", "client", "f", "Je n'aime pas les champignons. Le hamburger, sans champignons, s'il vous plaît.", True, [
        ("D'accord, j'écris « sans champignons ».", "juste"),
        ("J'annonce une allergie aux champignons à la cuisine.", "faux"),
        ("Désolé, on ne peut rien changer aux hamburgers.", "faux")]),
    ("a06", "client", "m", "J'ai une allergie aux fruits de mer. La soupe du jour, qu'est-ce qu'il y a dedans ?", False, [
        ("Je demande à la cuisine ce qu'il y a dans la soupe.", "juste"),
        ("C'est une soupe aux légumes, il n'y a pas de problème.", "grave"),
        ("Je ne sais pas. Prenez plutôt un club sandwich.", "faux")]),
    ("a07", "chef", "m", "Allergie aux arachides, table deux ! Change de gants pis prends une planche propre.", False, [
        ("« Oui, chef : table deux, arachides. » Je change de gants.", "juste"),
        ("Je garde mes gants : je viens de les laver à l'eau.", "grave"),
        ("Je fais la commande d'abord, pis je change de gants après.", "grave")]),
    ("a08", "client", "m", "Pas d'oignons pour moi, s'il vous plaît. C'est juste que je n'aime pas ça.", True, [
        ("J'écris « sans oignons », c'est tout.", "juste"),
        ("Je crie « allergie aux oignons ! » à la cuisine.", "faux"),
        ("Je lui explique que les oignons sont déjà cuits.", "faux")]),
    ("a09", "client", "f", "Mon mari est allergique au poisson. Les frites, elles cuisent dans la même huile que le poisson ?", False, [
        ("Je vérifie avec la cuisine avant de répondre.", "juste"),
        ("Non, jamais : les frites ont leur propre friteuse.", "grave"),
        ("Oui, mais ce n'est pas grave, l'huile est très chaude.", "grave")]),
    ("a10", "salle", "m", "Le pain doré, table six : allergie aux œufs !", False, [
        ("Je dis à la salle : le pain doré contient des œufs.", "juste"),
        ("Je fais le pain doré avec moins d'œufs, c'est correct.", "grave"),
        ("Je n'ai rien entendu, je continue mes commandes.", "grave")]),
]
QUI = {"client": "Un client vous parle, en salle.", "salle": "Le serveur parle à la cuisine. Vous êtes en cuisine.",
       "chef": "Le chef vous parle. Vous êtes en cuisine."}

# ── O3 · Les pièges ────────────────────────────────────────────────────────
# (id du piège, [trois contrastes pris AILLEURS dans le lexique, à la main])
PIEGES = [
    ("poele",            ["poele-appareil", "chaudron", "plaque"]),
    ("poele-appareil",   ["poele", "four", "plaque"]),
    ("chaudron",         ["poele", "bol", "passoire"]),
    ("patates",          ["pomme", "oignon", "champignon"]),
    ("ble-inde",         ["feves", "riz", "pates"]),
    ("feves",            ["ble-inde", "riz", "champignon"]),
    ("bleuets",          ["pomme", "citron", "feves"]),
    ("roties",           ["pain", "pain-dore", "crepes"]),
    ("pain-dore",        ["roties", "crepes", "pain"]),
    ("alg-arachides",    ["alg-noix", "alg-sesame", "alg-soya"]),
    ("ustensiles-table", ["pince", "louche", "couteau-chef"]),
    ("liqueur",          ["cafe", "verre", "lait"]),
    ("plaque",           ["poele-appareil", "four", "planche"]),
]
ORDINAIRES = ["assiette", "tomate", "fouet", "friteuse", "gants", "verre"]


def verifier():
    import importlib.util, pathlib, re
    p = pathlib.Path(__file__).with_name("lexique.py")
    spec = importlib.util.spec_from_file_location("lex_resto", p)
    L = importlib.util.module_from_spec(spec); spec.loader.exec_module(L)
    img = {e[0] for e in L.LEXIQUE if e[4] == "croquis"}
    mots = {e[0]: e[2] for e in L.LEXIQUE}
    for i, _ph, _q, b, d, _r in CONSIGNES:
        assert b in img and all(x in img for x in d) and len(set([b] + d)) == 4, i
    for i, _v, _ph, bon, autre, _r in COMMANDES:
        assert bon[0] in img and autre[0] in img and bon[2] in img and autre[2] in img, i
        assert all(a != b for a, b in zip(bon, autre)), f"{i} : les deux cartes doivent différer sur les trois traits"
    for i, qui, _v, _ph, _c, actes in ALLERGIES:
        assert qui in QUI and sum(s == "juste" for _a, s in actes) == 1, i
        n = [len(a) for a, _s in actes]
        assert max(n) <= 1.25 * min(n) + 4, f"{i} : longueurs trop inégales {n}"
    # La bonne n'est pas « la plus longue » plus souvent qu'au hasard.
    plus_longue = sum(max(actes, key=lambda x: len(x[0]))[1] == "juste" for *_x, actes in ALLERGIES)
    assert plus_longue * 3 <= len(ALLERGIES) + 1, f"la bonne est la plus longue {plus_longue} fois"
    assert sum(c for *_x, c, _a in ALLERGIES) >= 2, "au moins deux contre-exemples"
    for i, c in PIEGES:
        assert i in img and all(x in img for x in c) and mots[i], i
    assert all(x in img for x in ORDINAIRES)

    # Une consigne à plusieurs objets met les autres objets NOMMÉS parmi les choix.
    def nomme(ident, phrase):
        tete = re.sub(r"^(le |la |les |l'|un |une |des )", "", mots[ident].lower()).split(" ")[0]
        base = tete[:-1] if tete.endswith(("s", "x")) and len(tete) > 4 else tete
        return bool(re.search(r"(?<![\w-])" + re.escape(base) + r"[sx]?(?![\w-])", phrase.lower()))
    n = sum(any(nomme(d, ph) for d in dd) for _i, ph, _q, _b, dd, _r in CONSIGNES)
    assert n * 2 >= len(CONSIGNES), f"{n} consignes sur {len(CONSIGNES)} nomment un autre objet parmi les choix"
    return n


if __name__ == "__main__":
    n = verifier()
    print(f"{len(CONSIGNES)} consignes ({n} avec un autre objet nommé parmi les choix) · "
          f"{len(COMMANDES)} commandes · {len(ALLERGIES)} allergies "
          f"({sum(a[4] for a in ALLERGIES)} contre-exemples) · {len(PIEGES)} pièges")
