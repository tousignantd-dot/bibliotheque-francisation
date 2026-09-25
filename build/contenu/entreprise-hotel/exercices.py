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

# ── La série des pièges ──────────────────────────────────────────────────
# Pour un piège de la paire, vu dans une interface donnée : le mot appris est
# montré (et dit), et la « fausse lecture » qu'un locuteur de l'interface ferait
# se glisse parmi les choix. Une interface qui n'a pas de fausse lecture
# naturelle pour ce mot n'a pas d'item — on n'invente pas un piège.
PIEGES_FAUX = {
    # fr·en
    "souper":      {"fr": "le dîner"},              # « dinner » lu comme dîner
    "billet":      {"fr": "une contravention"},     # « a ticket » au sens québécois
    "etage":       {"fr": "le plancher"},           # « the floor »
    "lit-double":  {"fr": "un lit occupé", "en": "a double room"},
    "monnaie":     {"en": "money", "fr": "un changement"},
    "dejeuner":    {"en": "lunch"},
    "depot":       {"en": "a warehouse"},
    "location-auto": {"en": "the car's location"},
    # fr·es
    "stylo":       {"fr": "une plume"},
    "prenom":      {"fr": "le nom de famille", "es": "el apellido"},
    "serviettes":  {"es": "servilletas"},
    "diner":       {"fr": "le souper", "es": "la cena"},
    "frais":       {"fr": "un navire de charge", "es": "algo fresco"},
    "facture":     {"fr": "le compte en banque", "es": "la factura fiscal (con RFC)"},
    "autobus":     {"fr": "un camion"},
    "tout-droit":  {"fr": "à droite", "es": "a la derecha"},
    # es·en
    "sortie":      {"es": "el éxito"},
    "embarrasse":  {"es": "estoy embarazada", "en": "it hurts me"},
    "dossier":     {"en": "the carpet"},
}

# ── Épeler un nom ────────────────────────────────────────────────────────
NOMS = ["TREMBLAY", "NGUYEN", "OKAFOR", "MORENO", "GAUTHIER", "WHITFIELD", "KOWALSKI", "LACHANCE"]

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
                "ye", "zeta"])),
    "en": {c: c for c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"},
}
EPELER_INTRO = {"fr": "Ça s'écrit :", "en": "That's spelled", "es": "Se escribe:"}

# ── Les nombres et les heures ────────────────────────────────────────────
# (id, {langue: phrase dite}, [bonne, et trois voisines]). Les voisines sont
# les erreurs d'oreille réelles : chiffres inversés, 3 h contre 15 h.
NOMBRES = [
    ("n1", {"fr": "Vous êtes à la chambre quatre cent douze.",
            "en": "You're in room four-twelve.",
            "es": "Está en la habitación cuatrocientos doce."},
     ["412", "421", "214", "402"]),
    ("n2", {"fr": "La chambre douze cent huit, au douzième étage.",
            "en": "Room twelve-oh-eight, on the twelfth floor.",
            "es": "La habitación mil doscientos ocho, en el piso doce."},
     ["1208", "1280", "2108", "1218"]),
    ("n3", {"fr": "C'est cent quatre-vingt-neuf dollars la nuit.",
            "en": "It's a hundred and eighty-nine dollars a night.",
            "es": "Son ciento ochenta y nueve dólares la noche."},
     ["189 $", "198 $", "179 $", "89 $"]),
    ("n4", {"fr": "Ça fait cent quarante-neuf dollars et cinquante.",
            "en": "That comes to one forty-nine fifty.",
            "es": "Son ciento cuarenta y nueve dólares con cincuenta."},
     ["149,50 $", "140,50 $", "159,50 $", "149,15 $"]),
    ("n5", {"fr": "L'arrivée est à quinze heures.",
            "en": "Check-in is at three p.m.",
            "es": "La entrada es a las tres de la tarde."},
     ["15:00", "13:00", "3:00", "16:00"]),
    ("n6", {"fr": "Le départ est à onze heures.",
            "en": "Check-out is at eleven a.m.",
            "es": "La salida es a las once de la mañana."},
     ["11:00", "23:00", "7:00", "10:00"]),
    ("n7", {"fr": "Le déjeuner commence à sept heures et demie.",
            "en": "Breakfast starts at seven thirty.",
            "es": "El desayuno empieza a las siete y media."},
     ["7:30", "7:15", "6:30", "17:30"]),
    ("n8", {"fr": "La piscine ferme à vingt-deux heures quarante-cinq.",
            "en": "The pool closes at a quarter to eleven at night.",
            "es": "La alberca cierra a un cuarto para las once de la noche."},
     ["22:45", "23:15", "22:15", "10:45"]),
]

# ── Ce que le client veut ────────────────────────────────────────────────
# (id, lit, nuits, {langue: demande}). Les cartes montrent le croquis du lit
# et le nombre de nuits : les deux traits décident ensemble.
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
                             "en": "We're staying four nights. A full bed, please.",
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
                             "en": "Only one night, in a full bed.",
                             "es": "Una sola noche, en una cama matrimonial."}),
]
NUITS = {"fr": ("nuit", "nuits"), "en": ("night", "nights"), "es": ("noche", "noches")}

# ── Ce que je réponds ────────────────────────────────────────────────────
# (id, contexte {interface}, client {apprise}, [(réplique {apprise},
# rétroaction {interface} ou None si juste)]). La bonne est la première ;
# l'écran mélange. `hors_regle` marque l'item où promettre fait échouer (O4).
REPONSES = [
    ("r1", None,
     {"fr": "Bonjour, j'ai une réservation au nom de Moreno.",
      "en": "Hi, I have a reservation under Moreno.",
      "es": "Buenas tardes, tengo una reservación a nombre de Moreno."},
     [({"fr": "Bienvenue! Pouvez-vous épeler votre nom de famille, s'il vous plaît?",
        "en": "Welcome! Could you spell your last name, please?",
        "es": "¡Bienvenido! ¿Me puede deletrear su apellido, por favor?"}, None),
      ({"fr": "Quel est votre prénom?", "en": "What is your first name?", "es": "¿Cuál es su nombre?"},
       {"fr": "La réservation est au nom de famille : c'est lui qu'on fait épeler.",
        "en": "The booking is under the last name: that's the one to have spelled.",
        "es": "La reservación está a nombre del apellido: es el que se pide deletrear."}),
      ({"fr": "L'hôtel est complet ce soir.", "en": "We're fully booked tonight.",
        "es": "No tenemos disponibilidad esta noche."},
       {"fr": "Il a déjà une réservation : on la cherche, on ne refuse pas.",
        "en": "He already has a booking: look it up, don't turn him away.",
        "es": "Ya tiene reservación: se busca, no se rechaza."})], False),
    ("r2", None,
     {"fr": "Est-ce que le déjeuner est compris?", "en": "Is breakfast included?",
      "es": "¿El desayuno está incluido?"},
     [({"fr": "Oui, il est servi de sept heures à dix heures, au rez-de-chaussée.",
        "en": "Yes, it's served from seven to ten, on the ground floor.",
        "es": "Sí, se sirve de siete a diez, en la planta baja."}, None),
      ({"fr": "Le dîner est servi à midi.", "en": "Lunch is served at noon.",
        "es": "La comida se sirve a mediodía."},
       {"fr": "Il parle du repas du matin : au Québec, c'est le déjeuner.",
        "en": "He's asking about the morning meal.",
        "es": "Pregunta por el desayuno, la comida de la mañana."}),
      ({"fr": "Le départ est à onze heures.", "en": "Check-out is at eleven.",
        "es": "La salida es a las once."},
       {"fr": "Ce n'est pas sa question : il demande pour le repas.",
        "en": "That's not what he asked: he's asking about the meal.",
        "es": "No es lo que preguntó: pregunta por el desayuno."})], False),
    ("r3", {"fr": "Ce soir, l'hôtel est complet.", "en": "Tonight, the hotel is fully booked.",
            "es": "Esta noche, el hotel está lleno."},
     {"fr": "Avez-vous une chambre pour ce soir?", "en": "Do you have a room for tonight?",
      "es": "¿Tiene una habitación para esta noche?"},
     [({"fr": "Je suis désolé, l'hôtel est complet ce soir. Je peux appeler un autre hôtel près d'ici pour vous.",
        "en": "I'm sorry, we're fully booked tonight. I can call another hotel nearby for you.",
        "es": "Lo siento, no tenemos disponibilidad esta noche. Le puedo llamar a otro hotel cercano."}, None),
      ({"fr": "Non.", "en": "No.", "es": "No."},
       {"fr": "C'est vrai, mais sec : on s'excuse et on propose une solution.",
        "en": "True, but curt: apologize and offer a solution.",
        "es": "Es cierto, pero seco: hay que disculparse y ofrecer una solución."}),
      ({"fr": "Oui, bien sûr! La chambre quatre cent douze.", "en": "Yes, of course! Room four-twelve.",
        "es": "¡Sí, claro! La habitación cuatrocientos doce."},
       {"fr": "L'hôtel est complet : on ne promet pas une chambre qu'on n'a pas.",
        "en": "The hotel is full: never promise a room you don't have.",
        "es": "El hotel está lleno: no se promete una habitación que no hay."})], False),
    ("r4", None,
     {"fr": "La chambre était bruyante. Je veux être remboursé au complet.",
      "en": "The room was noisy. I want a full refund.",
      "es": "La habitación era muy ruidosa. Quiero un reembolso completo."},
     [({"fr": "Je suis vraiment désolé pour le bruit. Je vais en parler au gérant tout de suite.",
        "en": "I'm very sorry about the noise. I'll speak to the manager about it right away.",
        "es": "Lamento mucho el ruido. Voy a consultarlo con el gerente ahora mismo."}, None),
      ({"fr": "Bien sûr, je vous rembourse tout le séjour.", "en": "Of course, I'll refund your whole stay.",
        "es": "Claro, le reembolso toda la estancia."},
       {"fr": "Un remboursement revient au gérant : on ne le promet jamais seul.",
        "en": "A refund is the manager's call: never promise it yourself.",
        "es": "Un reembolso le toca al gerente: nunca se promete solo."}),
      ({"fr": "Ce n'est pas mon problème.", "en": "That's not my problem.", "es": "No es mi problema."},
       {"fr": "On écoute et on s'excuse d'abord, puis on passe le relais.",
        "en": "Listen and apologize first, then hand it over.",
        "es": "Primero se escucha y se disculpa, luego se pasa al gerente."})], True),
    ("r5", None,
     {"fr": "Ma carte-clé ne fonctionne pas.", "en": "My key card doesn't work.",
      "es": "Mi tarjeta llave no funciona."},
     [({"fr": "Désolé! Je peux la voir? Je vais la réencoder.", "en": "I'm sorry! May I see it? I'll re-encode it for you.",
        "es": "¡Disculpe! ¿Me la permite? Se la vuelvo a codificar."}, None),
      ({"fr": "Appelez le gérant.", "en": "Please call the manager.", "es": "Llame al gerente."},
       {"fr": "Réencoder une clé, c'est votre geste : pas besoin du gérant.",
        "en": "Re-encoding a key is your job: no need for the manager.",
        "es": "Recodificar una llave le toca a usted: no hace falta el gerente."}),
      ({"fr": "L'ascenseur est à gauche.", "en": "The elevator is on the left.",
        "es": "El elevador está a la izquierda."},
       {"fr": "Ce n'est pas sa demande : sa clé ne marche pas.",
        "en": "That's not what she asked: her key doesn't work.",
        "es": "No es lo que pidió: su llave no funciona."})], False),
    ("r6", {"fr": "Au téléphone.", "en": "On the phone.", "es": "Por teléfono."},
     {"fr": "Est-ce que je peux changer ma réservation pour vendredi?",
      "en": "Can I change my reservation to Friday?",
      "es": "¿Puedo cambiar mi reservación para el viernes?"},
     [({"fr": "Bien sûr. Pouvez-vous me donner votre numéro de confirmation?",
        "en": "Of course. Could I have your confirmation number?",
        "es": "Claro. ¿Me da su número de confirmación?"}, None),
      ({"fr": "Je ne sais pas.", "en": "I don't know.", "es": "No sé."},
       {"fr": "On ne laisse pas un client sans réponse : on cherche sa réservation.",
        "en": "Don't leave a guest without an answer: look up the booking.",
        "es": "No se deja a un cliente sin respuesta: se busca su reservación."}),
      ({"fr": "Le déjeuner est servi de sept heures à dix heures.", "en": "Breakfast is from seven to ten.",
        "es": "El desayuno es de siete a diez."},
       {"fr": "Ce n'est pas sa question : il veut changer sa date.",
        "en": "That's not what he asked: he wants to change his date.",
        "es": "No es lo que preguntó: quiere cambiar su fecha."})], False),
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
    "x_pieges_c": {"fr": "Que veut dire ce mot? Attention aux faux amis.", "en": "What does this word mean? Watch out for false friends.", "es": "¿Qué quiere decir esta palabra? Cuidado con los falsos amigos."},
    "x_epeler": {"fr": "Épeler un nom", "en": "Spelling a name", "es": "Deletrear un nombre"},
    "x_epeler_c": {"fr": "Le client épelle son nom. Écrivez-le.", "en": "The guest spells their name. Type it.", "es": "El cliente deletrea su apellido. Escríbalo."},
    "x_nombres": {"fr": "Les nombres et les heures", "en": "Numbers and times", "es": "Números y horas"},
    "x_nombres_c": {"fr": "Écoutez, puis touchez ce que vous avez entendu.", "en": "Listen, then tap what you heard.", "es": "Escuche y toque lo que oyó."},
    "x_client": {"fr": "Ce que le client veut", "en": "What the guest wants", "es": "Lo que quiere el cliente"},
    "x_client_c": {"fr": "Le client parle vite. Choisissez le lit ET le nombre de nuits.", "en": "The guest talks fast. Choose the bed AND the number of nights.", "es": "El cliente habla rápido. Elija la cama Y el número de noches."},
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
    "lettre_juste": {"fr": "lettres justes", "en": "letters right", "es": "letras correctas"},
    "hors_regle": {"fr": "Promettre ce qui revient au gérant fait échouer au comptoir.",
                   "en": "Promising what belongs to the manager fails you at the desk.",
                   "es": "Prometer lo que le toca al gerente es un error grave en el mostrador."},
    "lit_ok": {"fr": "Le lit est juste, pas le nombre de nuits.", "en": "The bed is right, not the number of nights.", "es": "La cama es correcta, pero no el número de noches."},
    "nuits_ok": {"fr": "Les nuits sont justes, pas le lit.", "en": "The nights are right, not the bed.", "es": "Las noches son correctas, pero no la cama."},
    "rien_ok": {"fr": "Ni le lit ni les nuits : réécoutez.", "en": "Neither the bed nor the nights: listen again.", "es": "Ni la cama ni las noches: vuelva a escuchar."},
    "plusieurs": {"fr": "planches mêlées", "en": "all topics mixed", "es": "todos los temas"},
    "aucun_piege": {"fr": "Pas de piège pour cette paire de langues.", "en": "No traps for this language pair.", "es": "No hay trampas para este par de idiomas."},
}
