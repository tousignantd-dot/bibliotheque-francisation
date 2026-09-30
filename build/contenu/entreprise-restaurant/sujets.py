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
