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
    "frutos_secos": ("objet", "a small bowl of mixed nuts: walnuts, almonds and hazelnuts."),
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
    "photograph of a sketchbook: no page edge, no paper shadow. No people in close-up. No text, "
    "no letters, no numbers, no signs, no logo. No frame, no border.\n\n"
    "THE SCENE: ")
PORTRAIT = (
    "A travel-sketchbook portrait in ink and light wash: head and shoulders of ONE person, facing "
    "slightly to the side, looking at the viewer, crisp black ink line of even weight, a few "
    "flat, soft, slightly muted colour fills, centred in a square frame, fading softly into a pure "
    "white background. A flat scan of the drawing, not a photograph of a sketchbook. No text, no "
    "letters, no logo, no badge text. No frame, no border.\n\n"
    "THE PERSON: ")
