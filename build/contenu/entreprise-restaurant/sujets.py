"""Ce que chaque croquis de la restauration montre — (famille, description).

Même registre que la Maison Francœur et l'hôtel (trait noir égal, aplat doux) :
la famille `objet` reprend son préambule mot pour mot. Le POSTE (le décor) est à
part : une scène 3:2, vue de la place du commis, qui servira de décor fixe aux
situations jouées en cuisine.

Étape 0 : trois témoins choisis pour leurs RISQUES, plus le décor.
  · etiquette   — un objet qui porte d'ordinaire un texte et une date ;
  · thermometre — un cadran à chiffres ;
  · poutine     — une matière difficile (sauce, fromage en grains), un plat vu en perspective.
"""

TEMOINS = ["etiquette", "thermometre", "poutine"]

SUJETS = {
    "etiquette": ("objet",
        "a clear plastic square food storage container with a lid, filled with diced carrots, "
        "with a small white rectangular label stuck on its side. On the label, only three plain "
        "grey bars where the writing would be. No letters, no numbers, no date. Seen at a "
        "three-quarter angle from slightly above."),
    "thermometre": ("objet",
        "a kitchen probe thermometer with a round dial and a long thin steel stem, lying "
        "diagonally. The dial shows only tick marks and a single red needle: no numbers, no "
        "letters, no brand."),
    "poutine": ("objet",
        "a serving of Quebec poutine in a simple round white bowl: thick golden French fries, "
        "white cheese curds in irregular small lumps, and brown gravy poured over the top, "
        "glossy. Seen at a three-quarter angle from slightly above. The bowl alone, no fork, "
        "no table, no napkin."),
}

# Le poste : vu de la place du commis sur la ligne, pour que le chef (ou le
# serveur) paraisse plus tard EN FACE, de l'autre côté du passe.
POSTE = (
    "A wide clean flat illustration in the style of a technical flat sketch, landscape format.\n"
    "LINE: crisp black ink outline of even weight, thin inner lines for details. No sketchy "
    "strokes, no hatching, no pencil texture.\n"
    "COLOUR: flat, soft, slightly muted fills — brushed stainless steel in pale cool grey, white "
    "tiles, warm light wood for the cutting board, a few muted colours in the vegetables. No "
    "gradient, no shading, no cast shadow, no 3D rendering, no photograph.\n"
    "THE SCENE: a small family restaurant kitchen seen from the cook's own standing position "
    "on the line, eye level. A stainless steel work counter runs across the lower third of the "
    "frame. On it, left to right, each object clearly separated: a wooden cutting board with a "
    "chef's knife; a row of four small steel bins holding sliced tomatoes, lettuce, onions and "
    "cheese; a flat-top griddle; a deep fryer with two wire baskets. Above the counter, the "
    "pass: a long steel shelf under two heat lamps, with a ticket rail holding three plain "
    "white paper slips (completely blank). Through the wide opening above the pass, the space "
    "directly across, in the middle, is EMPTY: a person will stand there later. On the left "
    "edge, the dish pit: a deep steel sink with a spray nozzle and a rack of plates. On the "
    "back wall, a range hood.\n"
    "NOTHING ELSE: no person, no hands, no text, no letters, no numbers, no logo, no sign, no "
    "brand name anywhere, nothing written on the slips. No frame, no border.")


# ── Étape 1 : les 108 autres croquis (lancés le 30 sept. 2026, avant la visite
# en cuisine, à la demande de Daniel ; on ajustera après). La famille « geste »
# montre deux mains seules, sans visage : le préambule « objet » sans la phrase
# qui exclut les mains. Tout ce qui porte d'ordinaire un texte (bouteille, menu,
# terminal) est décrit SANS étiquette ni chiffre.
_NU = "No label, no letters, no numbers, no brand. "
SUJETS.update({
    # Le poste de cuisine
    "lave-vaisselle": ("objet", "a commercial stainless steel dishwasher of the hood type, lid raised, with a plastic rack of white plates inside. " + _NU),
    "chambre-froide": ("objet", "the heavy stainless steel door of a walk-in cooler, slightly open, a long vertical handle, a thin strip of cold white mist at the bottom edge, shelves with boxes visible inside. " + _NU),
    "congelateur": ("objet", "a white chest freezer, lid open, frost inside and a few wrapped packages. " + _NU),
    "frigo": ("objet", "an upright commercial stainless steel refrigerator with two glass doors, shelves inside holding containers and vegetables. " + _NU),
    "friteuse": ("objet", "a commercial deep fryer in stainless steel with two wire baskets hanging above golden oil, seen from the front at a slight angle. " + _NU),
    "plaque": ("objet", "a commercial flat-top griddle: a wide flat dark steel cooking plate on a stainless steel base, with three burger patties cooking on it and a grease trough at the front. No knob markings. " + _NU),
    "four": ("objet", "a commercial stainless steel convection oven, door closed with a small window showing a tray inside; knobs with no markings. " + _NU),
    "poele-appareil": ("objet", "a commercial kitchen range: six gas burners with black grates on top and an oven below, stainless steel. Knobs with no markings. " + _NU),
    "hotte": ("objet", "a large stainless steel kitchen range hood with metal grease filters, seen from below at a slight angle, alone. " + _NU),
    "evier": ("objet", "a deep double stainless steel kitchen sink with a tall pre-rinse spray faucet on a spring. " + _NU),
    "lavabo": ("objet", "a small wall-mounted stainless steel hand-washing sink with a faucet, a soap dispenser and a paper towel dispenser on the wall above it. " + _NU),
    "poubelle": ("objet", "a large grey plastic kitchen garbage bin on wheels with a black bag inside and the lid open. " + _NU),
    # Les ustensiles
    "couteau-chef": ("objet", "a chef's knife with a wide stainless steel blade and a black handle, lying diagonally. " + _NU),
    "planche": ("objet", "a thick rectangular plastic cutting board in green, seen at a three-quarter angle from above, empty. " + _NU),
    "bol": ("objet", "a round-bottomed stainless steel mixing bowl, empty, seen at a three-quarter angle from above. " + _NU),
    "fouet": ("objet", "a balloon whisk with thin steel wires and a steel handle, lying diagonally. " + _NU),
    "louche": ("objet", "a stainless steel ladle with a deep round bowl and a long handle, lying diagonally. " + _NU),
    "pince": ("objet", "a pair of stainless steel kitchen tongs with scalloped tips, lying diagonally. " + _NU),
    "spatule": ("objet", "a wide flat metal griddle spatula (turner) with a wooden handle, lying diagonally. " + _NU),
    "poele": ("objet", "a black frying pan with a long handle, empty, seen at a three-quarter angle from above. " + _NU),
    "chaudron": ("objet", "a tall stainless steel stock pot with two side handles and a lid, seen from the front at a slight angle. " + _NU),
    "bac": ("objet", "a rectangular stainless steel hotel pan (steam table pan) filled with sliced red tomatoes, seen at a three-quarter angle from above. " + _NU),
    "passoire": ("objet", "a stainless steel colander full of small holes, with two handles, empty. " + _NU),
    "rape": ("objet", "a four-sided stainless steel box grater standing upright, with a handle on top. " + _NU),
    "eplucheur": ("objet", "a vegetable peeler with a swivel blade and a black handle, lying diagonally. " + _NU),
    "tasse-mesurer": ("objet", "a clear glass measuring cup with a spout and a handle, with plain lines on the side and no numbers, half full of water. " + _NU),
    # Préparer : les gestes
    "eplucher": ("geste", "two hands peeling a carrot with a vegetable peeler over a green cutting board; a few orange peel strips fall on the board."),
    "trancher": ("geste", "two hands slicing a tomato into even round slices with a chef's knife on a cutting board; the slices fan out beside it."),
    "en-des": ("geste", "a chef's knife and a neat pile of small even cubes of carrot on a cutting board, one hand holding the knife beside the cubes."),
    "hacher": ("geste", "a hand holding a chef's knife, rocking it over a small pile of finely chopped fresh parsley on a cutting board."),
    "emincer": ("geste", "two hands cutting an onion into very thin half-moon slices with a chef's knife on a cutting board."),
    "julienne": ("geste", "a chef's knife beside a neat bundle of long thin matchstick strips of carrot and green pepper on a cutting board, one hand holding the knife."),
    # Cuire : la cuisson de la viande, en coupe
    "saignant": ("objet", "a thick steak cut in half, seen from the side so the inside shows: a brown seared crust and a wide bright RED centre. On a white plate. " + _NU),
    "a-point": ("objet", "a thick steak cut in half, seen from the side so the inside shows: a brown seared crust and a PINK centre. On a white plate. " + _NU),
    "bien-cuit": ("objet", "a thick steak cut in half, seen from the side so the inside shows: brown all the way through, no pink at all. On a white plate. " + _NU),
    # Les aliments
    "boeuf-hache": ("objet", "a mound of raw red ground beef on a sheet of white butcher paper. " + _NU),
    "poulet": ("objet", "a whole raw chicken, pale pink, on a white plate. " + _NU),
    "jambon": ("objet", "a piece of ham with a few pink slices cut and laid beside it. " + _NU),
    "bacon": ("objet", "four strips of cooked bacon laid side by side. " + _NU),
    "saucisse": ("objet", "three grilled pork sausages side by side. " + _NU),
    "poisson": ("objet", "a whole raw fish with silver scales, lying on its side. " + _NU),
    "oeufs": ("objet", "six brown eggs in an open cardboard egg carton. " + _NU),
    "fromage": ("objet", "a wedge of orange cheddar cheese with two slices cut beside it. " + _NU),
    "fromage-grains": ("objet", "a small pile of fresh white cheese curds: irregular squeaky lumps, some elongated, in a small clear bag opened at the top. " + _NU),
    "lait": ("objet", "a white milk carton with a gable top and a glass of milk beside it. " + _NU),
    "creme": ("objet", "a small white cream pitcher pouring a thick white cream into a small bowl. " + _NU),
    "beurre": ("objet", "a rectangular block of yellow butter on a small plate, one pat cut off, with a butter knife. " + _NU),
    "pain": ("objet", "a sliced loaf of white sandwich bread with a few slices fanned out in front. " + _NU),
    "pates": ("objet", "a small heap of dry uncooked spaghetti and a handful of dry penne pasta beside it. " + _NU),
    "riz": ("objet", "a white bowl filled with cooked white rice. " + _NU),
    "patates": ("objet", "four whole raw brown potatoes, one cut in half showing the pale yellow inside. " + _NU),
    "oignon": ("objet", "a whole yellow onion with dry golden skin, and a half onion showing its rings. " + _NU),
    "tomate": ("objet", "a whole red tomato with its green stem, and a half tomato beside it. " + _NU),
    "laitue": ("objet", "a head of green leaf lettuce with loose, ruffled, wavy bright green leaves opening outward, and two separate leaves beside it. Clearly lettuce, not a cabbage. " + _NU),
    "carotte": ("objet", "three whole orange carrots with their green leafy tops. " + _NU),
    "champignon": ("objet", "three white button mushrooms, one cut in half. " + _NU),
    "poivron": ("objet", "three bell peppers side by side: one green, one red, one yellow. " + _NU),
    "ble-inde": ("objet", "one ear of yellow corn with its green husk pulled back, and a small pile of loose yellow corn kernels beside it. " + _NU),
    "feves": ("objet", "a small brown clay bean pot filled with Quebec baked beans in a thick brown sauce. " + _NU),
    "bleuets": ("objet", "a small pint basket full of blueberries, dark blue with a pale bloom. " + _NU),
    "pomme": ("objet", "a red apple with a small green leaf on its stem. " + _NU),
    "citron": ("objet", "a yellow lemon and a lemon half beside it. " + _NU),
    "farine": ("objet", "an open paper sack of white flour with a small scoop of flour in front of it. The sack is plain white. " + _NU),
    "sel-poivre": ("objet", "a pair of salt and pepper shakers: a glass one with white salt and a glass one with black pepper, side by side. " + _NU),
    "huile": ("objet", "a clear glass bottle of golden vegetable oil with a pour spout, and a small puddle of oil in a spoon beside it. " + _NU),
    "sirop-erable": ("objet", "a small glass jug of amber maple syrup with a round handle near the neck. " + _NU),
    # Les plats
    "pate-chinois": ("objet", "a square portion of Quebec shepherd's pie (pâté chinois) on a white plate, seen from the side so the three layers show: brown ground beef at the bottom, yellow corn in the middle, mashed potatoes on top, lightly browned. " + _NU),
    "club": ("objet", "a club sandwich cut into four triangles held with toothpicks, showing layers of toasted bread, chicken, bacon, lettuce and tomato, with a few French fries on the white plate. " + _NU),
    "hamburger": ("objet", "a hamburger in a sesame bun with a beef patty, cheese, lettuce, tomato and onion, on a white plate. " + _NU),
    "hot-chicken": ("objet", "a Quebec hot chicken sandwich on a white plate: sliced white bread with chicken between, covered with brown gravy, green peas on the side. " + _NU),
    "soupe-jour": ("objet", "a white bowl of vegetable soup with pieces of carrot and celery, a spoon beside it on a small saucer. " + _NU),
    "frites": ("objet", "a paper-lined basket of thick golden French fries. " + _NU),
    "oeufs-bacon": ("objet", "a breakfast plate: two sunny-side-up eggs, three strips of bacon, two slices of toast and home fries (small browned potato cubes). " + _NU),
    "roties": ("objet", "two slices of golden toast on a small white plate with a pat of butter. " + _NU),
    "pain-dore": ("objet", "three slices of French toast, golden brown, on a white plate with a dusting of sugar and a few berries. " + _NU),
    "crepes": ("objet", "a stack of three thick fluffy pancakes on a white plate with maple syrup running down the sides and a pat of butter on top. " + _NU),
    "tarte-sucre": ("objet", "a slice of Quebec sugar pie on a white plate: a golden crust and a smooth caramel-brown filling. " + _NU),
    "pouding": ("objet", "a portion of pouding chômeur in a small white ramekin: a golden cake on top of a glossy caramel syrup. " + _NU),
    # Les allergènes : l'aliment reconnaissable, rien d'autre
    "alg-arachides": ("objet", "a small pile of peanuts: some in their tan shells, some shelled, and a small jar of peanut butter. " + _NU),
    "alg-noix": ("objet", "a small mix of tree nuts: almonds, cashews, pecans and hazelnuts, grouped together. No peanuts. " + _NU),
    "alg-lait": ("objet", "a group of dairy products: a milk carton, a wedge of cheese, a small block of butter and a small cup of yogurt. " + _NU),
    "alg-oeufs": ("objet", "two whole brown eggs and one cracked egg with the yolk in a small bowl. " + _NU),
    "alg-ble": ("objet", "a sheaf of golden wheat stalks with a small loaf of bread beside it. " + _NU),
    "alg-poisson": ("objet", "a fillet of salmon and a small whole fish side by side. " + _NU),
    "alg-fruits-mer": ("objet", "a red cooked lobster, a few pink shrimp, two black mussels and a scallop, grouped together. " + _NU),
    "alg-soya": ("objet", "a green soybean pod opened to show the beans, a block of white tofu and a small dish of dark soy sauce. " + _NU),
    "alg-sesame": ("objet", "a small white dish of pale sesame seeds and a sesame-covered bun beside it. " + _NU),
    "alg-moutarde": ("objet", "a small white ramekin of yellow mustard with a spoon, and a few mustard seeds beside it. " + _NU),
    # L'hygiène et la sécurité
    "gants": ("objet", "a pair of disposable blue nitrile gloves, one lying flat, one half out of an open plain box. " + _NU),
    "filet": ("objet", "a fine black hair net, lying flat and spread out. " + _NU),
    "tablier": ("objet", "a long white bib apron with neck strap and waist ties, lying flat. " + _NU),
    "desinfectant": ("objet", "a plain white spray bottle with a trigger nozzle and a folded blue cloth beside it. " + _NU),
    "premiers-soins": ("objet", "a white plastic first aid box with a simple green cross symbol on the lid, lid open showing bandages and gauze. No letters, no numbers, no brand. "),
    "extincteur": ("objet", "a red fire extinguisher with a black hose and a pressure gauge showing only a needle and a coloured arc, no numbers. " + _NU),
    # La vaisselle
    "assiette": ("objet", "a round white dinner plate, empty, seen at a three-quarter angle from above. " + _NU),
    "bol-soupe": ("objet", "a white soup bowl, empty, seen at a three-quarter angle from above. " + _NU),
    "verre": ("objet", "a clear drinking glass of water. " + _NU),
    "tasse": ("objet", "a white coffee mug on a small saucer, empty. " + _NU),
    "ustensiles-table": ("objet", "a set of table cutlery side by side: a fork, a knife and a spoon, in stainless steel. " + _NU),
    "plateau": ("objet", "a round brown non-slip serving tray, empty, seen at a three-quarter angle from above. " + _NU),
    "bac-vaisselle": ("objet", "a grey plastic bus tub full of dirty plates, cups and cutlery. " + _NU),
    "napperon": ("objet", "a rectangular paper placemat, plain white with a simple scalloped border, lying flat, with a fork and knife on it. " + _NU),
    # La salle
    "banquette": ("objet", "a restaurant booth: two facing padded red vinyl bench seats and a small table between them, seen from the side. " + _NU),
    "menu": ("objet", "a closed restaurant menu in a dark red folder cover, standing slightly open. Inside only plain grey bars where the writing would be. " + _NU),
    "liqueur": ("objet", "a glass of dark fizzy soft drink with ice cubes, bubbles rising, and a straw. No bottle, no can. " + _NU),
    "cafe": ("objet", "a white mug of black coffee with a small wisp of steam, on a saucer. " + _NU),
    "emporter": ("objet", "a brown paper take-out bag, folded closed at the top, next to a closed white take-out food container and a paper cup with a lid. " + _NU),
    "terminal": ("objet", "a handheld card payment terminal: a small black device with a BLANK grey screen and a keypad of plain round buttons with no numbers and no symbols. " + _NU),
})

# Audit de l'étape 2, tour 2 : les cuissons se prennent sur un steak.
SUJETS["steak"] = ("objet", "a whole grilled beef steak with dark grill marks on a white plate, seen at a three-quarter angle from slightly above, alone. No knife, no fork. No label, no letters, no numbers, no brand. ")
