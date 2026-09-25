"""Les exercices de la réception (étape 2) — le contenu, dans les trois langues.

Quatre familles reprises de la Maison Francœur se construisent seules à partir
du lexique (« Je l'entends, je le trouve », « Le mot et son image », « Je me
souviens ») ou de `PIEGES_FAUX` ci-dessous. Quatre sont propres à la
réception et s'écrivent ici, une fois par langue apprise :

- ÉPELER UN NOM (objectif O2) : un client épelle son nom, l'employé l'écrit.
- LES NOMBRES ET LES HEURES (O2) : un numéro de chambre, un prix, une heure ;
  les choix sont écrits en chiffres, donc les mêmes pour toutes les langues.
- CE QUE LE CLIENT VEUT (O1) : une demande au débit d'un client ; le lit ET
  le nombre de nuits décident ensemble (le « trait qui décide » de Francœur).
- CE QUE JE RÉPONDS (O3, O4) : la réplique du réceptionniste ; chaque mauvais
  choix a sa rétroaction, dans la langue de l'employé.

Tout texte dit par un client est dans la langue APPRISE ; toute rétroaction est
dans la langue PARLÉE. Écrit à la main, à faire relire par un locuteur.
"""

# ── La série des pièges (révisée au tour 1 de l'audit, D4 bloquant) ─────
# Un faux ami montré SEUL était souvent vrai aussi (« a ticket » EST une
# contravention, « the floor » EST le plancher) : une réponse juste était
# marquée fausse. Chaque item pose donc le mot DANS UNE PHRASE de comptoir, qui
# fixe le sens. Pour un piège de la paire (a·b), un item par interface qui a
# une fausse lecture : la phrase est dans la langue APPRISE, la fausse lecture
# et l'explication dans la langue de l'INTERFACE.
#   PIEGES[id][interface] = (phrase dans la langue apprise, fausse lecture,
#                            second distracteur, explication)
# Le second distracteur est écrit à la main, plausible dans la phrase (tour 2 :
# tiré au hasard, il était absurde et la bonne se devinait). Relire chaque
# fausse lecture : serait-elle vraie dans UNE variété de la langue de l'employé ?
# (« une plume » = un stylo au Québec ; « le dîner » = le souper en France.)
PIEGES = {
    "souper": {
        "fr": ('The restaurant serves dinner from six to ten.',
               'le repas du midi', 'le déjeuner',
               'Le soir, « dinner » est le souper. Attention : au Québec, « le dîner » est le repas du midi.'),
    },
    "dejeuner": {
        "en": ('Le déjeuner est servi de sept heures à dix heures.',
               'lunch', 'brunch',
               'From seven to ten: in Québec, « le déjeuner » is breakfast. Lunch is « le dîner ».'),
    },
    "billet": {
        "fr": ("Your ticket for tonight's show is at the front desk.",
               'une contravention', 'un reçu',
               "Un billet de spectacle : ici, « ticket » n'est pas une contravention."),
        "en": ('Votre billet pour le spectacle est à la réception.',
               'a bill', 'a receipt',
               'A show ticket: « un billet » is not a bill to pay (« la facture »).'),
    },
    "etage": {
        "fr": ('Your room is on the twelfth floor.',
               'le plancher', "l'aile",
               "Une chambre au douzième : « floor », c'est ici l'étage, pas le plancher."),
    },
    "monnaie": {
        "fr": ("Here's your change: two dollars and fifty cents.",
               'un changement', 'un pourboire',
               "Deux dollars cinquante : « change », c'est la monnaie qu'on rend."),
        "en": ('Voici votre monnaie : deux dollars cinquante.',
               'money', 'a tip',
               "Two fifty handed back: « la monnaie » is change, not money (« l'argent »)."),
    },
    "depot": {
        "en": ('Nous prenons un dépôt de cent dollars sur votre carte.',
               'a warehouse', 'a fee',
               'A hundred dollars on your card: « un dépôt » is a deposit, not a warehouse.'),
    },
    "location-auto": {
        "en": ("Pour la location d'auto, il faut un permis de conduire.",
               "the car's location", 'the car wash',
               'You need a licence for it: « la location » is a rental, not a place.'),
    },
    "stylo": {
        "fr": ('Firme aquí, por favor. Aquí tiene una pluma.',
               "une plume d'oiseau", 'un formulaire',
               "Pour signer : au Mexique, « una pluma » est d'abord un stylo."),
    },
    "prenom": {
        "fr": ('¿Me dice su nombre? Su apellido ya lo tengo.',
               'le nom de famille', 'le surnom',
               "« Nombre », c'est le prénom ; le nom de famille, c'est « el apellido »."),
        "es": ("Votre prénom, s'il vous plaît? J'ai déjà votre nom de famille.",
               'el apellido', 'el apodo',
               '« Le prénom » es el nombre de pila; el apellido es « le nom de famille ».'),
    },
    "serviettes": {
        "es": ('Je vous monte des serviettes propres pour la douche.',
               'servilletas', 'sábanas',
               'Para la regadera: « des serviettes » son toallas, no servilletas.'),
    },
    "diner": {
        "fr": ('La comida se sirve de una a cuatro de la tarde.',
               'le souper', 'la collation',
               'De une heure à quatre heures : au Mexique, « la comida » est le repas du midi.'),
        "es": ('Le dîner est servi de midi à quatorze heures.',
               'la cena', 'el desayuno',
               'De doce a dos: en Quebec, « le dîner » es la comida del mediodía, no la cena.'),
    },
    "frais": {
        "fr": ('Hay un cargo de veinte dólares por el estacionamiento.',
               'un navire de charge', 'un pourboire',
               'Vingt dollars pour le stationnement : « un cargo » est un frais.'),
        "es": ('Il y a des frais de vingt dollars pour le stationnement.',
               'algo fresco', 'una propina',
               'Veinte dólares: « des frais » es un cargo, no algo fresco.'),
    },
    "facture": {
        "fr": ('Aquí tiene la cuenta de su estancia.',
               'le compte en banque', 'le reçu',
               "Pour un séjour : « la cuenta », c'est la facture de l'hôtel."),
    },
    "autobus": {
        "fr": ('El camión al centro pasa enfrente del hotel cada diez minutos.',
               'un camion', 'le taxi',
               "Toutes les dix minutes vers le centre : au Mexique, « el camión » est d'abord l'autobus."),
    },
    "tout-droit": {
        "fr": ('El museo está todo derecho, a dos cuadras.',
               'à droite', 'à gauche',
               "« Todo derecho », c'est tout droit ; à droite se dit « a la derecha »."),
        "es": ('Le musée est tout droit, à deux coins de rue.',
               'a la derecha', 'a la izquierda',
               '« Tout droit » es todo derecho; a la derecha es « à droite ».'),
    },
    "sortie": {
        "es": ('The emergency exit is at the end of the hall.',
               'el éxito', 'la escalera',
               'Al fondo del pasillo: « exit » es la salida; « éxito » en inglés es « success ».'),
    },
    "embarrasse": {
        "es": ("I'm so embarrassed, I forgot my wallet.",
               'estoy embarazada', 'estoy enojado',
               'Olvidó su cartera: « embarrassed » es « me da pena ». « Embarazada » es « pregnant ».'),
        "en": ('Me da pena, olvidé mi cartera.',
               'it hurts me', "I'm angry",
               "She forgot her wallet: « me da pena » means I'm embarrassed."),
    },
    "dossier": {
        "en": ('Su confirmación está en esta carpeta.',
               'the carpet', 'the envelope',
               'A confirmation inside it: « la carpeta » is a folder, not a carpet.'),
    },
}

# ── Épeler un nom (révisé au tour 1, D2) ─────────────────────────────────
# Des noms comme on en entend : accentué, composé, lettre doublée, deux
# apellidos. L'épellation s'ASSEMBLE à partir des lettres validées une à une
# (build/hotel_lettres.py), au débit d'un client, et la moitié des items passe
# par le filtre du téléphone.
NOMS = ["TREMBLAY", "NGUYEN", "OKAFOR", "MORENO", "GAUTHIER", "WHITFIELD", "KOWALSKI", "LACHANCE",
        "BÉLANGER", "SAINT-PIERRE", "HAMMOND", "GARCÍA LÓPEZ"]
TELEPHONE = {"NGUYEN", "GAUTHIER", "KOWALSKI", "SAINT-PIERRE", "HAMMOND", "GARCÍA LÓPEZ"}

# Le nom des lettres, ÉCRIT dans chaque langue : une lettre nue se fait dire à
# l'anglaise par la synthèse française (mémoire epellation-azure-anglaise).
LETTRES = {
    "fr": dict(zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ",
               ["a", "bé", "cé", "dé", "eu", "effe", "gé", "ache", "i", "ji", "ka", "elle", "emme",
                "enne", "o", "pé", "ku", "erre", "esse", "té", "u", "vé", "double vé", "ixe",
                "i grec", "zède"])),
    "es": dict(zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ",
               ["a", "be", "ce", "de", "e", "efe", "ge", "hache", "i", "jota", "ka", "ele", "eme",
                "ene", "o", "pe", "cu", "erre", "ese", "te", "u", "ve", "doble u", "equis",
                "i griega", "zeta"])),
    "en": {c: c for c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"},
}
# Au Mexique, B et V se prononcent pareil : on dit toujours lequel.
ANCRES = {"es": {"B": "be grande", "V": "ve chica"}}
# Les signes qui ne sont pas des lettres, dits comme au comptoir.
SIGNES = {
    "fr": {"accent_aigu": "accent aigu", "accent_grave": "accent grave", "trait": "trait d'union",
           "espace": "en deux mots", "double": "deux {l}"},
    "en": {"accent_aigu": "with an accent", "accent_grave": "with an accent", "trait": "hyphen",
           "espace": "two words", "double": "double {l}"},
    "es": {"accent_aigu": "con acento", "accent_grave": "con acento", "trait": "guion",
           "espace": "en dos palabras", "double": "doble {l}"},
}
EPELER_INTRO = {"fr": "Ça s'écrit :", "en": "That's spelled", "es": "Se escribe:"}

# ── Les nombres et les heures (révisé aux tours 1 et 2, E1) ──────────────
# (id, {langue: phrase dite}, bonne, {langue apprise: [(voisine, nature)]}).
# Les voisines sont écrites PAR LANGUE APPRISE (tour 2) : l'erreur d'oreille
# dépend de ce qu'on entend. « fifty/fifteen » n'existe qu'en anglais ; le
# français dit « quinze heures » et ne se trompe pas de « p.m. ».
_n = lambda *v: list(v)
NOMBRES = [
    ("n1", {"fr": "Vous êtes à la chambre quatre cent douze.",
            "en": "You're in room four-twelve.",
            "es": "Está en la habitación cuatrocientos doce."}, "412",
     {"fr": _n(("421", "inv"), ("402", "voisin"), ("413", "voisin")),
      "en": _n(("421", "inv"), ("420", "voisin"), ("214", "inv")),
      "es": _n(("421", "inv"), ("402", "voisin"), ("214", "inv"))}),
    ("n2", {"fr": "La chambre douze cent huit, au douzième étage.",
            "en": "Room twelve-oh-eight, on the twelfth floor.",
            "es": "La habitación mil doscientos ocho, en el piso doce."}, "1208",
     {"fr": _n(("1280", "inv"), ("2108", "inv"), ("1218", "voisin")),
      "en": _n(("1280", "voisin"), ("2108", "inv"), ("1218", "voisin")),
      "es": _n(("1280", "voisin"), ("2108", "inv"), ("1218", "voisin"))}),
    ("n3", {"fr": "C'est cent quatre-vingt-neuf dollars la nuit.",
            "en": "It's a hundred and eighty-nine dollars a night.",
            "es": "Son ciento ochenta y nueve dólares la noche."}, "189 $",
     {l: _n(("198 $", "inv"), ("179 $", "voisin"), ("89 $", "cent")) for l in ("fr", "en", "es")}),
    ("n4", {"fr": "Ça fait cent quarante-neuf dollars et cinquante.",
            "en": "That comes to one forty-nine fifty.",
            "es": "Son ciento cuarenta y nueve dólares con cincuenta."}, "149,50 $",
     {"fr": _n(("159,50 $", "voisin"), ("149,05 $", "voisin"), ("140,50 $", "voisin")),
      "en": _n(("140,50 $", "voisin"), ("159,50 $", "voisin"), ("149,15 $", "teen")),
      "es": _n(("159,50 $", "voisin"), ("149,05 $", "voisin"), ("140,50 $", "voisin"))}),
    ("n5", {"fr": "L'arrivée est à quinze heures.",
            "en": "Check-in is at three p.m.",
            "es": "La entrada es a las tres de la tarde."}, "15:00",
     {"fr": _n(("13:00", "heure"), ("16:00", "heure"), ("3:00", "h24")),
      "en": _n(("13:00", "heure"), ("3:00", "ampm"), ("16:00", "heure")),
      "es": _n(("13:00", "heure"), ("3:00", "ampm"), ("16:00", "heure"))}),
    ("n6", {"fr": "Le départ est à onze heures.",
            "en": "Check-out is at eleven a.m.",
            "es": "La salida es a las once de la mañana."}, "11:00",
     {"fr": _n(("23:00", "h24"), ("12:00", "heure"), ("7:00", "heure")),
      "en": _n(("23:00", "ampm"), ("7:00", "heure"), ("10:00", "heure")),
      "es": _n(("23:00", "ampm"), ("12:00", "heure"), ("10:00", "heure"))}),
    ("n7", {"fr": "Le déjeuner commence à sept heures et demie.",
            "en": "Breakfast starts at seven thirty.",
            "es": "El desayuno empieza a las siete y media."}, "7:30",
     {"fr": _n(("7:15", "fraction"), ("6:30", "heure"), ("17:30", "h24")),
      "en": _n(("7:13", "teen"), ("6:30", "heure"), ("17:30", "ampm")),
      "es": _n(("7:15", "fraction"), ("6:30", "heure"), ("17:30", "ampm"))}),
    ("n8", {"fr": "La piscine ferme à vingt-deux heures quarante-cinq.",
            "en": "The pool closes at a quarter to eleven at night.",
            "es": "La alberca cierra a un cuarto para las once de la noche."}, "22:45",
     {"fr": _n(("20:45", "voisin"), ("22:40", "voisin"), ("12:45", "voisin")),
      "en": _n(("23:15", "fraction"), ("22:15", "fraction"), ("10:45", "ampm")),
      "es": _n(("23:15", "fraction"), ("22:15", "fraction"), ("10:45", "ampm"))}),
    # Tour 3 (A2) : au comptoir, le français se DIT aussi sur 12 heures.
    ("n9", {"fr": "Je vais arriver vers onze heures du soir.",
            "en": "I'll be arriving around eleven p.m.",
            "es": "Voy a llegar como a las once de la noche."}, "23:00",
     {"fr": _n(("11:00", "soir"), ("21:00", "heure"), ("12:00", "heure")),
      "en": _n(("11:00", "ampm"), ("7:00", "heure"), ("21:00", "heure")),
      "es": _n(("11:00", "ampm"), ("12:00", "heure"), ("21:00", "heure"))}),
    ("n10", {"fr": "Pouvez-vous me réveiller à six heures et demie du matin?",
             "en": "Could you wake me up at six thirty a.m.?",
             "es": "¿Me puede despertar a las seis y media de la mañana?"}, "6:30",
     {"fr": _n(("18:30", "soir"), ("6:15", "fraction"), ("7:30", "heure")),
      "en": _n(("18:30", "ampm"), ("6:13", "teen"), ("7:30", "heure")),
      "es": _n(("18:30", "ampm"), ("6:15", "fraction"), ("7:30", "heure"))}),
]
# La rétroaction, dans la langue de l'INTERFACE. Pour les erreurs qui tiennent à
# la langue entendue (ampm, h24, fraction, teen), une version PAR LANGUE APPRISE.
ERREURS_NOMBRES = {
    "inv": {"fr": "Les chiffres sont inversés : réécoutez l'ordre.",
            "en": "The digits are reversed: listen to the order again.",
            "es": "Las cifras están invertidas: escuche otra vez el orden."},
    "voisin": {"fr": "Un chiffre a été mal entendu : réécoutez le nombre.",
               "en": "One digit was misheard: listen to the number again.",
               "es": "Una cifra se oyó mal: vuelva a escuchar el número."},
    "cent": {"fr": "Il manque la centaine : écoutez le début du nombre.",
             "en": "The hundreds are missing: listen to the start of the number.",
             "es": "Faltan las centenas: escuche el principio del número."},
    "heure": {"fr": "Ce n'est pas l'heure dite : réécoutez le nombre.",
              "en": "That's not the time that was said: listen to the number again.",
              "es": "No es la hora que se dijo: vuelva a escuchar el número."},
    "teen": {"en": {"fr": "Écoutez la fin : « fifty » (50) n'est pas « fifteen » (15), ni « thirty » (30) « thirteen » (13). L'accent tombe sur la fin de « fifteen ».",
                    "en": "Listen to the end: « fifty » (50) is not « fifteen » (15), nor « thirty » (30) « thirteen » (13). The stress falls on the end of « fifteen ».",
                    "es": "Escuche el final: « fifty » (50) no es « fifteen » (15), ni « thirty » (30) « thirteen » (13). El acento cae al final de « fifteen »."}},
    "ampm": {"en": {"fr": "Matin ou après-midi? « p.m. », c'est l'après-midi ou le soir : 3 p.m. = 15:00. On note sur 24 heures.",
                    "en": "Morning or afternoon? « p.m. » is afternoon or evening: 3 p.m. = 15:00. Write it on the 24-hour clock.",
                    "es": "¿Mañana o tarde? « p.m. » es la tarde o la noche: 3 p. m. = 15:00. Se anota en formato de 24 horas."},
             "es": {"fr": "Matin ou après-midi? « de la tarde », « de la noche », c'est l'après-midi ou le soir : las tres de la tarde = 15:00.",
                    "en": "Morning or afternoon? « de la tarde », « de la noche » mean afternoon or evening: las tres de la tarde = 15:00.",
                    "es": "¿Mañana o tarde? « de la tarde », « de la noche »: las tres de la tarde son las 15:00. Se anota en formato de 24 horas."}},
    # La NOTATION est sur 24 h ; la parole, elle, dit aussi « du matin », « du soir ».
    "h24": {"fr": {"fr": "« Quinze heures », c'est 15:00 : on note l'heure sur 24 heures. Au comptoir, on entend aussi « trois heures de l'après-midi ».",
                   "en": "« Quinze heures » is 15:00: times are written on the 24-hour clock. At the desk you'll also hear « trois heures de l'après-midi ».",
                   "es": "« Quinze heures » son las 15:00: la hora se anota en 24 horas. En el mostrador también se oye « trois heures de l'après-midi »."}},
    "soir": {"fr": {"fr": "Matin ou soir? « Du soir » : onze heures du soir = 23:00 ; « du matin » : six heures et demie du matin = 6:30. On note sur 24 heures.",
                    "en": "Morning or evening? « Du soir » means evening: onze heures du soir = 23:00; « du matin »: six heures et demie du matin = 6:30.",
                    "es": "¿Mañana o noche? « Du soir » es de la noche: onze heures du soir = 23:00; « du matin »: six heures et demie du matin = 6:30."}},
    "fraction": {"fr": {"fr": "Écoutez la fin : « et demie » = 30, « et quart » = 15, « moins le quart » = 45.",
                        "en": "Listen to the end: « et demie » = 30, « et quart » = 15, « moins le quart » = 45.",
                        "es": "Escuche el final: « et demie » = 30, « et quart » = 15, « moins le quart » = 45."},
                 "en": {"fr": "Écoutez la fin : « thirty » = 30, « quarter past » = 15, « a quarter to » = 45 (l'heure d'avant).",
                        "en": "Listen to the end: « thirty » = 30, « quarter past » = 15, « a quarter to » = 45 (of the hour before).",
                        "es": "Escuche el final: « thirty » = 30, « quarter past » = 15, « a quarter to » = 45 (de la hora anterior)."},
                 "es": {"fr": "Écoutez la fin : « y media » = 30, « y cuarto » = 15, « un cuarto para las once » = 10 h 45 (22:45 le soir).",
                        "en": "Listen to the end: « y media » = 30, « y cuarto » = 15, « un cuarto para las once » = 10:45 (22:45 at night).",
                        "es": "Escuche el final: « y media » = 30, « y cuarto » = 15, « un cuarto para las once » = 10:45 (22:45 de la noche)."}},
}

# ── Ce que le client veut (révisé au tour 1, A3) ─────────────────────────
# (id, lit, nuits, {langue: demande}). Quatre demandes ne DISENT PAS le nombre
# de nuits : il se déduit des dates, comme au téléphone.
LITS = ["lit-simple", "lit-double", "lit-queen", "lit-king"]
DEMANDES = [
    ("c1", "lit-queen", 2, {"fr": "Bonsoir! J'aurais besoin d'une chambre avec un lit queen, pour deux nuits.",
                            "en": "Hi there, I'd like a room with a queen bed for two nights.",
                            "es": "Buenas noches, quisiera una habitación con cama queen para dos noches."}),
    ("c2", "lit-king", 3, {"fr": "Avez-vous une chambre avec un lit king? C'est pour trois nuits.",
                           "en": "Do you have a room with a king bed? It's for three nights.",
                           "es": "¿Tiene una habitación con cama king size? Es para tres noches."}),
    ("c3", "lit-simple", 1, {"fr": "Juste une nuit, et un lit simple, ça va être parfait.",
                             "en": "Just one night, and a twin bed will be perfect.",
                             "es": "Solo una noche, y con una cama individual está perfecto."}),
    ("c4", "lit-double", 4, {"fr": "On reste quatre nuits. Un lit double, s'il vous plaît.",
                             "en": "We're staying four nights. A double bed, please.",
                             "es": "Nos quedamos cuatro noches. Una cama matrimonial, por favor."}),
    ("c5", "lit-queen", 5, {"fr": "Je voudrais réserver cinq nuits, avec un lit queen.",
                            "en": "I'd like to book five nights, with a queen bed.",
                            "es": "Quisiera reservar cinco noches, con cama queen."}),
    ("c6", "lit-king", 2, {"fr": "Un lit king pour deux nuits, est-ce que c'est possible?",
                           "en": "A king bed for two nights, is that possible?",
                           "es": "¿Una cama king size para dos noches, se puede?"}),
    ("c7", "lit-simple", 3, {"fr": "C'est pour trois nuits. Un lit simple, ça me suffit.",
                             "en": "It's for three nights. A twin bed is fine for me.",
                             "es": "Es para tres noches. Con una cama individual me basta."}),
    ("c8", "lit-double", 1, {"fr": "Une seule nuit, dans un lit double.",
                             "en": "Only one night, in a double bed.",
                             "es": "Una sola noche, en una cama matrimonial."}),
    ("c9", "lit-queen", 3, {"fr": "J'arrive le jeudi douze et je repars le dimanche quinze. Un lit queen, s'il vous plaît.",
                            "en": "I'm checking in Thursday the twelfth and leaving Sunday the fifteenth. A queen bed, please.",
                            "es": "Llego el jueves doce y me voy el domingo quince. Cama queen, por favor."}),
    ("c10", "lit-king", 2, {"fr": "Ce serait pour vendredi soir et samedi soir, avec un lit king.",
                            "en": "It's for Friday night and Saturday night, with a king bed.",
                            "es": "Sería para el viernes y el sábado en la noche, con cama king size."}),
    ("c11", "lit-double", 4, {"fr": "Du trois au sept mai, dans un lit double.",
                              "en": "From May third to May seventh, in a double bed.",
                              "es": "Del tres al siete de mayo, en una cama matrimonial."}),
    ("c12", "lit-simple", 1, {"fr": "Juste ce soir; je repars demain matin. Un lit simple.",
                              "en": "Just tonight, I'm leaving tomorrow morning. A twin bed.",
                              "es": "Nada más esta noche; me voy mañana temprano. Una cama individual."}),
]
NUITS = {"fr": ("nuit", "nuits"), "en": ("night", "nights"), "es": ("noche", "noches")}

# ── Ce que je réponds (révisé au tour 1 : A3, D4, E2) ────────────────────
# Chaque item : le contexte (interface, facultatif), la réplique du client
# (apprise), puis trois répliques du réceptionniste (apprise) de MÊME
# INTENTION et de longueur voisine — la bonne d'abord, l'écran mélange. Une
# mauvaise porte sa rétroaction (interface) et, si c'est une PROMESSE HORS
# RÈGLE, `promesse: True` : la conséquence s'affiche APRÈS le choix et l'item
# compte comme échoué (O4, éliminatoire). Aucun avertissement avant le choix.
def R(fr, en, es):
    return {"fr": fr, "en": en, "es": es}


REPONSES = [
    {"id": "r1", "ctx": None,
     "client": R("Bonjour, j'ai une réservation au nom de Moreno.", "Hi, I have a reservation under Moreno.",
                 "Buenas tardes, tengo una reservación a nombre de Moreno."),
     "reps": [
         (R("Bienvenue! Pouvez-vous m'épeler votre nom de famille?", "Welcome! Could you spell your last name for me?",
            "¡Bienvenido! ¿Me puede deletrear su apellido, por favor?"), None, False),
         (R("Salut! Tu peux m'épeler ton nom de famille?", "Hey! Spell your last name for me, buddy.",
            "¡Hola! ¿Me deletreas tu apellido, porfa, amigo?"),
          R("Même geste, mais trop familier : à la réception, on reste poli et formel.",
            "Right idea, but too casual: at the front desk, stay polite and formal.",
            "Buena idea, pero demasiado informal: en la recepción se habla con cortesía y formalidad."), False),
         (R("Bienvenue! Pouvez-vous m'épeler votre prénom?", "Welcome! Could you spell your first name for me?",
            "¡Bienvenido! ¿Me puede deletrear su nombre de pila?"),
          R("La réservation est au nom de famille : c'est lui qu'on fait épeler.",
            "The booking is under the last name: that's the one to have spelled.",
            "La reservación está a nombre del apellido: es el que se pide deletrear."), False)]},
    {"id": "r2", "ctx": None,
     "ctx_dire": R("Le déjeuner est compris : servi de 7 h à 10 h, au rez-de-chaussée.",
                   "Breakfast is included: served from 7 to 10 a.m., on the ground floor.",
                   "El desayuno está incluido: se sirve de 7 a 10 de la mañana, en la planta baja."),
     "client": R("Est-ce que le déjeuner est compris?", "Is breakfast included?", "¿El desayuno está incluido?"),
     "reps": [
         (R("Oui, il est servi de sept heures à dix heures, au rez-de-chaussée.",
            "Yes, it's served from seven to ten on the ground floor.",
            "Sí, se sirve de siete a diez en la planta baja."), None, False),
         (R("Oui, le repas est servi de midi à quatorze heures, au rez-de-chaussée.",
            "Yes, lunch is served from noon to two on the ground floor.",
            "Sí, la comida se sirve de doce a dos en la planta baja."),
          R("Il parle du repas du matin, pas du repas du midi.",
            "He means the morning meal, not the midday meal.",
            "Pregunta por la comida de la mañana, no la del mediodía."), False),
         (R("Oui, et je vous offre aussi le souper gratuitement ce soir.",
            "Yes, and dinner tonight is on us, free of charge.",
            "Sí, y además le regalo la cena de esta noche."),
          R("Offrir un repas gratuit revient au gérant : on ne le promet pas seul.",
            "A free meal is the manager's call: never promise it yourself.",
            "Una comida gratis le toca al gerente: no se promete solo."), True)]},
    {"id": "r3", "ctx": R("Ce soir, l'hôtel est complet.", "Tonight, the hotel is fully booked.",
                          "Esta noche, el hotel está lleno."),
     "client": R("Avez-vous une chambre pour ce soir?", "Do you have a room for tonight?",
                 "¿Tiene una habitación para esta noche?"),
     "reps": [
         (R("Désolé, c'est complet ce soir. Je peux appeler un hôtel voisin?",
            "Sorry, we're full tonight. Can I call a nearby hotel for you?",
            "Lo siento, estamos llenos. ¿Le llamo a un hotel cercano?"), None, False),
         (R("Non, c'est plein ce soir. Essayez ailleurs, peut-être au centre-ville.",
            "Nope, we're full tonight. Try somewhere else downtown, maybe.",
            "No, está lleno hoy. Busque en otro lado, a lo mejor en el centro."),
          R("C'est vrai, mais sec : on s'excuse et on offre une solution.",
            "True, but curt: apologize and offer a solution.",
            "Es cierto, pero seco: hay que disculparse y ofrecer una solución."), False),
         (R("Oui, bien sûr! Je vous donne la chambre quatre cent douze.",
            "Yes, of course! I'll give you room four-twelve right away.",
            "¡Sí, claro! Ahora mismo le doy la habitación cuatrocientos doce."),
          R("L'hôtel est complet : on ne promet pas une chambre qu'on n'a pas.",
            "The hotel is full: never promise a room you don't have.",
            "El hotel está lleno: no se promete una habitación que no hay."), True)]},
    {"id": "r4", "ctx": None,
     "client": R("La chambre était bruyante. Je veux être remboursé au complet.",
                 "The room was noisy. I want a full refund.",
                 "La habitación era muy ruidosa. Quiero un reembolso completo."),
     "reps": [
         (R("Je suis désolé pour le bruit. Je vais en parler au gérant tout de suite.",
            "I'm very sorry about the noise. I'll talk to the manager right away.",
            "Lamento mucho el ruido. Lo consulto con el gerente ahora mismo."), None, False),
         (R("Je suis désolé pour le bruit. Je vous rembourse tout le séjour tout de suite.",
            "I'm very sorry about the noise. I'll refund your whole stay right away.",
            "Lamento mucho el ruido. Le reembolso toda la estancia ahora mismo."),
          R("Un remboursement revient au gérant : on ne le promet jamais seul.",
            "A refund is the manager's call: never promise it yourself.",
            "Un reembolso le toca al gerente: nunca se promete solo."), True),
         (R("Je m'excuse pour le trouble, mais le bruit, ce n'est pas notre faute.",
            "Sorry for the trouble, but the noise is not our fault, you know.",
            "Perdón por la molestia, pero el ruido no es culpa nuestra."),
          R("On ne rejette pas la plainte : on s'excuse, puis on passe le relais au gérant.",
            "Don't brush off the complaint: apologize, then hand it to the manager.",
            "No se rechaza la queja: se disculpa y se pasa al gerente."), False)]},
    {"id": "r5", "ctx": None,
     "client": R("Ma carte-clé ne fonctionne pas.", "My key card doesn't work.", "Mi tarjeta llave no funciona."),
     "reps": [
         (R("Désolé! Je peux la voir? Je la réencode tout de suite.",
            "I'm sorry! May I see it? I'll re-encode it for you right away.",
            "¡Disculpe! ¿Me la permite? Se la vuelvo a codificar ahora."), None, False),
         (R("Désolé! Je vais appeler le gérant, il va s'en occuper.",
            "I'm sorry! I'll call the manager, he'll take care of it.",
            "¡Disculpe! Voy a llamar al gerente; él se encarga de eso enseguida."),
          R("Réencoder une clé, c'est votre geste : pas besoin du gérant.",
            "Re-encoding a key is your job: no need for the manager.",
            "Recodificar una llave le toca a usted: no hace falta el gerente."), False),
         (R("Désolé! Essayez de la frotter un peu, ça marche parfois.",
            "Sorry! Try rubbing it a little, sometimes that works.",
            "¡Perdón! Frótela un poquito, a veces así funciona."),
          R("Une carte démagnétisée se réencode : on ne renvoie pas le client essayer.",
            "A demagnetized card must be re-encoded: don't send the guest back to try.",
            "Una tarjeta desmagnetizada se vuelve a codificar: no se manda al cliente a intentarlo."), False)]},
    {"id": "r6", "ctx": R("Au téléphone.", "On the phone.", "Por teléfono."),
     "client": R("Est-ce que je peux changer ma réservation pour vendredi?",
                 "Can I change my reservation to Friday?",
                 "¿Puedo cambiar mi reservación para el viernes?"),
     "reps": [
         (R("Je vais vérifier. Quel est votre numéro de confirmation?",
            "Let me check. Could I have your confirmation number, please?",
            "Permítame revisar. ¿Me da su número de confirmación?"), None, False),
         (R("Bien sûr, c'est changé pour vendredi, pas de problème.",
            "Of course, it's changed to Friday, no problem at all.",
            "Claro, ya quedó para el viernes, no hay problema."),
          R("On vérifie la réservation et les chambres libres avant de confirmer.",
            "Check the booking and availability before you confirm.",
            "Primero se revisa la reservación y la disponibilidad."), False),
         (R("Ouin, OK. C'est quoi, ton numéro de confirmation, déjà, toi?",
            "Yeah, okay. So what's your confirmation number, then, buddy?",
            "Sí, órale. ¿Y cuál es tu número de confirmación?"),
          R("Même geste, mais trop familier : au téléphone aussi, on reste poli et formel.",
            "Right idea, but too casual: on the phone too, stay polite and formal.",
            "Buena idea, pero demasiado informal: por teléfono también, cortesía y formalidad."), False)]},
    # Expliquer des frais (O3)
    {"id": "r7", "ctx": None,
     "client": R("Pourquoi vous prenez cent dollars de plus sur ma carte?",
                 "Why are you holding an extra hundred dollars on my card?",
                 "¿Por qué me retienen cien dólares más en la tarjeta?"),
     "reps": [
         (R("C'est un dépôt pour les imprévus, libéré à votre départ.",
            "It's a deposit for incidentals, released at check-out.",
            "Es un depósito por imprevistos. Se libera cuando usted se va."), None, False),
         (R("C'est un dépôt, mais je peux l'annuler pour vous, sans problème.",
            "It's a deposit, but I can cancel it for you, no problem.",
            "Es un depósito, pero se lo puedo quitar, no hay problema."),
          R("Retirer le dépôt est une exception : elle revient au gérant.",
            "Dropping the deposit is an exception: that's the manager's call.",
            "Quitar el depósito es una excepción: le toca al gerente."), True),
         (R("Ce sont les taxes de la chambre. Elles sont déjà payées.",
            "Those are the room taxes. They've already been paid.",
            "Son los impuestos de la habitación. Ya están pagados, no se preocupe."),
          R("C'est un dépôt, pas une taxe : il sera libéré au départ.",
            "It's a deposit, not a tax: it will be released at check-out.",
            "Es un depósito, no un impuesto: se libera a la salida."), False)]},
    {"id": "r8", "ctx": None,
     "client": R("C'est quoi, cette ligne de trois dollars sur ma facture?",
                 "What's this three-dollar line on my bill?",
                 "¿Qué es este cargo de tres dólares en mi cuenta?"),
     "reps": [
         (R("C'est la taxe sur l'hébergement; elle s'applique à chaque nuit.",
            "That's the lodging tax. It applies to every night.",
            "Es el impuesto al hospedaje. Se cobra por cada noche de estancia."), None, False),
         (R("Je ne sais pas trop, c'est l'ordinateur qui l'ajoute tout seul, je pense.",
            "I'm not really sure, the computer just adds it by itself.",
            "No sé bien, la computadora lo agrega sola a la cuenta."),
          R("On explique les frais : c'est la taxe sur l'hébergement, par nuit.",
            "Explain the charge: it's the lodging tax, per night.",
            "Se explica el cargo: es el impuesto al hospedaje, por noche."), False),
         (R("C'est une taxe, mais je peux l'enlever de votre facture.",
            "It's a tax, but I can take it off your bill for you.",
            "Es un impuesto, pero se lo puedo quitar de la cuenta."),
          R("Une taxe ne s'enlève pas : c'est la loi, ni vous ni le gérant ne l'effacez.",
            "A tax can't be removed: it's the law, neither you nor the manager can waive it.",
            "Un impuesto no se quita: es la ley, ni usted ni el gerente pueden quitarlo."), True)]},
    {"id": "r9", "ctx": R("Le stationnement coûte 20 $ par nuit.", "Parking is $20 a night.",
                          "El estacionamiento cuesta 20 dólares por noche."),
     "client": R("Le stationnement, ce n'est pas gratuit?", "Isn't the parking free?",
                 "¿El estacionamiento no es gratis?"),
     "reps": [
         (R("Non, c'est vingt dollars par nuit, mais vous pouvez entrer et sortir.",
            "It's twenty dollars a night, and you're free to come and go.",
            "Cuesta veinte dólares por noche, y puede entrar y salir."), None, False),
         (R("Pour vous, je le laisse gratuit cette fois-ci, sans problème.",
            "For you, I'll make it free this time, no problem.",
            "Para usted, esta vez se lo dejo gratis, sin problema."),
          R("Un service gratuit est une exception : elle revient au gérant.",
            "A free service is an exception: that's the manager's call.",
            "Un servicio gratis es una excepción: le toca al gerente."), True),
         (R("Oui, il est gratuit, mais seulement la fin de semaine, pas en semaine.",
            "Yes, it's free, but only on weekends, not during the week.",
            "Sí, es gratis, pero solo el fin de semana, entre semana no."),
          R("Ce n'est pas le tarif : le stationnement coûte vingt dollars par nuit.",
            "That's not the rate: parking is twenty dollars a night.",
            "Esa no es la tarifa: el estacionamiento cuesta veinte dólares por noche."), True)]},
    # Ce qui revient au gérant (O4)
    {"id": "r10", "ctx": R("Départ tardif : 30 $ jusqu'à 14 h ; plus tard, c'est le gérant qui décide.",
                           "Late check-out: $30 until 2 p.m.; later than that, the manager decides.",
                           "Salida tardía: 30 dólares hasta las 2 p. m.; más tarde, decide el gerente."),
     "client": R("Est-ce que je peux partir à seize heures, sans frais?",
                 "Can I check out at four p.m., at no charge?",
                 "¿Puedo salir a las cuatro de la tarde sin costo?"),
     "reps": [
         (R("Jusqu'à 14 h, c'est 30 $. Pour 16 h, je dois demander au gérant.",
            "Until two, it's thirty dollars. For four, I'll check with the manager.",
            "Hasta las dos son treinta dólares. Para las cuatro, pregunto al gerente."), None, False),
         (R("Bien sûr, partez à seize heures, sans aucuns frais. Je m'en occupe.",
            "Sure, check out at four, at no charge at all. I'll take care of it for you.",
            "Claro, salga a las cuatro de la tarde, sin ningún costo. Yo me encargo de todo."),
          R("Un départ tardif gratuit est une exception : elle revient au gérant.",
            "A free late check-out is an exception: that's the manager's call.",
            "Una salida tardía sin costo es una excepción: le toca al gerente."), True),
         (R("Non, c'est impossible, désolé. Le départ est à onze heures, point.",
            "No, that's impossible. Check-out is at eleven o'clock, period.",
            "No, es imposible. La salida es a las once de la mañana y punto."),
          R("On ne ferme pas la porte : il y a le départ tardif payant, et le gérant pour le reste.",
            "Don't shut the door: there's the paid late check-out, and the manager for the rest.",
            "No se cierra la puerta: existe la salida tardía con costo, y el gerente para lo demás."), False)]},
    {"id": "r11", "ctx": None,
     "client": R("J'ai annulé trop tard, mais vous pouvez enlever les frais, non?",
                 "I cancelled too late, but you can waive the fee, right?",
                 "Cancelé muy tarde, pero me puede quitar el cargo, ¿no?"),
     "reps": [
         (R("Je comprends. Je ne peux pas les enlever moi-même; je transmets votre demande au gérant.",
            "I understand. I can't waive it myself; I'll pass it to the manager.",
            "Entiendo. Yo no puedo quitarlo; le paso su solicitud al gerente."), None, False),
         (R("Je comprends. Pas de souci, j'enlève les frais d'annulation tout de suite.",
            "I understand. No worries, I'll waive the cancellation fee right now.",
            "Entiendo. No se preocupe, le quito el cargo de cancelación ahora mismo."),
          R("Effacer des frais d'annulation est une exception : elle revient au gérant.",
            "Waiving a cancellation fee is an exception: that's the manager's call.",
            "Quitar un cargo de cancelación es una excepción: le toca al gerente."), True),
         (R("Les règles sont les règles. Il fallait annuler plus tôt que ça, désolé.",
            "Rules are rules, I'm afraid. You should have cancelled earlier.",
            "Las reglas son las reglas. Debió cancelar antes, lo siento."),
          R("Rappeler la règle sans rien offrir ferme la porte : on transmet au gérant.",
            "Quoting the rule and offering nothing shuts the door: pass it to the manager.",
            "Recordar la regla sin ofrecer nada cierra la puerta: se pasa al gerente."), False)]},
    {"id": "r12", "ctx": None,
     "client": R("C'est notre anniversaire de mariage. Vous pourriez nous surclasser?",
                 "It's our wedding anniversary. Could you upgrade us?",
                 "Es nuestro aniversario de bodas. ¿Nos podría dar un upgrade?"),
     "reps": [
         (R("Félicitations! Je vais demander au gérant si c'est possible.",
            "Congratulations! I'll ask the manager if that's possible.",
            "¡Muchas felicidades! Le voy a preguntar al gerente si es posible."), None, False),
         (R("Félicitations! Je vous donne la suite du dernier étage, gratuitement.",
            "Congratulations! I'll give you the top-floor suite, free.",
            "¡Felicidades! Les doy la suite del último piso, sin costo."),
          R("Un surclassement gratuit est une exception : il revient au gérant.",
            "A free upgrade is an exception: that's the manager's call.",
            "Un upgrade sin costo es una excepción: le toca al gerente."), True),
         (R("Ce n'est pas possible. Voici la clé de votre chambre standard.",
            "That's not possible. Here's the key to your standard room.",
            "No se puede. Aquí tiene la llave de su cuarto estándar."),
          R("On ne refuse pas d'emblée : on félicite, puis on demande au gérant.",
            "Don't refuse outright: congratulate them, then ask the manager.",
            "No se rechaza de entrada: se felicita y se pregunta al gerente."), False)]},
]

REPONSES.append(
    {"id": "r13", "ctx": R("Au téléphone.", "On the phone.", "Por teléfono."),
     "client": R("Je vais arriver vers huit heures.", "I'll be arriving around eight.",
                 "Voy a llegar como a las ocho."),
     "reps": [
         (R("Très bien. Huit heures du matin ou du soir?", "Great. Is that eight in the morning or evening?",
            "Muy bien. ¿A las ocho de la mañana o de la noche?"), None, False),
         (R("Très bien, je note votre arrivée à vingt heures.", "Great, I'll note your arrival for eight p.m.",
            "Muy bien, anoto su llegada a las ocho de la noche."),
          R("« Huit heures » peut être le matin ou le soir : on fait préciser avant de noter.",
            "« Eight » can be morning or evening: ask before you write it down.",
            "« Las ocho » puede ser de la mañana o de la noche: se pregunta antes de anotar."), False),
         (R("Très bien, je note votre arrivée à huit heures.", "Great, I'll note your arrival for eight a.m.",
            "Muy bien, anoto su llegada a las ocho de la mañana."),
          R("« Huit heures » peut être le matin ou le soir : on fait préciser avant de noter.",
            "« Eight » can be morning or evening: ask before you write it down.",
            "« Las ocho » puede ser de la mañana o de la noche: se pregunta antes de anotar."), False)]})

# La règle du relais, écrite UNE fois et citée partout (leçon de Francœur : dite
# trois fois, elle se contredisait).
REGLE_RELAIS = R(
    "Vous décidez seul : chercher une réservation, réencoder une clé, expliquer des frais. "
    "Le gérant décide : un remboursement, des frais effacés, un service gratuit, toute exception. "
    "Et personne ne promet ce que l'hôtel ne peut pas donner : une taxe ne s'enlève jamais, une chambre qu'on n'a pas ne se promet pas, un document faux (facture, date, mode de paiement) ne se fait jamais.",
    "You decide alone: look up a booking, re-encode a key, explain a charge. "
    "The manager decides: a refund, a waived fee, anything free, any exception. "
    "And no one promises what the hotel can't give: a tax is never removed, a room you don't have is never promised, a false document (bill, date, payment method) is never made.",
    "Usted decide solo: buscar una reservación, recodificar una llave, explicar un cargo. "
    "El gerente decide: un reembolso, un cargo que se quita, algo gratis, cualquier excepción. "
    "Y nadie promete lo que el hotel no puede dar: un impuesto nunca se quita, una habitación que no hay no se promete, un documento falso (factura, fecha, forma de pago) nunca se hace.")
PROMESSE = R(
    "Vous venez d'engager l'hôtel sans en avoir le pouvoir. Au comptoir, cette erreur fait échouer.",
    "You just committed the hotel without the authority to do so. At the desk, this mistake fails you.",
    "Acaba de comprometer al hotel sin tener autoridad para hacerlo. En el mostrador, este error es eliminatorio.")

# Les images qui ne vont JAMAIS ensemble dans une même série (tour 1, D4) :
# indiscernables, ou l'une contient l'autre.
JAMAIS_ENSEMBLE = [
    {"lit-simple", "lit-double", "lit-queen", "lit-king", "lit-appoint"},
    {"piece-identite", "permis", "passeport"},
    {"bagages", "valise", "chariot", "bagagiste"},
    {"carte-cle", "pochette"},
    {"douche", "bain"},
]

# ── Les textes des exercices, trois fois ─────────────────────────────────
UI = {
    "exercices": {"fr": "Les exercices", "en": "Practice", "es": "Ejercicios"},
    "x_entends": {"fr": "Je l'entends, je le trouve", "en": "I hear it, I find it", "es": "Lo escucho, lo encuentro"},
    "x_entends_c": {"fr": "Écoutez le mot, touchez l'image.", "en": "Listen to the word, tap the picture.", "es": "Escuche la palabra, toque la imagen."},
    "x_image": {"fr": "Le mot et son image", "en": "The word and its picture", "es": "La palabra y su imagen"},
    "x_image_c": {"fr": "Regardez l'image, choisissez le mot.", "en": "Look at the picture, choose the word.", "es": "Mire la imagen, elija la palabra."},
    "x_souviens": {"fr": "Je me souviens", "en": "I remember", "es": "Me acuerdo"},
    "x_souviens_c": {"fr": "Dites le sens à voix haute, puis vérifiez. Rien n'est noté.", "en": "Say the meaning out loud, then check. Nothing is scored.", "es": "Diga el significado en voz alta y luego verifique. No se califica."},
    "x_pieges": {"fr": "La série des pièges", "en": "The trap series", "es": "La serie de trampas"},
    "x_pieges_c": {"fr": "Que veut dire ce mot, dans cette phrase? Attention aux faux amis.", "en": "What does this word mean in this sentence? Watch out for false friends.", "es": "¿Qué quiere decir esta palabra en esta frase? Cuidado con los falsos amigos."},
    "x_epeler": {"fr": "Épeler un nom", "en": "Spelling a name", "es": "Deletrear un nombre"},
    "x_epeler_c": {"fr": "Le client épelle son nom. Écrivez-le.", "en": "The guest spells their name. Type it.", "es": "El cliente deletrea su apellido. Escríbalo."},
    "x_nombres": {"fr": "Les nombres et les heures", "en": "Numbers and times", "es": "Números y horas"},
    "x_nombres_c": {"fr": "Écoutez, puis touchez ce que vous avez entendu. Les heures s'écrivent sur 24 heures (15:00 = 3 h de l'après-midi).", "en": "Listen, then tap what you heard. Times are written on the 24-hour clock (15:00 = 3 p.m.).", "es": "Escuche y toque lo que oyó. La hora se escribe en formato de 24 horas (15:00 = 3 p. m.)."},
    "x_client": {"fr": "Ce que le client veut", "en": "What the guest wants", "es": "Lo que quiere el cliente"},
    "x_client_c": {"fr": "Le client parle vite. Choisissez le lit ET le nombre de nuits — parfois, il faut les compter à partir des dates.", "en": "The guest talks fast. Choose the bed AND the number of nights — sometimes you must count them from the dates.", "es": "El cliente habla rápido. Elija la cama Y el número de noches; a veces hay que contarlas a partir de las fechas."},
    "x_reponds": {"fr": "Ce que je réponds", "en": "What I answer", "es": "Lo que respondo"},
    "x_reponds_c": {"fr": "Choisissez la meilleure réponse du réceptionniste.", "en": "Choose the receptionist's best answer.", "es": "Elija la mejor respuesta del recepcionista."},
    "juste": {"fr": "Juste!", "en": "Right!", "es": "¡Correcto!"},
    "non_cest": {"fr": "Non : ça, c'est", "en": "No: that is", "es": "No: eso es"},
    "encore": {"fr": "Essayez encore.", "en": "Try again.", "es": "Intente otra vez."},
    "suivant": {"fr": "Suivant", "en": "Next", "es": "Siguiente"},
    "reecouter": {"fr": "Réécouter", "en": "Listen again", "es": "Volver a escuchar"},
    "lent": {"fr": "Plus lentement", "en": "More slowly", "es": "Más despacio"},
    "verifier": {"fr": "Vérifier", "en": "Check", "es": "Verificar"},
    "voir_sens": {"fr": "Voir le sens", "en": "Show the meaning", "es": "Ver el significado"},
    "je_savais": {"fr": "Je le savais", "en": "I knew it", "es": "Lo sabía"},
    "pas_encore": {"fr": "Pas encore", "en": "Not yet", "es": "Todavía no"},
    "premier_coup": {"fr": "du premier coup", "en": "on the first try", "es": "a la primera"},
    "sur": {"fr": "sur", "en": "out of", "es": "de"},
    "fini": {"fr": "Série terminée", "en": "Series complete", "es": "Serie terminada"},
    "recommencer": {"fr": "Recommencer", "en": "Start over", "es": "Volver a empezar"},
    "autres_ex": {"fr": "Les autres exercices", "en": "Other exercises", "es": "Otros ejercicios"},
    "votre_reponse": {"fr": "Votre réponse", "en": "Your answer", "es": "Su respuesta"},
    "la_bonne": {"fr": "La bonne réponse :", "en": "The right answer:", "es": "La respuesta correcta:"},
    "x_dire": {"fr": "Je le dis", "en": "I say it", "es": "Lo digo"},
    "x_dire_c": {"fr": "Lisez la situation, dites la phrase à voix haute dans la langue apprise, puis écoutez le modèle. Rien n'est noté.", "en": "Read the situation, say the sentence out loud in the language you're learning, then hear the model. Nothing is scored.", "es": "Lea la situación, diga la frase en voz alta en el idioma que aprende y luego escuche el modelo. No se califica."},
    "le_client_dit": {"fr": "Le client dit :", "en": "The guest says:", "es": "El cliente dice:"},
    "vous_dites": {"fr": "Vous voulez dire :", "en": "You want to say:", "es": "Usted quiere decir:"},
    "ecouter_modele": {"fr": "Écouter le modèle", "en": "Hear the model", "es": "Escuchar el modelo"},
    "dit_pareil": {"fr": "Je l'ai dit", "en": "I said it", "es": "Lo dije"},
    "accent_oublie": {"fr": "N'oubliez pas les accents et les traits d'union :", "en": "Don't forget the accents and hyphens:", "es": "No olvide los acentos y guiones:"},
    "premiere_fausse": {"fr": "La première lettre fausse est la lettre n°", "en": "The first wrong letter is letter number", "es": "La primera letra incorrecta es la número"},
    "phrase_dite": {"fr": "On a dit :", "en": "What was said:", "es": "Se dijo:"},
    "regle_tit": {"fr": "La règle du comptoir", "en": "The desk rule", "es": "La regla del mostrador"},
    "lit_ok": {"fr": "Le lit est juste, pas le nombre de nuits.", "en": "The bed is right, not the number of nights.", "es": "La cama es correcta, pero no el número de noches."},
    "nuits_ok": {"fr": "Les nuits sont justes, pas le lit.", "en": "The nights are right, not the bed.", "es": "Las noches son correctas, pero no la cama."},
    "rien_ok": {"fr": "Ni le lit ni les nuits : réécoutez.", "en": "Neither the bed nor the nights: listen again.", "es": "Ni la cama ni las noches: vuelva a escuchar."},
    "plusieurs": {"fr": "planches mêlées", "en": "all topics mixed", "es": "todos los temas"},
    "aucun_piege": {"fr": "Pas de piège pour cette paire de langues.", "en": "No traps for this language pair.", "es": "No hay trampas para este par de idiomas."},
}
