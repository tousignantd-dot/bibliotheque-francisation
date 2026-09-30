"""Le lexique de la trousse de restauration — la source unique (étape 0).

    python3 build/contenu/entreprise-restaurant/lexique.py   # vérifie et compte

Format de la Maison Francœur : (id, planche, mot, autre, dessin, note).
  · mot    = le mot d'ICI, avec son article : celui que le chef ou le client dira ;
  · autre  = l'autre qu'on entendra (France, métier, anglicisme de cuisine) ;
  · dessin = "croquis" (engendré seul) · "decor" (désigné dans le dessin du poste)
             · "" (sans image : phrases, repas, nombres) ;
  · note   = qui commence par « PIÈGE » = un faux ami d'ici ou un double sens.

Décisions de Daniel du 30 sept. 2026 : deux portes (cuisine d'abord), restaurant
familial québécois, formule Francœur. Le POSTE est porté par la planche : une
planche « cuisine » n'est pas montrée à la porte « salle », et inversement.

Écrit sans visite de cuisine : la visite (décidée, avant l'étape 1) arrêtera le
compte. Les listes réglementaires (allergènes de Santé Canada, zone de danger du
MAPAQ) sont à revérifier au cadrage, et le disent dans leur note.
"""

# (clé, titre, poste) — dans l'ordre où l'on entre dans le métier
PLANCHES = [
    ("cuisine", "La cuisine", "cuisine"),
    ("ustensiles", "Les ustensiles", "cuisine"),
    ("preparer", "Couper, préparer", "cuisine"),
    ("cuire", "Cuire", "deux"),
    ("aliments", "Les aliments", "deux"),
    ("plats", "Les plats de la maison", "deux"),
    ("allergenes", "Les allergènes", "deux"),
    ("hygiene", "L'hygiène et la sécurité", "deux"),
    ("vaisselle", "La vaisselle", "deux"),
    ("salle", "La salle", "salle"),
    ("temps", "Les repas, les nombres, le temps", "deux"),
    ("quart", "Le quart de travail", "deux"),
]

P = "PIÈGE"

LEXIQUE = [
    # ── La cuisine ─────────────────────────────────────────────────────────
    ("ligne", "cuisine", "la ligne", "la ligne chaude", "decor", "Le poste où l'on cuit et où l'on dresse les assiettes."),
    ("passe", "cuisine", "le passe", "", "decor", "Le comptoir entre la cuisine et la salle : les assiettes prêtes y attendent le serveur."),
    ("plonge", "cuisine", "la plonge", "", "decor", "Le poste où l'on lave la vaisselle. Celui qui y travaille : le plongeur."),
    ("lave-vaisselle", "cuisine", "le lave-vaisselle", "", "croquis", ""),
    ("chambre-froide", "cuisine", "la chambre froide", "la walk-in", "croquis", "Dans bien des cuisines d'ici, on dit « la walk-in »."),
    ("congelateur", "cuisine", "le congélateur", "le freezer", "croquis", ""),
    ("frigo", "cuisine", "le frigo", "le réfrigérateur", "croquis", ""),
    ("reserve", "cuisine", "la réserve", "le garde-manger", "", "Les produits secs : farine, riz, conserves."),
    ("friteuse", "cuisine", "la friteuse", "", "croquis", ""),
    ("plaque", "cuisine", "la plaque", "le grill", "croquis", f"{P} : deux sens — la plaque de cuisson du poste (le grill plat) et la plaque qu'on met au four."),
    ("four", "cuisine", "le four", "", "croquis", ""),
    ("poele-appareil", "cuisine", "le poêle", "la cuisinière", "croquis", f"{P} : au Québec, « le poêle » est la cuisinière ; « la poêle », c'est l'ustensile. Et « la cuisinière » est aussi la personne qui cuisine."),
    ("hotte", "cuisine", "la hotte", "", "croquis", ""),
    ("evier", "cuisine", "l'évier", "", "croquis", "Pour la vaisselle et les légumes ; les mains se lavent au lavabo, à part."),
    ("lavabo", "cuisine", "le lavabo pour les mains", "", "croquis", ""),
    ("poubelle", "cuisine", "la poubelle", "les vidanges", "croquis", "« Sortir les vidanges » : sortir les ordures."),

    # ── Les ustensiles ─────────────────────────────────────────────────────
    ("couteau-chef", "ustensiles", "le couteau du chef", "", "croquis", ""),
    ("planche", "ustensiles", "la planche à découper", "", "croquis", "Souvent une couleur par aliment : on ne coupe pas le poulet cru sur la planche des légumes."),
    ("bol", "ustensiles", "le bol à mélanger", "le cul-de-poule", "croquis", "« Cul-de-poule » : le mot de métier."),
    ("fouet", "ustensiles", "le fouet", "", "croquis", ""),
    ("louche", "ustensiles", "la louche", "", "croquis", ""),
    ("pince", "ustensiles", "la pince", "", "croquis", ""),
    ("spatule", "ustensiles", "la spatule", "", "croquis", ""),
    ("poele", "ustensiles", "la poêle", "", "croquis", f"{P} : « la poêle » (l'ustensile) n'est pas « le poêle » (la cuisinière)."),
    ("chaudron", "ustensiles", "le chaudron", "la casserole", "croquis", f"{P} : au Québec, « un chaudron » ; en France, « une casserole » ou « une marmite »."),
    ("bac", "ustensiles", "le bac", "le contenant", "croquis", "Le bac en inox du poste ; on entend aussi « un pan »."),
    ("passoire", "ustensiles", "la passoire", "", "croquis", ""),
    ("rape", "ustensiles", "la râpe", "", "croquis", ""),
    ("eplucheur", "ustensiles", "l'éplucheur", "l'économe", "croquis", ""),
    ("tasse-mesurer", "ustensiles", "la tasse à mesurer", "", "croquis", ""),

    # ── Couper, préparer ───────────────────────────────────────────────────
    ("eplucher", "preparer", "éplucher", "peler", "croquis", ""),
    ("laver-legumes", "preparer", "laver les légumes", "", "", ""),
    ("trancher", "preparer", "trancher", "couper en tranches", "croquis", ""),
    ("en-des", "preparer", "couper en dés", "", "croquis", ""),
    ("hacher", "preparer", "hacher", "", "croquis", ""),
    ("emincer", "preparer", "émincer", "", "croquis", ""),
    ("julienne", "preparer", "couper en julienne", "", "croquis", ""),
    ("raper", "preparer", "râper", "", "", ""),
    ("mariner", "preparer", "faire mariner", "", "", ""),
    ("portionner", "preparer", "portionner", "faire les portions", "", ""),
    ("decongeler", "preparer", "décongeler", "", "", "Au frigo, jamais sur le comptoir."),
    ("melanger", "preparer", "mélanger", "", "", ""),

    # ── Cuire ──────────────────────────────────────────────────────────────
    ("bouillir", "cuire", "faire bouillir", "", "", ""),
    ("frire", "cuire", "faire frire", "", "", ""),
    ("griller", "cuire", "griller", "", "", ""),
    ("rotir", "cuire", "rôtir", "", "", ""),
    ("cuire-four", "cuire", "cuire au four", "", "", ""),
    ("rechauffer", "cuire", "réchauffer", "", "", ""),
    ("gratiner", "cuire", "gratiner", "", "", ""),
    ("saignant", "cuire", "saignant", "", "croquis", "La viande encore rouge au centre."),
    ("a-point", "cuire", "à point", "médium", "croquis", ""),
    ("bien-cuit", "cuire", "bien cuit", "", "croquis", ""),
    ("cru", "cuire", "cru", "", "", ""),

    # ── Les aliments ───────────────────────────────────────────────────────
    ("boeuf-hache", "aliments", "le bœuf haché", "", "croquis", ""),
    ("poulet", "aliments", "le poulet", "", "croquis", ""),
    ("jambon", "aliments", "le jambon", "", "croquis", ""),
    ("bacon", "aliments", "le bacon", "", "croquis", ""),
    ("saucisse", "aliments", "la saucisse", "", "croquis", ""),
    ("poisson", "aliments", "le poisson", "", "croquis", ""),
    ("oeufs", "aliments", "les œufs", "", "croquis", ""),
    ("fromage", "aliments", "le fromage", "", "croquis", ""),
    ("fromage-grains", "aliments", "le fromage en grains", "", "croquis", "Celui de la poutine. Il fait « couic » sous la dent quand il est frais."),
    ("lait", "aliments", "le lait", "", "croquis", ""),
    ("creme", "aliments", "la crème", "", "croquis", ""),
    ("beurre", "aliments", "le beurre", "", "croquis", ""),
    ("pain", "aliments", "le pain", "", "croquis", ""),
    ("pates", "aliments", "les pâtes", "", "croquis", ""),
    ("riz", "aliments", "le riz", "", "croquis", ""),
    ("patates", "aliments", "les patates", "les pommes de terre", "croquis", f"{P} : au Québec, « les patates » ; en France, « les pommes de terre »."),
    ("oignon", "aliments", "l'oignon", "", "croquis", ""),
    ("tomate", "aliments", "la tomate", "", "croquis", ""),
    ("laitue", "aliments", "la laitue", "", "croquis", ""),
    ("carotte", "aliments", "la carotte", "", "croquis", ""),
    ("champignon", "aliments", "le champignon", "", "croquis", ""),
    ("poivron", "aliments", "le poivron", "", "croquis", ""),
    ("ble-inde", "aliments", "le blé d'Inde", "le maïs", "croquis", f"{P} : au Québec, « le blé d'Inde » ; ailleurs, « le maïs »."),
    ("feves", "aliments", "les fèves", "les haricots", "croquis", f"{P} : au Québec, « les fèves » (les fèves au lard) ; en France, « les haricots »."),
    ("bleuets", "aliments", "les bleuets", "les myrtilles", "croquis", f"{P} : au Québec, « les bleuets » ; en France, « les myrtilles »."),
    ("pomme", "aliments", "la pomme", "", "croquis", ""),
    ("citron", "aliments", "le citron", "", "croquis", ""),
    ("farine", "aliments", "la farine", "", "croquis", ""),
    ("sucre", "aliments", "le sucre", "", "", ""),
    ("sel-poivre", "aliments", "le sel et le poivre", "", "croquis", ""),
    ("huile", "aliments", "l'huile", "", "croquis", ""),
    ("sirop-erable", "aliments", "le sirop d'érable", "", "croquis", ""),

    # ── Les plats de la maison ─────────────────────────────────────────────
    ("poutine", "plats", "la poutine", "", "croquis", "Des frites, du fromage en grains, de la sauce brune."),
    ("steak", "plats", "le steak", "le bifteck", "", "Se commande saignant, à point ou bien cuit. Le hamburger (bœuf haché), lui, se sert toujours bien cuit — norme à revérifier (MAPAQ)."),
    ("pate-chinois", "plats", "le pâté chinois", "", "croquis", "Bœuf haché, blé d'Inde, patates pilées."),
    ("club", "plats", "le club sandwich", "", "croquis", ""),
    ("hamburger", "plats", "le hamburger", "le burger", "croquis", ""),
    ("hot-chicken", "plats", "le hot chicken", "", "croquis", "Du poulet entre deux tranches de pain, couvert de sauce brune et de petits pois."),
    ("soupe-jour", "plats", "la soupe du jour", "", "croquis", ""),
    ("frites", "plats", "les frites", "", "croquis", ""),
    ("oeufs-bacon", "plats", "les œufs-bacon", "", "croquis", "Le déjeuner classique : deux œufs, du bacon, des rôties, des patates rissolées."),
    ("roties", "plats", "les rôties", "le pain grillé", "croquis", f"{P} : au Québec, « des rôties » ; en France, « du pain grillé » ou « des toasts »."),
    ("pain-dore", "plats", "le pain doré", "le pain perdu", "croquis", f"{P} : au Québec, « le pain doré » ; en France, « le pain perdu »."),
    ("crepes", "plats", "les crêpes", "les pancakes", "croquis", "Au déjeuner d'ici, souvent des crêpes épaisses, avec du sirop d'érable."),
    ("tarte-sucre", "plats", "la tarte au sucre", "", "croquis", ""),
    ("pouding", "plats", "le pouding chômeur", "", "croquis", ""),

    # ── Les allergènes ─────────────────────────────────────────────────────
    ("allergie", "allergenes", "une allergie", "", "", "Toute question sur un allergène se vérifie. « Il n'y en a pas », sans vérifier, fait échouer."),
    ("alg-arachides", "allergenes", "les arachides", "les cacahuètes", "croquis", f"{P} : au Québec, « les arachides » (le beurre d'arachide) ; en France, « les cacahuètes »."),
    ("alg-noix", "allergenes", "les noix", "", "croquis", "Amandes, noix de cajou, pacanes, noisettes… Les arachides n'en sont pas."),
    ("alg-lait", "allergenes", "le lait", "les produits laitiers", "croquis", ""),
    ("alg-oeufs", "allergenes", "les œufs", "", "croquis", ""),
    ("alg-ble", "allergenes", "le blé", "le gluten", "croquis", ""),
    ("alg-poisson", "allergenes", "le poisson", "", "croquis", ""),
    ("alg-fruits-mer", "allergenes", "les fruits de mer", "les crustacés", "croquis", "Crevettes, homard, moules, pétoncles."),
    ("alg-soya", "allergenes", "le soya", "le soja", "croquis", ""),
    ("alg-sesame", "allergenes", "le sésame", "", "croquis", ""),
    ("alg-moutarde", "allergenes", "la moutarde", "", "croquis", ""),
    ("alg-sulfites", "allergenes", "les sulfites", "", "", "Liste des allergènes prioritaires de Santé Canada : à revérifier au cadrage."),

    # ── L'hygiène et la sécurité ───────────────────────────────────────────
    ("laver-mains", "hygiene", "se laver les mains", "", "", ""),
    ("gants", "hygiene", "les gants", "", "croquis", ""),
    ("filet", "hygiene", "le filet à cheveux", "la résille", "croquis", ""),
    ("tablier", "hygiene", "le tablier", "", "croquis", ""),
    ("thermometre", "hygiene", "le thermomètre", "", "croquis", ""),
    ("etiquette", "hygiene", "l'étiquette", "", "croquis", "Ce qu'il y a dans le bac, et la date où on l'a préparé."),
    ("date", "hygiene", "la date", "", "", ""),
    ("desinfectant", "hygiene", "le désinfectant", "", "croquis", ""),
    ("contamination", "hygiene", "la contamination croisée", "", "", "Le cru qui touche le cuit, le couteau du poulet sur les légumes."),
    ("zone-danger", "hygiene", "la zone de danger", "", "", "Entre 4 °C et 60 °C, les bactéries se multiplient — valeurs du MAPAQ à revérifier au cadrage."),
    ("premier-sorti", "hygiene", "premier entré, premier sorti", "", "", "Le plus vieux devant, le plus frais derrière."),
    ("chaud-derriere", "hygiene", "Chaud derrière !", "", "", "On l'annonce en passant derrière quelqu'un avec quelque chose de chaud."),
    ("derriere", "hygiene", "Derrière !", "", "", "Même chose, avec n'importe quoi : on ne recule jamais sans prévenir."),
    ("ca-glisse", "hygiene", "Attention, ça glisse !", "", "", ""),
    ("coupure", "hygiene", "une coupure", "", "", ""),
    ("brulure", "hygiene", "une brûlure", "", "", ""),
    ("premiers-soins", "hygiene", "la trousse de premiers soins", "", "croquis", ""),
    ("extincteur", "hygiene", "l'extincteur", "", "croquis", ""),

    # ── La vaisselle ───────────────────────────────────────────────────────
    ("assiette", "vaisselle", "l'assiette", "", "croquis", ""),
    ("bol-soupe", "vaisselle", "le bol", "", "croquis", ""),
    ("verre", "vaisselle", "le verre", "", "croquis", ""),
    ("tasse", "vaisselle", "la tasse", "", "croquis", ""),
    ("ustensiles-table", "vaisselle", "les ustensiles", "les couverts", "croquis", f"{P} : au Québec, « les ustensiles » (fourchette, couteau, cuillère) ; en France, « les couverts »."),
    ("fourchette", "vaisselle", "la fourchette", "", "", ""),
    ("cuillere", "vaisselle", "la cuillère", "", "", ""),
    ("plateau", "vaisselle", "le plateau", "", "croquis", ""),
    ("bac-vaisselle", "vaisselle", "le bac à vaisselle", "", "croquis", ""),
    ("napperon", "vaisselle", "le napperon", "", "croquis", ""),

    # ── La salle ───────────────────────────────────────────────────────────
    ("table", "salle", "la table", "", "", ""),
    ("banquette", "salle", "la banquette", "", "croquis", ""),
    ("menu", "salle", "le menu", "", "croquis", ""),
    ("special", "salle", "le spécial du jour", "le plat du jour", "", "Au Québec, on dit souvent « le spécial »."),
    ("entree", "salle", "l'entrée", "", "", f"{P} : ici, l'entrée ouvre le repas ; dans l'anglais des États-Unis, « entree » est le plat principal."),
    ("plat-principal", "salle", "le plat principal", "", "", ""),
    ("dessert", "salle", "le dessert", "", "", ""),
    ("breuvage", "salle", "un breuvage", "une boisson", "", f"{P} : au Québec, « un breuvage » ; en France, « une boisson »."),
    ("liqueur", "salle", "une liqueur", "une boisson gazeuse", "croquis", f"{P} : au Québec, « une liqueur » est une boisson gazeuse, sans alcool ; en France, c'est un alcool."),
    ("cafe", "salle", "un café", "", "croquis", ""),
    ("emporter", "salle", "pour emporter", "", "croquis", ""),
    ("sur-place", "salle", "pour manger ici", "sur place", "", ""),
    ("commande", "salle", "la commande", "", "", ""),
    ("addition", "salle", "l'addition", "la facture", "", f"{P} : au Québec, on demande souvent « la facture » ; en France, « l'addition »."),
    ("pourboire", "salle", "le pourboire", "le tip", "", ""),
    ("terminal", "salle", "le terminal de paiement", "la machine", "croquis", ""),
    ("extra", "salle", "un extra", "un supplément", "", f"{P} : au Québec, « un extra fromage » ; en France, « un supplément »."),
    ("a-part", "salle", "à part", "", "", "« La sauce à part » : dans un petit contenant, à côté de l'assiette."),
    ("sans", "salle", "sans", "", "", "« Sans oignons » : la modification qu'on redit au client."),
    ("couvert", "salle", "un couvert", "", "", "« Une table de quatre couverts » : quatre personnes."),

    # ── Les repas, les nombres, le temps ───────────────────────────────────
    ("dejeuner", "temps", "le déjeuner", "", "", f"{P} : au Québec, le repas du MATIN ; en France, celui du midi."),
    ("diner", "temps", "le dîner", "", "", f"{P} : au Québec, le repas du MIDI ; en France, celui du soir."),
    ("souper", "temps", "le souper", "", "", f"{P} : au Québec, le repas du SOIR ; en France, on dit « le dîner »."),
    ("table-douze", "temps", "la table douze", "", "", "Les tables ont un numéro : on les dit vite."),
    ("cinq-minutes", "temps", "dans cinq minutes", "", "", ""),
    ("rush", "temps", "le rush", "le coup de feu", "", "Le moment où tout arrive en même temps."),
    ("temperature", "temps", "la température", "", "", ""),
    ("degres", "temps", "les degrés", "", "", "« Soixante-quatorze degrés » : on les entend dans les consignes de cuisson."),
    ("douzaine", "temps", "une douzaine", "", "", ""),
    ("moitie", "temps", "la moitié", "", "", ""),
    ("portion", "temps", "une portion", "", "", ""),

    # ── Le quart de travail ────────────────────────────────────────────────
    ("horaire", "quart", "l'horaire", "", "", ""),
    ("quart", "quart", "le quart de travail", "le shift", "", ""),
    ("pis", "quart", "pis", "et puis", "", "Dans la cuisine, « pis » veut dire « et », « et puis » : « Coupe les tomates, pis lave la planche. » Dans vos phrases, dites plutôt « et »."),
    ("pause", "quart", "la pause", "", "", ""),
    ("ouverture", "quart", "l'ouverture", "", "", ""),
    ("fermeture", "quart", "la fermeture", "", "", ""),
    ("remplacer", "quart", "remplacer quelqu'un", "", "", ""),
    ("appeler-malade", "quart", "appeler malade", "", "", "Prévenir qu'on est malade et qu'on ne viendra pas."),
    ("paie", "quart", "la paie", "", "", ""),
    ("chef", "quart", "le chef", "la cheffe", "", "On lui répond « Oui, chef ! » : c'est dire qu'on a compris."),
    ("cuisinier", "quart", "le cuisinier", "la cuisinière", "", ""),
    ("plongeur", "quart", "le plongeur", "la plongeuse", "", ""),
    ("commis", "quart", "le commis", "", "", "Celui qui prépare : il coupe, il portionne, il aide sur la ligne."),
    ("serveur", "quart", "le serveur", "la serveuse", "", ""),
    ("hote", "quart", "l'hôte", "l'hôtesse", "", "La personne qui accueille et place les clients."),
    ("gerant", "quart", "le gérant", "la gérante", "", "Celui qui décide : les plaintes, les horaires, les remboursements."),
]

DESSINS = {"croquis", "decor", ""}


def par_planche():
    g = {k: [] for k, _, _ in PLANCHES}
    for e in LEXIQUE:
        g[e[1]].append(e)
    return g


def verifier():
    ids = [e[0] for e in LEXIQUE]
    doubles = {i for i in ids if ids.count(i) > 1}
    assert not doubles, f"identifiants en double : {sorted(doubles)}"
    cles = {k for k, _, _ in PLANCHES}
    for e in LEXIQUE:
        assert len(e) == 6, f"{e[0]} : six champs attendus"
        assert e[1] in cles, f"{e[0]} : planche inconnue {e[1]}"
        assert e[4] in DESSINS, f"{e[0]} : dessin inconnu {e[4]!r}"
        if e[5].startswith("PIÈGE"):
            assert len(e[5]) > 12, f"{e[0]} : un piège sans explication"
    vides = [k for k, v in par_planche().items() if not v]
    assert not vides, f"planches vides : {vides}"
    return True


if __name__ == "__main__":
    verifier()
    g = par_planche()
    for k, titre, poste in PLANCHES:
        print(f"  {titre:<36} {poste:<8} {len(g[k]):>3}")
    c = sum(1 for e in LEXIQUE if e[4] == "croquis")
    print(f"{len(LEXIQUE)} mots · {c} croquis ({c * 0.067:.2f} $) · "
          f"{sum(1 for e in LEXIQUE if e[4] == 'decor')} au décor · "
          f"{sum(1 for e in LEXIQUE if e[5].startswith('PIÈGE'))} pièges")
