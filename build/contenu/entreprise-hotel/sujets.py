"""Ce que chaque croquis de la réception montre — (famille, description).

Même registre que la Maison Francœur (trait noir égal, aplat doux) : la
famille `objet` reprend son préambule mot pour mot. Le comptoir est à part :
une scène large, 3:2, qui servira de décor fixe au jeu de rôle.
"""

SUJETS = {
    "carte-cle": ("objet",
        "a plain white plastic hotel key card, the size of a credit card, lying on a small folded "
        "paper sleeve in soft teal. The card is completely blank on both visible faces; the sleeve "
        "is blank too. Seen from slightly above at a three-quarter angle."),
    "lit-queen": ("objet",
        "a queen-size hotel bed seen at a three-quarter angle from the foot: a simple upholstered "
        "headboard in soft grey-blue, white sheets and duvet neatly made, two white pillows side by "
        "side, a folded accent runner in muted teal across the foot of the bed. The bed alone, no "
        "night table, no lamp, no wall."),
    "sonnette": ("objet",
        "a classic chrome hotel desk bell (a dome bell with a small push button on top) on a round "
        "dark-wood base. Seen from the front at a slight angle."),
}

# Le comptoir : la pièce maîtresse (volet 2). Vu de DERRIÈRE — de la place de
# l'employé — pour que le client, plus tard, apparaisse EN FACE, de l'autre
# côté. Tout ce que le lexique range sous « comptoir » doit y être désignable.
COMPTOIR = (
    "A wide clean flat illustration in the style of a technical flat sketch, landscape format.\n"
    "LINE: crisp black ink outline of even weight, thin inner lines for details. No sketchy "
    "strokes, no hatching, no pencil texture.\n"
    "COLOUR: flat, soft, slightly muted fills — warm light wood for the counter, pale warm grey "
    "walls, muted teal accents. No gradient, no shading, no cast shadow, no 3D rendering, no "
    "photograph.\n"
    "THE SCENE: a hotel reception desk seen from BEHIND the counter, from the receptionist's own "
    "standing position, eye level. The counter top runs across the whole lower third of the "
    "frame. On the counter, left to right, each object clearly separated from the others: a "
    "computer monitor with its keyboard (the screen is a plain pale blue, blank); a small "
    "receipt printer; a card payment terminal; a key card encoder with three blank white key "
    "cards beside it; a desk telephone with a coiled cord; a closed cash drawer under the "
    "counter edge; a chrome desk bell on the customer side of the counter; a plain folder. "
    "Beyond the counter, the empty hotel lobby: a floor of large pale tiles, a brochure rack "
    "standing to one side with folded leaflets (blank), a folded city map on the counter corner, "
    "the glass entrance doors in the far background. On the right wall, a closed wooden door "
    "(the manager's office). On a pillar, a row of three round wall clocks with hands and tick "
    "marks only. The space directly across the counter, in the middle, is EMPTY: a guest will "
    "stand there later.\n"
    "NOTHING ELSE: no person, no hands, no text, no letters, no numbers, no numerals on the "
    "clocks, no logo, no sign, no brand name anywhere. No frame, no border.")

# ── Le reste du lexique (étape 1, 25 sept. 2026) ──
# Tout objet qui PORTE d'ordinaire un texte ou un chiffre (passeport, carte,
# reçu, billet, clavier) est décrit avec ses zones écrites en BARRES GRISES
# ou en boutons VIERGES : une négation ne suffit pas, un cadrage si.
_O = "objet"
SUJETS.update({
    "piece-identite": (_O, "a plastic photo identity card lying flat, seen from slightly above: a small grey head-and-shoulders silhouette on the left, and on the right three plain grey bars where text would be. No letters, no numbers."),
    "passeport": (_O, "a closed passport booklet, plain dark navy-blue cover with a simple round embossed gold emblem in the middle, seen from slightly above at a three-quarter angle. No lettering anywhere on the cover."),
    "permis": (_O, "a driver's licence card lying flat, pale blue: a small grey head silhouette on the left, a tiny drawing of a car in the corner, plain grey bars where text would be. No letters, no numbers."),
    "carte-credit": (_O, "a credit card lying flat at a slight angle, deep blue with a gold chip and a subtle wave pattern. No numbers, no name, no logo."),
    "pochette": (_O, "a small folded paper key card sleeve in soft teal, closed and EMPTY, seen from slightly above. One short plain grey bar where the room number would be written. No numbers, no letters."),
    "fiche": (_O, "a hotel registration card on a small clipboard: printed form lines drawn as plain grey bars and empty boxes, a signature line at the bottom. No letters, no numbers."),
    "stylo": (_O, "a simple ballpoint pen lying diagonally, white body with a teal clip."),
    "bagages": (_O, "a group of travel luggage standing together: one large rolling suitcase, one smaller carry-on, and a soft duffel bag, in muted teal, grey and brown."),
    "valise": (_O, "one hard-shell rolling suitcase, standing upright, handle extended, muted teal, seen at a three-quarter angle."),
    "chariot": (_O, "a classic brass hotel luggage cart with a red carpeted base and a curved top rail, with two suitcases on it, seen at a three-quarter angle."),
    "lit-simple": (_O, "a narrow single bed (twin) seen at a three-quarter angle from the foot: simple grey-blue headboard, white sheets, ONE white pillow. The bed alone, no night table, no wall."),
    "lit-double": (_O, "a medium-width double bed seen at a three-quarter angle from the foot: simple grey-blue headboard, white duvet, two white pillows touching. The bed alone, no night table, no wall."),
    "lit-king": (_O, "a VERY WIDE king-size bed seen at a three-quarter angle from the foot: long low grey-blue headboard, white duvet, FOUR white pillows in two rows. The bed alone, no night table, no wall."),
    "lit-appoint": (_O, "a folding rollaway guest bed on small wheels, thin mattress with a white sheet and one pillow, metal frame visible, seen at a three-quarter angle."),
    "berceau": (_O, "a baby crib with vertical wooden slats and a small white mattress, seen at a three-quarter angle."),
    "ascenseur": (_O, "a pair of closed brushed-steel elevator doors set in a pale wall, with a small panel of two call buttons marked only by an up triangle and a down triangle. No numbers, no letters."),
    "sortie": (_O, "an emergency exit sign: a green rectangular box showing only the white pictogram of a running figure going through a doorway, with an arrow. No letters."),
    "escalier": (_O, "a short straight flight of stairs with a handrail, seen from the side at a three-quarter angle, pale grey steps."),
    "climatiseur": (_O, "a white wall-mounted air conditioning unit with horizontal vents, a small blank remote beside it. No display digits."),
    "coffre-fort": (_O, "a small in-room hotel safe, dark grey steel box with its door closed and a keypad of BLANK square buttons and a blank small display."),
    "minibar": (_O, "a small hotel minibar fridge with its door open, a few small bottles and cans inside with plain unlabelled shapes."),
    "serviettes": (_O, "a neat stack of three folded white bath towels with a small folded hand towel on top."),
    "oreiller": (_O, "one plump white bed pillow, seen at a slight angle."),
    "couverture": (_O, "a folded soft wool blanket in muted teal, laid flat, with a visible fringe edge."),
    "sechoir": (_O, "a handheld hair dryer, white with a grey nozzle, with its coiled cord."),
    "fer": (_O, "a steam iron standing on its heel, white and teal, seen from the side."),
    "telecommande": (_O, "a TV remote control lying diagonally, dark grey with round BLANK buttons, no symbols, no numbers."),
    "douche": (_O, "a shower corner: a chrome shower head on the wall with water drops falling, and a half-open white shower curtain on a rod."),
    "bain": (_O, "a white freestanding bathtub with a chrome faucet, seen at a three-quarter angle."),
    "dejeuner": (_O, "a breakfast tray seen from slightly above: a cup of coffee, a glass of orange juice, a croissant, a small bowl of fruit, cutlery on a napkin."),
    "stationnement": (_O, "a small car parked in a parking space marked by white painted lines on grey asphalt, seen from above at a slight angle. No sign, no letters."),
    "piscine": (_O, "an indoor swimming pool corner: blue water with a chrome ladder and a few pale tiles around the edge."),
    "gym": (_O, "a treadmill with a small rack of dumbbells beside it, seen at a three-quarter angle. Blank control panel, no display digits."),
    "navette": (_O, "a white minibus shuttle van seen from the side at a slight angle, windows tinted pale blue. No writing on the van."),
    "glace": (_O, "a hotel ice machine: a stainless steel cabinet with a small ice bucket sitting on top, full of ice cubes. No labels."),
    "distributrice": (_O, "a vending machine seen from the front at a slight angle: a glass front with rows of plain coloured snack packets and bottles without labels, a blank button panel."),
    "recu": (_O, "a paper receipt, slightly curled, printed lines drawn as plain grey bars of different lengths. No letters, no numbers."),
    "comptant": (_O, "a small fan of generic banknotes in muted green and brown, with abstract wavy patterns only, and a few coins beside them. No numbers, no portraits, no letters."),
    "fuite": (_O, "a water pipe under a bathroom sink, with a leak: water drops falling from a joint into a small puddle on the floor."),
    "ampoule": (_O, "a burned-out light bulb: a clear glass bulb gone greyish inside, with a visibly broken filament, lying on its side."),
    "pharmacie": (_O, "a small pharmacy storefront seen from the front: a glass door, a window with a few shelves of bottles, and above it a sign that is only a green cross. No letters."),
    "plage": (_O, "a small stretch of sandy beach with a striped beach umbrella, a folded towel and gentle blue waves behind."),
    "musee": (_O, "a classical museum building seen from the front: steps, a row of columns, a triangular pediment. No inscription."),
    "restaurant": (_O, "a restaurant table set for two seen from slightly above: white tablecloth, two plates, glasses, cutlery, a small vase with a flower."),
    "billet": (_O, "two admission tickets with a perforated stub edge, pale yellow, printed zones drawn as plain grey bars. No letters, no numbers."),
    "autobus": (_O, "a city bus seen from the side at a slight angle, white and teal. No route number, no writing, blank destination panel."),
    "metro": (_O, "a subway train car stopped at a platform, seen from the side, doors open. No writing, no line number."),
    "taxi": (_O, "a yellow taxi car seen from the side at a slight angle, with a blank roof light. No writing, no number."),
    "aeroport": (_O, "an airport scene reduced to two objects: a passenger airplane on the ground and a control tower behind it. No writing, no airline logo."),
})
SUJETS["bagagiste"] = ("personne",
    "a hotel bellhop in a burgundy uniform and a small pillbox cap, standing beside a brass luggage cart loaded with suitcases, full body, seen at a three-quarter angle. Simple calm face drawn with a few lines.")

TEMOINS = ["carte-cle", "lit-queen", "sonnette"]
