"""Ce que montre chaque croquis du lexique de Compostelle — (famille, description).

Familles : `objet` (le préambule OBJET de Francœur, importé, jamais recopié),
`corps` (une silhouette neutre, la partie nommée en couleur), `scene` (un
petit paysage de carnet, pour les mots qui sont des lieux ou du temps qu'il
fait). Chaque description est écrite pour ce qu'il y a de risqué dans l'objet :
un objet qui porte d'ordinaire un texte (borne, guichet, carte) est décrit
SANS sa face écrite.
"""

SUJETS = {
    # --- le chemin
    "flecha": ("objet", "a bold hand-painted bright yellow arrow pointing right, painted directly on an irregular rough grey stone block; the stone has an irregular natural outline — no square frame, no box, no border around it."),
    "concha": ("objet", "a scallop shell seen from the outside, ribbed, cream and pale ochre, with a small hole and a red cord tied at the top."),
    "mojon": ("objet", "a plain concrete waymarker post of the Way of St James, rounded top, with a blue ceramic tile showing a stylised yellow scallop shell; the post has NO numbers and NO plaque."),
    "credencial": ("objet", "a closed small folded paper booklet, cream cover with a simple red scallop shell drawing, a slightly worn corner; nothing written on it."),
    "sello": ("objet", "a wooden-handled rubber ink stamp standing next to a small open ink pad, dark red ink; the stamp face is not visible."),
    "baston": ("objet", "a wooden walking staff with a knot at the top, a scallop shell and a small gourd tied near the top with a cord."),
    "mochila": ("objet", "a hiking backpack, green, seen from the front, with a scallop shell hanging from a strap; no logo."),
    "botas": ("objet", "a pair of brown leather hiking boots, laced, seen at a slight angle, a little dusty."),
    "fuente": ("objet", "a small old stone drinking fountain with a metal spout and a trickle of water falling into a stone basin."),
    "puente": ("scene", "a small medieval stone footbridge with three arches over a stream, grass on the banks."),
    "cruce": ("scene", "a dirt path that splits in two at a fork, a stone waymarker with a painted yellow arrow at the fork pointing left."),
    "subida": ("scene", "a steep dirt path climbing up a green hillside, seen from below."),
    "bajada": ("scene", "a steep stony path going down a slope towards a valley, seen from above."),
    "peregrino": ("objet", "a hiker seen from behind, walking away, with a backpack, a wide hat and a wooden staff; no face visible."),
    "pueblo": ("scene", "a tiny Spanish village of stone houses with red tile roofs around a church bell tower, seen from a distance."),
    # --- l'albergue
    "albergue": ("scene", "a simple old two-storey stone house with a wooden door wide open, three hiking backpacks and a pair of boots lined up by the door; no sign on the building."),
    "litera": ("objet", "a metal bunk bed with two mattresses, a rolled sleeping bag on the top bunk, seen from the side."),
    "saco": ("objet", "a blue sleeping bag, half rolled, with its drawstring stuff sack beside it."),
    "almohada": ("objet", "a white pillow, slightly squashed."),
    "manta": ("objet", "a folded grey wool blanket with a simple striped border."),
    "ducha": ("objet", "a shower head on a tiled wall with water drops falling, a shower tray below."),
    "toalla": ("objet", "a folded light blue microfibre travel towel."),
    "taquilla": ("objet", "a small metal locker with its door half open and a padlock hanging from the latch; no number on it."),
    "lavadora": ("objet", "a front-loading washing machine, white, round glass door with clothes inside; the control panel is blank, no display text."),
    "secadora": ("objet", "a front-loading tumble dryer, white, round door closed; the control panel is blank."),
    "tendedero": ("objet", "a folding clothes drying rack with hiking socks and a T-shirt hanging on it with clothes pegs."),
    "enchufe": ("objet", "a European wall power socket (two round holes) with a phone charger plugged in, the cable hanging down."),
    "cargador": ("objet", "a small white phone charger with its coiled cable; no logo."),
    "tapones": ("objet", "a pair of soft orange foam earplugs."),
    # --- manger et boire
    "postre": ("objet", "a Spanish caramel flan (crème caramel) on a small white plate, caramel sauce glossy on top."),
    "cafe_leche": ("objet", "a glass of Spanish café con leche on a saucer with a small spoon and a sugar sachet with nothing written on it."),
    "cortado": ("objet", "a small glass of espresso with a little milk foam on top, on a saucer."),
    "zumo": ("objet", "a tall glass of fresh orange juice next to half an orange."),
    "agua": ("objet", "a plastic water bottle with a blue cap and a plain blank label."),
    "cana": ("objet", "a small glass of draught beer with a white foam head."),
    "vino": ("objet", "a short glass of red wine on a bar counter."),
    "tostada": ("objet", "a slice of toasted bread on a small plate, with a pat of butter and a small dish of jam."),
    "mantequilla": ("objet", "a block of butter on a small dish with a butter knife."),
    "tortilla": ("objet", "a thick slice of Spanish potato omelette on a small plate, the potato layers visible on the cut side."),
    "bocadillo": ("objet", "a baguette sandwich cut in half, filled with ham, on a paper napkin."),
    "pintxo": ("objet", "a Basque pintxo: a slice of baguette topped with a pepper and an anchovy, held together by a wooden toothpick."),
    "pulpo": ("objet", "Galician-style octopus: slices of cooked octopus on a round wooden plate, sprinkled with red paprika, a small wooden toothpick."),
    "pan": ("objet", "a rustic round loaf of bread with a crusty top."),
    "vaso": ("objet", "an empty plain drinking glass, a simple tumbler."),
    # --- acheter
    "cajero": ("objet", "a cash machine set in a wall, seen at a three-quarter angle; the screen is a plain blank blue glow, the keypad has blank keys, no text or logo anywhere."),
    "efectivo": ("objet", "a few coins and two folded banknotes, the banknotes shown from the edge so that no printing is readable."),
    "tarjeta": ("objet", "a plain bank card in teal, seen at an angle, with only a gold chip; no numbers, no name, no logo."),
    "bolsa": ("objet", "a reusable cloth shopping bag with a baguette and a bunch of bananas sticking out."),
    "fruta": ("objet", "a small wooden crate with apples, oranges and a bunch of grapes."),
    "platano": ("objet", "a bunch of three yellow bananas."),
    "queso": ("objet", "a round soft cow's-milk cheese from Galicia, pale yellow, one wedge cut out."),
    "jamon": ("objet", "a few thin slices of cured ham on a wooden board."),
    # --- le corps
    "farmacia": ("objet", "a green illuminated pharmacy cross sign, as seen outside Spanish pharmacies; just the green cross, no letters."),
    "ampolla": ("corps", "a bare human heel seen from the side, with one small round swollen blister on the back of the heel, coloured coral red."),
    "pie": ("corps", "a bare human foot seen from the side; the whole foot coloured in coral red."),
    "rodilla": ("corps", "a standing human figure seen from the front; only the KNEES are coloured in coral red."),
    "tobillo": ("corps", "a human lower leg and foot seen from the side; only the ANKLE is coloured in coral red."),
    "espalda": ("corps", "a standing human figure seen from BEHIND; only the BACK is coloured in coral red."),
    "hombro": ("corps", "a human figure from the waist up, seen from the front; only the SHOULDERS are coloured in coral red."),
    "tirita": ("objet", "two adhesive bandages, one flat and one slightly curved, beige with a white pad."),
    "aguja": ("objet", "a sewing needle threaded with white thread, the thread curling."),
    "crema": ("objet", "a squeezed tube of cream with a white cap, the tube is plain with no label."),
    "crema_solar": ("objet", "a bottle of sunscreen lotion, orange, with a small sun drawn on it and no text."),
    # --- le temps
    "lluvia": ("scene", "rain falling from a grey cloud onto a dirt path with puddles."),
    "sol": ("scene", "a bright sun in a clear blue sky above a golden wheat field."),
    "niebla": ("scene", "thick white fog over a mountain path, a few pine trees half hidden in the mist; the fog fades into the pure white background — no beige paper, no tinted background."),
    "viento": ("scene", "strong wind bending tall grass and a small tree, wind lines in the air."),
    "barro": ("scene", "a muddy path with deep boot prints and puddles."),
    "chubasquero": ("objet", "a red hooded rain jacket, zipped, seen from the front."),
    "gorra": ("objet", "a beige cotton cap with a visor, seen at a three-quarter angle."),
    # --- se déplacer
    "autobus": ("objet", "a white and green regional bus seen from the side; the destination display is blank."),
    "taxi": ("objet", "a white Spanish taxi car seen from the side, with a small green light on the roof; no text."),
    "transporte": ("objet", "a hiking backpack with a blank paper luggage tag attached to its strap by a string, placed next to a small van's open back door."),
    # --- visiter
    "catedral": ("scene", "a small Gothic cathedral with two spires and a rose window, seen from a square."),
    "iglesia": ("scene", "a small Romanesque stone village church with a bell gable."),
    "claustro": ("scene", "a cloister: a square garden surrounded by a gallery of round stone arches on columns."),
    "castillo": ("scene", "a medieval stone castle on a hill, with towers and battlements."),
    "plaza_mayor": ("scene", "a Spanish main square surrounded by arcaded buildings with balconies, a few tables of a café."),
    "vidriera": ("objet", "a Gothic stained-glass window with a pointed arch, bright blue, red and gold pieces of glass."),
    "mercado": ("scene", "a covered market stall with fruit and vegetables in crates."),
    "bodega": ("scene", "a wine cellar with oak barrels lying in rows under a stone vault."),
    # --- les mots sans objet (26 sept. 2026, « il manque des images ») : lieux et
    # repas en `scene`, gestes et formules en `geste`. Tout ce qui porterait un
    # texte (écriteau ouvert/fermé, horaire, billet, 112) est dessiné SANS lui.
    "etapa": ("scene", "a winding dirt path across green hills from a small village in the foreground to another small village with a church tower far away, like one day's walk."),
    "hospitalero": ("geste", "a friendly middle-aged hostel volunteer behind a simple wooden table in a stone entrance hall, welcoming a tired pilgrim with a backpack; bunk beds glimpsed through a doorway behind."),
    "completo": ("scene", "a hostel dormitory seen from the doorway: every bunk bed taken, each with a backpack and a sleeping bag on it, boots lined up underneath; not one free bed."),
    "donativo": ("objet", "a small rustic wooden box with a slot on top, standing on a stone table, a few coins beside it; nothing written on it."),
    "pension": ("scene", "the front of a small family guesthouse in a Spanish town: a narrow three-storey house with wooden balconies and flower pots, a door open onto the street; the sign above the door is blank."),
    "quedan": ("geste", "a pilgrim with a backpack at a hostel reception, pointing with a hopeful, questioning look towards a row of bunk beds; one bed is still empty."),
    "desayuno": ("objet", "a Spanish breakfast on a café table: a cup of milky coffee, a small glass of fresh orange juice, and a slice of toasted bread with crushed tomato and olive oil."),
    "comida": ("scene", "a sunny terrace at midday, a long table with plates of food, a jug of water and bread, the sun high overhead, short shadows."),
    "cena": ("scene", "a small village restaurant in the evening: a table with a lit candle, plates and a bottle of red wine, dark blue sky through the window."),
    "menu_peregrino": ("objet", "a pilgrim's meal set out on a tablecloth: a bowl of soup, a plate of roast chicken with fries, a small flan, a basket of bread and a bottle of red wine."),
    "primero": ("objet", "a single bowl of vegetable soup with a spoon, on a white plate, the first course of a meal."),
    "segundo": ("objet", "a single plate with a grilled fish fillet and fried potatoes, a main course, with knife and fork."),
    "carta": ("objet", "an open restaurant menu folder on a table, its pages covered only with small drawings of dishes (a fish, a chicken leg, a bowl, a glass) and blank lines — no letters, no prices."),
    "cuenta": ("objet", "a small saucer on a café table holding a folded blank paper bill, a few euro coins and a pen; nothing legible on the paper."),
    "propina": ("objet", "a few small coins left on a saucer beside an empty coffee cup on a café table."),
    "sin_gluten": ("objet", "a loaf of bread and a wheat ear, both inside a red circle crossed by a red diagonal bar, like a prohibition sign; no letters."),
    "vegetariano": ("objet", "a colourful plate of grilled vegetables — peppers, courgette, aubergine, tomatoes — with a sprig of parsley, no meat, no fish."),
    "marisco": ("objet", "a plate of seafood: prawns, mussels in their shells and a few clams, with a lemon wedge."),
    "pescado": ("objet", "a whole fresh fish, silvery, lying on a plate with a lemon slice."),
    "huevo": ("objet", "two brown eggs, one whole and one cracked open in a small bowl showing the yolk."),
    "leche": ("objet", "a glass bottle of milk next to a full glass of milk; no label."),
    "sesamo": ("objet", "a small wooden spoon full of pale sesame seeds, a few seeds scattered, and a bread roll covered in sesame seeds."),
    "lleva": ("geste", "a pilgrim at a bar counter pointing at one sandwich in the glass display case, with a questioning look at the barman, who is about to answer."),
    "a_que_hora": ("geste", "a pilgrim with a backpack pointing to a round wall clock (hands and tick marks only, no numbers) while looking questioningly at a hostel volunteer."),
    "abierto": ("scene", "a small village shop with its door wide open, warm light inside, crates of fruit on the pavement outside; no sign, no writing."),
    "cerrado": ("scene", "the same kind of small village shop with its metal rolling shutter pulled all the way down, the street empty in the hot early afternoon; no sign, no writing, no graffiti."),
    "manana": ("scene", "a bunk bed with a sleeping pilgrim at night, and through the window beside it a sun beginning to rise over the hills — tonight, then tomorrow."),
    "por_la_tarde": ("scene", "a village square in warm late-afternoon light, long shadows, people sitting at a café terrace under plain umbrellas; the café awning and the walls are completely plain, with NO sign and NO name anywhere."),
    "por_la_noche": ("scene", "a village street at night under a crescent moon and stars, a few lit windows and a street lamp."),
    "siesta": ("geste", "a man dozing in the shade on a bench under a tree, hat over his eyes, in a quiet sunny village street with closed shutters."),
    "tienda": ("scene", "the inside of a small village grocery: wooden shelves with jars, bread, fruit in crates, a counter with an old scale; no labels, no writing."),
    "supermercado": ("scene", "a supermarket aisle with a shopping trolley, shelves of colourful products seen from a distance; no labels, no brand, no price tags."),
    "panaderia": ("scene", "a bakery counter with round country loaves, baguettes and pastries on wooden shelves behind a glass counter; no writing."),
    "cuanto": ("geste", "a pilgrim holding up a bunch of bananas at a market stall with a questioning look, the grocer about to answer; no prices, no numbers."),
    "kilo": ("objet", "an old kitchen scale with a metal pan holding a small pile of red apples; the dial shows only tick marks, no numbers."),
    "ibuprofeno": ("objet", "a small white pill box with a blister strip of round white tablets half pushed out beside it; nothing written anywhere."),
    "me_duele": ("corps", "a standing human figure seen from the front, one hand on the knee, which is the coral red part: pain in the knee."),
    "tendinitis": ("corps", "a lower leg and foot seen from the side, the Achilles tendon at the back of the ankle in coral red."),
    "constipado": ("geste", "a pilgrim sitting on a bunk bed, wrapped in a blanket, blowing their nose into a tissue, a box of tissues beside them."),
    "guardia": ("scene", "a pharmacy front at night: a lit green cross sign glowing above a small lit door with a plain glass pane, the rest of the street dark; nothing written on the door, the windows or the walls."),
    "centro_salud": ("scene", "a modern low health-centre building with glass doors and a simple red cross above the entrance, a bench outside; no writing."),
    "emergencias": ("scene", "a white ambulance with blue lights flashing, parked on a country road; no writing, no numbers on the vehicle."),
    "calor": ("scene", "a dusty track under a blazing sun, heat shimmering over dry golden fields, a pilgrim drinking from a water bottle."),
    "frio": ("scene", "a mountain path in cold fog and light snow, a pilgrim wrapped in a scarf and woolly hat, breath visible."),
    "parada": ("scene", "a small rural bus shelter by the roadside with a bench, a pilgrim waiting with a backpack; the shelter has no writing and no timetable."),
    "billete": ("objet", "a small blank paper ticket held between two fingers, with a torn perforated edge; nothing printed on it."),
    "salida": ("scene", "an open door at the end of a corridor leading to bright daylight outside, with a green running-man pictogram above it; no letters."),
    "buenos_dias": ("geste", "early morning: two pilgrims with backpacks greeting each other with a wave on a path, the sun rising behind the hills."),
    "buenas_tardes": ("geste", "a pilgrim greeting a shopkeeper with a smile and a small wave, in warm afternoon light at a shop doorway."),
    "buenas_noches": ("geste", "two pilgrims in a dim dormitory waving goodnight from their bunk beds, a small bedside lamp, the night through the window."),
    "buen_camino": ("geste", "a villager at her doorway waving cheerfully at a pilgrim with a backpack walking past on the path."),
    "vale": ("geste", "a waiter with a notepad giving a relaxed thumbs-up with a smile to a pilgrim seated at a table."),
    "perdone": ("geste", "a pilgrim lightly touching the shoulder of a passer-by from behind to get attention, polite apologetic expression."),
    "no_entiendo": ("geste", "a pilgrim with a puzzled expression, palms turned up and shoulders shrugged, facing a local person who is talking."),
    "despacio": ("geste", "a pilgrim facing a talkative local, making a calming gesture with both hands pressed slowly downwards, meaning 'slow down'."),
    "repetir": ("geste", "a pilgrim leaning in with a hand cupped behind the ear, towards a smiling local person."),
    "como_se_dice": ("geste", "a pilgrim pointing at a loaf of bread on a counter with a questioning look towards the baker."),
    "lo_siento": ("geste", "a pilgrim with a hand on the heart and an apologetic face, having just bumped a chair, facing another person."),
    "de_nada": ("geste", "a local woman smiling and waving a hand dismissively in a friendly 'it was nothing' gesture, after handing a pilgrim a bottle of water."),
    "entrada": ("scene", "the arched stone entrance door of a church, open, with a few visitors going in."),
    "horario": ("objet", "a round wall clock with hands and tick marks only, no numbers, next to a heavy old wooden church door."),
    "visita_guiada": ("geste", "a small group of visitors with backpacks inside a Gothic cathedral nave, following a guide who points up at the stained-glass windows."),
    "misa": ("scene", "the interior of a stone church during a service: rows of pews with seated people, candles and a priest at the altar, seen from the back."),
    "descuento": ("geste", "at a museum ticket window, a pilgrim showing an open folded pilgrim passport covered with round red ink stamps (plain circles and shells, no letters); the clerk smiles and nods. No plaque, no sign, no word on the walls."),
    "de_donde": ("geste", "two pilgrims sitting on a low stone wall with their backpacks beside them, chatting, one asking the other with an open hand gesture."),
    "soy_de": ("geste", "a pilgrim with a small red maple leaf patch on the backpack, pointing to themselves with a smile while talking to another pilgrim."),
    "por_que": ("geste", "two pilgrims walking side by side on the Meseta, one turning to the other with a curious, thoughtful look."),
    "desde_donde": ("geste", "two pilgrims seen from behind, standing on a path and looking back at the long way they have walked, winding far away into distant mountains; no writing anywhere, no signature."),
    "hasta_donde": ("geste", "two pilgrims looking ahead together at a long path leading to a distant village with a church tower, one pointing forward."),
    "kilometros": ("scene", "a long straight dirt track stretching to the horizon, with plain stone waymarker posts at regular intervals along it (no numbers), a pair of boots in the foreground."),
    "cansado": ("geste", "an exhausted pilgrim sitting on the ground against a stone wall, boots off, backpack dropped beside, head tilted back, eyes closed."),
    "donde_duermes": ("geste", "two pilgrims at dusk on a village street, one pointing questioningly towards a hostel with bunk beds visible through a window."),
    "estas_bien": ("geste", "a pilgrim bending with concern over another pilgrim who sits on a rock holding an ankle, offering a hand."),
    "encantado": ("geste", "two pilgrims shaking hands warmly with a smile, meeting for the first time, backpacks on."),
    "nos_vemos": ("geste", "two pilgrims parting at a fork in a path, waving to each other with a smile over their shoulders."),
    "embarazada": ("geste", "a pilgrim blushing, one hand on the cheek, looking down with an embarrassed smile, in a small group of people at a table."),
}

# Les deux préambules propres à Compostelle, écrits sur le modèle d'OBJET :
# on garde le trait, l'aplat et le fond blanc ; on change ce qui est permis
# dans le cadre.
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
    "photograph of a sketchbook: no page edge, no paper shadow, no grey or beige paper tone: the background around the scene is PURE WHITE. No people in close-up. No text, "
    "no letters, no numbers, no signs, no logo. No frame, no border.\n\n"
    "THE SCENE: ")
GESTE = (
    "A small travel-sketchbook vignette in ink and light wash: one or two people shown full-length or "
    "from the waist up, their gesture and expression clearly readable, in a simple setting on the "
    "Way of St James; crisp black ink line of even weight, a few flat, soft, slightly muted colour "
    "fills, centred in a square frame, fading softly into a pure white background at its edges. A flat "
    "scan of the drawing, not a photograph of a sketchbook, no grey or beige paper tone: the background is PURE WHITE. No speech bubbles, no text, no letters, no "
    "numbers, no signs, no logo. No frame, no border.\n\n"
    "THE SCENE: ")
PORTRAIT = (
    "A travel-sketchbook portrait in ink and light wash: head and shoulders of ONE person, facing "
    "slightly to the side, looking at the viewer, crisp black ink line of even weight, a few "
    "flat, soft, slightly muted colour fills, centred in a square frame, fading softly into a pure "
    "white background. A flat scan of the drawing, not a photograph of a sketchbook. No text, no "
    "letters, no logo, no badge text. No frame, no border.\n\n"
    "THE PERSON: ")
