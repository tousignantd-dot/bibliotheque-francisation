"""Ce que montre chaque croquis d'« Une semaine à Toronto » — (famille, description).

Familles, comme à Compostelle (build/contenu/compostelle/sujets.py) :
- `objet` : le préambule OBJET de Francœur (trait noir égal, un aplat doux, fond
  blanc), importé par build/toronto_croquis.py, jamais recopié ;
- `scene` : une petite vignette de carnet, pour les lieux et le temps qu'il fait ;
- `corps` : une silhouette neutre, la partie nommée en couleur (les maux) ;
- `geste` : une ou deux personnes, le geste lisible (ce qu'on fait).

On décrit la FORME, jamais le mot. Tout ce qui porte d'ordinaire un texte (billet,
carte, menu, terminal, panneau de sortie, enseigne) est décrit SANS sa face
écrite, et aucune marque ni enseigne n'entre dans l'image (aucune chaîne de café,
aucun logo de la société de transport).
"""

CORPS = (
    "A clean flat illustration in the style of a medical diagram for beginners: a neutral human "
    "body part or figure drawn in crisp black ink outline, filled in ONE flat very pale grey, "
    "EXCEPT the part named below, filled in flat coral red. Centred, filling about 70 % of a "
    "square frame, on a pure white background. No face details, no gradient, no shadow, no "
    "photograph. No text, no letters, no arrows, no labels. No frame, no border.\n\n"
    "THE DRAWING: ")
SCENE = (
    "A small travel-sketchbook vignette in ink and light wash: crisp black ink line of even "
    "weight, a few flat, soft, slightly muted colour fills, centred in a square frame, the scene "
    "fading softly into a pure white background at its edges. A flat scan of the drawing, not a "
    "photograph of a sketchbook: no page edge, no paper shadow, no grey or beige paper tone: the "
    "background around the scene is PURE WHITE. No people in close-up. No text, no letters, no "
    "numbers, no signs, no logo, no brand. No frame, no border.\n\n"
    "THE SCENE: ")
GESTE = (
    "A small travel-sketchbook vignette in ink and light wash: one or two people shown full-length or "
    "from the waist up, their gesture and expression clearly readable, in a simple setting in a big "
    "Canadian city; crisp black ink line of even weight, a few flat, soft, slightly muted colour "
    "fills, centred in a square frame, fading softly into a pure white background at its edges. A flat "
    "scan of the drawing, not a photograph of a sketchbook, no grey or beige paper tone: the background "
    "is PURE WHITE. No speech bubbles, no text, no letters, no numbers, no signs, no logo. No frame, "
    "no border.\n\n"
    "THE SCENE: ")

SUJETS = {
    # --- Arriver et se déplacer
    "station": ("scene", "a grand old railway station hall: tall stone columns, a high coffered ceiling, big arched windows, a few small travellers with suitcases far away; no departure board, no signs."),
    "platform": ("scene", "an underground subway platform seen along its length: the platform edge with a yellow tactile strip, the track bed below, a curved tiled wall; no signs, no station name."),
    "subway": ("objet", "a modern subway train car seen from the side at a slight angle, silver with a thin red stripe, doors closed; no route number, no letters, no logo."),
    "streetcar": ("objet", "A modern red-and-white city streetcar (tram) seen in three-quarter view from the front, on rails in the street, with a pantograph on the roof. The destination sign above the windscreen is a plain dark blank band, no route number, no letters, no logo anywhere on the body."),
    "bus": ("objet", "a city bus seen in three-quarter view from the front, red and white, the destination sign a plain dark blank band; no route number, no letters, no logo."),
    "bus_stop": ("scene", "a simple glass bus shelter on a city sidewalk with a bench inside and a plain pole beside it topped by a blank coloured square plate; no letters, no numbers."),
    "transit_card": ("objet", "a plain contactless transit card, green, with only a small wave symbol in one corner; nothing written on it."),
    "tap": ("geste", "a person touching a contactless card to a round card reader on a pole at a subway turnstile; the reader shows a plain green light, no screen text."),
    "ferry": ("scene", "a small white passenger ferry crossing calm blue water, a low green island behind it; no name on the hull."),
    "taxi": ("objet", "a city taxi car seen in three-quarter view, with a small plain roof light; no letters, no number, no logo on the doors or roof light."),
    "exit": ("scene", "an open doorway at the top of a few steps leading out to bright daylight, above it a small green pictogram of a running figure and an arrow; no letters."),
    "entrance": ("scene", "the glass double doors of a building seen from the sidewalk, one door held open, a doormat; no sign, no letters."),
    "corner": ("scene", "a city street corner seen from above at an angle: two sidewalks meeting, a pedestrian crossing painted in white stripes, a traffic light pole on the corner; no street signs."),
    "underground": ("scene", "a bright underground pedestrian corridor between office towers: a long tiled passage with shops' glass fronts on both sides, a few small walkers; no signs, no shop names."),
    # --- L'hôtel
    "front_desk": ("scene", "a hotel front desk seen from the guest's side: a wooden counter with a small bell and a closed laptop, a key-card holder, plants; nobody behind it; no sign."),
    "room": ("scene", "a tidy hotel room seen from the door: one bed with white sheets, a lamp, a window with curtains, a small desk."),
    "double_bed": ("objet", "one large double bed with white sheets and two pillows, seen at a slight angle from the foot."),
    "two_beds": ("objet", "two separate double beds side by side with a small night table between them, seen from the foot."),
    "key_card": ("objet", "a plain white hotel key card in a small paper sleeve; nothing written on either."),
    "wifi": ("objet", "a small white wireless router with two antennas and a few small green lights on its front; no letters, no logo."),
    "towel": ("objet", "a neatly folded stack of two white bath towels."),
    "elevator": ("scene", "two closed brushed-steel elevator doors in a hotel corridor with a single call button panel between them; no floor numbers, no letters."),
    "lobby": ("scene", "a hotel lobby: armchairs, a low table, a large plant, a chandelier, the front desk far in the background; no signs."),
    "luggage": ("objet", "a rolling suitcase standing upright with its handle extended and a smaller travel bag beside it; no tags with text."),
    # --- Le café
    "coffee": ("objet", "a paper coffee cup with a plastic lid and a corrugated sleeve, steam rising; plain, no logo, nothing written."),
    "small": ("objet", "three plain paper coffee cups side by side of increasing size, the SMALLEST one coloured in soft orange and the other two in pale grey outline only; no letters."),
    "medium": ("objet", "three plain paper coffee cups side by side of increasing size, the MIDDLE one coloured in soft orange and the other two in pale grey outline only; no letters."),
    "large": ("objet", "three plain paper coffee cups side by side of increasing size, the LARGEST one coloured in soft orange and the other two in pale grey outline only; no letters."),
    "milk": ("objet", "a small glass jug of milk next to a white mug."),
    "cream": ("objet", "a few small sealed single-serve cream cups in a little dish; no printing on the lids."),
    "sugar": ("objet", "a small bowl of sugar cubes and two paper sugar sticks beside it; no printing."),
    "to_go": ("objet", "a paper bag with folded top and a paper coffee cup in a cardboard cup holder beside it, ready to carry away; no logo."),
    "tea": ("objet", "a white mug of tea with the string and plain tag of a tea bag hanging over the rim; nothing written on the tag."),
    "muffin": ("objet", "a blueberry muffin in a paper liner."),
    "bagel": ("objet", "a sesame bagel cut in half, one half spread with cream cheese."),
    "straw": ("objet", "a tall glass of iced drink with a paper straw."),
    "water": ("objet", "a clear glass of water with a few ice cubes."),
    "receipt": ("objet", "a small curled paper till receipt seen at an angle, covered only with thin grey horizontal lines instead of text; no letters, no numbers."),
    # --- Le restaurant
    "table_for_two": ("scene", "a small restaurant table set for two people: two chairs, two plates, glasses, a candle; no people."),
    "menu": ("objet", "a closed restaurant menu with a plain dark leather cover, standing slightly open; the visible inside pages show only thin grey lines, no letters."),
    "appetizer": ("objet", "a small plate with a starter: a few crispy spring rolls and a little bowl of dipping sauce."),
    "main": ("objet", "a large dinner plate with a main course: a grilled steak, roasted potatoes and green beans."),
    "dessert": ("objet", "a slice of chocolate cake on a small plate with a fork."),
    "tap_water": ("objet", "a clear glass carafe of water and a glass beside it, no bottle, no label."),
    "rare": ("objet", "three slices of steak side by side seen in cross-section: the first deep red inside, the second pink, the third brown all through."),
    "broth": ("objet", "two small bowls of clear soup side by side: one golden chicken broth with a few pieces of chicken, one green vegetable broth with carrots and celery."),
    "server": ("geste", "a restaurant server in a black apron holding a small notepad, standing at a table and smiling, ready to take an order."),
    "the_bill": ("objet", "a small black folder for the restaurant bill, open, holding a paper slip covered with grey lines only, a pen beside it; no letters, no numbers."),
    "leftovers": ("objet", "a closed white take-away box next to a plate with a little food left on it."),
    "napkin": ("objet", "a folded cloth napkin with a fork and knife on top."),
    "fork": ("objet", "a single metal fork."),
    "knife": ("objet", "a single table knife."),
    "spoon": ("objet", "a single metal spoon."),
    "peameal": ("objet", "A peameal bacon sandwich on a plate: a soft round kaiser bun stuffed with a thick stack of thin slices of pink back bacon whose edges are rolled in yellow cornmeal, a little mustard showing, cut in half so the stacked slices show."),
    # --- Payer
    "cash": ("objet", "a few coins and folded paper banknotes on a table, the banknotes seen edge-on so no printing is visible."),
    "card": ("objet", "two plain payment cards fanned out, one blue and one grey, each with only a small chip; no numbers, no names, no logo."),
    "terminal": ("objet", "A handheld card payment terminal held upright on its own, as if offered across a counter: a small dark device with a keypad of blank rounded keys and a small screen that is plain light grey and EMPTY (no numbers, no percentages, no letters), a contactless wave area at the top. No hand."),
    "bag": ("objet", "a reusable cloth shopping bag with handles, a baguette and some fruit sticking out; no logo."),
    # --- Visiter
    "ticket": ("objet", "a plain paper admission ticket with a perforated stub, pale yellow; nothing printed on it."),
    "guided_tour": ("geste", "a guide holding up a closed umbrella, leading a small group of tourists who look up at a building."),
    "audio_guide": ("objet", "a small handheld audio guide device with a speaker grille and a strap, and a pair of headphones; blank keys, no screen text."),
    "coat_check": ("scene", "a cloakroom counter with coats on hangers on a rail behind it and a small numbered-looking tag that is blank; no letters, no numbers."),
    "gift_shop": ("scene", "a small museum gift shop: shelves with mugs, postcards turned face down, small toys; no signs, no prices."),
    "museum": ("scene", "the front of a large museum: an old stone building with a huge modern angular glass-and-steel extension jutting out over the entrance; no signs."),
    "gallery": ("scene", "a bright art gallery room: a few framed paintings of landscapes on white walls, a bench in the middle, one small visitor looking."),
    "tower": ("scene", "a very tall slender concrete observation tower with a round pod near the top and a thin antenna, rising above a city skyline by a lake."),
    "market": ("scene", "the inside of a big old covered market hall: stalls of fruit, bread and cheese under a high roof with arched windows; no signs, no prices."),
    "island": ("scene", "a small green island with trees and a sandy shore in a lake, seen from a boat; no buildings with signs."),
    "lake": ("scene", "a wide calm lake reaching the horizon, a few sailboats, a pale sky."),
    "view": ("scene", "a city skyline with many towers and one very tall slender observation tower, seen across the water from an island park at sunset."),
    "line": ("scene", "a short queue of five people waiting one behind the other in front of a ticket window, seen from the side."),
    "bike": ("objet", "a city rental bicycle with a basket on the front, standing on its kickstand; no logo."),
    "game": ("scene", "a baseball stadium seen from the stands: the green field, the diamond, players far away, a crowd; no scoreboard text."),
    "neighbourhood": ("scene", "a lively city neighbourhood street: colourful low brick houses with shops at street level, trees, a few walkers and a bicycle; no shop signs, no letters."),
    # --- Magasiner
    "fitting_room": ("scene", "a row of shop fitting rooms with curtains, one curtain half open showing a mirror and a stool."),
    "on_sale": ("scene", "a clothing rack of shirts with bright red blank tags hanging from them; no letters, no numbers, no percent signs."),
    "cashier": ("geste", "a cashier behind a shop counter handing a paper bag to a customer, both smiling."),
    "toque": ("objet", "a knitted winter tuque with a pompom, red and white stripes; no logo."),
    "souvenir": ("objet", "a few small souvenirs together: a snow globe with a tiny city skyline, a small wooden moose, a fridge magnet shaped like a maple leaf; no letters."),
    # --- Le corps et la pharmacie
    "pharmacy": ("scene", "the inside of a pharmacy: white shelves of boxes with blank fronts, a counter at the back; no signs, no letters on any box."),
    "pharmacist": ("geste", "a pharmacist in a white coat behind a counter, explaining something to a customer while holding a small box with a blank front."),
    "fever": ("corps", "a person's head and shoulders with a thermometer in the mouth, the forehead coloured coral red."),
    "sunburn": ("corps", "the back and shoulders of a person, the shoulders and upper back coloured coral red as if sunburned."),
    "blister": ("corps", "a bare heel seen from the side with a small round blister on the back of the heel coloured coral red."),
    "pill": ("objet", "a few white round tablets beside a small plain bottle with a blank label; no letters."),
    "prescription": ("objet", "a small white prescription pad sheet with only grey lines, and a pen lying across it; no letters, no logo."),
    "walk_in": ("scene", "a small clinic waiting room: a row of chairs, a reception window, a plant; no signs, no letters."),
    # --- Le temps qu'il fait
    "hot": ("scene", "a bright sunny city park in summer: a strong sun, heat shimmering, a person fanning themselves on a bench."),
    "cold": ("scene", "a snowy winter street, people bundled in coats and tuques, breath visible in the cold air."),
    "rain": ("scene", "a city street in heavy rain, puddles, a few people with umbrellas."),
    "snow": ("scene", "snow falling softly on a park with trees and a bench covered in snow."),
    "windy": ("scene", "trees bending in strong wind by a lake, leaves blowing, a person holding their hat."),
    "sunny": ("scene", "a clear blue sky with a bright sun over a lakeside boardwalk."),
    "umbrella": ("objet", "an open black umbrella seen from the side, a few raindrops around it."),
    # --- Le petit bavardage
    "library": ("scene", "a bright public library reading room: tall shelves of books with blank spines, long tables, a few readers."),
}
TEMOINS = ["streetcar", "terminal", "peameal"]
