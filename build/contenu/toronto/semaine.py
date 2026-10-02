"""La semaine d'« Une semaine à Toronto » — dix lieux, leurs décors, leurs cartes postales, leurs gens.

Étape 3 (1er oct. 2026). Source unique du plan de la ville, de l'album des cartes
postales et, à l'étape 5, des situations jouées.

- LIEUX : (id, n, jour, lieu, situation, geste qui compte, qui, décor, carte postale).
  `decor` décrit la scène VUE DE LA PLACE DU TOURISTE (l'apprenant est le client) :
  le comptoir, le guichet ou la rue devant lui, et l'espace de la personne VIDE au
  centre — elle y sera posée, détourée, comme au comptoir de l'hôtel (méthode
  croquis-sequence : le décor ne bouge pas, les gens changent devant).
  `carte` décrit le recto de la carte postale gagnée : le lieu vu comme un
  touriste le photographie. Aucune enseigne, aucun texte, aucune marque dans
  l'une ou l'autre image.
- GENS : (id, prénom, voix, rôle, portrait). Huit personnes de la ville, plus Maya,
  la Torontoise qui revient chaque jour. Chaque portrait se dessine NEUTRE à partir
  du texte, puis chaque humeur en RETOUCHE du neutre (recette de Francœur, 32 sur 32).
"""

# Les voix (personnages.py) : une même voix peut servir deux personnes qui ne se
# répondent jamais dans une même scène (règle des voix du dépôt).
GENS = [
    ("maya", "Maya", "harper", "La Torontoise qui revient chaque jour",
     "a friendly Torontonian woman in her early thirties, light brown skin, curly dark hair tied up, small gold hoop earrings, a mustard-yellow knit cardigan over a white top"),
    ("kevin", "Kevin", "liam", "L'agent de la gare, puis le guichetier du traversier",
     "a young man in his late twenties, short blond hair, light stubble, a navy blue uniform jacket with a plain collar and no badge text"),
    ("marcus", "Marcus", "andrew", "Le réceptionniste de l'hôtel",
     "a Black man in his forties, short greying hair, neat beard, a charcoal suit jacket over a light blue shirt, a plain name tag with no letters"),
    ("rosa", "Rosa", "rosa", "La barista du café",
     "a Filipino-Canadian woman in her twenties, black hair in a high ponytail, a dark green apron over a grey t-shirt, a warm smile"),
    ("priya", "Priya", "aarti", "La guichetière de la tour",
     "an Indian-Canadian woman in her thirties, long black hair in a braid over one shoulder, a burgundy polo shirt with a plain collar"),
    ("wei", "Wei", "sam", "Le marchand du marché St. Lawrence",
     "a Chinese-Canadian man in his fifties, short black hair with grey at the temples, rectangular glasses, a white butcher's apron over a checked shirt"),
    ("raj", "Raj", "arjun", "Le passant de Kensington",
     "an Indian-Canadian man in his sixties, white beard, a dark blue turban, a beige rain jacket"),
    ("ada", "Ada", "ezinne", "La serveuse du restaurant",
     "a Nigerian-Canadian woman in her late twenties, short natural hair, small stud earrings, a black shirt and a black waist apron"),
    ("tom", "Tom", "andrew", "Le pharmacien",
     "a white man in his fifties, bald, round glasses, a white pharmacist's coat over a blue shirt, no badge text"),
]
HUMEURS = ["neutre", "contente", "hesitante", "impatiente"]

LIEUX = [
    ("union", 1, "Jour 1", "Union Station", "L'arrivée",
     "trouver le métro, payer son passage, comprendre l'annonce du quai", "kevin",
     "the inside of a grand old railway station seen from a traveller standing in front of a small information booth: a low wooden counter in the foreground, behind it EMPTY space where an agent will stand, then tall stone columns and arched windows; no signs, no departure board.",
     "a grand old stone railway station front with a long row of tall classical columns, on a sunny day, taxis and walkers in front; no signs, no letters."),
    ("hotel", 2, "Jour 1", "L'hôtel, rue King", "L'arrivée à la réception",
     "épeler son nom, comprendre le dépôt, l'heure du déjeuner, le code du wifi", "marcus",
     "a hotel front desk seen from the guest's side: a polished wooden counter in the foreground with a small bell and a key-card holder, behind it EMPTY space where the receptionist will stand, then a wall of soft wood panels and a plant; no signs, no letters.",
     "a busy downtown street lined with old brick buildings and glass towers, a red streetcar passing, evening lights; no signs, no letters."),
    ("cafe", 3, "Jour 2", "Le café du matin", "Le café du matin",
     "commander vite, comprendre « Anything else? For here or to go? », payer au terminal", "rosa",
     "a small coffee shop counter seen from the customer's side: the counter in the foreground with a card payment terminal (blank screen) and a glass pastry case, behind it EMPTY space where the barista will stand, then an espresso machine and shelves of cups; no menu board text, no logo.",
     "a cosy neighbourhood coffee shop window on a street corner in the morning, steam from cups, a bicycle leaning outside; no shop sign, no letters."),
    ("tour", 4, "Jour 2", "La tour CN", "Les billets",
     "acheter deux billets à heure fixe, comprendre l'heure de montée et le tarif", "priya",
     "a ticket window at the foot of a tall tower seen from the visitor's side: a glass ticket window with a small speaking grille in the foreground, behind the glass EMPTY space where the ticket agent will sit, a queue rope on the side; no signs, no prices, no letters.",
     "a very tall slender concrete observation tower with a round pod near the top, seen from below against a blue sky, a domed stadium beside it; no signs."),
    ("marche", 5, "Jour 3", "Le marché St. Lawrence", "Au comptoir",
     "commander au poids, comprendre le total taxe comprise", "wei",
     "a butcher and sandwich counter in a covered market seen from the customer's side: a glass display case of meats and cheeses in the foreground with a small scale, behind it EMPTY space where the vendor will stand, then the high roof of the market hall; no signs, no prices.",
     "the outside of a large old red-brick market hall with arched windows and a clock-less pediment, people walking in with bags; no signs, no letters."),
    ("kensington", 6, "Jour 4", "Kensington", "Perdu dans les quartiers",
     "demander son chemin à quelqu'un qui répond vite, avec un accent, et le suivre", "raj",
     "a colourful narrow street in an eclectic neighbourhood seen at eye level: brightly painted Victorian house fronts with shops, racks of vintage clothes and fruit stands on the sidewalk, the middle of the sidewalk in the foreground EMPTY where a passer-by will stand; no shop signs, no letters.",
     "a colourful eclectic market street with painted houses, murals of abstract shapes, fruit stalls and bicycles; no signs, no letters."),
    ("iles", 7, "Jour 5", "Les îles de Toronto", "Le traversier et le vélo",
     "acheter le passage, louer un vélo, comprendre l'heure du dernier bateau", "kevin",
     "a small ferry ticket booth at a waterfront dock seen from the passenger's side: a wooden booth window in the foreground, behind it EMPTY space where the ticket agent will stand, the lake and a white ferry beside the dock; no signs, no prices.",
     "the city skyline with a very tall slender observation tower seen across the water from a green island park at sunset, a ferry crossing; no signs."),
    ("pharmacie", 8, "Jour 6", "La pharmacie, Yonge", "Un coup de soleil, au lendemain des îles",
     "décrire, comprendre la posologie", "tom",
     "a pharmacy counter seen from the customer's side: a white counter in the foreground with a small basket, behind it EMPTY space where the pharmacist will stand, then white shelves of boxes with blank fronts; no signs, no letters on any box.",
     "a long busy main street with shops and a crowd on the sidewalks, a big intersection with a pedestrian scramble crossing seen from above; no signs, no screens with text."),
    ("resto", 9, "Jour 6", "Le restaurant, Little Italy", "Le souper",
     "avoir une table, commander, dire qu'on ne mange pas de viande et comprendre la réponse, payer séparément, laisser le pourboire", "ada",
     "a restaurant table for two seen from the seated guest's place: the table in the foreground with plates, glasses and a candle, an EMPTY space beside the table where the server will stand, warm lights and other tables behind; no menu text, no signs.",
     "a lively street of Italian restaurants at dusk, patios with string lights and red umbrellas, people dining outside; no signs, no letters."),
    ("depart", 10, "Jour 7", "Le départ", "Une erreur sur la facture",
     "contester poliment un montant, comprendre la solution, demander le chemin de l'UP Express", "marcus",
     "the same hotel front desk seen from the guest's side, at checkout: the polished wooden counter in the foreground with a printed bill shown only as grey lines and a pen, behind it EMPTY space where the receptionist will stand; no letters, no numbers.",
     "a modern airport train speeding on an elevated track past the city at morning, the skyline behind; no logo, no letters."),
]


def verifier(voix):
    ids = [g[0] for g in GENS]
    assert len(ids) == len(set(ids)), "personne en double"
    for g in GENS:
        assert g[2] in voix, (g[0], g[2])
    assert [l[1] for l in LIEUX] == list(range(1, 11)), "dix lieux, dans l'ordre"
    for l in LIEUX:
        assert l[6] in ids, (l[0], l[6])
        assert "EMPTY" in l[7], (l[0], "le décor garde la place de la personne vide")
    return True


if __name__ == "__main__":
    import importlib.util, pathlib
    sp = importlib.util.spec_from_file_location("toronto_personnages", pathlib.Path(__file__).parent / "personnages.py")
    ps = importlib.util.module_from_spec(sp); sp.loader.exec_module(ps)
    verifier(ps.VOIX)
    n = len(LIEUX) * 2 + len(GENS) * len(HUMEURS)
    print(f"{len(LIEUX)} lieux, {len(GENS)} personnes ; {n} images à dessiner ≈ {n * 0.067:.2f} $")
