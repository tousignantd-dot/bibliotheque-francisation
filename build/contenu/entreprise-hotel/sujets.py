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

TEMOINS = ["carte-cle", "lit-queen", "sonnette"]
