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

Audit de la boucle didactique, tour 1 (30 sept. 2026) : 1 bloquant, 8 majeurs,
11 mineurs. Chaque correction porte son code dans le commentaire concerné.
"""

# ── O1 · La consigne du chef ───────────────────────────────────────────────
# (id, phrase du chef, question, bonne, [distracteurs], ce que l'employé redit)
# Audit, tour 1 : (D4) l'objet nommé dans la QUESTION n'est jamais parmi les
# choix — on l'écartait en lisant (vérifié plus bas) ; (C4) les réponses à
# redire sont des phrases régulières, avec un verbe et « et », jamais « pis » ;
# c14 ne se réussit plus par le bon sens (« pas sur la plaque »).
CONSIGNES = [
    ("c01", "Coupe les carottes en dés, pas en julienne.", "Comment faut-il couper les carottes ?",
     "en-des", ["julienne", "trancher", "eplucher"], "Oui, chef : je coupe les carottes en dés."),
    ("c02", "Va chercher du fromage en grains dans la chambre froide.", "Qu'est-ce qu'il faut aller chercher ?",
     "fromage-grains", ["fromage", "chambre-froide", "frigo"], "Oui, chef : je vais chercher du fromage en grains."),
    ("c03", "Mets les frites dans la friteuse, pas sur la plaque.", "Où vont les frites ?",
     "friteuse", ["plaque", "four", "poele-appareil"], "Oui, chef : je mets les frites dans la friteuse."),
    ("c04", "Coupe-moi trois tomates, pis après, lave la planche.", "Qu'est-ce qu'il faut laver ?",
     "planche", ["tomate", "couteau-chef", "bac"], "Oui, chef : je coupe trois tomates, et je lave la planche."),
    ("c05", "J'ai besoin de la passoire pour les pâtes, vite !", "Qu'est-ce que le chef veut ?",
     "passoire", ["pates", "chaudron", "rape"], "Oui, chef : je vous apporte la passoire."),
    ("c06", "Sors le poulet du congélateur pis mets-le dans le frigo.", "Où va le poulet ?",
     "frigo", ["congelateur", "chambre-froide", "four"], "Oui, chef : je mets le poulet dans le frigo."),
    ("c07", "Donne-moi la poêle, pas le chaudron.", "Qu'est-ce que le chef veut ?",
     "poele", ["chaudron", "poele-appareil", "plaque"], "Oui, chef : je vous donne la poêle."),
    ("c08", "Il manque de laitue dans le bac. Remplis-le.", "Qu'est-ce qui manque ?",
     "laitue", ["bac", "oignon", "tomate"], "Oui, chef : je remplis le bac de laitue."),
    ("c09", "Mets des gants avant de toucher au poulet cru.", "Qu'est-ce qu'il faut mettre ?",
     "gants", ["poulet", "tablier", "filet"], "Oui, chef : je mets des gants."),
    ("c10", "Prends le thermomètre, pas la louche, pis vérifie la soupe.", "Avec quoi faut-il vérifier la soupe ?",
     "thermometre", ["louche", "tasse-mesurer", "etiquette"], "Oui, chef : je vérifie la soupe avec le thermomètre."),
    ("c11", "Oublie pas l'étiquette sur le bac d'hier, pis rapporte le thermomètre.", "Qu'est-ce qu'il faut mettre sur le bac ?",
     "etiquette", ["thermometre", "tablier", "gants"], "Oui, chef : je mets une étiquette sur le bac, et je rapporte le thermomètre."),
    ("c12", "Les assiettes sales, mets-les dans le lave-vaisselle, pas dans l'évier.", "Où vont les assiettes sales ?",
     "lave-vaisselle", ["evier", "lavabo", "bac-vaisselle"], "Oui, chef : je les mets dans le lave-vaisselle."),
    ("c13", "Va chercher des patates pis l'éplucheur.", "Quel outil faut-il apporter ?",
     "eplucheur", ["patates", "couteau-chef", "rape"], "Oui, chef : je vais chercher des patates et l'éplucheur."),
    ("c14", "Le pâté chinois, mets-le au four, pas sur la plaque.", "Où va le pâté chinois ?",
     "four", ["plaque", "friteuse", "poele-appareil"], "Oui, chef : je mets le pâté chinois au four."),
    ("c15", "Râpe-moi du fromage. La râpe est à côté de l'évier.", "Avec quoi faut-il travailler ?",
     "rape", ["fromage", "evier", "eplucheur"], "Oui, chef : je râpe du fromage."),
    ("c16", "Avant de servir, lave la planche au désinfectant, pis change de tablier.", "Qu'est-ce qu'il faut changer ?",
     "tablier", ["desinfectant", "planche", "gants"], "Oui, chef : je lave la planche, et je change de tablier."),
]

# ── O4 · La commande modifiée ──────────────────────────────────────────────
# (id, voix, phrase du client, bonne (plat, changement, ingrédient),
#  autre (plat, changement, ingrédient), ce que l'employé redit)
# La carte montre le plat en croquis, le changement ÉCRIT, l'ingrédient en
# croquis. Audit, tour 1 : (A3) « avec » et la cuisson manquaient à l'objectif ;
# (D4) avec des cartes qui ne différaient que d'un nom, reconnaître le plat et
# l'ingrédient suffisait : une carte fausse diffère maintenant de la bonne par
# le SEUL changement (le hamburger « sans oignons » servi « extra oignons »).
# Les commandes de CUISSON (ingrédient None) se répondent parmi trois cuissons
# du même plat.
COMMANDES = [
    ("k01", "f", "Bonjour ! Un hamburger sans oignons, s'il vous plaît.",
     ("hamburger", "sans", "oignon"), ("club", "extra", "fromage"), "Un hamburger sans oignons, c'est bien ça ?"),
    ("k02", "m", "Je vais prendre une poutine, avec un extra fromage.",
     ("poutine", "extra", "fromage"), ("frites", "a-part", "bacon"), "Une poutine avec un extra fromage, c'est bien ça ?"),
    ("k03", "f", "Un club sandwich, mais sans tomates.",
     ("club", "sans", "tomate"), ("hamburger", "extra", "laitue"), "Un club sans tomates, c'est bien ça ?"),
    ("k04", "m", "Les crêpes, avec le sirop à part, s'il vous plaît.",
     ("crepes", "a-part", "sirop-erable"), ("pain-dore", "sans", "beurre"), "Des crêpes, le sirop à part, c'est bien ça ?"),
    ("k05", "f", "Des œufs-bacon… avec un extra bacon.",
     ("oeufs-bacon", "extra", "bacon"), ("crepes", "sans", "champignon"), "Des œufs-bacon avec un extra bacon, c'est bien ça ?"),
    ("k06", "m", "Une poutine… non, attendez : des frites, avec le fromage à part.",
     ("frites", "a-part", "fromage"), ("poutine", "sans", "oignon"), "Des frites, le fromage à part, c'est bien ça ?"),
    ("k07", "f", "Un hamburger avec un extra bacon.",
     ("hamburger", "extra", "bacon"), ("club", "sans", "fromage"), "Un hamburger avec un extra bacon, c'est bien ça ?"),
    ("k08", "m", "Le club, mais sans bacon.",
     ("club", "sans", "bacon"), ("hamburger", "extra", "tomate"), "Un club sans bacon, c'est bien ça ?"),
    ("k09", "f", "Des rôties, avec le beurre à part.",
     ("roties", "a-part", "beurre"), ("pain-dore", "sans", "sirop-erable"), "Des rôties, le beurre à part, c'est bien ça ?"),
    ("k10", "m", "Une poutine sans… non, avec un extra de champignons.",
     ("poutine", "extra", "champignon"), ("frites", "sans", "fromage"), "Une poutine avec un extra de champignons, c'est bien ça ?"),
    ("k11", "f", "Du pain doré, sans sirop.",
     ("pain-dore", "sans", "sirop-erable"), ("crepes", "a-part", "beurre"), "Du pain doré sans sirop, c'est bien ça ?"),
    ("k12", "m", "Un hamburger, avec les oignons à part.",
     ("hamburger", "a-part", "oignon"), ("club", "extra", "laitue"), "Un hamburger, les oignons à part, c'est bien ça ?"),
    ("k13", "f", "Des frites avec du fromage, s'il vous plaît.",
     ("frites", "avec", "fromage"), ("poutine", "sans", "oignon"), "Des frites avec du fromage, c'est bien ça ?"),
    ("k14", "m", "Le club, avec des champignons.",
     ("club", "avec", "champignon"), ("hamburger", "sans", "tomate"), "Un club avec des champignons, c'est bien ça ?"),
    ("k15", "f", "Des crêpes avec du bacon, s'il vous plaît.",
     ("crepes", "avec", "bacon"), ("pain-dore", "a-part", "sirop-erable"), "Des crêpes avec du bacon, c'est bien ça ?"),
    # Audit, tour 2 (A2) : les cuissons se prennent sur un STEAK. Le hamburger
    # (bœuf haché) se sert toujours bien cuit — norme à revérifier au cadrage
    # (MAPAQ), comme la zone de danger.
    ("k16", "m", "Un steak bien cuit, s'il vous plaît.",
     ("steak", "bien-cuit", None), None, "Un steak bien cuit, c'est bien ça ?"),
    ("k17", "f", "Mon steak, je le veux saignant… non, à point.",
     ("steak", "a-point", None), None, "Un steak à point, c'est bien ça ?"),
    ("k18", "m", "Le steak, pas trop cuit : saignant.",
     ("steak", "saignant", None), None, "Un steak saignant, c'est bien ça ?"),
]
CHANGEMENTS = {"sans": "sans", "extra": "extra", "a-part": "à part", "avec": "avec",
               "bien-cuit": "bien cuit", "a-point": "à point", "saignant": "saignant"}
CUISSONS = ["saignant", "a-point", "bien-cuit"]

# ── O2 · L'allergie ────────────────────────────────────────────────────────
# LA RÈGLE, écrite ici une fois, affichée avant la série et citée après. Audit,
# tour 1 (C5/C6) : trois gestes numérotés, courts, et lus par une voix.
REGLE = [
    "Si ce n'est pas clair, je fais répéter : « Allergique à quoi ? »",
    "Je l'écris sur la commande et je le dis à la cuisine.",
    "Je vérifie. Je ne dis jamais « il n'y en a pas » sans vérifier.",
]
REGLE_PREFERENCE = "« Je n'aime pas » n'est pas une allergie : je l'écris, c'est tout."
REGLE_CUISINE = "En cuisine, je redis l'allergie et la table, et je change mes gestes."
# Audit, tour 2 (A3/E1) : la frontière faux/grave, écrite UNE fois et affichée
# avec la règle. Chaque statut « grave » se relit contre elle.
CRITERE_GRAVE = ("Erreur grave : dire ou laisser croire qu'un plat est sûr sans avoir vérifié, "
                 "ou ne pas transmettre la bonne allergie.")

# (id, qui parle, voix, phrase, contre-exemple ?, [(acte, statut, pourquoi)]) —
# statut : "juste" · "faux" · "grave" (l'erreur éliminatoire de O2). Le
# POURQUOI est dit après le choix, avant le rappel de la règle (audit E1).
# « qui » : client (je suis en salle) · salle (le serveur parle à la cuisine) ·
# chef (je suis en cuisine).
# Audit, tour 1 (A3 bloquant) : « faire répéter » n'était jamais pratiqué, et
# « écrire » n'était juste que pour les préférences : a11-a14 le corrigent.
ALLERGIES = [
    ("a01", "client", "f", "Je suis allergique aux arachides. Est-ce qu'il y en a dans le pouding chômeur ?", False, [
        ("Je vérifie avec la cuisine s'il y a des arachides.", "juste", "On ne sait pas ce qu'il y a dans un dessert sans demander."),
        ("Non, il n'y a pas d'arachides dans le pouding chômeur.", "grave", "Vous n'avez pas vérifié : c'est l'erreur qui peut rendre quelqu'un très malade."),
        ("Je vérifie avec la cuisine s'il y a des noix.", "grave", "Elle a dit « arachides » : les noix, c'est autre chose.")]),
    ("a02", "client", "m", "Mon fils a une allergie au lait. La poutine, c'est correct pour lui ?", False, [
        ("Non, il y a du fromage. Je vérifie le reste.", "juste", "Le fromage est fait avec du lait ; la sauce aussi peut en contenir."),
        ("Oui, la poutine, c'est correct pour lui.", "grave", "Le fromage est fait avec du lait."),
        ("Il peut enlever le fromage lui-même, dans l'assiette.", "grave", "Enlever le fromage n'enlève pas le lait : il en reste dans l'assiette.")]),
    ("a03", "salle", "f", "Table quatre, le club : allergie au sésame !", False, [
        ("Je redis « sésame, table quatre » et je vérifie le pain.", "juste", "Le sésame se cache dans le pain et dans certaines sauces."),
        ("Je redis « soya, table quatre » et je vérifie le pain.", "grave", "Le serveur a dit « sésame », pas « soya »."),
        ("Je continue : il n'y a jamais de sésame dans le pain du club.", "grave", "« Jamais » sans vérifier : c'est l'erreur éliminatoire.")]),
    ("a04", "client", "m", "Est-ce qu'il y a des noix dans la tarte au sucre ?", False, [
        ("Je vérifie avec la cuisine, puis je vous le dis.", "juste", "Même sans le mot « allergie », une question sur un allergène se vérifie."),
        ("Non, jamais : c'est juste du sucre et de la crème.", "grave", "Vous n'avez pas vérifié la recette."),
        ("Je ne sais pas, désolé. Voulez-vous autre chose ?", "faux", "« Je ne sais pas » n'aide pas : on va demander à la cuisine.")]),
    ("a05", "client", "f", "Je n'aime pas les champignons. Le hamburger, sans champignons, s'il vous plaît.", True, [
        ("D'accord, j'écris « sans champignons ».", "juste", ""),
        ("J'annonce une allergie aux champignons à la cuisine.", "faux", "Elle a dit « je n'aime pas » : ce n'est pas une allergie."),
        ("Je refuse : on ne change pas les plats ici.", "faux", "On peut enlever un ingrédient : on l'écrit, c'est tout.")]),
    ("a06", "client", "m", "J'ai une allergie aux fruits de mer. La soupe du jour, qu'est-ce qu'il y a dedans ?", False, [
        ("Je demande à la cuisine s'il y a des fruits de mer dans la soupe.", "juste", "Seule la cuisine sait ce qu'il y a dans la soupe aujourd'hui."),
        ("C'est une bonne soupe aux légumes, il n'y a aucun problème pour vous.", "grave", "Vous n'avez pas vérifié : un bouillon peut contenir des fruits de mer."),
        ("Je demande à la cuisine s'il y a du poisson dans la soupe.", "grave", "Il a dit « fruits de mer » : c'est pour eux qu'il faut demander.")]),
    ("a07", "chef", "m", "Allergie aux arachides, table deux ! Change de gants pis prends une planche propre.", False, [
        ("« Oui, chef : arachides, table deux. » Gants et planche propres.", "juste", "Je redis l'allergie au chef, et je fais les deux gestes demandés."),
        ("Je garde mes gants : je viens de les laver à l'eau.", "grave", "L'eau n'enlève pas les arachides des gants : on les change."),
        ("« Oui, chef : arachides, table six. » Gants et planche propres.", "grave", "Le chef a dit table DEUX : la mauvaise table recevrait l'assiette.")]),
    ("a08", "client", "m", "Pas d'oignons pour moi, s'il vous plaît. C'est juste que je n'aime pas ça.", True, [
        ("J'écris « sans oignons », c'est tout.", "juste", ""),
        ("Je crie « allergie aux oignons ! » à la cuisine.", "faux", "Il a dit « je n'aime pas ça » : ce n'est pas une allergie."),
        ("Je lui dis d'enlever les oignons lui-même.", "faux", "On peut les enlever à la cuisine : on l'écrit sur la commande.")]),
    ("a09", "client", "f", "Mon mari est allergique au poisson. Les frites, elles cuisent dans la même huile que le poisson ?", False, [
        ("Je vérifie avec la cuisine pour le poisson.", "juste", "Seule la cuisine sait quelle friteuse sert à quoi."),
        ("Non, jamais : les frites ont leur propre friteuse.", "grave", "Vous n'avez pas vérifié."),
        ("Je vérifie avec la cuisine pour les fruits de mer.", "grave", "Elle a dit « poisson » : c'est pour le poisson qu'il faut vérifier.")]),
    ("a10", "salle", "m", "Le pain doré, table six : allergie aux œufs !", False, [
        ("Je redis « œufs, table six » : le pain doré en contient.", "juste", "Le pain doré est fait avec des œufs : le client doit choisir autre chose."),
        ("Je fais le pain doré avec moins d'œufs pour la table six.", "grave", "Même un peu d'œuf peut rendre malade."),
        ("Je n'ai rien entendu, je continue mes commandes.", "grave", "Une allergie annoncée se redit toujours.")]),
    ("a11", "client", "f", "Attention, j'ai une allergie ! Le hamburger, c'est correct pour moi ?", False, [
        ("Pardon, vous êtes allergique à quoi ?", "juste", "Elle n'a pas dit à quoi : il faut le savoir avant tout."),
        ("Oui, le hamburger, c'est correct pour vous.", "grave", "Vous ne savez même pas à quoi elle est allergique."),
        ("J'écris « allergie » sur la commande, c'est tout.", "grave", "Sans savoir à quoi, la cuisine ne peut pas la traiter : l'allergie n'est pas transmise.")]),
    ("a12", "client", "m", "Je ne digère pas le lait. La soupe, il y a de la crème dedans ?", False, [
        ("C'est une allergie ? Je vérifie la soupe avec la cuisine.", "juste", "« Je ne digère pas » n'est pas clair : on demande, puis on vérifie."),
        ("Non, il n'y a pas de crème dans la soupe du jour.", "grave", "Vous n'avez pas vérifié."),
        ("Ce n'est pas une allergie : je lui sers la soupe du jour.", "grave", "Vous dites que c'est sûr sans avoir demandé ni vérifié.")]),
    ("a13", "client", "f", "Un hamburger, s'il vous plaît. Je suis allergique à la moutarde.", False, [
        ("J'écris « allergie : moutarde » et je le dis à la cuisine.", "juste", "Écrit ET dit : la cuisine change aussi ses gestes."),
        ("Il n'y a jamais de moutarde dans le hamburger de la maison.", "grave", "Vous n'avez pas vérifié : la sauce peut en contenir."),
        ("J'écris « sans moutarde », comme pour les oignons.", "grave", "« Sans », c'est pour une préférence : l'allergie n'est pas transmise à la cuisine.")]),
    ("a14", "client", "m", "Une poutine, s'il vous plaît. Pis ma fille est allergique aux œufs.", False, [
        ("J'écris l'allergie aux œufs et je la dis à la cuisine.", "juste", "Même si le plat n'en a pas, la cuisine doit le savoir."),
        ("Pas de problème : une poutine, ça n'a pas d'œufs.", "grave", "Vous n'avez pas vérifié la sauce ni la friteuse."),
        ("J'écris l'allergie au lait et je la dis à la cuisine.", "grave", "Il a dit « œufs », pas « lait »."),
    ]),
]
QUI = {"client": "Un client vous parle, en salle.", "salle": "Le serveur parle à la cuisine. Vous êtes en cuisine.",
       "chef": "Le chef vous parle. Vous êtes en cuisine."}

# « Je le redis » : les deux formules, montrées AVANT la série (audit C4).
FORMULES = [("chef", "Au chef, je réponds : « Oui, chef : … »", "c05"),
            ("client", "Au client, je redis la commande : « …, c'est bien ça ? »", "k01")]

# Les seuils du test, dits à l'apprenant (audit A1).
SEUILS = {"chef": "Au test : 7 consignes sur 8.", "commande": "Au test : 5 commandes sur 6.",
          "ecoute": "Au test : 18 mots sur 20.", "image": "Au test : 18 mots sur 20.", "pieges": "Au test : 18 mots sur 20.",
          "allergie": "Au test : une seule erreur grave fait échouer."}

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

    def nomme(ident, phrase):
        tete = re.sub(r"^(le |la |les |l'|un |une |des )", "", mots[ident].lower()).split(" ")[0]
        base = tete[:-1] if tete.endswith(("s", "x")) and len(tete) > 4 else tete
        return bool(re.search(r"(?<![\w-])" + re.escape(base) + r"[sx]?(?![\w-])", phrase.lower()))

    for i, _ph, q, b, d, r in CONSIGNES:
        assert b in img and all(x in img for x in d) and len(set([b] + d)) == 4, i
        # (audit D4) l'objet nommé dans la question ne se trouve pas parmi les choix
        # (les gestes, sans article, se nomment par leur verbe : « couper » n'est pas un objet)
        noms = [x for x in [b] + d if re.match(r"^(le |la |les |l'|un |une |des )", mots[x])]
        assert not any(nomme(x, q) for x in noms), f"{i} : un choix est nommé dans la question"
        assert " pis " not in r, f"{i} : le modèle à redire dit « pis »"
    for i, _v, _ph, bon, autre, _r in COMMANDES:
        assert bon[1] in CHANGEMENTS, i
        if bon[2] is None:
            # La cuisson : la carte montre la COUPE (les croquis saignant, à point,
            # bien cuit sont des steaks) ; le plat n'a pas besoin de croquis.
            assert all(c in img for c in CUISSONS), i
            assert bon[1] in CUISSONS and autre is None, i
            continue
        assert bon[0] in img, i
        assert autre[0] in img and bon[2] in img and autre[2] in img, i
        assert all(a != b for a, b in zip(bon, autre)), f"{i} : les deux cartes doivent différer sur les trois traits"
    ch = [c[3][1] for c in COMMANDES]
    assert all(ch.count(k) >= 3 or k in CUISSONS for k in CHANGEMENTS), f"chaque changement au moins trois fois : {ch}"
    for i, qui, _v, _ph, _c, actes in ALLERGIES:
        assert qui in QUI and sum(s == "juste" for _a, s, _p in actes) == 1, i
        assert all(p for _a, s, p in actes if s != "juste"), f"{i} : un choix faux sans « pourquoi »"
        n = [len(a) for a, _s, _p in actes]
        assert max(n) <= 1.25 * min(n) + 6, f"{i} : longueurs trop inégales {n}"
    for i, _qui, _v, _ph, contre, actes in ALLERGIES:
        for a, st, _p in actes:
            if st == "faux" and not contre:
                assert not re.search(r"correct|conseille|prenez|pas de problème", a.lower()), f"{i} : « {a} » laisse croire que c'est sûr : grave"
    # (audit, tour 3) Un distracteur « voisin » nomme un AUTRE allergène ou une
    # autre table que la phrase ; et la juste de ces items nomme le bon.
    ALG = ["arachides", "noix", "sésame", "soya", "poisson", "fruits de mer", "lait", "œufs", "moutarde"]
    TAB = ["table deux", "table quatre", "table six"]
    def noms(t):
        t = t.lower()
        return {a for a in ALG + TAB if a in t}
    voisin = 0
    for i, _qui, _v, ph, contre, actes in ALLERGIES:
        if contre:
            continue
        dans = noms(ph)
        juste = next(a for a, st, _p in actes if st == "juste")
        if any(st == "grave" and noms(a) and not noms(a) <= dans for a, st, _p in actes):
            voisin += 1
            assert noms(juste) & dans, f"{i} : la juste ne nomme pas l'allergène (ou la table) de la phrase"
    assert voisin * 2 >= len(ALLERGIES) - 2, f"(D4) seulement {voisin} items où le bon geste porte le mauvais allergène"
    plus_longue = sum(max(actes, key=lambda x: len(x[0]))[1] == "juste" for *_x, actes in ALLERGIES)
    assert plus_longue * 3 <= len(ALLERGIES) + 1, f"la bonne est la plus longue {plus_longue} fois"
    assert sum(c for *_x, c, _a in ALLERGIES) >= 2, "au moins deux contre-exemples"
    # (audit A3) « faire répéter » et « écrire + dire à la cuisine » sont pratiqués
    justes = [next(a for a, s, _p in actes if s == "juste") for *_x, actes in ALLERGIES]
    assert sum("quoi" in a.lower() or "c'est une allergie" in a.lower() for a in justes) >= 2, "faire répéter : moins de deux items"
    assert sum("j'écris" in a.lower() and "cuisine" in a.lower() for a in justes) >= 2, "écrire ET dire : moins de deux items"
    for i, c in PIEGES:
        assert i in img and all(x in img for x in c) and mots[i], i
    assert all(x in img for x in ORDINAIRES)
    n = sum(any(nomme(d, ph) for d in dd) for _i, ph, _q, _b, dd, _r in CONSIGNES)
    assert n * 2 >= len(CONSIGNES), f"{n} consignes sur {len(CONSIGNES)} nomment un autre objet parmi les choix"
    return n


if __name__ == "__main__":
    n = verifier()
    print(f"{len(CONSIGNES)} consignes ({n} avec un autre objet nommé parmi les choix) · "
          f"{len(COMMANDES)} commandes · {len(ALLERGIES)} allergies "
          f"({sum(a[4] for a in ALLERGIES)} contre-exemples) · {len(PIEGES)} pièges")
