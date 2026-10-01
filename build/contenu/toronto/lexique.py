"""Le lexique d'« Une semaine à Toronto » — l'anglais du touriste francophone.

    python3 build/contenu/toronto/lexique.py      # compte et vérifie

UNE SOURCE, UN TUPLE : (id, planche, en, fr, dessin, note)

- en : l'anglais du CANADA (décision du 1er oct. 2026) — washroom, toque,
  loonie, l'orthographe colour et centre. Une autre façon de dire, entendue aux
  États-Unis ou ailleurs, va dans la note. Ce qui est entre parenthèses est une
  glose, pas un texte à dire.
- fr : le français du QUÉBEC, celui de l'apprenant : le déjeuner est le repas
  du matin, le dîner celui du midi, le souper celui du soir.
- dessin : `croquis` (à engendrer), `picto:<nom>` (dessiné en SVG dans la
  page : flèches, horloges, pièces de monnaie), `""` (sans image — une
  formule, une phrase : elle se joue à l'oreille).
- note : une note qui commence par `PIÈGE` est un faux ami ou un piège
  d'oreille ; sa phrase de voyage vit dans PIEGES, plus bas. Règle payée à
  l'hôtel : jamais un faux ami montré seul, il est souvent vrai aussi.

Aucune marque dans le lexique ni dans les croquis : on dit « le café du
coin », jamais une chaîne ; « double-double » est un mot d'ici, il reste.
Le contenu est INVENTÉ pour la trousse, jamais recopié d'un guide.
"""

PLANCHES = [
    ("transport", "Arriver et se déplacer", "Getting around"),
    ("hotel", "L'hôtel", "The hotel"),
    ("cafe", "Le café", "The coffee shop"),
    ("resto", "Le restaurant", "The restaurant"),
    ("payer", "Payer", "Paying"),
    ("visiter", "Visiter", "Sightseeing"),
    ("magasin", "Magasiner", "Shopping"),
    ("sante", "Le corps et la pharmacie", "Health"),
    ("meteo", "Le temps qu'il fait", "The weather"),
    ("heure", "L'heure et les jours", "Time and days"),
    ("gens", "Les gens, la politesse", "People"),
    ("jasette", "Le petit bavardage", "Small talk"),
]

LEXIQUE = [
    # --- Arriver et se déplacer ---------------------------------------------
    ("station", "transport", "the train station", "la gare", "croquis", ""),
    ("platform", "transport", "the platform", "le quai", "croquis", ""),
    ("subway", "transport", "the subway", "le métro", "croquis", "On dit aussi « the TTC », du nom de la société de transport."),
    ("streetcar", "transport", "the streetcar", "le tramway", "croquis", "Le tramway rouge est un emblème de Toronto ; ailleurs, « tram » ou « trolley »."),
    ("bus", "transport", "the bus", "l'autobus", "croquis", ""),
    ("bus_stop", "transport", "the bus stop", "l'arrêt d'autobus", "croquis", ""),
    ("transfer", "transport", "a transfer", "une correspondance", "", ""),
    ("fare", "transport", "the fare", "le prix du passage", "", "PIÈGE : « fare » n'est pas « faire » ; c'est ce que coûte un trajet."),
    ("transit_card", "transport", "the transit card", "la carte de transport", "croquis", "À Toronto, la carte s'appelle PRESTO ; on paie aussi en touchant sa carte de crédit."),
    ("tap", "transport", "to tap your card", "toucher le lecteur avec sa carte", "croquis", ""),
    ("ferry", "transport", "the ferry", "le traversier", "croquis", ""),
    ("taxi", "transport", "a cab, a taxi", "un taxi", "croquis", ""),
    ("exit", "transport", "the exit", "la sortie", "croquis", "PIÈGE : « exit » est la sortie, pas un « excès »."),
    ("entrance", "transport", "the entrance", "l'entrée", "croquis", ""),
    ("block", "transport", "a block", "un coin de rue (un pâté de maisons)", "picto:blocs", "« Two blocks north » : deux coins de rue vers le nord."),
    ("corner", "transport", "the corner", "le coin", "croquis", ""),
    ("intersection", "transport", "Queen and Spadina", "le coin de Queen et Spadina", "picto:carrefour", "À Toronto, un lieu se donne par son intersection : « at Queen and Spadina »."),
    ("north", "transport", "north", "le nord", "picto:nord", ""),
    ("south", "transport", "south", "le sud", "picto:sud", "À Toronto, le sud, c'est le lac."),
    ("east", "transport", "east", "l'est", "picto:est", ""),
    ("west", "transport", "west", "l'ouest", "picto:ouest", ""),
    ("left", "transport", "turn left", "tournez à gauche", "picto:gauche", ""),
    ("right", "transport", "turn right", "tournez à droite", "picto:droite", ""),
    ("straight", "transport", "go straight", "allez tout droit", "picto:droit", ""),
    ("underground", "transport", "the PATH, underground", "la ville souterraine (le PATH)", "croquis", "Le PATH relie les tours du centre-ville sous terre, comme le RÉSO à Montréal."),

    # --- L'hôtel -------------------------------------------------------------
    ("reservation", "hotel", "a reservation", "une réservation", "", ""),
    ("check_in", "hotel", "to check in", "s'enregistrer, arriver à l'hôtel", "", ""),
    ("check_out", "hotel", "to check out", "quitter la chambre", "", ""),
    ("front_desk", "hotel", "the front desk", "la réception", "croquis", ""),
    ("room", "hotel", "a room", "une chambre", "croquis", "PIÈGE : « room » est une chambre ou une pièce, jamais un « rhum »."),
    ("double_bed", "hotel", "a queen bed", "un grand lit", "croquis", "Au Canada, on dit la taille : « a queen », « a king » ; « two doubles » : deux lits doubles."),
    ("two_beds", "hotel", "two double beds", "deux lits doubles", "croquis", ""),
    ("key_card", "hotel", "the key card", "la carte-clé", "croquis", ""),
    ("deposit", "hotel", "a deposit", "un dépôt (une garantie)", "", "PIÈGE : le « deposit » de l'hôtel est un montant bloqué sur la carte, remis au départ."),
    ("wifi", "hotel", "the Wi-Fi password", "le mot de passe du wifi", "croquis", ""),
    ("breakfast_incl", "hotel", "breakfast included", "le déjeuner inclus", "", "PIÈGE : « breakfast » est notre déjeuner (le matin)."),
    ("towel", "hotel", "a towel", "une serviette", "croquis", ""),
    ("elevator", "hotel", "the elevator", "l'ascenseur", "croquis", "« lift » en Angleterre."),
    ("lobby", "hotel", "the lobby", "le hall", "croquis", ""),
    ("housekeeping", "hotel", "housekeeping", "le service d'entretien des chambres", "", ""),
    ("late_checkout", "hotel", "a late checkout", "un départ tardif", "", ""),
    ("luggage", "hotel", "luggage, bags", "les bagages", "croquis", ""),
    ("floor", "hotel", "the third floor", "le troisième étage", "", "PIÈGE : au Canada, le « first floor » est le rez-de-chaussée."),

    # --- Le café --------------------------------------------------------------
    ("coffee", "cafe", "a coffee", "un café", "croquis", ""),
    ("small", "cafe", "small", "petit", "croquis", ""),
    ("medium", "cafe", "medium", "moyen", "croquis", ""),
    ("large", "cafe", "large", "grand", "croquis", "PIÈGE : « large » veut dire grand, pas large."),
    ("milk", "cafe", "milk", "du lait", "croquis", ""),
    ("cream", "cafe", "cream", "de la crème", "croquis", ""),
    ("sugar", "cafe", "sugar", "du sucre", "croquis", ""),
    ("double_double", "cafe", "a double-double", "un café deux crèmes, deux sucres", "", "Un mot d'ici, compris dans tout le Canada."),
    ("for_here", "cafe", "for here", "pour manger ici", "", ""),
    ("to_go", "cafe", "to go", "pour emporter", "croquis", "« takeaway » en Angleterre."),
    ("tea", "cafe", "a tea", "un thé", "croquis", ""),
    ("muffin", "cafe", "a muffin", "un muffin", "croquis", ""),
    ("bagel", "cafe", "a bagel", "un bagel", "croquis", ""),
    ("straw", "cafe", "a straw", "une paille", "croquis", ""),
    ("water", "cafe", "a glass of water", "un verre d'eau", "croquis", ""),
    ("receipt", "cafe", "the receipt", "le reçu", "croquis", "PIÈGE : le « p » de « receipt » ne se dit pas."),
    ("anything_else", "cafe", "Anything else?", "Autre chose ?", "", "La question qui suit toute commande : on répond « That's it, thanks »."),

    # --- Le restaurant -------------------------------------------------------
    ("table_for_two", "resto", "a table for two", "une table pour deux", "croquis", ""),
    ("menu", "resto", "the menu", "le menu (la carte)", "croquis", ""),
    ("appetizer", "resto", "an appetizer", "une entrée", "croquis", "PIÈGE : en Amérique du Nord, « entrée » veut dire le plat principal."),
    ("main", "resto", "the main course", "le plat principal", "croquis", ""),
    ("dessert", "resto", "dessert", "le dessert", "croquis", "PIÈGE : « dessert » (deux s) et « desert » (le désert) ne se disent pas pareil."),
    ("tap_water", "resto", "tap water", "l'eau du robinet", "croquis", ""),
    ("rare", "resto", "rare, medium, well done", "saignant, à point, bien cuit", "croquis", ""),
    ("allergy", "resto", "I'm allergic to…", "je suis allergique à…", "", ""),
    ("nuts", "resto", "nuts, peanuts", "les noix, les arachides", "croquis", ""),
    ("gluten_free", "resto", "gluten-free", "sans gluten", "", ""),
    ("vegetarian", "resto", "vegetarian", "végétarien", "", ""),
    ("server", "resto", "the server", "le serveur, la serveuse", "croquis", ""),
    ("the_bill", "resto", "the bill", "l'addition", "croquis", "PIÈGE : « the bill » est l'addition ; on entend aussi « the check » aux États-Unis."),
    ("separate", "resto", "separate bills", "des additions séparées", "", ""),
    ("tip", "resto", "the tip", "le pourboire", "", "À Toronto, 18 à 20 % du montant avant taxe ; le terminal propose ses pourcentages."),
    ("leftovers", "resto", "a box for the leftovers", "une boîte pour les restes", "croquis", ""),
    ("napkin", "resto", "a napkin", "une serviette de table", "croquis", "PIÈGE : « napkin » est la serviette de table ; « towel », celle de bain."),
    ("fork", "resto", "a fork", "une fourchette", "croquis", ""),
    ("knife", "resto", "a knife", "un couteau", "croquis", "Le « k » de « knife » ne se dit pas."),
    ("spoon", "resto", "a spoon", "une cuillère", "croquis", ""),
    ("spicy", "resto", "spicy", "épicé, piquant", "", ""),
    ("peameal", "resto", "a peameal bacon sandwich", "un sandwich au bacon de dos", "croquis", "La spécialité du marché St. Lawrence."),
    ("lunch", "resto", "lunch", "le dîner (le repas du midi)", "", "PIÈGE : notre dîner se dit « lunch »."),
    ("dinner", "resto", "dinner", "le souper (le repas du soir)", "", "PIÈGE : « dinner », c'est le souper."),

    # --- Payer ---------------------------------------------------------------
    ("price", "payer", "the price", "le prix", "", ""),
    ("how_much", "payer", "How much is it?", "Combien ça coûte ?", "", ""),
    ("tax", "payer", "plus tax", "plus les taxes", "", "En Ontario, une seule taxe, la TVH (HST), ajoutée à la caisse."),
    ("total", "payer", "the total", "le total", "", ""),
    ("cash", "payer", "cash", "comptant", "croquis", "PIÈGE : « cash » est l'argent comptant, pas la caisse (« the cash register », « the till »)."),
    ("card", "payer", "debit or credit?", "débit ou crédit ?", "croquis", ""),
    ("terminal", "payer", "the payment machine", "le terminal de paiement", "croquis", "On vous le tend : on touche, on choisit le pourboire, on confirme."),
    ("loonie", "payer", "a loonie", "une pièce d'un dollar (un huard)", "picto:huard", ""),
    ("toonie", "payer", "a toonie", "une pièce de deux dollars", "picto:deux", ""),
    ("quarter_coin", "payer", "a quarter", "une pièce de 25 sous", "picto:25", "PIÈGE : « a quarter » est aussi un quart d'heure."),
    ("change", "payer", "your change", "votre monnaie", "", "PIÈGE : « change » est aussi la monnaie qu'on vous rend, pas seulement un changement."),
    ("bag", "payer", "Do you need a bag?", "Voulez-vous un sac ?", "croquis", ""),
    ("price_four99", "payer", "four ninety-nine", "4,99 $", "", "Les prix se disent en deux nombres : « four ninety-nine », « twelve fifty »."),
    ("thirteen", "payer", "thirteen", "treize", "", "PIÈGE : « thirteen » (13) et « thirty » (30) : l'accent est à la fin dans 13, au début dans 30."),
    ("fifteen", "payer", "fifteen", "quinze", "", "PIÈGE : « fifteen » (15) et « fifty » (50)."),

    # --- Visiter -------------------------------------------------------------
    ("ticket", "visiter", "a ticket", "un billet", "croquis", ""),
    ("timed_entry", "visiter", "a timed entry", "une entrée à heure fixe", "", ""),
    ("adult", "visiter", "two adults", "deux adultes", "", ""),
    ("senior", "visiter", "a senior", "un aîné", "", ""),
    ("child", "visiter", "a child, kids", "un enfant, des enfants", "", ""),
    ("guided_tour", "visiter", "a guided tour", "une visite guidée", "croquis", ""),
    ("audio_guide", "visiter", "an audio guide", "un audioguide", "croquis", ""),
    ("coat_check", "visiter", "the coat check", "le vestiaire", "croquis", ""),
    ("gift_shop", "visiter", "the gift shop", "la boutique", "croquis", ""),
    ("open", "visiter", "open", "ouvert", "", ""),
    ("closed", "visiter", "closed", "fermé", "", ""),
    ("museum", "visiter", "the museum", "le musée", "croquis", ""),
    ("gallery", "visiter", "the art gallery", "le musée d'art", "croquis", ""),
    ("tower", "visiter", "the tower", "la tour", "croquis", ""),
    ("market", "visiter", "the market", "le marché", "croquis", ""),
    ("island", "visiter", "the island", "l'île", "croquis", "Le « s » de « island » ne se dit pas."),
    ("lake", "visiter", "the lake", "le lac", "croquis", ""),
    ("view", "visiter", "the view", "la vue", "croquis", ""),
    ("line", "visiter", "the line", "la file d'attente", "croquis", "PIÈGE : « the line » est la file ; « queue » en Angleterre."),
    ("bike", "visiter", "to rent a bike", "louer un vélo", "croquis", "PIÈGE : « to rent » veut dire louer, jamais « rentrer »."),
    ("game", "visiter", "a game (a baseball game)", "un match", "croquis", "PIÈGE : « a game » est un match, pas seulement un jeu."),
    ("neighbourhood", "visiter", "the neighbourhood", "le quartier", "croquis", "Orthographe du Canada : « neighbourhood », avec un « u »."),

    # --- Magasiner -----------------------------------------------------------
    ("size", "magasin", "What size?", "Quelle taille ?", "", ""),
    ("try_on", "magasin", "to try it on", "l'essayer", "", ""),
    ("fitting_room", "magasin", "the fitting room", "la cabine d'essayage", "croquis", ""),
    ("bigger", "magasin", "bigger, smaller", "plus grand, plus petit", "", ""),
    ("on_sale", "magasin", "on sale", "en solde", "croquis", "PIÈGE : « on sale » veut dire en solde ; « for sale », à vendre."),
    ("refund", "magasin", "a refund", "un remboursement", "", ""),
    ("exchange", "magasin", "an exchange", "un échange", "", ""),
    ("cashier", "magasin", "the cashier", "le caissier, la caissière", "croquis", ""),
    ("toque", "magasin", "a toque", "une tuque", "croquis", "Un mot du Canada : « toque » se dit « touk »."),
    ("souvenir", "magasin", "a souvenir", "un souvenir (un objet)", "croquis", ""),
    ("just_looking", "magasin", "I'm just looking", "Je regarde seulement", "", ""),

    # --- Le corps et la pharmacie --------------------------------------------
    ("pharmacy", "sante", "the pharmacy, the drugstore", "la pharmacie", "croquis", ""),
    ("pharmacist", "sante", "the pharmacist", "le pharmacien, la pharmacienne", "croquis", ""),
    ("headache", "sante", "a headache", "un mal de tête", "", ""),
    ("stomach", "sante", "a stomach ache", "un mal de ventre", "", ""),
    ("sore_throat", "sante", "a sore throat", "un mal de gorge", "", ""),
    ("fever", "sante", "a fever", "de la fièvre", "croquis", ""),
    ("sunburn", "sante", "a sunburn", "un coup de soleil", "croquis", ""),
    ("blister", "sante", "a blister", "une ampoule (au pied)", "croquis", ""),
    ("pill", "sante", "a pill, a tablet", "un comprimé", "croquis", ""),
    ("twice_a_day", "sante", "twice a day", "deux fois par jour", "", ""),
    ("prescription", "sante", "a prescription", "une ordonnance", "croquis", "PIÈGE : « prescription » est une ordonnance médicale."),
    ("walk_in", "sante", "a walk-in clinic", "une clinique sans rendez-vous", "croquis", ""),
    ("nine_one_one", "sante", "Call 911", "Appelez le 911", "", "Se dit « nine-one-one »."),
    ("drug", "sante", "a drug", "un médicament", "", "PIÈGE : « drug » est d'abord un médicament (« drugstore » : la pharmacie)."),

    # --- Le temps qu'il fait -------------------------------------------------
    ("hot", "meteo", "hot", "chaud", "croquis", ""),
    ("cold", "meteo", "cold", "froid", "croquis", ""),
    ("humid", "meteo", "humid", "humide (lourd)", "", ""),
    ("rain", "meteo", "rain, it's raining", "la pluie, il pleut", "croquis", ""),
    ("snow", "meteo", "snow", "la neige", "croquis", ""),
    ("windy", "meteo", "windy", "venteux", "croquis", ""),
    ("sunny", "meteo", "sunny", "ensoleillé", "croquis", ""),
    ("umbrella", "meteo", "an umbrella", "un parapluie", "croquis", ""),
    ("degrees", "meteo", "twenty degrees", "vingt degrés", "picto:thermo", "En Celsius au Canada, comme chez nous."),
    ("nice_day", "meteo", "Nice day, eh?", "Belle journée, hein ?", "", "Le « eh » canadien attend un oui."),

    # --- L'heure et les jours ------------------------------------------------
    ("oclock", "heure", "ten o'clock", "dix heures", "picto:h10", ""),
    ("quarter_past", "heure", "quarter past ten", "dix heures et quart", "picto:h1015", ""),
    ("half_past", "heure", "half past ten", "dix heures et demie", "picto:h1030", "On dit aussi « ten thirty »."),
    ("quarter_to", "heure", "quarter to ten", "dix heures moins quart", "picto:h0945", ""),
    ("am_pm", "heure", "a.m., p.m.", "le matin, l'après-midi ou le soir", "", "On ne dit pas « 21 h » : « nine p.m. »."),
    ("today", "heure", "today", "aujourd'hui", "", ""),
    ("tonight", "heure", "tonight", "ce soir", "", ""),
    ("tomorrow", "heure", "tomorrow", "demain", "", ""),
    ("weekend", "heure", "the weekend", "la fin de semaine", "", ""),
    ("monday", "heure", "Monday", "lundi", "", "Les jours prennent la majuscule en anglais."),
    ("last_ferry", "heure", "the last ferry", "le dernier traversier", "", ""),

    # --- Les gens, la politesse ----------------------------------------------
    ("hi", "gens", "Hi! How are you?", "Bonjour ! Comment ça va ?", "", "On répond « Good, thanks! And you? », même si ça va mal : c'est une salutation."),
    ("please", "gens", "please", "s'il vous plaît", "", ""),
    ("thanks", "gens", "thanks, thank you", "merci", "", ""),
    ("welcome", "gens", "You're welcome", "De rien", "", "On entend aussi « No problem », « No worries »."),
    ("sorry", "gens", "Sorry!", "Pardon !", "", "Dit à tout propos au Canada, même quand on vous bouscule."),
    ("excuse_me", "gens", "Excuse me…", "Excusez-moi… (pour attirer l'attention)", "", ""),
    ("again", "gens", "Sorry, could you say that again?", "Pardon, pouvez-vous répéter ?", "", ""),
    ("slowly", "gens", "more slowly, please", "plus lentement, s'il vous plaît", "", ""),
    ("spell", "gens", "Can you spell it?", "Pouvez-vous l'épeler ?", "", ""),
    ("dont_understand", "gens", "I don't understand", "Je ne comprends pas", "", ""),
    ("help", "gens", "Can you help me?", "Pouvez-vous m'aider ?", "", ""),
    ("assist", "gens", "to assist", "aider", "", "PIÈGE : « to assist » veut dire aider ; assister à un spectacle, c'est « to attend »."),
    ("attend", "gens", "to attend", "assister à", "", "PIÈGE : « to attend » n'est pas « attendre » (« to wait »)."),

    # --- Le petit bavardage --------------------------------------------------
    ("where_from", "jasette", "Where are you from?", "D'où venez-vous ?", "", ""),
    ("from_quebec", "jasette", "I'm from Quebec", "Je viens du Québec", "", "« Quebec » se dit « kwi-bec » ou « ké-bec » en anglais."),
    ("how_long", "jasette", "How long are you staying?", "Vous restez combien de temps ?", "", ""),
    ("first_time", "jasette", "Is it your first time in Toronto?", "C'est votre première fois à Toronto ?", "", ""),
    ("what_do_you_do", "jasette", "What do you do?", "Qu'est-ce que vous faites dans la vie ?", "", "La question porte sur le métier, pas sur l'instant."),
    ("seen", "jasette", "What have you seen so far?", "Qu'avez-vous vu jusqu'ici ?", "", ""),
    ("recommend", "jasette", "What would you recommend?", "Qu'est-ce que vous recommandez ?", "", ""),
    ("hockey", "jasette", "the Leafs, the Habs", "les Maple Leafs, le Canadien", "", "« The Habs » : le Canadien de Montréal ; un sujet de taquinerie sans fin."),
    ("actually", "jasette", "actually", "en fait", "", "PIÈGE : « actually » ne veut pas dire « actuellement » (« currently »)."),
    ("eventually", "jasette", "eventually", "finalement, un jour", "", "PIÈGE : « eventually » ne veut pas dire « éventuellement » (« maybe »)."),
    ("library", "jasette", "the library", "la bibliothèque", "croquis", "PIÈGE : « library » n'est pas une librairie (« bookstore »)."),
    ("sensible", "jasette", "sensible", "raisonnable", "", "PIÈGE : « sensible » veut dire raisonnable ; sensible se dit « sensitive »."),
    ("location", "jasette", "a nice location", "un bel emplacement", "", "PIÈGE : « location » est un endroit, jamais une location (« rental »)."),
    ("and_you", "jasette", "And you? How about you?", "Et vous ?", "", "La question qui relance : sans elle, la conversation s'arrête."),
    ("nice_to_meet", "jasette", "Nice to meet you", "Enchanté", "", ""),
    ("see_you", "jasette", "See you around! Take care!", "À la prochaine ! Prenez soin de vous !", "", ""),
]

# Chaque piège dans une phrase de voyage : (phrase, la bonne lecture, la fausse
# lecture du faux ami, un second choix, l'explication). La fausse lecture et le
# second choix ne doivent être justes dans AUCUNE variété d'anglais.
PIEGES = {
    "fare": ("The fare is three thirty.", "Le passage coûte 3,30 $.",
             "Il faut faire trois arrêts.", "Le métro passe à 3 h 30.",
             "« Fare » est le prix d'un trajet. Rien à voir avec le verbe faire."),
    "exit": ("Take the exit on the left.", "Prenez la sortie à gauche.",
             "Il y a un excès à gauche.", "Prenez l'entrée à gauche.",
             "« Exit » est la sortie ; l'entrée, c'est « the entrance »."),
    "room": ("Your room is on the fifth floor.", "Votre chambre est au cinquième étage.",
             "Votre rhum est au cinquième.", "Votre clé est au cinquième étage.",
             "« Room » est une chambre (ou une pièce). Le rhum se dit « rum »."),
    "deposit": ("We'll hold a hundred-dollar deposit on your card.", "On bloque 100 $ sur votre carte, remis au départ.",
                "On vous charge 100 $ de frais de dépôt de bagages.", "On vous rembourse 100 $ sur votre carte.",
                "Le « deposit » est une garantie bloquée sur la carte, libérée au départ."),
    "breakfast_incl": ("Breakfast is included, from seven to ten.", "Le déjeuner est inclus, de 7 h à 10 h.",
                       "Le dîner est inclus, de 7 h à 10 h.", "Le déjeuner coûte 7 $, jusqu'à 10 h.",
                       "« Breakfast » est le repas du matin : notre déjeuner. Le dîner du midi, c'est « lunch »."),
    "floor": ("The pool is on the first floor.", "La piscine est au rez-de-chaussée.",
              "La piscine est au premier étage, en haut de l'escalier.", "La piscine est au sous-sol.",
              "Au Canada, le « first floor » est le niveau de la rue ; le « second floor » est le premier étage."),
    "large": ("A large coffee, please.", "Un grand café, s'il vous plaît.",
              "Un café large et plat, s'il vous plaît.", "Un petit café, s'il vous plaît.",
              "« Large » veut dire grand. Large, au sens de la largeur, se dit « wide »."),
    "receipt": ("Do you want the receipt?", "Voulez-vous le reçu ?",
                "Voulez-vous la recette ?", "Voulez-vous un sac ?",
                "Le « receipt » est le reçu ; une recette de cuisine, c'est « a recipe »."),
    "appetizer": ("The entrées are on the right side of the menu.", "Les plats principaux sont à droite du menu.",
                  "Les entrées (soupes, salades) sont à droite du menu.", "Les desserts sont à droite du menu.",
                  "En Amérique du Nord, « entrée » désigne le plat principal ; notre entrée est un « appetizer »."),
    "dessert": ("Would you like to see the dessert menu?", "Voulez-vous voir la carte des desserts ?",
                "Voulez-vous voir le menu du désert ?", "Voulez-vous voir la carte des vins ?",
                "« Dessert » s'accentue à la fin ; « desert » (le désert), au début."),
    "the_bill": ("Can I get the bill, please?", "Pouvez-vous m'apporter l'addition ?",
                 "Puis-je avoir un billet de banque ?", "Puis-je avoir le menu ?",
                 "Au restaurant, « the bill » est l'addition. Un billet de banque se dit aussi « a bill », mais personne ne le demande au serveur."),
    "napkin": ("Could I get some napkins?", "Puis-je avoir des serviettes de table ?",
               "Puis-je avoir des couches ?", "Puis-je avoir des ustensiles ?",
               "« Napkin » est la serviette de table. Une couche se dit « diaper »."),
    "lunch": ("We're open for lunch at eleven.", "Nous ouvrons pour le dîner (le midi) à 11 h.",
              "Nous ouvrons pour le souper à 11 h.", "Nous ouvrons pour le déjeuner à 11 h du soir.",
              "« Lunch » est notre dîner, le repas du midi."),
    "dinner": ("Dinner is served until ten.", "Le souper est servi jusqu'à 22 h.",
               "Le dîner (le midi) est servi jusqu'à 10 h du matin.", "Le déjeuner est servi jusqu'à 10 h.",
               "« Dinner » est le repas du soir : notre souper."),
    "cash": ("Cash or card?", "Comptant ou carte ?",
             "À la caisse ou à la table ?", "Avec ou sans reçu ?",
             "« Cash » est l'argent comptant ; la caisse, c'est « the cash register » ou « the till »."),
    "quarter_coin": ("It's a quarter to seven.", "Il est sept heures moins quart.",
                     "Ça coûte 25 sous pour sept.", "Il est sept heures et quart.",
                     "« A quarter » est une pièce de 25 sous, mais dans l'heure c'est un quart d'heure : « a quarter to » = moins quart."),
    "change": ("Here's your change.", "Voici votre monnaie.",
               "Voici votre changement.", "Voici votre reçu.",
               "« Change » est la monnaie qu'on vous rend."),
    "thirteen": ("That's thirteen dollars.", "Ça fait 13 $.",
                 "Ça fait 30 $.", "Ça fait 3 $.",
                 "« ThirTEEN » : l'accent tombe à la fin. « THIRty » : au début."),
    "fifteen": ("Gate fifteen, on your left.", "La porte 15, à votre gauche.",
                "La porte 50, à votre gauche.", "La porte 5, à votre gauche.",
                "« FifTEEN » (15), l'accent à la fin ; « FIFty » (50), au début."),
    "line": ("Please wait in line behind the yellow sign.", "Faites la file derrière l'affiche jaune.",
             "Attendez sur la ligne jaune peinte au sol.", "Attendez dehors, près de l'affiche jaune.",
             "« The line », devant un guichet, c'est la file d'attente."),
    "bike": ("You can rent a bike by the hour.", "On peut louer un vélo à l'heure.",
             "On peut rentrer à vélo à toute heure.", "On peut acheter un vélo à l'heure.",
             "« To rent » veut dire louer."),
    "game": ("Are you going to the game tonight?", "Allez-vous au match ce soir ?",
             "Allez-vous jouer à un jeu ce soir ?", "Allez-vous au spectacle ce soir ?",
             "« The game », dit d'un soir précis, c'est le match."),
    "on_sale": ("These toques are on sale.", "Ces tuques sont en solde.",
                "Ces tuques sont sales.", "Ces tuques sont à vendre (sans rabais).",
                "« On sale » : en solde. « For sale » : à vendre."),
    "prescription": ("You don't need a prescription for that.", "Pas besoin d'ordonnance pour ça.",
                     "Ce n'est pas prescrit, c'est périmé.", "Il vous faut une ordonnance pour ça.",
                     "« Prescription » est l'ordonnance du médecin."),
    "drug": ("You'll find it at the drugstore.", "Vous le trouverez à la pharmacie.",
             "Vous le trouverez chez le revendeur de drogue.", "Vous le trouverez à l'épicerie.",
             "« Drugstore » est la pharmacie ; « drug » est d'abord un médicament."),
    "assist": ("Can I assist you?", "Puis-je vous aider ?",
               "Puis-je assister à votre réunion ?", "Puis-je vous accompagner ?",
               "« To assist » veut dire aider."),
    "attend": ("Are you attending the concert?", "Allez-vous assister au concert ?",
               "Attendez-vous le concert ?", "Organisez-vous le concert ?",
               "« To attend » : assister à. Attendre se dit « to wait »."),
    "actually": ("Actually, the museum is closed today.", "En fait, le musée est fermé aujourd'hui.",
                 "Actuellement, le musée est fermé (pour quelque temps).", "Heureusement, le musée est ouvert aujourd'hui.",
                 "« Actually » corrige ou précise : « en fait ». Actuellement se dit « currently »."),
    "eventually": ("Eventually, we found the hotel.", "Finalement, nous avons trouvé l'hôtel.",
                   "Éventuellement, nous trouverons l'hôtel.", "Rapidement, nous avons trouvé l'hôtel.",
                   "« Eventually » : à la fin, après un temps. Éventuellement se dit « possibly »."),
    "library": ("The library is free on Sundays.", "La bibliothèque est gratuite le dimanche.",
                "La librairie fait des rabais le dimanche.", "Le musée est gratuit le dimanche.",
                "« Library » : la bibliothèque. Une librairie est « a bookstore »."),
    "sensible": ("That's a sensible choice.", "C'est un choix raisonnable.",
                 "C'est un choix délicat, qui touche les émotions.", "C'est un choix cher.",
                 "« Sensible » veut dire raisonnable. Sensible, au sens français, se dit « sensitive »."),
    "location": ("The hotel has a great location.", "L'hôtel est très bien situé.",
                 "L'hôtel a une très bonne agence de location.", "L'hôtel a une très belle vue.",
                 "« Location » : l'emplacement. Une location de voiture, c'est « a rental »."),
}


def par_planche():
    g = {p[0]: [] for p in PLANCHES}
    for e in LEXIQUE:
        g[e[1]].append(e)
    return g


def verifier():
    ids = [e[0] for e in LEXIQUE]
    assert len(ids) == len(set(ids)), "identifiant en double"
    planches = {p[0] for p in PLANCHES}
    for e in LEXIQUE:
        assert len(e) == 6, e
        assert e[1] in planches, f"{e[0]} : planche inconnue {e[1]}"
        assert e[4] in ("croquis", "") or e[4].startswith("picto:"), e
        if e[5].startswith("PIÈGE"):
            assert e[0] in PIEGES, f"{e[0]} : piège sans phrase"
    for i, t in PIEGES.items():
        assert i in ids, f"piège {i} absent du lexique"
        assert len(t) == 5 and all(t), f"{i} : phrase, bonne, fausse, seconde, explication"
        assert len(set(t[1:4])) == 3, f"{i} : deux choix identiques"
    return True


if __name__ == "__main__":
    verifier()
    from collections import Counter
    c = Counter(e[1] for e in LEXIQUE)
    for p, fr, _ in PLANCHES:
        print(f"  {fr:28} {c[p]:3}")
    print(f"{len(LEXIQUE)} mots, {sum(1 for e in LEXIQUE if e[4]=='croquis')} croquis, "
          f"{len(PIEGES)} pièges")
