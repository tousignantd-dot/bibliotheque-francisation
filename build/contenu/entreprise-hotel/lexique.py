"""Le lexique de la réception d'hôtel — source unique, en trois langues.

Tout ce qui viendra après (planches, comptoir, exercices, voix, test) se lit
ICI. Rien ne se recopie ailleurs à la main.

CHAQUE ENTRÉE : (id, planche, fr, en, es, dessin, note)

- `fr`, `en`, `es` : le mot tel qu'on le dit au comptoir, dans les variétés
  décidées le 24 septembre 2026 — français du Québec, anglais nord-américain,
  espagnol du Mexique. Les trois sont à égalité : chacune peut être la langue
  apprise, chacune la langue de l'employé.
- `dessin` : "croquis" (engendré seul, fond blanc), "comptoir" (l'objet vit
  dans le grand dessin du comptoir, et s'y touche), "" (sans image : une
  formule, une heure, un mot de service).
- `note` : ce que le réceptionniste doit savoir, en français (la page de
  validation est pour Daniel). Une note qui commence par `PIÈGE (xx·yy)` est un
  faux ami ou un double sens ENTRE CES DEUX LANGUES : la série des pièges d'une
  direction ne montre que ceux de sa paire.

BROUILLON du 24 septembre 2026, à confronter à une vraie réception.
"""

PLANCHES = [
    ("arrivee",   "L'arrivée"),
    ("chambre",   "La chambre"),
    ("services",  "Les services"),
    ("paiement",  "Le paiement"),
    ("temps",     "Les heures et les dates"),
    ("problemes", "Les problèmes"),
    ("vacances",  "Les vacances"),
    ("politesse", "La politesse du comptoir"),
    ("comptoir",  "Le comptoir (volet 2)"),
]

C, K, N = "croquis", "comptoir", ""
LANGUES = ("fr", "en", "es")

LEXIQUE = [
    # ── L'arrivée ────────────────────────────────────────────────────────
    ("reservation",   "arrivee", "une réservation", "a reservation", "una reservación", N, "Au Mexique « reservación » ; « reserva » (Espagne) s'entend aussi."),
    ("confirmation",  "arrivee", "un numéro de confirmation", "a confirmation number", "un número de confirmación", N, ""),
    ("piece-identite","arrivee", "une pièce d'identité", "a photo ID", "una identificación oficial", C, "Au Mexique, la carte d'électeur (INE) sert de pièce d'identité."),
    ("passeport",     "arrivee", "un passeport", "a passport", "un pasaporte", C, ""),
    ("permis",        "arrivee", "un permis de conduire", "a driver's license", "una licencia de manejo", C, ""),
    ("carte-credit",  "arrivee", "une carte de crédit", "a credit card", "una tarjeta de crédito", C, ""),
    ("carte-cle",     "arrivee", "une carte-clé", "a key card", "una tarjeta llave", C, "On dit aussi « la clé » tout court, dans les trois langues."),
    ("pochette",      "arrivee", "une pochette de carte-clé", "a key card sleeve", "un sobre para la tarjeta", C, "On y écrit le numéro de la chambre, jamais sur la carte."),
    ("fiche",         "arrivee", "une fiche d'inscription", "a registration card", "una tarjeta de registro", C, ""),
    ("stylo",         "arrivee", "un stylo", "a pen", "una pluma", C, "PIÈGE (fr·es) : au Mexique, « una pluma » est d'abord un stylo (c'est aussi une plume d'oiseau) ; au comptoir, c'est le stylo."),
    ("signature",     "arrivee", "signer ici", "to sign here", "firmar aquí", N, ""),
    ("bagages",       "arrivee", "des bagages", "luggage", "el equipaje", C, "En anglais, « luggage » ne prend pas de s : on ne dit jamais « a luggage »."),
    ("valise",        "arrivee", "une valise", "a suitcase", "una maleta", C, ""),
    ("chariot",       "arrivee", "un chariot à bagages", "a luggage cart", "un carrito para equipaje", C, ""),
    ("enregistrement","arrivee", "l'arrivée (l'enregistrement)", "check-in", "el registro (el check-in)", N, "Au Québec comme au Mexique, « le check-in » s'entend partout."),
    ("prenom",        "arrivee", "le prénom", "the first name", "el nombre", N, "PIÈGE (fr·es) : « el nombre » est le PRÉNOM ; « le nom » français est « el apellido »."),
    ("nom-famille",   "arrivee", "le nom de famille", "the last name", "el apellido", N, "Un Mexicain en porte souvent DEUX (paternel, maternel) : la réservation est sous le premier."),
    ("courriel",      "arrivee", "l'adresse courriel", "the email address", "el correo electrónico", N, "Au Québec « courriel » ; l'arobase se dit « a commercial », « at », « arroba »."),

    # ── La chambre ───────────────────────────────────────────────────────
    ("chambre",       "chambre", "une chambre", "a room", "una habitación", N, "Au Mexique, « un cuarto » aussi — et « cuarto » veut aussi dire « quart »."),
    ("lit-simple",    "chambre", "un lit simple", "a twin bed", "una cama individual", C, "En anglais nord-américain, le lit simple est un « twin »."),
    ("lit-double",    "chambre", "un lit double", "a double bed", "una cama matrimonial", C, "PIÈGE (fr·en) : « a double room » est une chambre pour deux — un grand lit ou deux lits : on demande « one bed or two? ». « A full bed » s'entend aussi, surtout en magasin."),
    ("lit-queen",     "chambre", "un lit queen", "a queen bed", "una cama queen", C, "Au comptoir, les trois langues disent « queen » et « king »."),
    ("lit-king",      "chambre", "un lit king", "a king bed", "una cama king size", C, ""),
    ("lit-appoint",   "chambre", "un lit d'appoint", "a rollaway bed", "una cama extra", C, ""),
    ("berceau",       "chambre", "un lit de bébé", "a crib", "una cuna", C, "Un « cot » en anglais nord-américain est un lit de camp, pas un lit de bébé."),
    ("vue",           "chambre", "la vue", "the view", "la vista", N, ""),
    ("etage",         "chambre", "l'étage", "the floor", "el piso", N, "PIÈGE (fr·en) : aux États-Unis, « the first floor » est le rez-de-chaussée ; au Mexique, c'est « la planta baja »."),
    ("ascenseur",     "chambre", "l'ascenseur", "the elevator", "el elevador", C, "Au Mexique « elevador » ; « ascensor » en Espagne."),
    ("sortie",        "chambre", "la sortie", "the exit", "la salida", C, "PIÈGE (es·en) : « éxito » veut dire succès, pas sortie."),
    ("escalier",      "chambre", "l'escalier", "the stairs", "las escaleras", C, ""),
    ("climatiseur",   "chambre", "l'air climatisé", "the air conditioning", "el aire acondicionado", C, "Au Québec « l'air climatisé » ou « la clim » ; en anglais « the A/C »."),
    ("chauffage",     "chambre", "le chauffage", "the heat", "la calefacción", N, ""),
    ("coffre-fort",   "chambre", "le coffre-fort", "the safe", "la caja fuerte", C, ""),
    ("minibar",       "chambre", "le minibar", "the minibar", "el frigobar", C, "Au Mexique « el frigobar »."),
    ("serviettes",    "chambre", "des serviettes", "towels", "toallas", C, "PIÈGE (fr·es) : au bain, ce sont des « toallas » ; « servilletas » sont les serviettes de table (au Québec, « serviette » peut dire les deux)."),
    ("oreiller",      "chambre", "un oreiller", "a pillow", "una almohada", C, ""),
    ("couverture",    "chambre", "une couverture", "a blanket", "una cobija", C, "Au Québec « une couverte » s'entend ; au Mexique « cobija », en Espagne « manta »."),
    ("sechoir",       "chambre", "un séchoir à cheveux", "a hair dryer", "una secadora de pelo", C, "Au Québec « séchoir » ; « sèche-cheveux » en France."),
    ("fer",           "chambre", "un fer à repasser", "an iron", "una plancha", C, ""),
    ("telecommande",  "chambre", "la télécommande", "the remote", "el control remoto", C, "Au Québec on entend aussi « la manette »."),
    ("douche",        "chambre", "la douche", "the shower", "la regadera", C, "Au Mexique « la regadera » ; « la ducha » ailleurs."),
    ("bain",          "chambre", "le bain", "the bathtub", "la tina", C, "Au Québec « le bain » est aussi la baignoire."),
    ("non-fumeur",    "chambre", "une chambre non-fumeur", "a non-smoking room", "una habitación de no fumar", N, ""),

    # ── Les services ─────────────────────────────────────────────────────
    ("dejeuner",      "services", "le déjeuner", "breakfast", "el desayuno", C, "PIÈGE (fr·en) : au Québec le déjeuner est le repas du MATIN ; « lunch », c'est le dîner."),
    ("diner",         "services", "le dîner", "lunch", "la comida", N, "PIÈGE (fr·es) : au Mexique « la comida » est le repas du midi (vers 14 h), pas la nourriture seulement."),
    ("souper",        "services", "le souper", "dinner", "la cena", N, "PIÈGE (fr·en) : « dinner » est le repas du soir — le souper, pas le dîner québécois."),
    ("stationnement", "services", "le stationnement", "parking", "el estacionamiento", C, "Au Québec « stationnement » ; « parking » en France."),
    ("voiturier",     "services", "le service de voiturier", "valet parking", "el valet parking", N, ""),
    ("wifi",          "services", "le wifi", "the Wi-Fi", "el wifi", N, ""),
    ("mot-passe",     "services", "le mot de passe", "the password", "la contraseña", N, ""),
    ("piscine",       "services", "la piscine", "the pool", "la alberca", C, "Au Mexique « la alberca » ; « la piscina » ailleurs."),
    ("gym",           "services", "la salle d'entraînement", "the fitness center", "el gimnasio", C, "Au Québec « le gym » ; en anglais « the gym » aussi."),
    ("navette",       "services", "la navette", "the shuttle", "el transporte", C, "Au Mexique on entend « el shuttle »."),
    ("reveil",        "services", "un appel de réveil", "a wake-up call", "una llamada para despertar", N, ""),
    ("bagagiste",     "services", "le bagagiste", "the bellhop", "el botones", C, "« El botones » est singulier malgré le s."),
    ("entretien",     "services", "l'entretien ménager", "housekeeping", "el servicio de limpieza", N, "Au Mexique la femme de chambre est « la camarista »."),
    ("buanderie",     "services", "la buanderie", "the laundry room", "la lavandería", N, ""),
    ("glace",         "services", "la machine à glace", "the ice machine", "la máquina de hielo", C, "Au Québec « la glace », ce sont les glaçons."),
    ("distributrice", "services", "la machine distributrice", "the vending machine", "la máquina expendedora", C, "Au Québec « la distributrice »."),
    ("salle-reunion", "services", "la salle de réunion", "the meeting room", "la sala de juntas", N, "Au Mexique « sala de juntas »."),
    ("consigne",      "services", "la consigne à bagages", "luggage storage", "la guarda de equipaje", N, "Le client arrivé tôt, ou parti mais pas encore à l'aéroport."),

    # ── Le paiement ──────────────────────────────────────────────────────
    ("tarif",         "paiement", "le tarif", "the rate", "la tarifa", N, ""),
    ("taxes",         "paiement", "les taxes", "the taxes", "los impuestos", N, "Au Québec : TPS, TVQ et la taxe sur l'hébergement."),
    ("depot",         "paiement", "le dépôt", "the deposit", "el depósito", N, "PIÈGE (fr·en) : la « caution » française est un dépôt ; « caution » anglais veut dire prudence."),
    ("frais",         "paiement", "des frais", "a fee", "un cargo", N, "PIÈGE (fr·es) : « un cargo » est un frais porté à la note, pas un navire."),
    ("facture",       "paiement", "la facture", "the bill", "la cuenta", N, "PIÈGE (fr·es) : au Mexique « la factura » est une facture FISCALE, avec le numéro RFC ; la note, c'est « la cuenta »."),
    ("recu",          "paiement", "le reçu", "the receipt", "el recibo", C, ""),
    ("remboursement", "paiement", "un remboursement", "a refund", "un reembolso", N, ""),
    ("annulation",    "paiement", "une annulation", "a cancellation", "una cancelación", N, ""),
    ("carte-refusee", "paiement", "une carte refusée", "a declined card", "una tarjeta rechazada", N, ""),
    ("comptant",      "paiement", "l'argent comptant", "cash", "el efectivo", C, "Au Québec « payer comptant » ; « en espèces » en France."),
    ("debit",         "paiement", "la carte de débit", "a debit card", "una tarjeta de débito", N, "Au Québec on dit aussi « payer par Interac »."),
    ("monnaie",       "paiement", "de la monnaie", "change", "el cambio", N, "PIÈGE (fr·en) : « la monnaie », ce sont les pièces qu'on rend (« change ») ; l'argent, c'est « money »."),
    ("pourboire",     "paiement", "le pourboire", "the tip", "la propina", N, ""),
    ("surclassement", "paiement", "un surclassement", "an upgrade", "un upgrade", N, "Au Mexique « un upgrade » ou « una mejora de habitación »."),
    ("nuitee",        "paiement", "le prix par nuit", "the nightly rate", "el precio por noche", N, ""),

    # ── Les heures et les dates ──────────────────────────────────────────
    ("heure-arrivee", "temps", "l'heure d'arrivée", "check-in time", "la hora de entrada", N, "« À 15 h » se dit « at 3 p.m. » et « a las tres de la tarde » : l'anglais ne compte pas sur 24 heures."),
    ("heure-depart",  "temps", "l'heure de départ", "check-out time", "la hora de salida", N, ""),
    ("depart-tardif", "temps", "un départ tardif", "a late check-out", "una salida tardía", N, ""),
    ("arrivee-hative","temps", "une arrivée hâtive", "an early check-in", "una entrada anticipada", N, "Au Québec « hâtive » ; « anticipée » en France."),
    ("nuit",          "temps", "une nuit", "a night", "una noche", N, "« Pour trois nuits » : c'est le compte que le client donne."),
    ("semaine",       "temps", "une semaine", "a week", "una semana", N, ""),
    ("fin-semaine",   "temps", "la fin de semaine", "the weekend", "el fin de semana", N, "Au Québec « la fin de semaine » ; « le week-end » en France."),
    ("aujourdhui",    "temps", "aujourd'hui", "today", "hoy", N, ""),
    ("demain",        "temps", "demain", "tomorrow", "mañana", N, "« Mañana » veut aussi dire « le matin » : « mañana en la mañana » = demain matin."),
    ("hier",          "temps", "hier", "yesterday", "ayer", N, ""),
    ("matin",         "temps", "le matin", "the morning", "la mañana", N, ""),
    ("apres-midi",    "temps", "l'après-midi", "the afternoon", "la tarde", N, "« Tarde » va jusqu'à la tombée du jour ; « buenas tardes » se dit encore à 19 h."),
    ("soir",          "temps", "le soir", "the evening", "la noche", N, ""),
    ("midi",          "temps", "midi", "noon", "mediodía", N, ""),
    ("maintenant",    "temps", "en ce moment", "right now", "en este momento", N, "PIÈGE (es·en) : « actually » veut dire « en realidad », jamais « actualmente »."),
    ("minuit",        "temps", "minuit", "midnight", "medianoche", N, ""),
    ("date",          "temps", "la date", "the date", "la fecha", N, "PIÈGE (fr·en) : 04/05 est le 4 mai ici et au Mexique, mais le 5 avril aux États-Unis. Toujours dire le mois en lettres."),
    ("no-chambre",    "temps", "le numéro de chambre", "the room number", "el número de habitación", N, "« La 412 » : « four-twelve » en anglais, « cuatrocientos doce » en espagnol."),

    # ── Les problèmes ────────────────────────────────────────────────────
    ("bruit",         "problemes", "du bruit", "noise", "ruido", N, ""),
    ("cle-bloquee",   "problemes", "la clé ne fonctionne pas", "the key doesn't work", "la llave no funciona", N, "Le plus fréquent : la carte démagnétisée, à réencoder."),
    ("eau-chaude",    "problemes", "il n'y a pas d'eau chaude", "there's no hot water", "no hay agua caliente", N, ""),
    ("pas-prete",     "problemes", "la chambre n'est pas prête", "the room isn't ready", "la habitación no está lista", N, ""),
    ("complet",       "problemes", "l'hôtel est complet", "we're fully booked", "no tenemos disponibilidad", N, ""),
    ("surreservation","problemes", "une surréservation", "an overbooking", "una sobreventa", N, "Les trois langues disent aussi « overbooking »."),
    ("fuite",         "problemes", "une fuite d'eau", "a leak", "una fuga de agua", C, ""),
    ("toilette",      "problemes", "la toilette est bouchée", "the toilet is clogged", "el baño está tapado", N, ""),
    ("ampoule",       "problemes", "une ampoule brûlée", "a burned-out light bulb", "un foco fundido", C, "Au Mexique « un foco »."),
    ("plainte",       "problemes", "une plainte", "a complaint", "una queja", N, ""),
    ("objets-perdus", "problemes", "les objets perdus", "the lost and found", "los objetos perdidos", N, ""),
    ("malade",        "problemes", "avoir le rhume", "to have a cold", "estar resfriado", N, "PIÈGE (es·en) : « estoy constipado » veut dire « j'ai le rhume », pas « constipated »."),
    ("pharmacie",     "problemes", "la pharmacie", "the pharmacy", "la farmacia", C, "En anglais nord-américain on dit aussi « the drugstore »."),
    ("gerant",        "problemes", "le gérant", "the manager", "el gerente", N, "Celui à qui revient ce que la réception ne décide pas seule."),
    ("embarrasse",    "problemes", "je suis gêné", "I'm embarrassed", "me da pena", N, "PIÈGE (es·en) : « estoy embarazada » veut dire « je suis enceinte »."),

    # ── Les vacances ─────────────────────────────────────────────────────
    ("plage",         "vacances", "la plage", "the beach", "la playa", C, ""),
    ("excursion",     "vacances", "une excursion", "a tour", "un tour", N, ""),
    ("musee",         "vacances", "un musée", "a museum", "un museo", C, ""),
    ("restaurant",    "vacances", "un restaurant", "a restaurant", "un restaurante", C, ""),
    ("location-auto", "vacances", "la location d'auto", "the car rental", "la renta de autos", N, "PIÈGE (fr·en) : « location » en anglais veut dire « endroit » ; au Mexique, louer se dit « rentar »."),
    ("plan-ville",    "vacances", "le plan de la ville", "the city map", "el mapa de la ciudad", K, ""),
    ("depliant",      "vacances", "un dépliant", "a brochure", "un folleto", K, ""),
    ("billet",        "vacances", "un billet", "a ticket", "un boleto", C, "PIÈGE (fr·en) : « a bill » est une facture ou un billet de banque, jamais un billet de spectacle."),
    ("meteo",         "vacances", "la météo", "the weather forecast", "el pronóstico del tiempo", N, ""),
    ("autobus",       "vacances", "l'autobus", "the bus", "el camión", C, "PIÈGE (fr·es) : au Mexique, « el camión » est d'abord l'autobus (c'est aussi un camion de marchandises) ; pour un touriste, c'est l'autobus."),
    ("metro",         "vacances", "le métro", "the subway", "el metro", C, ""),
    ("taxi",          "vacances", "un taxi", "a cab", "un taxi", C, ""),
    ("aeroport",      "vacances", "l'aéroport", "the airport", "el aeropuerto", C, ""),
    ("centre-ville",  "vacances", "le centre-ville", "downtown", "el centro", N, ""),
    ("a-pied",        "vacances", "à distance de marche", "within walking distance", "a unos pasos", N, ""),
    ("droite",        "vacances", "à droite", "to the right", "a la derecha", N, ""),
    ("gauche",        "vacances", "à gauche", "to the left", "a la izquierda", N, ""),
    ("tout-droit",    "vacances", "tout droit", "straight ahead", "todo derecho", N, "PIÈGE (fr·es) : « derecho » (tout droit) n'est pas « derecha » (à droite) — une lettre de différence."),

    # ── La politesse du comptoir ─────────────────────────────────────────
    ("bienvenue",     "politesse", "Bienvenue!", "Welcome!", "¡Bienvenido!", N, "En espagnol l'accord suit le client : bienvenida, bienvenidos."),
    ("bonjour",       "politesse", "Bonjour!", "Good morning!", "¡Buenos días!", N, "L'anglais et l'espagnol changent de salutation à midi : good afternoon, buenas tardes."),
    ("aider",         "politesse", "Comment puis-je vous aider?", "How can I help you?", "¿En qué le puedo ayudar?", N, ""),
    ("instant",       "politesse", "Un instant, s'il vous plaît.", "One moment, please.", "Un momento, por favor.", N, ""),
    ("epeler",        "politesse", "Pouvez-vous épeler votre nom?", "Could you spell your last name?", "¿Me puede deletrear su apellido?", N, "Le geste le plus fréquent du comptoir ; au téléphone, il ne se rate pas."),
    ("repeter",       "politesse", "Pouvez-vous répéter?", "Could you repeat that?", "¿Me lo puede repetir?", N, ""),
    ("desole",        "politesse", "Je suis désolé.", "I'm sorry.", "Lo siento.", N, "« Disculpe » pour interrompre ; « lo siento » pour s'excuser d'un tort."),
    ("patience",      "politesse", "Merci de votre patience.", "Thank you for your patience.", "Gracias por su paciencia.", N, ""),
    ("voici-cle",     "politesse", "Voici votre clé.", "Here is your key.", "Aquí tiene su llave.", N, ""),
    ("autre-chose",   "politesse", "Autre chose?", "Anything else?", "¿Algo más?", N, ""),
    ("bon-sejour",    "politesse", "Bon séjour!", "Enjoy your stay!", "¡Que disfrute su estancia!", N, ""),
    ("bonne-journee", "politesse", "Bonne journée!", "Have a nice day!", "¡Que tenga buen día!", N, ""),
    ("vous",          "politesse", "vous", "you (sir, ma'am)", "usted", N, "L'anglais n'a pas de « vous » : la politesse passe par « could you », « sir », « ma'am ». En espagnol, « usted » et le verbe à la 3e personne."),
    ("monsieur",      "politesse", "Monsieur, Madame", "sir, ma'am", "señor, señora", N, ""),

    # ── Le comptoir : les objets du grand dessin (volet 2) ───────────────
    ("ecran",         "comptoir", "l'écran", "the screen", "la pantalla", K, ""),
    ("terminal",      "comptoir", "le terminal de paiement", "the card reader", "la terminal", K, "En espagnol « la terminal » est féminin."),
    ("encodeur",      "comptoir", "l'encodeur de clés", "the key card encoder", "el codificador de llaves", K, ""),
    ("sonnette",      "comptoir", "la sonnette", "the desk bell", "el timbre", K, ""),
    ("telephone",     "comptoir", "le téléphone", "the phone", "el teléfono", K, ""),
    ("horloges",      "comptoir", "les horloges", "the clocks", "los relojes", K, ""),
    ("imprimante",    "comptoir", "l'imprimante", "the printer", "la impresora", K, ""),
    ("presentoir",    "comptoir", "le présentoir", "the brochure rack", "el exhibidor", K, ""),
    ("bureau-gerant", "comptoir", "le bureau du gérant", "the manager's office", "la oficina del gerente", K, ""),
    ("tiroir-caisse", "comptoir", "le tiroir-caisse", "the cash drawer", "la caja", K, ""),
    ("dossier",       "comptoir", "la chemise (le dossier)", "the folder", "la carpeta", K, "PIÈGE (es·en) : « carpet » est un tapis ; « la carpeta » est une chemise à documents."),
    ("hall",          "comptoir", "le hall", "the lobby", "el lobby", K, "Au Québec on dit aussi « le lobby »."),
]


def par_planche():
    g = {k: [] for k, _ in PLANCHES}
    for e in LEXIQUE:
        g[e[1]].append(e)
    return g


def pieges(paire=None):
    """Les entrées piégées, toutes ou celles d'une paire (« fr·es »)."""
    out = []
    for e in LEXIQUE:
        n = e[6]
        if n.startswith("PIÈGE ("):
            p = n[len("PIÈGE ("):n.index(")")]
            if paire is None or set(p.split("·")) == set(paire.split("·")):
                out.append(e)
    return out


def verifier():
    ids = [e[0] for e in LEXIQUE]
    doublons = {i for i in ids if ids.count(i) > 1}
    assert not doublons, f"identifiants en double : {doublons}"
    planches = {k for k, _ in PLANCHES}
    for e in LEXIQUE:
        assert len(e) == 7, e
        assert e[1] in planches, f"{e[0]} : planche inconnue {e[1]}"
        assert all(e[2:5]), f"{e[0]} : une langue manque"
        assert e[5] in ("croquis", "comptoir", ""), f"{e[0]} : dessin {e[5]!r}"
        if e[6].startswith("PIÈGE"):
            p = e[6][len("PIÈGE ("):e[6].index(")")].split("·")
            assert len(p) == 2 and set(p) <= set(LANGUES), f"{e[0]} : paire {p}"
    return True


if __name__ == "__main__":
    verifier()
    g = par_planche()
    for k, t in PLANCHES:
        print(f"  {t:30} {len(g[k]):3}")
    print(f"{len(LEXIQUE)} mots · {sum(e[5] == 'croquis' for e in LEXIQUE)} croquis · "
          f"{sum(e[5] == 'comptoir' for e in LEXIQUE)} au comptoir · {len(pieges())} pièges")
    for p in ("fr·en", "fr·es", "es·en"):
        print(f"  pièges {p} : {len(pieges(p))}")
